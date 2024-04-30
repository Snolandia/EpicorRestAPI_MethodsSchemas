import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.RMADtlSearchSvc
// Description: Search for RMADtl records
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/$metadata", {
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
   Description: Get RMADtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RMADtlSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMADtlRow
   */  
export function get_RMADtlSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMADtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/RMADtlSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMADtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RMADtlSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RMADtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RMADtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RMADtlSearches(requestBody:Erp_Tablesets_RMADtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/RMADtlSearches", {
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
   Summary: Calls GetByID to retrieve the RMADtlSearch item
   Description: Calls GetByID to retrieve the RMADtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RMADtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param RMALine Desc: RMALine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RMADtlRow
   */  
export function get_RMADtlSearches_Company_RMANum_RMALine(Company:string, RMANum:string, RMALine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RMADtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/RMADtlSearches(" + Company + "," + RMANum + "," + RMALine + ")", {
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
         resolve(data as Erp_Tablesets_RMADtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RMADtlSearch for the service
   Description: Calls UpdateExt to update RMADtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RMADtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param RMALine Desc: RMALine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RMADtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RMADtlSearches_Company_RMANum_RMALine(Company:string, RMANum:string, RMALine:string, requestBody:Erp_Tablesets_RMADtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/RMADtlSearches(" + Company + "," + RMANum + "," + RMALine + ")", {
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
   Summary: Call UpdateExt to delete RMADtlSearch item
   Description: Call UpdateExt to delete RMADtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RMADtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RMANum Desc: RMANum   Required: True
      @param RMALine Desc: RMALine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RMADtlSearches_Company_RMANum_RMALine(Company:string, RMANum:string, RMALine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/RMADtlSearches(" + Company + "," + RMANum + "," + RMALine + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMADtlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMADtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMADtlListRow)
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
export function get_GetRows(whereClauseRMADtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseRMADtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRMADtl=" + whereClauseRMADtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/GetRows" + params, {
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(rmANum:string, rmALine:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof rmANum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "rmANum=" + rmANum
   }
   if(typeof rmALine!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "rmALine=" + rmALine
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetRowsContactTracker
   Description: Calls the normal GetRows method and then if a customer ID has been passed, it screens out only the appropriate rows.
   OperationID: GetRowsContactTracker
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsContactTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsContactTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsContactTracker(requestBody:GetRowsContactTracker_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsContactTracker_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/GetRowsContactTracker", {
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
         resolve(data as GetRowsContactTracker_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsCustomerTrackerAndSort
   Description: Calls the normal GetRows method and then constructs a custom data set combining Job and Order fields for the customer tracker.
   OperationID: GetRowsCustomerTrackerAndSort
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTrackerAndSort_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTrackerAndSort_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCustomerTrackerAndSort(requestBody:GetRowsCustomerTrackerAndSort_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsCustomerTrackerAndSort_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/GetRowsCustomerTrackerAndSort", {
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
         resolve(data as GetRowsCustomerTrackerAndSort_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsCustomerTracker
   Description: Calls the normal GetRows method and then if a customer ID has been passed, it screens out only the appropriate rows.
   OperationID: GetRowsCustomerTracker
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCustomerTracker(requestBody:GetRowsCustomerTracker_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsCustomerTracker_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/GetRowsCustomerTracker", {
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
         resolve(data as GetRowsCustomerTracker_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsProjectTracker
   Description: Get all RMA's associated with orders for this projectID
   OperationID: GetRowsProjectTracker
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsProjectTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsProjectTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsProjectTracker(requestBody:GetRowsProjectTracker_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsProjectTracker_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/GetRowsProjectTracker", {
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
         resolve(data as GetRowsProjectTracker_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRMADtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRMADtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRMADtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRMADtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRMADtl(requestBody:GetNewRMADtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRMADtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/GetNewRMADtl", {
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
         resolve(data as GetNewRMADtl_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMADtlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RMADtlListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMADtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RMADtlRow,
}

export interface Erp_Tablesets_RMADtlListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Mirror image of RMAHead.OpenRMA.  */  
   "OpenRMA":boolean,
      /**  Indicates the Open/Closed status of the RMADtl.  This gets set to closed when there are no pending actions to be taken on related receipts.  */  
   "OpenDtl":boolean,
      /**  Return Authorization Number. Used to relate RMADtl to RMAHead.  */  
   "RMANum":number,
      /**  An integer that uniquely identifies a detail record within a Return Authorization document. Assigned by the system. Generated by reading last related RMADtl record and use its RALine 1.  */  
   "RMALine":number,
      /**   The sales order number that the Return detail is related to.
Must be an order of the customer identified in the RMAHead.  When entered the OrderLine is then mandatory.  */  
   "OrderNum":number,
      /**  Sales order line that the Return detail is related to.  If entered it must be valid in the OrderDtl file. If entered the OrderDtl supplies the Part Number, LineDesc, IUM . . .  */  
   "OrderLine":number,
      /**  Reason code that links this return detail  to a Reason master record, which indicates why the item is being returned  and allows the system the ability to recap scrap by a code for analysis purposes. Uses Reason.ReasonType = "C" (customer returns) to find Reason master.  */  
   "ReturnReasonCode":string,
      /**   Notes the about the RMA detail.
Used to key in customer comments, explanation of why item is returned, inspection results, Order/Mfg instructions, and perhaps information concerning Billing.  */  
   "Note":string,
      /**  The user's Internal Part number used to identify line item part. It cannot  be blank. It does NOT have to valid in the Part master.  Defaulted from the OrderDtl if available.  */  
   "PartNum":string,
      /**  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  */  
   "LineDesc":string,
      /**  Optional field that contains the customers revision.  Default OrderDtl if available, else from finding the PartRev that is most current as of entry date.  */  
   "RevisionNum":string,
      /**  Quantity that is to be returned  */  
   "ReturnQty":number,
      /**  Unit Of Measure of the  ReturnQty.  */  
   "ReturnQtyUOM":string,
      /**  Reference Invoice number used for finding Tax Category  */  
   "RefInvoiceNum":number,
      /**  Reference invoice line - Used to obtain the correct tax category  */  
   "RefInvoiceLine":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  The Ship to number of the related header contact.  */  
   "ShipToNum":string,
      /**  The Contact Number of the related header contact  */  
   "ConNum":number,
      /**  Contains the system internal customer number used to relate this record to the customer master.  */  
   "CustNum":number,
      /**  The order release number that the RMA line was created from.  */  
   "OrderRelNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Reference AR Invoice Number  */  
   "InvoiceNum":number,
      /**  Reference AR Invoice Line Number  */  
   "InvoiceLine":number,
      /**  Job Number.  */  
   "JobNum":string,
      /**  Assembly sequence number that this material is associated with.  */  
   "AssemblySeq":number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  */  
   "MtlSeq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CustomerCustID":string,
      /**  From RMAHead.DebitMemoRef, used by Customer Tracker  */  
   "DebitMemoRef":string,
   "EnableDelete":boolean,
   "EnableUpdate":boolean,
      /**  From RMAHead.HDCaseNum, used by Customer Tracker  */  
   "HDCaseNum":number,
      /**  Set from RMAHead.RMADate, used by Customer Tracker  */  
   "RMADate":string,
   "RMARcptExists":boolean,
   "CustomerContactName":string,
   "CustomerShipToName":string,
   "CustomerName":string,
   "ShipToName":string,
   "CustomerContactEMailAddress":string,
      /**  Flag to determine if Serial Numbers are required for this transaction.  */  
   "EnableSN":boolean,
      /**  Customer Id of the third-party Ship To  */  
   "ShipToCustID":string,
   "LegalNumber":string,
      /**  The member's name on the credit card.  */  
   "OrderNumCardMemberName":string,
      /**  A unique code that identifies the currency.  */  
   "OrderNumCurrencyCode":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartNumSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartNumTrackLots":boolean,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartNumSellingFactor":number,
      /**  Indicates if this part is serial number tracked  */  
   "PartNumTrackSerialNum":boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
      /**  Full description of Reason... used on displays/reports.  */  
   "ReasonDescription":string,
      /**  Full description of Reason... used on displays/reports.  */  
   "ReturnReasonCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RMADtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Mirror image of RMAHead.OpenRMA.  */  
   "OpenRMA":boolean,
      /**  Indicates the Open/Closed status of the RMADtl.  This gets set to closed when there are no pending actions to be taken on related receipts.  */  
   "OpenDtl":boolean,
      /**  Return Authorization Number. Used to relate RMADtl to RMAHead.  */  
   "RMANum":number,
      /**  An integer that uniquely identifies a detail record within a Return Authorization document. Assigned by the system. Generated by reading last related RMADtl record and use its RALine 1.  */  
   "RMALine":number,
      /**   The sales order number that the Return detail is related to.
Must be an order of the customer identified in the RMAHead.  When entered the OrderLine is then mandatory.  */  
   "OrderNum":number,
      /**  Sales order line that the Return detail is related to.  If entered it must be valid in the OrderDtl file. If entered the OrderDtl supplies the Part Number, LineDesc, IUM . . .  */  
   "OrderLine":number,
      /**  Reason code that links this return detail  to a Reason master record, which indicates why the item is being returned  and allows the system the ability to recap scrap by a code for analysis purposes. Uses Reason.ReasonType = "C" (customer returns) to find Reason master.  */  
   "ReturnReasonCode":string,
      /**   Notes the about the RMA detail.
Used to key in customer comments, explanation of why item is returned, inspection results, Order/Mfg instructions, and perhaps information concerning Billing.  */  
   "Note":string,
      /**  The user's Internal Part number used to identify line item part. It cannot  be blank. It does NOT have to valid in the Part master.  Defaulted from the OrderDtl if available.  */  
   "PartNum":string,
      /**  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  */  
   "LineDesc":string,
      /**  Optional field that contains the customers revision.  Default OrderDtl if available, else from finding the PartRev that is most current as of entry date.  */  
   "RevisionNum":string,
      /**  Quantity that is to be returned  */  
   "ReturnQty":number,
      /**  Unit Of Measure of the  ReturnQty.  */  
   "ReturnQtyUOM":string,
      /**  Reference Invoice number used for finding Tax Category  */  
   "RefInvoiceNum":number,
      /**  Reference invoice line - Used to obtain the correct tax category  */  
   "RefInvoiceLine":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  The Ship to number of the related header contact.  */  
   "ShipToNum":string,
      /**  The Contact Number of the related header contact  */  
   "ConNum":number,
      /**  Contains the system internal customer number used to relate this record to the customer master.  */  
   "CustNum":number,
      /**  The order release number that the RMA line was created from.  */  
   "OrderRelNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Reference AR Invoice Number  */  
   "InvoiceNum":number,
      /**  Reference AR Invoice Line Number  */  
   "InvoiceLine":number,
      /**  Job Number.  */  
   "JobNum":string,
      /**  Assembly sequence number that this material is associated with.  */  
   "AssemblySeq":number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  */  
   "MtlSeq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ECC RMA Comment  */  
   "ECCComment":string,
      /**  ECC RMA Num  */  
   "ECCRMANum":string,
      /**  ECC RMA Line  */  
   "ECCRMALine":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  CNDeclarationBillLine  */  
   "CNDeclarationBillLine":number,
      /**  Indicates that the line of the invoice has multiple packs consolidated. Details of the pack should be reviewied in InvcDtlPack table  */  
   "ConsolidateLines":boolean,
      /**  Indicates that the invoice line has consolidated shipment lines that are related to the same release of the sales order  */  
   "ConsolidateOneRelease":boolean,
   "CustomerContactEMailAddress":string,
      /**  The full customer's name.  */  
   "CustomerName":string,
      /**  The name for the ship to location.  */  
   "CustomerShipToName":string,
      /**  From RMAHead.DebitMemoRef, used by Customer Tracker  */  
   "DebitMemoRef":string,
      /**  If company parameter 'Allow Multiple Credit Invoices' is off and there is a least one credit memo then another credit memo adding is not allowed.  */  
   "EnableAddCreditMemo":boolean,
   "EnableDelete":boolean,
      /**  Flag to determine if Serial Numbers are required for this transaction.  */  
   "EnableSN":boolean,
   "EnableUpdate":boolean,
      /**  Determines if the RMA is synchronized with Epicor FSA application.  */  
   "EpicorFSA":boolean,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderNum":number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderResourceNum":number,
      /**  Serivce Type  */  
   "FSAServiceType":string,
      /**  Technician  */  
   "FSATechnician":string,
      /**  From RMAHead.HDCaseNum, used by Customer Tracker  */  
   "HDCaseNum":number,
      /**  Unique identifier of related integration record.  */  
   "IntExternalKey":string,
   "LegalNumber":string,
   "LocalizationFlag":string,
      /**  Set from RMAHead.RMADate, used by Customer Tracker  */  
   "RMADate":string,
   "RMARcptExists":boolean,
      /**  Customer Id of the third-party Ship To  */  
   "ShipToCustID":string,
      /**  The name for the ship to location.  */  
   "ShipToName":string,
   "CustomerContactName":string,
      /**  The customer ID.  */  
   "CustomerCustID":string,
   "CNDeclarationBill":string,
   "BitFlag":number,
   "AttrValueSetDescription":string,
   "AttrValueSetShortDescription":string,
   "OrderNumCardMemberName":string,
   "OrderNumCurrencyCode":string,
   "PartNumAttrClassID":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumSellingFactor":number,
   "PartNumPartDescription":string,
   "PartNumIUM":string,
   "PartNumPricePerCode":string,
   "PartNumTrackDimension":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumSalesUM":string,
   "PartNumTrackLots":boolean,
   "PartNumTrackInventoryAttributes":boolean,
   "ReasonDescription":string,
   "ReturnReasonCodeDescription":string,
   "ShipToNumInactive":boolean,
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
      @param rmANum
      @param rmALine
   */  
export interface DeleteByID_input{
   rmANum:number,
   rmALine:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_RMADtlListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Mirror image of RMAHead.OpenRMA.  */  
   OpenRMA:boolean,
      /**  Indicates the Open/Closed status of the RMADtl.  This gets set to closed when there are no pending actions to be taken on related receipts.  */  
   OpenDtl:boolean,
      /**  Return Authorization Number. Used to relate RMADtl to RMAHead.  */  
   RMANum:number,
      /**  An integer that uniquely identifies a detail record within a Return Authorization document. Assigned by the system. Generated by reading last related RMADtl record and use its RALine 1.  */  
   RMALine:number,
      /**   The sales order number that the Return detail is related to.
Must be an order of the customer identified in the RMAHead.  When entered the OrderLine is then mandatory.  */  
   OrderNum:number,
      /**  Sales order line that the Return detail is related to.  If entered it must be valid in the OrderDtl file. If entered the OrderDtl supplies the Part Number, LineDesc, IUM . . .  */  
   OrderLine:number,
      /**  Reason code that links this return detail  to a Reason master record, which indicates why the item is being returned  and allows the system the ability to recap scrap by a code for analysis purposes. Uses Reason.ReasonType = "C" (customer returns) to find Reason master.  */  
   ReturnReasonCode:string,
      /**   Notes the about the RMA detail.
Used to key in customer comments, explanation of why item is returned, inspection results, Order/Mfg instructions, and perhaps information concerning Billing.  */  
   Note:string,
      /**  The user's Internal Part number used to identify line item part. It cannot  be blank. It does NOT have to valid in the Part master.  Defaulted from the OrderDtl if available.  */  
   PartNum:string,
      /**  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  */  
   LineDesc:string,
      /**  Optional field that contains the customers revision.  Default OrderDtl if available, else from finding the PartRev that is most current as of entry date.  */  
   RevisionNum:string,
      /**  Quantity that is to be returned  */  
   ReturnQty:number,
      /**  Unit Of Measure of the  ReturnQty.  */  
   ReturnQtyUOM:string,
      /**  Reference Invoice number used for finding Tax Category  */  
   RefInvoiceNum:number,
      /**  Reference invoice line - Used to obtain the correct tax category  */  
   RefInvoiceLine:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  The Ship to number of the related header contact.  */  
   ShipToNum:string,
      /**  The Contact Number of the related header contact  */  
   ConNum:number,
      /**  Contains the system internal customer number used to relate this record to the customer master.  */  
   CustNum:number,
      /**  The order release number that the RMA line was created from.  */  
   OrderRelNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Reference AR Invoice Number  */  
   InvoiceNum:number,
      /**  Reference AR Invoice Line Number  */  
   InvoiceLine:number,
      /**  Job Number.  */  
   JobNum:string,
      /**  Assembly sequence number that this material is associated with.  */  
   AssemblySeq:number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  */  
   MtlSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CustomerCustID:string,
      /**  From RMAHead.DebitMemoRef, used by Customer Tracker  */  
   DebitMemoRef:string,
   EnableDelete:boolean,
   EnableUpdate:boolean,
      /**  From RMAHead.HDCaseNum, used by Customer Tracker  */  
   HDCaseNum:number,
      /**  Set from RMAHead.RMADate, used by Customer Tracker  */  
   RMADate:string,
   RMARcptExists:boolean,
   CustomerContactName:string,
   CustomerShipToName:string,
   CustomerName:string,
   ShipToName:string,
   CustomerContactEMailAddress:string,
      /**  Flag to determine if Serial Numbers are required for this transaction.  */  
   EnableSN:boolean,
      /**  Customer Id of the third-party Ship To  */  
   ShipToCustID:string,
   LegalNumber:string,
      /**  The member's name on the credit card.  */  
   OrderNumCardMemberName:string,
      /**  A unique code that identifies the currency.  */  
   OrderNumCurrencyCode:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartNumTrackLots:boolean,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartNumSellingFactor:number,
      /**  Indicates if this part is serial number tracked  */  
   PartNumTrackSerialNum:boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
      /**  Full description of Reason... used on displays/reports.  */  
   ReasonDescription:string,
      /**  Full description of Reason... used on displays/reports.  */  
   ReturnReasonCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RMADtlListTableset{
   RMADtlList:Erp_Tablesets_RMADtlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_RMADtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Mirror image of RMAHead.OpenRMA.  */  
   OpenRMA:boolean,
      /**  Indicates the Open/Closed status of the RMADtl.  This gets set to closed when there are no pending actions to be taken on related receipts.  */  
   OpenDtl:boolean,
      /**  Return Authorization Number. Used to relate RMADtl to RMAHead.  */  
   RMANum:number,
      /**  An integer that uniquely identifies a detail record within a Return Authorization document. Assigned by the system. Generated by reading last related RMADtl record and use its RALine 1.  */  
   RMALine:number,
      /**   The sales order number that the Return detail is related to.
Must be an order of the customer identified in the RMAHead.  When entered the OrderLine is then mandatory.  */  
   OrderNum:number,
      /**  Sales order line that the Return detail is related to.  If entered it must be valid in the OrderDtl file. If entered the OrderDtl supplies the Part Number, LineDesc, IUM . . .  */  
   OrderLine:number,
      /**  Reason code that links this return detail  to a Reason master record, which indicates why the item is being returned  and allows the system the ability to recap scrap by a code for analysis purposes. Uses Reason.ReasonType = "C" (customer returns) to find Reason master.  */  
   ReturnReasonCode:string,
      /**   Notes the about the RMA detail.
Used to key in customer comments, explanation of why item is returned, inspection results, Order/Mfg instructions, and perhaps information concerning Billing.  */  
   Note:string,
      /**  The user's Internal Part number used to identify line item part. It cannot  be blank. It does NOT have to valid in the Part master.  Defaulted from the OrderDtl if available.  */  
   PartNum:string,
      /**  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  */  
   LineDesc:string,
      /**  Optional field that contains the customers revision.  Default OrderDtl if available, else from finding the PartRev that is most current as of entry date.  */  
   RevisionNum:string,
      /**  Quantity that is to be returned  */  
   ReturnQty:number,
      /**  Unit Of Measure of the  ReturnQty.  */  
   ReturnQtyUOM:string,
      /**  Reference Invoice number used for finding Tax Category  */  
   RefInvoiceNum:number,
      /**  Reference invoice line - Used to obtain the correct tax category  */  
   RefInvoiceLine:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  The Ship to number of the related header contact.  */  
   ShipToNum:string,
      /**  The Contact Number of the related header contact  */  
   ConNum:number,
      /**  Contains the system internal customer number used to relate this record to the customer master.  */  
   CustNum:number,
      /**  The order release number that the RMA line was created from.  */  
   OrderRelNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Reference AR Invoice Number  */  
   InvoiceNum:number,
      /**  Reference AR Invoice Line Number  */  
   InvoiceLine:number,
      /**  Job Number.  */  
   JobNum:string,
      /**  Assembly sequence number that this material is associated with.  */  
   AssemblySeq:number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  */  
   MtlSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ECC RMA Comment  */  
   ECCComment:string,
      /**  ECC RMA Num  */  
   ECCRMANum:string,
      /**  ECC RMA Line  */  
   ECCRMALine:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  CNDeclarationBillLine  */  
   CNDeclarationBillLine:number,
      /**  Indicates that the line of the invoice has multiple packs consolidated. Details of the pack should be reviewied in InvcDtlPack table  */  
   ConsolidateLines:boolean,
      /**  Indicates that the invoice line has consolidated shipment lines that are related to the same release of the sales order  */  
   ConsolidateOneRelease:boolean,
   CustomerContactEMailAddress:string,
      /**  The full customer's name.  */  
   CustomerName:string,
      /**  The name for the ship to location.  */  
   CustomerShipToName:string,
      /**  From RMAHead.DebitMemoRef, used by Customer Tracker  */  
   DebitMemoRef:string,
      /**  If company parameter 'Allow Multiple Credit Invoices' is off and there is a least one credit memo then another credit memo adding is not allowed.  */  
   EnableAddCreditMemo:boolean,
   EnableDelete:boolean,
      /**  Flag to determine if Serial Numbers are required for this transaction.  */  
   EnableSN:boolean,
   EnableUpdate:boolean,
      /**  Determines if the RMA is synchronized with Epicor FSA application.  */  
   EpicorFSA:boolean,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderNum:number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderResourceNum:number,
      /**  Serivce Type  */  
   FSAServiceType:string,
      /**  Technician  */  
   FSATechnician:string,
      /**  From RMAHead.HDCaseNum, used by Customer Tracker  */  
   HDCaseNum:number,
      /**  Unique identifier of related integration record.  */  
   IntExternalKey:string,
   LegalNumber:string,
   LocalizationFlag:string,
      /**  Set from RMAHead.RMADate, used by Customer Tracker  */  
   RMADate:string,
   RMARcptExists:boolean,
      /**  Customer Id of the third-party Ship To  */  
   ShipToCustID:string,
      /**  The name for the ship to location.  */  
   ShipToName:string,
   CustomerContactName:string,
      /**  The customer ID.  */  
   CustomerCustID:string,
   CNDeclarationBill:string,
   BitFlag:number,
   AttrValueSetDescription:string,
   AttrValueSetShortDescription:string,
   OrderNumCardMemberName:string,
   OrderNumCurrencyCode:string,
   PartNumAttrClassID:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumSellingFactor:number,
   PartNumPartDescription:string,
   PartNumIUM:string,
   PartNumPricePerCode:string,
   PartNumTrackDimension:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumSalesUM:string,
   PartNumTrackLots:boolean,
   PartNumTrackInventoryAttributes:boolean,
   ReasonDescription:string,
   ReturnReasonCodeDescription:string,
   ShipToNumInactive:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RMADtlSearchTableset{
   RMADtl:Erp_Tablesets_RMADtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtRMADtlSearchTableset{
   RMADtl:Erp_Tablesets_RMADtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param rmANum
      @param rmALine
   */  
export interface GetByID_input{
   rmANum:number,
   rmALine:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_RMADtlSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_RMADtlSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_RMADtlSearchTableset[],
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
   returnObj:Erp_Tablesets_RMADtlListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param rmANum
   */  
export interface GetNewRMADtl_input{
   ds:Erp_Tablesets_RMADtlSearchTableset[],
   rmANum:number,
}

export interface GetNewRMADtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMADtlSearchTableset,
}
}

   /** Required : 
      @param whereClauseRMADtl
      @param contactName
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsContactTracker_input{
      /**  Whereclause for RMADtl table.  */  
   whereClauseRMADtl:string,
      /**  The contact to return data for.  */  
   contactName:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsContactTracker_output{
   returnObj:Erp_Tablesets_RMADtlSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseRMADtl
      @param whereClauseRMAHead
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustomerTrackerAndSort_input{
      /**  Whereclause for RMADtl table.  */  
   whereClauseRMADtl:string,
      /**  Whereclause for RMAHead table.  */  
   whereClauseRMAHead:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsCustomerTrackerAndSort_output{
   returnObj:Erp_Tablesets_RMADtlSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseRMADtl
      @param whereClauseRMAHead
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustomerTracker_input{
      /**  Whereclause for RMADtl table.  */  
   whereClauseRMADtl:string,
      /**  Whereclause for RMAHead table.  */  
   whereClauseRMAHead:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsCustomerTracker_output{
   returnObj:Erp_Tablesets_RMADtlSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipProjectID
   */  
export interface GetRowsProjectTracker_input{
      /**  The Project ID  */  
   ipProjectID:string,
}

export interface GetRowsProjectTracker_output{
   returnObj:Erp_Tablesets_RMADtlSearchTableset[],
}

   /** Required : 
      @param whereClauseRMADtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseRMADtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_RMADtlSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtRMADtlSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtRMADtlSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_RMADtlSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RMADtlSearchTableset,
}
}

