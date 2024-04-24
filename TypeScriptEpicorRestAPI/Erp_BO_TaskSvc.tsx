import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.TaskSvc
// Description: The Task main object.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/$metadata", {
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
   Description: Get Tasks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Tasks
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskRow
   */  
export function get_Tasks(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/Tasks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Tasks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaskRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaskRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Tasks(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/Tasks", {
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
   Summary: Calls GetByID to retrieve the Task item
   Description: Calls GetByID to retrieve the Task item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Task
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param TaskSeqNum Desc: TaskSeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaskRow
   */  
export function get_Tasks_Company_RelatedToFile_Key1_Key2_Key3_TaskSeqNum(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, TaskSeqNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaskRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/Tasks(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + TaskSeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TaskRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Task for the service
   Description: Calls UpdateExt to update Task. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Task
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param TaskSeqNum Desc: TaskSeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaskRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Tasks_Company_RelatedToFile_Key1_Key2_Key3_TaskSeqNum(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, TaskSeqNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/Tasks(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + TaskSeqNum + ")", {
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
   Summary: Call UpdateExt to delete Task item
   Description: Call UpdateExt to delete Task item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Task
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param TaskSeqNum Desc: TaskSeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Tasks_Company_RelatedToFile_Key1_Key2_Key3_TaskSeqNum(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, TaskSeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/Tasks(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + TaskSeqNum + ")", {
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
   Description: Get TaskCnts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaskCnts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param TaskSeqNum Desc: TaskSeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskCntRow
   */  
export function get_Tasks_Company_RelatedToFile_Key1_Key2_Key3_TaskSeqNum_TaskCnts(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, TaskSeqNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskCntRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/Tasks(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + TaskSeqNum + ")/TaskCnts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskCntRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TaskCnt item
   Description: Calls GetByID to retrieve the TaskCnt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaskCnt1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param TaskSeqNum Desc: TaskSeqNum   Required: True
      @param PerConLnkRowID Desc: PerConLnkRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaskCntRow
   */  
export function get_Tasks_Company_RelatedToFile_Key1_Key2_Key3_TaskSeqNum_TaskCnts_Company_RelatedToFile_Key1_Key2_Key3_TaskSeqNum_PerConLnkRowID(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, TaskSeqNum:string, PerConLnkRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaskCntRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/Tasks(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + TaskSeqNum + ")/TaskCnts(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + TaskSeqNum + "," + PerConLnkRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TaskCntRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get TaskCnts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaskCnts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskCntRow
   */  
export function get_TaskCnts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskCntRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/TaskCnts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskCntRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaskCnts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaskCntRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaskCntRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TaskCnts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/TaskCnts", {
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
   Summary: Calls GetByID to retrieve the TaskCnt item
   Description: Calls GetByID to retrieve the TaskCnt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaskCnt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param TaskSeqNum Desc: TaskSeqNum   Required: True
      @param PerConLnkRowID Desc: PerConLnkRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaskCntRow
   */  
export function get_TaskCnts_Company_RelatedToFile_Key1_Key2_Key3_TaskSeqNum_PerConLnkRowID(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, TaskSeqNum:string, PerConLnkRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaskCntRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/TaskCnts(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + TaskSeqNum + "," + PerConLnkRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TaskCntRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TaskCnt for the service
   Description: Calls UpdateExt to update TaskCnt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaskCnt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param TaskSeqNum Desc: TaskSeqNum   Required: True
      @param PerConLnkRowID Desc: PerConLnkRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaskCntRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TaskCnts_Company_RelatedToFile_Key1_Key2_Key3_TaskSeqNum_PerConLnkRowID(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, TaskSeqNum:string, PerConLnkRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/TaskCnts(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + TaskSeqNum + "," + PerConLnkRowID + ")", {
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
   Summary: Call UpdateExt to delete TaskCnt item
   Description: Call UpdateExt to delete TaskCnt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaskCnt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param TaskSeqNum Desc: TaskSeqNum   Required: True
      @param PerConLnkRowID Desc: PerConLnkRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TaskCnts_Company_RelatedToFile_Key1_Key2_Key3_TaskSeqNum_PerConLnkRowID(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, TaskSeqNum:string, PerConLnkRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/TaskCnts(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + TaskSeqNum + "," + PerConLnkRowID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseTask:string, whereClauseTaskCnt:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseTask!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTask=" + whereClauseTask
   }
   if(typeof whereClauseTaskCnt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTaskCnt=" + whereClauseTaskCnt
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(relatedToFile:string, key1:string, key2:string, key3:string, taskSeqNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof relatedToFile!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "relatedToFile=" + relatedToFile
   }
   if(typeof key1!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key1=" + key1
   }
   if(typeof key2!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key2=" + key2
   }
   if(typeof key3!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key3=" + key3
   }
   if(typeof taskSeqNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "taskSeqNum=" + taskSeqNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/GetList" + params, {
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
   Description: GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/GetCodeDescList", {
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
   Summary: Invoke method AssignDefaultsFromQuote
   Description: Assigns defaults for the task when is created from a Quote.
   OperationID: AssignDefaultsFromQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignDefaultsFromQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignDefaultsFromQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssignDefaultsFromQuote(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/AssignDefaultsFromQuote", {
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
   Summary: Invoke method ChangeCompleteIncludingNextTaskWarning
   Description: Executes thw Changecomplete logic and provides an optional warning message for quotes that have subsequent tasks and more than one task will be updateable.
Use this method when you want the additional message sent back to the client.
   OperationID: ChangeCompleteIncludingNextTaskWarning
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCompleteIncludingNextTaskWarning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCompleteIncludingNextTaskWarning_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCompleteIncludingNextTaskWarning(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ChangeCompleteIncludingNextTaskWarning", {
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
   Summary: Invoke method ChangeVoid
   Description: Performs next task check when the void column is changed.
   OperationID: ChangeVoid
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVoid_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVoid_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVoid(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ChangeVoid", {
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
   Summary: Invoke method ChangeComplete
   Description: Assigns defaults for the task when the complete field is checked.
   OperationID: ChangeComplete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeComplete(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ChangeComplete", {
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
   Summary: Invoke method ChangeVoided
   Description: Assigns defaults for the task when the task gets Voided.
   OperationID: ChangeVoided
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVoided_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVoided_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVoided(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ChangeVoided", {
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
   Summary: Invoke method ChangeConclusion
   Description: Assigns defaults for the task when the conclusion is changed.
   OperationID: ChangeConclusion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeConclusion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeConclusion_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeConclusion(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ChangeConclusion", {
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
   Summary: Invoke method ChangeConName
   Description: Update TaskCnt information when the contact Name is changed.
   OperationID: ChangeConName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeConName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeConName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeConName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ChangeConName", {
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
   Summary: Invoke method ChangeConPerConLnkRowID
   Description: Update TaskCnt information when the contact PerConLnkRowID is changed.
   OperationID: ChangeConPerConLnkRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeConPerConLnkRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeConPerConLnkRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeConPerConLnkRowID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ChangeConPerConLnkRowID", {
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
   Summary: Invoke method ChangeCustomer
   Description: Assigns defaults for the task when the customer changes.
   OperationID: ChangeCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCustomer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ChangeCustomer", {
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
   Summary: Invoke method ChangeCustomerContact
   Description: Assigns defaults for the task when the customer contact changes.
   OperationID: ChangeCustomerContact
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCustomerContact_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustomerContact_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCustomerContact(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ChangeCustomerContact", {
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
   Summary: Invoke method ChangeCustomerShipTo
   Description: Assigns defaults for the task when the customer changes.
   OperationID: ChangeCustomerShipTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCustomerShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustomerShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCustomerShipTo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ChangeCustomerShipTo", {
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
   Summary: Invoke method ChangeTaskShipToCust
   Description: Assigns defaults for the task when the customer ship to changes.
   OperationID: ChangeTaskShipToCust
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaskShipToCust_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaskShipToCust_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaskShipToCust(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ChangeTaskShipToCust", {
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
   Summary: Invoke method ChangeTaskShipToCustContact
   Description: ChangeTaskShipToCustContact
   OperationID: ChangeTaskShipToCustContact
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaskShipToCustContact_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaskShipToCustContact_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaskShipToCustContact(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ChangeTaskShipToCustContact", {
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
   Summary: Invoke method ChangeNextTaskSeq
   Description: Get the Next Task Description when the NextTaskSeq changes.
   OperationID: ChangeNextTaskSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeNextTaskSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeNextTaskSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeNextTaskSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ChangeNextTaskSeq", {
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
   Summary: Invoke method ChangeSalesRep
   Description: Assigns defaults for the task when the salesRep changes.
   OperationID: ChangeSalesRep
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSalesRep_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSalesRep_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSalesRep(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ChangeSalesRep", {
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
   Summary: Invoke method ChangeTaskID
   Description: Assigns defaults for the task when the task id changes.
   OperationID: ChangeTaskID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaskID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaskID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaskID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ChangeTaskID", {
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
   Summary: Invoke method ChangeTaskTimeDisp
   Description: Assigns the format for the task Start and End Time fields when their value changes.
   OperationID: ChangeTaskTimeDisp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaskTimeDisp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaskTimeDisp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaskTimeDisp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ChangeTaskTimeDisp", {
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
   Summary: Invoke method ChangeTEApprovalAction
   Description: Assigns defaults for the task when the time or expense approval action changes.
   OperationID: ChangeTEApprovalAction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTEApprovalAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTEApprovalAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTEApprovalAction(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ChangeTEApprovalAction", {
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
   Summary: Invoke method ValidateConclusion
   Description: Validates Task Conclusion
   OperationID: ValidateConclusion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateConclusion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateConclusion_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateConclusion(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ValidateConclusion", {
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
   Summary: Invoke method ValidateVendorID
   Description: Validate Vendor ID.
   OperationID: ValidateVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateVendorID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ValidateVendorID", {
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
   Summary: Invoke method ValidatePurPoint
   Description: Validate Vendor Purchase Point.
   OperationID: ValidatePurPoint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePurPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePurPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePurPoint(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ValidatePurPoint", {
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
   Summary: Invoke method ChangeVendor
   Description: Assigns defaults for the task when the vendor changes.
   OperationID: ChangeVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendor(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ChangeVendor", {
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
   Summary: Invoke method ChangeVendorContact
   Description: Assigns defaults for the task when the vendor contact changes.
   OperationID: ChangeVendorContact
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendorContact_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendorContact_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendorContact(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ChangeVendorContact", {
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
   Summary: Invoke method ChangeVendorPP
   Description: Assigns defaults for the task when the vendor purchase point changes.
   OperationID: ChangeVendorPP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendorPP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendorPP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendorPP(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ChangeVendorPP", {
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
   Summary: Invoke method CheckQuoteForCreditLimit
   OperationID: CheckQuoteForCreditLimit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckQuoteForCreditLimit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckQuoteForCreditLimit_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckQuoteForCreditLimit(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/CheckQuoteForCreditLimit", {
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
   Summary: Invoke method PutCustomerOnCreditHold
   Description: PutCustomerOnCreditHold
   OperationID: PutCustomerOnCreditHold
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PutCustomerOnCreditHold_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PutCustomerOnCreditHold_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PutCustomerOnCreditHold(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/PutCustomerOnCreditHold", {
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
   Summary: Invoke method GetCreditHoldMessageText
   Description: Retrieve the customer on credit hold message text.
   OperationID: GetCreditHoldMessageText
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCreditHoldMessageText_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCreditHoldMessageText_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCreditHoldMessageText(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/GetCreditHoldMessageText", {
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
   Summary: Invoke method GetDefaultEndDate
   OperationID: GetDefaultEndDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultEndDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultEndDate(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/GetDefaultEndDate", {
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
   Summary: Invoke method GetListApprovers
   Description: This method returns a list of Tasks to be viewed in the Task List screen based
a Sales Representative, Date Range, and sort options.  This method builds the where
clause instead of having the UI build the where clause on their end.  Although either
method could be used to build the Tree.
   OperationID: GetListApprovers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListApprovers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListApprovers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListApprovers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/GetListApprovers", {
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
   Summary: Invoke method GetQuoteLinesWOQtyMessageText
   Description: This method returns the message text for the case where there aren't any quote
lines with an order quantity.
   OperationID: GetQuoteLinesWOQtyMessageText
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuoteLinesWOQtyMessageText_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQuoteLinesWOQtyMessageText(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/GetQuoteLinesWOQtyMessageText", {
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
   Summary: Invoke method ExistsUncompletedTasks
   Description: This method returns a true if there are remaining uncompleted tasks
   OperationID: ExistsUncompletedTasks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsUncompletedTasks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsUncompletedTasks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExistsUncompletedTasks(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ExistsUncompletedTasks", {
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
   Summary: Invoke method GetPrimarySalesRepForUser
   Description: Gets the primary sales rep for the user
   OperationID: GetPrimarySalesRepForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPrimarySalesRepForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPrimarySalesRepForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPrimarySalesRepForUser(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/GetPrimarySalesRepForUser", {
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
   Summary: Invoke method GetRemainUncompletedTasks
   Description: Retrieve yes/no regarding if there are ramain uncompleted milestone tasks in HDCase.
   OperationID: GetRemainUncompletedTasks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRemainUncompletedTasks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRemainUncompletedTasks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRemainUncompletedTasks(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/GetRemainUncompletedTasks", {
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
   Summary: Invoke method GetRowsContactTracker
   Description: Called from Contact tracker instead of GetRows for better performance
   OperationID: GetRowsContactTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsContactTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsContactTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsContactTracker(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/GetRowsContactTracker", {
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
   Summary: Invoke method GetRowsCustomerTracker
   Description: Called from Customer tracker instead of GetRows for better performance
   OperationID: GetRowsCustomerTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCustomerTracker(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/GetRowsCustomerTracker", {
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
   Summary: Invoke method GetTaskCnt
   Description: This method returns a list of Tasks to be viewed in the Task List screen based
a Sales Representative, Date Range, and sort options.  This method builds the where
clause instead of having the UI build the where clause on their end.  Although either
method could be used to build the Tree.
   OperationID: GetTaskCnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaskCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaskCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTaskCnt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/GetTaskCnt", {
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
   Summary: Invoke method GetTaskListByDateRange
   Description: This method returns a list of Tasks to be viewed in the Task List screen based
a Sales Representative, Date Range, and sort options.  This method builds the where
clause instead of having the UI build the where clause on their end.  Although either
method could be used to build the Tree.
   OperationID: GetTaskListByDateRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaskListByDateRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaskListByDateRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTaskListByDateRange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/GetTaskListByDateRange", {
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
   Summary: Invoke method GetTaskList
   Description: Deprecated method to get the list of Tasks to be viewed in the Task List screen based a Sales Representative, Date Range, and sort options.
   OperationID: GetTaskList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaskList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaskList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTaskList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/GetTaskList", {
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
   Summary: Invoke method GetCurrentTaskSeqNum
   Description: GetCurrentTaskSeqNum
   OperationID: GetCurrentTaskSeqNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCurrentTaskSeqNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentTaskSeqNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrentTaskSeqNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/GetCurrentTaskSeqNum", {
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
   Summary: Invoke method WorkFlowCompleteWithRemainingTask
   Description: Marks current Task as WorkflowComplete = true, and remaining tasks get completed
   OperationID: WorkFlowCompleteWithRemainingTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WorkFlowCompleteWithRemainingTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WorkFlowCompleteWithRemainingTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WorkFlowCompleteWithRemainingTask(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/WorkFlowCompleteWithRemainingTask", {
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
   Summary: Invoke method CheckTaskCanBeVoided
   Description: CheckTaskCanBeVoided
   OperationID: CheckTaskCanBeVoided
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTaskCanBeVoided_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTaskCanBeVoided_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckTaskCanBeVoided(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/CheckTaskCanBeVoided", {
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
   Summary: Invoke method CanCompleteWorkflow
   Description: CanCompleteWorkflow
   OperationID: CanCompleteWorkflow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CanCompleteWorkflow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CanCompleteWorkflow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CanCompleteWorkflow(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/CanCompleteWorkflow", {
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
   Summary: Invoke method TerritoryAuthorized
   Description: TerritoryAuthorized
   OperationID: TerritoryAuthorized
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TerritoryAuthorized_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TerritoryAuthorized_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TerritoryAuthorized(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/TerritoryAuthorized", {
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
   Summary: Invoke method VoidTask
   Description: Voids a task
   OperationID: VoidTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VoidTask(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/VoidTask", {
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
   Summary: Invoke method GetTaskTreeDataSet
   Description: Gets dataset for task tree view
   OperationID: GetTaskTreeDataSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaskTreeDataSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaskTreeDataSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTaskTreeDataSet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/GetTaskTreeDataSet", {
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
   Summary: Invoke method ExportFile
   Description: Export file
   OperationID: ExportFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/ExportFile", {
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
   Summary: Invoke method GetNewTask
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTask(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/GetNewTask", {
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
   Summary: Invoke method GetNewTaskCnt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaskCnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaskCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaskCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTaskCnt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/GetNewTaskCnt", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskCntRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaskCntRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaskListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaskRow[],
}

export interface Erp_Tablesets_TaskCntRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The master file to which the task is related. Opportunity/Quote, Customer, ECO Group etc...  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a task related to a quote (Customer) this field would contain the related Customer.CustNum value.  */  
   "Key1":string,
      /**  2nd component of the foreign key to the related master record.  */  
   "Key2":string,
      /**  3rd component of the foreign key to the related master record.  */  
   "Key3":string,
      /**  Used to uniquely identify the record. Used so more than 1 Task can exist for a given record. The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  */  
   "TaskSeqNum":number,
      /**  The SysRowId of the linked PerConLnk.  */  
   "PerConLnkRowID":string,
      /**  Primary contact for each Context type. Only one allowed per context type. The primary contact for each context type is shown on the detail sheet.  */  
   "Primary":boolean,
      /**  User entered comments.  */  
   "Comment":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "Address1":string,
   "Address2":string,
   "Address3":string,
   "BuyerID":string,
   "BuyerName":string,
   "City":string,
   "ContextLink":string,
   "CustID":string,
   "CustName":string,
   "EmpID":string,
   "EmpName":string,
   "Name":string,
   "PurPoint":string,
   "PurPointName":string,
   "SalesRepCode":string,
   "SalesRepName":string,
   "ShipToName":string,
   "ShipToNum":string,
   "State":string,
   "VendorID":string,
   "VendorName":string,
   "Zip":string,
   "PerConID":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TaskListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The master file to which the task is related.  Opportunity/Quote, Customer, ECO Group etc...  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a task related to a quote (Customer) this field would contain the related Customer.CustNum value.  */  
   "Key1":string,
      /**  2nd component of the foreign key to the related master record.  */  
   "Key2":string,
      /**  3rd component of the foreign key to the related master record.  */  
   "Key3":string,
      /**  Link to the TaskMast table. Contains the TaskMast.TaskID value related to this task.  */  
   "TaskID":string,
      /**  Used to uniquely identify the record.  Used so more than 1 Task can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  */  
   "TaskSeqNum":number,
      /**  Default description from the TaskMaster. TaskMast.TaskDescription. The user can override the default description for this specific task.  */  
   "TaskDescription":string,
      /**  The SalesRep that this task is assigned to. Will default from Role on TaskMaster  */  
   "SalesRepCode":string,
      /**  Defaults is TODAY.  */  
   "StartDate":string,
      /**  The Task should be completed by this date.  */  
   "DueDate":string,
      /**  Status Code. From TaskStat table  */  
   "StatusCode":string,
      /**  Percent of task that is complete.  Valid values are 0-100. User maintained.  */  
   "PercentComplete":number,
      /**  Indicates that this task is complete.  When checked this will trigger creation of the next task and the global alert process.  */  
   "Complete":boolean,
      /**  User entered completion date.  Default to TODAY when the complete flag is checked.  */  
   "CompleteDate":string,
      /**   The LOQ must be in this stage to be selected or it will be put in this stage if the LOQ is already past this stage.
Valid Choices are
Lead, Oppo = Opportunity, Quot = Quote.
Not maintainable  */  
   "CurrentStage":string,
      /**  This task must be completed before the LOQ can move to the next milestone.  Not maintainable as actual task  */  
   "Mandatory":boolean,
      /**  This task must be completed before the LOQ can move to the next Milestone.  Only one Milestone task can be active on a quote at one time.  Not maintainable as actual task.  */  
   "Milestone":boolean,
      /**  The date the task was created.  */  
   "CreateDate":string,
      /**  The UserID that created the task  */  
   "CreateDcdUserID":string,
      /**  The date the task was last changed.  */  
   "ChangeDate":string,
      /**  The UserID that last changed the task  */  
   "ChangeDcdUserID":string,
      /**  Completion of the task will send a Global Alert  */  
   "SendAlertComplete":boolean,
      /**  Valid values are 1 - 99 1 = HIGH,  99 = LOW  */  
   "PriorityCode":number,
      /**  Contains comments about the Task.  */  
   "TaskComment":string,
      /**  Valid values are "win" "lose" "next" "next" is the default .  This will display as a radio set.  If "win" is selected then completing this task will require a reason code from CRM Win type. A sales order will be created if all mandatory tasks at this milestone are complete.  If  "lose" is selected all tasks and the quote will close  and a CRM Lose reason code is required. If "next" is selected then the "next task" drop down is enabled and the list of possible next tasks from the task set(TaskSNxt) will be displayed, reason code will be optional  */  
   "Conclusion":string,
      /**  Select from list of Win or loss reason codes depending on the setting if the conclusion field  */  
   "ReasonCode":string,
      /**  When this task is completed and the conclusion is "next" this field will hold the next Milestone task to be created.  */  
   "NextTaskID":string,
      /**  Indentifies the nest milestone task sequence.  */  
   "NextTaskSeq":number,
      /**  The Quote that this Task is related to.  */  
   "TaskQuoteNum":number,
      /**  The Customer that this task is related to  */  
   "TaskCustNum":number,
      /**  The Customer Ship To that this task is related to  */  
   "TaskShipToNum":string,
      /**  The Customer contact that this Task is related to.  */  
   "TaskConNum":number,
      /**  Link to the task set.  */  
   "TaskSetID":string,
      /**  Link to the Task Set Detail  */  
   "TaskSetSeq":number,
      /**  Setting this when the opportunity is a "win" will trigger the logic that creates a sales order.  */  
   "CreateOrder":boolean,
      /**  Creation of the task will send a Global Alert  */  
   "SendAlertCreate":boolean,
      /**  Defines the type of task this is.  From the TaskType table.  */  
   "TypeCode":string,
      /**  The Vendor number associated with this task.  */  
   "TaskVendorNum":number,
      /**  The Vendor purchase point related to this task.  */  
   "TaskPurPoint":string,
      /**  The purchasing contact person associated with this task.  */  
   "TaskPrcConNum":number,
      /**  Link to the Marketing Campaign related to this Task.  */  
   "TaskMktgCampaignID":string,
      /**  A salesperson that the assigned salesperson needs to contact to complete this task  */  
   "OtherSalesRepCode":string,
      /**  Defines if this task is included in the Customer category.  Categories are used for selecting tasks for assignment to TaskSets.  */  
   "CustomerCategory":boolean,
      /**  Defines if this task is included in the Engineering category.  */  
   "EngineeringCategory":boolean,
      /**  Defines if this task is included in the Vendor category.  */  
   "VendorCategory":boolean,
      /**  Defines if this task is included in the Personal category.  */  
   "PersonalCategory":boolean,
      /**  Defines if this task is included in the Management category.  */  
   "ManagementCategory":boolean,
      /**  Defines if this task is included in the Other category.  */  
   "OtherCategory":boolean,
      /**  Role of person who would default as the owner of this task when the task is created. From the RoleCD table.  */  
   "RoleCode":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  EmployeeName  */  
   "EmployeeName":string,
      /**   Text to indicate if this task is for "Time" or "Expense" (translated text). Used only by Labor Approval
TaskList search for search results column.  */  
   "TimeOrExp":string,
      /**  ProjectID, used only by Task Time and Expense search as a search results grid.  */  
   "ProjectID":string,
      /**  Holds the date of the transaction that created the task, used by TimeExpense approval search form.  */  
   "TransDate":string,
      /**  JobNum, used only by task time and expense approbal search as search results grid  */  
   "JobNum":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TaskRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The master file to which the task is related.  Opportunity/Quote, Customer, ECO Group etc...  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a task related to a quote (Customer) this field would contain the related Customer.CustNum value.  */  
   "Key1":string,
      /**  2nd component of the foreign key to the related master record.  */  
   "Key2":string,
      /**  3rd component of the foreign key to the related master record.  */  
   "Key3":string,
      /**  Link to the TaskMast table. Contains the TaskMast.TaskID value related to this task.  */  
   "TaskID":string,
      /**  Used to uniquely identify the record.  Used so more than 1 Task can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  */  
   "TaskSeqNum":number,
      /**  Default description from the TaskMaster. TaskMast.TaskDescription. The user can override the default description for this specific task.  */  
   "TaskDescription":string,
      /**  The SalesRep that this task is assigned to. Will default from Role on TaskMaster  */  
   "SalesRepCode":string,
      /**  Defaults is TODAY.  */  
   "StartDate":string,
      /**  The Task should be completed by this date.  */  
   "DueDate":string,
      /**  Status Code. From TaskStat table  */  
   "StatusCode":string,
      /**  Percent of task that is complete.  Valid values are 0-100. User maintained.  */  
   "PercentComplete":number,
      /**  Indicates that this task is complete.  When checked this will trigger creation of the next task and the global alert process.  */  
   "Complete":boolean,
      /**  User entered completion date.  Default to TODAY when the complete flag is checked.  */  
   "CompleteDate":string,
      /**   The LOQ must be in this stage to be selected or it will be put in this stage if the LOQ is already past this stage.
Valid Choices are
Lead, Oppo = Opportunity, Quot = Quote.
Not maintainable  */  
   "CurrentStage":string,
      /**  This task must be completed before the LOQ can move to the next milestone.  Not maintainable as actual task  */  
   "Mandatory":boolean,
      /**  This task must be completed before the LOQ can move to the next Milestone.  Only one Milestone task can be active on a quote at one time.  Not maintainable as actual task.  */  
   "Milestone":boolean,
      /**  The date the task was created.  */  
   "CreateDate":string,
      /**  The UserID that created the task  */  
   "CreateDcdUserID":string,
      /**  The date the task was last changed.  */  
   "ChangeDate":string,
      /**  The UserID that last changed the task  */  
   "ChangeDcdUserID":string,
      /**  Completion of the task will send a Global Alert  */  
   "SendAlertComplete":boolean,
      /**  Valid values are 1 - 99 1 = HIGH,  99 = LOW  */  
   "PriorityCode":number,
      /**  Contains comments about the Task.  */  
   "TaskComment":string,
      /**  Valid values are "win" "lose" "next" "next" is the default .  This will display as a radio set.  If "win" is selected then completing this task will require a reason code from CRM Win type. A sales order will be created if all mandatory tasks at this milestone are complete.  If  "lose" is selected all tasks and the quote will close  and a CRM Lose reason code is required. If "next" is selected then the "next task" drop down is enabled and the list of possible next tasks from the task set(TaskSNxt) will be displayed, reason code will be optional  */  
   "Conclusion":string,
      /**  Select from list of Win or loss reason codes depending on the setting if the conclusion field  */  
   "ReasonCode":string,
      /**  When this task is completed and the conclusion is "next" this field will hold the next Milestone task to be created.  */  
   "NextTaskID":string,
      /**  Indentifies the nest milestone task sequence.  */  
   "NextTaskSeq":number,
      /**  The Quote that this Task is related to.  */  
   "TaskQuoteNum":number,
      /**  The Customer that this task is related to  */  
   "TaskCustNum":number,
      /**  The Customer Ship To that this task is related to  */  
   "TaskShipToNum":string,
      /**  The Customer contact that this Task is related to.  */  
   "TaskConNum":number,
      /**  Link to the task set.  */  
   "TaskSetID":string,
      /**  Link to the Task Set Detail  */  
   "TaskSetSeq":number,
      /**  Setting this when the opportunity is a "win" will trigger the logic that creates a sales order.  */  
   "CreateOrder":boolean,
      /**  Creation of the task will send a Global Alert  */  
   "SendAlertCreate":boolean,
      /**  Defines the type of task this is.  From the TaskType table.  */  
   "TypeCode":string,
      /**  The Vendor number associated with this task.  */  
   "TaskVendorNum":number,
      /**  The Vendor purchase point related to this task.  */  
   "TaskPurPoint":string,
      /**  The purchasing contact person associated with this task.  */  
   "TaskPrcConNum":number,
      /**  Link to the Marketing Campaign related to this Task.  */  
   "TaskMktgCampaignID":string,
      /**  A salesperson that the assigned salesperson needs to contact to complete this task  */  
   "OtherSalesRepCode":string,
      /**  Defines if this task is included in the Customer category.  Categories are used for selecting tasks for assignment to TaskSets.  */  
   "CustomerCategory":boolean,
      /**  Defines if this task is included in the Engineering category.  */  
   "EngineeringCategory":boolean,
      /**  Defines if this task is included in the Vendor category.  */  
   "VendorCategory":boolean,
      /**  Defines if this task is included in the Personal category.  */  
   "PersonalCategory":boolean,
      /**  Defines if this task is included in the Management category.  */  
   "ManagementCategory":boolean,
      /**  Defines if this task is included in the Other category.  */  
   "OtherCategory":boolean,
      /**  Role of person who would default as the owner of this task when the task is created. From the RoleCD table.  */  
   "RoleCode":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Start Time for task.  Stored as seconds from midnight  */  
   "StartTime":number,
      /**  End Time for task.  Stored as seconds from midnight  */  
   "EndTime":number,
      /**  For Time and Expense transactions, multiple persons within a Role can be assigned a Task to complete, and if ANY of these persons complete the Task, the Milestone is to be marked complete.  */  
   "AnyApprover":boolean,
      /**  The number of levels of supervisors above the employee where the approval responsibility lies.  Zero indicates the employee's supervisor does not approve.  One indicates the employee's supervisor (EmpBasic.SupervisorID) does approve. Two indicates that you need to find the employee's supervisor's supervisor, and so on.  */  
   "ApprovalSupervisorLevel":number,
      /**  Indicates if the Task has been Approved via Time and Expense Approval.  */  
   "Approved":boolean,
      /**   The action to take when the task is completed.  Applies to milestones only.  Used for time and expense tasks.  Values are:
SUB - Submit.  The time or expense record status is set to submitted when the milestone is complete.
APP - Approve.  The time or expense record is approved when the milestone is complete.  */  
   "CompletionAction":string,
      /**  Applies to milestones.  Auto complete the milestone when the related tasks are completed.  */  
   "AutoComplete":boolean,
      /**  Used for time and expense tasks.  Indicates the transaction the task is linked to will be marked as rejected when the task is completed.  */  
   "RejectApproval":boolean,
      /**  RelatedToSysRowID  */  
   "RelatedToSysRowID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  TaskShipToCustNum  */  
   "TaskShipToCustNum":number,
      /**  TaskShipToCustConNum  */  
   "TaskShipToCustConNum":number,
      /**  Voided  */  
   "Voided":boolean,
      /**  TaskPerConID  */  
   "TaskPerConID":number,
      /**  PrevTaskSetTask  */  
   "PrevTaskSetTask":boolean,
   "AllowUpdate":boolean,
      /**  Temporary display field for Change Time  */  
   "ChangeTimeDisp":string,
      /**  Current Stage Description  */  
   "CurrentStageDescription":string,
      /**  The customer ID.  */  
   "CustID":string,
   "CustomerContactFax":string,
   "CustomerContactName":string,
   "CustomerContactPhone":string,
      /**  The full customer's name.  */  
   "CustomerName":string,
      /**  The name for the ship to location.  */  
   "CustomerShipToName":string,
      /**  This is a boolean field to check if the Task is already completed or the user doesn't already complete the task.  */  
   "DisableOnComplete":boolean,
   "DisableTasks":boolean,
      /**  Temporary display field for End Time  */  
   "EndTimeDisp":string,
   "FilterIncludeComplete":boolean,
   "FilterStartAtDate":string,
   "FilterStartAtQuote":number,
   "FilterTaskType":string,
   "FilterType":string,
   "IsLoseable":boolean,
   "IsWinnable":boolean,
   "NewMilestoneTaskSeqNum":number,
   "NextStage":string,
   "NextTaskList":string,
   "OrigMilestoneTaskSeqNum":number,
   "OtherSalesRepName":string,
   "PromptCustCreditHoldWarning":boolean,
   "PromptQuoteLinesWOQty":boolean,
   "ReasonList":string,
      /**  Reject Approval Allowed - this option is available only for time and expense tasks  */  
   "RejectAppAllowed":boolean,
      /**  Name of the Sales Representative.  */  
   "SalesRepName":string,
      /**  Temporary display field for Start Time  */  
   "StartTimeDisp":string,
      /**  Indicates if the password to complete the task is valid.  */  
   "TaskCompletePasswordIsValid":boolean,
      /**  Indicates if a password is required to complete the task  */  
   "TaskCompletePasswordRequired":boolean,
   "TaskShipToCustConName":string,
   "TaskShipToCustID":string,
   "TaskShipToCustName":string,
      /**  This Column will store the value of the flag Customer.AllowShipTo3 for Task SoldTo Customers  */  
   "TaskSoldToCustNumAllowsShipTo3":boolean,
      /**  Indicates whether a time or expense task is being approved or rejected.  */  
   "TEApprovalAction":string,
      /**  Indicates if this is a time or expense task.  UI fields are enabled/disasbled based on this.  */  
   "TETask":boolean,
   "VendorContactEmail":string,
   "VendorContactFax":string,
   "VendorContactName":string,
   "VendorContactPhone":string,
   "VendorID":string,
   "VendorName":string,
   "WFCompleteAllowed":boolean,
   "WorkflowComplete":boolean,
   "CustomerContactEmail":string,
      /**  Used in Quote to verify if the task can be voided.  */  
   "CanBeVoided":boolean,
      /**  List of conclusion options  */  
   "ConclusionList":string,
   "BitFlag":number,
   "ChangeDcdUserIDName":string,
   "ReasonCodeHDDescription":string,
   "RoleCodeRoleDescription":string,
   "ShipToNumInactive":boolean,
   "StatusCodeStatusDescription":string,
   "TaskConNumNameMiddleName":string,
   "TaskConNumNameLastName":string,
   "TaskConNumNameFirstName":string,
   "TaskConNumNameName":string,
   "TaskConNumNameCorpName":string,
   "TaskConNumNameFaxNum":string,
   "TaskConNumNamePhoneNum":string,
   "TaskCustNumInactive":boolean,
   "TaskIDTaskDescription":string,
   "TaskSetIDWorkflowType":string,
   "TaskSetIDTaskSetDescription":string,
   "TaskSetSeqTaskDescription":string,
   "TypeCodeTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param quoteNum
      @param ds
   */  
export interface AssignDefaultsFromQuote_input{
      /**  Num of quote to assign values  */  
   quoteNum:number,
   ds:Erp_Tablesets_TaskTableset[],
}

export interface AssignDefaultsFromQuote_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param cRowIdent
   */  
export interface CanCompleteWorkflow_input{
      /**  SysRowID  */  
   cRowIdent:string,
}

export interface CanCompleteWorkflow_output{
   returnObj:boolean,
}

   /** Required : 
      @param ds
      @param lProposedComplete
   */  
export interface ChangeCompleteIncludingNextTaskWarning_input{
   ds:Erp_Tablesets_TaskTableset[],
      /**  The proposed value for the complete flag  */  
   lProposedComplete:boolean,
}

export interface ChangeCompleteIncludingNextTaskWarning_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
   cMessage:string,
   nextTaskWarning:string,
}
}

   /** Required : 
      @param ds
      @param lProposedComplete
   */  
export interface ChangeComplete_input{
   ds:Erp_Tablesets_TaskTableset[],
      /**  The proposed value for the complete flag  */  
   lProposedComplete:boolean,
}

export interface ChangeComplete_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
   cMessage:string,
}
}

   /** Required : 
      @param pName
      @param ds
   */  
export interface ChangeConName_input{
      /**  Proposed Name  */  
   pName:string,
   ds:Erp_Tablesets_TaskTableset[],
}

export interface ChangeConName_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param pPerConLnkRowID
      @param ds
   */  
export interface ChangeConPerConLnkRowID_input{
      /**  Proposed PerConLnkRowID  */  
   pPerConLnkRowID:string,
   ds:Erp_Tablesets_TaskTableset[],
}

export interface ChangeConPerConLnkRowID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeConclusion_input{
   ds:Erp_Tablesets_TaskTableset[],
}

export interface ChangeConclusion_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeCustomerContact_input{
   ds:Erp_Tablesets_TaskTableset[],
}

export interface ChangeCustomerContact_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeCustomerShipTo_input{
   ds:Erp_Tablesets_TaskTableset[],
}

export interface ChangeCustomerShipTo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeCustomer_input{
   ds:Erp_Tablesets_TaskTableset[],
}

export interface ChangeCustomer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeNextTaskSeq_input{
   ds:Erp_Tablesets_TaskTableset[],
}

export interface ChangeNextTaskSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeSalesRep_input{
   ds:Erp_Tablesets_TaskTableset[],
}

export interface ChangeSalesRep_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param ds
      @param lProposedTEApprovalAction
   */  
export interface ChangeTEApprovalAction_input{
   ds:Erp_Tablesets_TaskTableset[],
      /**  The proposed value for approval action  */  
   lProposedTEApprovalAction:string,
}

export interface ChangeTEApprovalAction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeTaskID_input{
   ds:Erp_Tablesets_TaskTableset[],
}

export interface ChangeTaskID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeTaskShipToCustContact_input{
   ds:Erp_Tablesets_TaskTableset[],
}

export interface ChangeTaskShipToCustContact_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeTaskShipToCust_input{
   ds:Erp_Tablesets_TaskTableset[],
}

export interface ChangeTaskShipToCust_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeTaskTimeDisp_input{
   ds:Erp_Tablesets_TaskTableset[],
}

export interface ChangeTaskTimeDisp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeVendorContact_input{
   ds:Erp_Tablesets_TaskTableset[],
}

export interface ChangeVendorContact_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeVendorPP_input{
   ds:Erp_Tablesets_TaskTableset[],
}

export interface ChangeVendorPP_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeVendor_input{
   ds:Erp_Tablesets_TaskTableset[],
}

export interface ChangeVendor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param proposedVoidValue
      @param ds
   */  
export interface ChangeVoid_input{
      /**  true or false depending upon whether or not the user ticked void or unticked it  */  
   proposedVoidValue:boolean,
   ds:Erp_Tablesets_TaskTableset[],
}

export interface ChangeVoid_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
   nextTaskWarning:string,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeVoided_input{
   ds:Erp_Tablesets_TaskTableset[],
}

export interface ChangeVoided_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param iQuoteNum
      @param iCustNum
   */  
export interface CheckQuoteForCreditLimit_input{
      /**  Quote Number  */  
   iQuoteNum:number,
      /**  Customer Number  */  
   iCustNum:number,
}

export interface CheckQuoteForCreditLimit_output{
parameters : {
      /**  output parameters  */  
   cCreditLimitMessage:string,
   cCreditStatus:string,
}
}

   /** Required : 
      @param sysRowID
   */  
export interface CheckTaskCanBeVoided_input{
      /**  SysRowID  */  
   sysRowID:string,
}

export interface CheckTaskCanBeVoided_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   outMessage:string,
}
}

   /** Required : 
      @param relatedToFile
      @param key1
      @param key2
      @param key3
      @param taskSeqNum
   */  
export interface DeleteByID_input{
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
   taskSeqNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_TaskCntRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The master file to which the task is related. Opportunity/Quote, Customer, ECO Group etc...  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a task related to a quote (Customer) this field would contain the related Customer.CustNum value.  */  
   Key1:string,
      /**  2nd component of the foreign key to the related master record.  */  
   Key2:string,
      /**  3rd component of the foreign key to the related master record.  */  
   Key3:string,
      /**  Used to uniquely identify the record. Used so more than 1 Task can exist for a given record. The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  */  
   TaskSeqNum:number,
      /**  The SysRowId of the linked PerConLnk.  */  
   PerConLnkRowID:string,
      /**  Primary contact for each Context type. Only one allowed per context type. The primary contact for each context type is shown on the detail sheet.  */  
   Primary:boolean,
      /**  User entered comments.  */  
   Comment:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   Address1:string,
   Address2:string,
   Address3:string,
   BuyerID:string,
   BuyerName:string,
   City:string,
   ContextLink:string,
   CustID:string,
   CustName:string,
   EmpID:string,
   EmpName:string,
   Name:string,
   PurPoint:string,
   PurPointName:string,
   SalesRepCode:string,
   SalesRepName:string,
   ShipToName:string,
   ShipToNum:string,
   State:string,
   VendorID:string,
   VendorName:string,
   Zip:string,
   PerConID:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaskListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The master file to which the task is related.  Opportunity/Quote, Customer, ECO Group etc...  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a task related to a quote (Customer) this field would contain the related Customer.CustNum value.  */  
   Key1:string,
      /**  2nd component of the foreign key to the related master record.  */  
   Key2:string,
      /**  3rd component of the foreign key to the related master record.  */  
   Key3:string,
      /**  Link to the TaskMast table. Contains the TaskMast.TaskID value related to this task.  */  
   TaskID:string,
      /**  Used to uniquely identify the record.  Used so more than 1 Task can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  */  
   TaskSeqNum:number,
      /**  Default description from the TaskMaster. TaskMast.TaskDescription. The user can override the default description for this specific task.  */  
   TaskDescription:string,
      /**  The SalesRep that this task is assigned to. Will default from Role on TaskMaster  */  
   SalesRepCode:string,
      /**  Defaults is TODAY.  */  
   StartDate:string,
      /**  The Task should be completed by this date.  */  
   DueDate:string,
      /**  Status Code. From TaskStat table  */  
   StatusCode:string,
      /**  Percent of task that is complete.  Valid values are 0-100. User maintained.  */  
   PercentComplete:number,
      /**  Indicates that this task is complete.  When checked this will trigger creation of the next task and the global alert process.  */  
   Complete:boolean,
      /**  User entered completion date.  Default to TODAY when the complete flag is checked.  */  
   CompleteDate:string,
      /**   The LOQ must be in this stage to be selected or it will be put in this stage if the LOQ is already past this stage.
Valid Choices are
Lead, Oppo = Opportunity, Quot = Quote.
Not maintainable  */  
   CurrentStage:string,
      /**  This task must be completed before the LOQ can move to the next milestone.  Not maintainable as actual task  */  
   Mandatory:boolean,
      /**  This task must be completed before the LOQ can move to the next Milestone.  Only one Milestone task can be active on a quote at one time.  Not maintainable as actual task.  */  
   Milestone:boolean,
      /**  The date the task was created.  */  
   CreateDate:string,
      /**  The UserID that created the task  */  
   CreateDcdUserID:string,
      /**  The date the task was last changed.  */  
   ChangeDate:string,
      /**  The UserID that last changed the task  */  
   ChangeDcdUserID:string,
      /**  Completion of the task will send a Global Alert  */  
   SendAlertComplete:boolean,
      /**  Valid values are 1 - 99 1 = HIGH,  99 = LOW  */  
   PriorityCode:number,
      /**  Contains comments about the Task.  */  
   TaskComment:string,
      /**  Valid values are "win" "lose" "next" "next" is the default .  This will display as a radio set.  If "win" is selected then completing this task will require a reason code from CRM Win type. A sales order will be created if all mandatory tasks at this milestone are complete.  If  "lose" is selected all tasks and the quote will close  and a CRM Lose reason code is required. If "next" is selected then the "next task" drop down is enabled and the list of possible next tasks from the task set(TaskSNxt) will be displayed, reason code will be optional  */  
   Conclusion:string,
      /**  Select from list of Win or loss reason codes depending on the setting if the conclusion field  */  
   ReasonCode:string,
      /**  When this task is completed and the conclusion is "next" this field will hold the next Milestone task to be created.  */  
   NextTaskID:string,
      /**  Indentifies the nest milestone task sequence.  */  
   NextTaskSeq:number,
      /**  The Quote that this Task is related to.  */  
   TaskQuoteNum:number,
      /**  The Customer that this task is related to  */  
   TaskCustNum:number,
      /**  The Customer Ship To that this task is related to  */  
   TaskShipToNum:string,
      /**  The Customer contact that this Task is related to.  */  
   TaskConNum:number,
      /**  Link to the task set.  */  
   TaskSetID:string,
      /**  Link to the Task Set Detail  */  
   TaskSetSeq:number,
      /**  Setting this when the opportunity is a "win" will trigger the logic that creates a sales order.  */  
   CreateOrder:boolean,
      /**  Creation of the task will send a Global Alert  */  
   SendAlertCreate:boolean,
      /**  Defines the type of task this is.  From the TaskType table.  */  
   TypeCode:string,
      /**  The Vendor number associated with this task.  */  
   TaskVendorNum:number,
      /**  The Vendor purchase point related to this task.  */  
   TaskPurPoint:string,
      /**  The purchasing contact person associated with this task.  */  
   TaskPrcConNum:number,
      /**  Link to the Marketing Campaign related to this Task.  */  
   TaskMktgCampaignID:string,
      /**  A salesperson that the assigned salesperson needs to contact to complete this task  */  
   OtherSalesRepCode:string,
      /**  Defines if this task is included in the Customer category.  Categories are used for selecting tasks for assignment to TaskSets.  */  
   CustomerCategory:boolean,
      /**  Defines if this task is included in the Engineering category.  */  
   EngineeringCategory:boolean,
      /**  Defines if this task is included in the Vendor category.  */  
   VendorCategory:boolean,
      /**  Defines if this task is included in the Personal category.  */  
   PersonalCategory:boolean,
      /**  Defines if this task is included in the Management category.  */  
   ManagementCategory:boolean,
      /**  Defines if this task is included in the Other category.  */  
   OtherCategory:boolean,
      /**  Role of person who would default as the owner of this task when the task is created. From the RoleCD table.  */  
   RoleCode:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  EmployeeName  */  
   EmployeeName:string,
      /**   Text to indicate if this task is for "Time" or "Expense" (translated text). Used only by Labor Approval
TaskList search for search results column.  */  
   TimeOrExp:string,
      /**  ProjectID, used only by Task Time and Expense search as a search results grid.  */  
   ProjectID:string,
      /**  Holds the date of the transaction that created the task, used by TimeExpense approval search form.  */  
   TransDate:string,
      /**  JobNum, used only by task time and expense approbal search as search results grid  */  
   JobNum:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaskListTableset{
   TaskList:Erp_Tablesets_TaskListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_TaskRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The master file to which the task is related.  Opportunity/Quote, Customer, ECO Group etc...  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a task related to a quote (Customer) this field would contain the related Customer.CustNum value.  */  
   Key1:string,
      /**  2nd component of the foreign key to the related master record.  */  
   Key2:string,
      /**  3rd component of the foreign key to the related master record.  */  
   Key3:string,
      /**  Link to the TaskMast table. Contains the TaskMast.TaskID value related to this task.  */  
   TaskID:string,
      /**  Used to uniquely identify the record.  Used so more than 1 Task can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  */  
   TaskSeqNum:number,
      /**  Default description from the TaskMaster. TaskMast.TaskDescription. The user can override the default description for this specific task.  */  
   TaskDescription:string,
      /**  The SalesRep that this task is assigned to. Will default from Role on TaskMaster  */  
   SalesRepCode:string,
      /**  Defaults is TODAY.  */  
   StartDate:string,
      /**  The Task should be completed by this date.  */  
   DueDate:string,
      /**  Status Code. From TaskStat table  */  
   StatusCode:string,
      /**  Percent of task that is complete.  Valid values are 0-100. User maintained.  */  
   PercentComplete:number,
      /**  Indicates that this task is complete.  When checked this will trigger creation of the next task and the global alert process.  */  
   Complete:boolean,
      /**  User entered completion date.  Default to TODAY when the complete flag is checked.  */  
   CompleteDate:string,
      /**   The LOQ must be in this stage to be selected or it will be put in this stage if the LOQ is already past this stage.
Valid Choices are
Lead, Oppo = Opportunity, Quot = Quote.
Not maintainable  */  
   CurrentStage:string,
      /**  This task must be completed before the LOQ can move to the next milestone.  Not maintainable as actual task  */  
   Mandatory:boolean,
      /**  This task must be completed before the LOQ can move to the next Milestone.  Only one Milestone task can be active on a quote at one time.  Not maintainable as actual task.  */  
   Milestone:boolean,
      /**  The date the task was created.  */  
   CreateDate:string,
      /**  The UserID that created the task  */  
   CreateDcdUserID:string,
      /**  The date the task was last changed.  */  
   ChangeDate:string,
      /**  The UserID that last changed the task  */  
   ChangeDcdUserID:string,
      /**  Completion of the task will send a Global Alert  */  
   SendAlertComplete:boolean,
      /**  Valid values are 1 - 99 1 = HIGH,  99 = LOW  */  
   PriorityCode:number,
      /**  Contains comments about the Task.  */  
   TaskComment:string,
      /**  Valid values are "win" "lose" "next" "next" is the default .  This will display as a radio set.  If "win" is selected then completing this task will require a reason code from CRM Win type. A sales order will be created if all mandatory tasks at this milestone are complete.  If  "lose" is selected all tasks and the quote will close  and a CRM Lose reason code is required. If "next" is selected then the "next task" drop down is enabled and the list of possible next tasks from the task set(TaskSNxt) will be displayed, reason code will be optional  */  
   Conclusion:string,
      /**  Select from list of Win or loss reason codes depending on the setting if the conclusion field  */  
   ReasonCode:string,
      /**  When this task is completed and the conclusion is "next" this field will hold the next Milestone task to be created.  */  
   NextTaskID:string,
      /**  Indentifies the nest milestone task sequence.  */  
   NextTaskSeq:number,
      /**  The Quote that this Task is related to.  */  
   TaskQuoteNum:number,
      /**  The Customer that this task is related to  */  
   TaskCustNum:number,
      /**  The Customer Ship To that this task is related to  */  
   TaskShipToNum:string,
      /**  The Customer contact that this Task is related to.  */  
   TaskConNum:number,
      /**  Link to the task set.  */  
   TaskSetID:string,
      /**  Link to the Task Set Detail  */  
   TaskSetSeq:number,
      /**  Setting this when the opportunity is a "win" will trigger the logic that creates a sales order.  */  
   CreateOrder:boolean,
      /**  Creation of the task will send a Global Alert  */  
   SendAlertCreate:boolean,
      /**  Defines the type of task this is.  From the TaskType table.  */  
   TypeCode:string,
      /**  The Vendor number associated with this task.  */  
   TaskVendorNum:number,
      /**  The Vendor purchase point related to this task.  */  
   TaskPurPoint:string,
      /**  The purchasing contact person associated with this task.  */  
   TaskPrcConNum:number,
      /**  Link to the Marketing Campaign related to this Task.  */  
   TaskMktgCampaignID:string,
      /**  A salesperson that the assigned salesperson needs to contact to complete this task  */  
   OtherSalesRepCode:string,
      /**  Defines if this task is included in the Customer category.  Categories are used for selecting tasks for assignment to TaskSets.  */  
   CustomerCategory:boolean,
      /**  Defines if this task is included in the Engineering category.  */  
   EngineeringCategory:boolean,
      /**  Defines if this task is included in the Vendor category.  */  
   VendorCategory:boolean,
      /**  Defines if this task is included in the Personal category.  */  
   PersonalCategory:boolean,
      /**  Defines if this task is included in the Management category.  */  
   ManagementCategory:boolean,
      /**  Defines if this task is included in the Other category.  */  
   OtherCategory:boolean,
      /**  Role of person who would default as the owner of this task when the task is created. From the RoleCD table.  */  
   RoleCode:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Start Time for task.  Stored as seconds from midnight  */  
   StartTime:number,
      /**  End Time for task.  Stored as seconds from midnight  */  
   EndTime:number,
      /**  For Time and Expense transactions, multiple persons within a Role can be assigned a Task to complete, and if ANY of these persons complete the Task, the Milestone is to be marked complete.  */  
   AnyApprover:boolean,
      /**  The number of levels of supervisors above the employee where the approval responsibility lies.  Zero indicates the employee's supervisor does not approve.  One indicates the employee's supervisor (EmpBasic.SupervisorID) does approve. Two indicates that you need to find the employee's supervisor's supervisor, and so on.  */  
   ApprovalSupervisorLevel:number,
      /**  Indicates if the Task has been Approved via Time and Expense Approval.  */  
   Approved:boolean,
      /**   The action to take when the task is completed.  Applies to milestones only.  Used for time and expense tasks.  Values are:
SUB - Submit.  The time or expense record status is set to submitted when the milestone is complete.
APP - Approve.  The time or expense record is approved when the milestone is complete.  */  
   CompletionAction:string,
      /**  Applies to milestones.  Auto complete the milestone when the related tasks are completed.  */  
   AutoComplete:boolean,
      /**  Used for time and expense tasks.  Indicates the transaction the task is linked to will be marked as rejected when the task is completed.  */  
   RejectApproval:boolean,
      /**  RelatedToSysRowID  */  
   RelatedToSysRowID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  TaskShipToCustNum  */  
   TaskShipToCustNum:number,
      /**  TaskShipToCustConNum  */  
   TaskShipToCustConNum:number,
      /**  Voided  */  
   Voided:boolean,
      /**  TaskPerConID  */  
   TaskPerConID:number,
      /**  PrevTaskSetTask  */  
   PrevTaskSetTask:boolean,
   AllowUpdate:boolean,
      /**  Temporary display field for Change Time  */  
   ChangeTimeDisp:string,
      /**  Current Stage Description  */  
   CurrentStageDescription:string,
      /**  The customer ID.  */  
   CustID:string,
   CustomerContactFax:string,
   CustomerContactName:string,
   CustomerContactPhone:string,
      /**  The full customer's name.  */  
   CustomerName:string,
      /**  The name for the ship to location.  */  
   CustomerShipToName:string,
      /**  This is a boolean field to check if the Task is already completed or the user doesn't already complete the task.  */  
   DisableOnComplete:boolean,
   DisableTasks:boolean,
      /**  Temporary display field for End Time  */  
   EndTimeDisp:string,
   FilterIncludeComplete:boolean,
   FilterStartAtDate:string,
   FilterStartAtQuote:number,
   FilterTaskType:string,
   FilterType:string,
   IsLoseable:boolean,
   IsWinnable:boolean,
   NewMilestoneTaskSeqNum:number,
   NextStage:string,
   NextTaskList:string,
   OrigMilestoneTaskSeqNum:number,
   OtherSalesRepName:string,
   PromptCustCreditHoldWarning:boolean,
   PromptQuoteLinesWOQty:boolean,
   ReasonList:string,
      /**  Reject Approval Allowed - this option is available only for time and expense tasks  */  
   RejectAppAllowed:boolean,
      /**  Name of the Sales Representative.  */  
   SalesRepName:string,
      /**  Temporary display field for Start Time  */  
   StartTimeDisp:string,
      /**  Indicates if the password to complete the task is valid.  */  
   TaskCompletePasswordIsValid:boolean,
      /**  Indicates if a password is required to complete the task  */  
   TaskCompletePasswordRequired:boolean,
   TaskShipToCustConName:string,
   TaskShipToCustID:string,
   TaskShipToCustName:string,
      /**  This Column will store the value of the flag Customer.AllowShipTo3 for Task SoldTo Customers  */  
   TaskSoldToCustNumAllowsShipTo3:boolean,
      /**  Indicates whether a time or expense task is being approved or rejected.  */  
   TEApprovalAction:string,
      /**  Indicates if this is a time or expense task.  UI fields are enabled/disasbled based on this.  */  
   TETask:boolean,
   VendorContactEmail:string,
   VendorContactFax:string,
   VendorContactName:string,
   VendorContactPhone:string,
   VendorID:string,
   VendorName:string,
   WFCompleteAllowed:boolean,
   WorkflowComplete:boolean,
   CustomerContactEmail:string,
      /**  Used in Quote to verify if the task can be voided.  */  
   CanBeVoided:boolean,
      /**  List of conclusion options  */  
   ConclusionList:string,
   BitFlag:number,
   ChangeDcdUserIDName:string,
   ReasonCodeHDDescription:string,
   RoleCodeRoleDescription:string,
   ShipToNumInactive:boolean,
   StatusCodeStatusDescription:string,
   TaskConNumNameMiddleName:string,
   TaskConNumNameLastName:string,
   TaskConNumNameFirstName:string,
   TaskConNumNameName:string,
   TaskConNumNameCorpName:string,
   TaskConNumNameFaxNum:string,
   TaskConNumNamePhoneNum:string,
   TaskCustNumInactive:boolean,
   TaskIDTaskDescription:string,
   TaskSetIDWorkflowType:string,
   TaskSetIDTaskSetDescription:string,
   TaskSetSeqTaskDescription:string,
   TypeCodeTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaskTableset{
   Task:Erp_Tablesets_TaskRow[],
   TaskCnt:Erp_Tablesets_TaskCntRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_TaskTreeDetailRow{
   Company:string,
   Complete:boolean,
      /**  Description for the tree node  */  
   Description:string,
      /**  Unique internal sequence  */  
   InternalSeq:number,
      /**  Indicates a task record exists for this row  */  
   IsTask:boolean,
   Milestone:boolean,
   ParentTaskSeq:number,
   TaskKey1:string,
   TaskKey2:string,
   TaskKey3:string,
   TaskRelatedToFile:string,
   TaskSeqNum:number,
   TaskSetID:string,
   TaskSetSeq:number,
   Voided:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaskTreeHeaderRow{
   Company:string,
   TaskSetID:string,
      /**  Description to show in the tree node  */  
   Description:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaskTreeTableset{
   TaskTreeHeader:Erp_Tablesets_TaskTreeHeaderRow[],
   TaskTreeDetail:Erp_Tablesets_TaskTreeDetailRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtTaskTableset{
   Task:Erp_Tablesets_TaskRow[],
   TaskCnt:Erp_Tablesets_TaskCntRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
   */  
export interface ExistsUncompletedTasks_input{
   ds:Erp_Tablesets_TaskTableset[],
}

export interface ExistsUncompletedTasks_output{
   returnObj:boolean,
}

   /** Required : 
      @param ds
      @param filename
   */  
export interface ExportFile_input{
   ds:Erp_Tablesets_TaskTableset[],
   filename:string,
}

export interface ExportFile_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param relatedToFile
      @param key1
      @param key2
      @param key3
      @param taskSeqNum
   */  
export interface GetByID_input{
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
   taskSeqNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_TaskTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_TaskTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_TaskTableset[],
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
      @param icCustID
   */  
export interface GetCreditHoldMessageText_input{
      /**  The customer id  */  
   icCustID:string,
}

export interface GetCreditHoldMessageText_output{
parameters : {
      /**  output parameters  */  
   ocMessageText:string,
}
}

   /** Required : 
      @param company
      @param relatedToFile
      @param key1
   */  
export interface GetCurrentTaskSeqNum_input{
      /**  Company  */  
   company:string,
      /**  Task record is related to  */  
   relatedToFile:string,
      /**  ID or Number  */  
   key1:string,
}

export interface GetCurrentTaskSeqNum_output{
   returnObj:number,
}

export interface GetDefaultEndDate_output{
parameters : {
      /**  output parameters  */  
   endDate:string,
}
}

   /** Required : 
      @param ipSalesRepCode
      @param ipApprovalStatus
      @param ipTime
      @param ipExpense
      @param ipSortby
      @param ipStartDate
      @param ipEndDate
      @param ipEmployeeNum
      @param ipProject
      @param ipPhase
      @param ipJobNum
      @param pageSize
      @param absolutePage
   */  
export interface GetListApprovers_input{
      /**  IPsalesRepCode  */  
   ipSalesRepCode:string,
      /**  Stauts of Tasks  */  
   ipApprovalStatus:string,
      /**  Include Time Transactions  */  
   ipTime:boolean,
      /**  Include Expense transactions  */  
   ipExpense:boolean,
      /**  Sort the data - currently not used  */  
   ipSortby:string,
      /**  Starting date of the results set, blank will return all dates  */  
   ipStartDate:string,
      /**  Starting date of the results set, blank will return all dates  */  
   ipEndDate:string,
      /**  Search for time or expenses for a employee, blank for all  */  
   ipEmployeeNum:string,
      /**  Search for time or expenses for a project, blank for al  */  
   ipProject:string,
      /**  Search for time or expenses for a phase depending of the previously selected project, blank for al  */  
   ipPhase:string,
      /**  Search for time or expenses for a job, blank for al  */  
   ipJobNum:string,
      /**  The page size  */  
   pageSize:number,
      /**  the absolute page  */  
   absolutePage:number,
}

export interface GetListApprovers_output{
   returnObj:Erp_Tablesets_TaskListTableset[],
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
export interface GetList_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_TaskListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param relatedToFile
      @param key1
      @param key2
      @param key3
      @param taskSeqNum
   */  
export interface GetNewTaskCnt_input{
   ds:Erp_Tablesets_TaskTableset[],
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
   taskSeqNum:number,
}

export interface GetNewTaskCnt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param ds
      @param relatedToFile
      @param key1
      @param key2
      @param key3
   */  
export interface GetNewTask_input{
   ds:Erp_Tablesets_TaskTableset[],
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
}

export interface GetNewTask_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param userID
   */  
export interface GetPrimarySalesRepForUser_input{
   userID:string,
}

export interface GetPrimarySalesRepForUser_output{
   returnObj:string,
}

export interface GetQuoteLinesWOQtyMessageText_output{
parameters : {
      /**  output parameters  */  
   ocMessageText:string,
}
}

   /** Required : 
      @param hdCaseNum
      @param taskSetId
   */  
export interface GetRemainUncompletedTasks_input{
      /**  HDCase id  */  
   hdCaseNum:string,
      /**  TaskSetId  */  
   taskSetId:string,
}

export interface GetRemainUncompletedTasks_output{
parameters : {
      /**  output parameters  */  
   remainUncompletedTasks:boolean,
}
}

   /** Required : 
      @param whereClauseTask
      @param contactName
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsContactTracker_input{
      /**  Whereclause for Task table.  */  
   whereClauseTask:string,
      /**  The contact to return data for.  */  
   contactName:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsContactTracker_output{
   returnObj:Erp_Tablesets_TaskTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseTask
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustomerTracker_input{
      /**  Whereclause for Task table.  */  
   whereClauseTask:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsCustomerTracker_output{
   returnObj:Erp_Tablesets_TaskTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseTask
      @param whereClauseTaskCnt
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseTask:string,
   whereClauseTaskCnt:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_TaskTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param relatedToFile
      @param key1
      @param key2
      @param key3
      @param taskSeqNum
      @param ds
   */  
export interface GetTaskCnt_input{
      /**  Current RelatedToFile value  */  
   relatedToFile:string,
      /**  Current Key1 value  */  
   key1:string,
      /**  Current Key2 value  */  
   key2:string,
      /**  Current Key3 value  */  
   key3:string,
      /**  Current taskSeqNum value  */  
   taskSeqNum:number,
   ds:Erp_Tablesets_TaskTableset[],
}

export interface GetTaskCnt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param salesRepCode
      @param includeComplete
      @param dateType
      @param startDate
      @param endDate
      @param filterStatus
      @param filterType
      @param pageSize
      @param absolutePage
   */  
export interface GetTaskListByDateRange_input{
      /**  Current SalesRep, blank to use default or code of SalesRep selected by user  */  
   salesRepCode:string,
      /**  Include Complete Tasks or not  */  
   includeComplete:boolean,
      /**  Options are startDate or dueDate  */  
   dateType:string,
      /**  Starting date of the results set, null will return everything up to the ending date  */  
   startDate:string,
      /**  Ending date of the results set, null will become the last day of the next month  */  
   endDate:string,
      /**  A Specific Task Status to look for, blank for all  */  
   filterStatus:string,
      /**  A specific Task Type to look for, blank for all  */  
   filterType:string,
      /**  The page size  */  
   pageSize:number,
      /**  the absolute page  */  
   absolutePage:number,
}

export interface GetTaskListByDateRange_output{
   returnObj:Erp_Tablesets_TaskTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param salesRepCode
      @param includeComplete
      @param dateType
      @param startDate
      @param endDate
      @param filterStatus
      @param filterType
      @param pageSize
      @param absolutePage
   */  
export interface GetTaskList_input{
      /**  Current SalesRep, blank to use default or code of SalesRep selected by user  */  
   salesRepCode:string,
      /**  Include Complete Tasks or not  */  
   includeComplete:boolean,
      /**  Options are startDate or dueDate  */  
   dateType:string,
      /**  Starting date of the results set, blank will return everything up to the ending date  */  
   startDate:string,
      /**  Ending date of the results set, blank will become the last day of the next month  */  
   endDate:string,
      /**  A Specific Task Status to look for, blank for all  */  
   filterStatus:string,
      /**  A specific Task Type to look for, blank for all  */  
   filterType:string,
      /**  The page size  */  
   pageSize:number,
      /**  the absolute page  */  
   absolutePage:number,
}

export interface GetTaskList_output{
   returnObj:Erp_Tablesets_TaskTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param taskSetID
      @param relatedToFile
      @param key1
      @param key2
      @param key3
   */  
export interface GetTaskTreeDataSet_input{
      /**  Task Set ID  */  
   taskSetID:string,
      /**  Related to file  */  
   relatedToFile:string,
      /**  Key1 for related to file  */  
   key1:string,
      /**  Key2 for related to file  */  
   key2:string,
      /**  Key3 for related to file  */  
   key3:string,
}

export interface GetTaskTreeDataSet_output{
   returnObj:Erp_Tablesets_TaskTreeTableset[],
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
      @param iCreditStatus
      @param iCustNum
   */  
export interface PutCustomerOnCreditHold_input{
      /**  Credit Status  */  
   iCreditStatus:string,
      /**  Customer Number  */  
   iCustNum:number,
}

export interface PutCustomerOnCreditHold_output{
}

   /** Required : 
      @param cCustID
      @param cShipToNum
      @param cTableName
      @param lPublishMessage
   */  
export interface TerritoryAuthorized_input{
      /**  Customer ID  */  
   cCustID:string,
      /**  Ship to Number  */  
   cShipToNum:string,
      /**  Table Name  */  
   cTableName:string,
      /**  Publish Message not authorized to access  */  
   lPublishMessage:boolean,
}

export interface TerritoryAuthorized_output{
   returnObj:boolean,
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtTaskTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtTaskTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_TaskTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param ds
      @param proposedConclusion
   */  
export interface ValidateConclusion_input{
   ds:Erp_Tablesets_TaskTableset[],
      /**  The proposed value for the Conclusion  */  
   proposedConclusion:string,
}

export interface ValidateConclusion_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param ds
      @param vendorID
      @param lProposedPurPoint
   */  
export interface ValidatePurPoint_input{
   ds:Erp_Tablesets_TaskTableset[],
      /**  Vendor ID parameter  */  
   vendorID:string,
      /**  The proposed value for vendor purchase point  */  
   lProposedPurPoint:string,
}

export interface ValidatePurPoint_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param ds
      @param lProposedVendorID
   */  
export interface ValidateVendorID_input{
   ds:Erp_Tablesets_TaskTableset[],
      /**  The proposed value for vendor id  */  
   lProposedVendorID:string,
}

export interface ValidateVendorID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface VoidTask_input{
   ds:Erp_Tablesets_TaskTableset[],
}

export interface VoidTask_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface WorkFlowCompleteWithRemainingTask_input{
   ds:Erp_Tablesets_TaskTableset[],
}

export interface WorkFlowCompleteWithRemainingTask_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskTableset[],
}
}

