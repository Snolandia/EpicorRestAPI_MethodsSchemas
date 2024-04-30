import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.GLAccountSvc
// Description: The GL Account service.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/$metadata", {
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
   Description: Get GLAccounts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLAccounts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLAccountRow
   */  
export function get_GLAccounts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAccountRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GLAccounts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAccountRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLAccounts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLAccountRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GLAccountRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLAccounts(requestBody:Erp_Tablesets_GLAccountRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GLAccounts", {
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
   Summary: Calls GetByID to retrieve the GLAccount item
   Description: Calls GetByID to retrieve the GLAccount item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLAccount
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param GLAccount1 Desc: GLAccount1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLAccountRow
   */  
export function get_GLAccounts_Company_COACode_GLAccount1(Company:string, COACode:string, GLAccount1:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLAccountRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GLAccounts(" + Company + "," + COACode + "," + GLAccount1 + ")", {
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
         resolve(data as Erp_Tablesets_GLAccountRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLAccount for the service
   Description: Calls UpdateExt to update GLAccount. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLAccount
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param GLAccount1 Desc: GLAccount1   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLAccountRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLAccounts_Company_COACode_GLAccount1(Company:string, COACode:string, GLAccount1:string, requestBody:Erp_Tablesets_GLAccountRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GLAccounts(" + Company + "," + COACode + "," + GLAccount1 + ")", {
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
   Summary: Call UpdateExt to delete GLAccount item
   Description: Call UpdateExt to delete GLAccount item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLAccount
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param GLAccount1 Desc: GLAccount1   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLAccounts_Company_COACode_GLAccount1(Company:string, COACode:string, GLAccount1:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GLAccounts(" + Company + "," + COACode + "," + GLAccount1 + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLAccountListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAccountListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAccountListRow)
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
export function get_GetRows(whereClauseGLAccount:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseGLAccount!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLAccount=" + whereClauseGLAccount
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GetRows" + params, {
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
export function get_GetByID(coACode:string, glAccount:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof coACode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "coACode=" + coACode
   }
   if(typeof glAccount!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "glAccount=" + glAccount
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GetList" + params, {
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
   Summary: Invoke method GetGLAccountGlobalFields
   Description: Get GLAccount global fields
   OperationID: GetGLAccountGlobalFields
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetGLAccountGlobalFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLAccountGlobalFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGLAccountGlobalFields(requestBody:GetGLAccountGlobalFields_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetGLAccountGlobalFields_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GetGLAccountGlobalFields", {
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
         resolve(data as GetGLAccountGlobalFields_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckActive
   Description: Verify the active flag against segment values
   OperationID: CheckActive
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckActive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckActive_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckActive(requestBody:CheckActive_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckActive_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/CheckActive", {
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
         resolve(data as CheckActive_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GLAccountActiveChanging
   Description: Called when the Active flag on the GL Account is changing.
Performs validations when marking an account is active.
Checks for GL Control Code references when marking an account as inactive.
   OperationID: GLAccountActiveChanging
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GLAccountActiveChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GLAccountActiveChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLAccountActiveChanging(requestBody:GLAccountActiveChanging_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GLAccountActiveChanging_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GLAccountActiveChanging", {
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
         resolve(data as GLAccountActiveChanging_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetGLControlReferences
   Description: Returns a dataset of GL Control Codes that reference the account
   OperationID: GetGLControlReferences
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetGLControlReferences_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLControlReferences_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGLControlReferences(requestBody:GetGLControlReferences_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetGLControlReferences_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GetGLControlReferences", {
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
         resolve(data as GetGLControlReferences_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckEffFrom
   Description: Verify the effective from is not earlier than any segment effective from
   OperationID: CheckEffFrom
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckEffFrom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckEffFrom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckEffFrom(requestBody:CheckEffFrom_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckEffFrom_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/CheckEffFrom", {
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
         resolve(data as CheckEffFrom_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckEffTo
   Description: Verify the effective to is not later than any segment effective to
   OperationID: CheckEffTo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckEffTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckEffTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckEffTo(requestBody:CheckEffTo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckEffTo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/CheckEffTo", {
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
         resolve(data as CheckEffTo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultsOnAdd
   Description: Set Default creating a new account
   OperationID: DefaultsOnAdd
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultsOnAdd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultsOnAdd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultsOnAdd(requestBody:DefaultsOnAdd_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultsOnAdd_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/DefaultsOnAdd", {
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
         resolve(data as DefaultsOnAdd_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GLAccountSearchFilter
   Description: Search GLAccount with account filter applied
   OperationID: GLAccountSearchFilter
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GLAccountSearchFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GLAccountSearchFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLAccountSearchFilter(requestBody:GLAccountSearchFilter_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GLAccountSearchFilter_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GLAccountSearchFilter", {
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
         resolve(data as GLAccountSearchFilter_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GLAccountSearchList
   Description: Search GLAccount in DataSetList mode.
   OperationID: GLAccountSearchList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GLAccountSearchList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GLAccountSearchList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLAccountSearchList(requestBody:GLAccountSearchList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GLAccountSearchList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GLAccountSearchList", {
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
         resolve(data as GLAccountSearchList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GLAccountSearchRows
   Description: Search GLAccount in DataSetRows mode.
   OperationID: GLAccountSearchRows
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GLAccountSearchRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GLAccountSearchRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLAccountSearchRows(requestBody:GLAccountSearchRows_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GLAccountSearchRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GLAccountSearchRows", {
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
         resolve(data as GLAccountSearchRows_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateAccount
   Description: Validate GL Account
   OperationID: ValidateAccount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateAccount(requestBody:ValidateAccount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateAccount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/ValidateAccount", {
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
         resolve(data as ValidateAccount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateCOACode
   Description: Returns a description and Global COA flags of the entered COA code
   OperationID: ValidateCOACode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateCOACode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCOACode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateCOACode(requestBody:ValidateCOACode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateCOACode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/ValidateCOACode", {
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
         resolve(data as ValidateCOACode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GlAccountExists
   Description: Return true if mentioned GL Account exists for the COA
   OperationID: GlAccountExists
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GlAccountExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GlAccountExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GlAccountExists(requestBody:GlAccountExists_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GlAccountExists_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GlAccountExists", {
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
         resolve(data as GlAccountExists_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetControlledCombination
   Description: This method returns only controlled combination of segments from full GLAccount
   OperationID: GetControlledCombination
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetControlledCombination_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetControlledCombination_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetControlledCombination(requestBody:GetControlledCombination_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetControlledCombination_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GetControlledCombination", {
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
         resolve(data as GetControlledCombination_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckExcludeInInclude
   Description: COA Segments validation step before mass Preview/Generation/Delete of gl accounts.
   OperationID: CheckExcludeInInclude
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckExcludeInInclude_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckExcludeInInclude_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckExcludeInInclude(requestBody:CheckExcludeInInclude_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckExcludeInInclude_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/CheckExcludeInInclude", {
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
         resolve(data as CheckExcludeInInclude_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetGLAcctDispAndDesc
   Description: This method should be called from UI GL Account control for Display and Description generation
   OperationID: GetGLAcctDispAndDesc
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetGLAcctDispAndDesc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLAcctDispAndDesc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGLAcctDispAndDesc(requestBody:GetGLAcctDispAndDesc_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetGLAcctDispAndDesc_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GetGLAcctDispAndDesc", {
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
         resolve(data as GetGLAcctDispAndDesc_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateGLAccount
   Description: This method should be called from UI GL Account control for account validation
   OperationID: ValidateGLAccount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateGLAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateGLAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateGLAccount(requestBody:ValidateGLAccount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateGLAccount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/ValidateGLAccount", {
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
         resolve(data as ValidateGLAccount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PutListInCorrectFormat
   Description: Prepare a list of Categories/Segment Codes for further Generate/Delete Accounts procedures.
   OperationID: PutListInCorrectFormat
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PutListInCorrectFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PutListInCorrectFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PutListInCorrectFormat(requestBody:PutListInCorrectFormat_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PutListInCorrectFormat_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/PutListInCorrectFormat", {
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
         resolve(data as PutListInCorrectFormat_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckBeforeDelete
   Description: Return confirmation message if needed for MultiCompany/Global accounts before deletion.
   OperationID: CheckBeforeDelete
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckBeforeDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBeforeDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckBeforeDelete(requestBody:CheckBeforeDelete_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckBeforeDelete_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/CheckBeforeDelete", {
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
         resolve(data as CheckBeforeDelete_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGLAccount
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLAccount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGLAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLAccount(requestBody:GetNewGLAccount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGLAccount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GetNewGLAccount", {
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
         resolve(data as GetNewGLAccount_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAccountListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLAccountListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAccountRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLAccountRow,
}

export interface Erp_Tablesets_GLAccountListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   "GLAccount":string,
      /**  Text that describes the account.  */  
   "AccountDesc":string,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   "SegValue1":string,
      /**  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   "SegValue2":string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   "SegValue3":string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   "SegValue4":string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   "SegValue5":string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   "SegValue6":string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   "SegValue7":string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   "SegValue8":string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   "SegValue9":string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   "SegValue10":string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   "SegValue11":string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   "SegValue12":string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   "SegValue13":string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   "SegValue14":string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   "SegValue15":string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   "SegValue16":string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   "SegValue17":string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   "SegValue18":string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   "SegValue19":string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   "SegValue20":string,
      /**  Indicates if the entered description shall be preserved when the tool to automatically generate GL Accounts is used.  */  
   "PreservDesc":boolean,
      /**  Indicates if the 'Active' flag and the 'Effective Date Range' shall be preserved when the tool to automatically generate GL accounts is used.  Default value = no.  */  
   "PreserveActivation":boolean,
      /**  Indicates if this account is active.  The user cannot post to an inactive account.  Yes indicates the account is active.  No indicates the account is not active.  */  
   "Active":boolean,
      /**  Date the GL Account begins to be effective.  It must be less than or equal to the Effective to date if one has been entered.  */  
   "EffFrom":string,
      /**  Date the GL Account is no longer effective.  This date must be greater than or equal to the Effective From date if one has been entered.  */  
   "EffTo":string,
      /**  A flag to indicate this GL Account may recieve multi-company journals.  */  
   "MultiCompany":boolean,
      /**  Full account including separator value up to 200 characters.  Unique identifier for the GL Account.  */  
   "ParentGLAccount":string,
      /**  Parent SegmentValue 1.  See COASegment segment number 11 for a description of this field.  */  
   "PntSegValue1":string,
      /**  Parent SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   "PntSegValue2":string,
      /**  Parent SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   "PntSegValue3":string,
      /**  Parent SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   "PntSegValue4":string,
      /**  Parent SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   "PntSegValue5":string,
      /**  Parent SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   "PntSegValue6":string,
      /**  Parent SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   "PntSegValue7":string,
      /**  Parent SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   "PntSegValue8":string,
      /**  Parent SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   "PntSegValue9":string,
      /**  Parent SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   "PntSegValue10":string,
      /**  Parent SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   "PntSegValue11":string,
      /**  Parent SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   "PntSegValue12":string,
      /**  Parent SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   "PntSegValue13":string,
      /**  Parent SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   "PntSegValue14":string,
      /**  Parent SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   "PntSegValue15":string,
      /**  Parent SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   "PntSegValue16":string,
      /**  Parent SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   "PntSegValue17":string,
      /**  Parent SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   "PntSegValue18":string,
      /**  Parent SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   "PntSegValue19":string,
      /**  Parent SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   "PntSegValue20":string,
      /**  Company ID of the external company this COA was imported from.  */  
   "ExtCompID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   "GLAcctDispGLAcctDisp":string,
      /**  Optional field that may be used for reporting purpose when the GL Account exceeds the space available on a printed document.  It is a shortened version of the 200 character GL Account that displays on reports.  The value of this field is the concatenation of the first three controlled display order segments.  For example, if a chart has 5 controlled segments that are displayed in the following order: seg5->seg3->seg4->seg2->seg1, this field contains the concatention of seg5->seg3->seg4 up to th  */  
   "GLAcctDispGLShortAcct":string,
      /**  Text that describes the account.  */  
   "GLAcctDispAccountDesc":string,
   "StatisticalDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLAccountRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Chart of Account ID  */  
   "COACode":string,
   "GLAccount1":string,
      /**  Text that describes the account.  */  
   "AccountDesc":string,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   "SegValue1":string,
      /**  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   "SegValue2":string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   "SegValue3":string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   "SegValue4":string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   "SegValue5":string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   "SegValue6":string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   "SegValue7":string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   "SegValue8":string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   "SegValue9":string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   "SegValue10":string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   "SegValue11":string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   "SegValue12":string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   "SegValue13":string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   "SegValue14":string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   "SegValue15":string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   "SegValue16":string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   "SegValue17":string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   "SegValue18":string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   "SegValue19":string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   "SegValue20":string,
      /**  Indicates if the entered description shall be preserved when the tool to automatically generate GL Accounts is used.  */  
   "PreservDesc":boolean,
      /**  Indicates if the 'Active' flag and the 'Effective Date Range' shall be preserved when the tool to automatically generate GL accounts is used.  Default value = no.  */  
   "PreserveActivation":boolean,
      /**  Indicates if this account is active.  The user cannot post to an inactive account.  Yes indicates the account is active.  No indicates the account is not active.  */  
   "Active":boolean,
      /**  Date the GL Account begins to be effective.  It must be less than or equal to the Effective to date if one has been entered.  */  
   "EffFrom":string,
      /**  Date the GL Account is no longer effective.  This date must be greater than or equal to the Effective From date if one has been entered.  */  
   "EffTo":string,
      /**  A flag to indicate this GL Account may recieve multi-company journals.  */  
   "MultiCompany":boolean,
      /**  Full account including separator value up to 200 characters.  Unique identifier for the GL Account.  */  
   "ParentGLAccount":string,
      /**  Parent SegmentValue 1.  See COASegment segment number 11 for a description of this field.  */  
   "PntSegValue1":string,
      /**  Parent SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   "PntSegValue2":string,
      /**  Parent SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   "PntSegValue3":string,
      /**  Parent SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   "PntSegValue4":string,
      /**  Parent SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   "PntSegValue5":string,
      /**  Parent SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   "PntSegValue6":string,
      /**  Parent SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   "PntSegValue7":string,
      /**  Parent SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   "PntSegValue8":string,
      /**  Parent SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   "PntSegValue9":string,
      /**  Parent SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   "PntSegValue10":string,
      /**  Parent SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   "PntSegValue11":string,
      /**  Parent SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   "PntSegValue12":string,
      /**  Parent SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   "PntSegValue13":string,
      /**  Parent SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   "PntSegValue14":string,
      /**  Parent SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   "PntSegValue15":string,
      /**  Parent SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   "PntSegValue16":string,
      /**  Parent SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   "PntSegValue17":string,
      /**  Parent SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   "PntSegValue18":string,
      /**  Parent SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   "PntSegValue19":string,
      /**  Parent SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   "PntSegValue20":string,
      /**  Company ID of the external company this COA was imported from.  */  
   "ExtCompID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MXConcept  */  
   "MXConcept":string,
   "StatisticalDesc":string,
      /**  GLBGLAccountFlag  */  
   "GLBGLAccountFlag":boolean,
      /**  Global COA Flag  */  
   "GlobalCOA":boolean,
      /**  Global Flag  */  
   "GlobalFlag":boolean,
      /**  Indicates the user has chosen to delete the account even if there is a record in GLBGLAccount.  */  
   "DeleteOverride":boolean,
   "BitFlag":number,
   "GLAcctDispGLAcctDisp":string,
   "GLAcctDispAccountDesc":string,
   "GLAcctDispGLShortAcct":string,
      /**  RowMod  */  
   "RowMod":string,
   "UD_SysRevID":string,
   "BudgetSegCode_c":string,
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
      @param ipActive
      @param ds
   */  
export interface CheckActive_input{
      /**  Proposed value of active  */  
   ipActive:boolean,
   ds:Erp_Tablesets_GLAccountTableset[],
}

export interface CheckActive_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLAccountTableset,
}
}

   /** Required : 
      @param coa
      @param glAccount
   */  
export interface CheckBeforeDelete_input{
      /**  Chart of Accounts of GL Account to check.  */  
   coa:string,
      /**  GL Account to check before trying to delete.  */  
   glAccount:string,
}

export interface CheckBeforeDelete_output{
   returnObj:string,
}

   /** Required : 
      @param ipEffFrom
      @param ds
   */  
export interface CheckEffFrom_input{
      /**  Effective From Date to validate  */  
   ipEffFrom:string,
   ds:Erp_Tablesets_GLAccountTableset[],
}

export interface CheckEffFrom_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLAccountTableset,
}
}

   /** Required : 
      @param ipEffTo
      @param ds
   */  
export interface CheckEffTo_input{
      /**  Effective To Date to validate  */  
   ipEffTo:string,
   ds:Erp_Tablesets_GLAccountTableset[],
}

export interface CheckEffTo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLAccountTableset,
}
}

   /** Required : 
      @param sIncFrom
      @param sIncTo
      @param sExcFrom
      @param sExcTo
   */  
export interface CheckExcludeInInclude_input{
   sIncFrom:string,
   sIncTo:string,
   sExcFrom:string,
   sExcTo:string,
}

export interface CheckExcludeInInclude_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   sErrMsg:string,
}
}

   /** Required : 
      @param ipGLAccount
      @param ds
   */  
export interface DefaultsOnAdd_input{
      /**  GL Account being added  */  
   ipGLAccount:string,
   ds:Erp_Tablesets_GLAccountTableset[],
}

export interface DefaultsOnAdd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLAccountTableset,
}
}

   /** Required : 
      @param coACode
      @param glAccount
   */  
export interface DeleteByID_input{
   coACode:string,
   glAccount:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_GLAccountListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   GLAccount:string,
      /**  Text that describes the account.  */  
   AccountDesc:string,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   SegValue1:string,
      /**  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   SegValue2:string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   SegValue3:string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   SegValue4:string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   SegValue5:string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   SegValue6:string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   SegValue7:string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   SegValue8:string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   SegValue9:string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   SegValue10:string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   SegValue11:string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   SegValue12:string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   SegValue13:string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   SegValue14:string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   SegValue15:string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   SegValue16:string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   SegValue17:string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   SegValue18:string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   SegValue19:string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   SegValue20:string,
      /**  Indicates if the entered description shall be preserved when the tool to automatically generate GL Accounts is used.  */  
   PreservDesc:boolean,
      /**  Indicates if the 'Active' flag and the 'Effective Date Range' shall be preserved when the tool to automatically generate GL accounts is used.  Default value = no.  */  
   PreserveActivation:boolean,
      /**  Indicates if this account is active.  The user cannot post to an inactive account.  Yes indicates the account is active.  No indicates the account is not active.  */  
   Active:boolean,
      /**  Date the GL Account begins to be effective.  It must be less than or equal to the Effective to date if one has been entered.  */  
   EffFrom:string,
      /**  Date the GL Account is no longer effective.  This date must be greater than or equal to the Effective From date if one has been entered.  */  
   EffTo:string,
      /**  A flag to indicate this GL Account may recieve multi-company journals.  */  
   MultiCompany:boolean,
      /**  Full account including separator value up to 200 characters.  Unique identifier for the GL Account.  */  
   ParentGLAccount:string,
      /**  Parent SegmentValue 1.  See COASegment segment number 11 for a description of this field.  */  
   PntSegValue1:string,
      /**  Parent SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   PntSegValue2:string,
      /**  Parent SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   PntSegValue3:string,
      /**  Parent SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   PntSegValue4:string,
      /**  Parent SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   PntSegValue5:string,
      /**  Parent SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   PntSegValue6:string,
      /**  Parent SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   PntSegValue7:string,
      /**  Parent SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   PntSegValue8:string,
      /**  Parent SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   PntSegValue9:string,
      /**  Parent SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   PntSegValue10:string,
      /**  Parent SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   PntSegValue11:string,
      /**  Parent SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   PntSegValue12:string,
      /**  Parent SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   PntSegValue13:string,
      /**  Parent SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   PntSegValue14:string,
      /**  Parent SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   PntSegValue15:string,
      /**  Parent SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   PntSegValue16:string,
      /**  Parent SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   PntSegValue17:string,
      /**  Parent SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   PntSegValue18:string,
      /**  Parent SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   PntSegValue19:string,
      /**  Parent SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   PntSegValue20:string,
      /**  Company ID of the external company this COA was imported from.  */  
   ExtCompID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   GLAcctDispGLAcctDisp:string,
      /**  Optional field that may be used for reporting purpose when the GL Account exceeds the space available on a printed document.  It is a shortened version of the 200 character GL Account that displays on reports.  The value of this field is the concatenation of the first three controlled display order segments.  For example, if a chart has 5 controlled segments that are displayed in the following order: seg5->seg3->seg4->seg2->seg1, this field contains the concatention of seg5->seg3->seg4 up to th  */  
   GLAcctDispGLShortAcct:string,
      /**  Text that describes the account.  */  
   GLAcctDispAccountDesc:string,
   StatisticalDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLAccountListTableset{
   GLAccountList:Erp_Tablesets_GLAccountListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GLAccountRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   GLAccount:string,
      /**  Text that describes the account.  */  
   AccountDesc:string,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   SegValue1:string,
      /**  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   SegValue2:string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   SegValue3:string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   SegValue4:string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   SegValue5:string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   SegValue6:string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   SegValue7:string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   SegValue8:string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   SegValue9:string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   SegValue10:string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   SegValue11:string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   SegValue12:string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   SegValue13:string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   SegValue14:string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   SegValue15:string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   SegValue16:string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   SegValue17:string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   SegValue18:string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   SegValue19:string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   SegValue20:string,
      /**  Indicates if the entered description shall be preserved when the tool to automatically generate GL Accounts is used.  */  
   PreservDesc:boolean,
      /**  Indicates if the 'Active' flag and the 'Effective Date Range' shall be preserved when the tool to automatically generate GL accounts is used.  Default value = no.  */  
   PreserveActivation:boolean,
      /**  Indicates if this account is active.  The user cannot post to an inactive account.  Yes indicates the account is active.  No indicates the account is not active.  */  
   Active:boolean,
      /**  Date the GL Account begins to be effective.  It must be less than or equal to the Effective to date if one has been entered.  */  
   EffFrom:string,
      /**  Date the GL Account is no longer effective.  This date must be greater than or equal to the Effective From date if one has been entered.  */  
   EffTo:string,
      /**  A flag to indicate this GL Account may recieve multi-company journals.  */  
   MultiCompany:boolean,
      /**  Full account including separator value up to 200 characters.  Unique identifier for the GL Account.  */  
   ParentGLAccount:string,
      /**  Parent SegmentValue 1.  See COASegment segment number 11 for a description of this field.  */  
   PntSegValue1:string,
      /**  Parent SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   PntSegValue2:string,
      /**  Parent SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   PntSegValue3:string,
      /**  Parent SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   PntSegValue4:string,
      /**  Parent SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   PntSegValue5:string,
      /**  Parent SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   PntSegValue6:string,
      /**  Parent SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   PntSegValue7:string,
      /**  Parent SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   PntSegValue8:string,
      /**  Parent SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   PntSegValue9:string,
      /**  Parent SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   PntSegValue10:string,
      /**  Parent SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   PntSegValue11:string,
      /**  Parent SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   PntSegValue12:string,
      /**  Parent SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   PntSegValue13:string,
      /**  Parent SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   PntSegValue14:string,
      /**  Parent SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   PntSegValue15:string,
      /**  Parent SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   PntSegValue16:string,
      /**  Parent SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   PntSegValue17:string,
      /**  Parent SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   PntSegValue18:string,
      /**  Parent SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   PntSegValue19:string,
      /**  Parent SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   PntSegValue20:string,
      /**  Company ID of the external company this COA was imported from.  */  
   ExtCompID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MXConcept  */  
   MXConcept:string,
   StatisticalDesc:string,
      /**  GLBGLAccountFlag  */  
   GLBGLAccountFlag:boolean,
      /**  Global COA Flag  */  
   GlobalCOA:boolean,
      /**  Global Flag  */  
   GlobalFlag:boolean,
      /**  Indicates the user has chosen to delete the account even if there is a record in GLBGLAccount.  */  
   DeleteOverride:boolean,
   BitFlag:number,
   GLAcctDispGLAcctDisp:string,
   GLAcctDispAccountDesc:string,
   GLAcctDispGLShortAcct:string,
      /**  RowMod  */  
   RowMod:string,
   UD_SysRevID:string,
   BudgetSegCode_c:string,
}

export interface Erp_Tablesets_GLAccountTableset{
   GLAccount:Erp_Tablesets_GLAccountRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GLCntrlAcctReferencesTableset{
   GLCntrlAcct:Erp_Tablesets_GLCntrlAcctRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GLCntrlAcctRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Identifier of the GL Control Type.  */  
   GLControlType:string,
      /**  GL Control Identifier.  */  
   GLControlCode:string,
      /**  String identifier of the account context.  */  
   GLAcctContext:string,
      /**  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  */  
   BookID:string,
      /**  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  */  
   COACode:string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   GLAccount:string,
      /**  This field in combination with GLControlType references the GLCTAcctCntxt record that this record was created from.  */  
   GLCTAcctNum:number,
      /**  Segement Value 1 of the account for this context.  */  
   SegValue1:string,
      /**  Segement Value 2 of the account for this context.  */  
   SegValue2:string,
      /**  Segement Value 3 of the account for this context.  */  
   SegValue3:string,
      /**  Segement Value 4 of the account for this context.  */  
   SegValue4:string,
      /**  Segement Value 5 of the account for this context.  */  
   SegValue5:string,
      /**  Segement Value 6 of the account for this context.  */  
   SegValue6:string,
      /**  Segement Value 7 of the account for this context.  */  
   SegValue7:string,
      /**  Segement Value 8 of the account for this context.  */  
   SegValue8:string,
      /**  Segement Value 9 of the account for this context.  */  
   SegValue9:string,
      /**  Segement Value 10 of the account for this context.  */  
   SegValue10:string,
      /**  Segement Value 11 of the account for this context.  */  
   SegValue11:string,
      /**  Segement Value 12 of the account for this context.  */  
   SegValue12:string,
      /**  Segement Value 13 of the account for this context.  */  
   SegValue13:string,
      /**  Segement Value 14 of the account for this context.  */  
   SegValue14:string,
      /**  Segement Value 15 of the account for this context.  */  
   SegValue15:string,
      /**  Segement Value 16 of the account for this context.  */  
   SegValue16:string,
      /**  Segement Value 17 of the account for this context.  */  
   SegValue17:string,
      /**  Segement Value 18 of the account for this context.  */  
   SegValue18:string,
      /**  Segement Value 19 of the account for this context.  */  
   SegValue19:string,
      /**  Segement Value 20 of the account for this context.  */  
   SegValue20:string,
      /**  Marks this GLCntrlAcct as global, available to be sent out to other companies.  */  
   GlobalGLCntrlAcct:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if an account is required for this record.  Data source is the GLCTAcctCntxt table.  */  
   IsRequired:boolean,
      /**  Indicates if the Master Chart is being used for this record.  The data source for this field is GLCTAcctCntxt.  */  
   UseMasterChart:boolean,
      /**  The name of the Master Chart of Accounts.  */  
   COAName:string,
   BitFlag:number,
   GLAccountAccountDesc:string,
   GLBookDescription:string,
   GLBookCurrencyCode:string,
   GLCntrlDescription:string,
   GLCntrlTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtGLAccountTableset{
   GLAccount:Erp_Tablesets_GLAccountRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param proposedActive
      @param ds
   */  
export interface GLAccountActiveChanging_input{
      /**  Proposed Active value  */  
   proposedActive:boolean,
   ds:Erp_Tablesets_GLAccountTableset[],
}

export interface GLAccountActiveChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLAccountTableset,
   glControlCodeReferences:boolean,
}
}

   /** Required : 
      @param whereClause
      @param descContains
      @param effFrom
      @param effTo
      @param coaCode
      @param plantList
      @param pageSize
      @param absolutePage
      @param accountMask
   */  
export interface GLAccountSearchFilter_input{
   whereClause:string,
   descContains:string,
   effFrom:string,
   effTo:string,
      /**  COACode  */  
   coaCode:string,
      /**  COACode  */  
   plantList:string,
   pageSize:number,
   absolutePage:number,
   accountMask:string,
}

export interface GLAccountSearchFilter_output{
   returnObj:Erp_Tablesets_GLAccountListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param WhereClause
      @param PageSize
      @param AbsolutePage
   */  
export interface GLAccountSearchList_input{
   WhereClause:string,
   PageSize:number,
   AbsolutePage:number,
}

export interface GLAccountSearchList_output{
   returnObj:Erp_Tablesets_GLAccountListTableset[],
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
export interface GLAccountSearchRows_input{
   whereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GLAccountSearchRows_output{
   returnObj:Erp_Tablesets_GLAccountTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param coACode
      @param glAccount
   */  
export interface GetByID_input{
   coACode:string,
   glAccount:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_GLAccountTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_GLAccountTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_GLAccountTableset[],
}

   /** Required : 
      @param company
      @param COACode
      @param GLAccount
   */  
export interface GetControlledCombination_input{
      /**  Company name  */  
   company:string,
      /**  COACode  */  
   COACode:string,
      /**  Full GLAccount with dynamic values  */  
   GLAccount:string,
}

export interface GetControlledCombination_output{
   returnObj:string,
}

   /** Required : 
      @param GLAccount
      @param CoaCode
      @param GlobalLock
   */  
export interface GetGLAccountGlobalFields_input{
      /**  GLAccount  */  
   GLAccount:string,
      /**  COA Code  */  
   CoaCode:string,
      /**  Flag GlobalLock  */  
   GlobalLock:boolean,
}

export interface GetGLAccountGlobalFields_output{
      /**  Return list of global fields  */  
   returnObj:string,
}

   /** Required : 
      @param COACode
      @param GLAccount
      @param ExtCompanyID
      @param isBalanceAcct
      @param balanceType
   */  
export interface GetGLAcctDispAndDesc_input{
      /**  COA Code value  */  
   COACode:string,
      /**  Account value  */  
   GLAccount:string,
      /**  External Company ID  */  
   ExtCompanyID:string,
      /**  Is balancing account?  */  
   isBalanceAcct:boolean,
      /**  Balance type  */  
   balanceType:string,
}

export interface GetGLAcctDispAndDesc_output{
parameters : {
      /**  output parameters  */  
   glAcctDisp:string,
   glAcctDesc:string,
}
}

   /** Required : 
      @param coaCode
      @param glAccount
   */  
export interface GetGLControlReferences_input{
      /**  COA Code  */  
   coaCode:string,
      /**  GL Account  */  
   glAccount:string,
}

export interface GetGLControlReferences_output{
   returnObj:Erp_Tablesets_GLCntrlAcctReferencesTableset[],
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
   returnObj:Erp_Tablesets_GLAccountListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param coACode
   */  
export interface GetNewGLAccount_input{
   ds:Erp_Tablesets_GLAccountTableset[],
   coACode:string,
}

export interface GetNewGLAccount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLAccountTableset,
}
}

   /** Required : 
      @param whereClauseGLAccount
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseGLAccount:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_GLAccountTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipCOACode
      @param ipGLAccount
   */  
export interface GlAccountExists_input{
      /**  COA Code  */  
   ipCOACode:string,
      /**  GL Account  */  
   ipGLAccount:string,
}

export interface GlAccountExists_output{
      /**  Return true if mentioned GL Account exists for the COA  */  
   returnObj:boolean,
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
      @param inpList
   */  
export interface PutListInCorrectFormat_input{
   inpList:string,
}

export interface PutListInCorrectFormat_output{
   returnObj:string,
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtGLAccountTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtGLAccountTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_GLAccountTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLAccountTableset,
}
}

   /** Required : 
      @param ipCOACode
      @param ipGLAccount
      @param ipNbrSegments
   */  
export interface ValidateAccount_input{
      /**  COA Code  */  
   ipCOACode:string,
      /**  GL Account  */  
   ipGLAccount:string,
      /**  Segment Number  */  
   ipNbrSegments:number,
}

export interface ValidateAccount_output{
}

   /** Required : 
      @param coaCode
      @param glAccount
   */  
export interface ValidateCOACode_input{
      /**  COA code entered  */  
   coaCode:string,
      /**  GL Account entered  */  
   glAccount:string,
}

export interface ValidateCOACode_output{
parameters : {
      /**  output parameters  */  
   opGlobalCOA:boolean,
}
}

   /** Required : 
      @param COACode
      @param GLAccount
      @param ExtCompanyID
      @param RestrictID
      @param EffectiveDate
      @param ValidateDynamicSegment
   */  
export interface ValidateGLAccount_input{
      /**  COA Code value  */  
   COACode:string,
      /**  Account value  */  
   GLAccount:string,
      /**  External Company ID  */  
   ExtCompanyID:string,
      /**  UI Code value  */  
   RestrictID:string,
      /**  Effective Date  */  
   EffectiveDate:string,
      /**  Validate Dynamic Segments value  */  
   ValidateDynamicSegment:boolean,
}

export interface ValidateGLAccount_output{
}

