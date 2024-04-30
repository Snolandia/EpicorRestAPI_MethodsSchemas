import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.WorkforceSearchSvc
// Description: Work Force Search.
           Retuns the list of SalesReps a user is authorized for
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkforceSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkforceSearchSvc/$metadata", {
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
   Description: Get WorkforceSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WorkforceSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesRepRow
   */  
export function get_WorkforceSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesRepRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkforceSearchSvc/WorkforceSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesRepRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WorkforceSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SalesRepRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.SalesRepRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WorkforceSearches(requestBody:Erp_Tablesets_SalesRepRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkforceSearchSvc/WorkforceSearches", {
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
   Summary: Calls GetByID to retrieve the WorkforceSearch item
   Description: Calls GetByID to retrieve the WorkforceSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WorkforceSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SalesRepCode Desc: SalesRepCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.SalesRepRow
   */  
export function get_WorkforceSearches_Company_SalesRepCode(Company:string, SalesRepCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SalesRepRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkforceSearchSvc/WorkforceSearches(" + Company + "," + SalesRepCode + ")", {
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
         resolve(data as Erp_Tablesets_SalesRepRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update WorkforceSearch for the service
   Description: Calls UpdateExt to update WorkforceSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WorkforceSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SalesRepCode Desc: SalesRepCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.SalesRepRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_WorkforceSearches_Company_SalesRepCode(Company:string, SalesRepCode:string, requestBody:Erp_Tablesets_SalesRepRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkforceSearchSvc/WorkforceSearches(" + Company + "," + SalesRepCode + ")", {
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
   Summary: Call UpdateExt to delete WorkforceSearch item
   Description: Call UpdateExt to delete WorkforceSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WorkforceSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SalesRepCode Desc: SalesRepCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_WorkforceSearches_Company_SalesRepCode(Company:string, SalesRepCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkforceSearchSvc/WorkforceSearches(" + Company + "," + SalesRepCode + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesRepListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesRepListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkforceSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesRepListRow)
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
export function get_GetRows(whereClauseSalesRep:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseSalesRep!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSalesRep=" + whereClauseSalesRep
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkforceSearchSvc/GetRows" + params, {
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
export function get_GetByID(salesRepCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof salesRepCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "salesRepCode=" + salesRepCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkforceSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkforceSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetListCustom
   Description: Retrieve the authorized workforces for the logged user.
   OperationID: GetListCustom
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListCustom(requestBody:GetListCustom_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListCustom_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkforceSearchSvc/GetListCustom", {
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
         resolve(data as GetListCustom_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewSalesRep
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSalesRep
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewSalesRep_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSalesRep_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSalesRep(requestBody:GetNewSalesRep_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewSalesRep_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkforceSearchSvc/GetNewSalesRep", {
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
         resolve(data as GetNewSalesRep_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkforceSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkforceSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkforceSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkforceSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkforceSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesRepListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SalesRepListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesRepRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SalesRepRow,
}

export interface Erp_Tablesets_SalesRepListRow{
      /**  Used to determine whether or not this individual appears in selection lists.  */  
   "InActive":boolean,
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique identifier of this individual assigned by the user.  */  
   "SalesRepCode":string,
      /**  Name  */  
   "Name":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SalesRepRow{
      /**  Used to determine whether or not this individual appears in selection lists.  */  
   "InActive":boolean,
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique identifier of this individual assigned by the user.  */  
   "SalesRepCode":string,
      /**  Name  */  
   "Name":string,
      /**  The default commission percent for this individual that is used as the default in Order Entry and Invoicing.  */  
   "CommissionPercent":number,
      /**  Indicates when commissions are considered as earned.  */  
   "CommissionEarnedAt":boolean,
      /**  Determines whether or not this individual will receive email alert messages.  */  
   "AlertFlag":boolean,
      /**  Address line 1  */  
   "Address1":string,
      /**  Address line 2  */  
   "Address2":string,
      /**  Address line 3  */  
   "Address3":string,
      /**  City  */  
   "City":string,
      /**  State/Province  */  
   "State":string,
      /**  Zip/Postal Code  */  
   "Zip":string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   "Country":string,
      /**  The Country.CountryNum value related to the SalesRep.Country value.  */  
   "CountryNum":number,
      /**  The individual's office phone Number.  */  
   "OfficePhoneNum":string,
      /**  The individual's fax number.  */  
   "FaxPhoneNum":string,
      /**  The individual's cell phone number.  */  
   "CellPhoneNum":string,
      /**  The individual's pager number.  */  
   "PagerNum":string,
      /**  The individual's home phone number.  */  
   "HomePhoneNum":string,
      /**  the individual's email address.  */  
   "EMailAddress":string,
      /**  The individual's title.  */  
   "SalesRepTitle":string,
      /**  The SalesRep.SalesRepCode value of the person that this individual reports to.  */  
   "RepReportsTo":string,
      /**  Comments are intended to be internal comments about a specific individual.  */  
   "Comment":string,
      /**  The Sales Manager's confidence factor, entered as a percentage, that this Sales Rep's leads, opportunities or quotes will be turned into actual sales orders.  Not viewable by the individual sales reps.  */  
   "SalesMgrConfidence":number,
      /**  Code that identifies the role of this person. Roles can be used to assign Tasks.  */  
   "RoleCode":string,
      /**  Setting this flag will give the individual the ability to view all territories when searching customers and opportunities.  This is only valid for the primary user for the salesperson.  */  
   "ViewAllTer":boolean,
      /**  Setting this flag will give this individual the ability to view the entire company when rolling up quota and pipeline information.  This is only valid for the primary user for the salesperson.  */  
   "ViewCompPipe":boolean,
      /**  Does a sale that originated via Customer Connect garner a Commission?  */  
   "WebSaleGetsCommission":boolean,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "CnvEmpID":string,
      /**  Unique identifier for a PerCon record.  */  
   "PerConID":number,
      /**  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  */  
   "SyncNameToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  */  
   "SyncAddressToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  */  
   "SyncPhoneToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  */  
   "SyncEmailToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  */  
   "SyncLinksToPerCon":boolean,
      /**  Contact's Website.  */  
   "WebSite":string,
      /**  Contact's IM.  */  
   "IM":string,
      /**  Contact's Twitter.  */  
   "Twitter":string,
      /**  Contact's LinkedIn.  */  
   "LinkedIn":string,
      /**  Contact's FaceBook.  */  
   "FaceBook":string,
      /**  User defined Link 1.  */  
   "WebLink1":string,
      /**  User defined Link 2.  */  
   "WebLink2":string,
      /**  User defined Link 3.  */  
   "WebLink3":string,
      /**  User defined Link 4.  */  
   "WebLink4":string,
      /**  User defined Link 5.  */  
   "WebLink5":string,
      /**  The Sales Manager's worst case confidence factor entered as a percentage, that this Sales Rep's leads, opportunities or quotes will be turned into actual sales orders. Not viewable by the individual sales reps.  */  
   "MgrWorstCsPct":number,
      /**  The Sales Manager's best case confidence factor entered as a percentage, that this Sales Rep's leads, opportunities or quotes will be turned into actual sales orders. Not viewable by the individual sales reps.  */  
   "MgrBestCsPct":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  This salesperson has access to ECC  */  
   "WebSalesRep":boolean,
      /**  Addisonal ECC ID this salesperson may be related to.  */  
   "ECCSalesRepCode":string,
      /**  Full name of the contact.  */  
   "PerConName":string,
   "RepReportsToName":string,
   "BitFlag":number,
   "CountryNumDescription":string,
   "RoleCodeRoleDescription":string,
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
      @param salesRepCode
   */  
export interface DeleteByID_input{
   salesRepCode:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_SalesRepListRow{
      /**  Used to determine whether or not this individual appears in selection lists.  */  
   InActive:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique identifier of this individual assigned by the user.  */  
   SalesRepCode:string,
      /**  Name  */  
   Name:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SalesRepListTableset{
   SalesRepList:Erp_Tablesets_SalesRepListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SalesRepRow{
      /**  Used to determine whether or not this individual appears in selection lists.  */  
   InActive:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique identifier of this individual assigned by the user.  */  
   SalesRepCode:string,
      /**  Name  */  
   Name:string,
      /**  The default commission percent for this individual that is used as the default in Order Entry and Invoicing.  */  
   CommissionPercent:number,
      /**  Indicates when commissions are considered as earned.  */  
   CommissionEarnedAt:boolean,
      /**  Determines whether or not this individual will receive email alert messages.  */  
   AlertFlag:boolean,
      /**  Address line 1  */  
   Address1:string,
      /**  Address line 2  */  
   Address2:string,
      /**  Address line 3  */  
   Address3:string,
      /**  City  */  
   City:string,
      /**  State/Province  */  
   State:string,
      /**  Zip/Postal Code  */  
   Zip:string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   Country:string,
      /**  The Country.CountryNum value related to the SalesRep.Country value.  */  
   CountryNum:number,
      /**  The individual's office phone Number.  */  
   OfficePhoneNum:string,
      /**  The individual's fax number.  */  
   FaxPhoneNum:string,
      /**  The individual's cell phone number.  */  
   CellPhoneNum:string,
      /**  The individual's pager number.  */  
   PagerNum:string,
      /**  The individual's home phone number.  */  
   HomePhoneNum:string,
      /**  the individual's email address.  */  
   EMailAddress:string,
      /**  The individual's title.  */  
   SalesRepTitle:string,
      /**  The SalesRep.SalesRepCode value of the person that this individual reports to.  */  
   RepReportsTo:string,
      /**  Comments are intended to be internal comments about a specific individual.  */  
   Comment:string,
      /**  The Sales Manager's confidence factor, entered as a percentage, that this Sales Rep's leads, opportunities or quotes will be turned into actual sales orders.  Not viewable by the individual sales reps.  */  
   SalesMgrConfidence:number,
      /**  Code that identifies the role of this person. Roles can be used to assign Tasks.  */  
   RoleCode:string,
      /**  Setting this flag will give the individual the ability to view all territories when searching customers and opportunities.  This is only valid for the primary user for the salesperson.  */  
   ViewAllTer:boolean,
      /**  Setting this flag will give this individual the ability to view the entire company when rolling up quota and pipeline information.  This is only valid for the primary user for the salesperson.  */  
   ViewCompPipe:boolean,
      /**  Does a sale that originated via Customer Connect garner a Commission?  */  
   WebSaleGetsCommission:boolean,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   CnvEmpID:string,
      /**  Unique identifier for a PerCon record.  */  
   PerConID:number,
      /**  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  */  
   SyncNameToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  */  
   SyncAddressToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  */  
   SyncPhoneToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  */  
   SyncEmailToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  */  
   SyncLinksToPerCon:boolean,
      /**  Contact's Website.  */  
   WebSite:string,
      /**  Contact's IM.  */  
   IM:string,
      /**  Contact's Twitter.  */  
   Twitter:string,
      /**  Contact's LinkedIn.  */  
   LinkedIn:string,
      /**  Contact's FaceBook.  */  
   FaceBook:string,
      /**  User defined Link 1.  */  
   WebLink1:string,
      /**  User defined Link 2.  */  
   WebLink2:string,
      /**  User defined Link 3.  */  
   WebLink3:string,
      /**  User defined Link 4.  */  
   WebLink4:string,
      /**  User defined Link 5.  */  
   WebLink5:string,
      /**  The Sales Manager's worst case confidence factor entered as a percentage, that this Sales Rep's leads, opportunities or quotes will be turned into actual sales orders. Not viewable by the individual sales reps.  */  
   MgrWorstCsPct:number,
      /**  The Sales Manager's best case confidence factor entered as a percentage, that this Sales Rep's leads, opportunities or quotes will be turned into actual sales orders. Not viewable by the individual sales reps.  */  
   MgrBestCsPct:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  This salesperson has access to ECC  */  
   WebSalesRep:boolean,
      /**  Addisonal ECC ID this salesperson may be related to.  */  
   ECCSalesRepCode:string,
      /**  Full name of the contact.  */  
   PerConName:string,
   RepReportsToName:string,
   BitFlag:number,
   CountryNumDescription:string,
   RoleCodeRoleDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtWorkforceSearchTableset{
   SalesRep:Erp_Tablesets_SalesRepRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_WorkforceSearchTableset{
   SalesRep:Erp_Tablesets_SalesRepRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param salesRepCode
   */  
export interface GetByID_input{
   salesRepCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_WorkforceSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_WorkforceSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_WorkforceSearchTableset[],
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListCustom_input{
   whereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetListCustom_output{
   returnObj:Erp_Tablesets_SalesRepListTableset[],
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
   returnObj:Erp_Tablesets_SalesRepListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewSalesRep_input{
   ds:Erp_Tablesets_WorkforceSearchTableset[],
}

export interface GetNewSalesRep_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WorkforceSearchTableset,
}
}

   /** Required : 
      @param whereClauseSalesRep
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseSalesRep:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_WorkforceSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtWorkforceSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtWorkforceSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_WorkforceSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WorkforceSearchTableset,
}
}

