import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.GLBGLAccountSvc
// Description: Add your summary for this object here
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/$metadata", {
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
   Description: Get GLBGLAccounts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLBGLAccounts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBGLAccountRow
   */  
export function get_GLBGLAccounts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBGLAccountRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/GLBGLAccounts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBGLAccountRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLBGLAccounts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLBGLAccountRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLBGLAccountRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLBGLAccounts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/GLBGLAccounts", {
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
   Summary: Calls GetByID to retrieve the GLBGLAccount item
   Description: Calls GetByID to retrieve the GLBGLAccount item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBGLAccount
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param GLAccount Desc: GLAccount   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBGLAccountRow
   */  
export function get_GLBGLAccounts_Company_ExtCompanyID_COACode_GLAccount(Company:string, ExtCompanyID:string, COACode:string, GLAccount:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLBGLAccountRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/GLBGLAccounts(" + Company + "," + ExtCompanyID + "," + COACode + "," + GLAccount + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GLBGLAccountRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLBGLAccount for the service
   Description: Calls UpdateExt to update GLBGLAccount. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLBGLAccount
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param GLAccount Desc: GLAccount   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLBGLAccountRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLBGLAccounts_Company_ExtCompanyID_COACode_GLAccount(Company:string, ExtCompanyID:string, COACode:string, GLAccount:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/GLBGLAccounts(" + Company + "," + ExtCompanyID + "," + COACode + "," + GLAccount + ")", {
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
   Summary: Call UpdateExt to delete GLBGLAccount item
   Description: Call UpdateExt to delete GLBGLAccount item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLBGLAccount
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param GLAccount Desc: GLAccount   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLBGLAccounts_Company_ExtCompanyID_COACode_GLAccount(Company:string, ExtCompanyID:string, COACode:string, GLAccount:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/GLBGLAccounts(" + Company + "," + ExtCompanyID + "," + COACode + "," + GLAccount + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbGLAccountListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbGLAccountListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbGLAccountListRow)
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
export function get_GetRows(whereClauseGLBGLAccount:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseGLBGLAccount!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLBGLAccount=" + whereClauseGLBGLAccount
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(extCompanyID:string, coACode:string, glAccount:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof extCompanyID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "extCompanyID=" + extCompanyID
   }
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/GetList" + params, {
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
   Summary: Invoke method GetNewGLBGLAccount
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLBGLAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLBGLAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLBGLAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLBGLAccount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/GetNewGLBGLAccount", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBGLAccountRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLBGLAccountRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbGLAccountListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GlbGLAccountListRow[],
}

export interface Erp_Tablesets_GLBGLAccountRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Company ID of the external company this COA was imported from.  */  
   "ExtCompanyID":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the segment separator.  This si the unique identifier for the GL Account.  */  
   "GLAccount":string,
      /**  Text that describes the account.  */  
   "AccountDesc":string,
      /**  Optional field that may be used for reporting purpose when the GL Account exceeds the space available on a printed document.  It is a shortened version of the 200 character GL Account that displays on reports.  The initial default value consits of the concatenation of the first three segments in display sequence order.  */  
   "GLShortAcct":string,
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
      /**  Indicates if the entered description shall be preserved when the tool to automatically generate GL Acocunts is used.  Default value = yes.  */  
   "PreservDesc":boolean,
      /**  Indicates if the 'Active' flag and the 'Effective Date Range' shall be preserved when the tool to automatically generate GL accounts is used.  Default value = no.  */  
   "PreserveActivation":boolean,
      /**  Indicates if this accoun tis active.  The user cannot post to an inactive account.  Yes indicates the account is active.  No indicates the account is not active.  */  
   "Active":boolean,
      /**  Date the GL Account beings to be effective.  It must be less than or equal to the Effective to date if one has been entered.  */  
   "EffFrom":string,
      /**  Date the GL Account is no longer effective.  This date must be greater than or equal to the Effective From date if one has been entered.  */  
   "EffTo":string,
      /**  A flag to indicate this GL Account my recieve multi-company journals.  */  
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
   "ExtCompID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "GlbGLAcctDispGLAcctDisp":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GlbGLAccountListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Company ID of the external company this COA was imported from.  */  
   "ExtCompanyID":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the segment separator.  This si the unique identifier for the GL Account.  */  
   "GLAccount":string,
      /**  Text that describes the account.  */  
   "AccountDesc":string,
      /**  Optional field that may be used for reporting purpose when the GL Account exceeds the space available on a printed document.  It is a shortened version of the 200 character GL Account that displays on reports.  The initial default value consits of the concatenation of the first three segments in display sequence order.  */  
   "GLShortAcct":string,
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
      /**  Indicates if the entered description shall be preserved when the tool to automatically generate GL Acocunts is used.  Default value = yes.  */  
   "PreservDesc":boolean,
      /**  Indicates if the 'Active' flag and the 'Effective Date Range' shall be preserved when the tool to automatically generate GL accounts is used.  Default value = no.  */  
   "PreserveActivation":boolean,
      /**  Indicates if this accoun tis active.  The user cannot post to an inactive account.  Yes indicates the account is active.  No indicates the account is not active.  */  
   "Active":boolean,
      /**  Date the GL Account beings to be effective.  It must be less than or equal to the Effective to date if one has been entered.  */  
   "EffFrom":string,
      /**  Date the GL Account is no longer effective.  This date must be greater than or equal to the Effective From date if one has been entered.  */  
   "EffTo":string,
      /**  A flag to indicate this GL Account my recieve multi-company journals.  */  
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
   "ExtCompID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  This is the GL Account in display order sequence.  */  
   "GlbGLAcctDispGLAcctDisp":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param extCompanyID
      @param coACode
      @param glAccount
   */  
export interface DeleteByID_input{
   extCompanyID:string,
   coACode:string,
   glAccount:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_GLBGLAccountRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Company ID of the external company this COA was imported from.  */  
   ExtCompanyID:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the segment separator.  This si the unique identifier for the GL Account.  */  
   GLAccount:string,
      /**  Text that describes the account.  */  
   AccountDesc:string,
      /**  Optional field that may be used for reporting purpose when the GL Account exceeds the space available on a printed document.  It is a shortened version of the 200 character GL Account that displays on reports.  The initial default value consits of the concatenation of the first three segments in display sequence order.  */  
   GLShortAcct:string,
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
      /**  Indicates if the entered description shall be preserved when the tool to automatically generate GL Acocunts is used.  Default value = yes.  */  
   PreservDesc:boolean,
      /**  Indicates if the 'Active' flag and the 'Effective Date Range' shall be preserved when the tool to automatically generate GL accounts is used.  Default value = no.  */  
   PreserveActivation:boolean,
      /**  Indicates if this accoun tis active.  The user cannot post to an inactive account.  Yes indicates the account is active.  No indicates the account is not active.  */  
   Active:boolean,
      /**  Date the GL Account beings to be effective.  It must be less than or equal to the Effective to date if one has been entered.  */  
   EffFrom:string,
      /**  Date the GL Account is no longer effective.  This date must be greater than or equal to the Effective From date if one has been entered.  */  
   EffTo:string,
      /**  A flag to indicate this GL Account my recieve multi-company journals.  */  
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
   ExtCompID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   GlbGLAcctDispGLAcctDisp:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLBGLAccountTableset{
   GLBGLAccount:Erp_Tablesets_GLBGLAccountRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GlbGLAccountListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Company ID of the external company this COA was imported from.  */  
   ExtCompanyID:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the segment separator.  This si the unique identifier for the GL Account.  */  
   GLAccount:string,
      /**  Text that describes the account.  */  
   AccountDesc:string,
      /**  Optional field that may be used for reporting purpose when the GL Account exceeds the space available on a printed document.  It is a shortened version of the 200 character GL Account that displays on reports.  The initial default value consits of the concatenation of the first three segments in display sequence order.  */  
   GLShortAcct:string,
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
      /**  Indicates if the entered description shall be preserved when the tool to automatically generate GL Acocunts is used.  Default value = yes.  */  
   PreservDesc:boolean,
      /**  Indicates if the 'Active' flag and the 'Effective Date Range' shall be preserved when the tool to automatically generate GL accounts is used.  Default value = no.  */  
   PreserveActivation:boolean,
      /**  Indicates if this accoun tis active.  The user cannot post to an inactive account.  Yes indicates the account is active.  No indicates the account is not active.  */  
   Active:boolean,
      /**  Date the GL Account beings to be effective.  It must be less than or equal to the Effective to date if one has been entered.  */  
   EffFrom:string,
      /**  Date the GL Account is no longer effective.  This date must be greater than or equal to the Effective From date if one has been entered.  */  
   EffTo:string,
      /**  A flag to indicate this GL Account my recieve multi-company journals.  */  
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
   ExtCompID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  This is the GL Account in display order sequence.  */  
   GlbGLAcctDispGLAcctDisp:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbGLAccountListTableset{
   GlbGLAccountList:Erp_Tablesets_GlbGLAccountListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtGLBGLAccountTableset{
   GLBGLAccount:Erp_Tablesets_GLBGLAccountRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param extCompanyID
      @param coACode
      @param glAccount
   */  
export interface GetByID_input{
   extCompanyID:string,
   coACode:string,
   glAccount:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_GLBGLAccountTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_GLBGLAccountTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_GLBGLAccountTableset[],
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
   returnObj:Erp_Tablesets_GlbGLAccountListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param extCompanyID
      @param coACode
   */  
export interface GetNewGLBGLAccount_input{
   ds:Erp_Tablesets_GLBGLAccountTableset[],
   extCompanyID:string,
   coACode:string,
}

export interface GetNewGLBGLAccount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLBGLAccountTableset[],
}
}

   /** Required : 
      @param whereClauseGLBGLAccount
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseGLBGLAccount:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_GLBGLAccountTableset[],
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
   ds:Erp_Tablesets_UpdExtGLBGLAccountTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtGLBGLAccountTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_GLBGLAccountTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLBGLAccountTableset[],
}
}

