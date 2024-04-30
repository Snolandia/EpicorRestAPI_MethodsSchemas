import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.BO.ProcessTaskSvc
// Description: The process task service.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/$metadata", {
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
   Description: Get ProcessTasks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ProcessTasks
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ProcessTaskRow
   */  
export function get_ProcessTasks(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ProcessTaskRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/ProcessTasks", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ProcessTaskRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ProcessTasks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ProcessTaskRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.ProcessTaskRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessTasks(requestBody:Ice_Tablesets_ProcessTaskRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/ProcessTasks", {
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
   Summary: Calls GetByID to retrieve the ProcessTask item
   Description: Calls GetByID to retrieve the ProcessTask item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProcessTask
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ProcessID Desc: ProcessID   Required: True   Allow empty value : True
      @param SysTaskNum Desc: SysTaskNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ProcessTaskRow
   */  
export function get_ProcessTasks_Company_SystemCode_ProcessID_SysTaskNum(Company:string, SystemCode:string, ProcessID:string, SysTaskNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ProcessTaskRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/ProcessTasks(" + Company + "," + SystemCode + "," + ProcessID + "," + SysTaskNum + ")", {
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
         resolve(data as Ice_Tablesets_ProcessTaskRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ProcessTask for the service
   Description: Calls UpdateExt to update ProcessTask. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ProcessTask
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ProcessID Desc: ProcessID   Required: True   Allow empty value : True
      @param SysTaskNum Desc: SysTaskNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.ProcessTaskRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ProcessTasks_Company_SystemCode_ProcessID_SysTaskNum(Company:string, SystemCode:string, ProcessID:string, SysTaskNum:string, requestBody:Ice_Tablesets_ProcessTaskRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/ProcessTasks(" + Company + "," + SystemCode + "," + ProcessID + "," + SysTaskNum + ")", {
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
   Summary: Call UpdateExt to delete ProcessTask item
   Description: Call UpdateExt to delete ProcessTask item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ProcessTask
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ProcessID Desc: ProcessID   Required: True   Allow empty value : True
      @param SysTaskNum Desc: SysTaskNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ProcessTasks_Company_SystemCode_ProcessID_SysTaskNum(Company:string, SystemCode:string, ProcessID:string, SysTaskNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/ProcessTasks(" + Company + "," + SystemCode + "," + ProcessID + "," + SysTaskNum + ")", {
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
   Description: Get ProcessTaskParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ProcessTaskParams1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ProcessID Desc: ProcessID   Required: True   Allow empty value : True
      @param SysTaskNum Desc: SysTaskNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ProcessTaskParamRow
   */  
export function get_ProcessTasks_Company_SystemCode_ProcessID_SysTaskNum_ProcessTaskParams(Company:string, SystemCode:string, ProcessID:string, SysTaskNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ProcessTaskParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/ProcessTasks(" + Company + "," + SystemCode + "," + ProcessID + "," + SysTaskNum + ")/ProcessTaskParams", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ProcessTaskParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ProcessTaskParam item
   Description: Calls GetByID to retrieve the ProcessTaskParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProcessTaskParam1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ProcessID Desc: ProcessID   Required: True   Allow empty value : True
      @param SysTaskNum Desc: SysTaskNum   Required: True
      @param ParamName Desc: ParamName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ProcessTaskParamRow
   */  
export function get_ProcessTasks_Company_SystemCode_ProcessID_SysTaskNum_ProcessTaskParams_Company_SystemCode_ProcessID_SysTaskNum_ParamName(Company:string, SystemCode:string, ProcessID:string, SysTaskNum:string, ParamName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ProcessTaskParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/ProcessTasks(" + Company + "," + SystemCode + "," + ProcessID + "," + SysTaskNum + ")/ProcessTaskParams(" + Company + "," + SystemCode + "," + ProcessID + "," + SysTaskNum + "," + ParamName + ")", {
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
         resolve(data as Ice_Tablesets_ProcessTaskParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ProcessTaskParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ProcessTaskParams
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ProcessTaskParamRow
   */  
export function get_ProcessTaskParams(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ProcessTaskParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/ProcessTaskParams", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ProcessTaskParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ProcessTaskParams
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ProcessTaskParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.ProcessTaskParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessTaskParams(requestBody:Ice_Tablesets_ProcessTaskParamRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/ProcessTaskParams", {
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
   Summary: Calls GetByID to retrieve the ProcessTaskParam item
   Description: Calls GetByID to retrieve the ProcessTaskParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProcessTaskParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ProcessID Desc: ProcessID   Required: True   Allow empty value : True
      @param SysTaskNum Desc: SysTaskNum   Required: True
      @param ParamName Desc: ParamName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ProcessTaskParamRow
   */  
export function get_ProcessTaskParams_Company_SystemCode_ProcessID_SysTaskNum_ParamName(Company:string, SystemCode:string, ProcessID:string, SysTaskNum:string, ParamName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ProcessTaskParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/ProcessTaskParams(" + Company + "," + SystemCode + "," + ProcessID + "," + SysTaskNum + "," + ParamName + ")", {
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
         resolve(data as Ice_Tablesets_ProcessTaskParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ProcessTaskParam for the service
   Description: Calls UpdateExt to update ProcessTaskParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ProcessTaskParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ProcessID Desc: ProcessID   Required: True   Allow empty value : True
      @param SysTaskNum Desc: SysTaskNum   Required: True
      @param ParamName Desc: ParamName   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.ProcessTaskParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ProcessTaskParams_Company_SystemCode_ProcessID_SysTaskNum_ParamName(Company:string, SystemCode:string, ProcessID:string, SysTaskNum:string, ParamName:string, requestBody:Ice_Tablesets_ProcessTaskParamRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/ProcessTaskParams(" + Company + "," + SystemCode + "," + ProcessID + "," + SysTaskNum + "," + ParamName + ")", {
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
   Summary: Call UpdateExt to delete ProcessTaskParam item
   Description: Call UpdateExt to delete ProcessTaskParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ProcessTaskParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ProcessID Desc: ProcessID   Required: True   Allow empty value : True
      @param SysTaskNum Desc: SysTaskNum   Required: True
      @param ParamName Desc: ParamName   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ProcessTaskParams_Company_SystemCode_ProcessID_SysTaskNum_ParamName(Company:string, SystemCode:string, ProcessID:string, SysTaskNum:string, ParamName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/ProcessTaskParams(" + Company + "," + SystemCode + "," + ProcessID + "," + SysTaskNum + "," + ParamName + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ProcessTaskListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ProcessTaskListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ProcessTaskListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseProcessTask:string, whereClauseProcessTaskParam:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseProcessTask!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseProcessTask=" + whereClauseProcessTask
   }
   if(typeof whereClauseProcessTaskParam!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseProcessTaskParam=" + whereClauseProcessTaskParam
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(company:string, systemCode:string, processID:string, sysTaskNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof company!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "company=" + company
   }
   if(typeof systemCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "systemCode=" + systemCode
   }
   if(typeof processID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "processID=" + processID
   }
   if(typeof sysTaskNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "sysTaskNum=" + sysTaskNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/GetList" + params, {
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
   Summary: Invoke method GetNewProcessTask
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewProcessTask
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewProcessTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewProcessTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewProcessTask(requestBody:GetNewProcessTask_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewProcessTask_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/GetNewProcessTask", {
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
         resolve(data as GetNewProcessTask_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewProcessTaskParam
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewProcessTaskParam
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewProcessTaskParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewProcessTaskParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewProcessTaskParam(requestBody:GetNewProcessTaskParam_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewProcessTaskParam_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/GetNewProcessTaskParam", {
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
         resolve(data as GetNewProcessTaskParam_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ProcessTaskSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ProcessTaskListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ProcessTaskListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ProcessTaskParamRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ProcessTaskParamRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ProcessTaskRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ProcessTaskRow,
}

export interface Ice_Tablesets_ProcessTaskListRow{
      /**  SystemCode  */  
   "SystemCode":string,
      /**  Unique ID for Process  */  
   "ProcessID":string,
      /**  System Task Number  */  
   "SysTaskNum":number,
      /**  System Task Description  */  
   "TaskDescription":string,
      /**   Used to control what program is used to initiate the running of the program that this task is suppose to run.
Example: TextRpt will run Task/TextRpt.p
                 DSRpt will run Task/DataSetRpt.p  */  
   "TaskType":string,
      /**  StartedOn  */  
   "StartedOn":string,
      /**  EndedOn  */  
   "EndedOn":string,
      /**  Task submitted by user  */  
   "SubmitUser":string,
      /**  Values are; Active, Complete, Cancelled, Error.  */  
   "TaskStatus":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Task Agent ID  */  
   "AgentID":string,
      /**  Task Agent Scheduling Number  */  
   "AgentSchedNum":number,
      /**  Task Agent Task Number  */  
   "AgentTaskNum":number,
      /**  Task Run Procedure  */  
   "RunProcedure":string,
      /**  Values are "Agent" or "Client".  */  
   "InitiatorSource":string,
      /**  A message string that the processing program periodically updates to provide an indication of the activity that it is working on.  */  
   "ActivityMsg":string,
      /**  Indicates if this task is considered as Historical. This is primarily used for filtering of records. The System Task monitor will not show records which are marked as History = Yes.  As tasks complete sucessfully this field gets set to Yes. If they happen to have an error, this will be set by the user so they have a chance to acknowledge the error.  */  
   "History":boolean,
      /**  An optional descriptive note about this Task.  This value comes from the parameter TaskNote field.  */  
   "TaskNote":string,
      /**  LastActivityOn  */  
   "LastActivityOn":string,
      /**  AStores the Progess DB connection user number and the appserver Process ID. Very useful when trying to related a task to a progress appserver agent.  */  
   "UserPIDInfo":string,
      /**  Application that defined the task.  Only this application can update the task.  */  
   "SourceDLL":string,
      /**  Sequence  */  
   "Sequence":number,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ProcessTaskParamRow{
      /**  Company  */  
   "Company":string,
      /**  SystemCode  */  
   "SystemCode":string,
      /**  Unique ID for Process  */  
   "ProcessID":string,
      /**  System Task Number  */  
   "SysTaskNum":number,
      /**  Parameter Name  */  
   "ParamName":string,
      /**  Parameter Label  */  
   "ParamLabel":string,
      /**  Variable/Pre-Processor/TempTable/Parameter  */  
   "ParamType":string,
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
      /**   Tokens are predefined values used to dynamically determine a value of a corresponding parameter. This setting of a parameter field based on a token is performed in the systaskparam write trigger.
Examples of valid tokens are; &FirstOfMonth, &EndOfMonth  */  
   "ParamToken":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
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

export interface Ice_Tablesets_ProcessTaskRow{
      /**  SystemCode  */  
   "SystemCode":string,
      /**  Unique ID for Process  */  
   "ProcessID":string,
      /**  System Task Number  */  
   "SysTaskNum":number,
      /**  System Task Description  */  
   "TaskDescription":string,
      /**   Used to control what program is used to initiate the running of the program that this task is suppose to run.
Example: TextRpt will run Task/TextRpt.p
                 DSRpt will run Task/DataSetRpt.p  */  
   "TaskType":string,
      /**  StartedOn  */  
   "StartedOn":string,
      /**  EndedOn  */  
   "EndedOn":string,
      /**  Task submitted by user  */  
   "SubmitUser":string,
      /**  Values are; Active, Complete, Cancelled, Error.  */  
   "TaskStatus":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Task Agent ID  */  
   "AgentID":string,
      /**  Task Agent Scheduling Number  */  
   "AgentSchedNum":number,
      /**  Task Agent Task Number  */  
   "AgentTaskNum":number,
      /**  Task Run Procedure  */  
   "RunProcedure":string,
      /**  Values are "Agent" or "Client".  */  
   "InitiatorSource":string,
      /**  A message string that the processing program periodically updates to provide an indication of the activity that it is working on.  */  
   "ActivityMsg":string,
      /**  Indicates if this task is considered as Historical. This is primarily used for filtering of records. The System Task monitor will not show records which are marked as History = Yes.  As tasks complete sucessfully this field gets set to Yes. If they happen to have an error, this will be set by the user so they have a chance to acknowledge the error.  */  
   "History":boolean,
      /**  An optional descriptive note about this Task.  This value comes from the parameter TaskNote field.  */  
   "TaskNote":string,
      /**  LastActivityOn  */  
   "LastActivityOn":string,
      /**  AStores the Progess DB connection user number and the appserver Process ID. Very useful when trying to related a task to a progress appserver agent.  */  
   "UserPIDInfo":string,
      /**  Application that defined the task.  Only this application can update the task.  */  
   "SourceDLL":string,
      /**  Sequence  */  
   "Sequence":number,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
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
      @param company
      @param systemCode
      @param processID
      @param sysTaskNum
   */  
export interface DeleteByID_input{
   company:string,
   systemCode:string,
   processID:string,
   sysTaskNum:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param company
      @param systemCode
      @param processID
      @param sysTaskNum
   */  
export interface GetByID_input{
   company:string,
   systemCode:string,
   processID:string,
   sysTaskNum:number,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_ProcessTaskTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_ProcessTaskTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_ProcessTaskTableset[],
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
   returnObj:Ice_Tablesets_ProcessTaskListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param company
      @param systemCode
      @param processID
      @param sysTaskNum
   */  
export interface GetNewProcessTaskParam_input{
   ds:Ice_Tablesets_ProcessTaskTableset[],
   company:string,
   systemCode:string,
   processID:string,
   sysTaskNum:number,
}

export interface GetNewProcessTaskParam_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ProcessTaskTableset,
}
}

   /** Required : 
      @param ds
      @param company
      @param systemCode
      @param processID
   */  
export interface GetNewProcessTask_input{
   ds:Ice_Tablesets_ProcessTaskTableset[],
   company:string,
   systemCode:string,
   processID:string,
}

export interface GetNewProcessTask_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ProcessTaskTableset,
}
}

   /** Required : 
      @param whereClauseProcessTask
      @param whereClauseProcessTaskParam
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseProcessTask:string,
   whereClauseProcessTaskParam:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_ProcessTaskTableset[],
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

export interface Ice_Tablesets_ProcessTaskListRow{
      /**  SystemCode  */  
   SystemCode:string,
      /**  Unique ID for Process  */  
   ProcessID:string,
      /**  System Task Number  */  
   SysTaskNum:number,
      /**  System Task Description  */  
   TaskDescription:string,
      /**   Used to control what program is used to initiate the running of the program that this task is suppose to run.
Example: TextRpt will run Task/TextRpt.p
                 DSRpt will run Task/DataSetRpt.p  */  
   TaskType:string,
      /**  StartedOn  */  
   StartedOn:string,
      /**  EndedOn  */  
   EndedOn:string,
      /**  Task submitted by user  */  
   SubmitUser:string,
      /**  Values are; Active, Complete, Cancelled, Error.  */  
   TaskStatus:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Task Agent ID  */  
   AgentID:string,
      /**  Task Agent Scheduling Number  */  
   AgentSchedNum:number,
      /**  Task Agent Task Number  */  
   AgentTaskNum:number,
      /**  Task Run Procedure  */  
   RunProcedure:string,
      /**  Values are "Agent" or "Client".  */  
   InitiatorSource:string,
      /**  A message string that the processing program periodically updates to provide an indication of the activity that it is working on.  */  
   ActivityMsg:string,
      /**  Indicates if this task is considered as Historical. This is primarily used for filtering of records. The System Task monitor will not show records which are marked as History = Yes.  As tasks complete sucessfully this field gets set to Yes. If they happen to have an error, this will be set by the user so they have a chance to acknowledge the error.  */  
   History:boolean,
      /**  An optional descriptive note about this Task.  This value comes from the parameter TaskNote field.  */  
   TaskNote:string,
      /**  LastActivityOn  */  
   LastActivityOn:string,
      /**  AStores the Progess DB connection user number and the appserver Process ID. Very useful when trying to related a task to a progress appserver agent.  */  
   UserPIDInfo:string,
      /**  Application that defined the task.  Only this application can update the task.  */  
   SourceDLL:string,
      /**  Sequence  */  
   Sequence:number,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ProcessTaskListTableset{
   ProcessTaskList:Ice_Tablesets_ProcessTaskListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_ProcessTaskParamRow{
      /**  Company  */  
   Company:string,
      /**  SystemCode  */  
   SystemCode:string,
      /**  Unique ID for Process  */  
   ProcessID:string,
      /**  System Task Number  */  
   SysTaskNum:number,
      /**  Parameter Name  */  
   ParamName:string,
      /**  Parameter Label  */  
   ParamLabel:string,
      /**  Variable/Pre-Processor/TempTable/Parameter  */  
   ParamType:string,
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
      /**   Tokens are predefined values used to dynamically determine a value of a corresponding parameter. This setting of a parameter field based on a token is performed in the systaskparam write trigger.
Examples of valid tokens are; &FirstOfMonth, &EndOfMonth  */  
   ParamToken:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
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

export interface Ice_Tablesets_ProcessTaskRow{
      /**  SystemCode  */  
   SystemCode:string,
      /**  Unique ID for Process  */  
   ProcessID:string,
      /**  System Task Number  */  
   SysTaskNum:number,
      /**  System Task Description  */  
   TaskDescription:string,
      /**   Used to control what program is used to initiate the running of the program that this task is suppose to run.
Example: TextRpt will run Task/TextRpt.p
                 DSRpt will run Task/DataSetRpt.p  */  
   TaskType:string,
      /**  StartedOn  */  
   StartedOn:string,
      /**  EndedOn  */  
   EndedOn:string,
      /**  Task submitted by user  */  
   SubmitUser:string,
      /**  Values are; Active, Complete, Cancelled, Error.  */  
   TaskStatus:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Task Agent ID  */  
   AgentID:string,
      /**  Task Agent Scheduling Number  */  
   AgentSchedNum:number,
      /**  Task Agent Task Number  */  
   AgentTaskNum:number,
      /**  Task Run Procedure  */  
   RunProcedure:string,
      /**  Values are "Agent" or "Client".  */  
   InitiatorSource:string,
      /**  A message string that the processing program periodically updates to provide an indication of the activity that it is working on.  */  
   ActivityMsg:string,
      /**  Indicates if this task is considered as Historical. This is primarily used for filtering of records. The System Task monitor will not show records which are marked as History = Yes.  As tasks complete sucessfully this field gets set to Yes. If they happen to have an error, this will be set by the user so they have a chance to acknowledge the error.  */  
   History:boolean,
      /**  An optional descriptive note about this Task.  This value comes from the parameter TaskNote field.  */  
   TaskNote:string,
      /**  LastActivityOn  */  
   LastActivityOn:string,
      /**  AStores the Progess DB connection user number and the appserver Process ID. Very useful when trying to related a task to a progress appserver agent.  */  
   UserPIDInfo:string,
      /**  Application that defined the task.  Only this application can update the task.  */  
   SourceDLL:string,
      /**  Sequence  */  
   Sequence:number,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ProcessTaskTableset{
   ProcessTask:Ice_Tablesets_ProcessTaskRow[],
   ProcessTaskParam:Ice_Tablesets_ProcessTaskParamRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UpdExtProcessTaskTableset{
   ProcessTask:Ice_Tablesets_ProcessTaskRow[],
   ProcessTaskParam:Ice_Tablesets_ProcessTaskParamRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtProcessTaskTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtProcessTaskTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_ProcessTaskTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ProcessTaskTableset,
}
}

