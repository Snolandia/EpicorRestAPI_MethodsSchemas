import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.BO.SysAgentSvc
// Description: SysAgent main object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/$metadata", {
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
   Summary: Calls GetRows for the service
   Description: Get SysAgents items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SysAgents
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysAgentRow
   */  
export function get_SysAgents(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgents", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SysAgents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SysAgentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SysAgentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SysAgents(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgents", {
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
   Summary: Calls GetByID to retrieve the SysAgent item
   Description: Calls GetByID to retrieve the SysAgent item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysAgent
      @param AgentID Desc: AgentID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysAgentRow
   */  
export function get_SysAgents_AgentID(AgentID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_SysAgentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgents(" + AgentID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_SysAgentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SysAgent for the service
   Description: Calls UpdateExt to update SysAgent. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SysAgent
      @param AgentID Desc: AgentID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SysAgentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SysAgents_AgentID(AgentID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgents(" + AgentID + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete SysAgent item
   Description: Call UpdateExt to delete SysAgent item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SysAgent
      @param AgentID Desc: AgentID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SysAgents_AgentID(AgentID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgents(" + AgentID + ")", {
          method: 'delete',
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
   Summary: Calls GetByID for the service
   Description: Get SysAgentScheds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SysAgentScheds1
      @param AgentID Desc: AgentID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysAgentSchedRow
   */  
export function get_SysAgents_AgentID_SysAgentScheds(AgentID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentSchedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgents(" + AgentID + ")/SysAgentScheds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentSchedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the SysAgentSched item
   Description: Calls GetByID to retrieve the SysAgentSched item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysAgentSched1
      @param AgentID Desc: AgentID   Required: True   Allow empty value : True
      @param AgentSchedNum Desc: AgentSchedNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysAgentSchedRow
   */  
export function get_SysAgents_AgentID_SysAgentScheds_AgentID_AgentSchedNum(AgentID:string, AgentSchedNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_SysAgentSchedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgents(" + AgentID + ")/SysAgentScheds(" + AgentID + "," + AgentSchedNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_SysAgentSchedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get SysAgentScheds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SysAgentScheds
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysAgentSchedRow
   */  
export function get_SysAgentScheds(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentSchedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentScheds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentSchedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SysAgentScheds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SysAgentSchedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SysAgentSchedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SysAgentScheds(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentScheds", {
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
   Summary: Calls GetByID to retrieve the SysAgentSched item
   Description: Calls GetByID to retrieve the SysAgentSched item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysAgentSched
      @param AgentID Desc: AgentID   Required: True   Allow empty value : True
      @param AgentSchedNum Desc: AgentSchedNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysAgentSchedRow
   */  
export function get_SysAgentScheds_AgentID_AgentSchedNum(AgentID:string, AgentSchedNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_SysAgentSchedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentScheds(" + AgentID + "," + AgentSchedNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_SysAgentSchedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SysAgentSched for the service
   Description: Calls UpdateExt to update SysAgentSched. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SysAgentSched
      @param AgentID Desc: AgentID   Required: True   Allow empty value : True
      @param AgentSchedNum Desc: AgentSchedNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SysAgentSchedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SysAgentScheds_AgentID_AgentSchedNum(AgentID:string, AgentSchedNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentScheds(" + AgentID + "," + AgentSchedNum + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete SysAgentSched item
   Description: Call UpdateExt to delete SysAgentSched item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SysAgentSched
      @param AgentID Desc: AgentID   Required: True   Allow empty value : True
      @param AgentSchedNum Desc: AgentSchedNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SysAgentScheds_AgentID_AgentSchedNum(AgentID:string, AgentSchedNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentScheds(" + AgentID + "," + AgentSchedNum + ")", {
          method: 'delete',
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
   Summary: Calls GetByID for the service
   Description: Get SysAgentTasks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SysAgentTasks1
      @param AgentID Desc: AgentID   Required: True   Allow empty value : True
      @param AgentSchedNum Desc: AgentSchedNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysAgentTaskRow
   */  
export function get_SysAgentScheds_AgentID_AgentSchedNum_SysAgentTasks(AgentID:string, AgentSchedNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentTaskRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentScheds(" + AgentID + "," + AgentSchedNum + ")/SysAgentTasks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentTaskRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the SysAgentTask item
   Description: Calls GetByID to retrieve the SysAgentTask item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysAgentTask1
      @param AgentID Desc: AgentID   Required: True   Allow empty value : True
      @param AgentSchedNum Desc: AgentSchedNum   Required: True   Allow empty value : True
      @param AgentTaskNum Desc: AgentTaskNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysAgentTaskRow
   */  
export function get_SysAgentScheds_AgentID_AgentSchedNum_SysAgentTasks_AgentID_AgentSchedNum_AgentTaskNum(AgentID:string, AgentSchedNum:string, AgentTaskNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_SysAgentTaskRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentScheds(" + AgentID + "," + AgentSchedNum + ")/SysAgentTasks(" + AgentID + "," + AgentSchedNum + "," + AgentTaskNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_SysAgentTaskRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get SysAgentTasks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SysAgentTasks
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysAgentTaskRow
   */  
export function get_SysAgentTasks(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentTaskRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentTasks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentTaskRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SysAgentTasks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SysAgentTaskRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SysAgentTaskRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SysAgentTasks(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentTasks", {
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
   Summary: Calls GetByID to retrieve the SysAgentTask item
   Description: Calls GetByID to retrieve the SysAgentTask item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysAgentTask
      @param AgentID Desc: AgentID   Required: True   Allow empty value : True
      @param AgentSchedNum Desc: AgentSchedNum   Required: True   Allow empty value : True
      @param AgentTaskNum Desc: AgentTaskNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysAgentTaskRow
   */  
export function get_SysAgentTasks_AgentID_AgentSchedNum_AgentTaskNum(AgentID:string, AgentSchedNum:string, AgentTaskNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_SysAgentTaskRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentTasks(" + AgentID + "," + AgentSchedNum + "," + AgentTaskNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_SysAgentTaskRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SysAgentTask for the service
   Description: Calls UpdateExt to update SysAgentTask. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SysAgentTask
      @param AgentID Desc: AgentID   Required: True   Allow empty value : True
      @param AgentSchedNum Desc: AgentSchedNum   Required: True   Allow empty value : True
      @param AgentTaskNum Desc: AgentTaskNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SysAgentTaskRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SysAgentTasks_AgentID_AgentSchedNum_AgentTaskNum(AgentID:string, AgentSchedNum:string, AgentTaskNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentTasks(" + AgentID + "," + AgentSchedNum + "," + AgentTaskNum + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete SysAgentTask item
   Description: Call UpdateExt to delete SysAgentTask item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SysAgentTask
      @param AgentID Desc: AgentID   Required: True   Allow empty value : True
      @param AgentSchedNum Desc: AgentSchedNum   Required: True   Allow empty value : True
      @param AgentTaskNum Desc: AgentTaskNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SysAgentTasks_AgentID_AgentSchedNum_AgentTaskNum(AgentID:string, AgentSchedNum:string, AgentTaskNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentTasks(" + AgentID + "," + AgentSchedNum + "," + AgentTaskNum + ")", {
          method: 'delete',
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
   Summary: Calls GetByID for the service
   Description: Get SysAgentTaskParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SysAgentTaskParams1
      @param AgentID Desc: AgentID   Required: True   Allow empty value : True
      @param AgentSchedNum Desc: AgentSchedNum   Required: True   Allow empty value : True
      @param AgentTaskNum Desc: AgentTaskNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysAgentTaskParamRow
   */  
export function get_SysAgentTasks_AgentID_AgentSchedNum_AgentTaskNum_SysAgentTaskParams(AgentID:string, AgentSchedNum:string, AgentTaskNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentTaskParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentTasks(" + AgentID + "," + AgentSchedNum + "," + AgentTaskNum + ")/SysAgentTaskParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentTaskParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the SysAgentTaskParam item
   Description: Calls GetByID to retrieve the SysAgentTaskParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysAgentTaskParam1
      @param AgentID Desc: AgentID   Required: True   Allow empty value : True
      @param AgentSchedNum Desc: AgentSchedNum   Required: True   Allow empty value : True
      @param AgentTaskNum Desc: AgentTaskNum   Required: True
      @param ParamName Desc: ParamName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysAgentTaskParamRow
   */  
export function get_SysAgentTasks_AgentID_AgentSchedNum_AgentTaskNum_SysAgentTaskParams_AgentID_AgentSchedNum_AgentTaskNum_ParamName(AgentID:string, AgentSchedNum:string, AgentTaskNum:string, ParamName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_SysAgentTaskParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentTasks(" + AgentID + "," + AgentSchedNum + "," + AgentTaskNum + ")/SysAgentTaskParams(" + AgentID + "," + AgentSchedNum + "," + AgentTaskNum + "," + ParamName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_SysAgentTaskParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get SysAgentTaskParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SysAgentTaskParams
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysAgentTaskParamRow
   */  
export function get_SysAgentTaskParams(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentTaskParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentTaskParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentTaskParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SysAgentTaskParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SysAgentTaskParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SysAgentTaskParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SysAgentTaskParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentTaskParams", {
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
   Summary: Calls GetByID to retrieve the SysAgentTaskParam item
   Description: Calls GetByID to retrieve the SysAgentTaskParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysAgentTaskParam
      @param AgentID Desc: AgentID   Required: True   Allow empty value : True
      @param AgentSchedNum Desc: AgentSchedNum   Required: True   Allow empty value : True
      @param AgentTaskNum Desc: AgentTaskNum   Required: True
      @param ParamName Desc: ParamName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysAgentTaskParamRow
   */  
export function get_SysAgentTaskParams_AgentID_AgentSchedNum_AgentTaskNum_ParamName(AgentID:string, AgentSchedNum:string, AgentTaskNum:string, ParamName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_SysAgentTaskParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentTaskParams(" + AgentID + "," + AgentSchedNum + "," + AgentTaskNum + "," + ParamName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_SysAgentTaskParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SysAgentTaskParam for the service
   Description: Calls UpdateExt to update SysAgentTaskParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SysAgentTaskParam
      @param AgentID Desc: AgentID   Required: True   Allow empty value : True
      @param AgentSchedNum Desc: AgentSchedNum   Required: True   Allow empty value : True
      @param AgentTaskNum Desc: AgentTaskNum   Required: True
      @param ParamName Desc: ParamName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SysAgentTaskParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SysAgentTaskParams_AgentID_AgentSchedNum_AgentTaskNum_ParamName(AgentID:string, AgentSchedNum:string, AgentTaskNum:string, ParamName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentTaskParams(" + AgentID + "," + AgentSchedNum + "," + AgentTaskNum + "," + ParamName + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete SysAgentTaskParam item
   Description: Call UpdateExt to delete SysAgentTaskParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SysAgentTaskParam
      @param AgentID Desc: AgentID   Required: True   Allow empty value : True
      @param AgentSchedNum Desc: AgentSchedNum   Required: True   Allow empty value : True
      @param AgentTaskNum Desc: AgentTaskNum   Required: True
      @param ParamName Desc: ParamName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SysAgentTaskParams_AgentID_AgentSchedNum_AgentTaskNum_ParamName(AgentID:string, AgentSchedNum:string, AgentTaskNum:string, ParamName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentTaskParams(" + AgentID + "," + AgentSchedNum + "," + AgentTaskNum + "," + ParamName + ")", {
          method: 'delete',
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysAgentListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentListRow)
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
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseSysAgent:string, whereClauseSysAgentSched:string, whereClauseSysAgentTask:string, whereClauseSysAgentTaskParam:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseSysAgent!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSysAgent=" + whereClauseSysAgent
   }
   if(typeof whereClauseSysAgentSched!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSysAgentSched=" + whereClauseSysAgentSched
   }
   if(typeof whereClauseSysAgentTask!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSysAgentTask=" + whereClauseSysAgentTask
   }
   if(typeof whereClauseSysAgentTaskParam!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSysAgentTaskParam=" + whereClauseSysAgentTaskParam
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/GetRows" + params, {
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
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(agentID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof agentID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "agentID=" + agentID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/GetByID" + params, {
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
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      @param whereClause Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/GetList" + params, {
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
   Summary: Invoke method SetSysAgentStatusToStarted
   Description: Sets the given SysAgent to a status of started. Also sets the NextRunOn date of any of the agent's schedules with a type of 'Startup'.
   OperationID: SetSysAgentStatusToStarted
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetSysAgentStatusToStarted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetSysAgentStatusToStarted_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetSysAgentStatusToStarted(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SetSysAgentStatusToStarted", {
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
   Summary: Invoke method SetSysAgentStatusToStopped
   Description: Sets the system agent status to stopped.
   OperationID: SetSysAgentStatusToStopped
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetSysAgentStatusToStopped_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetSysAgentStatusToStopped_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetSysAgentStatusToStopped(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SetSysAgentStatusToStopped", {
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
   Summary: Invoke method GetByIdForTaskAgent
   Description: Gets the SysAgent record and its associated schedules for use by the task agent.
   OperationID: GetByIdForTaskAgent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIdForTaskAgent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIdForTaskAgent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIdForTaskAgent(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/GetByIdForTaskAgent", {
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
   Summary: Invoke method ResetScheduleProcessingStartedOn
   Description: Deletes the SysAgentSchedProcessing record for the given schedule.
   OperationID: ResetScheduleProcessingStartedOn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResetScheduleProcessingStartedOn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetScheduleProcessingStartedOn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ResetScheduleProcessingStartedOn(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/ResetScheduleProcessingStartedOn", {
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
   Summary: Invoke method PurgeTaskHistory
   Description: Purges the SysTask rows that have History set to true and are older than our purge date.
   OperationID: PurgeTaskHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PurgeTaskHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PurgeTaskHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PurgeTaskHistory(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/PurgeTaskHistory", {
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
   Summary: Invoke method PurgeReports
   Description: Purges reports and their associated data that are older than the specified purge date.
   OperationID: PurgeReports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PurgeReports_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PurgeReports_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PurgeReports(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/PurgeReports", {
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
   Summary: Invoke method GetAgentSchedList
   Description: To return a dataset of SysAgentSched records for a given agent id.
   OperationID: GetAgentSchedList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAgentSchedList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAgentSchedList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAgentSchedList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/GetAgentSchedList", {
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
   Summary: Invoke method GetSchedListForDefaultAgent
   Description: Get list of schedules for default agent.
   OperationID: GetSchedListForDefaultAgent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSchedListForDefaultAgent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSchedListForDefaultAgent(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/GetSchedListForDefaultAgent", {
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
   Summary: Invoke method GetDefaultTaskAgentID
   Description: Returns the default Task Agent ID.
   OperationID: GetDefaultTaskAgentID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultTaskAgentID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultTaskAgentID(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/GetDefaultTaskAgentID", {
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
   Summary: Invoke method GetDefaultTaskAgent
   Description: Gets the default task agent.  If no SysAgent record exists will return an empty tableset.
   OperationID: GetDefaultTaskAgent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultTaskAgent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultTaskAgent(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/GetDefaultTaskAgent", {
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
   Summary: Invoke method RetryTask
   Description: Queues a task to be reran at configured intervals set up to the maximum amount of allowed attempts.
   OperationID: RetryTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RetryTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetryTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RetryTask(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/RetryTask", {
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
   Summary: Invoke method GetNewSysAgent
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSysAgent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSysAgent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSysAgent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSysAgent(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/GetNewSysAgent", {
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
   Summary: Invoke method GetNewSysAgentSched
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSysAgentSched
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSysAgentSched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSysAgentSched_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSysAgentSched(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/GetNewSysAgentSched", {
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
   Summary: Invoke method GetNewSysAgentTask
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSysAgentTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSysAgentTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSysAgentTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSysAgentTask(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/GetNewSysAgentTask", {
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
   Summary: Invoke method GetNewSysAgentTaskParam
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSysAgentTaskParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSysAgentTaskParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSysAgentTaskParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSysAgentTaskParam(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/GetNewSysAgentTaskParam", {
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
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/DeleteByID", {
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
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/GetBySysRowID" + params, {
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
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/GetBySysRowIDs" + params, {
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
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/Update", {
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
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_SysAgentListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentRow{
   "odatametadata":string,
   "value":Ice_Tablesets_SysAgentRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentSchedRow{
   "odatametadata":string,
   "value":Ice_Tablesets_SysAgentSchedRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentTaskParamRow{
   "odatametadata":string,
   "value":Ice_Tablesets_SysAgentTaskParamRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentTaskRow{
   "odatametadata":string,
   "value":Ice_Tablesets_SysAgentTaskRow[],
}

export interface Ice_Tablesets_SysAgentListRow{
      /**  System Agent Number  */  
   "AgentID":string,
      /**  System Agent Description  */  
   "AgentDesc":string,
      /**  System Agent Status  */  
   "AgentStatus":string,
      /**  System Agent started  */  
   "Started":boolean,
      /**  System Agent started by user  */  
   "StartUser":string,
      /**  Autostart System Agent  */  
   "AutoStart":boolean,
      /**  The delay between the time the agent is started and the time its schedules are processed  */  
   "ProcessingDelay":number,
      /**   Defines the root directory to user for files created by tasks run by this agent. This should be a shared directory, normally on the same machine as where the appserver is running. It should also be entered using UNC convention.
ex: \\mnsonoma\mfgsysdata  */  
   "FileRootDir":string,
      /**  The Maximum number of Simultaneous Tasks that the System Agent should submit to the Main AppServer.  Used to keep the System Agent from overloading the Main AppServer with reports and processes when the maximum number of agents is known.  */  
   "MaxSimultaneousTasks":number,
      /**  Menu Security Code  */  
   "SecCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "DTStartTime":string,
   "ClientFileRootDir":string,
   "ServerFileRootDir":string,
   "ClientProgRootDir":string,
      /**  Password to be used for ODBC connections  */  
   "ODBCPasswordPatchFld":string,
      /**  User ID to use for ODBC Connenctions (not a MfgSys user)  */  
   "ODBCUserIDPatchFld":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_SysAgentRow{
      /**  System Agent Number  */  
   "AgentID":string,
      /**  System Agent Description  */  
   "AgentDesc":string,
      /**  System Agent Status  */  
   "AgentStatus":string,
      /**  System Agent started  */  
   "Started":boolean,
      /**  StartedOn  */  
   "StartedOn":string,
      /**  System Agent started by user  */  
   "StartUser":string,
      /**  Autostart System Agent  */  
   "AutoStart":boolean,
      /**  The delay between the time the agent is started and the time its schedules are processed  */  
   "ProcessingDelay":number,
      /**  SysUserID  */  
   "SysUserID":string,
      /**  SysPassWord  */  
   "SysPassWord":string,
      /**   Defines the root directory to user for files created by tasks run by this agent. This should be a shared directory, normally on the same machine as where the appserver is running. It should also be entered using UNC convention.
ex: \\mnsonoma\mfgsysdata  */  
   "FileRootDir":string,
      /**  The Maximum number of Simultaneous Tasks that the System Agent should submit to the Main AppServer.  Used to keep the System Agent from overloading the Main AppServer with reports and processes when the maximum number of agents is known.  */  
   "MaxSimultaneousTasks":number,
      /**  Menu Security Code  */  
   "SecCode":string,
      /**  TaskPurgeIntervalDays  */  
   "TaskPurgeIntervalDays":number,
      /**  ReportPurgeIntervalTime  */  
   "ReportPurgeIntervalTime":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  SysAppserverURL  */  
   "SysAppserverURL":string,
      /**  SysDNSEndpointIdentity  */  
   "SysDNSEndpointIdentity":string,
   "ClientProgRootDir":string,
   "DTStartTime":string,
   "ServerFileRootDir":string,
      /**  Masked password field.  */  
   "SysPasswordMasked":string,
   "ClientFileRootDir":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_SysAgentSchedRow{
      /**  System Agent Number  */  
   "AgentID":string,
      /**  System Agent Scheduling Number  */  
   "AgentSchedNum":number,
      /**  Schedule Description  */  
   "SchedDesc":string,
      /**  Once, Daily, Weekly, Monthly, Interval or Startup  */  
   "SchedType":string,
      /**  NextRunOn  */  
   "NextRunOn":string,
      /**  Recurrencies  */  
   "Recurrences":number,
      /**  The task Agent will not run a task which has an effective date > the current date.  */  
   "EffectiveDate":string,
      /**  Used for montly schedules indicating a if they want to  schedule for a specific day of the month or by a specific week day withing a specific week of a month. Valid values are "Day, Week"  */  
   "MonthlyOption":string,
      /**  Day of month that task is to be run. Pertains only to SchedType of Monthly. Values can be 1 - 31.  */  
   "DayOfMonth":number,
      /**  Qualifys the DayOfWeek for Monthly processes. Values can be; First, Second, Third, Fourth, Fifth, or Last.  */  
   "WeekOfMonth":string,
      /**  Pertains only to Monthly schedules which are not defined as a specific day of the month or Weekly schedules. Represents the day of week ( 1 = Sun.... 7 = Sat) that the  process will run on. For Monthly schedules the WeekOfMonth value is also used to determine the actual run date.  */  
   "DayOfWeek":number,
      /**  For Weekly Schedules. Indicates that this should be run every n number of weeks. This along with DayOfWeek is used to determine the actual run date.  */  
   "EveryNWeeks":number,
      /**  LastRunOn  */  
   "LastRunOn":string,
      /**   Indicates if scheduled to run on Mondays.
Pertains only to SchedType = Daily.  */  
   "Mondays":boolean,
      /**   Indicates if scheduled to run on Tuesdays.
Pertains only to SchedType = Daily  */  
   "Tuesdays":boolean,
      /**   Indicates if scheduled to run on Wednesdays.
Pertains only to SchedType =  Daily.  */  
   "Wednesdays":boolean,
      /**   Indicates if scheduled to run on Thurdays.
Pertains only to SchedType = Daily.  */  
   "Thursdays":boolean,
      /**   Indicates if scheduled to run on Fridays.
Pertains only to SchedType =Daily.  */  
   "Fridays":boolean,
      /**   Indicates if scheduled to run on Saturdays.
Pertains only to SchedType =  Daily  */  
   "Saturdays":boolean,
      /**   Indicates if scheduled to run on Sundays.
Pertains only to SchedType = Daily  */  
   "Sundays":boolean,
      /**  Enable flag  */  
   "Enabled":boolean,
      /**   Progress AppServer ConnectionID that this task is using.
Format: appserver-host::appserver-name::global-unique-id  */  
   "AppSrvConnectionID":string,
      /**  The interval of time (expressed as hhhmmss) that this schedule will be run. Example: Run Every 10 minutes would have a value of 0001000. Only pertains with SchedType = "Interval"  */  
   "IntervalTime":number,
      /**  Menu Security Code  */  
   "SecCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ProcessingStartedOn  */  
   "ProcessingStartedOn":string,
      /**  TimeZoneID  */  
   "TimeZoneID":string,
      /**  External field for Weekly Panel. Stores same value as DayOfWeek.  */  
   "DayOfWeekWeekly":number,
      /**  The interval of time (expressed as hhh) that this schedule will be run. Only pertains with SchedType = "Interval"  */  
   "IntervalTimeHours":number,
      /**  The minutes portion of the interval of time (expressed as mm) that this schedule will be run. Only pertains with SchedType = "Interval"  */  
   "IntervalTimeMinutes":number,
      /**  The seconds portion of the interval of time (expressed as ss) that this schedule will be run. Only pertains with SchedType = "Interval"  */  
   "IntervalTimeSeconds":number,
      /**  The next run on value in the schedules time zone.  */  
   "NextRunOnInTimeZone":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_SysAgentTaskParamRow{
      /**  System Agent Number  */  
   "AgentID":string,
      /**  System Agent Scheduling Number  */  
   "AgentSchedNum":number,
      /**  System Agent Task Number  */  
   "AgentTaskNum":number,
      /**  Parameter Name  */  
   "ParamName":string,
      /**  Parameter Label  */  
   "ParamLabel":string,
      /**  Date/Logical/Character/Integer/Decimal  */  
   "ParamDataType":string,
      /**  Parameter Character Value  */  
   "ParamCharacter":string,
      /**  Parameter Date Value  */  
   "ParamDate":string,
      /**  Parameter Logical Value  */  
   "ParamLogical":boolean,
      /**  Parameter Integer Value  */  
   "ParamInteger":number,
      /**  Parameter Decimal Value  */  
   "ParamDecimal":number,
      /**   Tokens are predefined values used to dynamically determine a value of a corresponding parameter.
Examples of valid tokens are; &FirstOfMonth, &EndOfMonth  */  
   "ParamToken":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ParamLong  */  
   "ParamLong":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_SysAgentTaskRow{
      /**  System Agent Number  */  
   "AgentID":string,
      /**  System Agent Scheduling Number  */  
   "AgentSchedNum":number,
      /**  System Agent Task Number  */  
   "AgentTaskNum":number,
      /**  System Task Description  */  
   "TaskDesc":string,
      /**  Valid Values:  Process, Report  */  
   "TaskType":string,
      /**  Run Procedure  */  
   "RunProcedure":string,
      /**  Method (internal procedure) of the "RunProcedure" that this task will perform.  */  
   "RunMethod":string,
      /**  SubmittedOn  */  
   "SubmittedOn":string,
      /**  Submitted by user  */  
   "SubmitUser":string,
      /**   Name of .net program which is used to maintain the parameters.
Example: Epicor.Mfg.UI.xx/xxxxxxx.dll  */  
   "ParamMaintProgram":string,
      /**  Current Company when the task was created.  */  
   "Company":string,
      /**  An optional descriptive note about this Task.  This value comes from the parameter TaskNote field.  */  
   "TaskNote":string,
      /**  ProcessSetSystemCode  */  
   "ProcessSetSystemCode":string,
      /**  Unique ID for Process  */  
   "ProcessID":string,
      /**  ProcessTask.SysTaskNum that originated the schedule  */  
   "ProcessTaskNum":number,
      /**  IsSystemTask  */  
   "IsSystemTask":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ProcessSetCompany  */  
   "ProcessSetCompany":string,
      /**  Next Run on  */  
   "NextRunOn":string,
   "SchedDesc":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param agentID
   */  
export interface DeleteByID_input{
   agentID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param agentID
   */  
export interface GetAgentSchedList_input{
      /**  Agent ID which you want the schedules for.  */  
   agentID:string,
}

export interface GetAgentSchedList_output{
   returnObj:Ice_Tablesets_SysAgentSchedListTableset[],
}

   /** Required : 
      @param agentID
   */  
export interface GetByID_input{
   agentID:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_SysAgentTableset[],
}

   /** Required : 
      @param agentID
      @param firstPass
   */  
export interface GetByIdForTaskAgent_input{
      /**  The agent identifier.  */  
   agentID:string,
      /**  Indicates if startup type schedules should be included.  */  
   firstPass:boolean,
}

export interface GetByIdForTaskAgent_output{
   returnObj:Ice_Tablesets_SysAgentTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_SysAgentTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_SysAgentTableset[],
}

export interface GetDefaultTaskAgentID_output{
parameters : {
      /**  output parameters  */  
   defaultAgentID:string,
}
}

export interface GetDefaultTaskAgent_output{
   returnObj:Ice_Tablesets_SysAgentTableset[],
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
   returnObj:Ice_Tablesets_SysAgentListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param agentID
   */  
export interface GetNewSysAgentSched_input{
   ds:Ice_Tablesets_SysAgentTableset[],
   agentID:string,
}

export interface GetNewSysAgentSched_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_SysAgentTableset[],
}
}

   /** Required : 
      @param ds
      @param agentID
      @param agentSchedNum
      @param agentTaskNum
   */  
export interface GetNewSysAgentTaskParam_input{
   ds:Ice_Tablesets_SysAgentTableset[],
   agentID:string,
   agentSchedNum:number,
   agentTaskNum:number,
}

export interface GetNewSysAgentTaskParam_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_SysAgentTableset[],
}
}

   /** Required : 
      @param ds
      @param agentID
      @param agentSchedNum
   */  
export interface GetNewSysAgentTask_input{
   ds:Ice_Tablesets_SysAgentTableset[],
   agentID:string,
   agentSchedNum:number,
}

export interface GetNewSysAgentTask_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_SysAgentTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewSysAgent_input{
   ds:Ice_Tablesets_SysAgentTableset[],
}

export interface GetNewSysAgent_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_SysAgentTableset[],
}
}

   /** Required : 
      @param whereClauseSysAgent
      @param whereClauseSysAgentSched
      @param whereClauseSysAgentTask
      @param whereClauseSysAgentTaskParam
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseSysAgent:string,
   whereClauseSysAgentSched:string,
   whereClauseSysAgentTask:string,
   whereClauseSysAgentTaskParam:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_SysAgentTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetSchedListForDefaultAgent_output{
   returnObj:Ice_Tablesets_SysAgentSchedListTableset[],
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

export interface Ice_Tablesets_SysAgentListRow{
      /**  System Agent Number  */  
   AgentID:string,
      /**  System Agent Description  */  
   AgentDesc:string,
      /**  System Agent Status  */  
   AgentStatus:string,
      /**  System Agent started  */  
   Started:boolean,
      /**  System Agent started by user  */  
   StartUser:string,
      /**  Autostart System Agent  */  
   AutoStart:boolean,
      /**  The delay between the time the agent is started and the time its schedules are processed  */  
   ProcessingDelay:number,
      /**   Defines the root directory to user for files created by tasks run by this agent. This should be a shared directory, normally on the same machine as where the appserver is running. It should also be entered using UNC convention.
ex: \\mnsonoma\mfgsysdata  */  
   FileRootDir:string,
      /**  The Maximum number of Simultaneous Tasks that the System Agent should submit to the Main AppServer.  Used to keep the System Agent from overloading the Main AppServer with reports and processes when the maximum number of agents is known.  */  
   MaxSimultaneousTasks:number,
      /**  Menu Security Code  */  
   SecCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   DTStartTime:string,
   ClientFileRootDir:string,
   ServerFileRootDir:string,
   ClientProgRootDir:string,
      /**  Password to be used for ODBC connections  */  
   ODBCPasswordPatchFld:string,
      /**  User ID to use for ODBC Connenctions (not a MfgSys user)  */  
   ODBCUserIDPatchFld:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SysAgentListTableset{
   SysAgentList:Ice_Tablesets_SysAgentListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_SysAgentRow{
      /**  System Agent Number  */  
   AgentID:string,
      /**  System Agent Description  */  
   AgentDesc:string,
      /**  System Agent Status  */  
   AgentStatus:string,
      /**  System Agent started  */  
   Started:boolean,
      /**  StartedOn  */  
   StartedOn:string,
      /**  System Agent started by user  */  
   StartUser:string,
      /**  Autostart System Agent  */  
   AutoStart:boolean,
      /**  The delay between the time the agent is started and the time its schedules are processed  */  
   ProcessingDelay:number,
      /**  SysUserID  */  
   SysUserID:string,
      /**  SysPassWord  */  
   SysPassWord:string,
      /**   Defines the root directory to user for files created by tasks run by this agent. This should be a shared directory, normally on the same machine as where the appserver is running. It should also be entered using UNC convention.
ex: \\mnsonoma\mfgsysdata  */  
   FileRootDir:string,
      /**  The Maximum number of Simultaneous Tasks that the System Agent should submit to the Main AppServer.  Used to keep the System Agent from overloading the Main AppServer with reports and processes when the maximum number of agents is known.  */  
   MaxSimultaneousTasks:number,
      /**  Menu Security Code  */  
   SecCode:string,
      /**  TaskPurgeIntervalDays  */  
   TaskPurgeIntervalDays:number,
      /**  ReportPurgeIntervalTime  */  
   ReportPurgeIntervalTime:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  SysAppserverURL  */  
   SysAppserverURL:string,
      /**  SysDNSEndpointIdentity  */  
   SysDNSEndpointIdentity:string,
   ClientProgRootDir:string,
   DTStartTime:string,
   ServerFileRootDir:string,
      /**  Masked password field.  */  
   SysPasswordMasked:string,
   ClientFileRootDir:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SysAgentSchedListRow{
      /**  System Agent Number  */  
   AgentID:string,
      /**  System Agent Scheduling Number  */  
   AgentSchedNum:number,
      /**  Schedule Description  */  
   SchedDesc:string,
      /**  Once, Daily, Weekly, Monthly, Interval or Startup  */  
   SchedType:string,
      /**  Recurrencies  */  
   Recurrences:number,
      /**  The task Agent will not run a task which has an effective date > the current date.  */  
   EffectiveDate:string,
      /**  Used for montly schedules indicating a if they want to  schedule for a specific day of the month or by a specific week day withing a specific week of a month. Valid values are "Day, Week"  */  
   MonthlyOption:string,
      /**  Day of month that task is to be run. Pertains only to SchedType of Monthly. Values can be 1 - 31.  */  
   DayOfMonth:number,
      /**  Qualifys the DayOfWeek for Monthly processes. Values can be; First, Second, Third, Fourth, Fifth, or Last.  */  
   WeekOfMonth:string,
      /**  Pertains only to Monthly schedules which are not defined as a specific day of the month or Weekly schedules. Represents the day of week ( 1 = Sun.... 7 = Sat) that the  process will run on. For Monthly schedules the WeekOfMonth value is also used to determine the actual run date.  */  
   DayOfWeek:number,
      /**  For Weekly Schedules. Indicates that this should be run every n number of weeks. This along with DayOfWeek is used to determine the actual run date.  */  
   EveryNWeeks:number,
      /**   Indicates if scheduled to run on Mondays.
Pertains only to SchedType = Daily.  */  
   Mondays:boolean,
      /**   Indicates if scheduled to run on Tuesdays.
Pertains only to SchedType = Daily  */  
   Tuesdays:boolean,
      /**   Indicates if scheduled to run on Wednesdays.
Pertains only to SchedType =  Daily.  */  
   Wednesdays:boolean,
      /**   Indicates if scheduled to run on Thurdays.
Pertains only to SchedType = Daily.  */  
   Thursdays:boolean,
      /**   Indicates if scheduled to run on Fridays.
Pertains only to SchedType =Daily.  */  
   Fridays:boolean,
      /**   Indicates if scheduled to run on Saturdays.
Pertains only to SchedType =  Daily  */  
   Saturdays:boolean,
      /**   Indicates if scheduled to run on Sundays.
Pertains only to SchedType = Daily  */  
   Sundays:boolean,
      /**  Enable flag  */  
   Enabled:boolean,
      /**   Progress AppServer ConnectionID that this task is using.
Format: appserver-host::appserver-name::global-unique-id  */  
   AppSrvConnectionID:string,
      /**  The interval of time (expressed as hhhmmss) that this schedule will be run. Example: Run Every 10 minutes would have a value of 0001000. Only pertains with SchedType = "Interval"  */  
   IntervalTime:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   DTNextRunTime:string,
   DTLastRunTime:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SysAgentSchedListTableset{
   SysAgentSchedList:Ice_Tablesets_SysAgentSchedListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_SysAgentSchedRow{
      /**  System Agent Number  */  
   AgentID:string,
      /**  System Agent Scheduling Number  */  
   AgentSchedNum:number,
      /**  Schedule Description  */  
   SchedDesc:string,
      /**  Once, Daily, Weekly, Monthly, Interval or Startup  */  
   SchedType:string,
      /**  NextRunOn  */  
   NextRunOn:string,
      /**  Recurrencies  */  
   Recurrences:number,
      /**  The task Agent will not run a task which has an effective date > the current date.  */  
   EffectiveDate:string,
      /**  Used for montly schedules indicating a if they want to  schedule for a specific day of the month or by a specific week day withing a specific week of a month. Valid values are "Day, Week"  */  
   MonthlyOption:string,
      /**  Day of month that task is to be run. Pertains only to SchedType of Monthly. Values can be 1 - 31.  */  
   DayOfMonth:number,
      /**  Qualifys the DayOfWeek for Monthly processes. Values can be; First, Second, Third, Fourth, Fifth, or Last.  */  
   WeekOfMonth:string,
      /**  Pertains only to Monthly schedules which are not defined as a specific day of the month or Weekly schedules. Represents the day of week ( 1 = Sun.... 7 = Sat) that the  process will run on. For Monthly schedules the WeekOfMonth value is also used to determine the actual run date.  */  
   DayOfWeek:number,
      /**  For Weekly Schedules. Indicates that this should be run every n number of weeks. This along with DayOfWeek is used to determine the actual run date.  */  
   EveryNWeeks:number,
      /**  LastRunOn  */  
   LastRunOn:string,
      /**   Indicates if scheduled to run on Mondays.
Pertains only to SchedType = Daily.  */  
   Mondays:boolean,
      /**   Indicates if scheduled to run on Tuesdays.
Pertains only to SchedType = Daily  */  
   Tuesdays:boolean,
      /**   Indicates if scheduled to run on Wednesdays.
Pertains only to SchedType =  Daily.  */  
   Wednesdays:boolean,
      /**   Indicates if scheduled to run on Thurdays.
Pertains only to SchedType = Daily.  */  
   Thursdays:boolean,
      /**   Indicates if scheduled to run on Fridays.
Pertains only to SchedType =Daily.  */  
   Fridays:boolean,
      /**   Indicates if scheduled to run on Saturdays.
Pertains only to SchedType =  Daily  */  
   Saturdays:boolean,
      /**   Indicates if scheduled to run on Sundays.
Pertains only to SchedType = Daily  */  
   Sundays:boolean,
      /**  Enable flag  */  
   Enabled:boolean,
      /**   Progress AppServer ConnectionID that this task is using.
Format: appserver-host::appserver-name::global-unique-id  */  
   AppSrvConnectionID:string,
      /**  The interval of time (expressed as hhhmmss) that this schedule will be run. Example: Run Every 10 minutes would have a value of 0001000. Only pertains with SchedType = "Interval"  */  
   IntervalTime:number,
      /**  Menu Security Code  */  
   SecCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ProcessingStartedOn  */  
   ProcessingStartedOn:string,
      /**  TimeZoneID  */  
   TimeZoneID:string,
      /**  External field for Weekly Panel. Stores same value as DayOfWeek.  */  
   DayOfWeekWeekly:number,
      /**  The interval of time (expressed as hhh) that this schedule will be run. Only pertains with SchedType = "Interval"  */  
   IntervalTimeHours:number,
      /**  The minutes portion of the interval of time (expressed as mm) that this schedule will be run. Only pertains with SchedType = "Interval"  */  
   IntervalTimeMinutes:number,
      /**  The seconds portion of the interval of time (expressed as ss) that this schedule will be run. Only pertains with SchedType = "Interval"  */  
   IntervalTimeSeconds:number,
      /**  The next run on value in the schedules time zone.  */  
   NextRunOnInTimeZone:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SysAgentTableset{
   SysAgent:Ice_Tablesets_SysAgentRow[],
   SysAgentSched:Ice_Tablesets_SysAgentSchedRow[],
   SysAgentTask:Ice_Tablesets_SysAgentTaskRow[],
   SysAgentTaskParam:Ice_Tablesets_SysAgentTaskParamRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_SysAgentTaskParamRow{
      /**  System Agent Number  */  
   AgentID:string,
      /**  System Agent Scheduling Number  */  
   AgentSchedNum:number,
      /**  System Agent Task Number  */  
   AgentTaskNum:number,
      /**  Parameter Name  */  
   ParamName:string,
      /**  Parameter Label  */  
   ParamLabel:string,
      /**  Date/Logical/Character/Integer/Decimal  */  
   ParamDataType:string,
      /**  Parameter Character Value  */  
   ParamCharacter:string,
      /**  Parameter Date Value  */  
   ParamDate:string,
      /**  Parameter Logical Value  */  
   ParamLogical:boolean,
      /**  Parameter Integer Value  */  
   ParamInteger:number,
      /**  Parameter Decimal Value  */  
   ParamDecimal:number,
      /**   Tokens are predefined values used to dynamically determine a value of a corresponding parameter.
Examples of valid tokens are; &FirstOfMonth, &EndOfMonth  */  
   ParamToken:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ParamLong  */  
   ParamLong:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SysAgentTaskRow{
      /**  System Agent Number  */  
   AgentID:string,
      /**  System Agent Scheduling Number  */  
   AgentSchedNum:number,
      /**  System Agent Task Number  */  
   AgentTaskNum:number,
      /**  System Task Description  */  
   TaskDesc:string,
      /**  Valid Values:  Process, Report  */  
   TaskType:string,
      /**  Run Procedure  */  
   RunProcedure:string,
      /**  Method (internal procedure) of the "RunProcedure" that this task will perform.  */  
   RunMethod:string,
      /**  SubmittedOn  */  
   SubmittedOn:string,
      /**  Submitted by user  */  
   SubmitUser:string,
      /**   Name of .net program which is used to maintain the parameters.
Example: Epicor.Mfg.UI.xx/xxxxxxx.dll  */  
   ParamMaintProgram:string,
      /**  Current Company when the task was created.  */  
   Company:string,
      /**  An optional descriptive note about this Task.  This value comes from the parameter TaskNote field.  */  
   TaskNote:string,
      /**  ProcessSetSystemCode  */  
   ProcessSetSystemCode:string,
      /**  Unique ID for Process  */  
   ProcessID:string,
      /**  ProcessTask.SysTaskNum that originated the schedule  */  
   ProcessTaskNum:number,
      /**  IsSystemTask  */  
   IsSystemTask:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ProcessSetCompany  */  
   ProcessSetCompany:string,
      /**  Next Run on  */  
   NextRunOn:string,
   SchedDesc:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_UpdExtSysAgentTableset{
   SysAgent:Ice_Tablesets_SysAgentRow[],
   SysAgentSched:Ice_Tablesets_SysAgentSchedRow[],
   SysAgentTask:Ice_Tablesets_SysAgentTaskRow[],
   SysAgentTaskParam:Ice_Tablesets_SysAgentTaskParamRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param purgeDate
   */  
export interface PurgeReports_input{
      /**  The purge date.  */  
   purgeDate:string,
}

export interface PurgeReports_output{
}

   /** Required : 
      @param purgeDate
   */  
export interface PurgeTaskHistory_input{
      /**  The purge date.  */  
   purgeDate:string,
}

export interface PurgeTaskHistory_output{
}

   /** Required : 
      @param agentId
      @param scheduleNum
   */  
export interface ResetScheduleProcessingStartedOn_input{
      /**  The agent identifier.  */  
   agentId:string,
      /**  The schedule number.  */  
   scheduleNum:number,
}

export interface ResetScheduleProcessingStartedOn_output{
}

   /** Required : 
      @param sysTaskNum
   */  
export interface RetryTask_input{
   sysTaskNum:number,
}

export interface RetryTask_output{
}

   /** Required : 
      @param agentId
   */  
export interface SetSysAgentStatusToStarted_input{
   agentId:string,
}

export interface SetSysAgentStatusToStarted_output{
      /**  False if the given Agent ID does not exist, otherwise true.  */  
   returnObj:boolean,
}

   /** Required : 
      @param AgentID
      @param killRunningTasks
   */  
export interface SetSysAgentStatusToStopped_input{
      /**  The agent identifier.  */  
   AgentID:string,
      /**  if set to `true` creates a SysTaskKill record for any running tasks.  */  
   killRunningTasks:boolean,
}

export interface SetSysAgentStatusToStopped_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtSysAgentTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtSysAgentTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_SysAgentTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_SysAgentTableset[],
}
}

