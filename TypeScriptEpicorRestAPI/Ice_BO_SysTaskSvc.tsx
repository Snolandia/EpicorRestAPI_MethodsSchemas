import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.BO.SysTaskSvc
// Description: The SysTask service.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/$metadata", {
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
   Description: Get SysTasks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SysTasks
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysTaskRow
   */  
export function get_SysTasks(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysTaskRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTasks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysTaskRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SysTasks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SysTaskRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SysTaskRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SysTasks(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTasks", {
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
   Summary: Calls GetByID to retrieve the SysTask item
   Description: Calls GetByID to retrieve the SysTask item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysTask
      @param SysTaskNum Desc: SysTaskNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysTaskRow
   */  
export function get_SysTasks_SysTaskNum(SysTaskNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_SysTaskRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTasks(" + SysTaskNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_SysTaskRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SysTask for the service
   Description: Calls UpdateExt to update SysTask. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SysTask
      @param SysTaskNum Desc: SysTaskNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SysTaskRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SysTasks_SysTaskNum(SysTaskNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTasks(" + SysTaskNum + ")", {
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
   Summary: Call UpdateExt to delete SysTask item
   Description: Call UpdateExt to delete SysTask item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SysTask
      @param SysTaskNum Desc: SysTaskNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SysTasks_SysTaskNum(SysTaskNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTasks(" + SysTaskNum + ")", {
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
   Description: Get SysTaskParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SysTaskParams1
      @param SysTaskNum Desc: SysTaskNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysTaskParamRow
   */  
export function get_SysTasks_SysTaskNum_SysTaskParams(SysTaskNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysTaskParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTasks(" + SysTaskNum + ")/SysTaskParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysTaskParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the SysTaskParam item
   Description: Calls GetByID to retrieve the SysTaskParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysTaskParam1
      @param SysTaskNum Desc: SysTaskNum   Required: True   Allow empty value : True
      @param ParamName Desc: ParamName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysTaskParamRow
   */  
export function get_SysTasks_SysTaskNum_SysTaskParams_SysTaskNum_ParamName(SysTaskNum:string, ParamName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_SysTaskParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTasks(" + SysTaskNum + ")/SysTaskParams(" + SysTaskNum + "," + ParamName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_SysTaskParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get SysTaskParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SysTaskParams
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysTaskParamRow
   */  
export function get_SysTaskParams(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysTaskParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTaskParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysTaskParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SysTaskParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SysTaskParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SysTaskParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SysTaskParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTaskParams", {
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
   Summary: Calls GetByID to retrieve the SysTaskParam item
   Description: Calls GetByID to retrieve the SysTaskParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysTaskParam
      @param SysTaskNum Desc: SysTaskNum   Required: True   Allow empty value : True
      @param ParamName Desc: ParamName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysTaskParamRow
   */  
export function get_SysTaskParams_SysTaskNum_ParamName(SysTaskNum:string, ParamName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_SysTaskParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTaskParams(" + SysTaskNum + "," + ParamName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_SysTaskParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SysTaskParam for the service
   Description: Calls UpdateExt to update SysTaskParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SysTaskParam
      @param SysTaskNum Desc: SysTaskNum   Required: True   Allow empty value : True
      @param ParamName Desc: ParamName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SysTaskParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SysTaskParams_SysTaskNum_ParamName(SysTaskNum:string, ParamName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTaskParams(" + SysTaskNum + "," + ParamName + ")", {
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
   Summary: Call UpdateExt to delete SysTaskParam item
   Description: Call UpdateExt to delete SysTaskParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SysTaskParam
      @param SysTaskNum Desc: SysTaskNum   Required: True   Allow empty value : True
      @param ParamName Desc: ParamName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SysTaskParams_SysTaskNum_ParamName(SysTaskNum:string, ParamName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTaskParams(" + SysTaskNum + "," + ParamName + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysTaskListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysTaskListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysTaskListRow)
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
export function get_GetRows(whereClauseSysTask:string, whereClauseSysTaskParam:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseSysTask!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSysTask=" + whereClauseSysTask
   }
   if(typeof whereClauseSysTaskParam!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSysTaskParam=" + whereClauseSysTaskParam
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/GetRows" + params, {
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
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(sysTaskNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/GetList" + params, {
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
   Summary: Invoke method SysTaskExists
   Description: Determines if a SysTask record exists with the given AgentID and agentSchedNum with the History flag set to the indicated value.
   OperationID: SysTaskExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SysTaskExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SysTaskExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SysTaskExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTaskExists", {
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
   Summary: Invoke method DeleteSysTaskKillRecords
   Description: Clears SysTaskKill records.
   OperationID: DeleteSysTaskKillRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteSysTaskKillRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteSysTaskKillRecords(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/DeleteSysTaskKillRecords", {
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
   Summary: Invoke method CleanUpActiveTasks
   Description: This functionality is no longer available.
   OperationID: CleanUpActiveTasks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CleanUpActiveTasks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CleanUpActiveTasks(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/CleanUpActiveTasks", {
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
   Summary: Invoke method KillActiveTasks
   Description: Kills the active tasks by writing out SysTaskKill records for them.
   OperationID: KillActiveTasks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/KillActiveTasks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_KillActiveTasks(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/KillActiveTasks", {
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
   Summary: Invoke method CheckForDups
   Description: Checks for a duplicate running task using the supplied parameters.
   OperationID: CheckForDups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckForDups_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckForDups_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckForDups(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/CheckForDups", {
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
   Summary: Invoke method SetSysTaskStatusForPendingTask
   Description: Sets the system task status for task that is currently pending.
   OperationID: SetSysTaskStatusForPendingTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetSysTaskStatusForPendingTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetSysTaskStatusForPendingTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetSysTaskStatusForPendingTask(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SetSysTaskStatusForPendingTask", {
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
   Summary: Invoke method WriteToTaskLog
   Description: Writes a message to the SysTaskLog file.
   OperationID: WriteToTaskLog
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WriteToTaskLog_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WriteToTaskLog_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WriteToTaskLog(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/WriteToTaskLog", {
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
   Summary: Invoke method GetNewSysTask
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSysTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSysTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSysTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSysTask(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/GetNewSysTask", {
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
   Summary: Invoke method GetNewSysTaskParam
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSysTaskParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSysTaskParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSysTaskParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSysTaskParam(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/GetNewSysTaskParam", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysTaskListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_SysTaskListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysTaskParamRow{
   "odatametadata":string,
   "value":Ice_Tablesets_SysTaskParamRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysTaskRow{
   "odatametadata":string,
   "value":Ice_Tablesets_SysTaskRow[],
}

export interface Ice_Tablesets_SysTaskListRow{
      /**  System Task Number  */  
   "SysTaskNum":number,
      /**  Task Description  */  
   "TaskDescription":string,
      /**   Used to control what program is used to initiate the running of the program that this task is suppose to run.
Example: TextRpt will run Task/TextRpt.p
                 DSRpt will run Task/DataSetRpt.p  */  
   "TaskType":string,
      /**  Date-time field that the task Started On in UTC time zone  */  
   "StartedOn":string,
      /**  Date-time field that the task Ended On in UTC time zone  */  
   "EndedOn":string,
      /**  User who submitrted the task  */  
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
      /**  Run Procedure  */  
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
      /**  Unique ID for Process  */  
   "ProcessID":string,
      /**  IsSystemTask  */  
   "IsSystemTask":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ProgressPercent  */  
   "ProgressPercent":number,
      /**  EdgeCorrelationID  */  
   "EdgeCorrelationID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_SysTaskParamRow{
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

export interface Ice_Tablesets_SysTaskRow{
      /**  System Task Number  */  
   "SysTaskNum":number,
      /**  Task Description  */  
   "TaskDescription":string,
      /**   Used to control what program is used to initiate the running of the program that this task is suppose to run.
Example: TextRpt will run Task/TextRpt.p
                 DSRpt will run Task/DataSetRpt.p  */  
   "TaskType":string,
      /**  Date-time field that the task Started On in UTC time zone  */  
   "StartedOn":string,
      /**  Date-time field that the task Ended On in UTC time zone  */  
   "EndedOn":string,
      /**  User who submitrted the task  */  
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
      /**  Run Procedure  */  
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
      /**  Unique ID for Process  */  
   "ProcessID":string,
      /**  IsSystemTask  */  
   "IsSystemTask":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ProgressPercent  */  
   "ProgressPercent":number,
      /**  EdgeCorrelationID  */  
   "EdgeCorrelationID":string,
   "ErrorMsg":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param SysTaskNum
      @param RunProcedure
      @param ProcessID
   */  
export interface CheckForDups_input{
   SysTaskNum:number,
   RunProcedure:string,
   ProcessID:string,
}

export interface CheckForDups_output{
      /**  `true` if another task is found for the same RunProcedure/ProcessID, otherwise `false`.  */  
   returnObj:boolean,
}

export interface CleanUpActiveTasks_output{
}

   /** Required : 
      @param sysTaskNum
   */  
export interface DeleteByID_input{
   sysTaskNum:number,
}

export interface DeleteByID_output{
}

export interface DeleteSysTaskKillRecords_output{
}

   /** Required : 
      @param sysTaskNum
   */  
export interface GetByID_input{
   sysTaskNum:number,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_SysTaskTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_SysTaskTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_SysTaskTableset[],
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
   returnObj:Ice_Tablesets_SysTaskListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param sysTaskNum
   */  
export interface GetNewSysTaskParam_input{
   ds:Ice_Tablesets_SysTaskTableset[],
   sysTaskNum:number,
}

export interface GetNewSysTaskParam_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_SysTaskTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewSysTask_input{
   ds:Ice_Tablesets_SysTaskTableset[],
}

export interface GetNewSysTask_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_SysTaskTableset[],
}
}

   /** Required : 
      @param whereClauseSysTask
      @param whereClauseSysTaskParam
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseSysTask:string,
   whereClauseSysTaskParam:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_SysTaskTableset[],
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

export interface Ice_Tablesets_SysTaskListRow{
      /**  System Task Number  */  
   SysTaskNum:number,
      /**  Task Description  */  
   TaskDescription:string,
      /**   Used to control what program is used to initiate the running of the program that this task is suppose to run.
Example: TextRpt will run Task/TextRpt.p
                 DSRpt will run Task/DataSetRpt.p  */  
   TaskType:string,
      /**  Date-time field that the task Started On in UTC time zone  */  
   StartedOn:string,
      /**  Date-time field that the task Ended On in UTC time zone  */  
   EndedOn:string,
      /**  User who submitrted the task  */  
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
      /**  Run Procedure  */  
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
      /**  Unique ID for Process  */  
   ProcessID:string,
      /**  IsSystemTask  */  
   IsSystemTask:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ProgressPercent  */  
   ProgressPercent:number,
      /**  EdgeCorrelationID  */  
   EdgeCorrelationID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SysTaskListTableset{
   SysTaskList:Ice_Tablesets_SysTaskListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_SysTaskParamRow{
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

export interface Ice_Tablesets_SysTaskRow{
      /**  System Task Number  */  
   SysTaskNum:number,
      /**  Task Description  */  
   TaskDescription:string,
      /**   Used to control what program is used to initiate the running of the program that this task is suppose to run.
Example: TextRpt will run Task/TextRpt.p
                 DSRpt will run Task/DataSetRpt.p  */  
   TaskType:string,
      /**  Date-time field that the task Started On in UTC time zone  */  
   StartedOn:string,
      /**  Date-time field that the task Ended On in UTC time zone  */  
   EndedOn:string,
      /**  User who submitrted the task  */  
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
      /**  Run Procedure  */  
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
      /**  Unique ID for Process  */  
   ProcessID:string,
      /**  IsSystemTask  */  
   IsSystemTask:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ProgressPercent  */  
   ProgressPercent:number,
      /**  EdgeCorrelationID  */  
   EdgeCorrelationID:string,
   ErrorMsg:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SysTaskTableset{
   SysTask:Ice_Tablesets_SysTaskRow[],
   SysTaskParam:Ice_Tablesets_SysTaskParamRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UpdExtSysTaskTableset{
   SysTask:Ice_Tablesets_SysTaskRow[],
   SysTaskParam:Ice_Tablesets_SysTaskParamRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface KillActiveTasks_output{
}

   /** Required : 
      @param sysTaskNum
      @param runProcedure
      @param taskStatus
      @param messageToLog
   */  
export interface SetSysTaskStatusForPendingTask_input{
      /**  The system task number.  */  
   sysTaskNum:number,
      /**  The run procedure for the task.  */  
   runProcedure:string,
      /**  The task status.  */  
   taskStatus:string,
      /**  The message to log.  */  
   messageToLog:string,
}

export interface SetSysTaskStatusForPendingTask_output{
}

   /** Required : 
      @param history
      @param agentID
      @param agentSchedNum
   */  
export interface SysTaskExists_input{
   history:boolean,
   agentID:string,
   agentSchedNum:number,
}

export interface SysTaskExists_output{
      /**  `true` if the Ice.Services.BO.SysTaskSvc.SysTask exits.  */  
   returnObj:boolean,
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtSysTaskTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtSysTaskTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_SysTaskTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_SysTaskTableset[],
}
}

   /** Required : 
      @param NewMessage
      @param TaskNum
   */  
export interface WriteToTaskLog_input{
   NewMessage:string,
   TaskNum:number,
}

export interface WriteToTaskLog_output{
}

