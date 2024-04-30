import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.AgingRptFmtSvc
// Description: Aging Report Format Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AgingRptFmtSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AgingRptFmtSvc/$metadata", {
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
   Description: Get AgingRptFmts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AgingRptFmts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AgingRptFmtRow
   */  
export function get_AgingRptFmts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AgingRptFmtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AgingRptFmtSvc/AgingRptFmts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AgingRptFmtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AgingRptFmts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AgingRptFmtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.AgingRptFmtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AgingRptFmts(requestBody:Erp_Tablesets_AgingRptFmtRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AgingRptFmtSvc/AgingRptFmts", {
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
   Summary: Calls GetByID to retrieve the AgingRptFmt item
   Description: Calls GetByID to retrieve the AgingRptFmt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AgingRptFmt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FmtCode Desc: FmtCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.AgingRptFmtRow
   */  
export function get_AgingRptFmts_Company_FmtCode(Company:string, FmtCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AgingRptFmtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AgingRptFmtSvc/AgingRptFmts(" + Company + "," + FmtCode + ")", {
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
         resolve(data as Erp_Tablesets_AgingRptFmtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AgingRptFmt for the service
   Description: Calls UpdateExt to update AgingRptFmt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AgingRptFmt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FmtCode Desc: FmtCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.AgingRptFmtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AgingRptFmts_Company_FmtCode(Company:string, FmtCode:string, requestBody:Erp_Tablesets_AgingRptFmtRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AgingRptFmtSvc/AgingRptFmts(" + Company + "," + FmtCode + ")", {
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
   Summary: Call UpdateExt to delete AgingRptFmt item
   Description: Call UpdateExt to delete AgingRptFmt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AgingRptFmt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FmtCode Desc: FmtCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AgingRptFmts_Company_FmtCode(Company:string, FmtCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AgingRptFmtSvc/AgingRptFmts(" + Company + "," + FmtCode + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AgingRptFmtListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AgingRptFmtListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AgingRptFmtSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AgingRptFmtListRow)
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
export function get_GetRows(whereClauseAgingRptFmt:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseAgingRptFmt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAgingRptFmt=" + whereClauseAgingRptFmt
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AgingRptFmtSvc/GetRows" + params, {
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
export function get_GetByID(fmtCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof fmtCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "fmtCode=" + fmtCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AgingRptFmtSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AgingRptFmtSvc/GetList" + params, {
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
   Summary: Invoke method GetNewAgingRptFmt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAgingRptFmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAgingRptFmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAgingRptFmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAgingRptFmt(requestBody:GetNewAgingRptFmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAgingRptFmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AgingRptFmtSvc/GetNewAgingRptFmt", {
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
         resolve(data as GetNewAgingRptFmt_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AgingRptFmtSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AgingRptFmtSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AgingRptFmtSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AgingRptFmtSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AgingRptFmtSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AgingRptFmtListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AgingRptFmtListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AgingRptFmtRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AgingRptFmtRow,
}

export interface Erp_Tablesets_AgingRptFmtListRow{
      /**  Code the uniquely identifies an aging format.  */  
   "FmtCode":string,
      /**  Aging report format description.  */  
   "Description":string,
      /**  Default Format  */  
   "DefaultFmt":boolean,
      /**  Company Identifier.  */  
   "Company":string,
      /**  An array which establishes the number of days to be used when calculating the aging category of an invoice. This is user maintainable. The values must all be entered and be in ascending value.  Elements represent the # of days in which an invoice delinquent days must be "Greater than" in order to fall into this elements category. For example if you want to define categories of "Future, 0 - 30 days, 31 - 60, 61 - 90, 91 - 120 and 120+. The array would have values of 0, 30, 60, 90, 120.  */  
   "AgeDays2":number,
      /**  An array which establishes the number of days to be used when calculating the aging category of an invoice. This is user maintainable. The values must all be entered and be in ascending value.  Elements represent the # of days in which an invoice delinquent days must be "Greater than" in order to fall into this elements category. For example if you want to define categories of "Future, 0 - 30 days, 31 - 60, 61 - 90, 91 - 120 and 120+. The array would have values of 0, 30, 60, 90, 120.  */  
   "AgeDays4":number,
      /**  An array which establishes the number of days to be used when calculating the aging category of an invoice. This is user maintainable. The values must all be entered and be in ascending value.  Elements represent the # of days in which an invoice delinquent days must be "Greater than" in order to fall into this elements category. For example if you want to define categories of "Future, 0 - 30 days, 31 - 60, 61 - 90, 91 - 120 and 120+. The array would have values of 0, 30, 60, 90, 120.  */  
   "AgeDays5":number,
      /**  An array which establishes the number of days to be used when calculating the aging category of an invoice. This is user maintainable. The values must all be entered and be in ascending value.  Elements represent the # of days in which an invoice delinquent days must be "Greater than" in order to fall into this elements category. For example if you want to define categories of "Future, 0 - 30 days, 31 - 60, 61 - 90, 91 - 120 and 120+. The array would have values of 0, 30, 60, 90, 120.  */  
   "AgeDays3":number,
      /**  An array which establishes the number of days to be used when calculating the aging category of an invoice. This is user maintainable. The values must all be entered and be in ascending value.  Elements represent the # of days in which an invoice delinquent days must be "Greater than" in order to fall into this elements category. For example if you want to define categories of "Future, 0 - 30 days, 31 - 60, 61 - 90, 91 - 120 and 120+. The array would have values of 0, 30, 60, 90, 120.  */  
   "AgeDays1":number,
      /**  Contains the column heading labels used to describe the invoice aging categories.  */  
   "AgeLabels2":string,
      /**  Contains the column heading labels used to describe the invoice aging categories.  */  
   "AgeLabels3":string,
      /**  Contains the column heading labels used to describe the invoice aging categories.  */  
   "AgeLabels4":string,
      /**  Contains the column heading labels used to describe the invoice aging categories.  */  
   "AgeLabels6":string,
      /**  Contains the column heading labels used to describe the invoice aging categories.  */  
   "AgeLabels5":string,
      /**  Contains the column heading labels used to describe the invoice aging categories.  */  
   "AgeLabels1":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Flag to indicate if this is the default format for AP  */  
   "APDefault":boolean,
      /**  Flag to indicate if this is the default format for AR  */  
   "ARDefault":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AgingRptFmtRow{
      /**  Code the uniquely identifies an aging format.  */  
   "FmtCode":string,
      /**  Aging report format description.  */  
   "Description":string,
      /**  Default Format  */  
   "DefaultFmt":boolean,
      /**  Company Identifier.  */  
   "Company":string,
      /**  An array which establishes the number of days to be used when calculating the aging category of an invoice. This is user maintainable. The values must all be entered and be in ascending value.  Elements represent the # of days in which an invoice delinquent days must be "Greater than" in order to fall into this elements category. For example if you want to define categories of "Future, 0 - 30 days, 31 - 60, 61 - 90, 91 - 120 and 120+. The array would have values of 0, 30, 60, 90, 120.  */  
   "AgeDays2":number,
      /**  An array which establishes the number of days to be used when calculating the aging category of an invoice. This is user maintainable. The values must all be entered and be in ascending value.  Elements represent the # of days in which an invoice delinquent days must be "Greater than" in order to fall into this elements category. For example if you want to define categories of "Future, 0 - 30 days, 31 - 60, 61 - 90, 91 - 120 and 120+. The array would have values of 0, 30, 60, 90, 120.  */  
   "AgeDays4":number,
      /**  An array which establishes the number of days to be used when calculating the aging category of an invoice. This is user maintainable. The values must all be entered and be in ascending value.  Elements represent the # of days in which an invoice delinquent days must be "Greater than" in order to fall into this elements category. For example if you want to define categories of "Future, 0 - 30 days, 31 - 60, 61 - 90, 91 - 120 and 120+. The array would have values of 0, 30, 60, 90, 120.  */  
   "AgeDays5":number,
      /**  An array which establishes the number of days to be used when calculating the aging category of an invoice. This is user maintainable. The values must all be entered and be in ascending value.  Elements represent the # of days in which an invoice delinquent days must be "Greater than" in order to fall into this elements category. For example if you want to define categories of "Future, 0 - 30 days, 31 - 60, 61 - 90, 91 - 120 and 120+. The array would have values of 0, 30, 60, 90, 120.  */  
   "AgeDays3":number,
      /**  An array which establishes the number of days to be used when calculating the aging category of an invoice. This is user maintainable. The values must all be entered and be in ascending value.  Elements represent the # of days in which an invoice delinquent days must be "Greater than" in order to fall into this elements category. For example if you want to define categories of "Future, 0 - 30 days, 31 - 60, 61 - 90, 91 - 120 and 120+. The array would have values of 0, 30, 60, 90, 120.  */  
   "AgeDays1":number,
      /**  Contains the column heading labels used to describe the invoice aging categories.  */  
   "AgeLabels2":string,
      /**  Contains the column heading labels used to describe the invoice aging categories.  */  
   "AgeLabels3":string,
      /**  Contains the column heading labels used to describe the invoice aging categories.  */  
   "AgeLabels4":string,
      /**  Contains the column heading labels used to describe the invoice aging categories.  */  
   "AgeLabels6":string,
      /**  Contains the column heading labels used to describe the invoice aging categories.  */  
   "AgeLabels5":string,
      /**  Contains the column heading labels used to describe the invoice aging categories.  */  
   "AgeLabels1":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Flag to indicate if this is the default format for AP  */  
   "APDefault":boolean,
      /**  Flag to indicate if this is the default format for AR  */  
   "ARDefault":boolean,
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
      @param fmtCode
   */  
export interface DeleteByID_input{
   fmtCode:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_AgingRptFmtListRow{
      /**  Code the uniquely identifies an aging format.  */  
   FmtCode:string,
      /**  Aging report format description.  */  
   Description:string,
      /**  Default Format  */  
   DefaultFmt:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  An array which establishes the number of days to be used when calculating the aging category of an invoice. This is user maintainable. The values must all be entered and be in ascending value.  Elements represent the # of days in which an invoice delinquent days must be "Greater than" in order to fall into this elements category. For example if you want to define categories of "Future, 0 - 30 days, 31 - 60, 61 - 90, 91 - 120 and 120+. The array would have values of 0, 30, 60, 90, 120.  */  
   AgeDays2:number,
      /**  An array which establishes the number of days to be used when calculating the aging category of an invoice. This is user maintainable. The values must all be entered and be in ascending value.  Elements represent the # of days in which an invoice delinquent days must be "Greater than" in order to fall into this elements category. For example if you want to define categories of "Future, 0 - 30 days, 31 - 60, 61 - 90, 91 - 120 and 120+. The array would have values of 0, 30, 60, 90, 120.  */  
   AgeDays4:number,
      /**  An array which establishes the number of days to be used when calculating the aging category of an invoice. This is user maintainable. The values must all be entered and be in ascending value.  Elements represent the # of days in which an invoice delinquent days must be "Greater than" in order to fall into this elements category. For example if you want to define categories of "Future, 0 - 30 days, 31 - 60, 61 - 90, 91 - 120 and 120+. The array would have values of 0, 30, 60, 90, 120.  */  
   AgeDays5:number,
      /**  An array which establishes the number of days to be used when calculating the aging category of an invoice. This is user maintainable. The values must all be entered and be in ascending value.  Elements represent the # of days in which an invoice delinquent days must be "Greater than" in order to fall into this elements category. For example if you want to define categories of "Future, 0 - 30 days, 31 - 60, 61 - 90, 91 - 120 and 120+. The array would have values of 0, 30, 60, 90, 120.  */  
   AgeDays3:number,
      /**  An array which establishes the number of days to be used when calculating the aging category of an invoice. This is user maintainable. The values must all be entered and be in ascending value.  Elements represent the # of days in which an invoice delinquent days must be "Greater than" in order to fall into this elements category. For example if you want to define categories of "Future, 0 - 30 days, 31 - 60, 61 - 90, 91 - 120 and 120+. The array would have values of 0, 30, 60, 90, 120.  */  
   AgeDays1:number,
      /**  Contains the column heading labels used to describe the invoice aging categories.  */  
   AgeLabels2:string,
      /**  Contains the column heading labels used to describe the invoice aging categories.  */  
   AgeLabels3:string,
      /**  Contains the column heading labels used to describe the invoice aging categories.  */  
   AgeLabels4:string,
      /**  Contains the column heading labels used to describe the invoice aging categories.  */  
   AgeLabels6:string,
      /**  Contains the column heading labels used to describe the invoice aging categories.  */  
   AgeLabels5:string,
      /**  Contains the column heading labels used to describe the invoice aging categories.  */  
   AgeLabels1:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Flag to indicate if this is the default format for AP  */  
   APDefault:boolean,
      /**  Flag to indicate if this is the default format for AR  */  
   ARDefault:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AgingRptFmtListTableset{
   AgingRptFmtList:Erp_Tablesets_AgingRptFmtListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_AgingRptFmtRow{
      /**  Code the uniquely identifies an aging format.  */  
   FmtCode:string,
      /**  Aging report format description.  */  
   Description:string,
      /**  Default Format  */  
   DefaultFmt:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  An array which establishes the number of days to be used when calculating the aging category of an invoice. This is user maintainable. The values must all be entered and be in ascending value.  Elements represent the # of days in which an invoice delinquent days must be "Greater than" in order to fall into this elements category. For example if you want to define categories of "Future, 0 - 30 days, 31 - 60, 61 - 90, 91 - 120 and 120+. The array would have values of 0, 30, 60, 90, 120.  */  
   AgeDays2:number,
      /**  An array which establishes the number of days to be used when calculating the aging category of an invoice. This is user maintainable. The values must all be entered and be in ascending value.  Elements represent the # of days in which an invoice delinquent days must be "Greater than" in order to fall into this elements category. For example if you want to define categories of "Future, 0 - 30 days, 31 - 60, 61 - 90, 91 - 120 and 120+. The array would have values of 0, 30, 60, 90, 120.  */  
   AgeDays4:number,
      /**  An array which establishes the number of days to be used when calculating the aging category of an invoice. This is user maintainable. The values must all be entered and be in ascending value.  Elements represent the # of days in which an invoice delinquent days must be "Greater than" in order to fall into this elements category. For example if you want to define categories of "Future, 0 - 30 days, 31 - 60, 61 - 90, 91 - 120 and 120+. The array would have values of 0, 30, 60, 90, 120.  */  
   AgeDays5:number,
      /**  An array which establishes the number of days to be used when calculating the aging category of an invoice. This is user maintainable. The values must all be entered and be in ascending value.  Elements represent the # of days in which an invoice delinquent days must be "Greater than" in order to fall into this elements category. For example if you want to define categories of "Future, 0 - 30 days, 31 - 60, 61 - 90, 91 - 120 and 120+. The array would have values of 0, 30, 60, 90, 120.  */  
   AgeDays3:number,
      /**  An array which establishes the number of days to be used when calculating the aging category of an invoice. This is user maintainable. The values must all be entered and be in ascending value.  Elements represent the # of days in which an invoice delinquent days must be "Greater than" in order to fall into this elements category. For example if you want to define categories of "Future, 0 - 30 days, 31 - 60, 61 - 90, 91 - 120 and 120+. The array would have values of 0, 30, 60, 90, 120.  */  
   AgeDays1:number,
      /**  Contains the column heading labels used to describe the invoice aging categories.  */  
   AgeLabels2:string,
      /**  Contains the column heading labels used to describe the invoice aging categories.  */  
   AgeLabels3:string,
      /**  Contains the column heading labels used to describe the invoice aging categories.  */  
   AgeLabels4:string,
      /**  Contains the column heading labels used to describe the invoice aging categories.  */  
   AgeLabels6:string,
      /**  Contains the column heading labels used to describe the invoice aging categories.  */  
   AgeLabels5:string,
      /**  Contains the column heading labels used to describe the invoice aging categories.  */  
   AgeLabels1:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Flag to indicate if this is the default format for AP  */  
   APDefault:boolean,
      /**  Flag to indicate if this is the default format for AR  */  
   ARDefault:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AgingRptFmtTableset{
   AgingRptFmt:Erp_Tablesets_AgingRptFmtRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtAgingRptFmtTableset{
   AgingRptFmt:Erp_Tablesets_AgingRptFmtRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param fmtCode
   */  
export interface GetByID_input{
   fmtCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_AgingRptFmtTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_AgingRptFmtTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_AgingRptFmtTableset[],
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
   returnObj:Erp_Tablesets_AgingRptFmtListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewAgingRptFmt_input{
   ds:Erp_Tablesets_AgingRptFmtTableset[],
}

export interface GetNewAgingRptFmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AgingRptFmtTableset,
}
}

   /** Required : 
      @param whereClauseAgingRptFmt
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseAgingRptFmt:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_AgingRptFmtTableset[],
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
   ds:Erp_Tablesets_UpdExtAgingRptFmtTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtAgingRptFmtTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_AgingRptFmtTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AgingRptFmtTableset,
}
}

