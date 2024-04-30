import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PlanningWBSvc
// Description: Service for Planning Work Bench.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/$metadata", {
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
   Description: Get PlanningWBs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlanningWBs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartSugRow
   */  
export function get_PlanningWBs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSugRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/PlanningWBs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSugRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlanningWBs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartSugRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PartSugRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlanningWBs(requestBody:Erp_Tablesets_PartSugRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/PlanningWBs", {
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
   Summary: Calls GetByID to retrieve the PlanningWB item
   Description: Calls GetByID to retrieve the PlanningWB item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlanningWB
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PartSugRow
   */  
export function get_PlanningWBs_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartSugRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/PlanningWBs(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_PartSugRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PlanningWB for the service
   Description: Calls UpdateExt to update PlanningWB. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlanningWB
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartSugRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PlanningWBs_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_PartSugRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/PlanningWBs(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete PlanningWB item
   Description: Call UpdateExt to delete PlanningWB item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlanningWB
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PlanningWBs_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/PlanningWBs(" + SysRowID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartSugListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSugListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSugListRow)
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
export function get_GetRows(whereClausePartSug:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePartSug!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartSug=" + whereClausePartSug
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/GetRows" + params, {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(sysRowID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof sysRowID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "sysRowID=" + sysRowID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/GetList" + params, {
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
   Summary: Invoke method CreateJobFromPWB
   Description: This method will create jobs from pwb
   OperationID: CreateJobFromPWB
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateJobFromPWB_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateJobFromPWB_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateJobFromPWB(requestBody:CreateJobFromPWB_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateJobFromPWB_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/CreateJobFromPWB", {
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
         resolve(data as CreateJobFromPWB_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPartSug
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartSug
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPartSug_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartSug_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartSug(requestBody:GetNewPartSug_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPartSug_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/GetNewPartSug", {
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
         resolve(data as GetNewPartSug_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSugListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartSugListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSugRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartSugRow,
}

export interface Erp_Tablesets_PartSugListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Suggestions fall into two classes.
"MFG" = Suggestion pertains to manufacturing 
"PUR" = Suggestion pertains to purchasing.
Used to keep Mfg and Purchase suggestions separate.  */  
   "Classifier":string,
      /**  New Requirement.  Used to filter between New and Changes.  */  
   "NewFlag":boolean,
      /**  Suggestions can be;  "New" , "Can", "Dat", "Qty",  "Chg", "Cfg"  */  
   "Type":string,
      /**   Suggested action to be taken for this Purchase Order release.
"X" = Expedite, "P" = Postpone,  "C" = Cancel, R = Reduce Qty.  */  
   "SubType":string,
      /**  Part Number  */  
   "PartNum":string,
      /**  Job Number. Think of this as the Job that the suggestion is for ("target job")  */  
   "TargetJobNum":string,
      /**  Job Assembly Sequence.  The assembly that the suggestion is for ("target assembly").  This can occur when an assembly has a PullQuantity that is marked "Make Direct."  */  
   "TargetAssemblySeq":number,
      /**  Job Material Sequence.  The material that the suggestion is for ("target material").  This can occur when the material is marked as "Make Direct."  */  
   "TargetMtlSeq":number,
      /**  Indicates the source of the requirement that suggestion is related to; "Order", "Stock" or "Job".  */  
   "Source":string,
      /**  Job Number  */  
   "JobNum":string,
      /**  Assembly Sequence  */  
   "AssemblySeq":number,
      /**  Qualifies the JobSeq field as to be a "M" - Material (JobMtl) record or "S" - Subcontract (JobOper) reference.  */  
   "JobSeqType":string,
      /**  Seq # of specific material or subcontract operation record.  */  
   "JobSeq":number,
      /**  Related sales order number. For build to stock demands the OrderNum, OrderLine and OrderRel fields are all zero  */  
   "OrderNum":number,
      /**  Related Sales order line number.  */  
   "OrderLine":number,
      /**  Related sales order release number.  */  
   "OrderRelNum":number,
      /**   Inventory warehouse that job is producing for.
Only relevant for build to stock demands (ordernum = 0). In this case a valid Part must be referenced.  */  
   "WarehouseCode":string,
      /**   Due date of the related requirement record.
OrderRel.ReqDate.....  */  
   "DueDate":string,
      /**  Suggested due date to change meet the requirement.  */  
   "SugDate":string,
      /**  Suggested quantity.  */  
   "SugQty":number,
      /**  Unit of Measure that qualifies SugQty.  */  
   "SugQtyUOM":string,
      /**  Suggested change to Revision Number.  */  
   "SugRevisionNum":string,
      /**   Description of the proposed suggestion.
Ex: Change Job Due date to xx/xx/xx.  */  
   "Description":string,
      /**  1st 8 characters of customer name. Used for sorting suggestions  */  
   "CustShortName":string,
      /**  Duplicated from the customer.custid. Used for sorting purposes.  */  
   "CustID":string,
      /**  Purchase order that suggestion is for.  */  
   "PONum":number,
      /**  The line # of  PoDetail record suggestion is for.  */  
   "POLine":number,
      /**  Purchase order release number that suggestion if for.  */  
   "PORelNum":number,
      /**  The ID of the Planner. Used to filter suggestions.  */  
   "PlannerID":string,
      /**  A duplicate of "OrderRel.FirmRelease".  This only pertains to suggestions related to OrderRel.  Used to filter suggestions.  */  
   "FirmRelease":boolean,
      /**   Indicates if this suggestion affects stock.
Only the MRP Process creates StockTrans = Yes.  Various DB triggers and MRP create StockTrans = No (direct buy/mfg)  */  
   "StockTrans":boolean,
      /**  Site Identifier for this manufacturing suggestion.  */  
   "Plant":string,
      /**  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  */  
   "SugNum":number,
      /**  This is the unique key for the TFOrdDtl table.  */  
   "TFLineNum":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "Planner":string,
   "SugSource":string,
      /**  An error message description.  Used initially when creating a job.  */  
   "ErrorMsg":string,
   "CustFullName":string,
   "WarehouseDescription":string,
   "UOM":string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   "AssemblySeqDescription":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "OrderLineLineDesc":string,
      /**  A unique code that identifies the currency.  */  
   "OrderNumCurrencyCode":string,
      /**  The member's name on the credit card.  */  
   "OrderNumCardMemberName":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartNumSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartNumTrackLots":boolean,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartNumSellingFactor":number,
      /**  Indicates if this part is serial number tracked  */  
   "PartNumTrackSerialNum":boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   "POLineLineDesc":string,
      /**  OUR internal Part number for this item.  */  
   "POLinePartNum":string,
      /**  Supplier Part Number  */  
   "POLineVenPartNum":string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   "PORelNumRefCodeDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartSugRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Suggestions fall into two classes.
"MFG" = Suggestion pertains to manufacturing 
"PUR" = Suggestion pertains to purchasing.
Used to keep Mfg and Purchase suggestions separate.  */  
   "Classifier":string,
      /**  New Requirement.  Used to filter between New and Changes.  */  
   "NewFlag":boolean,
      /**  Suggestions can be;  "New" , "Can", "Dat", "Qty",  "Chg", "Cfg"  */  
   "Type":string,
      /**   Suggested action to be taken for this Purchase Order release.
"X" = Expedite, "P" = Postpone,  "C" = Cancel, R = Reduce Qty.  */  
   "SubType":string,
      /**  Part Number  */  
   "PartNum":string,
      /**  Job Number. Think of this as the Job that the suggestion is for ("target job")  */  
   "TargetJobNum":string,
      /**  Job Assembly Sequence.  The assembly that the suggestion is for ("target assembly").  This can occur when an assembly has a PullQuantity that is marked "Make Direct."  */  
   "TargetAssemblySeq":number,
      /**  Job Material Sequence.  The material that the suggestion is for ("target material").  This can occur when the material is marked as "Make Direct."  */  
   "TargetMtlSeq":number,
      /**  Indicates the source of the requirement that suggestion is related to; "Order", "Stock" or "Job".  */  
   "Source":string,
      /**  Job Number  */  
   "JobNum":string,
      /**  Assembly Sequence  */  
   "AssemblySeq":number,
      /**  Qualifies the JobSeq field as to be a "M" - Material (JobMtl) record or "S" - Subcontract (JobOper) reference.  */  
   "JobSeqType":string,
      /**  Seq # of specific material or subcontract operation record.  */  
   "JobSeq":number,
      /**  Related sales order number. For build to stock demands the OrderNum, OrderLine and OrderRel fields are all zero  */  
   "OrderNum":number,
      /**  Related Sales order line number.  */  
   "OrderLine":number,
      /**  Related sales order release number.  */  
   "OrderRelNum":number,
      /**   Inventory warehouse that job is producing for.
Only relevant for build to stock demands (ordernum = 0). In this case a valid Part must be referenced.  */  
   "WarehouseCode":string,
      /**   Due date of the related requirement record.
OrderRel.ReqDate.....  */  
   "DueDate":string,
      /**  Suggested due date to change meet the requirement.  */  
   "SugDate":string,
      /**  Suggested quantity.  */  
   "SugQty":number,
      /**  Unit of Measure that qualifies SugQty.  */  
   "SugQtyUOM":string,
      /**  Suggested change to Revision Number.  */  
   "SugRevisionNum":string,
      /**   Description of the proposed suggestion.
Ex: Change Job Due date to xx/xx/xx.  */  
   "Description":string,
      /**  1st 8 characters of customer name. Used for sorting suggestions  */  
   "CustShortName":string,
      /**  Duplicated from the customer.custid. Used for sorting purposes.  */  
   "CustID":string,
      /**  Purchase order that suggestion is for.  */  
   "PONum":number,
      /**  The line # of  PoDetail record suggestion is for.  */  
   "POLine":number,
      /**  Purchase order release number that suggestion if for.  */  
   "PORelNum":number,
      /**  The ID of the Planner. Used to filter suggestions.  */  
   "PlannerID":string,
      /**  A duplicate of "OrderRel.FirmRelease".  This only pertains to suggestions related to OrderRel.  Used to filter suggestions.  */  
   "FirmRelease":boolean,
      /**   Indicates if this suggestion affects stock.
Only the MRP Process creates StockTrans = Yes.  Various DB triggers and MRP create StockTrans = No (direct buy/mfg)  */  
   "StockTrans":boolean,
      /**  Site Identifier for this manufacturing suggestion.  */  
   "Plant":string,
      /**  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  */  
   "SugNum":number,
      /**  This is the unique key for the TFOrdDtl table.  */  
   "TFLineNum":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ContractID  */  
   "ContractID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Planning number of pieces for this attribute set.  */  
   "PlanningNumberOfPieces":number,
      /**  Date and time when this record was created.  */  
   "CreatedOn":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
   "CustFullName":string,
      /**  An error message description.  Used initially when creating a job.  */  
   "ErrorMsg":string,
   "JobInProcess":boolean,
   "Planner":string,
   "SugSource":string,
   "UOM":string,
   "WarehouseDescription":string,
      /**  Used for selecting record on landing page grid for Kinetic version.  */  
   "SelectedPartSug":boolean,
   "BitFlag":number,
   "AssemblySeqDescription":string,
   "DynAttrValueSetDescription":string,
   "DynAttrValueSetShortDescription":string,
   "JobNumReqDueDate":string,
   "JobNumStartDate":string,
   "OrderLineLineDesc":string,
   "OrderNumCardMemberName":string,
   "OrderNumCurrencyCode":string,
   "PartNumSellingFactor":number,
   "PartNumIUM":string,
   "PartNumSalesUM":string,
   "PartNumPricePerCode":string,
   "PartNumTrackDimension":boolean,
   "PartNumPartDescription":string,
   "PartNumTrackLots":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumAttrClassID":string,
   "POLinePartNum":string,
   "POLineLineDesc":string,
   "POLineVenPartNum":string,
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
      @param ipNewJobNum
      @param ipMessageResponseFlag
      @param ipGetDetails
      @param ipScheduleAll
      @param ipReleaseAll
      @param ipTravelerReadyToPrint
      @param ipBackground
   */  
export interface CreateJobFromPWB_input{
   ds:Erp_Tablesets_PlanningWBTableset[],
      /**  New Job Number  */  
   ipNewJobNum:string,
      /**  Did user respond to any messages regarding the parts to process?  */  
   ipMessageResponseFlag:boolean,
      /**  Get Details flag  */  
   ipGetDetails:boolean,
      /**  Schedule All flag  */  
   ipScheduleAll:boolean,
      /**  Release All flag  */  
   ipReleaseAll:boolean,
      /**  TravelerReadyToPrint/MassPrint flag  */  
   ipTravelerReadyToPrint:boolean,
      /**  Process jobs in the background/more than one job flag  */  
   ipBackground:boolean,
}

export interface CreateJobFromPWB_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlanningWBTableset,
   opCreatedJobNum:string,
   opErrMsg:string,
   opPartQuantityMessage:string,
}
}

   /** Required : 
      @param sysRowID
   */  
export interface DeleteByID_input{
   sysRowID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PartSugListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Suggestions fall into two classes.
"MFG" = Suggestion pertains to manufacturing 
"PUR" = Suggestion pertains to purchasing.
Used to keep Mfg and Purchase suggestions separate.  */  
   Classifier:string,
      /**  New Requirement.  Used to filter between New and Changes.  */  
   NewFlag:boolean,
      /**  Suggestions can be;  "New" , "Can", "Dat", "Qty",  "Chg", "Cfg"  */  
   Type:string,
      /**   Suggested action to be taken for this Purchase Order release.
"X" = Expedite, "P" = Postpone,  "C" = Cancel, R = Reduce Qty.  */  
   SubType:string,
      /**  Part Number  */  
   PartNum:string,
      /**  Job Number. Think of this as the Job that the suggestion is for ("target job")  */  
   TargetJobNum:string,
      /**  Job Assembly Sequence.  The assembly that the suggestion is for ("target assembly").  This can occur when an assembly has a PullQuantity that is marked "Make Direct."  */  
   TargetAssemblySeq:number,
      /**  Job Material Sequence.  The material that the suggestion is for ("target material").  This can occur when the material is marked as "Make Direct."  */  
   TargetMtlSeq:number,
      /**  Indicates the source of the requirement that suggestion is related to; "Order", "Stock" or "Job".  */  
   Source:string,
      /**  Job Number  */  
   JobNum:string,
      /**  Assembly Sequence  */  
   AssemblySeq:number,
      /**  Qualifies the JobSeq field as to be a "M" - Material (JobMtl) record or "S" - Subcontract (JobOper) reference.  */  
   JobSeqType:string,
      /**  Seq # of specific material or subcontract operation record.  */  
   JobSeq:number,
      /**  Related sales order number. For build to stock demands the OrderNum, OrderLine and OrderRel fields are all zero  */  
   OrderNum:number,
      /**  Related Sales order line number.  */  
   OrderLine:number,
      /**  Related sales order release number.  */  
   OrderRelNum:number,
      /**   Inventory warehouse that job is producing for.
Only relevant for build to stock demands (ordernum = 0). In this case a valid Part must be referenced.  */  
   WarehouseCode:string,
      /**   Due date of the related requirement record.
OrderRel.ReqDate.....  */  
   DueDate:string,
      /**  Suggested due date to change meet the requirement.  */  
   SugDate:string,
      /**  Suggested quantity.  */  
   SugQty:number,
      /**  Unit of Measure that qualifies SugQty.  */  
   SugQtyUOM:string,
      /**  Suggested change to Revision Number.  */  
   SugRevisionNum:string,
      /**   Description of the proposed suggestion.
Ex: Change Job Due date to xx/xx/xx.  */  
   Description:string,
      /**  1st 8 characters of customer name. Used for sorting suggestions  */  
   CustShortName:string,
      /**  Duplicated from the customer.custid. Used for sorting purposes.  */  
   CustID:string,
      /**  Purchase order that suggestion is for.  */  
   PONum:number,
      /**  The line # of  PoDetail record suggestion is for.  */  
   POLine:number,
      /**  Purchase order release number that suggestion if for.  */  
   PORelNum:number,
      /**  The ID of the Planner. Used to filter suggestions.  */  
   PlannerID:string,
      /**  A duplicate of "OrderRel.FirmRelease".  This only pertains to suggestions related to OrderRel.  Used to filter suggestions.  */  
   FirmRelease:boolean,
      /**   Indicates if this suggestion affects stock.
Only the MRP Process creates StockTrans = Yes.  Various DB triggers and MRP create StockTrans = No (direct buy/mfg)  */  
   StockTrans:boolean,
      /**  Site Identifier for this manufacturing suggestion.  */  
   Plant:string,
      /**  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  */  
   SugNum:number,
      /**  This is the unique key for the TFOrdDtl table.  */  
   TFLineNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   Planner:string,
   SugSource:string,
      /**  An error message description.  Used initially when creating a job.  */  
   ErrorMsg:string,
   CustFullName:string,
   WarehouseDescription:string,
   UOM:string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   AssemblySeqDescription:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   OrderLineLineDesc:string,
      /**  A unique code that identifies the currency.  */  
   OrderNumCurrencyCode:string,
      /**  The member's name on the credit card.  */  
   OrderNumCardMemberName:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartNumTrackLots:boolean,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartNumSellingFactor:number,
      /**  Indicates if this part is serial number tracked  */  
   PartNumTrackSerialNum:boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   POLineLineDesc:string,
      /**  OUR internal Part number for this item.  */  
   POLinePartNum:string,
      /**  Supplier Part Number  */  
   POLineVenPartNum:string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   PORelNumRefCodeDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartSugListTableset{
   PartSugList:Erp_Tablesets_PartSugListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartSugRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Suggestions fall into two classes.
"MFG" = Suggestion pertains to manufacturing 
"PUR" = Suggestion pertains to purchasing.
Used to keep Mfg and Purchase suggestions separate.  */  
   Classifier:string,
      /**  New Requirement.  Used to filter between New and Changes.  */  
   NewFlag:boolean,
      /**  Suggestions can be;  "New" , "Can", "Dat", "Qty",  "Chg", "Cfg"  */  
   Type:string,
      /**   Suggested action to be taken for this Purchase Order release.
"X" = Expedite, "P" = Postpone,  "C" = Cancel, R = Reduce Qty.  */  
   SubType:string,
      /**  Part Number  */  
   PartNum:string,
      /**  Job Number. Think of this as the Job that the suggestion is for ("target job")  */  
   TargetJobNum:string,
      /**  Job Assembly Sequence.  The assembly that the suggestion is for ("target assembly").  This can occur when an assembly has a PullQuantity that is marked "Make Direct."  */  
   TargetAssemblySeq:number,
      /**  Job Material Sequence.  The material that the suggestion is for ("target material").  This can occur when the material is marked as "Make Direct."  */  
   TargetMtlSeq:number,
      /**  Indicates the source of the requirement that suggestion is related to; "Order", "Stock" or "Job".  */  
   Source:string,
      /**  Job Number  */  
   JobNum:string,
      /**  Assembly Sequence  */  
   AssemblySeq:number,
      /**  Qualifies the JobSeq field as to be a "M" - Material (JobMtl) record or "S" - Subcontract (JobOper) reference.  */  
   JobSeqType:string,
      /**  Seq # of specific material or subcontract operation record.  */  
   JobSeq:number,
      /**  Related sales order number. For build to stock demands the OrderNum, OrderLine and OrderRel fields are all zero  */  
   OrderNum:number,
      /**  Related Sales order line number.  */  
   OrderLine:number,
      /**  Related sales order release number.  */  
   OrderRelNum:number,
      /**   Inventory warehouse that job is producing for.
Only relevant for build to stock demands (ordernum = 0). In this case a valid Part must be referenced.  */  
   WarehouseCode:string,
      /**   Due date of the related requirement record.
OrderRel.ReqDate.....  */  
   DueDate:string,
      /**  Suggested due date to change meet the requirement.  */  
   SugDate:string,
      /**  Suggested quantity.  */  
   SugQty:number,
      /**  Unit of Measure that qualifies SugQty.  */  
   SugQtyUOM:string,
      /**  Suggested change to Revision Number.  */  
   SugRevisionNum:string,
      /**   Description of the proposed suggestion.
Ex: Change Job Due date to xx/xx/xx.  */  
   Description:string,
      /**  1st 8 characters of customer name. Used for sorting suggestions  */  
   CustShortName:string,
      /**  Duplicated from the customer.custid. Used for sorting purposes.  */  
   CustID:string,
      /**  Purchase order that suggestion is for.  */  
   PONum:number,
      /**  The line # of  PoDetail record suggestion is for.  */  
   POLine:number,
      /**  Purchase order release number that suggestion if for.  */  
   PORelNum:number,
      /**  The ID of the Planner. Used to filter suggestions.  */  
   PlannerID:string,
      /**  A duplicate of "OrderRel.FirmRelease".  This only pertains to suggestions related to OrderRel.  Used to filter suggestions.  */  
   FirmRelease:boolean,
      /**   Indicates if this suggestion affects stock.
Only the MRP Process creates StockTrans = Yes.  Various DB triggers and MRP create StockTrans = No (direct buy/mfg)  */  
   StockTrans:boolean,
      /**  Site Identifier for this manufacturing suggestion.  */  
   Plant:string,
      /**  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  */  
   SugNum:number,
      /**  This is the unique key for the TFOrdDtl table.  */  
   TFLineNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ContractID  */  
   ContractID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  Date and time when this record was created.  */  
   CreatedOn:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
   CustFullName:string,
      /**  An error message description.  Used initially when creating a job.  */  
   ErrorMsg:string,
   JobInProcess:boolean,
   Planner:string,
   SugSource:string,
   UOM:string,
   WarehouseDescription:string,
      /**  Used for selecting record on landing page grid for Kinetic version.  */  
   SelectedPartSug:boolean,
   BitFlag:number,
   AssemblySeqDescription:string,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
   JobNumReqDueDate:string,
   JobNumStartDate:string,
   OrderLineLineDesc:string,
   OrderNumCardMemberName:string,
   OrderNumCurrencyCode:string,
   PartNumSellingFactor:number,
   PartNumIUM:string,
   PartNumSalesUM:string,
   PartNumPricePerCode:string,
   PartNumTrackDimension:boolean,
   PartNumPartDescription:string,
   PartNumTrackLots:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumAttrClassID:string,
   POLinePartNum:string,
   POLineLineDesc:string,
   POLineVenPartNum:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlanningWBTableset{
   PartSug:Erp_Tablesets_PartSugRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPlanningWBTableset{
   PartSug:Erp_Tablesets_PartSugRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param sysRowID
   */  
export interface GetByID_input{
   sysRowID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PlanningWBTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PlanningWBTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PlanningWBTableset[],
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
   returnObj:Erp_Tablesets_PartSugListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPartSug_input{
   ds:Erp_Tablesets_PlanningWBTableset[],
}

export interface GetNewPartSug_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlanningWBTableset,
}
}

   /** Required : 
      @param whereClausePartSug
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePartSug:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PlanningWBTableset[],
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
   ds:Erp_Tablesets_UpdExtPlanningWBTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPlanningWBTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PlanningWBTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlanningWBTableset,
}
}

