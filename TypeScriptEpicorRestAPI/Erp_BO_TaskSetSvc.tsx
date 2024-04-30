import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.TaskSetSvc
// Description: Task Set main object.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/$metadata", {
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
   Description: Get TaskSets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaskSets
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskSetRow
   */  
export function get_TaskSets(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSets", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaskSets
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaskSetRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.TaskSetRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TaskSets(requestBody:Erp_Tablesets_TaskSetRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSets", {
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
   Summary: Calls GetByID to retrieve the TaskSet item
   Description: Calls GetByID to retrieve the TaskSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaskSet
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaskSetID Desc: TaskSetID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TaskSetRow
   */  
export function get_TaskSets_Company_TaskSetID(Company:string, TaskSetID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaskSetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSets(" + Company + "," + TaskSetID + ")", {
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
         resolve(data as Erp_Tablesets_TaskSetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TaskSet for the service
   Description: Calls UpdateExt to update TaskSet. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaskSet
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaskSetID Desc: TaskSetID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaskSetRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TaskSets_Company_TaskSetID(Company:string, TaskSetID:string, requestBody:Erp_Tablesets_TaskSetRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSets(" + Company + "," + TaskSetID + ")", {
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
   Summary: Call UpdateExt to delete TaskSet item
   Description: Call UpdateExt to delete TaskSet item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaskSet
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaskSetID Desc: TaskSetID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TaskSets_Company_TaskSetID(Company:string, TaskSetID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSets(" + Company + "," + TaskSetID + ")", {
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
   Summary: Calls GetByID for the service
   Description: Get TaskSMilestones items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaskSMilestones1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaskSetID Desc: TaskSetID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskSMilestoneRow
   */  
export function get_TaskSets_Company_TaskSetID_TaskSMilestones(Company:string, TaskSetID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSMilestoneRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSets(" + Company + "," + TaskSetID + ")/TaskSMilestones", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSMilestoneRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TaskSMilestone item
   Description: Calls GetByID to retrieve the TaskSMilestone item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaskSMilestone1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaskSetID Desc: TaskSetID   Required: True   Allow empty value : True
      @param TaskSetSeq Desc: TaskSetSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TaskSMilestoneRow
   */  
export function get_TaskSets_Company_TaskSetID_TaskSMilestones_Company_TaskSetID_TaskSetSeq(Company:string, TaskSetID:string, TaskSetSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaskSMilestoneRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSets(" + Company + "," + TaskSetID + ")/TaskSMilestones(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")", {
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
         resolve(data as Erp_Tablesets_TaskSMilestoneRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get TaskSMilestones items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaskSMilestones
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskSMilestoneRow
   */  
export function get_TaskSMilestones(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSMilestoneRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSMilestones", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSMilestoneRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaskSMilestones
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaskSMilestoneRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.TaskSMilestoneRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TaskSMilestones(requestBody:Erp_Tablesets_TaskSMilestoneRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSMilestones", {
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
   Summary: Calls GetByID to retrieve the TaskSMilestone item
   Description: Calls GetByID to retrieve the TaskSMilestone item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaskSMilestone
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaskSetID Desc: TaskSetID   Required: True   Allow empty value : True
      @param TaskSetSeq Desc: TaskSetSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TaskSMilestoneRow
   */  
export function get_TaskSMilestones_Company_TaskSetID_TaskSetSeq(Company:string, TaskSetID:string, TaskSetSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaskSMilestoneRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSMilestones(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")", {
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
         resolve(data as Erp_Tablesets_TaskSMilestoneRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TaskSMilestone for the service
   Description: Calls UpdateExt to update TaskSMilestone. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaskSMilestone
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaskSetID Desc: TaskSetID   Required: True   Allow empty value : True
      @param TaskSetSeq Desc: TaskSetSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaskSMilestoneRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TaskSMilestones_Company_TaskSetID_TaskSetSeq(Company:string, TaskSetID:string, TaskSetSeq:string, requestBody:Erp_Tablesets_TaskSMilestoneRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSMilestones(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")", {
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
   Summary: Call UpdateExt to delete TaskSMilestone item
   Description: Call UpdateExt to delete TaskSMilestone item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaskSMilestone
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaskSetID Desc: TaskSetID   Required: True   Allow empty value : True
      @param TaskSetSeq Desc: TaskSetSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TaskSMilestones_Company_TaskSetID_TaskSetSeq(Company:string, TaskSetID:string, TaskSetSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSMilestones(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")", {
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
   Summary: Calls GetByID for the service
   Description: Get TaskSDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaskSDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaskSetID Desc: TaskSetID   Required: True   Allow empty value : True
      @param TaskSetSeq Desc: TaskSetSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskSDtlRow
   */  
export function get_TaskSMilestones_Company_TaskSetID_TaskSetSeq_TaskSDtls(Company:string, TaskSetID:string, TaskSetSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSMilestones(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")/TaskSDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TaskSDtl item
   Description: Calls GetByID to retrieve the TaskSDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaskSDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaskSetID Desc: TaskSetID   Required: True   Allow empty value : True
      @param TaskSetSeq Desc: TaskSetSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TaskSDtlRow
   */  
export function get_TaskSMilestones_Company_TaskSetID_TaskSetSeq_TaskSDtls_Company_TaskSetID_TaskSetSeq(Company:string, TaskSetID:string, TaskSetSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaskSDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSMilestones(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")/TaskSDtls(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")", {
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
         resolve(data as Erp_Tablesets_TaskSDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get TaskSNxts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaskSNxts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaskSetID Desc: TaskSetID   Required: True   Allow empty value : True
      @param TaskSetSeq Desc: TaskSetSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskSNxtRow
   */  
export function get_TaskSMilestones_Company_TaskSetID_TaskSetSeq_TaskSNxts(Company:string, TaskSetID:string, TaskSetSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSNxtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSMilestones(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")/TaskSNxts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSNxtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TaskSNxt item
   Description: Calls GetByID to retrieve the TaskSNxt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaskSNxt1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaskSetID Desc: TaskSetID   Required: True   Allow empty value : True
      @param TaskSetSeq Desc: TaskSetSeq   Required: True
      @param NextTaskSeq Desc: NextTaskSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TaskSNxtRow
   */  
export function get_TaskSMilestones_Company_TaskSetID_TaskSetSeq_TaskSNxts_Company_TaskSetID_TaskSetSeq_NextTaskSeq(Company:string, TaskSetID:string, TaskSetSeq:string, NextTaskSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaskSNxtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSMilestones(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")/TaskSNxts(" + Company + "," + TaskSetID + "," + TaskSetSeq + "," + NextTaskSeq + ")", {
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
         resolve(data as Erp_Tablesets_TaskSNxtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get TaskSDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaskSDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskSDtlRow
   */  
export function get_TaskSDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaskSDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaskSDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.TaskSDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TaskSDtls(requestBody:Erp_Tablesets_TaskSDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSDtls", {
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
   Summary: Calls GetByID to retrieve the TaskSDtl item
   Description: Calls GetByID to retrieve the TaskSDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaskSDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaskSetID Desc: TaskSetID   Required: True   Allow empty value : True
      @param TaskSetSeq Desc: TaskSetSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TaskSDtlRow
   */  
export function get_TaskSDtls_Company_TaskSetID_TaskSetSeq(Company:string, TaskSetID:string, TaskSetSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaskSDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSDtls(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")", {
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
         resolve(data as Erp_Tablesets_TaskSDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TaskSDtl for the service
   Description: Calls UpdateExt to update TaskSDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaskSDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaskSetID Desc: TaskSetID   Required: True   Allow empty value : True
      @param TaskSetSeq Desc: TaskSetSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaskSDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TaskSDtls_Company_TaskSetID_TaskSetSeq(Company:string, TaskSetID:string, TaskSetSeq:string, requestBody:Erp_Tablesets_TaskSDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSDtls(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")", {
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
   Summary: Call UpdateExt to delete TaskSDtl item
   Description: Call UpdateExt to delete TaskSDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaskSDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaskSetID Desc: TaskSetID   Required: True   Allow empty value : True
      @param TaskSetSeq Desc: TaskSetSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TaskSDtls_Company_TaskSetID_TaskSetSeq(Company:string, TaskSetID:string, TaskSetSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSDtls(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")", {
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
   Summary: Calls GetRows for the service
   Description: Get TaskSNxts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaskSNxts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskSNxtRow
   */  
export function get_TaskSNxts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSNxtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSNxts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSNxtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaskSNxts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaskSNxtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.TaskSNxtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TaskSNxts(requestBody:Erp_Tablesets_TaskSNxtRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSNxts", {
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
   Summary: Calls GetByID to retrieve the TaskSNxt item
   Description: Calls GetByID to retrieve the TaskSNxt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaskSNxt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaskSetID Desc: TaskSetID   Required: True   Allow empty value : True
      @param TaskSetSeq Desc: TaskSetSeq   Required: True
      @param NextTaskSeq Desc: NextTaskSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TaskSNxtRow
   */  
export function get_TaskSNxts_Company_TaskSetID_TaskSetSeq_NextTaskSeq(Company:string, TaskSetID:string, TaskSetSeq:string, NextTaskSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaskSNxtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSNxts(" + Company + "," + TaskSetID + "," + TaskSetSeq + "," + NextTaskSeq + ")", {
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
         resolve(data as Erp_Tablesets_TaskSNxtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TaskSNxt for the service
   Description: Calls UpdateExt to update TaskSNxt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaskSNxt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaskSetID Desc: TaskSetID   Required: True   Allow empty value : True
      @param TaskSetSeq Desc: TaskSetSeq   Required: True
      @param NextTaskSeq Desc: NextTaskSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaskSNxtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TaskSNxts_Company_TaskSetID_TaskSetSeq_NextTaskSeq(Company:string, TaskSetID:string, TaskSetSeq:string, NextTaskSeq:string, requestBody:Erp_Tablesets_TaskSNxtRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSNxts(" + Company + "," + TaskSetID + "," + TaskSetSeq + "," + NextTaskSeq + ")", {
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
   Summary: Call UpdateExt to delete TaskSNxt item
   Description: Call UpdateExt to delete TaskSNxt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaskSNxt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaskSetID Desc: TaskSetID   Required: True   Allow empty value : True
      @param TaskSetSeq Desc: TaskSetSeq   Required: True
      @param NextTaskSeq Desc: NextTaskSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TaskSNxts_Company_TaskSetID_TaskSetSeq_NextTaskSeq(Company:string, TaskSetID:string, TaskSetSeq:string, NextTaskSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/TaskSNxts(" + Company + "," + TaskSetID + "," + TaskSetSeq + "," + NextTaskSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskSetListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSetListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSetListRow)
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseTaskSet:string, whereClauseTaskSMilestone:string, whereClauseTaskSDtl:string, whereClauseTaskSNxt:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseTaskSet!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTaskSet=" + whereClauseTaskSet
   }
   if(typeof whereClauseTaskSMilestone!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTaskSMilestone=" + whereClauseTaskSMilestone
   }
   if(typeof whereClauseTaskSDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTaskSDtl=" + whereClauseTaskSDtl
   }
   if(typeof whereClauseTaskSNxt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTaskSNxt=" + whereClauseTaskSNxt
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/GetRows" + params, {
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
export function get_GetByID(taskSetID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof taskSetID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "taskSetID=" + taskSetID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/GetList" + params, {
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
   Summary: Invoke method GetCodeDescList
   Description: Returns a Code Description
   OperationID: GetCodeDescList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:GetCodeDescList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCodeDescList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/GetCodeDescList", {
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
         resolve(data as GetCodeDescList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildNextTaskList
   Description: Returns a delimited list of next task sequences available in id`desc pairs
   OperationID: BuildNextTaskList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildNextTaskList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildNextTaskList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildNextTaskList(requestBody:BuildNextTaskList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildNextTaskList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/BuildNextTaskList", {
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
         resolve(data as BuildNextTaskList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildParentTaskList
   Description: Returns a delimited list of available parent task sequences in id`desc pairs
   OperationID: BuildParentTaskList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildParentTaskList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildParentTaskList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildParentTaskList(requestBody:BuildParentTaskList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildParentTaskList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/BuildParentTaskList", {
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
         resolve(data as BuildParentTaskList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildStageList
   Description: Returns a delimited list of available stages in the format "ID`Desc~ID`Desc"
   OperationID: BuildStageList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildStageList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildStageList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildStageList(requestBody:BuildStageList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildStageList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/BuildStageList", {
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
         resolve(data as BuildStageList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopyTaskSet
   Description: Copies a task set to a new task set
   OperationID: CopyTaskSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopyTaskSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyTaskSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyTaskSet(requestBody:CopyTaskSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopyTaskSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/CopyTaskSet", {
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
         resolve(data as CopyTaskSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultMilestoneInfo
   Description: This method assigns the RoleCode and CurrentStage based on the task selected
   OperationID: DefaultMilestoneInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultMilestoneInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultMilestoneInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultMilestoneInfo(requestBody:DefaultMilestoneInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultMilestoneInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/DefaultMilestoneInfo", {
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
         resolve(data as DefaultMilestoneInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultNextTaskInfo
   Description: This method updates the TaskSNxt record after the next seq has been selected
   OperationID: DefaultNextTaskInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultNextTaskInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultNextTaskInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultNextTaskInfo(requestBody:DefaultNextTaskInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultNextTaskInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/DefaultNextTaskInfo", {
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
         resolve(data as DefaultNextTaskInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultRelatedTaskInfo
   Description: This method updates the RoleCode and Mandatory fields once the TaskId has been selected
   OperationID: DefaultRelatedTaskInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultRelatedTaskInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultRelatedTaskInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultRelatedTaskInfo(requestBody:DefaultRelatedTaskInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultRelatedTaskInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/DefaultRelatedTaskInfo", {
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
         resolve(data as DefaultRelatedTaskInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCRMTaskSetList
   Description: This method asks for a taskSetId and activeTaskId (currently found on QuoteHed) and
it will only return TaskSets that are applicable to those inputs
   OperationID: GetCRMTaskSetList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCRMTaskSetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCRMTaskSetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCRMTaskSetList(requestBody:GetCRMTaskSetList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCRMTaskSetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/GetCRMTaskSetList", {
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
         resolve(data as GetCRMTaskSetList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListFilterTaskSet
   Description: This method is used to filter the search results of TaskSet depending on the
current Active TaskID.
   OperationID: GetListFilterTaskSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListFilterTaskSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListFilterTaskSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListFilterTaskSet(requestBody:GetListFilterTaskSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListFilterTaskSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/GetListFilterTaskSet", {
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
         resolve(data as GetListFilterTaskSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTaskDetail
   Description: This method creates the new TaskSDtl record in place of the standard method
   OperationID: GetNewTaskDetail
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewTaskDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaskDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTaskDetail(requestBody:GetNewTaskDetail_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewTaskDetail_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/GetNewTaskDetail", {
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
         resolve(data as GetNewTaskDetail_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTaskSets
   Description: This Method get available Task Sets
   OperationID: GetTaskSets
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaskSets_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTaskSets(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTaskSets_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/GetTaskSets", {
          method: 'post',
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
         resolve(data as GetTaskSets_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTaskSet
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaskSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewTaskSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaskSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTaskSet(requestBody:GetNewTaskSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewTaskSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/GetNewTaskSet", {
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
         resolve(data as GetNewTaskSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTaskSMilestone
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaskSMilestone
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewTaskSMilestone_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaskSMilestone_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTaskSMilestone(requestBody:GetNewTaskSMilestone_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewTaskSMilestone_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/GetNewTaskSMilestone", {
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
         resolve(data as GetNewTaskSMilestone_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTaskSDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaskSDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewTaskSDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaskSDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTaskSDtl(requestBody:GetNewTaskSDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewTaskSDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/GetNewTaskSDtl", {
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
         resolve(data as GetNewTaskSDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTaskSNxt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaskSNxt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewTaskSNxt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaskSNxt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTaskSNxt(requestBody:GetNewTaskSNxt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewTaskSNxt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/GetNewTaskSNxt", {
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
         resolve(data as GetNewTaskSNxt_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSetSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaskSDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSMilestoneRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaskSMilestoneRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSNxtRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaskSNxtRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSetListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaskSetListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSetRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaskSetRow,
}

export interface Erp_Tablesets_TaskSDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Link to the related task set (TaskSet.TaskSetID).  */  
   "TaskSetID":string,
      /**  Unique identifier that determines the sequence of this task in the task set.  */  
   "TaskSetSeq":number,
      /**  Link to the related task master record (TaskMast.TaskID).  */  
   "TaskID":string,
      /**  Description of the task.  */  
   "TaskDescription":string,
      /**  A task that is marked as a Milestone must be completed before the Next Milestone or the Next Milestone's related tasks can be completed.  Only one Milestone task can be active at any point in time.  */  
   "Milestone":boolean,
      /**  Used to group non-milestone tasks to a parent milestone task.  When the next milestone task is creates the milestone and all its children will be created and available for completing.  */  
   "ParentTaskSeq":number,
      /**  This field only applies to milestone tasks.  Determines what stage or state the related quote or ECO group is in while this milestone is active.  */  
   "CurrentStage":string,
      /**  This field only applies to milestone tasks for Opportunities and Quotes. When completing this task the win function will be allowed. Only  */  
   "WinAllowed":boolean,
      /**  This field only applies to milestone tasks for opportunities and quotes. When completing this task the Lose function will be allowed.  */  
   "LoseAllowed":boolean,
      /**  The date the task was created.  */  
   "CreateDate":string,
      /**  The UserID that created the task  */  
   "CreateDcdUserID":string,
      /**  The date the task was last changed.  */  
   "ChangeDate":string,
      /**  The UserID that last changed the task  */  
   "ChangeDcdUserID":string,
      /**  This task must be completed before the task set can move to the next milestone. If a Milestone task has mandatory related tasks, the milestone cannot be completed until the mandatory related tasks are completed.  */  
   "Mandatory":boolean,
      /**  The number of days this task normally takes to complete. This is used to determine when one task can end and the next task can begin.  For example, when a task is assigned the Task.DueDate is calculated as the Task.StartDate plus the TaskSDtl.DaysToComplete.  */  
   "DaysToComplete":number,
      /**  This field only applies to milestone tasks for ECO groups.  Determines whether or not revisions can be checked in when this milestone is active.  */  
   "ECOCheckOutAllowed":boolean,
      /**  This field only applies to milestone tasks for ECO groups.  Determines whether or not revisions can be checked in when this milestone is active.  */  
   "ECOCheckInAllowed":boolean,
      /**  This applies only to milestone tasks for ECO groups.  If set to true, then the milestone can be completed without requiring a next milestone which essentially completes the task set.  */  
   "WFCompleteAllowed":boolean,
      /**  RoleCd.RoleCode of person who would normally be assigned this task when it is created.  */  
   "RoleCode":string,
      /**   The action to take when the task is completed.  Applies to milestones only.  Used for time and expense tasks.  Values are:
SUB - Submit.  The time or expense record status is set to submitted when the milestone is complete.
APP - Approve.  The time or expense record is approved when the milestone is complete.  */  
   "CompletionAction":string,
      /**  Applies to milestones.  Auto complete the milestone when the related tasks are completed.  */  
   "AutoComplete":boolean,
      /**  Indicates if this task is for submitting time or expense transactions.  Applies only to task types for time or expense.  */  
   "SubmitTask":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "StageDescription":string,
   "FirstMilestone":boolean,
   "ParentTaskDescription":string,
   "RoleDescription":string,
   "TaskAnyApprover":boolean,
      /**  Flag to tell us whether the associated TaskID has a TaskType that is Time and Expense.  */  
   "TETaskType":boolean,
   "BitFlag":number,
   "TaskIDTaskDescription":string,
   "TaskSetIDTaskSetDescription":string,
   "TaskSetIDWorkflowType":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TaskSMilestoneRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Link to the related task set (TaskSet.TaskSetID).  */  
   "TaskSetID":string,
      /**  Unique identifier that determines the sequence of this task in the task set.  */  
   "TaskSetSeq":number,
      /**  Link to the related task master record (TaskMast.TaskID).  */  
   "TaskID":string,
      /**  Description of the task.  */  
   "TaskDescription":string,
      /**  A task that is marked as a Milestone must be completed before the Next Milestone or the Next Milestone's related tasks can be completed.  Only one Milestone task can be active at any point in time.  */  
   "Milestone":boolean,
      /**  Used to group non-milestone tasks to a parent milestone task.  When the next milestone task is creates the milestone and all its children will be created and available for completing.  */  
   "ParentTaskSeq":number,
      /**  This field only applies to milestone tasks.  Determines what stage or state the related quote or ECO group is in while this milestone is active.  */  
   "CurrentStage":string,
      /**  This field only applies to milestone tasks for Opportunities and Quotes. When completing this task the win function will be allowed. Only  */  
   "WinAllowed":boolean,
      /**  This field only applies to milestone tasks for opportunities and quotes. When completing this task the Lose function will be allowed.  */  
   "LoseAllowed":boolean,
      /**  The date the task was created.  */  
   "CreateDate":string,
      /**  The UserID that created the task  */  
   "CreateDcdUserID":string,
      /**  The date the task was last changed.  */  
   "ChangeDate":string,
      /**  The UserID that last changed the task  */  
   "ChangeDcdUserID":string,
      /**  This task must be completed before the task set can move to the next milestone. If a Milestone task has mandatory related tasks, the milestone cannot be completed until the mandatory related tasks are completed.  */  
   "Mandatory":boolean,
      /**  The number of days this task normally takes to complete. This is used to determine when one task can end and the next task can begin.  For example, when a task is assigned the Task.DueDate is calculated as the Task.StartDate plus the TaskSDtl.DaysToComplete.  */  
   "DaysToComplete":number,
      /**  This field only applies to milestone tasks for ECO groups.  Determines whether or not revisions can be checked in when this milestone is active.  */  
   "ECOCheckOutAllowed":boolean,
      /**  This field only applies to milestone tasks for ECO groups.  Determines whether or not revisions can be checked in when this milestone is active.  */  
   "ECOCheckInAllowed":boolean,
      /**  This applies only to milestone tasks for ECO groups.  If set to true, then the milestone can be completed without requiring a next milestone which essentially completes the task set.  */  
   "WFCompleteAllowed":boolean,
      /**  RoleCd.RoleCode of person who would normally be assigned this task when it is created.  */  
   "RoleCode":string,
   "StageDescription":string,
      /**  Applies to milestones.  Auto complete the milestone when the related tasks are completed.  */  
   "AutoComplete":boolean,
      /**  Indicates if this task is for submitting time or expense transactions.  Applies only to task types for time or expense.  */  
   "SubmitTask":boolean,
   "FirstMilestone":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "RoleDescription":string,
   "TaskAnyApprover":boolean,
   "BitFlag":number,
   "TaskSetIDTaskSetDescription":string,
   "TaskSetIDWorkflowType":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TaskSNxtRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Link to the related task set (TaskSet.TaskSetID) record.  */  
   "TaskSetID":string,
      /**  The TaskSDtl.TaskSetSeq value of the milestone for which you are defining a next milestone.  */  
   "TaskSetSeq":number,
      /**  The TaskSDtl.TaskSetSeq value of the next milestone.  */  
   "NextTaskSeq":number,
      /**  If this next milestone is marked as the default (TaskSNxt.DefaultNext = True) then it will by default be the next milestone.  However, another milestone set up in the TaskSNxt table could be manually selected based on the outcome of the current milestone.  */  
   "DefaultNext":boolean,
      /**  Indicates if this is the default next milestone when a time or expense is rejected.  */  
   "DefaultNextForReject":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "TaskDescription":string,
   "StageDescription":string,
   "RoleDescription":string,
   "WinAllowed":boolean,
   "LoseAllowed":boolean,
   "DefaultRejectAllowed":boolean,
   "BitFlag":number,
   "TaskSetIDTaskSetDescription":string,
   "TaskSetIDWorkflowType":string,
   "TaskSetSeqTaskDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TaskSetListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of the task set assigned by the user.  */  
   "TaskSetID":string,
      /**  Description of the task set.  */  
   "TaskSetDescription":string,
      /**  The date the record was created.  */  
   "CreateDate":string,
      /**  The DCDUserID of the person that created this record.  */  
   "CreateUserID":string,
      /**  The date the record was last changed.  */  
   "ChangeDate":string,
      /**  The DCDUserID of the person that last changed the record.  */  
   "ChangeUserID":string,
      /**  Indicates if this task set can be used for new quotes or eco groups.  */  
   "Inactive":boolean,
      /**  Identifies the first Milestone task for the task set. The first milestone will be considered as the Active Milestone when a task set is assigned.  */  
   "FirstTaskSeq":number,
      /**  The type of workflow of this task set.  Possible values are "CRM" - CRM related tasks and "ECO" - ECO tasks  */  
   "WorkflowType":string,
      /**  When a TaskSet is initially added to an ECOGroup the ECOGroup CheckOutAllowed is set to this value.  */  
   "ECOCheckOutAllowed":boolean,
      /**  When a TaskSet is initially added to an ECOGroup the ECOGroup CheckInAllowed is set to this value.  */  
   "ECOCheckInAllowed":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates if the task set contains a submit milestone task.  Used by the UI in rowrules to determine if First Milestone for milestones is enabled or not.  */  
   "HasTESubmitTask":boolean,
      /**  W  */  
   "WFGroupID":string,
      /**  Workflow type description.  */  
   "WFDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TaskSetRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of the task set assigned by the user.  */  
   "TaskSetID":string,
      /**  Description of the task set.  */  
   "TaskSetDescription":string,
      /**  The date the record was created.  */  
   "CreateDate":string,
      /**  The DCDUserID of the person that created this record.  */  
   "CreateUserID":string,
      /**  The date the record was last changed.  */  
   "ChangeDate":string,
      /**  The DCDUserID of the person that last changed the record.  */  
   "ChangeUserID":string,
      /**  Indicates if this task set can be used for new quotes or eco groups.  */  
   "Inactive":boolean,
      /**  Identifies the first Milestone task for the task set. The first milestone will be considered as the Active Milestone when a task set is assigned.  */  
   "FirstTaskSeq":number,
      /**  The type of workflow of this task set.  Possible values are "CRM" - CRM related tasks and "ECO" - ECO tasks  */  
   "WorkflowType":string,
      /**  When a TaskSet is initially added to an ECOGroup the ECOGroup CheckOutAllowed is set to this value.  */  
   "ECOCheckOutAllowed":boolean,
      /**  When a TaskSet is initially added to an ECOGroup the ECOGroup CheckInAllowed is set to this value.  */  
   "ECOCheckInAllowed":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates if the task set contains a submit milestone task.  Used by the UI in rowrules to determine if First Milestone for milestones is enabled or not.  */  
   "HasTESubmitTask":boolean,
      /**  W  */  
   "WFGroupID":string,
      /**  Workflow type description.  */  
   "WFDescription":string,
   "BitFlag":number,
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
      @param taskSetId
      @param taskSetSeq
      @param taskNextSeq
   */  
export interface BuildNextTaskList_input{
      /**  Task Set Id  */  
   taskSetId:string,
      /**  Current Task Sequence  */  
   taskSetSeq:number,
      /**  Existing Next Task to exclude from list  */  
   taskNextSeq:number,
}

export interface BuildNextTaskList_output{
parameters : {
      /**  output parameters  */  
   nextList:string,
}
}

   /** Required : 
      @param cTaskSetId
   */  
export interface BuildParentTaskList_input{
      /**  Task Set Id  */  
   cTaskSetId:string,
}

export interface BuildParentTaskList_output{
parameters : {
      /**  output parameters  */  
   cParentList:string,
}
}

   /** Required : 
      @param workflowType
   */  
export interface BuildStageList_input{
      /**  Workflow Type to determine the list of stages  */  
   workflowType:string,
}

export interface BuildStageList_output{
parameters : {
      /**  output parameters  */  
   stageList:string,
}
}

   /** Required : 
      @param sourceTaskSetID
      @param targetTaskSetID
      @param targetTaskSetDesc
   */  
export interface CopyTaskSet_input{
      /**  The ID of the source task set (copy from)  */  
   sourceTaskSetID:string,
      /**  The ID of the new task set (copy to)  */  
   targetTaskSetID:string,
      /**  The Description of the new task set  */  
   targetTaskSetDesc:string,
}

export interface CopyTaskSet_output{
   returnObj:Erp_Tablesets_TaskSetTableset[],
}

   /** Required : 
      @param ds
   */  
export interface DefaultMilestoneInfo_input{
   ds:Erp_Tablesets_TaskSetTableset[],
}

export interface DefaultMilestoneInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskSetTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface DefaultNextTaskInfo_input{
   ds:Erp_Tablesets_TaskSetTableset[],
}

export interface DefaultNextTaskInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskSetTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface DefaultRelatedTaskInfo_input{
   ds:Erp_Tablesets_TaskSetTableset[],
}

export interface DefaultRelatedTaskInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskSetTableset,
}
}

   /** Required : 
      @param taskSetID
   */  
export interface DeleteByID_input{
   taskSetID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_TaskSDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Link to the related task set (TaskSet.TaskSetID).  */  
   TaskSetID:string,
      /**  Unique identifier that determines the sequence of this task in the task set.  */  
   TaskSetSeq:number,
      /**  Link to the related task master record (TaskMast.TaskID).  */  
   TaskID:string,
      /**  Description of the task.  */  
   TaskDescription:string,
      /**  A task that is marked as a Milestone must be completed before the Next Milestone or the Next Milestone's related tasks can be completed.  Only one Milestone task can be active at any point in time.  */  
   Milestone:boolean,
      /**  Used to group non-milestone tasks to a parent milestone task.  When the next milestone task is creates the milestone and all its children will be created and available for completing.  */  
   ParentTaskSeq:number,
      /**  This field only applies to milestone tasks.  Determines what stage or state the related quote or ECO group is in while this milestone is active.  */  
   CurrentStage:string,
      /**  This field only applies to milestone tasks for Opportunities and Quotes. When completing this task the win function will be allowed. Only  */  
   WinAllowed:boolean,
      /**  This field only applies to milestone tasks for opportunities and quotes. When completing this task the Lose function will be allowed.  */  
   LoseAllowed:boolean,
      /**  The date the task was created.  */  
   CreateDate:string,
      /**  The UserID that created the task  */  
   CreateDcdUserID:string,
      /**  The date the task was last changed.  */  
   ChangeDate:string,
      /**  The UserID that last changed the task  */  
   ChangeDcdUserID:string,
      /**  This task must be completed before the task set can move to the next milestone. If a Milestone task has mandatory related tasks, the milestone cannot be completed until the mandatory related tasks are completed.  */  
   Mandatory:boolean,
      /**  The number of days this task normally takes to complete. This is used to determine when one task can end and the next task can begin.  For example, when a task is assigned the Task.DueDate is calculated as the Task.StartDate plus the TaskSDtl.DaysToComplete.  */  
   DaysToComplete:number,
      /**  This field only applies to milestone tasks for ECO groups.  Determines whether or not revisions can be checked in when this milestone is active.  */  
   ECOCheckOutAllowed:boolean,
      /**  This field only applies to milestone tasks for ECO groups.  Determines whether or not revisions can be checked in when this milestone is active.  */  
   ECOCheckInAllowed:boolean,
      /**  This applies only to milestone tasks for ECO groups.  If set to true, then the milestone can be completed without requiring a next milestone which essentially completes the task set.  */  
   WFCompleteAllowed:boolean,
      /**  RoleCd.RoleCode of person who would normally be assigned this task when it is created.  */  
   RoleCode:string,
      /**   The action to take when the task is completed.  Applies to milestones only.  Used for time and expense tasks.  Values are:
SUB - Submit.  The time or expense record status is set to submitted when the milestone is complete.
APP - Approve.  The time or expense record is approved when the milestone is complete.  */  
   CompletionAction:string,
      /**  Applies to milestones.  Auto complete the milestone when the related tasks are completed.  */  
   AutoComplete:boolean,
      /**  Indicates if this task is for submitting time or expense transactions.  Applies only to task types for time or expense.  */  
   SubmitTask:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   StageDescription:string,
   FirstMilestone:boolean,
   ParentTaskDescription:string,
   RoleDescription:string,
   TaskAnyApprover:boolean,
      /**  Flag to tell us whether the associated TaskID has a TaskType that is Time and Expense.  */  
   TETaskType:boolean,
   BitFlag:number,
   TaskIDTaskDescription:string,
   TaskSetIDTaskSetDescription:string,
   TaskSetIDWorkflowType:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaskSMilestoneRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Link to the related task set (TaskSet.TaskSetID).  */  
   TaskSetID:string,
      /**  Unique identifier that determines the sequence of this task in the task set.  */  
   TaskSetSeq:number,
      /**  Link to the related task master record (TaskMast.TaskID).  */  
   TaskID:string,
      /**  Description of the task.  */  
   TaskDescription:string,
      /**  A task that is marked as a Milestone must be completed before the Next Milestone or the Next Milestone's related tasks can be completed.  Only one Milestone task can be active at any point in time.  */  
   Milestone:boolean,
      /**  Used to group non-milestone tasks to a parent milestone task.  When the next milestone task is creates the milestone and all its children will be created and available for completing.  */  
   ParentTaskSeq:number,
      /**  This field only applies to milestone tasks.  Determines what stage or state the related quote or ECO group is in while this milestone is active.  */  
   CurrentStage:string,
      /**  This field only applies to milestone tasks for Opportunities and Quotes. When completing this task the win function will be allowed. Only  */  
   WinAllowed:boolean,
      /**  This field only applies to milestone tasks for opportunities and quotes. When completing this task the Lose function will be allowed.  */  
   LoseAllowed:boolean,
      /**  The date the task was created.  */  
   CreateDate:string,
      /**  The UserID that created the task  */  
   CreateDcdUserID:string,
      /**  The date the task was last changed.  */  
   ChangeDate:string,
      /**  The UserID that last changed the task  */  
   ChangeDcdUserID:string,
      /**  This task must be completed before the task set can move to the next milestone. If a Milestone task has mandatory related tasks, the milestone cannot be completed until the mandatory related tasks are completed.  */  
   Mandatory:boolean,
      /**  The number of days this task normally takes to complete. This is used to determine when one task can end and the next task can begin.  For example, when a task is assigned the Task.DueDate is calculated as the Task.StartDate plus the TaskSDtl.DaysToComplete.  */  
   DaysToComplete:number,
      /**  This field only applies to milestone tasks for ECO groups.  Determines whether or not revisions can be checked in when this milestone is active.  */  
   ECOCheckOutAllowed:boolean,
      /**  This field only applies to milestone tasks for ECO groups.  Determines whether or not revisions can be checked in when this milestone is active.  */  
   ECOCheckInAllowed:boolean,
      /**  This applies only to milestone tasks for ECO groups.  If set to true, then the milestone can be completed without requiring a next milestone which essentially completes the task set.  */  
   WFCompleteAllowed:boolean,
      /**  RoleCd.RoleCode of person who would normally be assigned this task when it is created.  */  
   RoleCode:string,
   StageDescription:string,
      /**  Applies to milestones.  Auto complete the milestone when the related tasks are completed.  */  
   AutoComplete:boolean,
      /**  Indicates if this task is for submitting time or expense transactions.  Applies only to task types for time or expense.  */  
   SubmitTask:boolean,
   FirstMilestone:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   RoleDescription:string,
   TaskAnyApprover:boolean,
   BitFlag:number,
   TaskSetIDTaskSetDescription:string,
   TaskSetIDWorkflowType:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaskSNxtRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Link to the related task set (TaskSet.TaskSetID) record.  */  
   TaskSetID:string,
      /**  The TaskSDtl.TaskSetSeq value of the milestone for which you are defining a next milestone.  */  
   TaskSetSeq:number,
      /**  The TaskSDtl.TaskSetSeq value of the next milestone.  */  
   NextTaskSeq:number,
      /**  If this next milestone is marked as the default (TaskSNxt.DefaultNext = True) then it will by default be the next milestone.  However, another milestone set up in the TaskSNxt table could be manually selected based on the outcome of the current milestone.  */  
   DefaultNext:boolean,
      /**  Indicates if this is the default next milestone when a time or expense is rejected.  */  
   DefaultNextForReject:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   TaskDescription:string,
   StageDescription:string,
   RoleDescription:string,
   WinAllowed:boolean,
   LoseAllowed:boolean,
   DefaultRejectAllowed:boolean,
   BitFlag:number,
   TaskSetIDTaskSetDescription:string,
   TaskSetIDWorkflowType:string,
   TaskSetSeqTaskDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaskSetListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of the task set assigned by the user.  */  
   TaskSetID:string,
      /**  Description of the task set.  */  
   TaskSetDescription:string,
      /**  The date the record was created.  */  
   CreateDate:string,
      /**  The DCDUserID of the person that created this record.  */  
   CreateUserID:string,
      /**  The date the record was last changed.  */  
   ChangeDate:string,
      /**  The DCDUserID of the person that last changed the record.  */  
   ChangeUserID:string,
      /**  Indicates if this task set can be used for new quotes or eco groups.  */  
   Inactive:boolean,
      /**  Identifies the first Milestone task for the task set. The first milestone will be considered as the Active Milestone when a task set is assigned.  */  
   FirstTaskSeq:number,
      /**  The type of workflow of this task set.  Possible values are "CRM" - CRM related tasks and "ECO" - ECO tasks  */  
   WorkflowType:string,
      /**  When a TaskSet is initially added to an ECOGroup the ECOGroup CheckOutAllowed is set to this value.  */  
   ECOCheckOutAllowed:boolean,
      /**  When a TaskSet is initially added to an ECOGroup the ECOGroup CheckInAllowed is set to this value.  */  
   ECOCheckInAllowed:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if the task set contains a submit milestone task.  Used by the UI in rowrules to determine if First Milestone for milestones is enabled or not.  */  
   HasTESubmitTask:boolean,
      /**  W  */  
   WFGroupID:string,
      /**  Workflow type description.  */  
   WFDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaskSetListTableset{
   TaskSetList:Erp_Tablesets_TaskSetListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_TaskSetRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of the task set assigned by the user.  */  
   TaskSetID:string,
      /**  Description of the task set.  */  
   TaskSetDescription:string,
      /**  The date the record was created.  */  
   CreateDate:string,
      /**  The DCDUserID of the person that created this record.  */  
   CreateUserID:string,
      /**  The date the record was last changed.  */  
   ChangeDate:string,
      /**  The DCDUserID of the person that last changed the record.  */  
   ChangeUserID:string,
      /**  Indicates if this task set can be used for new quotes or eco groups.  */  
   Inactive:boolean,
      /**  Identifies the first Milestone task for the task set. The first milestone will be considered as the Active Milestone when a task set is assigned.  */  
   FirstTaskSeq:number,
      /**  The type of workflow of this task set.  Possible values are "CRM" - CRM related tasks and "ECO" - ECO tasks  */  
   WorkflowType:string,
      /**  When a TaskSet is initially added to an ECOGroup the ECOGroup CheckOutAllowed is set to this value.  */  
   ECOCheckOutAllowed:boolean,
      /**  When a TaskSet is initially added to an ECOGroup the ECOGroup CheckInAllowed is set to this value.  */  
   ECOCheckInAllowed:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if the task set contains a submit milestone task.  Used by the UI in rowrules to determine if First Milestone for milestones is enabled or not.  */  
   HasTESubmitTask:boolean,
      /**  W  */  
   WFGroupID:string,
      /**  Workflow type description.  */  
   WFDescription:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaskSetTableset{
   TaskSet:Erp_Tablesets_TaskSetRow[],
   TaskSMilestone:Erp_Tablesets_TaskSMilestoneRow[],
   TaskSDtl:Erp_Tablesets_TaskSDtlRow[],
   TaskSNxt:Erp_Tablesets_TaskSNxtRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtTaskSetTableset{
   TaskSet:Erp_Tablesets_TaskSetRow[],
   TaskSMilestone:Erp_Tablesets_TaskSMilestoneRow[],
   TaskSDtl:Erp_Tablesets_TaskSDtlRow[],
   TaskSNxt:Erp_Tablesets_TaskSNxtRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param taskSetID
   */  
export interface GetByID_input{
   taskSetID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_TaskSetTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_TaskSetTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_TaskSetTableset[],
}

   /** Required : 
      @param taskSetId
      @param activeTaskId
      @param pageSize
      @param absolutePage
   */  
export interface GetCRMTaskSetList_input{
      /**  QuoteHed.TaskSetId  */  
   taskSetId:string,
      /**  QuoteHed.ActiveTaskId  */  
   activeTaskId:string,
      /**  The page size  */  
   pageSize:number,
      /**  The absolute page  */  
   absolutePage:number,
}

export interface GetCRMTaskSetList_output{
   returnObj:Erp_Tablesets_TaskSetListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
      /**  Table Name  */  
   tableName:string,
      /**  Field Name  */  
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param WhereClause
      @param PageSize
      @param AbsolutePage
      @param ActiveTaskID
   */  
export interface GetListFilterTaskSet_input{
      /**  WorkflowType='HelpDesk' And Inactive=true  */  
   WhereClause:string,
      /**  PageSize  */  
   PageSize:number,
      /**  AbsolutePage  */  
   AbsolutePage:number,
      /**  HDCase.ActiveTaskID  */  
   ActiveTaskID:string,
}

export interface GetListFilterTaskSet_output{
   returnObj:Erp_Tablesets_TaskSetListTableset[],
parameters : {
      /**  output parameters  */  
   MorePages:boolean,
}
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
   returnObj:Erp_Tablesets_TaskSetListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param TaskSetID
      @param ParentTaskSeq
   */  
export interface GetNewTaskDetail_input{
   ds:Erp_Tablesets_TaskSetTableset[],
      /**  Task Set Id  */  
   TaskSetID:string,
      /**  TaskSetSeq of the parent milestone  */  
   ParentTaskSeq:number,
}

export interface GetNewTaskDetail_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskSetTableset,
}
}

   /** Required : 
      @param ds
      @param taskSetID
   */  
export interface GetNewTaskSDtl_input{
   ds:Erp_Tablesets_TaskSetTableset[],
   taskSetID:string,
}

export interface GetNewTaskSDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskSetTableset,
}
}

   /** Required : 
      @param ds
      @param taskSetID
   */  
export interface GetNewTaskSMilestone_input{
   ds:Erp_Tablesets_TaskSetTableset[],
   taskSetID:string,
}

export interface GetNewTaskSMilestone_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskSetTableset,
}
}

   /** Required : 
      @param ds
      @param taskSetID
      @param taskSetSeq
   */  
export interface GetNewTaskSNxt_input{
   ds:Erp_Tablesets_TaskSetTableset[],
   taskSetID:string,
   taskSetSeq:number,
}

export interface GetNewTaskSNxt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskSetTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewTaskSet_input{
   ds:Erp_Tablesets_TaskSetTableset[],
}

export interface GetNewTaskSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskSetTableset,
}
}

   /** Required : 
      @param whereClauseTaskSet
      @param whereClauseTaskSMilestone
      @param whereClauseTaskSDtl
      @param whereClauseTaskSNxt
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseTaskSet:string,
   whereClauseTaskSMilestone:string,
   whereClauseTaskSDtl:string,
   whereClauseTaskSNxt:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_TaskSetTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetTaskSets_output{
   returnObj:Erp_Tablesets_TaskSetListTableset[],
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
   ds:Erp_Tablesets_UpdExtTaskSetTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtTaskSetTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_TaskSetTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskSetTableset,
}
}

