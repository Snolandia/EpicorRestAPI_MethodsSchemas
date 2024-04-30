import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.RFQEntryQuoteSearchSvc
// Description: This is a QuoteSearch object for RFQEntr.
It is used to display Quotes which are relevant in
Add From Quote functionality of RFQEntry.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/$metadata", {
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
   Description: Get RFQEntryQuoteSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQEntryQuoteSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteHedRow
   */  
export function get_RFQEntryQuoteSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/RFQEntryQuoteSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQEntryQuoteSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.QuoteHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RFQEntryQuoteSearches(requestBody:Erp_Tablesets_QuoteHedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/RFQEntryQuoteSearches", {
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
   Summary: Calls GetByID to retrieve the RFQEntryQuoteSearch item
   Description: Calls GetByID to retrieve the RFQEntryQuoteSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQEntryQuoteSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.QuoteHedRow
   */  
export function get_RFQEntryQuoteSearches_Company_QuoteNum(Company:string, QuoteNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/RFQEntryQuoteSearches(" + Company + "," + QuoteNum + ")", {
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
         resolve(data as Erp_Tablesets_QuoteHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RFQEntryQuoteSearch for the service
   Description: Calls UpdateExt to update RFQEntryQuoteSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQEntryQuoteSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RFQEntryQuoteSearches_Company_QuoteNum(Company:string, QuoteNum:string, requestBody:Erp_Tablesets_QuoteHedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/RFQEntryQuoteSearches(" + Company + "," + QuoteNum + ")", {
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
   Summary: Call UpdateExt to delete RFQEntryQuoteSearch item
   Description: Call UpdateExt to delete RFQEntryQuoteSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQEntryQuoteSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RFQEntryQuoteSearches_Company_QuoteNum(Company:string, QuoteNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/RFQEntryQuoteSearches(" + Company + "," + QuoteNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteHedListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedListRow)
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
export function get_GetRows(whereClauseQuoteHed:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseQuoteHed!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteHed=" + whereClauseQuoteHed
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/GetRows" + params, {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(quoteNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof quoteNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "quoteNum=" + quoteNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewQuoteHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteHed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewQuoteHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteHed(requestBody:GetNewQuoteHed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewQuoteHed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/GetNewQuoteHed", {
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
         resolve(data as GetNewQuoteHed_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteHedListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteHedRow,
}

export interface Erp_Tablesets_QuoteHedListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number is an integer which is used to uniquely identify a quote within the system.  This is automatically assigned by the system when the user requests to create a new quote. To create a new quote the user either takes an "add" option or leaves the Quote Number fill-in zero. The system generates a number by finding the quote number of the last record on file and then a 1 to it. It then uses the greater of Last quote number + 1 or the EQSyst.StartQuoteNum.  */  
   "QuoteNum":number,
      /**  Contains the internal Customer number that the links the quote to the customer master. This is not directly entered by the user. Instead the CustID is entered which provides the CustNum from the customer master. The quote must reference a valid Customer master.  */  
   "CustNum":number,
      /**  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  */  
   "DueDate":string,
      /**  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  */  
   "Quoted":boolean,
      /**  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  */  
   "DateQuoted":string,
      /**   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.

This date is also used as part of the quote purging criteria testing.  */  
   "ExpirationDate":string,
      /**  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  */  
   "FollowUpDate":string,
      /**  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  */  
   "Reference":string,
      /**  Indicates if the Quote has expired.  A quote is expired when QuoteHed.ExpirationDate < Today.  Each time a user logs on the system does a quick check for any unexpired quotes that have an expiration date < Today and sets them as expired. This field is also set during the QuoteHed write trigger.  */  
   "Expired":boolean,
      /**  Full Description for CurrentStage field  */  
   "CurrentStageDesc":string,
      /**  Link to the territory Id for this LOQ  */  
   "TerritoryID":string,
      /**  Link to Task set  */  
   "TaskSetID":string,
      /**   Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  */  
   "CurrentStage":string,
      /**  Bill to customer id.  */  
   "BTCustID":string,
      /**  The Currently active Stage changing task  */  
   "ActiveTaskID":string,
      /**  Bill to customer name.  */  
   "BTCustomerName":string,
      /**  The Last Complete Milestone task  */  
   "LastTaskID":string,
   "CustomerName":string,
   "TerritoryTerritoryDesc":string,
      /**  Indicates the Type of reason for closing this quote.   "W" Win CRM "L" - Loss CRM, "T" Task CRM.  */  
   "ReasonType":string,
   "CustomerCustID":string,
   "CustomerBTName":string,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential  */  
   "ConfidencePct":number,
      /**  Link to the Marketing Campaign related to this Quote.  */  
   "MktgCampaignID":string,
      /**  Link to the marketing event associated with this record.  */  
   "MktgEvntSeq":number,
      /**  This is an optional field used to enter the customers Purchase Order Number.  */  
   "PONum":string,
      /**  Indicates that the one or more detail line items have been ordered on this quote. Note: This can be set via 3 methods. 1 - When the task is marked as a win and order is created, 2 - Via the Order Entry Get function, 2 - Via the Order Entry Add from Quote Line function.  */  
   "Ordered":boolean,
      /**  Bill To Customer Number  */  
   "BTCustNum":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteHedRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number is an integer which is used to uniquely identify a quote within the system.  This is automatically assigned by the system when the user requests to create a new quote. To create a new quote the user either takes an "add" option or leaves the Quote Number fill-in zero. The system generates a number by finding the quote number of the last record on file and then a 1 to it. It then uses the greater of Last quote number + 1 or the EQSyst.StartQuoteNum.  */  
   "QuoteNum":number,
      /**  Contains the internal Customer number that the links the quote to the customer master. This is not directly entered by the user. Instead the CustID is entered which provides the CustNum from the customer master. The quote must reference a valid Customer master.  */  
   "CustNum":number,
      /**  Date that quote was created in the system. Not user maintainable. Set equal to the system date when record was created.  */  
   "EntryDate":string,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   "PrcConNum":number,
      /**  Contains comments about the overall Quote. These will be printed on the Quote form.  */  
   "QuoteComment":string,
      /**  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  */  
   "DueDate":string,
      /**  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  */  
   "Quoted":boolean,
      /**  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  */  
   "DateQuoted":string,
      /**   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.

This date is also used as part of the quote purging criteria testing.  */  
   "ExpirationDate":string,
      /**  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  */  
   "FollowUpDate":string,
      /**  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  */  
   "Reference":string,
      /**   Optional Quote check off # 1. The label for this field is found in EQSyst. If the label field is blank then field should be invisible.
These "check offs" could be used for selecting quotes. An example would be a "Engineering" or "Purchasing" check off.  */  
   "CheckOff1":boolean,
      /**  Optional check off # 2.  */  
   "CheckOff2":boolean,
      /**  Optional check off # 3.  */  
   "CheckOff3":boolean,
      /**  Optional check off # 4.  */  
   "CheckOff4":boolean,
      /**  Optional check off # 5.  */  
   "CheckOff5":boolean,
      /**  Indicates if the Quote has expired.  A quote is expired when QuoteHed.ExpirationDate < Today.  Each time a user logs on the system does a quick check for any unexpired quotes that have an expiration date < Today and sets them as expired. This field is also set during the QuoteHed write trigger.  */  
   "Expired":boolean,
      /**  System maintained flag - set to yes when the quote follow up alert has been sent.  */  
   "FlwAlrtSnt":boolean,
      /**  System maintained flag - set to yes when the quote due date alert has been sent.  */  
   "DueAlrtSnt":boolean,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  A = High, Z = Low  */  
   "LeadRating":string,
      /**  Link to the territory Id for this LOQ  */  
   "TerritoryID":string,
      /**  Link to Task set  */  
   "TaskSetID":string,
      /**   Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  */  
   "CurrentStage":string,
      /**  Link to the parent Quote.  This Quote is a for the same job as the parent but for a different customer.  This quotes revenues estimates won't be included in the sales managers figures.  */  
   "ParentQuoteNum":number,
      /**  The Currently active Stage changing task  */  
   "ActiveTaskID":string,
      /**  The Last Complete Milestone task  */  
   "LastTaskID":string,
      /**  The date this quote is expected to close.  */  
   "ExpectedClose":string,
      /**  Indicates the Type of reason for closing this quote.   "W" Win CRM "L" - Loss CRM, "T" Task CRM.  */  
   "ReasonType":string,
      /**  Select from list of Win or loss reason codes depending on the setting if the conclusion field  */  
   "ReasonCode":string,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential  */  
   "ConfidencePct":number,
      /**  Used to establish a discount percent value which will be used as a default during Quote line entry. It can be left as zero.  Use the CUSTOMER.DISCOUNTPERCENT field as a default. Refreshed whenever QUOTEHED.CUSTOMER field changes.  */  
   "DiscountPercent":number,
      /**  Indicates which customer ship to is to be used as the default for the Order release record created from this Quote. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new Quotes or when the QuoteHED.CUSTNUM is changed.  */  
   "ShipToNum":string,
      /**  Establishes the Shipping Contact to be used as default on the Order release record created from this Quote. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   "ShpConNum":number,
      /**  This quote is no longer updatable.  */  
   "QuoteClosed":boolean,
      /**  The date that the Quote was closed.  */  
   "ClosedDate":string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table. Use the CUSTOMER.SHIPVIA as the default when the CUSTNUM field is changed and the SHIPTO is blank. Use SHIPTO.SHIPVIA when CUSTNUM or SHIPTO fields are changed and the SHIPTO is not blank.  */  
   "ShipViaCode":string,
      /**  Link to the Marketing Campaign related to this Quote.  */  
   "MktgCampaignID":string,
      /**  Link to the marketing event associated with this record.  */  
   "MktgEvntSeq":number,
      /**  CallType code from the CallType table.  Identifies what type of communication this is. For example email, phone, visit, etc.  */  
   "CallTypeCode":string,
      /**  This is an optional field used to enter the customers Purchase Order Number.  */  
   "PONum":string,
      /**   Contains the key value of the record in the TERMS table which indicates the sales terms established for this Opportunity/Quote. On change of QutoeHED.CUSTNUM use the CUSTOMER.TERMS
field as the default.  */  
   "TermsCode":string,
      /**  Indicates that the one or more detail line items have been ordered on this quote. Note: This can be set via 3 methods. 1 - When the task is marked as a win and order is created, 2 - Via the Order Entry Get function, 2 - Via the Order Entry Add from Quote Line function.  */  
   "Ordered":boolean,
      /**  Indicates if order based discounting needs to be applied to the quote.  */  
   "ApplyOrderBasedDisc":boolean,
      /**  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  */  
   "AutoOrderBasedDisc":boolean,
      /**  The help desk case that created this quote.  */  
   "HDCaseNum":number,
      /**  Bill To Customer Number  */  
   "BTCustNum":number,
      /**  When checked the exchange rate defaults the currency's exchanged reate, but the user can change it. When not checked the exchange rate defaults the currecy's exchange rate, and the field is disabled  */  
   "LockRate":boolean,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  This flag will be used to indicate if the Quote is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the quote which could affect taxes (QuoteDtl, QuoteHed, QuoteMsc, etc). It defaults from EQSyst.QuoReadyToCalcDflt field when an order is created.  */  
   "ReadyToCalc":boolean,
      /**  This field is used to store a code that represents the external system that the Quote is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  */  
   "ExportRequested":string,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   "Rounding":number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   "DocRounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Rounding":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Total quote Amount. This field is an accumulation of the extended net amounts of the detail line items.  */  
   "QuoteAmt":number,
      /**  Total quote Amount in customer currency. This field is an accumulation of the extended net amounts of the detail line items and rounded according to the Doc currency Round rule  */  
   "DocQuoteAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1QuoteAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2QuoteAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3QuoteAmt":number,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   "UseOTS":boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   "OTSName":string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   "OTSAddress1":string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   "OTSAddress2":string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   "OTSAddress3":string,
      /**  City portion of the One Time Shipto  address.  */  
   "OTSCity":string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   "OTSState":string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   "OTSZIP":string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   "OTSResaleID":string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   "OTSTaxRegionCode":string,
      /**  One Time Ship To Contact Name  */  
   "OTSContact":string,
      /**  Fax number for the One Time ShipTo.  */  
   "OTSFaxNum":string,
      /**  Phone number for the One Time ShipTo  */  
   "OTSPhoneNum":string,
      /**  One Time Shipping Country Number  */  
   "OTSCountryNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Indicates that the tax is included in the unit price  */  
   "InPrice":boolean,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (worst case) for the quote line.  */  
   "WorstCsPct":number,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (best case) for the quote line.  */  
   "BestCsPct":number,
      /**  The demand contract this demand is for.  */  
   "DemandContractNum":number,
      /**  Demand Header sequence number to which this record is related.  */  
   "DemandHeadSeq":number,
      /**  Defines if this document is marked as EDI Ready.  */  
   "EDIReady":boolean,
      /**  Quote created from EDI interfaced module.  */  
   "EDIQuote":boolean,
      /**  Updated from EDI module this type of document is created.  */  
   "EDIAck":boolean,
      /**  Incremented whenever an outbound quote document is generated from the quote i.e. Response to Request For Quotes, etc.  */  
   "OutboundQuoteDocCtr":number,
      /**  Date in which the related demand was last processed.  */  
   "DemandProcessDate":string,
      /**  System Time when demand was last processed.  */  
   "DemandProcessTime":number,
      /**  EDI Transaction Control Number  */  
   "LastTCtrlNum":string,
      /**  EDI Batch Control Number  */  
   "LastBatchNum":string,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "DocTotalSATax":number,
      /**   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "DocTotalTax":number,
      /**   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "DocTotalWHTax":number,
      /**   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "Rpt1TotalSATax":number,
      /**   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Quote Total - TotalComm  */  
   "Rpt1TotalTax":number,
      /**   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "Rpt1TotalWHTax":number,
      /**   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "Rpt2TotalSATax":number,
      /**   Total Quote Invoice TaxesQuote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "Rpt2TotalTax":number,
      /**   Total Order Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "Rpt2TotalWHTax":number,
      /**   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "Rpt3TotalSATax":number,
      /**  Declared Insurance Amount  */  
   "DeclaredAmt":number,
      /**   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "Rpt3TotalTax":number,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   "DeclaredIns":boolean,
      /**   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "Rpt3TotalWHTax":number,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   "DeliveryConf":number,
      /**  Tax Point  */  
   "TaxPoint":string,
      /**  Service Home Delivery Type Code  */  
   "DeliveryType":string,
      /**  Date Used to calculate Tax Rates  */  
   "TaxRateDate":string,
      /**  Documents Only delivery  */  
   "DocOnly":boolean,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   "TaxRegionCode":string,
      /**  Freight charges will not be returned if 'yes'  */  
   "DropShip":boolean,
      /**   Quote Total Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "TotalSATax":number,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
      /**   Quote Total Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "TotalTax":number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   "GroundType":string,
      /**   Quote Total Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   "TotalWHTax":number,
      /**  Hazmat or Dangerous Goods delivery  */  
   "Hazmat":boolean,
      /**  Inter-Company Purchase order number that uniquely identifies the purchase order.  */  
   "ICPONum":number,
      /**  Indicates if this quote header is linked to an inter-company PO header.  */  
   "Linked":boolean,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the quote quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   "LockQty":boolean,
      /**  Date customer needs the items on the order to arrive. This is used only as the default value for the NeedByDate when creating quote detail line items. This can be left blank.  */  
   "NeedByDate":string,
      /**  The list of email address to notify about a delivery  */  
   "NotifyEMail":string,
      /**  Indicates whether to send an email notification of delivery  */  
   "NotifyFlag":boolean,
      /**  True if Customer or ShipTo record was created using the  OTS info.  */  
   "OTSCustSaved":boolean,
      /**  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  */  
   "OTSSaveAs":string,
      /**  CustID to be used if the OTS is used to create a customer record.  */  
   "OTSSaveCustID":string,
      /**  Override Carrier Defaults.  If not checked then the Site values will be used  */  
   "OverrideCarrier":boolean,
      /**  Override Service Options.  If not checked then the Site values will be used  */  
   "OverrideService":boolean,
      /**  Reference Notes for the delivery  */  
   "RefNotes":string,
      /**  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for QuoteDtl.RequestDate.  */  
   "RequestDate":string,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
      /**  Service Signature Release authorization number  */  
   "ServAuthNum":string,
      /**  Service Home Delivery date  */  
   "ServDeliveryDate":string,
      /**  Service Home Delivery allowed  */  
   "ServHomeDel":boolean,
      /**  Service Delivery Instructions  */  
   "ServInstruct":string,
      /**  Home delivery phone number  */  
   "ServPhone":string,
      /**  Service Reference 1  */  
   "ServRef1":string,
      /**  Service Reference 2  */  
   "ServRef2":string,
      /**  Service Reference 3  */  
   "ServRef3":string,
      /**  Service Reference 4  */  
   "ServRef4":string,
      /**  Service Reference 5  */  
   "ServRef5":string,
      /**  Service Signature release is on file  */  
   "ServRelease":boolean,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Indicates that the Quote item was closed before any shipments were made against it.  */  
   "VoidQuote":boolean,
      /**  Apply Handling Charge to shipment  */  
   "ApplyChrg":boolean,
      /**  Handling Charge Amount  */  
   "ChrgAmount":number,
      /**  Prefer COD delivery  */  
   "COD":boolean,
      /**  Total discount percent.  */  
   "TotalDiscPct":number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   "TotalExpected":number,
   "TotalGrossValue":number,
   "TotalMiscAmt":number,
   "TotalPotential":number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   "TotalWorstCs":number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   "DocTotalBestCs":number,
   "DocTotalDiscount":number,
      /**  Total discount percent.  */  
   "DocTotalDiscPct":number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   "DocTotalExpected":number,
   "DocTotalGrossValue":number,
   "DocTotalMiscAmt":number,
   "DocTotalPotential":number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   "DocTotalWorstCs":number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   "Rpt1TotalBestCs":number,
   "Rpt1TotalDiscount":number,
      /**  Total discount percent.  */  
   "Rpt1TotalDiscPct":number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   "Rpt1TotalExpected":number,
   "Rpt1TotalGrossValue":number,
   "Rpt1TotalMiscAmt":number,
   "Rpt1TotalPotential":number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   "Rpt1TotalWorstCs":number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   "Rpt2TotalBestCs":number,
   "Rpt2TotalDiscount":number,
      /**  Total discount percent.  */  
   "Rpt2TotalDiscPct":number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   "Rpt2TotalExpected":number,
   "Rpt2TotalGrossValue":number,
   "Rpt2TotalMiscAmt":number,
   "Rpt2TotalPotential":number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   "Rpt2TotalWorstCs":number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   "Rpt3TotalBestCs":number,
   "Rpt3TotalDiscount":number,
      /**  Total discount percent.  */  
   "Rpt3TotalDiscPct":number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   "Rpt3TotalExpected":number,
   "Rpt3TotalGrossValue":number,
   "Rpt3TotalMiscAmt":number,
   "Rpt3TotalPotential":number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   "Rpt3TotalWorstCs":number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   "TotalBestCs":number,
   "TotalDiscount":number,
      /**  Amount due on Cashier's check or money order  */  
   "CODAmount":number,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   "CODCheck":boolean,
      /**  Add Freight COD Amount owed  */  
   "CODFreight":boolean,
      /**  LOQPrepressText  */  
   "LOQPrepressText":string,
      /**  LOQNewPageOnQuoteLine  */  
   "LOQNewPageOnQuoteLine":boolean,
      /**  LOQBookPCFinishing  */  
   "LOQBookPCFinishing":boolean,
      /**  LOQBookPCPaper  */  
   "LOQBookPCPaper":boolean,
      /**  LOQBookPCPress  */  
   "LOQBookPCPress":boolean,
      /**  LOQBookPCPlates  */  
   "LOQBookPCPlates":boolean,
      /**  LOQVariations  */  
   "LOQVariations":boolean,
      /**  AEPLOQType  */  
   "AEPLOQType":string,
      /**  LOQPrepressStyle  */  
   "LOQPrepressStyle":string,
      /**  QuoteCSR  */  
   "QuoteCSR":string,
      /**  DueHour  */  
   "DueHour":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Quote was confirmed/rejected by ECC Web  */  
   "ECCConfirmed":boolean,
      /**  Quote was confirmed/rejected by this ECC user  */  
   "ECCConfirmedBy":string,
      /**  ECC quote message: RFQ or GQR  */  
   "ECCMsgType":string,
      /**  Quote is ready to be approved by user via ECC web site.  */  
   "ECCWebReady":boolean,
      /**  ECC Quote Number  */  
   "ECCQuoteNum":string,
      /**  ECC Comment Reference Number  */  
   "ECCCmmtRef":string,
      /**  ECCComment  */  
   "ECCComment":string,
      /**  ECC Quote Status  */  
   "ECCStatus":string,
      /**  ECC Expiration Date  */  
   "ECCExpirationDate":string,
      /**  ECCCmmtRefSK  */  
   "ECCCmmtRefSK":string,
      /**  This field defines if the Quote  is synchronized to an External CRM.  */  
   "ExternalCRMQuote":boolean,
      /**  This field holds the  id of this quote in the External CRM  */  
   "ExternalCRMQuoteID":string,
      /**  This field holds the sales order created in the External CRM. This id might not match an Epicor ERP Order id.  */  
   "ExternalCRMOrderID":string,
      /**  Web Sales Rep ID  */  
   "ECCSalesRepID":string,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   "Tax":number,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   "DocTax":number,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   "Rpt1Tax":number,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   "Rpt2Tax":number,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   "Rpt3Tax":number,
      /**  HdrTaxNoUpdt  */  
   "HdrTaxNoUpdt":boolean,
      /**  This field defines the last time that the Quote has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  */  
   "ExternalCRMLastSync":string,
      /**  This fields determines if the quotes needs to be synchronized to the External CRM. If there are changes in the quote or quote detail file, Epicor ERP automatically turns on this field.  */  
   "ExternalCRMSyncRequired":boolean,
      /**  Total of claims credit lines  */  
   "TotalClaimsCredit":number,
      /**  Total of claims credit lines in customer currency  */  
   "DocTotalClaimsCredit":number,
      /**  Total of claims credit lines in report currency  */  
   "Rpt1TotalClaimsCredit":number,
      /**  Total of claims credit lines in report currency  */  
   "Rpt2TotalClaimsCredit":number,
      /**  Total of claims credit lines in report currency  */  
   "Rpt3TotalClaimsCredit":number,
      /**  Total Quote claims credit Invoice Taxes.  */  
   "TotalClaimsTax":number,
      /**  Total Quote claims credit Invoice Taxes in customer currency.  */  
   "DocTotalClaimsTax":number,
      /**  Total Quote claims credit Invoice Taxes in report currency.  */  
   "Rpt1TotalClaimsTax":number,
      /**  Total Quote claims credit Invoice Taxes in report currency.  */  
   "Rpt2TotalClaimsTax":number,
      /**  Total Quote claims credit Invoice Taxes in report currency.  */  
   "Rpt3TotalClaimsTax":number,
      /**  Total Quote claims credit Self Assessed Taxes.  */  
   "TotalClaimsSATax":number,
      /**  Total Quote claims credit Self Assessed Taxes in customer currency.  */  
   "DocTotalClaimsSATax":number,
      /**  Total Quote claims credit Self Assessed Taxes in customer currency.  */  
   "Rpt1TotalClaimsSATax":number,
      /**  Total Quote claims credit Self Assessed Taxes in customer currency.  */  
   "Rpt2TotalClaimsSATax":number,
      /**  Total Quote claims credit Self Assessed Taxes in customer currency.  */  
   "Rpt3TotalClaimsSATax":number,
      /**  Total Quote claims credit Withholding Taxes.  */  
   "TotalClaimsWHTax":number,
      /**  Total Quote claims credit Withholding Taxes in customer currency.  */  
   "DocTotalClaimsWHTax":number,
      /**  Total Quote claims credit Withholding Taxes in report currency.  */  
   "Rpt1TotalClaimsWHTax":number,
      /**  Total Quote claims credit Withholding Taxes in report currency.  */  
   "Rpt2TotalClaimsWHTax":number,
      /**  Total Quote claims credit Withholding Taxes in report currency.  */  
   "Rpt3TotalClaimsWHTax":number,
      /**  OTSTaxValidationStatus  */  
   "OTSTaxValidationStatus":number,
      /**  OTSTaxValidationDate  */  
   "OTSTaxValidationDate":string,
      /**  FSMSendTo  */  
   "FSMSendTo":boolean,
      /**  Incoterm Code  */  
   "IncotermCode":string,
      /**  Incoterm Location  */  
   "IncotermLocation":string,
   "AddrList":string,
   "BaseCurrencyID":string,
      /**  Bill To Customer Name.  */  
   "BTCustomerName":string,
      /**  Audit Log change description  */  
   "ChangeDescription":string,
   "CheckOffLabel1":string,
   "CheckOffLabel2":string,
   "CheckOffLabel3":string,
   "CheckOffLabel4":string,
   "CheckOffLabel5":string,
   "Conclusion":string,
      /**  Primary Contact Name  */  
   "ConName":string,
   "CurrencySwitch":boolean,
      /**  Full Description of the CurrentStage field  */  
   "CurrentStageDesc":string,
      /**  Value of the Customer.AllowOTS (customer allows one time shipment)  */  
   "CustAllowOTS":boolean,
   "CustOnCreditHold":boolean,
      /**  Number of days Quote has been open  */  
   "DaysOpen":number,
      /**   Display the true discount percent of the quote. It's calculated by dividing the sum Discount Percent over Gross Value.
DiscountPercentCalc = (DocTotalDiscount / TotalGrossValue) *100  */  
   "DiscountPercentCalc":number,
      /**  Total tax in Doc currency. The sum of all the tax details for the quote.  */  
   "DocTaxAmt":number,
      /**   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  */  
   "DocTotalQuote":number,
      /**  Used for screen display. If SoldTo and Alt-Bill to are the same, this displays as null.  */  
   "dspBTCustID":string,
   "EmailAddress":string,
      /**  Indicates if it's okay to enable OrderBased Pricing  */  
   "EnableOrderBasedDisc":boolean,
      /**   The expected revenue potential percentage of all lines.
ExpectedCsPct = (TotalExpected / TotalPotential) * 100  */  
   "ExpectedCsPct":number,
   "FaxNum":string,
   "FOB":string,
   "FOBDescription":string,
      /**  Used by IU to disabled Currency Code  */  
   "HasQuoteLines":boolean,
      /**  EqSyst.LogChanges  */  
   "LogChanges":boolean,
      /**  Order Date  */  
   "OrderDate":string,
   "OrderDiscount":number,
   "OrderPONum":string,
   "OrderShipVia":string,
   "OrderTerms":string,
   "OTSSaved":boolean,
   "OTSShipToNum":string,
   "PhoneNum":string,
   "PreventQQChange":boolean,
      /**  Label for ExchangeRate  */  
   "RateLabel":string,
   "Rpt1TaxAmt":number,
      /**   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  */  
   "Rpt1TotalQuote":number,
   "Rpt2TaxAmt":number,
      /**   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  */  
   "Rpt2TotalQuote":number,
   "Rpt3TaxAmt":number,
      /**   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  */  
   "Rpt3TotalQuote":number,
   "SalesRepCode":string,
   "SalesRepName":string,
   "ShipByDate":string,
   "ShipToAddrList":string,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   "TaxAmt":number,
      /**   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  */  
   "TotalQuote":number,
      /**   Displays the calculated revenue potential percentage (worst case) for the quote line.
WorseCsPctCalc = (TotalWorstCs / TotalPotential) * 100  */  
   "WorseCsPctCalc":number,
      /**  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  */  
   "AvailBTCustList":string,
      /**  Currency.CurrSymbol for currency "BASE"  */  
   "BaseCurrSymbol":string,
      /**   Displays the calculated revenue potential percentage (best case) for the quote line.
BestCsPctCalc = (TotalBestCs / TotalPotential) * 100  */  
   "BestCsPctCalc":number,
      /**  Bill To Address List.  */  
   "BTAddressList":string,
      /**  Customer ID of the bill to customer.  */  
   "BTCustID":string,
      /**  Indicates if the order contains any credit type line  */  
   "HasCreditLines":boolean,
      /**  Returns true if Customer.ECCType is B2C OR Dealer OR Distributor AND Customer.WebCustomer  */  
   "IsValidECC":boolean,
      /**  Flag indicating whether to enable CaseNum or not  */  
   "EnableHDCaseNum":boolean,
      /**  Indicates if the quote can be updated  */  
   "UpdateAllowed":boolean,
      /**  Formatted address  */  
   "AddressFormatted":string,
      /**  Ship To Address formatted  */  
   "ShipToAddressFormatted":string,
      /**  Indicates if tax region is one of the field changes the user is asked about for propogating changes to lines  */  
   "PromptTaxRegionCode":boolean,
      /**  Indicates a customer referenced on the quote is inactive.  */  
   "InactiveCustomer":boolean,
      /**  Update primary contact on save of the quote header  */  
   "UpdatePrimContact":boolean,
      /**  Flag indicating whether to enable Incoterm Location  */  
   "EnableIncotermLocation":boolean,
   "BitFlag":number,
   "ActiveTaskTaskDescription":string,
   "CurrencyDocumentDesc":string,
   "CurrencyCurrencyID":string,
   "CurrencyCurrName":string,
   "CurrencyCurrDesc":string,
   "CurrencyCurrSymbol":string,
   "CurrencyBaseCurr":boolean,
   "CustomerAllowShipTo3":boolean,
   "CustomerBTName":string,
   "CustomerCustID":string,
   "CustomerName":string,
   "CustomerCheckDuplicatePO":boolean,
   "HDCaseDescription":string,
   "IncotermsDescription":string,
   "LastTaskTaskDescription":string,
   "MktgCpgnCampDescription":string,
   "MktgEventEvntDescription":string,
   "OTSCountryNumISOCode":string,
   "OTSCountryNumDescription":string,
   "OTSCountryNumEUMember":boolean,
   "OTSTaxRegionCodeDescription":string,
   "RateGrpDescription":string,
   "ReasonDescription":string,
   "ResponseCallTypeDesc":string,
   "ShipToBTName":string,
   "ShipToCustID":string,
   "ShipToName":string,
   "ShipToNumName":string,
   "ShipToNumInactive":boolean,
   "ShipViaWebDesc":string,
   "ShipViaDescription":string,
   "ShipViaInactive":boolean,
   "TaskSetTaskSetDescription":string,
   "TaskSetWorkflowType":string,
   "TaxRegionTaxConnectCalc":boolean,
   "TaxRegionDescription":string,
   "TermsDescription":string,
   "TerritoryTerritoryDesc":string,
   "XbSystCalcQuoteTax":boolean,
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
      @param quoteNum
   */  
export interface DeleteByID_input{
   quoteNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_QuoteHedListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number is an integer which is used to uniquely identify a quote within the system.  This is automatically assigned by the system when the user requests to create a new quote. To create a new quote the user either takes an "add" option or leaves the Quote Number fill-in zero. The system generates a number by finding the quote number of the last record on file and then a 1 to it. It then uses the greater of Last quote number + 1 or the EQSyst.StartQuoteNum.  */  
   QuoteNum:number,
      /**  Contains the internal Customer number that the links the quote to the customer master. This is not directly entered by the user. Instead the CustID is entered which provides the CustNum from the customer master. The quote must reference a valid Customer master.  */  
   CustNum:number,
      /**  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  */  
   DueDate:string,
      /**  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  */  
   Quoted:boolean,
      /**  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  */  
   DateQuoted:string,
      /**   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.

This date is also used as part of the quote purging criteria testing.  */  
   ExpirationDate:string,
      /**  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  */  
   FollowUpDate:string,
      /**  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  */  
   Reference:string,
      /**  Indicates if the Quote has expired.  A quote is expired when QuoteHed.ExpirationDate < Today.  Each time a user logs on the system does a quick check for any unexpired quotes that have an expiration date < Today and sets them as expired. This field is also set during the QuoteHed write trigger.  */  
   Expired:boolean,
      /**  Full Description for CurrentStage field  */  
   CurrentStageDesc:string,
      /**  Link to the territory Id for this LOQ  */  
   TerritoryID:string,
      /**  Link to Task set  */  
   TaskSetID:string,
      /**   Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  */  
   CurrentStage:string,
      /**  Bill to customer id.  */  
   BTCustID:string,
      /**  The Currently active Stage changing task  */  
   ActiveTaskID:string,
      /**  Bill to customer name.  */  
   BTCustomerName:string,
      /**  The Last Complete Milestone task  */  
   LastTaskID:string,
   CustomerName:string,
   TerritoryTerritoryDesc:string,
      /**  Indicates the Type of reason for closing this quote.   "W" Win CRM "L" - Loss CRM, "T" Task CRM.  */  
   ReasonType:string,
   CustomerCustID:string,
   CustomerBTName:string,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential  */  
   ConfidencePct:number,
      /**  Link to the Marketing Campaign related to this Quote.  */  
   MktgCampaignID:string,
      /**  Link to the marketing event associated with this record.  */  
   MktgEvntSeq:number,
      /**  This is an optional field used to enter the customers Purchase Order Number.  */  
   PONum:string,
      /**  Indicates that the one or more detail line items have been ordered on this quote. Note: This can be set via 3 methods. 1 - When the task is marked as a win and order is created, 2 - Via the Order Entry Get function, 2 - Via the Order Entry Add from Quote Line function.  */  
   Ordered:boolean,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteHedListTableset{
   QuoteHedList:Erp_Tablesets_QuoteHedListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_QuoteHedRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number is an integer which is used to uniquely identify a quote within the system.  This is automatically assigned by the system when the user requests to create a new quote. To create a new quote the user either takes an "add" option or leaves the Quote Number fill-in zero. The system generates a number by finding the quote number of the last record on file and then a 1 to it. It then uses the greater of Last quote number + 1 or the EQSyst.StartQuoteNum.  */  
   QuoteNum:number,
      /**  Contains the internal Customer number that the links the quote to the customer master. This is not directly entered by the user. Instead the CustID is entered which provides the CustNum from the customer master. The quote must reference a valid Customer master.  */  
   CustNum:number,
      /**  Date that quote was created in the system. Not user maintainable. Set equal to the system date when record was created.  */  
   EntryDate:string,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   PrcConNum:number,
      /**  Contains comments about the overall Quote. These will be printed on the Quote form.  */  
   QuoteComment:string,
      /**  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  */  
   DueDate:string,
      /**  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  */  
   Quoted:boolean,
      /**  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  */  
   DateQuoted:string,
      /**   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.

This date is also used as part of the quote purging criteria testing.  */  
   ExpirationDate:string,
      /**  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  */  
   FollowUpDate:string,
      /**  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  */  
   Reference:string,
      /**   Optional Quote check off # 1. The label for this field is found in EQSyst. If the label field is blank then field should be invisible.
These "check offs" could be used for selecting quotes. An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff1:boolean,
      /**  Optional check off # 2.  */  
   CheckOff2:boolean,
      /**  Optional check off # 3.  */  
   CheckOff3:boolean,
      /**  Optional check off # 4.  */  
   CheckOff4:boolean,
      /**  Optional check off # 5.  */  
   CheckOff5:boolean,
      /**  Indicates if the Quote has expired.  A quote is expired when QuoteHed.ExpirationDate < Today.  Each time a user logs on the system does a quick check for any unexpired quotes that have an expiration date < Today and sets them as expired. This field is also set during the QuoteHed write trigger.  */  
   Expired:boolean,
      /**  System maintained flag - set to yes when the quote follow up alert has been sent.  */  
   FlwAlrtSnt:boolean,
      /**  System maintained flag - set to yes when the quote due date alert has been sent.  */  
   DueAlrtSnt:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  A = High, Z = Low  */  
   LeadRating:string,
      /**  Link to the territory Id for this LOQ  */  
   TerritoryID:string,
      /**  Link to Task set  */  
   TaskSetID:string,
      /**   Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  */  
   CurrentStage:string,
      /**  Link to the parent Quote.  This Quote is a for the same job as the parent but for a different customer.  This quotes revenues estimates won't be included in the sales managers figures.  */  
   ParentQuoteNum:number,
      /**  The Currently active Stage changing task  */  
   ActiveTaskID:string,
      /**  The Last Complete Milestone task  */  
   LastTaskID:string,
      /**  The date this quote is expected to close.  */  
   ExpectedClose:string,
      /**  Indicates the Type of reason for closing this quote.   "W" Win CRM "L" - Loss CRM, "T" Task CRM.  */  
   ReasonType:string,
      /**  Select from list of Win or loss reason codes depending on the setting if the conclusion field  */  
   ReasonCode:string,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential  */  
   ConfidencePct:number,
      /**  Used to establish a discount percent value which will be used as a default during Quote line entry. It can be left as zero.  Use the CUSTOMER.DISCOUNTPERCENT field as a default. Refreshed whenever QUOTEHED.CUSTOMER field changes.  */  
   DiscountPercent:number,
      /**  Indicates which customer ship to is to be used as the default for the Order release record created from this Quote. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new Quotes or when the QuoteHED.CUSTNUM is changed.  */  
   ShipToNum:string,
      /**  Establishes the Shipping Contact to be used as default on the Order release record created from this Quote. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   ShpConNum:number,
      /**  This quote is no longer updatable.  */  
   QuoteClosed:boolean,
      /**  The date that the Quote was closed.  */  
   ClosedDate:string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table. Use the CUSTOMER.SHIPVIA as the default when the CUSTNUM field is changed and the SHIPTO is blank. Use SHIPTO.SHIPVIA when CUSTNUM or SHIPTO fields are changed and the SHIPTO is not blank.  */  
   ShipViaCode:string,
      /**  Link to the Marketing Campaign related to this Quote.  */  
   MktgCampaignID:string,
      /**  Link to the marketing event associated with this record.  */  
   MktgEvntSeq:number,
      /**  CallType code from the CallType table.  Identifies what type of communication this is. For example email, phone, visit, etc.  */  
   CallTypeCode:string,
      /**  This is an optional field used to enter the customers Purchase Order Number.  */  
   PONum:string,
      /**   Contains the key value of the record in the TERMS table which indicates the sales terms established for this Opportunity/Quote. On change of QutoeHED.CUSTNUM use the CUSTOMER.TERMS
field as the default.  */  
   TermsCode:string,
      /**  Indicates that the one or more detail line items have been ordered on this quote. Note: This can be set via 3 methods. 1 - When the task is marked as a win and order is created, 2 - Via the Order Entry Get function, 2 - Via the Order Entry Add from Quote Line function.  */  
   Ordered:boolean,
      /**  Indicates if order based discounting needs to be applied to the quote.  */  
   ApplyOrderBasedDisc:boolean,
      /**  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  */  
   AutoOrderBasedDisc:boolean,
      /**  The help desk case that created this quote.  */  
   HDCaseNum:number,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**  When checked the exchange rate defaults the currency's exchanged reate, but the user can change it. When not checked the exchange rate defaults the currecy's exchange rate, and the field is disabled  */  
   LockRate:boolean,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  This flag will be used to indicate if the Quote is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the quote which could affect taxes (QuoteDtl, QuoteHed, QuoteMsc, etc). It defaults from EQSyst.QuoReadyToCalcDflt field when an order is created.  */  
   ReadyToCalc:boolean,
      /**  This field is used to store a code that represents the external system that the Quote is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  */  
   ExportRequested:string,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   Rounding:number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   DocRounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt2Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt3Rounding:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Total quote Amount. This field is an accumulation of the extended net amounts of the detail line items.  */  
   QuoteAmt:number,
      /**  Total quote Amount in customer currency. This field is an accumulation of the extended net amounts of the detail line items and rounded according to the Doc currency Round rule  */  
   DocQuoteAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1QuoteAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2QuoteAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3QuoteAmt:number,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   UseOTS:boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portion of the One Time Shipto  address.  */  
   OTSCity:string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   OTSZIP:string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   OTSResaleID:string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   OTSTaxRegionCode:string,
      /**  One Time Ship To Contact Name  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipping Country Number  */  
   OTSCountryNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Indicates that the tax is included in the unit price  */  
   InPrice:boolean,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (worst case) for the quote line.  */  
   WorstCsPct:number,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (best case) for the quote line.  */  
   BestCsPct:number,
      /**  The demand contract this demand is for.  */  
   DemandContractNum:number,
      /**  Demand Header sequence number to which this record is related.  */  
   DemandHeadSeq:number,
      /**  Defines if this document is marked as EDI Ready.  */  
   EDIReady:boolean,
      /**  Quote created from EDI interfaced module.  */  
   EDIQuote:boolean,
      /**  Updated from EDI module this type of document is created.  */  
   EDIAck:boolean,
      /**  Incremented whenever an outbound quote document is generated from the quote i.e. Response to Request For Quotes, etc.  */  
   OutboundQuoteDocCtr:number,
      /**  Date in which the related demand was last processed.  */  
   DemandProcessDate:string,
      /**  System Time when demand was last processed.  */  
   DemandProcessTime:number,
      /**  EDI Transaction Control Number  */  
   LastTCtrlNum:string,
      /**  EDI Batch Control Number  */  
   LastBatchNum:string,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   DocTotalSATax:number,
      /**   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   DocTotalTax:number,
      /**   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   DocTotalWHTax:number,
      /**   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt1TotalSATax:number,
      /**   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt1TotalTax:number,
      /**   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt1TotalWHTax:number,
      /**   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt2TotalSATax:number,
      /**   Total Quote Invoice TaxesQuote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt2TotalTax:number,
      /**   Total Order Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt2TotalWHTax:number,
      /**   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt3TotalSATax:number,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt3TotalTax:number,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt3TotalWHTax:number,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   DeliveryConf:number,
      /**  Tax Point  */  
   TaxPoint:string,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Date Used to calculate Tax Rates  */  
   TaxRateDate:string,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**  Freight charges will not be returned if 'yes'  */  
   DropShip:boolean,
      /**   Quote Total Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   TotalSATax:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**   Quote Total Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   TotalTax:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**   Quote Total Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   TotalWHTax:number,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Inter-Company Purchase order number that uniquely identifies the purchase order.  */  
   ICPONum:number,
      /**  Indicates if this quote header is linked to an inter-company PO header.  */  
   Linked:boolean,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the quote quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   LockQty:boolean,
      /**  Date customer needs the items on the order to arrive. This is used only as the default value for the NeedByDate when creating quote detail line items. This can be left blank.  */  
   NeedByDate:string,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  True if Customer or ShipTo record was created using the  OTS info.  */  
   OTSCustSaved:boolean,
      /**  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  */  
   OTSSaveAs:string,
      /**  CustID to be used if the OTS is used to create a customer record.  */  
   OTSSaveCustID:string,
      /**  Override Carrier Defaults.  If not checked then the Site values will be used  */  
   OverrideCarrier:boolean,
      /**  Override Service Options.  If not checked then the Site values will be used  */  
   OverrideService:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for QuoteDtl.RequestDate.  */  
   RequestDate:string,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Indicates that the Quote item was closed before any shipments were made against it.  */  
   VoidQuote:boolean,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Total discount percent.  */  
   TotalDiscPct:number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   TotalExpected:number,
   TotalGrossValue:number,
   TotalMiscAmt:number,
   TotalPotential:number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   TotalWorstCs:number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   DocTotalBestCs:number,
   DocTotalDiscount:number,
      /**  Total discount percent.  */  
   DocTotalDiscPct:number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   DocTotalExpected:number,
   DocTotalGrossValue:number,
   DocTotalMiscAmt:number,
   DocTotalPotential:number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   DocTotalWorstCs:number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   Rpt1TotalBestCs:number,
   Rpt1TotalDiscount:number,
      /**  Total discount percent.  */  
   Rpt1TotalDiscPct:number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   Rpt1TotalExpected:number,
   Rpt1TotalGrossValue:number,
   Rpt1TotalMiscAmt:number,
   Rpt1TotalPotential:number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   Rpt1TotalWorstCs:number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   Rpt2TotalBestCs:number,
   Rpt2TotalDiscount:number,
      /**  Total discount percent.  */  
   Rpt2TotalDiscPct:number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   Rpt2TotalExpected:number,
   Rpt2TotalGrossValue:number,
   Rpt2TotalMiscAmt:number,
   Rpt2TotalPotential:number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   Rpt2TotalWorstCs:number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   Rpt3TotalBestCs:number,
   Rpt3TotalDiscount:number,
      /**  Total discount percent.  */  
   Rpt3TotalDiscPct:number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   Rpt3TotalExpected:number,
   Rpt3TotalGrossValue:number,
   Rpt3TotalMiscAmt:number,
   Rpt3TotalPotential:number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   Rpt3TotalWorstCs:number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   TotalBestCs:number,
   TotalDiscount:number,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  LOQPrepressText  */  
   LOQPrepressText:string,
      /**  LOQNewPageOnQuoteLine  */  
   LOQNewPageOnQuoteLine:boolean,
      /**  LOQBookPCFinishing  */  
   LOQBookPCFinishing:boolean,
      /**  LOQBookPCPaper  */  
   LOQBookPCPaper:boolean,
      /**  LOQBookPCPress  */  
   LOQBookPCPress:boolean,
      /**  LOQBookPCPlates  */  
   LOQBookPCPlates:boolean,
      /**  LOQVariations  */  
   LOQVariations:boolean,
      /**  AEPLOQType  */  
   AEPLOQType:string,
      /**  LOQPrepressStyle  */  
   LOQPrepressStyle:string,
      /**  QuoteCSR  */  
   QuoteCSR:string,
      /**  DueHour  */  
   DueHour:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Quote was confirmed/rejected by ECC Web  */  
   ECCConfirmed:boolean,
      /**  Quote was confirmed/rejected by this ECC user  */  
   ECCConfirmedBy:string,
      /**  ECC quote message: RFQ or GQR  */  
   ECCMsgType:string,
      /**  Quote is ready to be approved by user via ECC web site.  */  
   ECCWebReady:boolean,
      /**  ECC Quote Number  */  
   ECCQuoteNum:string,
      /**  ECC Comment Reference Number  */  
   ECCCmmtRef:string,
      /**  ECCComment  */  
   ECCComment:string,
      /**  ECC Quote Status  */  
   ECCStatus:string,
      /**  ECC Expiration Date  */  
   ECCExpirationDate:string,
      /**  ECCCmmtRefSK  */  
   ECCCmmtRefSK:string,
      /**  This field defines if the Quote  is synchronized to an External CRM.  */  
   ExternalCRMQuote:boolean,
      /**  This field holds the  id of this quote in the External CRM  */  
   ExternalCRMQuoteID:string,
      /**  This field holds the sales order created in the External CRM. This id might not match an Epicor ERP Order id.  */  
   ExternalCRMOrderID:string,
      /**  Web Sales Rep ID  */  
   ECCSalesRepID:string,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   Tax:number,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   DocTax:number,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   Rpt1Tax:number,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   Rpt2Tax:number,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   Rpt3Tax:number,
      /**  HdrTaxNoUpdt  */  
   HdrTaxNoUpdt:boolean,
      /**  This field defines the last time that the Quote has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  */  
   ExternalCRMLastSync:string,
      /**  This fields determines if the quotes needs to be synchronized to the External CRM. If there are changes in the quote or quote detail file, Epicor ERP automatically turns on this field.  */  
   ExternalCRMSyncRequired:boolean,
      /**  Total of claims credit lines  */  
   TotalClaimsCredit:number,
      /**  Total of claims credit lines in customer currency  */  
   DocTotalClaimsCredit:number,
      /**  Total of claims credit lines in report currency  */  
   Rpt1TotalClaimsCredit:number,
      /**  Total of claims credit lines in report currency  */  
   Rpt2TotalClaimsCredit:number,
      /**  Total of claims credit lines in report currency  */  
   Rpt3TotalClaimsCredit:number,
      /**  Total Quote claims credit Invoice Taxes.  */  
   TotalClaimsTax:number,
      /**  Total Quote claims credit Invoice Taxes in customer currency.  */  
   DocTotalClaimsTax:number,
      /**  Total Quote claims credit Invoice Taxes in report currency.  */  
   Rpt1TotalClaimsTax:number,
      /**  Total Quote claims credit Invoice Taxes in report currency.  */  
   Rpt2TotalClaimsTax:number,
      /**  Total Quote claims credit Invoice Taxes in report currency.  */  
   Rpt3TotalClaimsTax:number,
      /**  Total Quote claims credit Self Assessed Taxes.  */  
   TotalClaimsSATax:number,
      /**  Total Quote claims credit Self Assessed Taxes in customer currency.  */  
   DocTotalClaimsSATax:number,
      /**  Total Quote claims credit Self Assessed Taxes in customer currency.  */  
   Rpt1TotalClaimsSATax:number,
      /**  Total Quote claims credit Self Assessed Taxes in customer currency.  */  
   Rpt2TotalClaimsSATax:number,
      /**  Total Quote claims credit Self Assessed Taxes in customer currency.  */  
   Rpt3TotalClaimsSATax:number,
      /**  Total Quote claims credit Withholding Taxes.  */  
   TotalClaimsWHTax:number,
      /**  Total Quote claims credit Withholding Taxes in customer currency.  */  
   DocTotalClaimsWHTax:number,
      /**  Total Quote claims credit Withholding Taxes in report currency.  */  
   Rpt1TotalClaimsWHTax:number,
      /**  Total Quote claims credit Withholding Taxes in report currency.  */  
   Rpt2TotalClaimsWHTax:number,
      /**  Total Quote claims credit Withholding Taxes in report currency.  */  
   Rpt3TotalClaimsWHTax:number,
      /**  OTSTaxValidationStatus  */  
   OTSTaxValidationStatus:number,
      /**  OTSTaxValidationDate  */  
   OTSTaxValidationDate:string,
      /**  FSMSendTo  */  
   FSMSendTo:boolean,
      /**  Incoterm Code  */  
   IncotermCode:string,
      /**  Incoterm Location  */  
   IncotermLocation:string,
   AddrList:string,
   BaseCurrencyID:string,
      /**  Bill To Customer Name.  */  
   BTCustomerName:string,
      /**  Audit Log change description  */  
   ChangeDescription:string,
   CheckOffLabel1:string,
   CheckOffLabel2:string,
   CheckOffLabel3:string,
   CheckOffLabel4:string,
   CheckOffLabel5:string,
   Conclusion:string,
      /**  Primary Contact Name  */  
   ConName:string,
   CurrencySwitch:boolean,
      /**  Full Description of the CurrentStage field  */  
   CurrentStageDesc:string,
      /**  Value of the Customer.AllowOTS (customer allows one time shipment)  */  
   CustAllowOTS:boolean,
   CustOnCreditHold:boolean,
      /**  Number of days Quote has been open  */  
   DaysOpen:number,
      /**   Display the true discount percent of the quote. It's calculated by dividing the sum Discount Percent over Gross Value.
DiscountPercentCalc = (DocTotalDiscount / TotalGrossValue) *100  */  
   DiscountPercentCalc:number,
      /**  Total tax in Doc currency. The sum of all the tax details for the quote.  */  
   DocTaxAmt:number,
      /**   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  */  
   DocTotalQuote:number,
      /**  Used for screen display. If SoldTo and Alt-Bill to are the same, this displays as null.  */  
   dspBTCustID:string,
   EmailAddress:string,
      /**  Indicates if it's okay to enable OrderBased Pricing  */  
   EnableOrderBasedDisc:boolean,
      /**   The expected revenue potential percentage of all lines.
ExpectedCsPct = (TotalExpected / TotalPotential) * 100  */  
   ExpectedCsPct:number,
   FaxNum:string,
   FOB:string,
   FOBDescription:string,
      /**  Used by IU to disabled Currency Code  */  
   HasQuoteLines:boolean,
      /**  EqSyst.LogChanges  */  
   LogChanges:boolean,
      /**  Order Date  */  
   OrderDate:string,
   OrderDiscount:number,
   OrderPONum:string,
   OrderShipVia:string,
   OrderTerms:string,
   OTSSaved:boolean,
   OTSShipToNum:string,
   PhoneNum:string,
   PreventQQChange:boolean,
      /**  Label for ExchangeRate  */  
   RateLabel:string,
   Rpt1TaxAmt:number,
      /**   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  */  
   Rpt1TotalQuote:number,
   Rpt2TaxAmt:number,
      /**   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  */  
   Rpt2TotalQuote:number,
   Rpt3TaxAmt:number,
      /**   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  */  
   Rpt3TotalQuote:number,
   SalesRepCode:string,
   SalesRepName:string,
   ShipByDate:string,
   ShipToAddrList:string,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   TaxAmt:number,
      /**   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  */  
   TotalQuote:number,
      /**   Displays the calculated revenue potential percentage (worst case) for the quote line.
WorseCsPctCalc = (TotalWorstCs / TotalPotential) * 100  */  
   WorseCsPctCalc:number,
      /**  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  */  
   AvailBTCustList:string,
      /**  Currency.CurrSymbol for currency "BASE"  */  
   BaseCurrSymbol:string,
      /**   Displays the calculated revenue potential percentage (best case) for the quote line.
BestCsPctCalc = (TotalBestCs / TotalPotential) * 100  */  
   BestCsPctCalc:number,
      /**  Bill To Address List.  */  
   BTAddressList:string,
      /**  Customer ID of the bill to customer.  */  
   BTCustID:string,
      /**  Indicates if the order contains any credit type line  */  
   HasCreditLines:boolean,
      /**  Returns true if Customer.ECCType is B2C OR Dealer OR Distributor AND Customer.WebCustomer  */  
   IsValidECC:boolean,
      /**  Flag indicating whether to enable CaseNum or not  */  
   EnableHDCaseNum:boolean,
      /**  Indicates if the quote can be updated  */  
   UpdateAllowed:boolean,
      /**  Formatted address  */  
   AddressFormatted:string,
      /**  Ship To Address formatted  */  
   ShipToAddressFormatted:string,
      /**  Indicates if tax region is one of the field changes the user is asked about for propogating changes to lines  */  
   PromptTaxRegionCode:boolean,
      /**  Indicates a customer referenced on the quote is inactive.  */  
   InactiveCustomer:boolean,
      /**  Update primary contact on save of the quote header  */  
   UpdatePrimContact:boolean,
      /**  Flag indicating whether to enable Incoterm Location  */  
   EnableIncotermLocation:boolean,
   BitFlag:number,
   ActiveTaskTaskDescription:string,
   CurrencyDocumentDesc:string,
   CurrencyCurrencyID:string,
   CurrencyCurrName:string,
   CurrencyCurrDesc:string,
   CurrencyCurrSymbol:string,
   CurrencyBaseCurr:boolean,
   CustomerAllowShipTo3:boolean,
   CustomerBTName:string,
   CustomerCustID:string,
   CustomerName:string,
   CustomerCheckDuplicatePO:boolean,
   HDCaseDescription:string,
   IncotermsDescription:string,
   LastTaskTaskDescription:string,
   MktgCpgnCampDescription:string,
   MktgEventEvntDescription:string,
   OTSCountryNumISOCode:string,
   OTSCountryNumDescription:string,
   OTSCountryNumEUMember:boolean,
   OTSTaxRegionCodeDescription:string,
   RateGrpDescription:string,
   ReasonDescription:string,
   ResponseCallTypeDesc:string,
   ShipToBTName:string,
   ShipToCustID:string,
   ShipToName:string,
   ShipToNumName:string,
   ShipToNumInactive:boolean,
   ShipViaWebDesc:string,
   ShipViaDescription:string,
   ShipViaInactive:boolean,
   TaskSetTaskSetDescription:string,
   TaskSetWorkflowType:string,
   TaxRegionTaxConnectCalc:boolean,
   TaxRegionDescription:string,
   TermsDescription:string,
   TerritoryTerritoryDesc:string,
   XbSystCalcQuoteTax:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RFQEntryQuoteSearchTableset{
   QuoteHed:Erp_Tablesets_QuoteHedRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtRFQEntryQuoteSearchTableset{
   QuoteHed:Erp_Tablesets_QuoteHedRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param quoteNum
   */  
export interface GetByID_input{
   quoteNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_RFQEntryQuoteSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_RFQEntryQuoteSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_RFQEntryQuoteSearchTableset[],
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
   returnObj:Erp_Tablesets_QuoteHedListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewQuoteHed_input{
   ds:Erp_Tablesets_RFQEntryQuoteSearchTableset[],
}

export interface GetNewQuoteHed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryQuoteSearchTableset,
}
}

   /** Required : 
      @param whereClauseQuoteHed
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseQuoteHed:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_RFQEntryQuoteSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtRFQEntryQuoteSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtRFQEntryQuoteSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_RFQEntryQuoteSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryQuoteSearchTableset,
}
}

