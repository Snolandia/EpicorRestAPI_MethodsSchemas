import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.JobPartSvc
// Description: Job part business object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/$metadata", {
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
   Summary: Calls GetRows for the service
   Description: Get JobParts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JobParts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobPartRow
   */  
export function get_JobParts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/JobParts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JobParts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JobPartRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.JobPartRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_JobParts(requestBody:Erp_Tablesets_JobPartRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/JobParts", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the JobPart item
   Description: Calls GetByID to retrieve the JobPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JobPart
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.JobPartRow
   */  
export function get_JobParts_Company_JobNum_PartNum(Company:string, JobNum:string, PartNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_JobPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/JobParts(" + Company + "," + JobNum + "," + PartNum + ")", {
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
         resolve(data as Erp_Tablesets_JobPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update JobPart for the service
   Description: Calls UpdateExt to update JobPart. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JobPart
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.JobPartRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_JobParts_Company_JobNum_PartNum(Company:string, JobNum:string, PartNum:string, requestBody:Erp_Tablesets_JobPartRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/JobParts(" + Company + "," + JobNum + "," + PartNum + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete JobPart item
   Description: Call UpdateExt to delete JobPart item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JobPart
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_JobParts_Company_JobNum_PartNum(Company:string, JobNum:string, PartNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/JobParts(" + Company + "," + JobNum + "," + PartNum + ")", {
          method: 'delete',
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobPartListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobPartListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobPartListRow)
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
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseJobPart:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseJobPart!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseJobPart=" + whereClauseJobPart
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/GetRows" + params, {
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
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(jobNum:string, partNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof jobNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "jobNum=" + jobNum
   }
   if(typeof partNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "partNum=" + partNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/GetByID" + params, {
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
         resolve(data as GetByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      @param whereClause Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
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

   return (new Promise<GetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/GetList" + params, {
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
   Summary: Invoke method GetNewJobPart
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJobPart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewJobPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewJobPart(requestBody:GetNewJobPart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewJobPart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/GetNewJobPart", {
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
         resolve(data as GetNewJobPart_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:DeleteByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/DeleteByID", {
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
         resolve(data as DeleteByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowID(id:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof id!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "id=" + id
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBySysRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/GetBySysRowID" + params, {
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
         resolve(data as GetBySysRowID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowIDs(ids:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof ids!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ids=" + ids
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBySysRowIDs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/GetBySysRowIDs" + params, {
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
         resolve(data as GetBySysRowIDs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:Update_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Update_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/Update", {
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
         resolve(data as Update_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:UpdateExt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateExt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/UpdateExt", {
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
         resolve(data as UpdateExt_output)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobPartListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JobPartListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobPartRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JobPartRow,
}

export interface Erp_Tablesets_JobPartListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Job Number. Used in tying record back to its parent JobHead record.  */  
   "JobNum":string,
      /**   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  */  
   "PartNum":string,
      /**  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**   Part Per Operation. Active only for Concurrent process
Jobs. Otherwise set to 1.  */  
   "PartsPerOp":number,
      /**   The number of individual parts that are being produced
part. Sum of all related JobProd.ProdQty.
Not Directly maintable.  */  
   "PartQty":number,
      /**  Part Qty that is being produced for Stock.  */  
   "StockQty":number,
      /**   Total Quantity of the end part shipped from this job.
Updated via the ShipDtl write triggers.  */  
   "ShippedQty":number,
      /**   Total quantity received to stock for the end part of the Job.
Updated via the Manufacturing receipts process.  */  
   "ReceivedQty":number,
      /**   Represents the "outstanding" WIP of production quantity.
A summary of JobProd.WIPQty, updated via JobProd write trigger.  */  
   "WIPQty":number,
      /**   Part Production quantity completed.
Updated via JobOper write trigger or LaborPart trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  */  
   "QtyCompleted":number,
      /**  Quantity of the job completed quantity that is "Reserved" for the linked demands (sales orders/other jobs). Summary of PartAlloc.ReservedQty where PartAlloc.SupplyJobNum = JobHead.JobNum.  Reservations for Orders are made via the Order Allocations program. They are excluded from available quantity calculations for the job. Available Quantity = JobHead.QtyCompleted - (Shipped + Received to stk + ReservedAllocQty + PickingQty + PickedQty).  Maintained via PartAlloc write trigger.  */  
   "ReservedQty":number,
      /**  Total Allocated Quantity for this job part  */  
   "AllocatedQty900":number,
      /**  Quantity of the job completed quantity that is considered as in the "Picking" process for the linked sales orders. Summary of PartAlloc.PickingQty where PartAlloc.SupplyJobNum = JobHead.JobNum. PickingQty is set in the Order Allocation program. Maintained via PartAlloc write trigger.  */  
   "PickingQty":number,
      /**  Quantity of the job completed quantity that is considered as in the shipping "Staging" process for the linked sales orders. Summary of PartAlloc.PickedQty where PartAlloc.SupplyJobNum = JobHead.JobNum. PickedQty is updated when the material move moves the item to the staging area.  Maintained via PartAlloc write trigger.  */  
   "PickedQty":number,
      /**   Defines an integer value which is used to calculate a
ratio for prorating the labor costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  */  
   "LbrCostBase":number,
      /**   Defines an integer value which is used to calculate a
ratio for prorating the material costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  */  
   "MtlCostBase":number,
      /**  Indicates if Job is closed.  Mirror image of JobHead.JobClosed. Duplicated for performance reasons  */  
   "JobClosed":boolean,
      /**  Indicates if production is complete for the job.   Mirror image of JobHead.JobClosed. Duplicated for performance reasons  */  
   "JobComplete":boolean,
      /**  Site Identifier.  Mirror image of JobHead.Site. Duplicated for performance reasons  */  
   "Plant":string,
      /**  Describes the Part.  */  
   "PartDescription":string,
      /**  Defines the Unit of Measure used when part is issued, this is also how it is stocked.  Use the value from XaSyst.UM as a default when creating new part records.  */  
   "IUM":string,
      /**   Shipping Documents Required.
Indicates if shipping documents are required when shipping this part from the Job. Pertains to Job Shipments only and only if the PartNum does not exist in the PartTable. If it does exist then the Part.ShipDocReq. If checked, then at the time of shipping the system will require that the JobPart.ShipDocsAvail flag is true before allowing the shipment.Requires DocManagement license.  */  
   "ShipDocReq":boolean,
      /**   Required Shipping Documents Available.
A flag manually set by the user to indicate that the required documents for the Job Part  are available. In order to set to Yes, at least one attachment having a DocType with Shipment = yes must exist for the Job Part.  If the Part.ShipDocReq = yes  then JobPart.ShipDocsA vail must = yes before the system will allow shipment of the Part from the job.Requires DocManagement license.  */  
   "ShipDocAvail":boolean,
      /**  List of materials that us this part as cost base  */  
   "MtlList":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "OrderQty":number,
      /**  The value of the JobHead.ProcessMode  */  
   "ProcessMode":string,
      /**  Indicates if ShipDocReq is enabled. Only if JobPart.PartNum does not exist in Part Table and if Document Management is installed.  */  
   "EnableShipDocReq":boolean,
      /**  Logical field signifying whether JobPart.PartNum is a valid part master part.  */  
   "PartmasterPart":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_JobPartRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Job Number. Used in tying record back to its parent JobHead record.  */  
   "JobNum":string,
      /**   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  */  
   "PartNum":string,
      /**  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**   Part Per Operation. Active only for Concurrent process
Jobs. Otherwise set to 1.  */  
   "PartsPerOp":number,
      /**   The number of individual parts that are being produced
part. Sum of all related JobProd.ProdQty.
Not Directly maintable.  */  
   "PartQty":number,
      /**  Part Qty that is being produced for Stock.  */  
   "StockQty":number,
      /**   Total Quantity of the end part shipped from this job.
Updated via the ShipDtl write triggers.  */  
   "ShippedQty":number,
      /**   Total quantity received to stock for the end part of the Job.
Updated via the Manufacturing receipts process.  */  
   "ReceivedQty":number,
      /**   Represents the "outstanding" WIP of production quantity.
A summary of JobProd.WIPQty, updated via JobProd write trigger.  */  
   "WIPQty":number,
      /**   Part Production quantity completed.
Updated via JobOper write trigger or LaborPart trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  */  
   "QtyCompleted":number,
      /**  Quantity of the job completed quantity that is "Reserved" for the linked demands (sales orders/other jobs). Summary of PartAlloc.ReservedQty where PartAlloc.SupplyJobNum = JobHead.JobNum.  Reservations for Orders are made via the Order Allocations program. They are excluded from available quantity calculations for the job. Available Quantity = JobHead.QtyCompleted - (Shipped + Received to stk + ReservedAllocQty + PickingQty + PickedQty).  Maintained via PartAlloc write trigger.  */  
   "ReservedQty":number,
      /**  Total Allocated Quantity for this job part  */  
   "AllocatedQty900":number,
      /**  Quantity of the job completed quantity that is considered as in the "Picking" process for the linked sales orders. Summary of PartAlloc.PickingQty where PartAlloc.SupplyJobNum = JobHead.JobNum. PickingQty is set in the Order Allocation program. Maintained via PartAlloc write trigger.  */  
   "PickingQty":number,
      /**  Quantity of the job completed quantity that is considered as in the shipping "Staging" process for the linked sales orders. Summary of PartAlloc.PickedQty where PartAlloc.SupplyJobNum = JobHead.JobNum. PickedQty is updated when the material move moves the item to the staging area.  Maintained via PartAlloc write trigger.  */  
   "PickedQty":number,
      /**   Defines an integer value which is used to calculate a
ratio for prorating the labor costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  */  
   "LbrCostBase":number,
      /**   Defines an integer value which is used to calculate a
ratio for prorating the material costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  */  
   "MtlCostBase":number,
      /**  Indicates if Job is closed.  Mirror image of JobHead.JobClosed. Duplicated for performance reasons  */  
   "JobClosed":boolean,
      /**  Indicates if production is complete for the job.   Mirror image of JobHead.JobClosed. Duplicated for performance reasons  */  
   "JobComplete":boolean,
      /**  Site Identifier.  Mirror image of JobHead.Site. Duplicated for performance reasons  */  
   "Plant":string,
      /**  Describes the Part.  */  
   "PartDescription":string,
      /**  Defines the Unit of Measure used when part is issued, this is also how it is stocked.  Use the value from XaSyst.UM as a default when creating new part records.  */  
   "IUM":string,
      /**   Shipping Documents Required.
Indicates if shipping documents are required when shipping this part from the Job. Pertains to Job Shipments only and only if the PartNum does not exist in the PartTable. If it does exist then the Part.ShipDocReq. If checked, then at the time of shipping the system will require that the JobPart.ShipDocsAvail flag is true before allowing the shipment.Requires DocManagement license.  */  
   "ShipDocReq":boolean,
      /**   Required Shipping Documents Available.
A flag manually set by the user to indicate that the required documents for the Job Part  are available. In order to set to Yes, at least one attachment having a DocType with Shipment = yes must exist for the Job Part.  If the Part.ShipDocReq = yes  then JobPart.ShipDocsA vail must = yes before the system will allow shipment of the Part from the job.Requires DocManagement license.  */  
   "ShipDocAvail":boolean,
      /**  List of materials that us this part as cost base  */  
   "MtlList":string,
      /**  Indicates that MRP should not create job suggestions for the specified co-part  */  
   "PreventSugg":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
   "OrderQty":number,
      /**  The value of the JobHead.ProcessMode  */  
   "ProcessMode":string,
      /**  Indicates if ShipDocReq is enabled. Only if JobPart.PartNum does not exist in Part Table and if Document Management is installed.  */  
   "EnableShipDocReq":boolean,
      /**  Logical field signifying whether JobPart.PartNum is a valid part master part.  */  
   "PartmasterPart":boolean,
   "EnableSugg":boolean,
   "BitFlag":number,
   "DynAttrValueSetDescription":string,
   "DynAttrValueSetShortDescription":string,
   "PartTrackDimension":boolean,
   "PartPricePerCode":string,
   "PartTrackInventoryByRevision":boolean,
   "PartAttrClassID":string,
   "PartPartDescription":string,
   "PartTrackLots":boolean,
   "PartIUM":string,
   "PartSellingFactor":number,
   "PartSalesUM":string,
   "PartTrackInventoryAttributes":boolean,
   "PartTrackSerialNum":boolean,
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
      @param jobNum
      @param partNum
   */  
export interface DeleteByID_input{
   jobNum:string,
   partNum:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_JobPartListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Job Number. Used in tying record back to its parent JobHead record.  */  
   JobNum:string,
      /**   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  */  
   PartNum:string,
      /**  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**   Part Per Operation. Active only for Concurrent process
Jobs. Otherwise set to 1.  */  
   PartsPerOp:number,
      /**   The number of individual parts that are being produced
part. Sum of all related JobProd.ProdQty.
Not Directly maintable.  */  
   PartQty:number,
      /**  Part Qty that is being produced for Stock.  */  
   StockQty:number,
      /**   Total Quantity of the end part shipped from this job.
Updated via the ShipDtl write triggers.  */  
   ShippedQty:number,
      /**   Total quantity received to stock for the end part of the Job.
Updated via the Manufacturing receipts process.  */  
   ReceivedQty:number,
      /**   Represents the "outstanding" WIP of production quantity.
A summary of JobProd.WIPQty, updated via JobProd write trigger.  */  
   WIPQty:number,
      /**   Part Production quantity completed.
Updated via JobOper write trigger or LaborPart trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  */  
   QtyCompleted:number,
      /**  Quantity of the job completed quantity that is "Reserved" for the linked demands (sales orders/other jobs). Summary of PartAlloc.ReservedQty where PartAlloc.SupplyJobNum = JobHead.JobNum.  Reservations for Orders are made via the Order Allocations program. They are excluded from available quantity calculations for the job. Available Quantity = JobHead.QtyCompleted - (Shipped + Received to stk + ReservedAllocQty + PickingQty + PickedQty).  Maintained via PartAlloc write trigger.  */  
   ReservedQty:number,
      /**  Total Allocated Quantity for this job part  */  
   AllocatedQty900:number,
      /**  Quantity of the job completed quantity that is considered as in the "Picking" process for the linked sales orders. Summary of PartAlloc.PickingQty where PartAlloc.SupplyJobNum = JobHead.JobNum. PickingQty is set in the Order Allocation program. Maintained via PartAlloc write trigger.  */  
   PickingQty:number,
      /**  Quantity of the job completed quantity that is considered as in the shipping "Staging" process for the linked sales orders. Summary of PartAlloc.PickedQty where PartAlloc.SupplyJobNum = JobHead.JobNum. PickedQty is updated when the material move moves the item to the staging area.  Maintained via PartAlloc write trigger.  */  
   PickedQty:number,
      /**   Defines an integer value which is used to calculate a
ratio for prorating the labor costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  */  
   LbrCostBase:number,
      /**   Defines an integer value which is used to calculate a
ratio for prorating the material costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  */  
   MtlCostBase:number,
      /**  Indicates if Job is closed.  Mirror image of JobHead.JobClosed. Duplicated for performance reasons  */  
   JobClosed:boolean,
      /**  Indicates if production is complete for the job.   Mirror image of JobHead.JobClosed. Duplicated for performance reasons  */  
   JobComplete:boolean,
      /**  Site Identifier.  Mirror image of JobHead.Site. Duplicated for performance reasons  */  
   Plant:string,
      /**  Describes the Part.  */  
   PartDescription:string,
      /**  Defines the Unit of Measure used when part is issued, this is also how it is stocked.  Use the value from XaSyst.UM as a default when creating new part records.  */  
   IUM:string,
      /**   Shipping Documents Required.
Indicates if shipping documents are required when shipping this part from the Job. Pertains to Job Shipments only and only if the PartNum does not exist in the PartTable. If it does exist then the Part.ShipDocReq. If checked, then at the time of shipping the system will require that the JobPart.ShipDocsAvail flag is true before allowing the shipment.Requires DocManagement license.  */  
   ShipDocReq:boolean,
      /**   Required Shipping Documents Available.
A flag manually set by the user to indicate that the required documents for the Job Part  are available. In order to set to Yes, at least one attachment having a DocType with Shipment = yes must exist for the Job Part.  If the Part.ShipDocReq = yes  then JobPart.ShipDocsA vail must = yes before the system will allow shipment of the Part from the job.Requires DocManagement license.  */  
   ShipDocAvail:boolean,
      /**  List of materials that us this part as cost base  */  
   MtlList:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   OrderQty:number,
      /**  The value of the JobHead.ProcessMode  */  
   ProcessMode:string,
      /**  Indicates if ShipDocReq is enabled. Only if JobPart.PartNum does not exist in Part Table and if Document Management is installed.  */  
   EnableShipDocReq:boolean,
      /**  Logical field signifying whether JobPart.PartNum is a valid part master part.  */  
   PartmasterPart:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobPartListTableset{
   JobPartList:Erp_Tablesets_JobPartListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_JobPartRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Job Number. Used in tying record back to its parent JobHead record.  */  
   JobNum:string,
      /**   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  */  
   PartNum:string,
      /**  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**   Part Per Operation. Active only for Concurrent process
Jobs. Otherwise set to 1.  */  
   PartsPerOp:number,
      /**   The number of individual parts that are being produced
part. Sum of all related JobProd.ProdQty.
Not Directly maintable.  */  
   PartQty:number,
      /**  Part Qty that is being produced for Stock.  */  
   StockQty:number,
      /**   Total Quantity of the end part shipped from this job.
Updated via the ShipDtl write triggers.  */  
   ShippedQty:number,
      /**   Total quantity received to stock for the end part of the Job.
Updated via the Manufacturing receipts process.  */  
   ReceivedQty:number,
      /**   Represents the "outstanding" WIP of production quantity.
A summary of JobProd.WIPQty, updated via JobProd write trigger.  */  
   WIPQty:number,
      /**   Part Production quantity completed.
Updated via JobOper write trigger or LaborPart trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  */  
   QtyCompleted:number,
      /**  Quantity of the job completed quantity that is "Reserved" for the linked demands (sales orders/other jobs). Summary of PartAlloc.ReservedQty where PartAlloc.SupplyJobNum = JobHead.JobNum.  Reservations for Orders are made via the Order Allocations program. They are excluded from available quantity calculations for the job. Available Quantity = JobHead.QtyCompleted - (Shipped + Received to stk + ReservedAllocQty + PickingQty + PickedQty).  Maintained via PartAlloc write trigger.  */  
   ReservedQty:number,
      /**  Total Allocated Quantity for this job part  */  
   AllocatedQty900:number,
      /**  Quantity of the job completed quantity that is considered as in the "Picking" process for the linked sales orders. Summary of PartAlloc.PickingQty where PartAlloc.SupplyJobNum = JobHead.JobNum. PickingQty is set in the Order Allocation program. Maintained via PartAlloc write trigger.  */  
   PickingQty:number,
      /**  Quantity of the job completed quantity that is considered as in the shipping "Staging" process for the linked sales orders. Summary of PartAlloc.PickedQty where PartAlloc.SupplyJobNum = JobHead.JobNum. PickedQty is updated when the material move moves the item to the staging area.  Maintained via PartAlloc write trigger.  */  
   PickedQty:number,
      /**   Defines an integer value which is used to calculate a
ratio for prorating the labor costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  */  
   LbrCostBase:number,
      /**   Defines an integer value which is used to calculate a
ratio for prorating the material costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  */  
   MtlCostBase:number,
      /**  Indicates if Job is closed.  Mirror image of JobHead.JobClosed. Duplicated for performance reasons  */  
   JobClosed:boolean,
      /**  Indicates if production is complete for the job.   Mirror image of JobHead.JobClosed. Duplicated for performance reasons  */  
   JobComplete:boolean,
      /**  Site Identifier.  Mirror image of JobHead.Site. Duplicated for performance reasons  */  
   Plant:string,
      /**  Describes the Part.  */  
   PartDescription:string,
      /**  Defines the Unit of Measure used when part is issued, this is also how it is stocked.  Use the value from XaSyst.UM as a default when creating new part records.  */  
   IUM:string,
      /**   Shipping Documents Required.
Indicates if shipping documents are required when shipping this part from the Job. Pertains to Job Shipments only and only if the PartNum does not exist in the PartTable. If it does exist then the Part.ShipDocReq. If checked, then at the time of shipping the system will require that the JobPart.ShipDocsAvail flag is true before allowing the shipment.Requires DocManagement license.  */  
   ShipDocReq:boolean,
      /**   Required Shipping Documents Available.
A flag manually set by the user to indicate that the required documents for the Job Part  are available. In order to set to Yes, at least one attachment having a DocType with Shipment = yes must exist for the Job Part.  If the Part.ShipDocReq = yes  then JobPart.ShipDocsA vail must = yes before the system will allow shipment of the Part from the job.Requires DocManagement license.  */  
   ShipDocAvail:boolean,
      /**  List of materials that us this part as cost base  */  
   MtlList:string,
      /**  Indicates that MRP should not create job suggestions for the specified co-part  */  
   PreventSugg:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   OrderQty:number,
      /**  The value of the JobHead.ProcessMode  */  
   ProcessMode:string,
      /**  Indicates if ShipDocReq is enabled. Only if JobPart.PartNum does not exist in Part Table and if Document Management is installed.  */  
   EnableShipDocReq:boolean,
      /**  Logical field signifying whether JobPart.PartNum is a valid part master part.  */  
   PartmasterPart:boolean,
   EnableSugg:boolean,
   BitFlag:number,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
   PartTrackDimension:boolean,
   PartPricePerCode:string,
   PartTrackInventoryByRevision:boolean,
   PartAttrClassID:string,
   PartPartDescription:string,
   PartTrackLots:boolean,
   PartIUM:string,
   PartSellingFactor:number,
   PartSalesUM:string,
   PartTrackInventoryAttributes:boolean,
   PartTrackSerialNum:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobPartTableset{
   JobPart:Erp_Tablesets_JobPartRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtJobPartTableset{
   JobPart:Erp_Tablesets_JobPartRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param jobNum
      @param partNum
   */  
export interface GetByID_input{
   jobNum:string,
   partNum:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_JobPartTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_JobPartTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_JobPartTableset[],
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_JobPartListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param jobNum
   */  
export interface GetNewJobPart_input{
   ds:Erp_Tablesets_JobPartTableset[],
   jobNum:string,
}

export interface GetNewJobPart_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobPartTableset,
}
}

   /** Required : 
      @param whereClauseJobPart
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseJobPart:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_JobPartTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface Ice_BOUpdErrorRow{
   TableName:string,
   ErrorLevel:string,
   ErrorType:string,
   ErrorText:string,
   ErrorSysRowID:string,
   SysRowID:string,
   RowMod:string,
}

export interface Ice_BOUpdErrorTableset{
   BOUpdError:Ice_BOUpdErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtJobPartTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtJobPartTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_JobPartTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobPartTableset,
}
}

