import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.GLDailyBalanceSvc
// Description: GL Account Masks
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLDailyBalanceSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLDailyBalanceSvc/$metadata", {
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
   Description: Get GLDailyBalances items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLDailyBalances
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLAccountMasksRow
   */  
export function get_GLDailyBalances(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAccountMasksRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLDailyBalanceSvc/GLDailyBalances", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAccountMasksRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLDailyBalances
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLAccountMasksRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GLAccountMasksRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLDailyBalances(requestBody:Erp_Tablesets_GLAccountMasksRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLDailyBalanceSvc/GLDailyBalances", {
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
   Summary: Calls GetByID to retrieve the GLDailyBalance item
   Description: Calls GetByID to retrieve the GLDailyBalance item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLDailyBalance
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param MaskType Desc: MaskType   Required: True   Allow empty value : True
      @param GLMaskedAccount Desc: GLMaskedAccount   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLAccountMasksRow
   */  
export function get_GLDailyBalances_Company_COACode_BookID_MaskType_GLMaskedAccount(Company:string, COACode:string, BookID:string, MaskType:string, GLMaskedAccount:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLAccountMasksRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLDailyBalanceSvc/GLDailyBalances(" + Company + "," + COACode + "," + BookID + "," + MaskType + "," + GLMaskedAccount + ")", {
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
         resolve(data as Erp_Tablesets_GLAccountMasksRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLDailyBalance for the service
   Description: Calls UpdateExt to update GLDailyBalance. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLDailyBalance
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param MaskType Desc: MaskType   Required: True   Allow empty value : True
      @param GLMaskedAccount Desc: GLMaskedAccount   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLAccountMasksRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLDailyBalances_Company_COACode_BookID_MaskType_GLMaskedAccount(Company:string, COACode:string, BookID:string, MaskType:string, GLMaskedAccount:string, requestBody:Erp_Tablesets_GLAccountMasksRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLDailyBalanceSvc/GLDailyBalances(" + Company + "," + COACode + "," + BookID + "," + MaskType + "," + GLMaskedAccount + ")", {
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
   Summary: Call UpdateExt to delete GLDailyBalance item
   Description: Call UpdateExt to delete GLDailyBalance item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLDailyBalance
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param MaskType Desc: MaskType   Required: True   Allow empty value : True
      @param GLMaskedAccount Desc: GLMaskedAccount   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLDailyBalances_Company_COACode_BookID_MaskType_GLMaskedAccount(Company:string, COACode:string, BookID:string, MaskType:string, GLMaskedAccount:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLDailyBalanceSvc/GLDailyBalances(" + Company + "," + COACode + "," + BookID + "," + MaskType + "," + GLMaskedAccount + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLAccountMasksListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAccountMasksListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLDailyBalanceSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAccountMasksListRow)
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
export function get_GetRows(whereClauseGLAccountMasks:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseGLAccountMasks!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLAccountMasks=" + whereClauseGLAccountMasks
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLDailyBalanceSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(coACode:string, bookID:string, maskType:string, glMaskedAccount:string, epicorHeaders?:Headers){
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
   if(typeof bookID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "bookID=" + bookID
   }
   if(typeof maskType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "maskType=" + maskType
   }
   if(typeof glMaskedAccount!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "glMaskedAccount=" + glMaskedAccount
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLDailyBalanceSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLDailyBalanceSvc/GetList" + params, {
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
   Summary: Invoke method CopyMasks
   Description: This method copies all masks for a given COACode and Book to a list of Books.
   OperationID: CopyMasks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopyMasks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyMasks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyMasks(requestBody:CopyMasks_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopyMasks_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLDailyBalanceSvc/CopyMasks", {
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
         resolve(data as CopyMasks_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteMasksByBook
   Description: This method deletes all masks for a given COACode and Book.
   OperationID: DeleteMasksByBook
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteMasksByBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteMasksByBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteMasksByBook(requestBody:DeleteMasksByBook_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteMasksByBook_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLDailyBalanceSvc/DeleteMasksByBook", {
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
         resolve(data as DeleteMasksByBook_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBooksForCOACode
   Description: This method retrieves all records for table GLAccountMasks for a given COACode.
   OperationID: GetBooksForCOACode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetBooksForCOACode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBooksForCOACode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBooksForCOACode(requestBody:GetBooksForCOACode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBooksForCOACode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLDailyBalanceSvc/GetBooksForCOACode", {
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
         resolve(data as GetBooksForCOACode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateCOACode
   Description: Validate the COA code against the COA table.  If it is valid, retrieve all GLBooks with the specified COA code.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLDailyBalanceSvc/ValidateCOACode", {
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
   Summary: Invoke method GetNewGLAccountMasks
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLAccountMasks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGLAccountMasks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLAccountMasks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLAccountMasks(requestBody:GetNewGLAccountMasks_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGLAccountMasks_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLDailyBalanceSvc/GetNewGLAccountMasks", {
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
         resolve(data as GetNewGLAccountMasks_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLDailyBalanceSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLDailyBalanceSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLDailyBalanceSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLDailyBalanceSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLDailyBalanceSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAccountMasksListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLAccountMasksListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAccountMasksRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLAccountMasksRow,
}

export interface Erp_Tablesets_GLAccountMasksListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  GL Book ID  */  
   "BookID":string,
      /**   Indicates the type of Mask to search and apply.  Valid values include:
DB = Daily Balance
RU = Roll-Up Accounts
RT = Reference Type  */  
   "MaskType":string,
      /**  GL Account Mask in COA segment number format separated by the vertical bar.  This field is not intended ofr end user use.  */  
   "GLMaskedAccount":string,
      /**  GL Account Mask in COA display order format  */  
   "GLMaskAcctDisp":string,
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
      /**  This is the account/mask to use if the mask matches the transactional GL account.  Used with Alternative Retained Earnings Masks.  This field is intended for internal use only.  */  
   "TgtAccount":string,
      /**  This is the account/mask to use if the mask matches the transactional GL account.  Used with Alternative Retained Earnings Masks  */  
   "TgtAcctDisp":string,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   "TgtSegValue1":string,
      /**  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   "TgtSegValue2":string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   "TgtSegValue3":string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   "TgtSegValue4":string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   "TgtSegValue5":string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   "TgtSegValue6":string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   "TgtSegValue7":string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   "TgtSegValue8":string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   "TgtSegValue9":string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   "TgtSegValue10":string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   "TgtSegValue11":string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   "TgtSegValue12":string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   "TgtSegValue13":string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   "TgtSegValue14":string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   "TgtSegValue15":string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   "TgtSegValue16":string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   "TgtSegValue17":string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   "TgtSegValue18":string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   "TgtSegValue19":string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   "TgtSegValue20":string,
      /**  Order in which Mask is applied  */  
   "MaskRank":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLAccountMasksRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  GL Book ID  */  
   "BookID":string,
      /**   Indicates the type of Mask to search and apply.  Valid values include:
DB = Daily Balance
RU = Roll-Up Accounts
RT = Reference Type  */  
   "MaskType":string,
      /**  GL Account Mask in COA segment number format separated by the vertical bar.  This field is not intended ofr end user use.  */  
   "GLMaskedAccount":string,
      /**  GL Account Mask in COA display order format  */  
   "GLMaskAcctDisp":string,
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
      /**  This is the account/mask to use if the mask matches the transactional GL account.  Used with Alternative Retained Earnings Masks.  This field is intended for internal use only.  */  
   "TgtAccount":string,
      /**  This is the account/mask to use if the mask matches the transactional GL account.  Used with Alternative Retained Earnings Masks  */  
   "TgtAcctDisp":string,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   "TgtSegValue1":string,
      /**  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   "TgtSegValue2":string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   "TgtSegValue3":string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   "TgtSegValue4":string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   "TgtSegValue5":string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   "TgtSegValue6":string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   "TgtSegValue7":string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   "TgtSegValue8":string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   "TgtSegValue9":string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   "TgtSegValue10":string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   "TgtSegValue11":string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   "TgtSegValue12":string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   "TgtSegValue13":string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   "TgtSegValue14":string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   "TgtSegValue15":string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   "TgtSegValue16":string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   "TgtSegValue17":string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   "TgtSegValue18":string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   "TgtSegValue19":string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   "TgtSegValue20":string,
      /**  Order in which Mask is applied  */  
   "MaskRank":number,
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
      @param ipCOACode
      @param ipSourceBookID
      @param ipTargetBookIDList
      @param ds
   */  
export interface CopyMasks_input{
      /**  Chart Of Account Code  */  
   ipCOACode:string,
      /**  Source Book ID  */  
   ipSourceBookID:string,
      /**  Delimeter separated list of target Book IDs  */  
   ipTargetBookIDList:string,
   ds:Erp_Tablesets_GLDailyBalanceTableset[],
}

export interface CopyMasks_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLDailyBalanceTableset,
}
}

   /** Required : 
      @param coACode
      @param bookID
      @param maskType
      @param glMaskedAccount
   */  
export interface DeleteByID_input{
   coACode:string,
   bookID:string,
   maskType:string,
   glMaskedAccount:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param ipCOACode
      @param ipBookID
   */  
export interface DeleteMasksByBook_input{
      /**  Chart Of Account Code  */  
   ipCOACode:string,
      /**  Book ID  */  
   ipBookID:string,
}

export interface DeleteMasksByBook_output{
   returnObj:Erp_Tablesets_GLAccountMasksListTableset[],
}

export interface Erp_Tablesets_GLAccountMasksListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  GL Book ID  */  
   BookID:string,
      /**   Indicates the type of Mask to search and apply.  Valid values include:
DB = Daily Balance
RU = Roll-Up Accounts
RT = Reference Type  */  
   MaskType:string,
      /**  GL Account Mask in COA segment number format separated by the vertical bar.  This field is not intended ofr end user use.  */  
   GLMaskedAccount:string,
      /**  GL Account Mask in COA display order format  */  
   GLMaskAcctDisp:string,
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
      /**  This is the account/mask to use if the mask matches the transactional GL account.  Used with Alternative Retained Earnings Masks.  This field is intended for internal use only.  */  
   TgtAccount:string,
      /**  This is the account/mask to use if the mask matches the transactional GL account.  Used with Alternative Retained Earnings Masks  */  
   TgtAcctDisp:string,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   TgtSegValue1:string,
      /**  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   TgtSegValue2:string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   TgtSegValue3:string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   TgtSegValue4:string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   TgtSegValue5:string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   TgtSegValue6:string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   TgtSegValue7:string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   TgtSegValue8:string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   TgtSegValue9:string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   TgtSegValue10:string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   TgtSegValue11:string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   TgtSegValue12:string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   TgtSegValue13:string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   TgtSegValue14:string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   TgtSegValue15:string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   TgtSegValue16:string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   TgtSegValue17:string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   TgtSegValue18:string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   TgtSegValue19:string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   TgtSegValue20:string,
      /**  Order in which Mask is applied  */  
   MaskRank:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLAccountMasksListTableset{
   GLAccountMasksList:Erp_Tablesets_GLAccountMasksListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GLAccountMasksRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  GL Book ID  */  
   BookID:string,
      /**   Indicates the type of Mask to search and apply.  Valid values include:
DB = Daily Balance
RU = Roll-Up Accounts
RT = Reference Type  */  
   MaskType:string,
      /**  GL Account Mask in COA segment number format separated by the vertical bar.  This field is not intended ofr end user use.  */  
   GLMaskedAccount:string,
      /**  GL Account Mask in COA display order format  */  
   GLMaskAcctDisp:string,
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
      /**  This is the account/mask to use if the mask matches the transactional GL account.  Used with Alternative Retained Earnings Masks.  This field is intended for internal use only.  */  
   TgtAccount:string,
      /**  This is the account/mask to use if the mask matches the transactional GL account.  Used with Alternative Retained Earnings Masks  */  
   TgtAcctDisp:string,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   TgtSegValue1:string,
      /**  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   TgtSegValue2:string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   TgtSegValue3:string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   TgtSegValue4:string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   TgtSegValue5:string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   TgtSegValue6:string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   TgtSegValue7:string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   TgtSegValue8:string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   TgtSegValue9:string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   TgtSegValue10:string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   TgtSegValue11:string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   TgtSegValue12:string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   TgtSegValue13:string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   TgtSegValue14:string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   TgtSegValue15:string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   TgtSegValue16:string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   TgtSegValue17:string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   TgtSegValue18:string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   TgtSegValue19:string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   TgtSegValue20:string,
      /**  Order in which Mask is applied  */  
   MaskRank:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLDailyBalanceTableset{
   GLAccountMasks:Erp_Tablesets_GLAccountMasksRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtGLDailyBalanceTableset{
   GLAccountMasks:Erp_Tablesets_GLAccountMasksRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ipCOACode
   */  
export interface GetBooksForCOACode_input{
      /**  Chart Of Account Code  */  
   ipCOACode:string,
}

export interface GetBooksForCOACode_output{
   returnObj:Erp_Tablesets_GLAccountMasksListTableset[],
}

   /** Required : 
      @param coACode
      @param bookID
      @param maskType
      @param glMaskedAccount
   */  
export interface GetByID_input{
   coACode:string,
   bookID:string,
   maskType:string,
   glMaskedAccount:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_GLDailyBalanceTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_GLDailyBalanceTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_GLDailyBalanceTableset[],
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
   returnObj:Erp_Tablesets_GLAccountMasksListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param coACode
      @param bookID
      @param maskType
   */  
export interface GetNewGLAccountMasks_input{
   ds:Erp_Tablesets_GLDailyBalanceTableset[],
   coACode:string,
   bookID:string,
   maskType:string,
}

export interface GetNewGLAccountMasks_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLDailyBalanceTableset,
}
}

   /** Required : 
      @param whereClauseGLAccountMasks
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseGLAccountMasks:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_GLDailyBalanceTableset[],
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
   ds:Erp_Tablesets_UpdExtGLDailyBalanceTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtGLDailyBalanceTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_GLDailyBalanceTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLDailyBalanceTableset,
}
}

   /** Required : 
      @param ipCOACode
   */  
export interface ValidateCOACode_input{
      /**  COA Code to validate  */  
   ipCOACode:string,
}

export interface ValidateCOACode_output{
}

