import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.IssueReturnSvc
// Description: Use this function to enter inventory issues or returns.
1) [Hold] Special public methods for DDSLs FromWhse and ToWhse as they have special conditions.
2) [ FYI ]This procedure gets called from lots of other program too -
im/ime20.w flmenu.w am/ame10.w am/ame20-am.p am/ame20-aw.p am/ame20-mm.p am/ame20-mw.p
Only am/ame20-dg.w uses MtlQueue functionality
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/$metadata", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.IssueReturnJobAsmblRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IssueReturnJobAsmblRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IssueReturnJobAsmblRow)
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
   Description: List of jobs that can be selected for Mass Issue.
   OperationID: Get_GetRows
      @param whereClauseJobHead Desc: Where condition without the where word   Required: True   Allow empty value : True
      @param whereClauseJobAsmbl Desc: Where condition without the where word   Required: True   Allow empty value : True
      @param pageSize Desc: # of records returned.  0 means all   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseJobHead:string, whereClauseJobAsmbl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseJobHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseJobHead=" + whereClauseJobHead
   }
   if(typeof whereClauseJobAsmbl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseJobAsmbl=" + whereClauseJobAsmbl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/GetRows" + params, {
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
   Summary: Invoke method _History07_08
   OperationID: _History07_08
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/_History07_08_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_History07_08(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/_History07_08", {
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
   Description: List of jobs that can be selected for Mass Issue.
   OperationID: Get_GetList
      @param whereClauseJobHead Desc: Where condition without the where word   Required: True   Allow empty value : True
      @param whereClauseJobAsmbl Desc: Where condition without the where word   Required: True   Allow empty value : True
      @param pageSize Desc: # of records returned.  0 means all   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(whereClauseJobHead:string, whereClauseJobAsmbl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseJobHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseJobHead=" + whereClauseJobHead
   }
   if(typeof whereClauseJobAsmbl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseJobAsmbl=" + whereClauseJobAsmbl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/GetList" + params, {
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
   Summary: Invoke method GetListJobs
   Description: List of jobs that can be selected for Mass Issue.
   OperationID: GetListJobs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListJobs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListJobs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListJobs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/GetListJobs", {
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
   Summary: Invoke method GetNewIssueReturn
   Description: Call this method to create a new Epicor.Mfg.BO.IssueReturnDataSet with
default values.
   OperationID: GetNewIssueReturn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewIssueReturn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewIssueReturn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewIssueReturn(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/GetNewIssueReturn", {
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
   Summary: Invoke method GetNewIssueReturnFromJob
   Description: Call this method to create a new Epicor.Mfg.BO.IssueReturnDataSet with
default values.
   OperationID: GetNewIssueReturnFromJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewIssueReturnFromJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewIssueReturnFromJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewIssueReturnFromJob(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/GetNewIssueReturnFromJob", {
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
   Summary: Invoke method GetNewIssueReturnToJob
   Description: Call this method to create a new Epicor.Mfg.BO.IssueReturnDataSet with
default values.
   OperationID: GetNewIssueReturnToJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewIssueReturnToJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewIssueReturnToJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewIssueReturnToJob(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/GetNewIssueReturnToJob", {
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
   Summary: Invoke method GetNewJobAsmblMultiple
   Description: This method creates multiple IssueReturnJobs rows using IssueReturnJobSearch dataset.
   OperationID: GetNewJobAsmblMultiple
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJobAsmblMultiple_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobAsmblMultiple_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewJobAsmblMultiple(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/GetNewJobAsmblMultiple", {
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
   Summary: Invoke method GetNewJobAsmblSearch
   Description: This method creates a new ttSelectedJobAsmbl row entry.
   OperationID: GetNewJobAsmblSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJobAsmblSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobAsmblSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewJobAsmblSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/GetNewJobAsmblSearch", {
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
   Summary: Invoke method GetNewPartMultiple
   Description: This method creates multiple IssueReturnJobs rows using IssueReturnJobSearch dataset.
   OperationID: GetNewPartMultiple
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartMultiple_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartMultiple_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartMultiple(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/GetNewPartMultiple", {
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
   Summary: Invoke method GetNewPartNum
   Description: Call this method to create a new Epicor.Mfg.BO.IssueReturnDataSet with
Part#.
   OperationID: GetNewPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/GetNewPartNum", {
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
   Summary: Invoke method GetNewPartSearch
   Description: This method creates a new ttSelectedParts row entry.
   OperationID: GetNewPartSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/GetNewPartSearch", {
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
   Summary: Invoke method GetRowsJobAssemblies
   Description: List of jobs/assemblies that can be selected for Mass Issue.
   OperationID: Get_GetRowsJobAssemblies
      @param whereClause Desc: Where condition without the where word   Required: True   Allow empty value : True
      @param pageSize Desc: # of records returned.  0 means all   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsJobAssemblies_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRowsJobAssemblies(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/GetRowsJobAssemblies" + params, {
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
   Summary: Invoke method GetRowsWIP
   Description: List of jobs/assemblies that can be selected for Move WIP and Move Material.
   OperationID: Get_GetRowsWIP
      @param whereClause Desc: Where condition without the where word   Required: True   Allow empty value : True
      @param pageSize Desc: # of records returned.   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsWIP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRowsWIP(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/GetRowsWIP" + params, {
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
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Gets parameters required for launching Select Serial Numbers
   OperationID: GetSelectSerialNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectSerialNumbersParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/GetSelectSerialNumbersParams", {
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
   Summary: Invoke method GetUnissuedQty
   Description: Call this method to set the Qty to the remaining unissued amount.
   OperationID: GetUnissuedQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUnissuedQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUnissuedQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetUnissuedQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/GetUnissuedQty", {
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
   Summary: Invoke method GetUnpickSettings
   Description: Sets ttIssueReturn fields for Unpick
   OperationID: GetUnpickSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUnpickSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUnpickSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetUnpickSettings(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/GetUnpickSettings", {
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
   Summary: Invoke method IsValidAssembly
   Description: Validate if an assembly is valid for a job. if not returns false,
otherwise returns true.
   OperationID: IsValidAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsValidAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsValidAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsValidAssembly(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/IsValidAssembly", {
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
   Summary: Invoke method OnChangeFromPCID
   Description: Validate if FromPCID change is valid
otherwise returns true.
   OperationID: OnChangeFromPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFromPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFromPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFromPCID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/OnChangeFromPCID", {
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
   Summary: Invoke method JobExists
   Description: Check JobNum and return JobRelease and JobClosed
   OperationID: JobExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/JobExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/JobExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_JobExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/JobExists", {
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
   Summary: Invoke method OnChangeToPCID
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.ToPCID changes (this is for ToPCID, for FromPCID use OnChangeFromPCID method).
   OperationID: OnChangeToPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeToPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeToPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeToPCID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/OnChangeToPCID", {
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
   Summary: Invoke method OnChangeFromAssemblySeq
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.FromAssemblySeq changes.
   OperationID: OnChangeFromAssemblySeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFromAssemblySeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFromAssemblySeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFromAssemblySeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/OnChangeFromAssemblySeq", {
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
   Summary: Invoke method OnChangeFromBinNum
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.FromBinNum changes.
   OperationID: OnChangeFromBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFromBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFromBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFromBinNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/OnChangeFromBinNum", {
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
   Summary: Invoke method OnChangeFromJobNum
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.FromJobNum changes.
   OperationID: OnChangeFromJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFromJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFromJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFromJobNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/OnChangeFromJobNum", {
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
   Summary: Invoke method OnChangeFromJobSeq
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.FromJobNum changes.
   OperationID: OnChangeFromJobSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFromJobSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFromJobSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFromJobSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/OnChangeFromJobSeq", {
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
   Summary: Invoke method OnChangeFromWarehouse
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.PartNum changes.
   OperationID: OnChangeFromWarehouse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFromWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFromWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFromWarehouse(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/OnChangeFromWarehouse", {
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
   Summary: Invoke method ChangeFromWarehouseDefaultBin
   Description: Call when from warehouse changes.  This method will also reset the bin to the default value for the warehouse
   OperationID: ChangeFromWarehouseDefaultBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFromWarehouseDefaultBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFromWarehouseDefaultBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFromWarehouseDefaultBin(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/ChangeFromWarehouseDefaultBin", {
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
   Summary: Invoke method OnChangeLotNum
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.LotNum changes.
   OperationID: OnChangeLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeLotNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/OnChangeLotNum", {
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
   Summary: Invoke method OnChangePartNum
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.PartNum changes.
   OperationID: OnChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/OnChangePartNum", {
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
   Summary: Invoke method OnChangeToAssemblySeq
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.ToAssemblySeq changes.
   OperationID: OnChangeToAssemblySeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeToAssemblySeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeToAssemblySeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeToAssemblySeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/OnChangeToAssemblySeq", {
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
   Summary: Invoke method OnChangeToJobNum
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.ToJobNum changes.
   OperationID: OnChangeToJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeToJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeToJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeToJobNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/OnChangeToJobNum", {
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
   Summary: Invoke method OnChangeToJobSeq
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.ToJobSeq changes.
   OperationID: OnChangeToJobSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeToJobSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeToJobSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeToJobSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/OnChangeToJobSeq", {
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
   Summary: Invoke method OnChangeToWarehouse
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.PartNum changes.
   OperationID: OnChangeToWarehouse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeToWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeToWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeToWarehouse(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/OnChangeToWarehouse", {
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
   Summary: Invoke method ChangeToWarehouseDefaultBin
   Description: Call when to warehouse changes.  This method will also reset the bin to the default value for the warehouse
   OperationID: ChangeToWarehouseDefaultBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeToWarehouseDefaultBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeToWarehouseDefaultBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeToWarehouseDefaultBin(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/ChangeToWarehouseDefaultBin", {
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
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new tran qty
   OperationID: OnChangingNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingNumberOfPieces(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/OnChangingNumberOfPieces", {
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
   Summary: Invoke method OnChangingAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangingAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingAttributeSet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/OnChangingAttributeSet", {
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
   Summary: Invoke method OnChangingAttributeSetAdjustments
   Description: Call this method when the attribute set changes for adjustment transactions (Issue Misc, Return Misc) to maintain inventory tracking
   OperationID: OnChangingAttributeSetAdjustments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSetAdjustments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSetAdjustments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingAttributeSetAdjustments(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/OnChangingAttributeSetAdjustments", {
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
   Summary: Invoke method OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingRevisionNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/OnChangingRevisionNum", {
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
   Summary: Invoke method OnChangingRevisionNumAdjustments
   Description: Call this method when the Revision changes for adjustment transactions (Issue Misc, Return Misc) to maintain inventory tracking
   OperationID: OnChangingRevisionNumAdjustments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNumAdjustments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNumAdjustments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingRevisionNumAdjustments(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/OnChangingRevisionNumAdjustments", {
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
   Summary: Invoke method OnChangeTranQty
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.TranQty changes.
This method performs validation on TranQty and sets the Issued Complete flag.
   OperationID: OnChangeTranQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTranQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTranQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTranQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/OnChangeTranQty", {
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
   Summary: Invoke method OnChangeUM
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.UM changes.
   OperationID: OnChangeUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeUM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/OnChangeUM", {
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
   Summary: Invoke method OnChangeASTUom
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.FromBinNum is changing.
   OperationID: OnChangeASTUom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeASTUom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeASTUom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeASTUom(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/OnChangeASTUom", {
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
   Summary: Invoke method OnChangingFromBinNum
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.FromBinNum is changing.
   OperationID: OnChangingFromBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingFromBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingFromBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingFromBinNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/OnChangingFromBinNum", {
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
   Summary: Invoke method OnChangingJobSeq
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSetjobseq (either to or from is changing)
   OperationID: OnChangingJobSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingJobSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingJobSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingJobSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/OnChangingJobSeq", {
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
   Summary: Invoke method OnChangingToJobSeq
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.ToJobSeq is changing.
   OperationID: OnChangingToJobSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingToJobSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingToJobSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingToJobSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/OnChangingToJobSeq", {
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
   Summary: Invoke method PerformMaterialMovement
   Description: Perform Material Movement.
   OperationID: PerformMaterialMovement
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PerformMaterialMovement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PerformMaterialMovement_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PerformMaterialMovement(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/PerformMaterialMovement", {
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
   Summary: Invoke method PerformMaterialMovement2
   Description: Perform Material Movement.
   OperationID: PerformMaterialMovement2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PerformMaterialMovement2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PerformMaterialMovement2_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PerformMaterialMovement2(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/PerformMaterialMovement2", {
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
   Summary: Invoke method PerformMaterialMovementWithLegalNum
   Description: Perform Material Movement.
   OperationID: PerformMaterialMovementWithLegalNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PerformMaterialMovementWithLegalNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PerformMaterialMovementWithLegalNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PerformMaterialMovementWithLegalNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/PerformMaterialMovementWithLegalNum", {
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
   Summary: Invoke method MassUnpickByPCID
   Description: Performs a mass unpick by PCID - this handles the actual inventory movement - everything else is handled by UnpickTransaction BO
   OperationID: MassUnpickByPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MassUnpickByPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassUnpickByPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MassUnpickByPCID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/MassUnpickByPCID", {
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
   Summary: Invoke method GenerateDynamicPCID
   Description: Generate a dynamic PCID
   OperationID: GenerateDynamicPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateDynamicPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateDynamicPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateDynamicPCID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/GenerateDynamicPCID", {
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
   Summary: Invoke method SuppressPrintMessages
   Description: Returns if the employee has the 'Suppress Print Messages' flag on
   OperationID: SuppressPrintMessages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SuppressPrintMessages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SuppressPrintMessages_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SuppressPrintMessages(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/SuppressPrintMessages", {
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
   Summary: Invoke method IsAutoPrintSetup
   Description: To verify if autoprint is setup
   OperationID: IsAutoPrintSetup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsAutoPrintSetup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsAutoPrintSetup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsAutoPrintSetup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/IsAutoPrintSetup", {
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
   Summary: Invoke method ValidatePkgControlID
   Description: Validates a pkg control ID code
   OperationID: ValidatePkgControlID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePkgControlID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePkgControlID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePkgControlID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/ValidatePkgControlID", {
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
   Summary: Invoke method PreGetNewIssueReturn
   Description: This method will check, depending on the Tran Type, if the available quantity
has been reduced before the creation of the issue return.
   OperationID: PreGetNewIssueReturn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreGetNewIssueReturn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreGetNewIssueReturn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreGetNewIssueReturn(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/PreGetNewIssueReturn", {
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
   Summary: Invoke method PrePerformMaterialMovement
   Description: This method performs multiple functions:
It will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
            
It will also auto populate ttSelectedSerialNumbers table under some conditions for eligible types of IR transactions
   OperationID: PrePerformMaterialMovement
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePerformMaterialMovement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePerformMaterialMovement_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrePerformMaterialMovement(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/PrePerformMaterialMovement", {
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
   Summary: Invoke method SetQuantity
   Description: Purpose:  Gets the PartWip
sets the "From quantity" (ttIssueReturn.QtyPrevioulsyIssued)
and "TO Quantity" (ttIssueReturn.TranQty) to the PartWip.
Notes:This is called when the from fields are changed. (FromJobNum, FromAssemblySeq, FromJobSeq, FromWarehouseCode, FromBinNum)
Currently this is only for a WIP-WIP transaction
Created as part of scr57730
   OperationID: SetQuantity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetQuantity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetQuantity(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/SetQuantity", {
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
   Summary: Invoke method ValidateSN
   Description: Validates that a single serial number is valid for this transaction
   OperationID: ValidateSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSN(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/ValidateSN", {
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
   Summary: Invoke method validateToBinNum
   Description: Validates To Location, Bin Number exists
   OperationID: validateToBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/validateToBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/validateToBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_validateToBinNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/validateToBinNum", {
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
   Summary: Invoke method GetInventoryQtyAdjBrw
   Description: Gets the default values for the browse section of the adjustment screen
   OperationID: GetInventoryQtyAdjBrw
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInventoryQtyAdjBrw_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryQtyAdjBrw_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInventoryQtyAdjBrw(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/GetInventoryQtyAdjBrw", {
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
   Summary: Invoke method GetInventoryQtyAdjBrwInventoryTracking
   Description: Gets the default values for the browse section of the adjustment screen
   OperationID: GetInventoryQtyAdjBrwInventoryTracking
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInventoryQtyAdjBrwInventoryTracking_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryQtyAdjBrwInventoryTracking_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInventoryQtyAdjBrwInventoryTracking(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/GetInventoryQtyAdjBrwInventoryTracking", {
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
   Summary: Invoke method GetInventoryQtyAdjBrwForWeb
   Description: Gets the default values for the browse section of the adjustment screen
Copy of the same method of BO InventoryQtyAdj
Specific for web (client) use.
   OperationID: GetInventoryQtyAdjBrwForWeb
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInventoryQtyAdjBrwForWeb_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryQtyAdjBrwForWeb_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInventoryQtyAdjBrwForWeb(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/GetInventoryQtyAdjBrwForWeb", {
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
   Summary: Invoke method GetPartXRefInfo
   Description: This method defaults PartAdvisor fields when the PartNum field changes
   OperationID: GetPartXRefInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartXRefInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/GetPartXRefInfo", {
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
   Summary: Invoke method ValidUOM
   OperationID: ValidUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidUOM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/ValidUOM", {
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
   Summary: Invoke method GetAvailTranDocTypes
   Description: Method to call to get available tran doc types.
   OperationID: GetAvailTranDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailTranDocTypes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/GetAvailTranDocTypes", {
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
   Summary: Invoke method NegativeInventoryTestTran
   OperationID: NegativeInventoryTestTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/NegativeInventoryTestTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NegativeInventoryTestTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NegativeInventoryTestTran(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/NegativeInventoryTestTran", {
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
   Summary: Invoke method NegativeInventoryTest
   OperationID: NegativeInventoryTest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/NegativeInventoryTest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NegativeInventoryTest_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NegativeInventoryTest(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/NegativeInventoryTest", {
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
   Summary: Invoke method MasterInventoryBinTests
   Description: Methods to check Negative Inventory and Contract bin.
Planning Contract Bin Actions.
   OperationID: MasterInventoryBinTests
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MasterInventoryBinTests_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MasterInventoryBinTests_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MasterInventoryBinTests(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/MasterInventoryBinTests", {
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
   Summary: Invoke method checkWhseBin
   Description: Method to check values for whsebin.
   OperationID: checkWhseBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/checkWhseBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/checkWhseBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_checkWhseBin(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/checkWhseBin", {
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
   Summary: Invoke method FillForeignFields
   OperationID: FillForeignFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FillForeignFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FillForeignFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FillForeignFields(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/FillForeignFields", {
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
   Summary: Invoke method CheckPackageCodeAllocNegQty
   OperationID: CheckPackageCodeAllocNegQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPackageCodeAllocNegQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackageCodeAllocNegQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPackageCodeAllocNegQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/CheckPackageCodeAllocNegQty", {
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
   Summary: Invoke method AreSNumsAllocated
   Description: Returns true if there are any PartAllocSerial records for the company/part, consistent with InvTransfer.
   OperationID: AreSNumsAllocated
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AreSNumsAllocated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AreSNumsAllocated_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AreSNumsAllocated(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/AreSNumsAllocated", {
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
   Summary: Invoke method GetToBinNumWhereClause
   Description: Returns a whereclause for To Bin Num searches
   OperationID: GetToBinNumWhereClause
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetToBinNumWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetToBinNumWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetToBinNumWhereClause(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/GetToBinNumWhereClause", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IssueReturnJobAsmblRow{
   "odatametadata":string,
   "value":Erp_Tablesets_IssueReturnJobAsmblRow[],
}

export interface Erp_Tablesets_IssueReturnJobAsmblRow{
   "Company":string,
   "JobNum":string,
   "AssemblySeq":number,
   "PartNum":string,
   "Description":string,
   "JobHeadPartNum":string,
   "JobHeadPartDescription":string,
   "EquipID":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param companyID
      @param partNum
   */  
export interface AreSNumsAllocated_input{
   companyID:string,
   partNum:string,
}

export interface AreSNumsAllocated_output{
   returnObj:boolean,
}

   /** Required : 
      @param ds
      @param pCallProcess
   */  
export interface ChangeFromWarehouseDefaultBin_input{
   ds:Erp_Tablesets_IssueReturnTableset[],
   pCallProcess:string,
}

export interface ChangeFromWarehouseDefaultBin_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param ds
      @param pCallProcess
   */  
export interface ChangeToWarehouseDefaultBin_input{
   ds:Erp_Tablesets_IssueReturnTableset[],
   pCallProcess:string,
}

export interface ChangeToWarehouseDefaultBin_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param ipcalledFrom
      @param ipPCID
      @param ipQty
   */  
export interface CheckPackageCodeAllocNegQty_input{
   ipcalledFrom:string,
   ipPCID:string,
   ipQty:number,
}

export interface CheckPackageCodeAllocNegQty_output{
parameters : {
      /**  output parameters  */  
   opWarning:string,
   opAction:string,
   opAllocWarning:string,
   opAllocAction:string,
}
}

export interface Erp_Tablesets_InventoryQtyAdjBrwRow{
      /**  Company  */  
   Company:string,
      /**  Bin number  */  
   BinNum:string,
      /**  On hand quantity  */  
   OnHandQty:number,
      /**  Non nettable flag  */  
   NonNettable:boolean,
      /**  Ware house code  */  
   WareHseCode:string,
      /**  Lot number  */  
   LotNum:string,
      /**  WareHouse Bin description.  */  
   WhseBinDesc:string,
   StkUOMCode:string,
   StkUOMDesc:string,
      /**  The PartBin.OnHandQty expressed in Part Base UOM  */  
   BaseOnHandQty:number,
      /**  Unit of Measure to qualifiy BaseOnHandQty. This is the Part Base UOM.  */  
   BaseOnHandUOM:string,
   BinType:string,
      /**  Translated description string of Bin Type  */  
   BinTypeDesc:string,
      /**  Determines if the Part Bin has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  The parent PCID for the bin or child PCID record.  */  
   PCID:string,
      /**  PartNum for the bin record.  */  
   PartNum:string,
      /**  The PCID of the child in the parent PCID.  */  
   ItemPCID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
   PartAttrClassID:string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   NumberOfPieces:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InventoryQtyAdjBrwTableset{
   InventoryQtyAdjBrw:Erp_Tablesets_InventoryQtyAdjBrwRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_IssueReturnJobAsmblRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   PartNum:string,
   Description:string,
   JobHeadPartNum:string,
   JobHeadPartDescription:string,
   EquipID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IssueReturnJobAsmblTableset{
   IssueReturnJobAsmbl:Erp_Tablesets_IssueReturnJobAsmblRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_IssueReturnJobListTableset{
   JobHead:Erp_Tablesets_JobHeadRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_IssueReturnRow{
      /**  Company identifier  */  
   Company:string,
      /**  Transaction Date  */  
   TranDate:string,
      /**  Part number  */  
   PartNum:string,
      /**  Transaction Quantity  */  
   TranQty:number,
      /**  Dimension code  */  
   DimCode:string,
      /**  Lot number  */  
   LotNum:string,
      /**  Reason code  */  
   ReasonCode:string,
      /**  Order number  */  
   OrderNum:number,
      /**  Line #  */  
   OrderLine:number,
      /**  Release #  */  
   OrderRel:number,
      /**  From Job #  */  
   FromJobNum:string,
      /**  From Assembly Seq  */  
   FromAssemblySeq:number,
      /**  From Job sequence  */  
   FromJobSeq:number,
      /**  From Warehouse code  */  
   FromWarehouseCode:string,
      /**  From Bin number  */  
   FromBinNum:string,
      /**  From Job Part num  */  
   FromJobPartNum:string,
      /**  From Assembly Part num  */  
   FromAssemblyPartNum:string,
      /**  From Job sequence Part num  */  
   FromJobSeqPartNum:string,
      /**  From Job Part Desc  */  
   FromJobPartDesc:string,
      /**  From Assembly Part Desc  */  
   FromAssemblyPartDesc:string,
      /**  From Job sequence Part Desc  */  
   FromJobSeqPartDesc:string,
      /**  On hand quantity  */  
   OnHandQty:number,
      /**  Quantity required  */  
   QtyRequired:number,
      /**  Quantity previously required  */  
   QtyPreviouslyIssued:number,
      /**  Issued Complete  */  
   IssuedComplete:boolean,
      /**  To Job #  */  
   ToJobNum:string,
      /**  To Assembly Seq  */  
   ToAssemblySeq:number,
      /**  To Job sequence  */  
   ToJobSeq:number,
      /**  To Warehouse code  */  
   ToWarehouseCode:string,
      /**  To Bin number  */  
   ToBinNum:string,
      /**  To Job Part num  */  
   ToJobPartNum:string,
      /**  To Assembly Part num  */  
   ToAssemblyPartNum:string,
      /**  To Job sequence Part num  */  
   ToJobSeqPartNum:string,
      /**  To Job Part Desc  */  
   ToJobPartDesc:string,
      /**  To Assembly Part Desc  */  
   ToAssemblyPartDesc:string,
      /**  To Job sequence part desc  */  
   ToJobSeqPartDesc:string,
   ReasonType:string,
   FromJobPartDescription:string,
   FromAssemblyPartDescription:string,
   FromJobSeqPartDescription:string,
   ToJobPartDescription:string,
   ToAssemblyPartDescription:string,
   ToJobSeqPartDescription:string,
   TranReference:string,
   SerialNoQty:number,
   MtlQueueRowId:string,
   TranType:string,
   DimConvFactor:number,
   InvAdjReason:string,
   DUM:string,
   UM:string,
   FromJobPlant:string,
   ToJobPlant:string,
      /**  Dummy key field.  It is the primary key of the dataset  */  
   DummyKeyField:string,
      /**  The value displayed in the JobAsmbl tree  */  
   TreeDisplay:string,
   EnableToFields:boolean,
   EnableFromFields:boolean,
   RequirementUOM:string,
   RequirementQty:number,
      /**  This external field would be used to indicate for the BL whether serial numbers should be validated/updated and indicated for the various UIs whether the serial number button will be enabled.  */  
   EnableSN:boolean,
      /**  The plant id of the plant that is controlling the serial tracking options, set depending on the IssueReturn UI  */  
   SerialControlPlant:string,
      /**  Indicates whether the plant in SerialControlPlant field is the from plant. Yes = is the from plant, No= is the to plant.  */  
   SerialControlPlantIsFromPlt:boolean,
      /**  The process ID for the UI process that has created this IssueReturn record, only used by serial tracking logic  */  
   ProcessID:string,
      /**  If SerialControlPlantIsFromPlt = yes, then this field contains the to plant for the issue or return; it will be blank for Misc Issue  */  
   SerialControlPlant2:string,
      /**  It is true when Multi UOM is tracked for the PartNum  */  
   TrackDimension:boolean,
      /**  Unit of measure of the On Hand Quantity displayed  */  
   OnHandUM:string,
      /**  Transaction Document Type ID  */  
   TranDocTypeID:string,
   TFOrdNum:string,
   TFOrdLine:number,
   ReassignSNAsm:boolean,
   ReplenishDecreased:boolean,
      /**  Sets whether generate button in process material queue screen is enabled.  */  
   EnablePCIDGen:boolean,
      /**  Sets whether print button in process material queue screen is enabled.  */  
   EnablePCIDPrint:boolean,
      /**  Current Plant ID - external - used for filtering combos  */  
   Plant:string,
   PkgControlID:string,
      /**  PCID to pick from.  */  
   FromPCID:string,
      /**  PCID to pick to.  */  
   ToPCID:string,
   ToPCIDItemSeq:number,
   FromPCIDItemSeq:number,
      /**  Disable PCID related fields  */  
   DisablePCIDRelatedFields:boolean,
      /**  Flag in PlantConfCtrl that enables Package Control functionality.  */  
   PlantConfCtrlEnablePackageControl:boolean,
   EnableToPCID:boolean,
   EnableFromPCID:boolean,
      /**  Indicates if a PkgControlHeader record was deleted during the Unpick Transaction.  */  
   PkgControlHeaderDeleted:boolean,
   EpicorFSA:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
   EnableAttributeSetSearch:boolean,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
      /**  Revision related to this transaction.  */  
   RevisionNum:string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   FromJobRevisionNum:string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   FromAssemblyRevisionNum:string,
   PartWipSysRowID:string,
   SysRowID:string,
   DimCodeDimCodeDescription:string,
   FromBinNumDescription:string,
   FromWarehouseCodeDescription:string,
   LotNumPartLotDescription:string,
   PartTrackInventoryAttributes:boolean,
   PartAttrClassID:string,
   PartTrackLots:boolean,
   PartTrackSerialNum:boolean,
   PartTrackDimension:boolean,
   PartSalesUM:string,
   PartIUM:string,
   PartPricePerCode:string,
   PartSellingFactor:number,
   PartPartDescription:string,
   PartTrackInventoryByRevision:boolean,
   ReasonCodeDescription:string,
   ToBinNumDescription:string,
   ToWarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IssueReturnTableset{
   IssueReturn:Erp_Tablesets_IssueReturnRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_JobHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  */  
   JobClosed:boolean,
      /**  Date the Job was closed.  Defaults as the system but can be overridden.  */  
   ClosedDate:string,
      /**  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  */  
   JobComplete:boolean,
      /**  The date that production was completed for this Job.  Maintained via Job Completion Processing.  */  
   JobCompletionDate:string,
      /**  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  */  
   JobEngineered:boolean,
      /**   Optional Job check off number 1.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff1:boolean,
      /**   Optional Job check off number 2.  The label for this field is found in JCSyst. If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff2:boolean,
      /**   Optional Job check off number 3.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff3:boolean,
      /**  Optional Job check off number 4.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff4:boolean,
      /**  Optional Job check off number 5.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff5:boolean,
      /**  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  */  
   JobReleased:boolean,
      /**  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  */  
   JobHeld:boolean,
      /**  Scheduling Status Control (R-Required, P-Pending, A-Active, C-Complete).  NOT CURRENTLY IMPLEMENTED.  */  
   SchedStatus:string,
      /**  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  */  
   JobNum:string,
      /**   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  */  
   PartNum:string,
      /**  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  */  
   DrawNum:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   PartDescription:string,
      /**  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  */  
   ProdQty:number,
      /**  The unit of measure for the job.  Defaulted from Part.IUM.  */  
   IUM:string,
      /**  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   StartDate:string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   StartHour:number,
      /**  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  */  
   DueDate:string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  */  
   DueHour:number,
      /**  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  */  
   ReqDueDate:string,
      /**  An optional user defined code.  This will be used for report selections and views of job headers.  */  
   JobCode:string,
      /**  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  */  
   QuoteNum:number,
      /**  Contains the quote line number reference. (see QuoteNum )  */  
   QuoteLine:number,
      /**  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  UserChar1  */  
   UserChar1:string,
      /**  UserChar2  */  
   UserChar2:string,
      /**  UserChar3  */  
   UserChar3:string,
      /**  UserChar4  */  
   UserChar4:string,
      /**  UserDate1  */  
   UserDate1:string,
      /**  UserDate2  */  
   UserDate2:string,
      /**  UserDate3  */  
   UserDate3:string,
      /**  UserDate4  */  
   UserDate4:string,
      /**  UserDecimal1  */  
   UserDecimal1:number,
      /**  UserDecimal2  */  
   UserDecimal2:number,
      /**  UserInteger1  */  
   UserInteger1:number,
      /**  UserInteger2  */  
   UserInteger2:number,
      /**  Editor widget for Job header comments.  */  
   CommentText:string,
      /**  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  */  
   ExpenseCode:string,
      /**  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  */  
   InCopyList:boolean,
      /**   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  */  
   WIName:string,
      /**  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   WIStartDate:string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   WIStartHour:number,
      /**  Scheduled "What If" finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  */  
   WIDueDate:string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  */  
   WIDueHour:number,
      /**   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  */  
   Candidate:boolean,
      /**  Scheduling Code.  SchedCode references a record in the SchedPri table.  */  
   SchedCode:string,
      /**  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  */  
   SchedLocked:boolean,
      /**  Associates the JobHead with a project in the Project table.  This can be blank.  */  
   ProjectID:string,
      /**  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  */  
   WIPCleared:boolean,
      /**  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  */  
   JobFirm:boolean,
      /**  A LIST-DELIM delimited list of people.  */  
   PersonList:string,
      /**   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  */  
   PersonID:string,
      /**  Production Team for the Job.  Associates the JobHead with a ProdTeam.  */  
   ProdTeamID:string,
      /**   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  */  
   QtyCompleted:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  */  
   DatePurged:string,
      /**  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  */  
   TravelerReadyToPrint:boolean,
      /**  The last date the job traveler was mass printed.  */  
   TravelerLastPrinted:string,
      /**  Indicates if the Status can be printed. Print functions are not available if this is = No.  */  
   StatusReadyToPrint:boolean,
      /**  The last date the job status was mass printed.  */  
   StatusLastPrinted:string,
      /**  The Service Call number that this Job is linked to.  */  
   CallNum:number,
      /**  The Service Call Line that this Job is linked to.  */  
   CallLine:number,
      /**  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  */  
   JobType:string,
      /**  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  */  
   RestoreFlag:string,
      /**  Project Phase ID  */  
   PhaseID:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  Indicates that the quantity on this job is locked  */  
   LockQty:boolean,
      /**  The help desk case that created this job.  */  
   HDCaseNum:number,
      /**   Values: S(Sequential) or C(Concurrent).
Defaults as S. Must have Advanced Production License to change. Controls how the operations and material requirements are developed. Concurrent jobs are used where the production time is based on the number of machine operations performed and not on the number of parts created. For example, a stamping operation where each cycle of the machine stamps out x number of parts. A further extension of this is that the operation can yield multiple different parts from each cycle of the machine.  Identification of these parts and there associated PPO (parts per operation) is define in the JobPart table.  */  
   ProcessMode:string,
      /**  The planned date when the job needs to be actioned by the production department to make sure that the job is ready on the planned completion date.  */  
   PlannedActionDate:string,
      /**  The date that the job needs to be ready for the warehouse to kit to make sure that it is ready for the job start date.  */  
   PlannedKitDate:string,
      /**  The task ID that is returned from Microsoft Project.  */  
   MSPTaskID:string,
      /**  This is the Microsoft Project predecessor. This needs to be a text field as Microsoft Project may pass back an alpha numeric string.  */  
   MSPPredecessor:string,
      /**  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   UserMapData:string,
      /**  Flag to indicate whether operations for this job will use the production yield features set up in OpMaster for the operation code. Defaulted from Site.ProductionYield  */  
   ProductionYield:boolean,
      /**  This field will be set to the value of the JobHead.ProdQty at the time the JobHead.Engineered flag is set to true.  */  
   OrigProdQty:number,
      /**  This field is used to indicate whether the original quantities should be reset in the job header and its assemblies at JobHead update if JobHead.JobEngineered has been changed from false to true. Generally the orig qtys will be reset, unless this flag is set to true because the user was asked if they wanted to reset the orig qtys and they answered yes.  */  
   PreserveOrigQtys:boolean,
      /**  If set to yes then exclude this job from the Job Auto-Completion process. Not directly maintainable.  */  
   NoAutoCompletion:boolean,
      /**  No Auto Closing. If set to yes then exclude this job from the Job Auto-Closing process.  */  
   NoAutoClosing:boolean,
      /**  The user that created this Job.  */  
   CreatedBy:string,
      /**  The date that this Job was created.  */  
   CreateDate:string,
      /**  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  */  
   WhseAllocFlag:boolean,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   OwnershipStatus:string,
      /**  Holds the internal object id of PDM parts.  */  
   PDMObjID:string,
      /**  This field is used to store a code that represents the external system that the Job is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  */  
   ExportRequested:string,
      /**  Flag to indicate how to split the manufacturing cost elements when a manufactured material is issued to the job.  If flag is set to true, the cost of the issued material will be split into individual manufacturing cost elements. If set to false, the cost of the issued material is added to the manufacturing material cost element only.  This is defaulted from the JCSyst.SplitMfgCostElements and is not user maintainable.  */  
   SplitMfgCostElements:boolean,
      /**  Cross Reference Part Num. Used for alternate serial mask support.  */  
   XRefPartNum:string,
      /**   Cross Reference Part Type. Used for alternate serial mask support.

I=Internal Cross Reference / C = Customer Part  */  
   XRefPartType:string,
      /**  Customer Number XRefPartNum is related to if it is a customer part. Used for alternate serial number mask support.  */  
   XRefCustNum:number,
      /**  Base Part Number. Used in the configurator to identify the configurator part Number.  */  
   BasePartNum:string,
      /**  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  */  
   BaseRevisionNum:string,
      /**  Indicates if the job was rough cut scheduled.  */  
   RoughCutScheduled:boolean,
      /**   The ID of the Equipment that this "Maintenance Job" is for.
Foreign key component to Equip table.  */  
   EquipID:string,
      /**   Preventive Maintenance Plan Number that this "Maintenance Job" is for. Foreign key component to EquipPlan table.
Note: A Maintenance Job does not have to be for a Preventive Maintenance plan, in which case this is zero.
If time based plan, then the closing process will update the EquipPlan.NextDate. Therefore, the Job must know the EquipID and PlanNum in order to do this.  */  
   PlanNum:number,
      /**  Maintenance Job Priority. Valid values: H - High, M - Medium, L - Low.  M is default or if created from a Maint Request then MaintReq.Priority is used as default.  */  
   MaintPriority:string,
      /**  Internal field indicating this job was created by a job split.  Assigned true when a job has been split due to start minimum lot size quantity processing.  */  
   SplitJob:boolean,
      /**  Indicates the type of prefix which is used for create jobs in MRP  */  
   NumberSource:boolean,
      /**  The Meter Reading value entered at time of Job Closing.  */  
   CloseMeterReading:number,
      /**  Maintenance Issue Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  */  
   IssueTopicID1:string,
      /**  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  */  
   IssueTopicID2:string,
      /**  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  */  
   IssueTopicID3:string,
      /**  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  */  
   IssueTopicID4:string,
      /**  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  */  
   IssueTopicID5:string,
      /**  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  */  
   IssueTopicID6:string,
      /**  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  */  
   IssueTopicID7:string,
      /**  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  */  
   IssueTopicID8:string,
      /**  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  */  
   IssueTopicID9:string,
      /**  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  */  
   IssueTopicID10:string,
      /**  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  */  
   IssueTopics:string,
      /**  Maintenance Resolution Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintRes = Yes  */  
   ResTopicID1:string,
      /**  Maintenance Resolution Topic 2. A sub-topic of ResTopicID1.  */  
   ResTopicID2:string,
      /**  Maintenace  Resolution Topic 3. A sub-topic of ResTopicID2.  */  
   ResTopicID3:string,
      /**  Maintenance Resolution Topic 4. A sub-topic of ResTopicID3.  */  
   ResTopicID4:string,
      /**  Maintenance Resolution Topic 5. A sub-topic of ResTopicID4.  */  
   ResTopicID5:string,
      /**  Maintenance Resolution Topic 6. A sub-topic of ResTopicID5.  */  
   ResTopicID6:string,
      /**  Maintenance Resolution Topic 7. A sub-topic of ResTopicID6.  */  
   ResTopicID7:string,
      /**  Maintenance Resolution Topic 8. A sub-topic of ResTopicID7.  */  
   ResTopicID8:string,
      /**  Maintenance Resolution Topic 9. A sub-topic of ResTopicID8.  */  
   ResTopicID9:string,
      /**  Maintenance Resolution Topic 10. A sub-topic of ResTopicID9.  */  
   ResTopicID10:string,
      /**  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  */  
   ResTopics:string,
      /**  It is updated by Calculate Global Scheduling Order process, it indicates if a job has to be scheduled Backwards or Forwards by Global Scheduling Process and it can be modified by Adjust Scheduling Global Order  */  
   Forward:boolean,
      /**  This is the sequence number used to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  */  
   SchedSeq:number,
      /**  Indicates if at least one subassembly contains a part that is plan as assembly.  It does not indicate if the assembly is marked as PAA - only that the part is PAA in the BOM.  Used in MRP when determining if a job can be reused.  */  
   PAAExists:boolean,
      /**  Indicates if the job structure (BOM) was created inside or outside of the mfg lead time for the job part.  Used in MRP when determining if a job can be reused.  */  
   DtlsWithinLeadTime:boolean,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  It indicates that the shop load for that job was not generated (shopload table). The load in shopload can be recreated by Save Resource Load process  */  
   RoughCut:boolean,
      /**  PlanGUID  */  
   PlanGUID:string,
      /**  PlanUserID  */  
   PlanUserID:string,
      /**  LastChangedBy  */  
   LastChangedBy:string,
      /**  LastChangedOn  */  
   LastChangedOn:string,
      /**  EPMExportLevel  */  
   EPMExportLevel:number,
      /**  JobWorkflowState  */  
   JobWorkflowState:string,
      /**  JobCSR  */  
   JobCSR:string,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  LastExternalMESDate  */  
   LastExternalMESDate:string,
      /**  LastScheduleDate  */  
   LastScheduleDate:string,
      /**  LastScheduleProc  */  
   LastScheduleProc:string,
      /**  Sequence priority used internally by Calculate Global Scheduling Order process to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  */  
   SchedPriority:number,
      /**  It indicates the days a job is going to be late in relation to its required due date  */  
   DaysLate:number,
      /**  ContractID  */  
   ContractID:string,
      /**  Logical field to indicate if this record has been read by project analysis process  */  
   ProjProcessed:boolean,
      /**  SyncReqBy  */  
   SyncReqBy:boolean,
      /**  CustName  */  
   CustName:string,
      /**  CustID  */  
   CustID:string,
      /**  IsCSRSet  */  
   IsCSRSet:boolean,
      /**  UnReadyCostProcess  */  
   UnReadyCostProcess:boolean,
      /**  ProcSuspendedUpdates  */  
   ProcSuspendedUpdates:string,
      /**  DateTime field to indicate when this record has been read by project analysis process  */  
   ProjProcessedDate:string,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
      /**  Related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   KBConfigProdID:number,
      /**  Indicates if this revision is to use Advanced Staging.  */  
   UseAdvancedStaging:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  PersonIDName  */  
   PersonIDName:string,
      /**  This flag indicates if the job is ready to be fulfilled.  */  
   ReadyToFulfill:boolean,
      /**  FSMSendTo  */  
   FSMSendTo:boolean,
      /**  FSMServiceReportID  */  
   FSMServiceReportID:string,
   AdvanceLaborRate:boolean,
      /**  Calculated field is set Not UnReadyCostProcess  */  
   dspReadyCostProcess:boolean,
      /**  Determine if jobengineered is enabled or disabled.  */  
   EnableJobEngineered:boolean,
      /**  Should JobFirm be enabled or disabled?  */  
   EnableJobFirm:boolean,
      /**  Determine if jobreleased is enabled or disabled.  */  
   EnableJobReleased:boolean,
   EnableMaterialStatus:boolean,
   EnableProject:boolean,
      /**  Is the job allowed to be engineered?  */  
   EngineerAllowed:boolean,
   EquipLocDesc:string,
      /**  If some fields except ToFirm have been updated  */  
   ExtUpdated:boolean,
      /**   Final Operation – This is scheduled Due Date for either:
1.	Operation on ASM that has Final Operation checkbox selected
2.	If no Operation on ASM has Final Operation selected than use Last Operation on ASM  */  
   FinalOpDueDate:string,
      /**  If it's Stocked assembly and PlanAsAsm is true.  */  
   FirmProcEnable:boolean,
      /**  is used to select stocked Job which will be processed by Firming Process instead of Firm check-box. Is available only for .FirmProcEnable = true (in Job Status Maintenance).  */  
   FirmProcess:boolean,
      /**  Job has at least one assembly with flag Plan as Assembly.  */  
   HasPlanAsAsm:boolean,
      /**  Depending on the engineered job flag, is the header information enabled?  */  
   HeaderSensitive:boolean,
      /**  It will allow displaying default of this value from Plant.IgnoreMtlConstraints  */  
   IgnoreMtlConstraints:boolean,
   JobTypeName:string,
      /**  If part is backflush the kit time is ignored.  */  
   KitTime:number,
      /**  Locked Qty Flag  */  
   LockedQty:boolean,
   NewMeter:number,
      /**  The old Job Number when JobFirm is changed from no to yes.  */  
   OldJobNum:string,
      /**  The order qty  */  
   OrderQty:number,
      /**  Logical field signifying whether JobHead.PartNum is a valid part master part.  */  
   PartmasterPart:boolean,
   PhaseDescription:string,
      /**  Relative to Maintenance Jobs (JobType = "MNT") indicates if job is for "Preventive Maintenance".  This is a job that was created for a Equipment Maintenance Plan (JobHead.PlanNum > 0)  */  
   PMJob:boolean,
      /**  Process Mode Description  */  
   ProcessModeDescription:string,
      /**  Receive Time field for Job Part entered on Job  */  
   ReceiveTime:number,
      /**  Original smart string passed in for configuration  */  
   SmartString:string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   SmartStringProcessed:boolean,
   SOExists:boolean,
   StockQty:number,
      /**  To be Firmed  */  
   ToFirm:boolean,
      /**  Description for XRefPartType  */  
   XRefPartTypeDesc:string,
      /**  The audit change description for the jobaudit record.  */  
   ChangeDescription:string,
   ClearDataset:boolean,
      /**  True if more than one co-part exists  */  
   IsCoPart:boolean,
      /**  The identifier of related Process Manufacturing.  */  
   PartRevProcessMfgID:string,
      /**  Type of Process Manufacturing.  */  
   PartRevProcessMfgType:string,
      /**  Determines if the Service Job has to be synchronized with Epicor FSI application.  */  
   SendToFSA:boolean,
   BitFlag:number,
   AnalysisCdDescription:string,
   CallLineLineDesc:string,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
   EquipMeterUOM:string,
   EquipSerialNum:string,
   EquipLocID:string,
   EquipPlant:string,
   EquipDescription:string,
   EquipBrand:string,
   EquipModel:string,
   EquipCurrentMeter:number,
   EquipTypeID:string,
   EquipOEM:string,
   ExpenseCodeDescription:string,
   HDCaseDescription:string,
   IssueTopicID1Description:string,
   IssueTopicID10Description:string,
   IssueTopicID2Description:string,
   IssueTopicID3Description:string,
   IssueTopicID4Description:string,
   IssueTopicID5Description:string,
   IssueTopicID6Description:string,
   IssueTopicID7Description:string,
   IssueTopicID8Description:string,
   IssueTopicID9Description:string,
   PartNumSalesUM:string,
   PartNumIUM:string,
   PartNumTrackLots:boolean,
   PartNumPartDescription:string,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   PartNumSellingFactor:number,
   PartNumPricePerCode:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumLocationIDNumReq:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PartNumAttrClassID:string,
   PlantName:string,
   PlantMaintPlant:string,
   ProdCodeDescription:string,
   ProdTeamIDDescription:string,
   ProdTeamIDName:string,
   ProjectIDDescription:string,
   QuoteLineLineDesc:string,
   QuoteNumCurrencyCode:string,
   ResTopicID1Description:string,
   ResTopicID10Description:string,
   ResTopicID2Description:string,
   ResTopicID3Description:string,
   ResTopicID4Description:string,
   ResTopicID5Description:string,
   ResTopicID6Description:string,
   ResTopicID7Description:string,
   ResTopicID8Description:string,
   ResTopicID9Description:string,
   SchedCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LegalNumGenOptsRow{
   Company:string,
   LegalNumberID:string,
   TransYear:number,
   TransYearSuffix:string,
   DspTransYear:string,
      /**  Indicates if DspTransYear should be displayed when prompting for a manual number.  */  
   ShowDspTransYear:boolean,
   Prefix:string,
      /**  The list of prefixes that can be selected by the user for manual numbers.  */  
   PrefixList:string,
      /**  The suffix portion of the legal number.  */  
   NumberSuffix:string,
      /**  Indicates if the prefix can be entered by the user.  */  
   EnablePrefix:boolean,
      /**  Indicates if the suffix (number) can be entered by the user.  */  
   EnableSuffix:boolean,
   NumberOption:string,
   DocumentDate:string,
   GenerationType:string,
   Description:string,
   TransPeriod:number,
      /**  Prefix for the period  */  
   PeriodPrefix:string,
   ShowTransPeriod:boolean,
      /**  Used when the full legal number is entered  */  
   LegalNumber:string,
   TranDocTypeID:string,
   TranDocTypeID2:string,
   GenerationOption:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SNFormatRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  The PartNum field identifies the Part and is used in the primary key.  */  
   PartNum:string,
      /**  Number of digits in the serial number  */  
   NumberOfDigits:number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   SNMask:string,
      /**   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  */  
   SNBaseDataType:string,
      /**   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  */  
   SNFormat:string,
      /**  Whether or not to have leading zeroes  */  
   LeadingZeroes:boolean,
      /**   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  */  
   SNPrefix:string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   SNMaskSuffix:string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   SNMaskPrefix:string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   SNLastUsedSeq:string,
   HasSerialNumbers:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   PartPricePerCode:string,
   PartTrackLots:boolean,
   PartTrackSerialNum:boolean,
   PartTrackDimension:boolean,
   PartSalesUM:string,
   PartIUM:string,
   PartSellingFactor:number,
   PartPartDescription:string,
   SerialMaskMaskType:number,
   SerialMaskMask:string,
   SerialMaskExample:string,
   SerialMaskDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SelectSerialNumbersParamsRow{
      /**  The part number to which the serial numbers have been assigned.  */  
   partNum:string,
      /**  The quantity of serial numbers that need to be selected.  */  
   quantity:number,
      /**  whereClause for filtering available serial numbers  */  
   whereClause:string,
      /**  transType of this transaction  */  
   transType:string,
      /**  Include when filtering a set of SN's for BL processing is necessary.  It may be null if not needed.  */  
   sourceRowID:string,
      /**  Determines if serial numbers can be created.  */  
   enableCreate:boolean,
      /**  Determines if serial numbers can be selected.  */  
   enableSelect:boolean,
      /**  Determines if serial numbers can be retrieved.  */  
   enableRetrieve:boolean,
      /**  Specifies whether Voided serial numbers can be manually selected.  */  
   allowVoided:boolean,
      /**  The Plant associated with this transaction  */  
   plant:string,
   xrefPartNum:string,
   xrefPartType:string,
   xrefCustNum:number,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   poLinkValues:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   attributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   attributeSetShortDescription:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   revisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SelectSerialNumbersParamsTableset{
   SelectSerialNumbersParams:Erp_Tablesets_SelectSerialNumbersParamsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SelectedJobAsmblRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SelectedJobAsmblTableset{
   SelectedJobAsmbl:Erp_Tablesets_SelectedJobAsmblRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SelectedPartTableset{
   SelectedParts:Erp_Tablesets_SelectedPartsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SelectedPartsRow{
   Company:string,
   PartNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SelectedSerialNumbersRow{
      /**  Company  */  
   Company:string,
      /**  SerialNumber  */  
   SerialNumber:string,
      /**  Scrapped flag  */  
   Scrapped:boolean,
      /**  Scrapped reason code  */  
   ScrappedReasonCode:string,
      /**  Voided flag  */  
   Voided:boolean,
      /**  Reference field  */  
   Reference:string,
      /**  Reason code type = s  */  
   ReasonCodeType:string,
      /**  Reason code description  */  
   ReasonCodeDesc:string,
      /**  PartNumber  */  
   PartNum:string,
      /**  Serial number prefix  */  
   SNPrefix:string,
      /**  Base number used to create the serial number  */  
   SNBaseNumber:string,
      /**  RowID of the source record for this serial number  */  
   SourceRowID:string,
      /**  TransType of the record that created this serial number  */  
   TransType:string,
      /**  True if this serial numbered part passed inspection  */  
   PassedInspection:boolean,
      /**  Used to flag previously selected serial numbers as deselected  */  
   Deselected:boolean,
   KitWhseList:string,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  */  
   RawSerialNum:string,
      /**  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  */  
   KBLbrAction:number,
      /**  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  */  
   KBLbrActionDesc:string,
      /**  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  */  
   PreventDeselect:boolean,
      /**  Used only by SN Assignment  */  
   XRefPartNum:string,
      /**  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  */  
   XRefPartType:string,
   PreDeselected:boolean,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   poLinkValues:string,
      /**  The mask the was used to generate the serial number  */  
   SNMask:string,
      /**  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  */  
   NotSavedToDB:boolean,
   RowSelected:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ttIssueReturn
   */  
export interface FillForeignFields_input{
   ttIssueReturn:Erp_Tablesets_IssueReturnRow[],
}

export interface FillForeignFields_output{
}

   /** Required : 
      @param pkgControlID
   */  
export interface GenerateDynamicPCID_input{
      /**  Package control ID code  */  
   pkgControlID:string,
}

export interface GenerateDynamicPCID_output{
      /**  PCID  */  
   returnObj:string,
}

export interface GetAvailTranDocTypes_output{
parameters : {
      /**  output parameters  */  
   AvailTypes:string,
}
}

   /** Required : 
      @param partNum
      @param attributeSetID
      @param wareHouseCode
   */  
export interface GetInventoryQtyAdjBrwForWeb_input{
      /**  Part number for the adjustment.  */  
   partNum:string,
      /**  Attribute Set ID for the adjustment  */  
   attributeSetID:number,
      /**  Warehouse code used to get bin information.  */  
   wareHouseCode:string,
}

export interface GetInventoryQtyAdjBrwForWeb_output{
   returnObj:Erp_Tablesets_InventoryQtyAdjBrwTableset[],
parameters : {
      /**  output parameters  */  
   primaryBin:string,
}
}

   /** Required : 
      @param partNum
      @param revisionNum
      @param attributeSetID
      @param wareHouseCode
   */  
export interface GetInventoryQtyAdjBrwInventoryTracking_input{
      /**  Part number for the adjustment.  */  
   partNum:string,
      /**  Revision Number used to get bin information. Bins are not filtered by Revision Number if no value is sent.  */  
   revisionNum:string,
      /**  Attribute Set ID used to get bin information. Bins are not filtered by Attribute Set ID if a zero is sent  */  
   attributeSetID:number,
      /**  Warehouse code used to get bin information.  */  
   wareHouseCode:string,
}

export interface GetInventoryQtyAdjBrwInventoryTracking_output{
   returnObj:Erp_Tablesets_InventoryQtyAdjBrwTableset[],
parameters : {
      /**  output parameters  */  
   primaryBin:string,
}
}

   /** Required : 
      @param partNum
      @param attributeSetID
      @param wareHouseCode
   */  
export interface GetInventoryQtyAdjBrw_input{
      /**  Part number for the adjustment.  */  
   partNum:string,
      /**  Attribute Set ID used to get bin information. Bins are not filtered by Attribute Set ID if a zero is sent  */  
   attributeSetID:number,
      /**  Warehouse code used to get bin information.  */  
   wareHouseCode:string,
}

export interface GetInventoryQtyAdjBrw_output{
   returnObj:Erp_Tablesets_InventoryQtyAdjBrwTableset[],
parameters : {
      /**  output parameters  */  
   primaryBin:string,
}
}

   /** Required : 
      @param whereClauseJobHead
      @param pageSize
      @param absolutePage
   */  
export interface GetListJobs_input{
      /**  Where condition without the where word  */  
   whereClauseJobHead:string,
      /**  # of records returned.  0 means all  */  
   pageSize:number,
   absolutePage:number,
}

export interface GetListJobs_output{
   returnObj:Erp_Tablesets_IssueReturnJobListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseJobHead
      @param whereClauseJobAsmbl
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  Where condition without the where word  */  
   whereClauseJobHead:string,
      /**  Where condition without the where word  */  
   whereClauseJobAsmbl:string,
      /**  # of records returned.  0 means all  */  
   pageSize:number,
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_IssueReturnJobAsmblTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param pcFromJobNum
      @param piFromAssemblySeq
      @param pcTranType
      @param pcMtlQueueRowID
      @param ds
   */  
export interface GetNewIssueReturnFromJob_input{
      /**  From Job number.  */  
   pcFromJobNum:string,
      /**  From Assembly Seq.  */  
   piFromAssemblySeq:number,
      /**  Material movement type XXX-XXX e.g STK-MTL  */  
   pcTranType:string,
      /**  Progress database rowid for MtlQueue record  */  
   pcMtlQueueRowID:string,
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface GetNewIssueReturnFromJob_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param pcToJobNum
      @param piToAssemblySeq
      @param pcTranType
      @param pcMtlQueueRowID
      @param ds
   */  
export interface GetNewIssueReturnToJob_input{
      /**  To Job number.  */  
   pcToJobNum:string,
      /**  To Assembly Seq.  */  
   piToAssemblySeq:number,
      /**  Material movement type XXX-XXX e.g STK-MTL  */  
   pcTranType:string,
      /**  Progress database rowid for MtlQueue record  */  
   pcMtlQueueRowID:string,
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface GetNewIssueReturnToJob_output{
parameters : {
      /**  output parameters  */  
   pcMessage:string,
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param pcTranType
      @param pcMtlQueueRowID
      @param pCallProcess
      @param ds
   */  
export interface GetNewIssueReturn_input{
      /**  Material movement type XXX-XXX e.g STK-MTL.  It can be blank when a valid MtlQueue RowIdent is passed.  */  
   pcTranType:string,
      /**  Progress database RowId of MtlQueue record  */  
   pcMtlQueueRowID:string,
      /**  Calling Process  */  
   pCallProcess:string,
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface GetNewIssueReturn_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param pcTranType
      @param pcMtlQueueRowID
      @param pCallProcess
      @param ds
   */  
export interface GetNewJobAsmblMultiple_input{
      /**  Material movement type XXX-XXX e.g STK-MTL  */  
   pcTranType:string,
      /**  Progress database rowid for MtlQueue record  */  
   pcMtlQueueRowID:string,
      /**  Calling Process  */  
   pCallProcess:string,
   ds:Erp_Tablesets_SelectedJobAsmblTableset[],
}

export interface GetNewJobAsmblMultiple_output{
   returnObj:Erp_Tablesets_IssueReturnTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SelectedJobAsmblTableset[],
   pcMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewJobAsmblSearch_input{
   ds:Erp_Tablesets_SelectedJobAsmblTableset[],
}

export interface GetNewJobAsmblSearch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SelectedJobAsmblTableset[],
}
}

   /** Required : 
      @param pcTranType
      @param pcMtlQueueRowID
      @param ds
   */  
export interface GetNewPartMultiple_input{
      /**  Material movement type XXX-XXX e.g STK-MTL  */  
   pcTranType:string,
      /**  Progress database rowid for MtlQueue record  */  
   pcMtlQueueRowID:string,
   ds:Erp_Tablesets_SelectedPartTableset[],
}

export interface GetNewPartMultiple_output{
   returnObj:Erp_Tablesets_IssueReturnTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SelectedPartTableset[],
   pcMessage:string,
}
}

   /** Required : 
      @param pcPartNum
      @param pcTranType
      @param pcMtlQueueRowID
      @param ds
   */  
export interface GetNewPartNum_input{
      /**  Part number  */  
   pcPartNum:string,
      /**  Material movement type XXX-XXX e.g STK-UKN  */  
   pcTranType:string,
      /**  Progress database rowid for MtlQueue record  */  
   pcMtlQueueRowID:string,
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface GetNewPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPartSearch_input{
   ds:Erp_Tablesets_SelectedPartTableset[],
}

export interface GetNewPartSearch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SelectedPartTableset[],
}
}

   /** Required : 
      @param partNum
      @param sysRowID
      @param rowType
      @param uomCode
      @param qty
   */  
export interface GetPartXRefInfo_input{
      /**  Proposed PartNumber change  */  
   partNum:string,
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   sysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
      /**  UOM Code (only used for Product Codes)  */  
   uomCode:string,
      /**  Qty (converted if UOM is different)  */  
   qty:number,
}

export interface GetPartXRefInfo_output{
parameters : {
      /**  output parameters  */  
   partNum:string,
   uomCode:string,
   qty:number,
   serialWarning:string,
   questionString:string,
   multipleMatch:boolean,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsJobAssemblies_input{
      /**  Where condition without the where word  */  
   whereClause:string,
      /**  # of records returned.  0 means all  */  
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsJobAssemblies_output{
   returnObj:Erp_Tablesets_IssueReturnJobAsmblTableset[],
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
export interface GetRowsWIP_input{
      /**  Where condition without the where word  */  
   whereClause:string,
      /**  # of records returned.  */  
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsWIP_output{
   returnObj:Erp_Tablesets_IssueReturnJobAsmblTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseJobHead
      @param whereClauseJobAsmbl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
      /**  Where condition without the where word  */  
   whereClauseJobHead:string,
      /**  Where condition without the where word  */  
   whereClauseJobAsmbl:string,
      /**  # of records returned.  0 means all  */  
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_IssueReturnJobAsmblTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetSelectSerialNumbersParams_input{
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface GetSelectSerialNumbersParams_output{
   returnObj:Erp_Tablesets_SelectSerialNumbersParamsTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param tranType
      @param toWarehouseCode
      @param toBinNum
   */  
export interface GetToBinNumWhereClause_input{
      /**  Tran Type from IssueReturn  */  
   tranType:string,
      /**  To Warehouse Code from IssueReturn  */  
   toWarehouseCode:string,
      /**  To Bin Num from IssueReturn (can be blank)  */  
   toBinNum:string,
}

export interface GetToBinNumWhereClause_output{
parameters : {
      /**  output parameters  */  
   toBinNumWhereClause:string,
}
}

   /** Required : 
      @param ds
   */  
export interface GetUnissuedQty_input{
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface GetUnissuedQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetUnpickSettings_input{
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface GetUnpickSettings_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
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
      @param ipWriteToStaged
   */  
export interface IsAutoPrintSetup_input{
      /**  write to staged table  */  
   ipWriteToStaged:boolean,
}

export interface IsAutoPrintSetup_output{
   returnObj:boolean,
}

   /** Required : 
      @param pcJobNum
      @param piAssemblySeq
   */  
export interface IsValidAssembly_input{
      /**  Job Number  */  
   pcJobNum:string,
      /**  A sequence number that uniquely
            identifies the JobAsmbl record within the JobNum.  */  
   piAssemblySeq:number,
}

export interface IsValidAssembly_output{
parameters : {
      /**  output parameters  */  
   plFound:boolean,
}
}

   /** Required : 
      @param ipJobNum
   */  
export interface JobExists_input{
      /**  JobNum which should check  */  
   ipJobNum:string,
}

export interface JobExists_output{
parameters : {
      /**  output parameters  */  
   opJobReleased:boolean,
   opJobClosed:boolean,
   opJobExists:boolean,
}
}

   /** Required : 
      @param pcid
      @param whse
      @param bin
      @param partNum
      @param ds
   */  
export interface MassUnpickByPCID_input{
      /**  PCID  */  
   pcid:string,
      /**  Destination Warehouse Code  */  
   whse:string,
      /**  Destination Bin Num  */  
   bin:string,
      /**  Part number for Mass Unpick By PCID (optional)  */  
   partNum:string,
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface MassUnpickByPCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
   legalNumMsg:string,
}
}

   /** Required : 
      @param ds
   */  
export interface MasterInventoryBinTests_input{
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface MasterInventoryBinTests_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
   pcNeqQtyAction:string,
   pcNeqQtyMessage:string,
   pcPCBinAction:string,
   pcPCBinMessage:string,
   pcOutBinAction:string,
   pcOutBinMessage:string,
}
}

   /** Required : 
      @param pcPartNum
      @param pcWhseCode
      @param pcBinNum
      @param pcLotNum
      @param pcAttributeSetID
      @param pcPCID
      @param pcDimCode
      @param pdDimConvFactor
      @param pgTranRowId
      @param ipSellingQuantity
   */  
export interface NegativeInventoryTestTran_input{
   pcPartNum:string,
   pcWhseCode:string,
   pcBinNum:string,
   pcLotNum:string,
   pcAttributeSetID:number,
   pcPCID:string,
   pcDimCode:string,
   pdDimConvFactor:number,
   pgTranRowId:string,
   ipSellingQuantity:number,
}

export interface NegativeInventoryTestTran_output{
parameters : {
      /**  output parameters  */  
   pcNeqQtyAction:string,
   pcMessage:string,
}
}

   /** Required : 
      @param pcPartNum
      @param pcWhseCode
      @param pcBinNum
      @param pcLotNum
      @param pcAttributeSetID
      @param pcPCID
      @param pcDimCode
      @param pdDimConvFactor
      @param ipSellingQuantity
   */  
export interface NegativeInventoryTest_input{
   pcPartNum:string,
   pcWhseCode:string,
   pcBinNum:string,
   pcLotNum:string,
   pcAttributeSetID:number,
   pcPCID:string,
   pcDimCode:string,
   pdDimConvFactor:number,
   ipSellingQuantity:number,
}

export interface NegativeInventoryTest_output{
parameters : {
      /**  output parameters  */  
   pcNeqQtyAction:string,
   pcMessage:string,
}
}

   /** Required : 
      @param pUM
      @param ds
   */  
export interface OnChangeASTUom_input{
      /**  from unit of measure  */  
   pUM:string,
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface OnChangeASTUom_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param piFromAssemblySeq
      @param ds
      @param pCallProcess
   */  
export interface OnChangeFromAssemblySeq_input{
      /**  From Assembly Seq  */  
   piFromAssemblySeq:number,
   ds:Erp_Tablesets_IssueReturnTableset[],
      /**  Calling Process value  */  
   pCallProcess:string,
}

export interface OnChangeFromAssemblySeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeFromBinNum_input{
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface OnChangeFromBinNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param pcFromJobNum
      @param ds
      @param pCallProcess
   */  
export interface OnChangeFromJobNum_input{
      /**  From Job Number  */  
   pcFromJobNum:string,
   ds:Erp_Tablesets_IssueReturnTableset[],
      /**  Calling Process value  */  
   pCallProcess:string,
}

export interface OnChangeFromJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param ds
      @param pCallProcess
   */  
export interface OnChangeFromJobSeq_input{
   ds:Erp_Tablesets_IssueReturnTableset[],
      /**  Calling Process value  */  
   pCallProcess:string,
}

export interface OnChangeFromJobSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
   pcMessage:string,
}
}

   /** Required : 
      @param fromPCID
      @param allowDiffPartAndUM
      @param questionCheck
      @param pCallProcess
      @param ds
   */  
export interface OnChangeFromPCID_input{
      /**  From PCID  */  
   fromPCID:string,
      /**  If true allows to default parts that have a different part and/or  unit of measure  */  
   allowDiffPartAndUM:boolean,
      /**  If true throws questions  for the user before defaulting PCID and Part values,
            depending on whether it found a match for the Assembly part on the selected PCID  */  
   questionCheck:boolean,
      /**  Calling process  */  
   pCallProcess:string,
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface OnChangeFromPCID_output{
parameters : {
      /**  output parameters  */  
   questionMsg:string,
   ds:Erp_Tablesets_IssueReturnTableset[],
   pcMessage:string,
}
}

   /** Required : 
      @param ds
      @param pCallProcess
   */  
export interface OnChangeFromWarehouse_input{
   ds:Erp_Tablesets_IssueReturnTableset[],
      /**  Calling Process value  */  
   pCallProcess:string,
}

export interface OnChangeFromWarehouse_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param pcLotNum
      @param ds
   */  
export interface OnChangeLotNum_input{
      /**  Proposed LotNum value  */  
   pcLotNum:string,
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface OnChangeLotNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param ds
      @param pCallProcess
   */  
export interface OnChangePartNum_input{
   ds:Erp_Tablesets_IssueReturnTableset[],
      /**  Calling Process value  */  
   pCallProcess:string,
}

export interface OnChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param ds
      @param pCallProcess
   */  
export interface OnChangeToAssemblySeq_input{
   ds:Erp_Tablesets_IssueReturnTableset[],
      /**  Calling Process value  */  
   pCallProcess:string,
}

export interface OnChangeToAssemblySeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param ds
      @param pCallProcess
   */  
export interface OnChangeToJobNum_input{
   ds:Erp_Tablesets_IssueReturnTableset[],
      /**  Calling Process value  */  
   pCallProcess:string,
}

export interface OnChangeToJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
   pcMessage:string,
}
}

   /** Required : 
      @param ds
      @param pCallProcess
   */  
export interface OnChangeToJobSeq_input{
   ds:Erp_Tablesets_IssueReturnTableset[],
      /**  Calling Process value  */  
   pCallProcess:string,
}

export interface OnChangeToJobSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
   pcMessage:string,
}
}

   /** Required : 
      @param ipPCID
      @param ds
      @param pCallProcess
   */  
export interface OnChangeToPCID_input{
      /**  Proposed To PCID value  */  
   ipPCID:string,
   ds:Erp_Tablesets_IssueReturnTableset[],
      /**  Calling Process value  */  
   pCallProcess:string,
}

export interface OnChangeToPCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param ds
      @param pCallProcess
   */  
export interface OnChangeToWarehouse_input{
   ds:Erp_Tablesets_IssueReturnTableset[],
      /**  Calling Process value  */  
   pCallProcess:string,
}

export interface OnChangeToWarehouse_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param pdTranQty
      @param ds
   */  
export interface OnChangeTranQty_input{
      /**  Transaction Qty  */  
   pdTranQty:number,
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface OnChangeTranQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param pUM
      @param ds
   */  
export interface OnChangeUM_input{
      /**  Transaction UOM  */  
   pUM:string,
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface OnChangeUM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param attributeSetID
      @param ds
   */  
export interface OnChangingAttributeSetAdjustments_input{
   attributeSetID:number,
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface OnChangingAttributeSetAdjustments_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param attributeSetID
      @param ds
   */  
export interface OnChangingAttributeSet_input{
   attributeSetID:number,
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface OnChangingAttributeSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangingFromBinNum_input{
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface OnChangingFromBinNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
   pcMessage:string,
}
}

   /** Required : 
      @param piJobSeq
      @param pcDirection
      @param pCallProcess
      @param ds
   */  
export interface OnChangingJobSeq_input{
      /**  JobSeq  */  
   piJobSeq:number,
      /**  Direction  */  
   pcDirection:string,
      /**  Calling Process value  */  
   pCallProcess:string,
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface OnChangingJobSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param numberOfPieces
      @param ds
   */  
export interface OnChangingNumberOfPieces_input{
   numberOfPieces:number,
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface OnChangingNumberOfPieces_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingRevisionNumAdjustments_input{
   revisionNum:string,
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface OnChangingRevisionNumAdjustments_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface OnChangingRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param piToJobSeq
      @param ds
   */  
export interface OnChangingToJobSeq_input{
      /**  Propose ToJobSeq value.  */  
   piToJobSeq:number,
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface OnChangingToJobSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

   /** Required : 
      @param plNegQtyAction
      @param ds
   */  
export interface PerformMaterialMovement2_input{
      /**  when TranQty changes, perform NegativeInventoryTest. Provide the answer of that test here.  */  
   plNegQtyAction:boolean,
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface PerformMaterialMovement2_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
   legalNumberMessage:string,
   message:string,
   partTranPKs:string,
}
}

   /** Required : 
      @param plNegQtyAction
      @param ds
      @param legalNum
   */  
export interface PerformMaterialMovementWithLegalNum_input{
      /**  when TranQty changes, perform NegativeInventoryTest. Provide the answer of that test here.  */  
   plNegQtyAction:boolean,
   ds:Erp_Tablesets_IssueReturnTableset[],
      /**  The Legal Number to be used in PartTran.  */  
   legalNum:string,
}

export interface PerformMaterialMovementWithLegalNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
   legalNumberMessage:string,
   partTranPKs:string,
}
}

   /** Required : 
      @param plNegQtyAction
      @param ds
   */  
export interface PerformMaterialMovement_input{
      /**  when TranQty changes, perform NegativeInventoryTest. Provide the answer of that test here.  */  
   plNegQtyAction:boolean,
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface PerformMaterialMovement_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
   legalNumberMessage:string,
   partTranPKs:string,
}
}

   /** Required : 
      @param pcMtlQueueRowID
   */  
export interface PreGetNewIssueReturn_input{
      /**  Progress database RowId of MtlQueue record  */  
   pcMtlQueueRowID:string,
}

export interface PreGetNewIssueReturn_output{
parameters : {
      /**  output parameters  */  
   pcAction:string,
   pcMessage:string,
   pdQtyAvailable:number,
}
}

   /** Required : 
      @param ds
   */  
export interface PrePerformMaterialMovement_input{
   ds:Erp_Tablesets_IssueReturnTableset[],
}

export interface PrePerformMaterialMovement_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
   requiresUserInput:boolean,
}
}

export interface SetQuantity_output{
}

   /** Required : 
      @param empID
   */  
export interface SuppressPrintMessages_input{
      /**  Employee ID  */  
   empID:string,
}

export interface SuppressPrintMessages_output{
      /**  Suppress Print Messages  */  
   returnObj:boolean,
}

   /** Required : 
      @param iPartNum
      @param iUOM
   */  
export interface ValidUOM_input{
   iPartNum:string,
   iUOM:string,
}

export interface ValidUOM_output{
   returnObj:boolean,
}

   /** Required : 
      @param pkgControlIDCode
   */  
export interface ValidatePkgControlID_input{
      /**  Proposed package control ID code  */  
   pkgControlIDCode:string,
}

export interface ValidatePkgControlID_output{
}

   /** Required : 
      @param ds
      @param serialNumber
   */  
export interface ValidateSN_input{
   ds:Erp_Tablesets_IssueReturnTableset[],
      /**  Serial number to validate.  */  
   serialNumber:string,
}

export interface ValidateSN_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
   isVoided:boolean,
}
}

export interface _History07_08_output{
}

   /** Required : 
      @param ttIssueReturn
   */  
export interface checkWhseBin_input{
   ttIssueReturn:Erp_Tablesets_IssueReturnRow[],
}

export interface checkWhseBin_output{
}

   /** Required : 
      @param ds
      @param binNum
   */  
export interface validateToBinNum_input{
   ds:Erp_Tablesets_IssueReturnTableset[],
      /**  binNum  */  
   binNum:string,
}

export interface validateToBinNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IssueReturnTableset[],
}
}

