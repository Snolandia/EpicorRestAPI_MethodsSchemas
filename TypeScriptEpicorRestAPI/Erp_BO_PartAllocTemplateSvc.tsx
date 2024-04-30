import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PartAllocTemplateSvc
// Description: PartAllocationTemplate Entry
            A PartAllocTemplate record serves as an entry to define parameters used for the
            algorithm that searches for available inventory throughout the warehouse.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/$metadata", {
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
   Description: Get PartAllocTemplates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartAllocTemplates
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartAllocTemplateRow
   */  
export function get_PartAllocTemplates(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocTemplateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/PartAllocTemplates", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocTemplateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartAllocTemplates
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartAllocTemplateRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PartAllocTemplateRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartAllocTemplates(requestBody:Erp_Tablesets_PartAllocTemplateRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/PartAllocTemplates", {
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
   Summary: Calls GetByID to retrieve the PartAllocTemplate item
   Description: Calls GetByID to retrieve the PartAllocTemplate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartAllocTemplate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocTemplateID Desc: AllocTemplateID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PartAllocTemplateRow
   */  
export function get_PartAllocTemplates_Company_AllocTemplateID(Company:string, AllocTemplateID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartAllocTemplateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/PartAllocTemplates(" + Company + "," + AllocTemplateID + ")", {
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
         resolve(data as Erp_Tablesets_PartAllocTemplateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PartAllocTemplate for the service
   Description: Calls UpdateExt to update PartAllocTemplate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartAllocTemplate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocTemplateID Desc: AllocTemplateID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartAllocTemplateRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PartAllocTemplates_Company_AllocTemplateID(Company:string, AllocTemplateID:string, requestBody:Erp_Tablesets_PartAllocTemplateRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/PartAllocTemplates(" + Company + "," + AllocTemplateID + ")", {
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
   Summary: Call UpdateExt to delete PartAllocTemplate item
   Description: Call UpdateExt to delete PartAllocTemplate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartAllocTemplate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocTemplateID Desc: AllocTemplateID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PartAllocTemplates_Company_AllocTemplateID(Company:string, AllocTemplateID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/PartAllocTemplates(" + Company + "," + AllocTemplateID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartAllocTemplateListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocTemplateListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocTemplateListRow)
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
export function get_GetRows(whereClausePartAllocTemplate:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePartAllocTemplate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartAllocTemplate=" + whereClausePartAllocTemplate
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/GetRows" + params, {
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
export function get_GetByID(allocTemplateID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof allocTemplateID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "allocTemplateID=" + allocTemplateID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/GetList" + params, {
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
   Summary: Invoke method GetWhseTeamUserList
   Description: Returns the list of all employees from Database Table WhseGroupEmp
   OperationID: GetWhseTeamUserList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetWhseTeamUserList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWhseTeamUserList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetWhseTeamUserList(requestBody:GetWhseTeamUserList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetWhseTeamUserList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/GetWhseTeamUserList", {
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
         resolve(data as GetWhseTeamUserList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeEmpID
   Description: Call this method when User Assignment is changed.
   OperationID: OnChangeEmpID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeEmpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeEmpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeEmpID(requestBody:OnChangeEmpID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeEmpID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/OnChangeEmpID", {
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
         resolve(data as OnChangeEmpID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeWhseTeam
   Description: Call this method when the user changes team whse group.
   OperationID: OnChangeWhseTeam
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeWhseTeam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWhseTeam_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeWhseTeam(requestBody:OnChangeWhseTeam_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeWhseTeam_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/OnChangeWhseTeam", {
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
         resolve(data as OnChangeWhseTeam_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PartalloctemplateCheckAllocType
   Description: Checks PartAllocType code entered
   OperationID: PartalloctemplateCheckAllocType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PartalloctemplateCheckAllocType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartalloctemplateCheckAllocType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartalloctemplateCheckAllocType(requestBody:PartalloctemplateCheckAllocType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PartalloctemplateCheckAllocType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/PartalloctemplateCheckAllocType", {
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
         resolve(data as PartalloctemplateCheckAllocType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PartAllocTemplateCheckDemandType
   Description: Checks Part Alloc Demand Type code entered
   OperationID: PartAllocTemplateCheckDemandType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PartAllocTemplateCheckDemandType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartAllocTemplateCheckDemandType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartAllocTemplateCheckDemandType(requestBody:PartAllocTemplateCheckDemandType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PartAllocTemplateCheckDemandType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/PartAllocTemplateCheckDemandType", {
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
         resolve(data as PartAllocTemplateCheckDemandType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPartAllocTemplate
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartAllocTemplate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPartAllocTemplate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartAllocTemplate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartAllocTemplate(requestBody:GetNewPartAllocTemplate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPartAllocTemplate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/GetNewPartAllocTemplate", {
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
         resolve(data as GetNewPartAllocTemplate_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocTemplateListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartAllocTemplateListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocTemplateRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartAllocTemplateRow,
}

export interface Erp_Tablesets_PartAllocTemplateListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Part Allocation Template Identifier.  */  
   "AllocTemplateID":string,
      /**  Part Allocation Template Description  */  
   "AllocTemplateDesc":string,
      /**  Allocation Type.  Valid values:  Order or Wave.  */  
   "AllocType":string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   "WarehouseCode":string,
      /**  Part Allocation Demand Type.  Valid Values:  Order, Job, or Transfer.  */  
   "DemandType":string,
      /**  ID that uniquely Identifies a Zone within a warehouse.  */  
   "ZoneID":string,
      /**  Search Sort.  Valid values:  FIFO, LIFO, BINASC, BINDESC, QTYASC, or QTYDESC.  */  
   "SearchSort":string,
      /**  Bin Type.  Valid values:  Standard, Managed or Both.  */  
   "BinType":string,
      /**  The first option for the bin from which to select inventory within the warehouse.  */  
   "BinNumFirstOption":string,
      /**  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  */  
   "DistributionType":string,
      /**  Warehouse Group Identifier.  */  
   "WhseGroupCode":string,
      /**  Transaction Priority.  Valid values:  1,2,3,4,5,6,7,8,9,0.  One is the highest priority.  */  
   "TransPriority":number,
      /**  True if Cross-Docking is enabled.  */  
   "CrossDocking":boolean,
      /**  When Material Queue items are added, they should be automatically On Hold.  */  
   "OnHold":boolean,
      /**  True if Multiple Parts Per Bin is allowed.  */  
   "MultiplePartsPerBin":boolean,
      /**  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  */  
   "PackStation":string,
      /**  The user defined Production In bin number within the warehouse.  */  
   "BinNumProductionIn":string,
      /**  ID that uniquely Identifies a Forward Stage Group Bin Zone within a warehouse.  */  
   "ForwardStageGroup":string,
      /**  User defined warehouse destination.  */  
   "WarehouseCodeForwardStage":string,
      /**  Employee ID  */  
   "EmpID":string,
      /**  Employee ID that should be assigned to process record from the queue.  */  
   "AssignEmpID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "Replenishable":boolean,
      /**  Description.  */  
   "WarehouseDescription":string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   "WhseBinDescription":string,
      /**  Description.  */  
   "WhseCodeFwdStageDescDescription":string,
      /**  Warehouse Group Description.  */  
   "WhseGroupWhseGroupDesc":string,
      /**  Mandatory  */  
   "WhseZoneZoneDesc":string,
      /**  Mandatory  */  
   "WhseZoneFwdStageZoneDesc":string,
      /**  Description of the station  */  
   "WorkstationDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartAllocTemplateRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Part Allocation Template Identifier.  */  
   "AllocTemplateID":string,
      /**  Part Allocation Template Description  */  
   "AllocTemplateDesc":string,
      /**  Allocation Type.  Valid values:  Order or Wave.  */  
   "AllocType":string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   "WarehouseCode":string,
      /**  Part Allocation Demand Type.  Valid Values:  Order, Job, or Transfer.  */  
   "DemandType":string,
      /**  ID that uniquely Identifies a Zone within a warehouse.  */  
   "ZoneID":string,
      /**  Search Sort.  Valid values:  FIFO, LIFO, BINASC, BINDESC, QTYASC, or QTYDESC.  */  
   "SearchSort":string,
      /**  Bin Type.  Valid values:  Standard, Managed or Both.  */  
   "BinType":string,
      /**  The first option for the bin from which to select inventory within the warehouse.  */  
   "BinNumFirstOption":string,
      /**  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  */  
   "DistributionType":string,
      /**  Warehouse Group Identifier.  */  
   "WhseGroupCode":string,
      /**  Transaction Priority.  Valid values:  1,2,3,4,5,6,7,8,9,0.  One is the highest priority.  */  
   "TransPriority":number,
      /**  True if Cross-Docking is enabled.  */  
   "CrossDocking":boolean,
      /**  When Material Queue items are added, they should be automatically On Hold.  */  
   "OnHold":boolean,
      /**  True if Multiple Parts Per Bin is allowed.  */  
   "MultiplePartsPerBin":boolean,
      /**  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  */  
   "PackStation":string,
      /**  The user defined Production In bin number within the warehouse.  */  
   "BinNumProductionIn":string,
      /**  ID that uniquely Identifies a Forward Stage Group Bin Zone within a warehouse.  */  
   "ForwardStageGroup":string,
      /**  User defined warehouse destination.  */  
   "WarehouseCodeForwardStage":string,
      /**  Employee ID  */  
   "EmpID":string,
      /**  Employee ID that should be assigned to process record from the queue.  */  
   "AssignEmpID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Warehouse Destination for the allocated qty.  */  
   "WhseDestWarehouseCode":string,
      /**  The allocated demand is ready to be Released to Picking.  */  
   "ReleaseToPicking":boolean,
   "Replenishable":boolean,
   "BitFlag":number,
   "WarehouseDescription":string,
   "WhseBinDescription":string,
   "WhseCodeFwdStageDescDescription":string,
   "WhseGroupWhseGroupDesc":string,
   "WhseZoneZoneDesc":string,
   "WhseZoneFwdStageZoneDesc":string,
   "WorkstationDescription":string,
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
      @param allocTemplateID
   */  
export interface DeleteByID_input{
   allocTemplateID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PartAllocTemplateListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Part Allocation Template Identifier.  */  
   AllocTemplateID:string,
      /**  Part Allocation Template Description  */  
   AllocTemplateDesc:string,
      /**  Allocation Type.  Valid values:  Order or Wave.  */  
   AllocType:string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   WarehouseCode:string,
      /**  Part Allocation Demand Type.  Valid Values:  Order, Job, or Transfer.  */  
   DemandType:string,
      /**  ID that uniquely Identifies a Zone within a warehouse.  */  
   ZoneID:string,
      /**  Search Sort.  Valid values:  FIFO, LIFO, BINASC, BINDESC, QTYASC, or QTYDESC.  */  
   SearchSort:string,
      /**  Bin Type.  Valid values:  Standard, Managed or Both.  */  
   BinType:string,
      /**  The first option for the bin from which to select inventory within the warehouse.  */  
   BinNumFirstOption:string,
      /**  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  */  
   DistributionType:string,
      /**  Warehouse Group Identifier.  */  
   WhseGroupCode:string,
      /**  Transaction Priority.  Valid values:  1,2,3,4,5,6,7,8,9,0.  One is the highest priority.  */  
   TransPriority:number,
      /**  True if Cross-Docking is enabled.  */  
   CrossDocking:boolean,
      /**  When Material Queue items are added, they should be automatically On Hold.  */  
   OnHold:boolean,
      /**  True if Multiple Parts Per Bin is allowed.  */  
   MultiplePartsPerBin:boolean,
      /**  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  */  
   PackStation:string,
      /**  The user defined Production In bin number within the warehouse.  */  
   BinNumProductionIn:string,
      /**  ID that uniquely Identifies a Forward Stage Group Bin Zone within a warehouse.  */  
   ForwardStageGroup:string,
      /**  User defined warehouse destination.  */  
   WarehouseCodeForwardStage:string,
      /**  Employee ID  */  
   EmpID:string,
      /**  Employee ID that should be assigned to process record from the queue.  */  
   AssignEmpID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   Replenishable:boolean,
      /**  Description.  */  
   WarehouseDescription:string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   WhseBinDescription:string,
      /**  Description.  */  
   WhseCodeFwdStageDescDescription:string,
      /**  Warehouse Group Description.  */  
   WhseGroupWhseGroupDesc:string,
      /**  Mandatory  */  
   WhseZoneZoneDesc:string,
      /**  Mandatory  */  
   WhseZoneFwdStageZoneDesc:string,
      /**  Description of the station  */  
   WorkstationDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartAllocTemplateListTableset{
   PartAllocTemplateList:Erp_Tablesets_PartAllocTemplateListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartAllocTemplateRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Part Allocation Template Identifier.  */  
   AllocTemplateID:string,
      /**  Part Allocation Template Description  */  
   AllocTemplateDesc:string,
      /**  Allocation Type.  Valid values:  Order or Wave.  */  
   AllocType:string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   WarehouseCode:string,
      /**  Part Allocation Demand Type.  Valid Values:  Order, Job, or Transfer.  */  
   DemandType:string,
      /**  ID that uniquely Identifies a Zone within a warehouse.  */  
   ZoneID:string,
      /**  Search Sort.  Valid values:  FIFO, LIFO, BINASC, BINDESC, QTYASC, or QTYDESC.  */  
   SearchSort:string,
      /**  Bin Type.  Valid values:  Standard, Managed or Both.  */  
   BinType:string,
      /**  The first option for the bin from which to select inventory within the warehouse.  */  
   BinNumFirstOption:string,
      /**  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  */  
   DistributionType:string,
      /**  Warehouse Group Identifier.  */  
   WhseGroupCode:string,
      /**  Transaction Priority.  Valid values:  1,2,3,4,5,6,7,8,9,0.  One is the highest priority.  */  
   TransPriority:number,
      /**  True if Cross-Docking is enabled.  */  
   CrossDocking:boolean,
      /**  When Material Queue items are added, they should be automatically On Hold.  */  
   OnHold:boolean,
      /**  True if Multiple Parts Per Bin is allowed.  */  
   MultiplePartsPerBin:boolean,
      /**  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  */  
   PackStation:string,
      /**  The user defined Production In bin number within the warehouse.  */  
   BinNumProductionIn:string,
      /**  ID that uniquely Identifies a Forward Stage Group Bin Zone within a warehouse.  */  
   ForwardStageGroup:string,
      /**  User defined warehouse destination.  */  
   WarehouseCodeForwardStage:string,
      /**  Employee ID  */  
   EmpID:string,
      /**  Employee ID that should be assigned to process record from the queue.  */  
   AssignEmpID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Warehouse Destination for the allocated qty.  */  
   WhseDestWarehouseCode:string,
      /**  The allocated demand is ready to be Released to Picking.  */  
   ReleaseToPicking:boolean,
   Replenishable:boolean,
   BitFlag:number,
   WarehouseDescription:string,
   WhseBinDescription:string,
   WhseCodeFwdStageDescDescription:string,
   WhseGroupWhseGroupDesc:string,
   WhseZoneZoneDesc:string,
   WhseZoneFwdStageZoneDesc:string,
   WorkstationDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartAllocTemplateTableset{
   PartAllocTemplate:Erp_Tablesets_PartAllocTemplateRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPartAllocTemplateTableset{
   PartAllocTemplate:Erp_Tablesets_PartAllocTemplateRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_WhseTeamUserListRow{
   Company:string,
   WhseGroupCode:string,
   EmpID:string,
   EmpName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_WhseTeamUserListTableset{
   WhseTeamUserList:Erp_Tablesets_WhseTeamUserListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param allocTemplateID
   */  
export interface GetByID_input{
   allocTemplateID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PartAllocTemplateTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PartAllocTemplateTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PartAllocTemplateTableset[],
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
   returnObj:Erp_Tablesets_PartAllocTemplateListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPartAllocTemplate_input{
   ds:Erp_Tablesets_PartAllocTemplateTableset[],
}

export interface GetNewPartAllocTemplate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartAllocTemplateTableset,
}
}

   /** Required : 
      @param whereClausePartAllocTemplate
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePartAllocTemplate:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PartAllocTemplateTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param groupCode
   */  
export interface GetWhseTeamUserList_input{
      /**  Warehouse Group Code.  */  
   groupCode:string,
}

export interface GetWhseTeamUserList_output{
   returnObj:Erp_Tablesets_WhseTeamUserListTableset[],
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
      @param empID
      @param ds
   */  
export interface OnChangeEmpID_input{
      /**  Proposed value for User Assignment.  */  
   empID:string,
   ds:Erp_Tablesets_PartAllocTemplateTableset[],
}

export interface OnChangeEmpID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartAllocTemplateTableset,
}
}

   /** Required : 
      @param teamWhse
      @param ds
   */  
export interface OnChangeWhseTeam_input{
      /**  Proposed value for team whse.  */  
   teamWhse:string,
   ds:Erp_Tablesets_PartAllocTemplateTableset[],
}

export interface OnChangeWhseTeam_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartAllocTemplateTableset,
}
}

   /** Required : 
      @param newPartAllocDemandType
      @param ds
   */  
export interface PartAllocTemplateCheckDemandType_input{
      /**  PartAllocDemandType code entered  */  
   newPartAllocDemandType:string,
   ds:Erp_Tablesets_PartAllocTemplateTableset[],
}

export interface PartAllocTemplateCheckDemandType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartAllocTemplateTableset,
}
}

   /** Required : 
      @param newPartAllocType
      @param ds
   */  
export interface PartalloctemplateCheckAllocType_input{
      /**  PartAllocType code entered  */  
   newPartAllocType:string,
   ds:Erp_Tablesets_PartAllocTemplateTableset[],
}

export interface PartalloctemplateCheckAllocType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartAllocTemplateTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPartAllocTemplateTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPartAllocTemplateTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PartAllocTemplateTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartAllocTemplateTableset,
}
}

