import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.MassIssueToMfgSvc
// Description: Use this function to quickly issue all planned materials to a job,
instead of entering them individually.
Serialized parts cannot be issued using this function depending on plant serial tracking setting.
Issue transactions generated in this way reduce inventory quantities,
and post material costs to the Job.
This is a useful function if your material estimates are fairly accurate.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/$metadata", {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobHeadRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobHeadRow)
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
   Summary: Invoke method GetRows
   Description: List of jobs that can be selected for Mass Issue.
   OperationID: Get_GetRows
      @param whereClauseSetupGrp Desc: Where condition without the where word   Required: True   Allow empty value : True
      @param pageSize Desc: # of records returned.  0 means all   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseSetupGrp:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseSetupGrp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSetupGrp=" + whereClauseSetupGrp
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

   return (new Promise<GetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/GetRows" + params, {
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
         resolve(data as GetRows_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAvailTranDocTypes
   Description: Get Available Transaction Doc Types method.
   OperationID: GetAvailTranDocTypes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAvailTranDocTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailTranDocTypes(requestBody:GetAvailTranDocTypes_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAvailTranDocTypes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/GetAvailTranDocTypes", {
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
         resolve(data as GetAvailTranDocTypes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildMassIssueBrowse
   Description: This method is called when the user presses Issue button after entering the Job#.
This method builds and returns the Epicor.Mfg.BO.MassIssueToMfgDataSet dataset.
   OperationID: BuildMassIssueBrowse
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildMassIssueBrowse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildMassIssueBrowse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildMassIssueBrowse(requestBody:BuildMassIssueBrowse_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildMassIssueBrowse_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/BuildMassIssueBrowse", {
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
         resolve(data as BuildMassIssueBrowse_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMassIssueToMfg
   Description: Returns dataset MassIssueToMfg that contains records that can be issued/returned
   OperationID: GetMassIssueToMfg
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetMassIssueToMfg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMassIssueToMfg_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMassIssueToMfg(requestBody:GetMassIssueToMfg_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetMassIssueToMfg_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/GetMassIssueToMfg", {
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
         resolve(data as GetMassIssueToMfg_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ClearAll
   Description: Clear All - Clear all issued quantities
   OperationID: ClearAll
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ClearAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClearAll(requestBody:ClearAll_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ClearAll_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/ClearAll", {
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
         resolve(data as ClearAll_output)
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
      @param whereClauseSetupGrp Desc: Where condition without the where word   Required: True   Allow empty value : True
      @param pageSize Desc: # of records returned.  0 means all   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(whereClauseSetupGrp:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseSetupGrp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSetupGrp=" + whereClauseSetupGrp
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

   return (new Promise<GetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/GetList" + params, {
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
         resolve(data as GetList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListPaging
   Description: List of jobs that can be selected for Mass Issue.  This method considers server paging
   OperationID: Get_GetListPaging
      @param whereClause Desc: Where condition without the where word   Required: True   Allow empty value : True
      @param pageSize Desc: # of records returned.  0 means all   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListPaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetListPaging(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
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

   return (new Promise<GetListPaging_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/GetListPaging" + params, {
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
         resolve(data as GetListPaging_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMassIssueInput
   Description: Create a new Epicor.Mfg.BO.MassIssueInputDataSet.  Only few fields like
Company and TranDate are populated.  All other fields are dependent on
the user selecting a job#.  After the user enters a Job# call OnChangeJobNum
to populate other fields in MassIssueInputDataSet .
   OperationID: GetNewMassIssueInput
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMassIssueInput_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMassIssueInput_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMassIssueInput(requestBody:GetNewMassIssueInput_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMassIssueInput_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/GetNewMassIssueInput", {
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
         resolve(data as GetNewMassIssueInput_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMassIssueInputJobNum
   Description: Create a new Epicor.Mfg.BO.MassIssueInputDataSet based on the Job# input.
   OperationID: GetNewMassIssueInputJobNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMassIssueInputJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMassIssueInputJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMassIssueInputJobNum(requestBody:GetNewMassIssueInputJobNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMassIssueInputJobNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/GetNewMassIssueInputJobNum", {
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
         resolve(data as GetNewMassIssueInputJobNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMassIssueInputList
   Description: This method creates a new ttMassIssueInputList row entry.
   OperationID: GetNewMassIssueInputList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMassIssueInputList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMassIssueInputList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMassIssueInputList(requestBody:GetNewMassIssueInputList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMassIssueInputList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/GetNewMassIssueInputList", {
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
         resolve(data as GetNewMassIssueInputList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMassIssueInputMultiple
   Description: Call this method when the user selects multiple jobs.  This method populates
the Epicor.Mfg.BO.JobClosingDataSet dataset with Job , JobOper and JobMtl information.
   OperationID: GetNewMassIssueInputMultiple
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMassIssueInputMultiple_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMassIssueInputMultiple_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMassIssueInputMultiple(requestBody:GetNewMassIssueInputMultiple_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMassIssueInputMultiple_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/GetNewMassIssueInputMultiple", {
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
         resolve(data as GetNewMassIssueInputMultiple_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMassIssueInputForJob
   Description: Call this method to return data for a specific job
   OperationID: GetMassIssueInputForJob
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetMassIssueInputForJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMassIssueInputForJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMassIssueInputForJob(requestBody:GetMassIssueInputForJob_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetMassIssueInputForJob_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/GetMassIssueInputForJob", {
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
         resolve(data as GetMassIssueInputForJob_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IssueAll
   Description: Issue All - Default Issue All
   OperationID: IssueAll
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IssueAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IssueAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IssueAll(requestBody:IssueAll_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IssueAll_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/IssueAll", {
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
         resolve(data as IssueAll_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method NegativeStockCheck
   Description: This method performs the Negative Stock check.  This procedure should be run
before calling PerformMassIssue method.
   OperationID: NegativeStockCheck
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/NegativeStockCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NegativeStockCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NegativeStockCheck(requestBody:NegativeStockCheck_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<NegativeStockCheck_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/NegativeStockCheck", {
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
         resolve(data as NegativeStockCheck_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeAssemblySeq
   Description: To populate the MassIssueInputDataSet dataset with the fields when JobNum changes
This method populates and returns the Epicor.Mfg.BO.MassIssueInputDataSet dataset.
   OperationID: OnChangeAssemblySeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeAssemblySeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAssemblySeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAssemblySeq(requestBody:OnChangeAssemblySeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeAssemblySeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/OnChangeAssemblySeq", {
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
         resolve(data as OnChangeAssemblySeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBinNum
   Description: Call this method when binnum changes in Epicor.Mfg.BO.MassIssueToMfgDataSet dataset
It returns a new Bin number and onhandqty.
   OperationID: OnChangeBinNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBinNum(requestBody:OnChangeBinNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBinNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/OnChangeBinNum", {
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
         resolve(data as OnChangeBinNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBinNumForSysRow
   Description: Call this method when binNum changes in Epicor.Mfg.BO.MassIssueToMfgDataSet dataset
It returns a new Bin number and onhandqty.
   OperationID: OnChangeBinNumForSysRow
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBinNumForSysRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBinNumForSysRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBinNumForSysRow(requestBody:OnChangeBinNumForSysRow_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBinNumForSysRow_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/OnChangeBinNumForSysRow", {
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
         resolve(data as OnChangeBinNumForSysRow_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeJobNum
   Description: Call this method when the Job# changes in ttMassIssueInputJob.
   OperationID: OnChangeJobNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeJobNum(requestBody:OnChangeJobNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeJobNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/OnChangeJobNum", {
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
         resolve(data as OnChangeJobNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeLotNum
   Description: Call this method when Lot number changes in Epicor.Mfg.BO.MassIssueToMfgDataSet dataset.
This method checks whether the user has security permissions to create lot.
   OperationID: OnChangeLotNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeLotNum(requestBody:OnChangeLotNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeLotNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/OnChangeLotNum", {
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
         resolve(data as OnChangeLotNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeLotNumForSysRowID
   Description: Call this method when Lot number changes in Epicor.Mfg.BO.MassIssueToMfgDataSet dataset.
This method checks whether the user has security permissions to create lot.
   OperationID: OnChangeLotNumForSysRowID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeLotNumForSysRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLotNumForSysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeLotNumForSysRowID(requestBody:OnChangeLotNumForSysRowID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeLotNumForSysRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/OnChangeLotNumForSysRowID", {
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
         resolve(data as OnChangeLotNumForSysRowID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePartNum
   Description: To populate the Epicor.Mfg.BO.MassIssueToMfgDataSet dataset with the fields when PartNum changes
Call this method when PartNum changes.
   OperationID: OnChangePartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartNum(requestBody:OnChangePartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/OnChangePartNum", {
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
         resolve(data as OnChangePartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeQtyIssued
   Description: Call this method when Qty Issued changes in Epicor.Mfg.BO.MassIssueToMfgDataSet dataset
It returns a yes or no value for IssuedComplete.
   OperationID: OnChangeQtyIssued
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeQtyIssued_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQtyIssued_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeQtyIssued(requestBody:OnChangeQtyIssued_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeQtyIssued_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/OnChangeQtyIssued", {
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
         resolve(data as OnChangeQtyIssued_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeUOMCode
   Description: Recalculates stockqty when the UOM changes.
   OperationID: OnChangeUOMCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeUOMCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUOMCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeUOMCode(requestBody:OnChangeUOMCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeUOMCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/OnChangeUOMCode", {
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
         resolve(data as OnChangeUOMCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeWareHouse
   Description: Call this method when Ware house changes in Epicor.Mfg.BO.MassIssueToMfgDataSet dataset
It returns a new Bin number
   OperationID: OnChangeWareHouse
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeWareHouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWareHouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeWareHouse(requestBody:OnChangeWareHouse_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeWareHouse_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/OnChangeWareHouse", {
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
         resolve(data as OnChangeWareHouse_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnPartNumChanging
   Description: Call this method when the value of Part is changing for validation.
   OperationID: OnPartNumChanging
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnPartNumChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnPartNumChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnPartNumChanging(requestBody:OnPartNumChanging_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnPartNumChanging_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/OnPartNumChanging", {
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
         resolve(data as OnPartNumChanging_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingNumberOfPieces(requestBody:OnChangingNumberOfPieces_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingNumberOfPieces_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/OnChangingNumberOfPieces", {
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
         resolve(data as OnChangingNumberOfPieces_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PerformMassIssue
   Description: This function performs the processing required to do the Mass Issue to
manufacturing.  No transactions are committed to the database unless
this function is invoked.
Please call NegativeStockCheck method before calling PerformMassIssue.
   OperationID: PerformMassIssue
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PerformMassIssue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PerformMassIssue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PerformMassIssue(requestBody:PerformMassIssue_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PerformMassIssue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/PerformMassIssue", {
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
         resolve(data as PerformMassIssue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PerformMassIssueReturn
   Description: This function performs the processing required to do the Mass Issue to
Manufacturing and Mass Return from Manufacturing.  No transactions are committed to the database unless
this function is invoked.
Call NegativeStockCheck method before calling PerformMassIssueReturn.
This method returns a list that contains the keys of PartTran records created.
   OperationID: PerformMassIssueReturn
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PerformMassIssueReturn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PerformMassIssueReturn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PerformMassIssueReturn(requestBody:PerformMassIssueReturn_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PerformMassIssueReturn_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/PerformMassIssueReturn", {
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
         resolve(data as PerformMassIssueReturn_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PrePerformMassIssueHT
   Description: Store the results of PrePerformMassIssue in hash-table htPrePerform
   OperationID: PrePerformMassIssueHT
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PrePerformMassIssueHT_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePerformMassIssueHT_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrePerformMassIssueHT(requestBody:PrePerformMassIssueHT_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PrePerformMassIssueHT_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/PrePerformMassIssueHT", {
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
         resolve(data as PrePerformMassIssueHT_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PrePerformMassIssue
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PrePerformMassIssue
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PrePerformMassIssue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePerformMassIssue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrePerformMassIssue(requestBody:PrePerformMassIssue_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PrePerformMassIssue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/PrePerformMassIssue", {
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
         resolve(data as PrePerformMassIssue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PrePerformMassIssueOneItem
   Description: This method will return a record in the LegalNumGenOpts datatable against the current Mtl if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PrePerformMassIssueOneItem
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PrePerformMassIssueOneItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePerformMassIssueOneItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrePerformMassIssueOneItem(requestBody:PrePerformMassIssueOneItem_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PrePerformMassIssueOneItem_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/PrePerformMassIssueOneItem", {
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
         resolve(data as PrePerformMassIssueOneItem_output)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JobHeadRow,
}

export interface Erp_Tablesets_JobHeadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  */  
   "JobClosed":boolean,
      /**  Date the Job was closed.  Defaults as the system but can be overridden.  */  
   "ClosedDate":string,
      /**  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  */  
   "JobComplete":boolean,
      /**  The date that production was completed for this Job.  Maintained via Job Completion Processing.  */  
   "JobCompletionDate":string,
      /**  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  */  
   "JobEngineered":boolean,
      /**   Optional Job check off number 1.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   "CheckOff1":boolean,
      /**   Optional Job check off number 2.  The label for this field is found in JCSyst. If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   "CheckOff2":boolean,
      /**   Optional Job check off number 3.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   "CheckOff3":boolean,
      /**  Optional Job check off number 4.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   "CheckOff4":boolean,
      /**  Optional Job check off number 5.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   "CheckOff5":boolean,
      /**  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  */  
   "JobReleased":boolean,
      /**  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  */  
   "JobHeld":boolean,
      /**  Scheduling Status Control (R-Required, P-Pending, A-Active, C-Complete).  NOT CURRENTLY IMPLEMENTED.  */  
   "SchedStatus":string,
      /**  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  */  
   "JobNum":string,
      /**   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  */  
   "PartNum":string,
      /**  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  */  
   "DrawNum":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "PartDescription":string,
      /**  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  */  
   "ProdQty":number,
      /**  The unit of measure for the job.  Defaulted from Part.IUM.  */  
   "IUM":string,
      /**  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   "StartDate":string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   "StartHour":number,
      /**  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  */  
   "DueDate":string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  */  
   "DueHour":number,
      /**  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  */  
   "ReqDueDate":string,
      /**  An optional user defined code.  This will be used for report selections and views of job headers.  */  
   "JobCode":string,
      /**  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  */  
   "QuoteNum":number,
      /**  Contains the quote line number reference. (see QuoteNum )  */  
   "QuoteLine":number,
      /**  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   "ProdCode":string,
      /**  UserChar1  */  
   "UserChar1":string,
      /**  UserChar2  */  
   "UserChar2":string,
      /**  UserChar3  */  
   "UserChar3":string,
      /**  UserChar4  */  
   "UserChar4":string,
      /**  UserDate1  */  
   "UserDate1":string,
      /**  UserDate2  */  
   "UserDate2":string,
      /**  UserDate3  */  
   "UserDate3":string,
      /**  UserDate4  */  
   "UserDate4":string,
      /**  UserDecimal1  */  
   "UserDecimal1":number,
      /**  UserDecimal2  */  
   "UserDecimal2":number,
      /**  UserInteger1  */  
   "UserInteger1":number,
      /**  UserInteger2  */  
   "UserInteger2":number,
      /**  Editor widget for Job header comments.  */  
   "CommentText":string,
      /**  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  */  
   "ExpenseCode":string,
      /**  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  */  
   "InCopyList":boolean,
      /**   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  */  
   "WIName":string,
      /**  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   "WIStartDate":string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   "WIStartHour":number,
      /**  Scheduled "What If" finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  */  
   "WIDueDate":string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  */  
   "WIDueHour":number,
      /**   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  */  
   "Candidate":boolean,
      /**  Scheduling Code.  SchedCode references a record in the SchedPri table.  */  
   "SchedCode":string,
      /**  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  */  
   "SchedLocked":boolean,
      /**  Associates the JobHead with a project in the Project table.  This can be blank.  */  
   "ProjectID":string,
      /**  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  */  
   "WIPCleared":boolean,
      /**  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  */  
   "JobFirm":boolean,
      /**  A LIST-DELIM delimited list of people.  */  
   "PersonList":string,
      /**   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  */  
   "PersonID":string,
      /**  Production Team for the Job.  Associates the JobHead with a ProdTeam.  */  
   "ProdTeamID":string,
      /**   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  */  
   "QtyCompleted":number,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  */  
   "DatePurged":string,
      /**  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  */  
   "TravelerReadyToPrint":boolean,
      /**  The last date the job traveler was mass printed.  */  
   "TravelerLastPrinted":string,
      /**  Indicates if the Status can be printed. Print functions are not available if this is = No.  */  
   "StatusReadyToPrint":boolean,
      /**  The last date the job status was mass printed.  */  
   "StatusLastPrinted":string,
      /**  The Service Call number that this Job is linked to.  */  
   "CallNum":number,
      /**  The Service Call Line that this Job is linked to.  */  
   "CallLine":number,
      /**  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  */  
   "JobType":string,
      /**  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  */  
   "RestoreFlag":string,
      /**  Project Phase ID  */  
   "PhaseID":string,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**  Indicates that the quantity on this job is locked  */  
   "LockQty":boolean,
      /**  The help desk case that created this job.  */  
   "HDCaseNum":number,
      /**   Values: S(Sequential) or C(Concurrent).
Defaults as S. Must have Advanced Production License to change. Controls how the operations and material requirements are developed. Concurrent jobs are used where the production time is based on the number of machine operations performed and not on the number of parts created. For example, a stamping operation where each cycle of the machine stamps out x number of parts. A further extension of this is that the operation can yield multiple different parts from each cycle of the machine.  Identification of these parts and there associated PPO (parts per operation) is define in the JobPart table.  */  
   "ProcessMode":string,
      /**  The planned date when the job needs to be actioned by the production department to make sure that the job is ready on the planned completion date.  */  
   "PlannedActionDate":string,
      /**  The date that the job needs to be ready for the warehouse to kit to make sure that it is ready for the job start date.  */  
   "PlannedKitDate":string,
      /**  The task ID that is returned from Microsoft Project.  */  
   "MSPTaskID":string,
      /**  This is the Microsoft Project predecessor. This needs to be a text field as Microsoft Project may pass back an alpha numeric string.  */  
   "MSPPredecessor":string,
      /**  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   "UserMapData":string,
      /**  Flag to indicate whether operations for this job will use the production yield features set up in OpMaster for the operation code. Defaulted from Site.ProductionYield  */  
   "ProductionYield":boolean,
      /**  This field will be set to the value of the JobHead.ProdQty at the time the JobHead.Engineered flag is set to true.  */  
   "OrigProdQty":number,
      /**  This field is used to indicate whether the original quantities should be reset in the job header and its assemblies at JobHead update if JobHead.JobEngineered has been changed from false to true. Generally the orig qtys will be reset, unless this flag is set to true because the user was asked if they wanted to reset the orig qtys and they answered yes.  */  
   "PreserveOrigQtys":boolean,
      /**  If set to yes then exclude this job from the Job Auto-Completion process. Not directly maintainable.  */  
   "NoAutoCompletion":boolean,
      /**  No Auto Closing. If set to yes then exclude this job from the Job Auto-Closing process.  */  
   "NoAutoClosing":boolean,
      /**  The user that created this Job.  */  
   "CreatedBy":string,
      /**  The date that this Job was created.  */  
   "CreateDate":string,
      /**  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  */  
   "WhseAllocFlag":boolean,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   "OwnershipStatus":string,
      /**  Holds the internal object id of PDM parts.  */  
   "PDMObjID":string,
      /**  This field is used to store a code that represents the external system that the Job is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  */  
   "ExportRequested":string,
      /**  Flag to indicate how to split the manufacturing cost elements when a manufactured material is issued to the job.  If flag is set to true, the cost of the issued material will be split into individual manufacturing cost elements. If set to false, the cost of the issued material is added to the manufacturing material cost element only.  This is defaulted from the JCSyst.SplitMfgCostElements and is not user maintainable.  */  
   "SplitMfgCostElements":boolean,
      /**  Cross Reference Part Num. Used for alternate serial mask support.  */  
   "XRefPartNum":string,
      /**   Cross Reference Part Type. Used for alternate serial mask support.

I=Internal Cross Reference / C = Customer Part  */  
   "XRefPartType":string,
      /**  Customer Number XRefPartNum is related to if it is a customer part. Used for alternate serial number mask support.  */  
   "XRefCustNum":number,
      /**  Base Part Number. Used in the configurator to identify the configurator part Number.  */  
   "BasePartNum":string,
      /**  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  */  
   "BaseRevisionNum":string,
      /**  Indicates if the job was rough cut scheduled.  */  
   "RoughCutScheduled":boolean,
      /**   The ID of the Equipment that this "Maintenance Job" is for.
Foreign key component to Equip table.  */  
   "EquipID":string,
      /**   Preventive Maintenance Plan Number that this "Maintenance Job" is for. Foreign key component to EquipPlan table.
Note: A Maintenance Job does not have to be for a Preventive Maintenance plan, in which case this is zero.
If time based plan, then the closing process will update the EquipPlan.NextDate. Therefore, the Job must know the EquipID and PlanNum in order to do this.  */  
   "PlanNum":number,
      /**  Maintenance Job Priority. Valid values: H - High, M - Medium, L - Low.  M is default or if created from a Maint Request then MaintReq.Priority is used as default.  */  
   "MaintPriority":string,
      /**  Internal field indicating this job was created by a job split.  Assigned true when a job has been split due to start minimum lot size quantity processing.  */  
   "SplitJob":boolean,
      /**  Indicates the type of prefix which is used for create jobs in MRP  */  
   "NumberSource":boolean,
      /**  The Meter Reading value entered at time of Job Closing.  */  
   "CloseMeterReading":number,
      /**  Maintenance Issue Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  */  
   "IssueTopicID1":string,
      /**  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  */  
   "IssueTopicID2":string,
      /**  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  */  
   "IssueTopicID3":string,
      /**  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  */  
   "IssueTopicID4":string,
      /**  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  */  
   "IssueTopicID5":string,
      /**  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  */  
   "IssueTopicID6":string,
      /**  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  */  
   "IssueTopicID7":string,
      /**  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  */  
   "IssueTopicID8":string,
      /**  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  */  
   "IssueTopicID9":string,
      /**  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  */  
   "IssueTopicID10":string,
      /**  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  */  
   "IssueTopics":string,
      /**  Maintenance Resolution Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintRes = Yes  */  
   "ResTopicID1":string,
      /**  Maintenance Resolution Topic 2. A sub-topic of ResTopicID1.  */  
   "ResTopicID2":string,
      /**  Maintenace  Resolution Topic 3. A sub-topic of ResTopicID2.  */  
   "ResTopicID3":string,
      /**  Maintenance Resolution Topic 4. A sub-topic of ResTopicID3.  */  
   "ResTopicID4":string,
      /**  Maintenance Resolution Topic 5. A sub-topic of ResTopicID4.  */  
   "ResTopicID5":string,
      /**  Maintenance Resolution Topic 6. A sub-topic of ResTopicID5.  */  
   "ResTopicID6":string,
      /**  Maintenance Resolution Topic 7. A sub-topic of ResTopicID6.  */  
   "ResTopicID7":string,
      /**  Maintenance Resolution Topic 8. A sub-topic of ResTopicID7.  */  
   "ResTopicID8":string,
      /**  Maintenance Resolution Topic 9. A sub-topic of ResTopicID8.  */  
   "ResTopicID9":string,
      /**  Maintenance Resolution Topic 10. A sub-topic of ResTopicID9.  */  
   "ResTopicID10":string,
      /**  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  */  
   "ResTopics":string,
      /**  It is updated by Calculate Global Scheduling Order process, it indicates if a job has to be scheduled Backwards or Forwards by Global Scheduling Process and it can be modified by Adjust Scheduling Global Order  */  
   "Forward":boolean,
      /**  This is the sequence number used to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  */  
   "SchedSeq":number,
      /**  Indicates if at least one subassembly contains a part that is plan as assembly.  It does not indicate if the assembly is marked as PAA - only that the part is PAA in the BOM.  Used in MRP when determining if a job can be reused.  */  
   "PAAExists":boolean,
      /**  Indicates if the job structure (BOM) was created inside or outside of the mfg lead time for the job part.  Used in MRP when determining if a job can be reused.  */  
   "DtlsWithinLeadTime":boolean,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  It indicates that the shop load for that job was not generated (shopload table). The load in shopload can be recreated by Save Resource Load process  */  
   "RoughCut":boolean,
      /**  PlanGUID  */  
   "PlanGUID":string,
      /**  PlanUserID  */  
   "PlanUserID":string,
      /**  LastChangedBy  */  
   "LastChangedBy":string,
      /**  LastChangedOn  */  
   "LastChangedOn":string,
      /**  EPMExportLevel  */  
   "EPMExportLevel":number,
      /**  JobWorkflowState  */  
   "JobWorkflowState":string,
      /**  JobCSR  */  
   "JobCSR":string,
      /**  Indicates the record is used with Machine MES  */  
   "ExternalMES":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  LastExternalMESDate  */  
   "LastExternalMESDate":string,
      /**  LastScheduleDate  */  
   "LastScheduleDate":string,
      /**  LastScheduleProc  */  
   "LastScheduleProc":string,
      /**  Sequence priority used internally by Calculate Global Scheduling Order process to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  */  
   "SchedPriority":number,
      /**  It indicates the days a job is going to be late in relation to its required due date  */  
   "DaysLate":number,
      /**  ContractID  */  
   "ContractID":string,
      /**  Logical field to indicate if this record has been read by project analysis process  */  
   "ProjProcessed":boolean,
      /**  SyncReqBy  */  
   "SyncReqBy":boolean,
      /**  CustName  */  
   "CustName":string,
      /**  CustID  */  
   "CustID":string,
      /**  IsCSRSet  */  
   "IsCSRSet":boolean,
      /**  UnReadyCostProcess  */  
   "UnReadyCostProcess":boolean,
      /**  ProcSuspendedUpdates  */  
   "ProcSuspendedUpdates":string,
      /**  DateTime field to indicate when this record has been read by project analysis process  */  
   "ProjProcessedDate":string,
      /**  PCLinkRemoved  */  
   "PCLinkRemoved":boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   "ExternalMESSyncRequired":boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   "ExternalMESLastSync":string,
      /**  Related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   "KBConfigProdID":number,
      /**  Indicates if this revision is to use Advanced Staging.  */  
   "UseAdvancedStaging":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  PersonIDName  */  
   "PersonIDName":string,
      /**  This flag indicates if the job is ready to be fulfilled.  */  
   "ReadyToFulfill":boolean,
      /**  FSMSendTo  */  
   "FSMSendTo":boolean,
      /**  FSMServiceReportID  */  
   "FSMServiceReportID":string,
   "AdvanceLaborRate":boolean,
      /**  Calculated field is set Not UnReadyCostProcess  */  
   "dspReadyCostProcess":boolean,
      /**  Determine if jobengineered is enabled or disabled.  */  
   "EnableJobEngineered":boolean,
      /**  Should JobFirm be enabled or disabled?  */  
   "EnableJobFirm":boolean,
      /**  Determine if jobreleased is enabled or disabled.  */  
   "EnableJobReleased":boolean,
   "EnableMaterialStatus":boolean,
   "EnableProject":boolean,
      /**  Is the job allowed to be engineered?  */  
   "EngineerAllowed":boolean,
   "EquipLocDesc":string,
      /**  If some fields except ToFirm have been updated  */  
   "ExtUpdated":boolean,
      /**   Final Operation – This is scheduled Due Date for either:
1.	Operation on ASM that has Final Operation checkbox selected
2.	If no Operation on ASM has Final Operation selected than use Last Operation on ASM  */  
   "FinalOpDueDate":string,
      /**  If it's Stocked assembly and PlanAsAsm is true.  */  
   "FirmProcEnable":boolean,
      /**  is used to select stocked Job which will be processed by Firming Process instead of Firm check-box. Is available only for .FirmProcEnable = true (in Job Status Maintenance).  */  
   "FirmProcess":boolean,
      /**  Job has at least one assembly with flag Plan as Assembly.  */  
   "HasPlanAsAsm":boolean,
      /**  Depending on the engineered job flag, is the header information enabled?  */  
   "HeaderSensitive":boolean,
      /**  It will allow displaying default of this value from Plant.IgnoreMtlConstraints  */  
   "IgnoreMtlConstraints":boolean,
   "JobTypeName":string,
      /**  If part is backflush the kit time is ignored.  */  
   "KitTime":number,
      /**  Locked Qty Flag  */  
   "LockedQty":boolean,
   "NewMeter":number,
      /**  The old Job Number when JobFirm is changed from no to yes.  */  
   "OldJobNum":string,
      /**  The order qty  */  
   "OrderQty":number,
      /**  Logical field signifying whether JobHead.PartNum is a valid part master part.  */  
   "PartmasterPart":boolean,
   "PhaseDescription":string,
      /**  Relative to Maintenance Jobs (JobType = "MNT") indicates if job is for "Preventive Maintenance".  This is a job that was created for a Equipment Maintenance Plan (JobHead.PlanNum > 0)  */  
   "PMJob":boolean,
      /**  Process Mode Description  */  
   "ProcessModeDescription":string,
      /**  Receive Time field for Job Part entered on Job  */  
   "ReceiveTime":number,
      /**  Original smart string passed in for configuration  */  
   "SmartString":string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   "SmartStringProcessed":boolean,
   "SOExists":boolean,
   "StockQty":number,
      /**  To be Firmed  */  
   "ToFirm":boolean,
      /**  Description for XRefPartType  */  
   "XRefPartTypeDesc":string,
      /**  The audit change description for the jobaudit record.  */  
   "ChangeDescription":string,
   "ClearDataset":boolean,
      /**  True if more than one co-part exists  */  
   "IsCoPart":boolean,
      /**  The identifier of related Process Manufacturing.  */  
   "PartRevProcessMfgID":string,
      /**  Type of Process Manufacturing.  */  
   "PartRevProcessMfgType":string,
      /**  Determines if the Service Job has to be synchronized with Epicor FSI application.  */  
   "SendToFSA":boolean,
   "BitFlag":number,
   "AnalysisCdDescription":string,
   "CallLineLineDesc":string,
   "DynAttrValueSetDescription":string,
   "DynAttrValueSetShortDescription":string,
   "EquipMeterUOM":string,
   "EquipSerialNum":string,
   "EquipLocID":string,
   "EquipPlant":string,
   "EquipDescription":string,
   "EquipBrand":string,
   "EquipModel":string,
   "EquipCurrentMeter":number,
   "EquipTypeID":string,
   "EquipOEM":string,
   "ExpenseCodeDescription":string,
   "HDCaseDescription":string,
   "IssueTopicID1Description":string,
   "IssueTopicID10Description":string,
   "IssueTopicID2Description":string,
   "IssueTopicID3Description":string,
   "IssueTopicID4Description":string,
   "IssueTopicID5Description":string,
   "IssueTopicID6Description":string,
   "IssueTopicID7Description":string,
   "IssueTopicID8Description":string,
   "IssueTopicID9Description":string,
   "PartNumSalesUM":string,
   "PartNumIUM":string,
   "PartNumTrackLots":boolean,
   "PartNumPartDescription":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumSellingFactor":number,
   "PartNumPricePerCode":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumLocationIDNumReq":boolean,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumAttrClassID":string,
   "PlantName":string,
   "PlantMaintPlant":string,
   "ProdCodeDescription":string,
   "ProdTeamIDDescription":string,
   "ProdTeamIDName":string,
   "ProjectIDDescription":string,
   "QuoteLineLineDesc":string,
   "QuoteNumCurrencyCode":string,
   "ResTopicID1Description":string,
   "ResTopicID10Description":string,
   "ResTopicID2Description":string,
   "ResTopicID3Description":string,
   "ResTopicID4Description":string,
   "ResTopicID5Description":string,
   "ResTopicID6Description":string,
   "ResTopicID7Description":string,
   "ResTopicID8Description":string,
   "ResTopicID9Description":string,
   "SchedCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
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
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ds
      @param ipSysRowID
   */  
export interface BuildMassIssueBrowse_input{
   ds:Erp_Tablesets_MassIssueInputTableset[],
      /**  SysRowID of the selected row.  */  
   ipSysRowID:string,
}

export interface BuildMassIssueBrowse_output{
   returnObj:Erp_Tablesets_MassIssueToMfgTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassIssueInputTableset,
   pcMessage:string,
}
}

   /** Required : 
      @param pcView
      @param ds
   */  
export interface ClearAll_input{
      /**  Input the filter shown in the browse.  Valid values are Open, Completed or All.  */  
   pcView:string,
   ds:Erp_Tablesets_MassIssueToMfgTableset[],
}

export interface ClearAll_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassIssueToMfgTableset,
}
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

export interface Erp_Tablesets_MassIssueInputJobRow{
   Company:string,
   JobNum:string,
   dummyKeyField:string,
      /**  Indicated if it's a return from mfg  */  
   IsReturn:boolean,
      /**  Warning Message if the Quantity completed on this Job was received or shipped  */  
   WarnMessage:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MassIssueInputListRow{
   Company:string,
   JobNum:string,
      /**  Indicated if it's a return from mfg  */  
   IsReturn:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MassIssueInputListTableset{
   MassIssueInputList:Erp_Tablesets_MassIssueInputListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MassIssueInputRow{
      /**  Transaction Date  */  
   TranDate:string,
      /**  Job Number  */  
   JobNum:string,
      /**  Job type  */  
   JobType:string,
      /**  Assembly Sequence  */  
   AssemblySeq:number,
      /**  Include Sub assemblies  */  
   IncludeSubassemblies:boolean,
      /**  Include Subassemblies' overrun quantity  */  
   IncludeSubassembliesOverrun:boolean,
      /**  Part Number Jobhead  */  
   PartNumJH:string,
      /**  Part Jobhead description  */  
   PartDescJH:string,
      /**  Call Number  */  
   CallNum:number,
      /**  Call Line  */  
   CallLine:number,
      /**  Part Number Assembly  */  
   PartNumAsm:string,
      /**  Part Assembly description  */  
   PartDescAsm:string,
      /**  Company indentifier  */  
   Company:string,
   JobDescJH:string,
   IUM:string,
   AssemblyQty:number,
      /**  Dummy key field.  It is the primary key of the dataset  */  
   dummyKeyfield:string,
   FSCallhdInvoiced:boolean,
   RequiredQty:number,
      /**  Set to true if the user chooses Include Subassembly and the record is part of the parent assembly  */  
   ReadOnly:boolean,
   PartNum:string,
   Description:string,
      /**  Return from Mfg  */  
   IsReturn:boolean,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum  */  
   RevisionNum:string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum  */  
   RevisionNumAsm:string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum  */  
   RevisionNumJH:string,
   SysRowID:string,
   PartTrackInventoryByRevision:boolean,
   PartSalesUM:string,
   PartTrackLots:boolean,
   PartPartDescription:string,
   PartIUM:string,
   PartPricePerCode:string,
   PartTrackSerialNum:boolean,
   PartTrackDimension:boolean,
   PartSellingFactor:number,
   PartAttrClassID:string,
   PartAsmTrackInventoryByRevision:boolean,
   PartAsmPartDescription:string,
   PartAsmPricePerCode:string,
   PartAsmTrackDimension:boolean,
   PartAsmSellingFactor:number,
   PartAsmTrackLots:boolean,
   PartAsmSalesUM:string,
   PartAsmTrackSerialNum:boolean,
   PartAsmIUM:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MassIssueInputTableset{
   MassIssueInputJob:Erp_Tablesets_MassIssueInputJobRow[],
   MassIssueInput:Erp_Tablesets_MassIssueInputRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MassIssueJobListTableset{
   JobHead:Erp_Tablesets_JobHeadRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MassIssueRow{
      /**  Assembly Sequence  */  
   AssemblySeq:number,
      /**  Sequence Number  */  
   SeqNum:number,
      /**  Parent  */  
   Parent:number,
      /**  Part Number  */  
   PartNum:string,
      /**  Revision Number  */  
   RevisionNum:string,
      /**  Part Description  */  
   Description:string,
      /**  Quantity Required  */  
   QtyRequired:number,
      /**  Qty Save Request  */  
   SaveReq:number,
      /**  Original JobMtl required Qty  */  
   QtyRequiredMtl:number,
      /**  Quantity Issued  */  
   QtyIssued:number,
      /**  Product Quantity  */  
   ProdQty:number,
      /**  Pull Quantity  */  
   PullQty:number,
      /**  Quantity Per  */  
   QtyPer:number,
      /**  Over run quantity  */  
   OverRunQty:number,
      /**  Build quantity  */  
   BuildQty:number,
      /**  Rem pull quantity  */  
   RemPullQty:number,
      /**  Estimated scrap type  */  
   EstScrapType:string,
      /**  Estimated scrap  */  
   EstScrap:number,
      /**  Fixed Quantity  */  
   FixedQty:boolean,
      /**  Ware house  */  
   Warehouse:string,
      /**  Bin number  */  
   BinNum:string,
      /**  To Ware house  */  
   ToWarehouse:string,
      /**  To Bin Number  */  
   ToBinNum:string,
      /**  Issued Complete  */  
   IssuedComplete:boolean,
      /**  CmpFlagOrig  */  
   CmpFlagOrig:boolean,
      /**  Job complete  */  
   JobComplete:boolean,
      /**  Previous issued  */  
   PrevIssued:number,
      /**  Save Issued  */  
   SaveIssued:number,
      /**  Dimension tracked ?  */  
   DimTrack:boolean,
      /**  Track lots ?  */  
   LotTrack:boolean,
      /**  Lot Number  */  
   LotNum:string,
      /**  Unit of measure  */  
   UnitMeasure:string,
      /**  Transaction type  */  
   TranType:string,
      /**  Transaction class  */  
   TranClass:string,
      /**  Transaction reference  */  
   TranReference:string,
      /**  Inventory transaction  */  
   InventoryTrans:boolean,
      /**  Transaction entered by  */  
   EntryPerson:string,
      /**  Cost method  */  
   CostMethod:string,
      /**  Material unit cost  */  
   MtlUnitCost:number,
      /**  Labor unit cost  */  
   LbrUnitCost:number,
      /**  Burden unit cost  */  
   BurUnitCost:number,
      /**  Subcontractor unit cost  */  
   SubUnitCost:number,
      /**  Material Burden Unit Cost  */  
   MtlBurUnitCost:number,
      /**  Is Part  */  
   IsPart:boolean,
      /**  Job Number  */  
   JobNum:string,
      /**  Transaction Date  */  
   TranDate:string,
      /**  Part Number Jobhead  */  
   PartNumJH:string,
      /**  Part Jobhead description  */  
   PartDescJH:string,
      /**  Part Number Assembly  */  
   PartNumAsm:string,
      /**  Part Assembly description  */  
   PartDescAsm:string,
      /**  Part Material sequence description  */  
   PartDescMS:string,
      /**  Part Number Material Sequence  */  
   PartNumMS:string,
      /**  Job type  */  
   JobType:string,
      /**  Call Number  */  
   CallNum:number,
      /**  Call Line  */  
   CallLine:number,
      /**  Include Sub assemblies  */  
   IncludeSubassemblies:boolean,
      /**  Include Subassemblies' overrun quantity  */  
   IncludeSubassembliesOverrun:boolean,
      /**  Company  */  
   Company:string,
   dummyKeyField:string,
   StopAction:string,
   StockQty:number,
      /**  Display value of StopAction.  */  
   DispStopAction:string,
      /**  For UI use only.  */  
   OKToIssue:boolean,
      /**  For UI Use only  */  
   JustQtyIssued:number,
   ActTransUOM:string,
   ThisTransaction:number,
   StockUOM:string,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
   PartTranPKs:string,
      /**  This is the manually entered legal number suffix entered by the user.  This column only contains data when the legal number assigned to the transaction document type is a manual enter legal number.  */  
   ManualNumberSuffix:string,
   RelatedOperSort:number,
   AbleToIssue:boolean,
      /**  Is Return from Mfg  */  
   IsReturn:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  This is the manually entered legal number prefix. This column only contains data when the legal number assigned to the transaction document type is a manual enter legal number.  */  
   ManualPrefix:string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
   SysRowID:string,
   BinNumDescription:string,
   PartAttrClassID:string,
   PartTrackInventoryAttributes:boolean,
   PartSellingFactor:number,
   PartPricePerCode:string,
   PartTrackLots:boolean,
   PartTrackDimension:boolean,
   PartSalesUM:string,
   PartIUM:string,
   PartPartDescription:string,
   PartTrackSerialNum:boolean,
   PartTrackInventoryByRevision:boolean,
   PartLotPartLotDescription:string,
   ToBinNumDescription:string,
   ToWarehouseDescription:string,
   WarehouseDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MassIssueToMfgTableset{
   MassIssue:Erp_Tablesets_MassIssueRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param sysTranTypeID
   */  
export interface GetAvailTranDocTypes_input{
      /**  System Transaction Document Type  */  
   sysTranTypeID:string,
}

export interface GetAvailTranDocTypes_output{
parameters : {
      /**  output parameters  */  
   availTypes:string,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListPaging_input{
      /**  Where condition without the where word  */  
   whereClause:string,
      /**  # of records returned.  0 means all  */  
   pageSize:number,
   absolutePage:number,
}

export interface GetListPaging_output{
   returnObj:Erp_Tablesets_MassIssueJobListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseSetupGrp
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  Where condition without the where word  */  
   whereClauseSetupGrp:string,
      /**  # of records returned.  0 means all  */  
   pageSize:number,
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_MassIssueJobListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param jobNum
      @param isReturn
   */  
export interface GetMassIssueInputForJob_input{
      /**  The job number  */  
   jobNum:string,
      /**  Is for return  */  
   isReturn:boolean,
}

export interface GetMassIssueInputForJob_output{
   returnObj:Erp_Tablesets_MassIssueInputTableset[],
}

   /** Required : 
      @param ds
      @param sysRowID
   */  
export interface GetMassIssueToMfg_input{
   ds:Erp_Tablesets_MassIssueInputTableset[],
      /**  SysRowID of the selected row  */  
   sysRowID:string,
}

export interface GetMassIssueToMfg_output{
   returnObj:Erp_Tablesets_MassIssueToMfgTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassIssueInputTableset,
   message:string,
}
}

   /** Required : 
      @param pcJobNum
      @param ds
      @param isReturn
   */  
export interface GetNewMassIssueInputJobNum_input{
      /**  Job number.  */  
   pcJobNum:string,
   ds:Erp_Tablesets_MassIssueInputTableset[],
      /**  Is Return from Mfg  */  
   isReturn:boolean,
}

export interface GetNewMassIssueInputJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassIssueInputTableset,
}
}

   /** Required : 
      @param ds
      @param isReturn
   */  
export interface GetNewMassIssueInputList_input{
   ds:Erp_Tablesets_MassIssueInputListTableset[],
      /**  Is Return from Mfg  */  
   isReturn:boolean,
}

export interface GetNewMassIssueInputList_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassIssueInputListTableset,
}
}

   /** Required : 
      @param ds
      @param isReturn
   */  
export interface GetNewMassIssueInputMultiple_input{
   ds:Erp_Tablesets_MassIssueInputListTableset[],
      /**  Is Return from Mfg  */  
   isReturn:boolean,
}

export interface GetNewMassIssueInputMultiple_output{
   returnObj:Erp_Tablesets_MassIssueInputTableset[],
}

   /** Required : 
      @param ds
      @param isReturn
   */  
export interface GetNewMassIssueInput_input{
   ds:Erp_Tablesets_MassIssueInputTableset[],
      /**  Is return to mfg  */  
   isReturn:boolean,
}

export interface GetNewMassIssueInput_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassIssueInputTableset,
}
}

   /** Required : 
      @param whereClauseSetupGrp
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
      /**  Where condition without the where word  */  
   whereClauseSetupGrp:string,
      /**  # of records returned.  0 means all  */  
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_MassIssueJobListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
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
      @param pcView
      @param ds
   */  
export interface IssueAll_input{
      /**  Input the filter shown in the browse.  Valid values are Open, Completed or All.  */  
   pcView:string,
   ds:Erp_Tablesets_MassIssueToMfgTableset[],
}

export interface IssueAll_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassIssueToMfgTableset,
}
}

   /** Required : 
      @param pcJobNum
      @param ds
   */  
export interface NegativeStockCheck_input{
      /**  Job# to which the Mass issue is to be done.  */  
   pcJobNum:string,
   ds:Erp_Tablesets_MassIssueToMfgTableset[],
}

export interface NegativeStockCheck_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassIssueToMfgTableset,
   pcQuestion:string,
   pcError:string,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeAssemblySeq_input{
   ds:Erp_Tablesets_MassIssueInputTableset[],
}

export interface OnChangeAssemblySeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassIssueInputTableset,
}
}

   /** Required : 
      @param pcWarehouse
      @param pcBinNum
      @param pcSysRowID
      @param ds
   */  
export interface OnChangeBinNumForSysRow_input{
      /**  Warehouse  */  
   pcWarehouse:string,
      /**  New Bin number which should be checked  */  
   pcBinNum:string,
      /**  Current SysRowID  */  
   pcSysRowID:string,
   ds:Erp_Tablesets_MassIssueToMfgTableset[],
}

export interface OnChangeBinNumForSysRow_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassIssueToMfgTableset,
}
}

   /** Required : 
      @param pcWarehouse
      @param pcPartNum
      @param pcBinNum
      @param ds
   */  
export interface OnChangeBinNum_input{
      /**  Warehouse  */  
   pcWarehouse:string,
      /**  Part number  */  
   pcPartNum:string,
      /**  New Bin number which should be checked  */  
   pcBinNum:string,
   ds:Erp_Tablesets_MassIssueToMfgTableset[],
}

export interface OnChangeBinNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassIssueToMfgTableset,
}
}

   /** Required : 
      @param pcJobNum
      @param ds
   */  
export interface OnChangeJobNum_input{
      /**  Job Number.  */  
   pcJobNum:string,
   ds:Erp_Tablesets_MassIssueInputTableset[],
}

export interface OnChangeJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassIssueInputTableset,
}
}

   /** Required : 
      @param plLotTrack
      @param pcLotNum
      @param plCreatePartLot
      @param sysRowID
      @param ds
   */  
export interface OnChangeLotNumForSysRowID_input{
      /**  Is the part lot tracked ?  */  
   plLotTrack:boolean,
      /**  Lot number  */  
   pcLotNum:string,
      /**  User's answer to the question - Do you want to create a lot number  */  
   plCreatePartLot:boolean,
      /**  Current SysRowID  */  
   sysRowID:string,
   ds:Erp_Tablesets_MassIssueToMfgTableset[],
}

export interface OnChangeLotNumForSysRowID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassIssueToMfgTableset,
}
}

   /** Required : 
      @param plLotTrack
      @param pcLotNum
      @param plCreatePartLot
      @param ds
   */  
export interface OnChangeLotNum_input{
      /**  Is the part lot tracked ?  */  
   plLotTrack:boolean,
      /**  Lot number  */  
   pcLotNum:string,
      /**  User's answer to the question - Do you want to create a lot number  */  
   plCreatePartLot:boolean,
   ds:Erp_Tablesets_MassIssueToMfgTableset[],
}

export interface OnChangeLotNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassIssueToMfgTableset,
}
}

   /** Required : 
      @param pcJobNum
      @param piAssemblySeq
      @param piSeqNum
      @param ds
   */  
export interface OnChangePartNum_input{
      /**  Job # to which the Mass Issue is done  */  
   pcJobNum:string,
      /**  Assembly#  */  
   piAssemblySeq:number,
      /**  Seq Number  */  
   piSeqNum:number,
   ds:Erp_Tablesets_MassIssueToMfgTableset[],
}

export interface OnChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassIssueToMfgTableset,
}
}

   /** Required : 
      @param piAssemblySeq
      @param piSeqNum
      @param pdQtyIssued
      @param pdAssemblyQty
      @param ds
   */  
export interface OnChangeQtyIssued_input{
      /**  Assembly#  */  
   piAssemblySeq:number,
      /**  Seq Number  */  
   piSeqNum:number,
      /**  Proposed Quantity Issued  */  
   pdQtyIssued:number,
      /**  Current Assembly Quantity  */  
   pdAssemblyQty:number,
   ds:Erp_Tablesets_MassIssueToMfgTableset[],
}

export interface OnChangeQtyIssued_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassIssueToMfgTableset,
   pcWarning:string,
}
}

   /** Required : 
      @param pcRowIdent
      @param pcUOM
      @param pdAssemblyQty
      @param ds
   */  
export interface OnChangeUOMCode_input{
      /**  RowIdent of the current record  */  
   pcRowIdent:string,
      /**  Proposed UOM  */  
   pcUOM:string,
      /**  Current Assembly Quantity  */  
   pdAssemblyQty:number,
   ds:Erp_Tablesets_MassIssueToMfgTableset[],
}

export interface OnChangeUOMCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassIssueToMfgTableset,
}
}

   /** Required : 
      @param pcWarehouse
      @param pcPartNum
      @param ds
   */  
export interface OnChangeWareHouse_input{
      /**  Ware house  */  
   pcWarehouse:string,
      /**  Part number  */  
   pcPartNum:string,
   ds:Erp_Tablesets_MassIssueToMfgTableset[],
}

export interface OnChangeWareHouse_output{
parameters : {
      /**  output parameters  */  
   pcWarning:string,
   ds:Erp_Tablesets_MassIssueToMfgTableset,
}
}

   /** Required : 
      @param dispNumberOfPieces
      @param piAssemblySeq
      @param piSeqNum
      @param ds
   */  
export interface OnChangingNumberOfPieces_input{
   dispNumberOfPieces:number,
      /**  Assembly#  */  
   piAssemblySeq:number,
      /**  Seq Number  */  
   piSeqNum:number,
   ds:Erp_Tablesets_MassIssueToMfgTableset[],
}

export interface OnChangingNumberOfPieces_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassIssueToMfgTableset,
}
}

   /** Required : 
      @param pcPartNum
   */  
export interface OnPartNumChanging_input{
      /**  PartNum  */  
   pcPartNum:string,
}

export interface OnPartNumChanging_output{
}

   /** Required : 
      @param pcJobNum
      @param pdtTranDate
      @param piCallNum
      @param plMaterialComplete
      @param plNegStockCheckContinue
      @param ds
      @param pcPartTranKeys
   */  
export interface PerformMassIssueReturn_input{
      /**  Job# to which the Mass issue is to be done.  */  
   pcJobNum:string,
      /**  Transaction Date  */  
   pdtTranDate:string,
      /**  Identifies the Service Call.  */  
   piCallNum:number,
      /**  Material complete? - Answer to the user question - Have all materials been issued for this Service Call?  */  
   plMaterialComplete:boolean,
      /**  The response to the question generated from NegativeStockCheck method.  */  
   plNegStockCheckContinue:boolean,
   ds:Erp_Tablesets_MassIssueToMfgTableset[],
      /**  List of keys of PartTran records created  */  
   pcPartTranKeys:string,
}

export interface PerformMassIssueReturn_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassIssueToMfgTableset,
   pcMessage:string,
   pcPartTranKeys:string,
}
}

   /** Required : 
      @param pcJobNum
      @param pdtTranDate
      @param piCallNum
      @param plMaterialComplete
      @param plNegStockCheckContinue
      @param ds
   */  
export interface PerformMassIssue_input{
      /**  Job# to which the Mass issue is to be done.  */  
   pcJobNum:string,
      /**  Transaction Date  */  
   pdtTranDate:string,
      /**  Identifies the Service Call.  */  
   piCallNum:number,
      /**  Material complete? - Answer to the user question - Have all materials been issued for this Service Call?  */  
   plMaterialComplete:boolean,
      /**  The response to the question generated from NegativeStockCheck method.  */  
   plNegStockCheckContinue:boolean,
   ds:Erp_Tablesets_MassIssueToMfgTableset[],
}

export interface PerformMassIssue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassIssueToMfgTableset,
   pcMessage:string,
}
}

   /** Required : 
      @param ds
      @param htPrePerform
   */  
export interface PrePerformMassIssueHT_input{
   ds:Erp_Tablesets_MassIssueToMfgTableset[],
      /**  RequiresUserInput results HashTable  */  
   htPrePerform:any,      //schema had no properties on an object.
}

export interface PrePerformMassIssueHT_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassIssueToMfgTableset,
   htPrePerform: UNKNOW TYPE(error 2338),
}
}

   /** Required : 
      @param pdtTranDate
      @param ipTranDocType
      @param ipSysTranType
   */  
export interface PrePerformMassIssueOneItem_input{
      /**  Transaction Date  */  
   pdtTranDate:string,
      /**  Transaction document type  */  
   ipTranDocType:string,
      /**  System Transaction document type  */  
   ipSysTranType:string,
}

export interface PrePerformMassIssueOneItem_output{
parameters : {
      /**  output parameters  */  
   RequiresUserInput:boolean,
}
}

   /** Required : 
      @param pdtTranDate
      @param ipTranDocType
      @param ipSysTranType
      @param ds
   */  
export interface PrePerformMassIssue_input{
      /**  Transaction Date  */  
   pdtTranDate:string,
      /**  Transaction document type  */  
   ipTranDocType:string,
      /**  System Transaction document type  */  
   ipSysTranType:string,
   ds:Erp_Tablesets_MassIssueToMfgTableset[],
}

export interface PrePerformMassIssue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassIssueToMfgTableset,
   RequiresUserInput:boolean,
}
}

