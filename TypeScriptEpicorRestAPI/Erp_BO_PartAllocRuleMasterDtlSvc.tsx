import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PartAllocRuleMasterDtlSvc
// Description: PartAllocRuleMasterDtlSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/$metadata", {
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
   Description: Get PartAllocRuleMasterDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartAllocRuleMasterDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartAllocRuleMasterDtlRow
   */  
export function get_PartAllocRuleMasterDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocRuleMasterDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/PartAllocRuleMasterDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocRuleMasterDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartAllocRuleMasterDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartAllocRuleMasterDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartAllocRuleMasterDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartAllocRuleMasterDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/PartAllocRuleMasterDtls", {
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
   Summary: Calls GetByID to retrieve the PartAllocRuleMasterDtl item
   Description: Calls GetByID to retrieve the PartAllocRuleMasterDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartAllocRuleMasterDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MasterRuleID Desc: MasterRuleID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartAllocRuleMasterDtlRow
   */  
export function get_PartAllocRuleMasterDtls_Company_MasterRuleID(Company:string, MasterRuleID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartAllocRuleMasterDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/PartAllocRuleMasterDtls(" + Company + "," + MasterRuleID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PartAllocRuleMasterDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PartAllocRuleMasterDtl for the service
   Description: Calls UpdateExt to update PartAllocRuleMasterDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartAllocRuleMasterDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MasterRuleID Desc: MasterRuleID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartAllocRuleMasterDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PartAllocRuleMasterDtls_Company_MasterRuleID(Company:string, MasterRuleID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/PartAllocRuleMasterDtls(" + Company + "," + MasterRuleID + ")", {
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
   Summary: Call UpdateExt to delete PartAllocRuleMasterDtl item
   Description: Call UpdateExt to delete PartAllocRuleMasterDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartAllocRuleMasterDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MasterRuleID Desc: MasterRuleID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PartAllocRuleMasterDtls_Company_MasterRuleID(Company:string, MasterRuleID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/PartAllocRuleMasterDtls(" + Company + "," + MasterRuleID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartAllocRuleMasterDtlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocRuleMasterDtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocRuleMasterDtlListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClausePartAllocRuleMasterDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePartAllocRuleMasterDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartAllocRuleMasterDtl=" + whereClausePartAllocRuleMasterDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/GetRows" + params, {
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
export function get_GetByID(masterRuleID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof masterRuleID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "masterRuleID=" + masterRuleID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/GetList" + params, {
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
   Summary: Invoke method CopyPartAllocRuleMasterDtl
   Description: Copies the Master Rule to a new record
   OperationID: CopyPartAllocRuleMasterDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyPartAllocRuleMasterDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyPartAllocRuleMasterDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyPartAllocRuleMasterDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/CopyPartAllocRuleMasterDtl", {
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
   Summary: Invoke method OnChangeAction
   Description: Invoked when Action is changed.
   OperationID: OnChangeAction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAction(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/OnChangeAction", {
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
   Summary: Invoke method OnChangeAllocTemplate
   Description: Invoked when AllocTemplateID is changed.
   OperationID: OnChangeAllocTemplate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAllocTemplate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAllocTemplate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAllocTemplate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/OnChangeAllocTemplate", {
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
   Summary: Invoke method OnChangeQueryID
   Description: Invoked when QueryID is changed.  Query must have PartAllocQueueInfo as its first table.
   OperationID: OnChangeQueryID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeQueryID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQueryID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeQueryID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/OnChangeQueryID", {
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
   Summary: Invoke method GetNewPartAllocRuleMasterDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartAllocRuleMasterDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartAllocRuleMasterDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartAllocRuleMasterDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartAllocRuleMasterDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/GetNewPartAllocRuleMasterDtl", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocRuleMasterDtlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartAllocRuleMasterDtlListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocRuleMasterDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartAllocRuleMasterDtlRow[],
}

export interface Erp_Tablesets_PartAllocRuleMasterDtlListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique ID of Master Rule.  */  
   "MasterRuleID":string,
      /**  Description of the rule.  */  
   "Description":string,
      /**  The action that is executed for this rule.  */  
   "Action":string,
      /**  Indicates if the Rule is Active.  */  
   "Active":boolean,
      /**  Indicates the PartAllocTemplate to use when allocating.  */  
   "AllocTemplateID":string,
      /**  QueryID of a BAQ used to join other tables to the PartAllocQueueInfo.  */  
   "QueryID":string,
      /**  The formula defined for this rule.  */  
   "Formula":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartAllocRuleMasterDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique ID of Master Rule.  */  
   "MasterRuleID":string,
      /**  Description of the rule.  */  
   "Description":string,
      /**  The action that is executed for this rule.  */  
   "Action":string,
      /**  Indicates if the Rule is Active.  */  
   "Active":boolean,
      /**  Indicates the PartAllocTemplate to use when allocating.  */  
   "AllocTemplateID":string,
      /**  QueryID of a BAQ used to join other tables to the PartAllocQueueInfo.  */  
   "QueryID":string,
      /**  The formula defined for this rule.  */  
   "Formula":string,
      /**  Used to determine whether or not we (re)calculate fulfillment values following the return of the results of a search.  */  
   "RuleCalcFulfillOnSearch":boolean,
      /**  When TRUE the fulfillment calculations and actions will consider the Demand Warehouse only.  When false, all warehouses will be considered in fulfillment calculations, and the user will be able to choose on Reserve actions whether to consider only the Primary Warehouse or all warehouses.  */  
   "RuleUseDemandWhseOnly":boolean,
      /**  Following the execution of an action (Reserve, Allocate, Release for Picking, Unreserve, Unallocate), when true we will only refresh the rows that were actioned on, when false we will refresh all records.  */  
   "RuleLimitedRefresh":boolean,
      /**  DevCharacter01  */  
   "DevCharacter01":string,
      /**  DevDecimal01  */  
   "DevDecimal01":number,
      /**  DevBoolean01  */  
   "DevBoolean01":boolean,
      /**  DevDate01  */  
   "DevDate01":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  The type of allocation based on the Action.  Valid Values:  Order, Job, Transfer, or blank.  */  
   "AllocDemandType":string,
      /**  Indicates if the AllocationTemplate field should be enabled  */  
   "EnableAllocTemplateID":boolean,
      /**  Indicates if the user is able to enter a formula  */  
   "EnableFormula":boolean,
      /**  Indicates if the QueryID field should be enabled  */  
   "EnableQueryID":boolean,
      /**  Flag indicating if there are any synchronized rules linked to this master rule  */  
   "RuleInUse":boolean,
      /**  Indicates if an Active SysTask exists for this rule class.  */  
   "ActiveSysTaskExists":boolean,
   "BitFlag":number,
   "PartAllocTemplateAllocTemplateDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param masterRuleID
      @param ds
   */  
export interface CopyPartAllocRuleMasterDtl_input{
   masterRuleID:string,
   ds:Erp_Tablesets_PartAllocRuleMasterDtlTableset[],
}

export interface CopyPartAllocRuleMasterDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartAllocRuleMasterDtlTableset[],
}
}

   /** Required : 
      @param masterRuleID
   */  
export interface DeleteByID_input{
   masterRuleID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PartAllocRuleMasterDtlListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique ID of Master Rule.  */  
   MasterRuleID:string,
      /**  Description of the rule.  */  
   Description:string,
      /**  The action that is executed for this rule.  */  
   Action:string,
      /**  Indicates if the Rule is Active.  */  
   Active:boolean,
      /**  Indicates the PartAllocTemplate to use when allocating.  */  
   AllocTemplateID:string,
      /**  QueryID of a BAQ used to join other tables to the PartAllocQueueInfo.  */  
   QueryID:string,
      /**  The formula defined for this rule.  */  
   Formula:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartAllocRuleMasterDtlListTableset{
   PartAllocRuleMasterDtlList:Erp_Tablesets_PartAllocRuleMasterDtlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartAllocRuleMasterDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique ID of Master Rule.  */  
   MasterRuleID:string,
      /**  Description of the rule.  */  
   Description:string,
      /**  The action that is executed for this rule.  */  
   Action:string,
      /**  Indicates if the Rule is Active.  */  
   Active:boolean,
      /**  Indicates the PartAllocTemplate to use when allocating.  */  
   AllocTemplateID:string,
      /**  QueryID of a BAQ used to join other tables to the PartAllocQueueInfo.  */  
   QueryID:string,
      /**  The formula defined for this rule.  */  
   Formula:string,
      /**  Used to determine whether or not we (re)calculate fulfillment values following the return of the results of a search.  */  
   RuleCalcFulfillOnSearch:boolean,
      /**  When TRUE the fulfillment calculations and actions will consider the Demand Warehouse only.  When false, all warehouses will be considered in fulfillment calculations, and the user will be able to choose on Reserve actions whether to consider only the Primary Warehouse or all warehouses.  */  
   RuleUseDemandWhseOnly:boolean,
      /**  Following the execution of an action (Reserve, Allocate, Release for Picking, Unreserve, Unallocate), when true we will only refresh the rows that were actioned on, when false we will refresh all records.  */  
   RuleLimitedRefresh:boolean,
      /**  DevCharacter01  */  
   DevCharacter01:string,
      /**  DevDecimal01  */  
   DevDecimal01:number,
      /**  DevBoolean01  */  
   DevBoolean01:boolean,
      /**  DevDate01  */  
   DevDate01:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  The type of allocation based on the Action.  Valid Values:  Order, Job, Transfer, or blank.  */  
   AllocDemandType:string,
      /**  Indicates if the AllocationTemplate field should be enabled  */  
   EnableAllocTemplateID:boolean,
      /**  Indicates if the user is able to enter a formula  */  
   EnableFormula:boolean,
      /**  Indicates if the QueryID field should be enabled  */  
   EnableQueryID:boolean,
      /**  Flag indicating if there are any synchronized rules linked to this master rule  */  
   RuleInUse:boolean,
      /**  Indicates if an Active SysTask exists for this rule class.  */  
   ActiveSysTaskExists:boolean,
   BitFlag:number,
   PartAllocTemplateAllocTemplateDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartAllocRuleMasterDtlTableset{
   PartAllocRuleMasterDtl:Erp_Tablesets_PartAllocRuleMasterDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPartAllocRuleMasterDtlTableset{
   PartAllocRuleMasterDtl:Erp_Tablesets_PartAllocRuleMasterDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param masterRuleID
   */  
export interface GetByID_input{
   masterRuleID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PartAllocRuleMasterDtlTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PartAllocRuleMasterDtlTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PartAllocRuleMasterDtlTableset[],
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
   returnObj:Erp_Tablesets_PartAllocRuleMasterDtlListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPartAllocRuleMasterDtl_input{
   ds:Erp_Tablesets_PartAllocRuleMasterDtlTableset[],
}

export interface GetNewPartAllocRuleMasterDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartAllocRuleMasterDtlTableset[],
}
}

   /** Required : 
      @param whereClausePartAllocRuleMasterDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePartAllocRuleMasterDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PartAllocRuleMasterDtlTableset[],
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
      @param newAction
      @param checkForWarnings
      @param ds
   */  
export interface OnChangeAction_input{
   newAction:string,
   checkForWarnings:boolean,
   ds:Erp_Tablesets_PartAllocRuleMasterDtlTableset[],
}

export interface OnChangeAction_output{
parameters : {
      /**  output parameters  */  
   warningMsg:string,
   ds:Erp_Tablesets_PartAllocRuleMasterDtlTableset[],
}
}

   /** Required : 
      @param newAllocTemplateID
      @param ds
   */  
export interface OnChangeAllocTemplate_input{
   newAllocTemplateID:string,
   ds:Erp_Tablesets_PartAllocRuleMasterDtlTableset[],
}

export interface OnChangeAllocTemplate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartAllocRuleMasterDtlTableset[],
}
}

   /** Required : 
      @param newQueryID
      @param checkForWarnings
      @param ds
   */  
export interface OnChangeQueryID_input{
   newQueryID:string,
   checkForWarnings:boolean,
   ds:Erp_Tablesets_PartAllocRuleMasterDtlTableset[],
}

export interface OnChangeQueryID_output{
parameters : {
      /**  output parameters  */  
   warningMsg:string,
   ds:Erp_Tablesets_PartAllocRuleMasterDtlTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPartAllocRuleMasterDtlTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPartAllocRuleMasterDtlTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PartAllocRuleMasterDtlTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartAllocRuleMasterDtlTableset[],
}
}

