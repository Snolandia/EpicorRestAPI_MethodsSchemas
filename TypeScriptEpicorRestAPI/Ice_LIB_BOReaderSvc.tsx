import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.LIB.BOReaderSvc
// Description: Business Object Data Reader.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/$metadata", {
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
   Description: Call GetRows method
   OperationID: Get_GetRows
      @param serviceNamespace Desc: The fully resolved Service name   Required: True   Allow empty value : True
      @param whereClause Desc: WhereClause   Required: True   Allow empty value : True
      @param columnList Desc: List of Columns to return   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(serviceNamespace:string, whereClause:string, columnList:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof serviceNamespace!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "serviceNamespace=" + serviceNamespace
   }
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
   }
   if(typeof columnList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "columnList=" + columnList
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/GetRows" + params, {
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
   Description: Call GetList method
   OperationID: Get_GetList
      @param serviceNamespace Desc: The fully resolved Service name   Required: True   Allow empty value : True
      @param whereClause Desc: WhereClause   Required: True   Allow empty value : True
      @param columnList Desc: List of Columns to return   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(serviceNamespace:string, whereClause:string, columnList:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof serviceNamespace!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "serviceNamespace=" + serviceNamespace
   }
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
   }
   if(typeof columnList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "columnList=" + columnList
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/GetList" + params, {
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
   Summary: Invoke method GetCodeDescList
   Description: Gets a list of code and description pairs for a column.  First tries to find the list
using the ICE system code and then if not found will try the ERP system code.
   OperationID: Get_GetCodeDescList
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetCodeDescList(tableName:string, columnName:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof tableName!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tableName=" + tableName
   }
   if(typeof columnName!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "columnName=" + columnName
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/GetCodeDescList" + params, {
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
   Summary: Invoke method GetCodeDescriptionList
   Description: Get a list of code and description pairs for a column.
   OperationID: Get_GetCodeDescriptionList
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescriptionList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetCodeDescriptionList(systemCode:string, tableName:string, columnName:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof systemCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "systemCode=" + systemCode
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
   if(typeof columnName!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "columnName=" + columnName
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/GetCodeDescriptionList" + params, {
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
   Summary: Invoke method GetListWithPaging
   Description: Call GetList method
   OperationID: Get_GetListWithPaging
      @param serviceNamespace Desc: The fully resolved Service name   Required: True   Allow empty value : True
      @param whereClause Desc: WhereClause   Required: True   Allow empty value : True
   Required: True
      @param columnList Desc: List of Columns to return   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListWithPaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetListWithPaging(serviceNamespace:string, whereClause:string, pageSize:string, columnList:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof serviceNamespace!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "serviceNamespace=" + serviceNamespace
   }
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
   if(typeof columnList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "columnList=" + columnList
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/GetListWithPaging" + params, {
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
   Summary: Invoke method GetRowsWithPaging
   Description: Call GetRows method
   OperationID: Get_GetRowsWithPaging
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsWithPaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRowsWithPaging(serviceNamespace:string, whereClause:string, pageSize:string, columnList:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof serviceNamespace!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "serviceNamespace=" + serviceNamespace
   }
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
   if(typeof columnList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "columnList=" + columnList
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/GetRowsWithPaging" + params, {
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
   Summary: Invoke method GetRowsFirstTable
   Description: Method returns dataset with first data table only
   OperationID: Get_GetRowsFirstTable
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsFirstTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRowsFirstTable(serviceNamespace:string, whereClause:string, columnList:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof serviceNamespace!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "serviceNamespace=" + serviceNamespace
   }
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
   }
   if(typeof columnList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "columnList=" + columnList
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/GetRowsFirstTable" + params, {
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
   Summary: Invoke method GetRowsFirstTableWithPaging
   Description: Method returns dataset with first data table only with paging
   OperationID: Get_GetRowsFirstTableWithPaging
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsFirstTableWithPaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRowsFirstTableWithPaging(serviceNamespace:string, whereClause:string, pageSize:string, columnList:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof serviceNamespace!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "serviceNamespace=" + serviceNamespace
   }
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
   if(typeof columnList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "columnList=" + columnList
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/GetRowsFirstTableWithPaging" + params, {
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
   Summary: Invoke method InvokeAlternateSearchMethod
   Description: Invoke the Alternate Search Method by method name
   OperationID: Get_InvokeAlternateSearchMethod
      @param serviceNamespace Desc: The fully resolved Service name   Required: True   Allow empty value : True
      @param searchMethod Desc: The name of the Alternate Search method   Required: True   Allow empty value : True
      @param whereClause Desc: WhereClause   Required: True   Allow empty value : True
      @param columnList Desc: List of Columns to return   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/InvokeAlternateSearchMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_InvokeAlternateSearchMethod(serviceNamespace:string, searchMethod:string, whereClause:string, columnList:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof serviceNamespace!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "serviceNamespace=" + serviceNamespace
   }
   if(typeof searchMethod!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "searchMethod=" + searchMethod
   }
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
   }
   if(typeof columnList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "columnList=" + columnList
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/InvokeAlternateSearchMethod" + params, {
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
   Summary: Invoke method InvokeAlternateSearchMethodWithPaging
   Description: Invoke the Alternate Search Method by method name
   OperationID: Get_InvokeAlternateSearchMethodWithPaging
      @param serviceNamespace Desc: The fully resolved Service name   Required: True   Allow empty value : True
      @param searchMethod Desc: The name of the Alternate Search method   Required: True   Allow empty value : True
      @param whereClause Desc: WhereClause   Required: True   Allow empty value : True
      @param columnList Desc: List of Columns to return   Required: True   Allow empty value : True
      @param pageSize Desc: Number of records   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/InvokeAlternateSearchMethodWithPaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_InvokeAlternateSearchMethodWithPaging(serviceNamespace:string, searchMethod:string, whereClause:string, columnList:string, pageSize:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof serviceNamespace!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "serviceNamespace=" + serviceNamespace
   }
   if(typeof searchMethod!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "searchMethod=" + searchMethod
   }
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
   }
   if(typeof columnList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "columnList=" + columnList
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

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/InvokeAlternateSearchMethodWithPaging" + params, {
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
   Summary: Invoke method InvokeAlternateSearchMethodWithParams
   Description: Invoke the Alternate Search Method by method name
   OperationID: Get_InvokeAlternateSearchMethodWithParams
      @param serviceNamespace Desc: The fully resolved Service name   Required: True   Allow empty value : True
      @param searchMethod Desc: The name of the Alternate Search method   Required: True   Allow empty value : True
      @param executionParamsJson Desc: Parameters of alternative search method as json string   Required: True   Allow empty value : True
      @param columnList Desc: List of Columns to return   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/InvokeAlternateSearchMethodWithParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_InvokeAlternateSearchMethodWithParams(serviceNamespace:string, searchMethod:string, executionParamsJson:string, columnList:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof serviceNamespace!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "serviceNamespace=" + serviceNamespace
   }
   if(typeof searchMethod!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "searchMethod=" + searchMethod
   }
   if(typeof executionParamsJson!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "executionParamsJson=" + executionParamsJson
   }
   if(typeof columnList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "columnList=" + columnList
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/InvokeAlternateSearchMethodWithParams" + params, {
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
   Summary: Invoke method InvokeAlternateSearchMethodWithParamsWithPaging
   Description: Invoke the Alternate Search Method by method name
   OperationID: Get_InvokeAlternateSearchMethodWithParamsWithPaging
      @param serviceNamespace Desc: The fully resolved Service name   Required: True   Allow empty value : True
      @param searchMethod Desc: The name of the Alternate Search method   Required: True   Allow empty value : True
      @param executionParamsJson Desc: Parameters of alternative search method as json string   Required: True   Allow empty value : True
      @param columnList Desc: List of Columns to return   Required: True   Allow empty value : True
      @param pageSize Desc: Number of records   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/InvokeAlternateSearchMethodWithParamsWithPaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_InvokeAlternateSearchMethodWithParamsWithPaging(serviceNamespace:string, searchMethod:string, executionParamsJson:string, columnList:string, pageSize:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof serviceNamespace!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "serviceNamespace=" + serviceNamespace
   }
   if(typeof searchMethod!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "searchMethod=" + searchMethod
   }
   if(typeof executionParamsJson!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "executionParamsJson=" + executionParamsJson
   }
   if(typeof columnList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "columnList=" + columnList
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

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.BOReaderSvc/InvokeAlternateSearchMethodWithParamsWithPaging" + params, {
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
      @param tableName
      @param columnName
   */  
export interface GetCodeDescList_input{
   tableName:string,
   columnName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param systemCode
      @param tableName
      @param columnName
   */  
export interface GetCodeDescriptionList_input{
   systemCode:string,
   tableName:string,
   columnName:string,
}

export interface GetCodeDescriptionList_output{
   returnObj:string,
}

   /** Required : 
      @param serviceNamespace
      @param whereClause
      @param pageSize
      @param columnList
   */  
export interface GetListWithPaging_input{
      /**  The fully resolved Service name  */  
   serviceNamespace:string,
      /**  WhereClause  */  
   whereClause:string,
   pageSize:number,
      /**  List of Columns to return  */  
   columnList:string,
}

export interface GetListWithPaging_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param serviceNamespace
      @param whereClause
      @param columnList
   */  
export interface GetList_input{
      /**  The fully resolved Service name  */  
   serviceNamespace:string,
      /**  WhereClause  */  
   whereClause:string,
      /**  List of Columns to return  */  
   columnList:string,
}

export interface GetList_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param serviceNamespace
      @param whereClause
      @param pageSize
      @param columnList
   */  
export interface GetRowsFirstTableWithPaging_input{
   serviceNamespace:string,
   whereClause:string,
   pageSize:number,
   columnList:string,
}

export interface GetRowsFirstTableWithPaging_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param serviceNamespace
      @param whereClause
      @param columnList
   */  
export interface GetRowsFirstTable_input{
   serviceNamespace:string,
   whereClause:string,
   columnList:string,
}

export interface GetRowsFirstTable_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param serviceNamespace
      @param whereClause
      @param pageSize
      @param columnList
   */  
export interface GetRowsWithPaging_input{
   serviceNamespace:string,
   whereClause:string,
   pageSize:number,
   columnList:string,
}

export interface GetRowsWithPaging_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param serviceNamespace
      @param whereClause
      @param columnList
   */  
export interface GetRows_input{
      /**  The fully resolved Service name  */  
   serviceNamespace:string,
      /**  WhereClause  */  
   whereClause:string,
      /**  List of Columns to return  */  
   columnList:string,
}

export interface GetRows_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param serviceNamespace
      @param searchMethod
      @param whereClause
      @param columnList
      @param pageSize
   */  
export interface InvokeAlternateSearchMethodWithPaging_input{
      /**  The fully resolved Service name  */  
   serviceNamespace:string,
      /**  The name of the Alternate Search method  */  
   searchMethod:string,
      /**  WhereClause  */  
   whereClause:string,
      /**  List of Columns to return  */  
   columnList:string,
      /**  Number of records  */  
   pageSize:number,
}

export interface InvokeAlternateSearchMethodWithPaging_output{
      /**  The results of the Alternate Search method  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param serviceNamespace
      @param searchMethod
      @param executionParamsJson
      @param columnList
      @param pageSize
   */  
export interface InvokeAlternateSearchMethodWithParamsWithPaging_input{
      /**  The fully resolved Service name  */  
   serviceNamespace:string,
      /**  The name of the Alternate Search method  */  
   searchMethod:string,
      /**  Parameters of alternative search method as json string  */  
   executionParamsJson:string,
      /**  List of Columns to return  */  
   columnList:string,
      /**  Number of records  */  
   pageSize:number,
}

export interface InvokeAlternateSearchMethodWithParamsWithPaging_output{
      /**  The results of the Alternate Search method  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param serviceNamespace
      @param searchMethod
      @param executionParamsJson
      @param columnList
   */  
export interface InvokeAlternateSearchMethodWithParams_input{
      /**  The fully resolved Service name  */  
   serviceNamespace:string,
      /**  The name of the Alternate Search method  */  
   searchMethod:string,
      /**  Parameters of alternative search method as json string  */  
   executionParamsJson:string,
      /**  List of Columns to return  */  
   columnList:string,
}

export interface InvokeAlternateSearchMethodWithParams_output{
      /**  The results of the Alternate Search method  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param serviceNamespace
      @param searchMethod
      @param whereClause
      @param columnList
   */  
export interface InvokeAlternateSearchMethod_input{
      /**  The fully resolved Service name  */  
   serviceNamespace:string,
      /**  The name of the Alternate Search method  */  
   searchMethod:string,
      /**  WhereClause  */  
   whereClause:string,
      /**  List of Columns to return  */  
   columnList:string,
}

export interface InvokeAlternateSearchMethod_output{
      /**  The results of the Alternate Search method  */  
   returnObj:any,      //schema had no properties on an object.
}

