import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.CashHeadSearchSvc
// Description: 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/$metadata", {
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
   Description: Get CashHeadSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashHeadSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashHeadRow
   */  
export function get_CashHeadSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/CashHeadSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashHeadSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CashHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CashHeadSearches(requestBody:Erp_Tablesets_CashHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/CashHeadSearches", {
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
   Summary: Calls GetByID to retrieve the CashHeadSearch item
   Description: Calls GetByID to retrieve the CashHeadSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashHeadSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CashHeadRow
   */  
export function get_CashHeadSearches_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/CashHeadSearches(" + Company + "," + GroupID + "," + HeadNum + ")", {
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
         resolve(data as Erp_Tablesets_CashHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CashHeadSearch for the service
   Description: Calls UpdateExt to update CashHeadSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashHeadSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CashHeadSearches_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, requestBody:Erp_Tablesets_CashHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/CashHeadSearches(" + Company + "," + GroupID + "," + HeadNum + ")", {
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
   Summary: Call UpdateExt to delete CashHeadSearch item
   Description: Call UpdateExt to delete CashHeadSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashHeadSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CashHeadSearches_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/CashHeadSearches(" + Company + "," + GroupID + "," + HeadNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadListRow)
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
export function get_GetRows(whereClauseCashHead:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCashHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCashHead=" + whereClauseCashHead
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/GetRows" + params, {
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
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(groupID:string, headNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof groupID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "groupID=" + groupID
   }
   if(typeof headNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "headNum=" + headNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetCashReceiptRelationshipMap
   Description: Returns a serialized json string to show a Relationship Map for Cash Receipt
   OperationID: GetCashReceiptRelationshipMap
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCashReceiptRelationshipMap_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCashReceiptRelationshipMap_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCashReceiptRelationshipMap(requestBody:GetCashReceiptRelationshipMap_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCashReceiptRelationshipMap_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/GetCashReceiptRelationshipMap", {
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
         resolve(data as GetCashReceiptRelationshipMap_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListByInvoice
   OperationID: GetListByInvoice
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListByInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListByInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListByInvoice(requestBody:GetListByInvoice_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListByInvoice_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/GetListByInvoice", {
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
         resolve(data as GetListByInvoice_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListByInvoiceWhereClause
   Description: Receives a where clause string and extracts the variables needed to run GetListByInvoice
   OperationID: GetListByInvoiceWhereClause
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListByInvoiceWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListByInvoiceWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListByInvoiceWhereClause(requestBody:GetListByInvoiceWhereClause_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListByInvoiceWhereClause_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/GetListByInvoiceWhereClause", {
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
         resolve(data as GetListByInvoiceWhereClause_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetGroupHeadQuery
   OperationID: GetGroupHeadQuery
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetGroupHeadQuery_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGroupHeadQuery_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGroupHeadQuery(requestBody:GetGroupHeadQuery_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetGroupHeadQuery_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/GetGroupHeadQuery", {
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
         resolve(data as GetGroupHeadQuery_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsForInvoice
   Description: Invokes GetRows filtering on Cash Receipts for the specified Invoice
   OperationID: GetRowsForInvoice
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsForInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForInvoice(requestBody:GetRowsForInvoice_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsForInvoice_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/GetRowsForInvoice", {
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
         resolve(data as GetRowsForInvoice_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsForQuote
   Description: Invokes GetRows filtering on Cash Receipts for the specified Quote
   OperationID: GetRowsForQuote
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsForQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForQuote(requestBody:GetRowsForQuote_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsForQuote_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/GetRowsForQuote", {
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
         resolve(data as GetRowsForQuote_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsForSalesOrder
   Description: Invokes GetRows filtering on Cash Receipts for the specified Sales Order
   OperationID: GetRowsForSalesOrder
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsForSalesOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForSalesOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForSalesOrder(requestBody:GetRowsForSalesOrder_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsForSalesOrder_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/GetRowsForSalesOrder", {
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
         resolve(data as GetRowsForSalesOrder_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsForShipment
   Description: Invokes GetRows filtering on Cash Receipts for the specified Customer Shipment
   OperationID: GetRowsForShipment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsForShipment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForShipment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForShipment(requestBody:GetRowsForShipment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsForShipment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/GetRowsForShipment", {
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
         resolve(data as GetRowsForShipment_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCashHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCashHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashHead(requestBody:GetNewCashHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCashHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/GetNewCashHead", {
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
         resolve(data as GetNewCashHead_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashHeadListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashHeadRow,
}

export interface Erp_Tablesets_CashHeadListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Displays the ID of the group the transaction is assigned to.  */  
   "GroupID":string,
      /**  Displays the receipt header number used for internal reference.  */  
   "HeadNum":number,
      /**  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   "Posted":boolean,
      /**  Displays the transaction type.  */  
   "TranType":string,
      /**  Displays the number of the check.  */  
   "CheckRef":string,
      /**  Sales Order #.  This is only used by the PrePay transaction. It must be a valid order found in OrderHed.  */  
   "OrderNum":number,
      /**  The invoice # that is to be adjusted or the invoice number of a credit memo that is to be applied. This field is only used when TranType = CMemo or Adjust. It must be a valid open invoice memo found in the InvcHead file.  */  
   "InvoiceNum":number,
      /**  Displays the transaction amount.  */  
   "TranAmt":number,
      /**  Displays the transaction amount in customer currency.  */  
   "DocTranAmt":number,
      /**  Displays the customer ID.  */  
   "CustID":string,
      /**  Displays the date of the transaction.  */  
   "TranDate":string,
      /**  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  */  
   "CustNum":number,
      /**  Displays the unapplied amount.  */  
   "UnAppliedAmt":number,
      /**  Displays the unapplied amount in base currency.  */  
   "DocUnAppliedAmt":number,
      /**  Displays the amount applied to invoices.  */  
   "AppliedAmt":number,
      /**  Displays the amount in document currency applied to invoices.  */  
   "DocAppliedAmt":number,
      /**  Displays the fiscal year that the check is posted to.  */  
   "FiscalYear":number,
      /**  Displays the fiscal period that the check is posted to.  */  
   "FiscalPeriod":number,
      /**  Displays any reference.  */  
   "Reference":string,
      /**  Indicates if this transaction has been posted.  */  
   "GLPosted":boolean,
      /**  The invoice number that was used to create the credit memo for the unapplied cash receipt. This is updated during the cash receipt posting process and is used to link to the invchead.  */  
   "CreditMemoNum":number,
      /**  Displays the customer currency.  */  
   "CurrencyCode":string,
      /**  Displays the exchange rate that is used for this check.  */  
   "ExchangeRate":number,
      /**  The Tax Region for this payment.  */  
   "TaxRegionCode":string,
      /**  Total Tax Amount.  */  
   "TaxAmt":number,
      /**  Displays the tax amount.  */  
   "DocTaxAmt":number,
      /**  This field identifies a bankslip.  */  
   "CashBookNum":number,
      /**  This field identifies a line of a bankslip.  */  
   "CashbookLine":number,
      /**  Displays the legal number of the check.  */  
   "LegalNumber":string,
      /**  External ID  */  
   "ExternalID":string,
      /**  Link to the related GLRefTyp.RefType.  */  
   "GLRefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "GLRefCode":string,
      /**  The member's name on the credit card.  */  
   "CardMemberName":string,
      /**  The credit card account identifier.  */  
   "CardNumber":string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   "CardType":string,
      /**  The expiration month of the credit card.  */  
   "ExpirationMonth":number,
      /**  The expiration year of the credit card.  */  
   "ExpirationYear":number,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  */  
   "CardID":string,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   "CardmemberReference":string,
      /**  Stores the encrypted credit card number  */  
   "ProcessCard":string,
      /**  Credit Transaction Amount, makes up part of CCTotal  */  
   "CCAmount":number,
      /**  Credit Card transaction freight amount, part of CCTotal  */  
   "CCFreight":number,
      /**  Credit Card Transaction Tax amount, part of CCTotal  */  
   "CCTax":number,
      /**  Total amount being sent to the credit card processor  */  
   "CCTotal":number,
      /**  See CCAmount  */  
   "CCDocAmount":number,
      /**  See CCFreight  */  
   "CCDocFreight":number,
      /**  See CCTax  */  
   "CCDocTax":number,
      /**  See CCTotal  */  
   "CCDocTotal":number,
      /**  Address used during AVS validation for credit transactions  */  
   "CCStreetAddr":string,
      /**  Zip used during AVS validation in credit transactions  */  
   "CCZip":string,
      /**  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available. If this flag is yes the check amount is 0 (no cash processed) and the check number is not assigned by the user.  */  
   "DebNoteOnly":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1AppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2AppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3AppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnAppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnAppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnAppliedAmt":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Amount of deposit applied  */  
   "DocDepApplied":number,
      /**  See CCAmount  */  
   "Rpt1CCAmount":number,
      /**  See CCAmount  */  
   "Rpt2CCAmount":number,
      /**  See CCAmount  */  
   "Rpt3CCAmount":number,
      /**  See CCFreight  */  
   "Rpt1CCFreight":number,
      /**  See CCFreight  */  
   "Rpt2CCFreight":number,
      /**  See CCFreight  */  
   "Rpt3CCFreight":number,
      /**  See CCTax  */  
   "Rpt1CCTax":number,
      /**  See CCTax  */  
   "Rpt2CCTax":number,
      /**  See CCTax  */  
   "Rpt3CCTax":number,
      /**  See CCTotal  */  
   "Rpt1CCTotal":number,
      /**  See CCTotal  */  
   "Rpt2CCTotal":number,
      /**  See CCTotal  */  
   "Rpt3CCTotal":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   "RecalcBeforePost":boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
      /**  Withholding Tax Amount.  */  
   "WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "DocWithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt1WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt2WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt3WithholdAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "DocSelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt1SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt2SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt3SelfAssessAmt":number,
      /**  The unique code of Receipt Currency.  */  
   "ReceiptCurrencyCode":string,
      /**  Amount of Receipt in Receipt Currency.  */  
   "ReceiptAmt":number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Bank Currency.  */  
   "BankRcptExchangeRate":number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Settlement Currency.  */  
   "SettlementExchangeRate":number,
      /**  The unique Currency code for Credit Memo.  */  
   "CMCurrencyCode":string,
      /**  Amount of Credit Memo in CM Currency.  */  
   "CMAmount":number,
      /**  Reference to cash receipt which had been reversed.  */  
   "ReverseRef":number,
      /**  Date when cash receipt had been reversed  */  
   "ReverseDate":string,
      /**  Bank Account ID  */  
   "BankAcctID":string,
      /**  Withhold Tax  */  
   "TaxWhld":number,
      /**  Dsicount Date  */  
   "DiscountDate":string,
      /**  Calculate Withhold Tax  */  
   "TaxWhldCalc":number,
      /**  Addition to Contract  */  
   "ContractDate":string,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   "Plant":string,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Base currency.  */  
   "UnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Document currency.  */  
   "DocUnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt1 currency.  */  
   "Rpt1UnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt2 currency.  */  
   "Rpt2UnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt3 currency.  */  
   "Rpt3UnallocatedAmt":number,
      /**  Number of the unallocated deposit payment to be apply.  */  
   "ApplyHeadNum":number,
      /**  Used during the allocation process of the unallocated deposit payment. Base currency.  */  
   "AllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Document currency.  */  
   "DocAllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt1 currency.  */  
   "Rpt1AllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt2 currency.  */  
   "Rpt2AllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt3 currency.  */  
   "Rpt3AllocatedAmt":number,
      /**  Comments related to the cash receipt.  */  
   "Comment":string,
      /**  Payment Method Unique Identifier  */  
   "PMUID":number,
      /**  Unique identifier of Petty Cash Desk  */  
   "PCashDeskID":string,
      /**  ID Given by the Bank assigned during matching  */  
   "BankTranID":string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   "PCashRefNum":number,
      /**  Transaction Document Type for the record.  */  
   "TranDocTypeID":string,
      /**  Main Site  */  
   "MainSite":boolean,
      /**  Site Code  */  
   "SiteCode":string,
      /**  Branch ID  */  
   "BranchID":string,
      /**  Invoice Date  */  
   "InvoiceDate":string,
      /**  Tax Remarks  */  
   "TaxRemarks":string,
      /**  Non Deductable Code  */  
   "NonDeductCode":string,
      /**  Non Deductable Amount  */  
   "NonDeductAmt":number,
      /**  Non Deductable Doc Amount  */  
   "NonDeductDocAmt":number,
      /**  Non Deductable Rpt1 Amount  */  
   "NonDeductRpt1Amt":number,
      /**  Non Deductable Rpt2 Amount  */  
   "NonDeductRpt2Amt":number,
      /**  Non Deductable Rpt3 Amount  */  
   "NonDeductRpt3Amt":number,
      /**  Asset Type Code  */  
   "AssetTypeCode":string,
      /**  Cash  */  
   "Cash":boolean,
      /**  Credit Card  */  
   "CreditCard":boolean,
      /**  Normal  */  
   "Normal":boolean,
      /**  Excluded  */  
   "Excluded":boolean,
      /**  Deferred  */  
   "Deferred":boolean,
      /**  Bank Transaction Date  */  
   "BankTransDate":string,
      /**  Payee  */  
   "Payee":string,
      /**  AccountNumber  */  
   "AccountNumber":string,
      /**  OtherDetails  */  
   "OtherDetails":string,
      /**  MandateReference  */  
   "MandateReference":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  SEPADDExportDate  */  
   "SEPADDExportDate":string,
      /**  BOE Invoice Number  */  
   "BOEInvoiceNum":number,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  OwnReference  */  
   "OwnReference":string,
      /**  DocumentType  */  
   "DocumentType":string,
      /**  ABTUID  */  
   "ABTUID":string,
      /**  BankRcptExchangeRate10D  */  
   "BankRcptExchangeRate10D":number,
      /**  SettlementExchangeRate10D  */  
   "SettlementExchangeRate10D":number,
      /**  Indicates that cash receipt is currently excluded from batch in Bank Statement Processing.  */  
   "BankBatchExcluded":boolean,
      /**  BankBatchSysRowID  */  
   "BankBatchSysRowID":string,
      /**  PayMethodReference  */  
   "PayMethodReference":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  OnAccount  */  
   "OnAccount":boolean,
      /**  MX Receipt’s Fiscal Folio (UUID)  */  
   "MXFiscalFolio":string,
      /**  For TranType = "PayInv" it is true only if ARSyst.AllowSettlementInDiffCurr is true. For other types it is true always.  */  
   "AllowUpdSettlementCurr":boolean,
   "ApplyDate":string,
      /**  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   "AVSAddr":string,
      /**  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   "AVSZip":string,
   "BankAcctDesc":string,
      /**  The Bank's full name.  */  
   "BankAcctIDBankName":string,
      /**  Bank Currency Value  */  
   "BankAmount":number,
   "BankBaseXRateLabel":string,
   "BankCurrencyCode":string,
      /**  Bank Currency Symbol  */  
   "BankCurrSymbol":string,
   "BankExchangeRate":number,
   "BankRcptXRateLabel":string,
   "BaseCurrencyCode":string,
   "BaseCurrSymbol":string,
      /**  Bill To Name  */  
   "BillToName":string,
      /**  Indicates if rate was calculated from TranAmt fields instead of CurrExRate table  */  
   "calcRate":boolean,
      /**  Stored Credit Card Number  */  
   "CardStore":string,
      /**  The credit card description. For example, American Express, Visa, Master Card, Discover, etc.  */  
   "CardTypeDescription":string,
      /**  Description  */  
   "CashbookLineDescription":string,
      /**  Field to enable/disable the Sale and Deposit Buttons in the Credit Card Tab. This button will depend in the status of the AllowDepPay in CreditCardProc.  */  
   "CCAllowSales":boolean,
   "CCApprovalNum":string,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  */  
   "CCCSCID":string,
      /**  Field to enable/disable the Customer Address fields in the Credit Card Tab. This button will depend in the status of the UseAVSin CreditCardProc.  */  
   "CCEnableAddress":boolean,
      /**  s fields in the Credit Card Tab. This button will depend in the status of the UseCSC in CreditCardProc.  */  
   "CCEnableCSC":boolean,
      /**  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  */  
   "CCResponse":string,
      /**  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  */  
   "CCTranID":string,
      /**  Credit Card Transaction Type  */  
   "CCTranType":string,
      /**  Description of the currency  */  
   "CMCurrencyCodeCurrDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CMCurrencyCodeCurrencyID":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CMCurrencyCodeCurrName":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CMCurrencyCodeCurrSymbol":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CMCurrencyCodeDocumentDesc":string,
      /**  Customer Credit Hold flag  */  
   "CreditHold":boolean,
      /**  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   "CSCResult":string,
      /**  Description of the currency  */  
   "CurrencyCodeCurrDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCodeCurrencyID":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCodeCurrName":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCodeCurrSymbol":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyCodeDocumentDesc":string,
   "CurrencySwitch":boolean,
   "CustFullAddr":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustNumBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustNumCustID":string,
      /**  The full name of the customer.  */  
   "CustNumName":string,
   "CustomerName":string,
      /**  Display GL Account  */  
   "DispGLAcct":string,
   "DocDiscount":number,
   "DocReceipt":number,
      /**  Transaction Amount less Tax Amount  */  
   "DocTranTaxAmt":number,
      /**  Document number: Invoice Number if source document is AR Invoice or HeadNum if source document is Deposit Payment.  */  
   "DocumentNum":number,
      /**  Amount of Credit Memo in CM Currency.  */  
   "DspCMAmount":number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user enters this amount and then it is used as a limit/control when applying it to the invoices.  */  
   "DspDocTranAmt":number,
   "DspSalesOrderValue":number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  */  
   "DspTranAmt":number,
   "EnableTransactionDate":boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  */  
   "FullyPaid":boolean,
      /**  The InvcHead legal number  */  
   "InvcLegalNumber":string,
      /**  The member's name on the credit card.  */  
   "InvoiceNumCardMemberName":string,
      /**  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   "InvoiceNumTermsCode":string,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
   "LegalNumberDsp":string,
   "LegalNumMessage":string,
      /**  Copied from OrderHed.LockRate  */  
   "LockRate":boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
      /**  The member's name on the credit card.  */  
   "OrderNumCardMemberName":string,
      /**  A unique code that identifies the currency.  */  
   "OrderNumCurrencyCode":string,
   "PaymentMethod":string,
      /**  Description  */  
   "RateGrpDescription":string,
      /**  Description of the currency  */  
   "RcptCurrencyCodeCurrDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "RcptCurrencyCodeCurrencyID":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "RcptCurrencyCodeCurrName":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "RcptCurrencyCodeCurrSymbol":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "RcptCurrencyCodeDocumentDesc":string,
      /**  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  */  
   "ReferencePNRef":string,
      /**  Transaction Amount less Tax Amount  */  
   "Rpt1TranTaxAmt":number,
      /**  Transaction Amount less Tax Amount  */  
   "Rpt2TranTaxAmt":number,
      /**  Transaction Amount less Tax Amount  */  
   "Rpt3TranTaxAmt":number,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
   "SalesOrderValue":number,
   "SettlementXRateLabel":string,
      /**  Name of the Sold To customer if this is a Deposit (created using an OrderHed).  */  
   "SoldToCustomerName":string,
      /**  Full description for the Tax Region.  */  
   "TaxRegionCodeDescription":string,
      /**  Sum of all rounding differences of the payments for one Cash Receipt and one Check  */  
   "TotalRoundDiff":number,
      /**  Transaction Amount less Tax Amount  */  
   "TranTaxAmt":number,
      /**  Description of TranType  */  
   "TranTypeDesc":string,
      /**  Yes if Cash Receipt has Unapplied amount but credit memo is applied.  */  
   "UnappliedAmountApplied":boolean,
   "XRateLabel":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CashHeadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Displays the ID of the group the transaction is assigned to.  */  
   "GroupID":string,
      /**  Displays the receipt header number used for internal reference.  */  
   "HeadNum":number,
      /**  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   "Posted":boolean,
      /**  Displays the transaction type.  */  
   "TranType":string,
      /**  Displays the number of the check.  */  
   "CheckRef":string,
      /**  Sales Order #.  This is only used by the PrePay transaction. It must be a valid order found in OrderHed.  */  
   "OrderNum":number,
      /**  The invoice # that is to be adjusted or the invoice number of a credit memo that is to be applied. This field is only used when TranType = CMemo or Adjust. It must be a valid open invoice memo found in the InvcHead file.  */  
   "InvoiceNum":number,
      /**  Displays the transaction amount.  */  
   "TranAmt":number,
      /**  Displays the transaction amount in customer currency.  */  
   "DocTranAmt":number,
      /**  Displays the customer ID.  */  
   "CustID":string,
      /**  Displays the date of the transaction.  */  
   "TranDate":string,
      /**  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  */  
   "CustNum":number,
      /**  Displays the unapplied amount.  */  
   "UnAppliedAmt":number,
      /**  Displays the unapplied amount in base currency.  */  
   "DocUnAppliedAmt":number,
      /**  Displays the amount applied to invoices.  */  
   "AppliedAmt":number,
      /**  Displays the amount in document currency applied to invoices.  */  
   "DocAppliedAmt":number,
      /**  Displays the fiscal year that the check is posted to.  */  
   "FiscalYear":number,
      /**  Displays the fiscal period that the check is posted to.  */  
   "FiscalPeriod":number,
      /**  Displays any reference.  */  
   "Reference":string,
      /**  Indicates if this transaction has been posted.  */  
   "GLPosted":boolean,
      /**  The invoice number that was used to create the credit memo for the unapplied cash receipt. This is updated during the cash receipt posting process and is used to link to the invchead.  */  
   "CreditMemoNum":number,
      /**  Displays the customer currency.  */  
   "CurrencyCode":string,
      /**  Displays the exchange rate that is used for this check.  */  
   "ExchangeRate":number,
      /**  The Tax Region for this payment.  */  
   "TaxRegionCode":string,
      /**  Total Tax Amount.  */  
   "TaxAmt":number,
      /**  Displays the tax amount.  */  
   "DocTaxAmt":number,
      /**  This field identifies a bankslip.  */  
   "CashBookNum":number,
      /**  This field identifies a line of a bankslip.  */  
   "CashbookLine":number,
      /**  Displays the legal number of the check.  */  
   "LegalNumber":string,
      /**  External ID  */  
   "ExternalID":string,
      /**  Link to the related GLRefTyp.RefType.  */  
   "GLRefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "GLRefCode":string,
      /**  The member's name on the credit card.  */  
   "CardMemberName":string,
      /**  The credit card account identifier.  */  
   "CardNumber":string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   "CardType":string,
      /**  The expiration month of the credit card.  */  
   "ExpirationMonth":number,
      /**  The expiration year of the credit card.  */  
   "ExpirationYear":number,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  */  
   "CardID":string,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   "CardmemberReference":string,
      /**  Stores the encrypted credit card number  */  
   "ProcessCard":string,
      /**  Credit Transaction Amount, makes up part of CCTotal  */  
   "CCAmount":number,
      /**  Credit Card transaction freight amount, part of CCTotal  */  
   "CCFreight":number,
      /**  Credit Card Transaction Tax amount, part of CCTotal  */  
   "CCTax":number,
      /**  Total amount being sent to the credit card processor  */  
   "CCTotal":number,
      /**  See CCAmount  */  
   "CCDocAmount":number,
      /**  See CCFreight  */  
   "CCDocFreight":number,
      /**  See CCTax  */  
   "CCDocTax":number,
      /**  See CCTotal  */  
   "CCDocTotal":number,
      /**  Address used during AVS validation for credit transactions  */  
   "CCStreetAddr":string,
      /**  Zip used during AVS validation in credit transactions  */  
   "CCZip":string,
      /**  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available. If this flag is yes the check amount is 0 (no cash processed) and the check number is not assigned by the user.  */  
   "DebNoteOnly":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1AppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2AppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3AppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnAppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnAppliedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnAppliedAmt":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Amount of deposit applied  */  
   "DocDepApplied":number,
      /**  See CCAmount  */  
   "Rpt1CCAmount":number,
      /**  See CCAmount  */  
   "Rpt2CCAmount":number,
      /**  See CCAmount  */  
   "Rpt3CCAmount":number,
      /**  See CCFreight  */  
   "Rpt1CCFreight":number,
      /**  See CCFreight  */  
   "Rpt2CCFreight":number,
      /**  See CCFreight  */  
   "Rpt3CCFreight":number,
      /**  See CCTax  */  
   "Rpt1CCTax":number,
      /**  See CCTax  */  
   "Rpt2CCTax":number,
      /**  See CCTax  */  
   "Rpt3CCTax":number,
      /**  See CCTotal  */  
   "Rpt1CCTotal":number,
      /**  See CCTotal  */  
   "Rpt2CCTotal":number,
      /**  See CCTotal  */  
   "Rpt3CCTotal":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   "RecalcBeforePost":boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
      /**  Withholding Tax Amount.  */  
   "WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "DocWithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt1WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt2WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt3WithholdAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "DocSelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt1SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt2SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt3SelfAssessAmt":number,
      /**  The unique code of Receipt Currency.  */  
   "ReceiptCurrencyCode":string,
      /**  Amount of Receipt in Receipt Currency.  */  
   "ReceiptAmt":number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Bank Currency.  */  
   "BankRcptExchangeRate":number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Settlement Currency.  */  
   "SettlementExchangeRate":number,
      /**  The unique Currency code for Credit Memo.  */  
   "CMCurrencyCode":string,
      /**  Amount of Credit Memo in CM Currency.  */  
   "CMAmount":number,
      /**  Reference to cash receipt which had been reversed.  */  
   "ReverseRef":number,
      /**  Date when cash receipt had been reversed  */  
   "ReverseDate":string,
      /**  Bank Account ID  */  
   "BankAcctID":string,
      /**  Withhold Tax  */  
   "TaxWhld":number,
      /**  Dsicount Date  */  
   "DiscountDate":string,
      /**  Calculate Withhold Tax  */  
   "TaxWhldCalc":number,
      /**  Addition to Contract  */  
   "ContractDate":string,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   "Plant":string,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Base currency.  */  
   "UnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Document currency.  */  
   "DocUnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt1 currency.  */  
   "Rpt1UnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt2 currency.  */  
   "Rpt2UnallocatedAmt":number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt3 currency.  */  
   "Rpt3UnallocatedAmt":number,
      /**  Number of the unallocated deposit payment to be apply.  */  
   "ApplyHeadNum":number,
      /**  Used during the allocation process of the unallocated deposit payment. Base currency.  */  
   "AllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Document currency.  */  
   "DocAllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt1 currency.  */  
   "Rpt1AllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt2 currency.  */  
   "Rpt2AllocatedAmt":number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt3 currency.  */  
   "Rpt3AllocatedAmt":number,
      /**  Comments related to the cash receipt.  */  
   "Comment":string,
      /**  Payment Method Unique Identifier  */  
   "PMUID":number,
      /**  Unique identifier of Petty Cash Desk  */  
   "PCashDeskID":string,
      /**  ID Given by the Bank assigned during matching  */  
   "BankTranID":string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   "PCashRefNum":number,
      /**  Transaction Document Type for the record.  */  
   "TranDocTypeID":string,
      /**  Main Site  */  
   "MainSite":boolean,
      /**  Site Code  */  
   "SiteCode":string,
      /**  Branch ID  */  
   "BranchID":string,
      /**  Invoice Date  */  
   "InvoiceDate":string,
      /**  Tax Remarks  */  
   "TaxRemarks":string,
      /**  Non Deductable Code  */  
   "NonDeductCode":string,
      /**  Non Deductable Amount  */  
   "NonDeductAmt":number,
      /**  Non Deductable Doc Amount  */  
   "NonDeductDocAmt":number,
      /**  Non Deductable Rpt1 Amount  */  
   "NonDeductRpt1Amt":number,
      /**  Non Deductable Rpt2 Amount  */  
   "NonDeductRpt2Amt":number,
      /**  Non Deductable Rpt3 Amount  */  
   "NonDeductRpt3Amt":number,
      /**  Asset Type Code  */  
   "AssetTypeCode":string,
      /**  Cash  */  
   "Cash":boolean,
      /**  Credit Card  */  
   "CreditCard":boolean,
      /**  Normal  */  
   "Normal":boolean,
      /**  Excluded  */  
   "Excluded":boolean,
      /**  Deferred  */  
   "Deferred":boolean,
      /**  Bank Transaction Date  */  
   "BankTransDate":string,
      /**  Payee  */  
   "Payee":string,
      /**  AccountNumber  */  
   "AccountNumber":string,
      /**  OtherDetails  */  
   "OtherDetails":string,
      /**  MandateReference  */  
   "MandateReference":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  SEPADDExportDate  */  
   "SEPADDExportDate":string,
      /**  BOE Invoice Number  */  
   "BOEInvoiceNum":number,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  OwnReference  */  
   "OwnReference":string,
      /**  DocumentType  */  
   "DocumentType":string,
      /**  ABTUID  */  
   "ABTUID":string,
      /**  BankRcptExchangeRate10D  */  
   "BankRcptExchangeRate10D":number,
      /**  SettlementExchangeRate10D  */  
   "SettlementExchangeRate10D":number,
      /**  Indicates that cash receipt is currently excluded from batch in Bank Statement Processing.  */  
   "BankBatchExcluded":boolean,
      /**  BankBatchSysRowID  */  
   "BankBatchSysRowID":string,
      /**  PayMethodReference  */  
   "PayMethodReference":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  OnAccount  */  
   "OnAccount":boolean,
      /**  The amount of the cash receipt applied to invoices in receipt currency  */  
   "RcptCurAppliedAmt":number,
      /**  The amount of the cash receipt that is unapplied in receipt currency  */  
   "RcptCurUnAppliedAmt":number,
      /**  MXAccountNumber  */  
   "MXAccountNumber":string,
      /**  MX Method of Payment: single, multiple, etc.  */  
   "MXPaidAs":string,
      /**  If TRUE then MX Electronic Payment XML is required  */  
   "MXPaySupplementFlag":boolean,
      /**  LockboxID  */  
   "LockboxID":string,
      /**  MX Receipt’s Fiscal Folio (UUID)  */  
   "MXFiscalFolio":string,
      /**  MX UUID of the original Receipt being corrected  */  
   "MXOriginalCheckRef":string,
      /**  MX Confirmation Code for special Cash Receipts  */  
   "MXConfirmationCode":string,
      /**  MX Customer’s Bank ID  */  
   "MXBankID":string,
      /**  Text entered by the user to indicate the reason Cash receipt was Reversed.  */  
   "ReversedReason":string,
      /**  Credit Card Holder City.  */  
   "CCCity":string,
      /**  Credit Card Holder State.  */  
   "CCState":string,
      /**  ccToken  */  
   "ccToken":string,
      /**  DepositBalance  */  
   "DepositBalance":number,
      /**  DocDepositBalance  */  
   "DocDepositBalance":number,
      /**  Rpt1DepositBalance  */  
   "Rpt1DepositBalance":number,
      /**  Rpt2DepositBalance  */  
   "Rpt2DepositBalance":number,
      /**  Rpt3DepositBalance  */  
   "Rpt3DepositBalance":number,
      /**  Indicates this record is an adjustment CashHead.  */  
   "Adjustment":boolean,
      /**  Reference to cash receipt which had been adjusted.  */  
   "AdjustmentRef":number,
      /**  The reason for the adjustment entered by the user  */  
   "AdjustmentReason":string,
      /**  Total Check Write Off Amount  */  
   "WriteOffAmount":number,
      /**  DocWriteOffAmount  */  
   "DocWriteOffAmount":number,
      /**  Rpt1WriteOffAmount  */  
   "Rpt1WriteOffAmount":number,
      /**  Rpt2WriteOffAmount  */  
   "Rpt2WriteOffAmount":number,
      /**  Rpt3WriteOffAmount  */  
   "Rpt3WriteOffAmount":number,
      /**  Mexico Certified Timestamp  */  
   "MXCertifiedTimestamp":string,
      /**  Mexico SAT Seal  */  
   "MXSATSeal":string,
      /**  Mexico Digital Seal  */  
   "MXDigitalSeal":string,
      /**  Mexico SAT Certificate Serial Number  */  
   "MXSATCertificateSN":string,
      /**  Mexico Original String Timbre Fiscal Digital  */  
   "MXOriginalStringTFD":string,
      /**  Mexico Certificate  */  
   "MXCertificate":string,
      /**  Mexico Certificate Serial Number  */  
   "MXCertificateSN":string,
      /**  SourceGroupID  */  
   "SourceGroupID":string,
      /**  SourceHeadNum  */  
   "SourceHeadNum":number,
      /**  Standard Entry Class Code  */  
   "SEC":string,
      /**  ACH Transaction Code  */  
   "ACHTranCode":number,
      /**  ID of the Customer's bank.  */  
   "CustomerBankID":string,
      /**  The Bank account number for the Customer.  */  
   "CustomerBankAcctNumber":string,
      /**  CustomerBankSwiftNum  */  
   "CustomerBankSwiftNum":string,
      /**  The Bank account IBAN Code  */  
   "CustomerBankIBANCode":string,
      /**  Name on the Bank Account.  */  
   "CustomerBankNameOnAccount":string,
      /**  First address line of customer bank.  */  
   "CustomerBankAddress1":string,
      /**  Second address line of customer bank.  */  
   "CustomerBankAddress2":string,
      /**  Third address line of customer bank.  */  
   "CustomerBankAddress3":string,
      /**  Bank City  */  
   "CustomerBankCity":string,
      /**  Bank State/Prov  */  
   "CustomerBankState":string,
      /**  Postal Code or zip code  */  
   "CustomerBankPostalCode":string,
      /**  Bank account Country Number.  */  
   "CustomerBankCountryNum":number,
      /**  ARRemittanceSlipPrinted  */  
   "ARRemittanceSlipPrinted":boolean,
      /**  Customer Bank Name  */  
   "CustomerBankName":string,
      /**  MXPostedTimeStamp  */  
   "MXPostedTimeStamp":string,
      /**  MXSerie  */  
   "MXSerie":string,
      /**  MXFolio  */  
   "MXFolio":string,
      /**  MXEPaymentType  */  
   "MXEPaymentType":string,
      /**  MXEPaymentCertificateNumber  */  
   "MXEPaymentCertificateNumber":string,
      /**  MXEPaymentOriginalString  */  
   "MXEPaymentOriginalString":string,
      /**  MXEPaymentDigitalSeal  */  
   "MXEPaymentDigitalSeal":string,
      /**  Source  */  
   "Source":string,
      /**  Id of the netting transaction that generated this document.  */  
   "NettingID":number,
      /**  GL Description for the Reverse process  */  
   "RevDescription":string,
      /**  GL Description for AR - Apply Credit Memo  */  
   "CMDescription":string,
      /**  Receipt Amount in Bank Currency  */  
   "BankReceiptAmt":number,
      /**  MXCancelReasonCode  */  
   "MXCancelReasonCode":string,
      /**  MXSubstHeadNum  */  
   "MXSubstHeadNum":number,
      /**  MXCancellationMode  */  
   "MXCancellationMode":string,
      /**  E-invoice error description.  */  
   "ELIEInvException":string,
      /**  EInvoice ID  */  
   "ELIEInvID":string,
      /**  E-invoice  */  
   "ELIEInvoice":boolean,
      /**  E-invoice Service Provider Status  */  
   "ELIEInvServiceProviderStatus":number,
      /**  E-invoice Status  */  
   "ELIEInvStatus":number,
      /**  User Id of the person generated E-invoice.  */  
   "ELIEInvUpdatedBy":string,
      /**  E-invoice Updated On  */  
   "ELIEInvUpdatedOn":string,
      /**  Adjustment Customer Name  */  
   "AdjustmentCustName":string,
      /**  Customer to which the new invoices will be applied.  */  
   "AdjustmentCustNum":number,
      /**  Date the adjustment was made.  */  
   "AdjustmentDate":string,
      /**  Displays the amount available to apply to the invoices.  */  
   "AdjustmentDocUnAppliedAmt":number,
      /**  On Account  */  
   "AdjustmentOnAccount":boolean,
      /**  Temp TranDocTypeID used when adjusting a Cash Rececipt  */  
   "AdjustmentTranDocTypeID":string,
   "AllocDepBal":number,
   "AllowChgAfterPrint":boolean,
      /**  For TranType = "PayInv" it is true only if ARSyst.AllowSettlementInDiffCurr is true. For other types it is true always.  */  
   "AllowUpdSettlementCurr":boolean,
      /**  Amount to Allocate  */  
   "AmtToAlloc":number,
   "ApplyDate":string,
      /**  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   "AVSAddr":string,
      /**  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   "AVSZip":string,
      /**  Bank Currency Value  */  
   "BankAmount":number,
   "BankBaseXRateLabel":string,
   "BankCurrencyCode":string,
      /**  Bank Currency Symbol  */  
   "BankCurrSymbol":string,
   "BankExchangeRate":number,
   "BankRcptXRateLabel":string,
   "BaseCurrencyCode":string,
      /**  Base Currency Symbol  */  
   "BaseCurrSymbol":string,
      /**  Bill To Name  */  
   "BillToName":string,
      /**  Indicates if rate was calculated from TranAmt fields instead of CurrExRate table  */  
   "calcRate":boolean,
      /**  Stored Credit Card Number  */  
   "CardStore":string,
      /**  Field to enable/disable the Sale and Deposit Buttons in the Credit Card Tab. This button will depend in the status of the AllowDepPay in CreditCardProc.  */  
   "CCAllowSales":boolean,
   "CCApprovalNum":string,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  */  
   "CCCSCID":string,
      /**  Tokenized value of CSCID  */  
   "CCCSCIDToken":string,
      /**  Field to enable/disable the Customer Address fields in the Credit Card Tab. This button will depend in the status of the UseAVSin CreditCardProc.  */  
   "CCEnableAddress":boolean,
      /**  s fields in the Credit Card Tab. This button will depend in the status of the UseCSC in CreditCardProc.  */  
   "CCEnableCSC":boolean,
      /**   Indicates if the credit card setup will be using a testing Paygate instance for transactions.
Force requests to use Paygate test url: paygate-test1.eaglesoa.com  */  
   "CCIsTraining":boolean,
      /**  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  */  
   "CCResponse":string,
      /**  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  */  
   "CCTranID":string,
      /**  Credit Card Transaction Type  */  
   "CCTranType":string,
      /**  Check Box on the UI to filter records by Central Collection flag  */  
   "CentralCollectionCheck":boolean,
      /**  If the user selects Credit Memo/Correction Invoice document type this flag indicates that this is Correction Invoice with negative amount  */  
   "CorrectionInv":boolean,
      /**  Customer Credit Hold flag  */  
   "CreditHold":boolean,
      /**  If the user selects Credit Memo/Correction Invoice document type this flag indicates that this is Credit Memo  */  
   "CreditMemo":boolean,
      /**  CREProcessor is true when Credit Card Configuration is CRE Server.  */  
   "CREProcessor":boolean,
      /**  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   "CSCResult":string,
      /**  Current Amount Selected on Invoice Select Tab  */  
   "CurrAmtSelected":number,
   "CurrencySwitch":boolean,
      /**  Displays the address of the customer that paid the receipt.  */  
   "CustFullAddr":string,
   "CustomerName":string,
   "DisableFieldsForPCashDoc":boolean,
      /**  Display GL Account  */  
   "DispGLAcct":string,
   "DocAllocDepBal":number,
      /**  Doc Amount to Allocate  */  
   "DocAmtToAlloc":number,
      /**  Displays the discount applied to the receipt.  */  
   "DocDiscount":number,
      /**  Displays the invoice amount paid by this receipt. The amount includes both discount and payment amounts.  */  
   "DocReceipt":number,
      /**  Transaction Amount less Tax Amount  */  
   "DocTranTaxAmt":number,
      /**  Document number: Invoice Number if source document is AR Invoice or HeadNum if source document is Deposit Payment.  */  
   "DocumentNum":number,
   "DocWhldTax":number,
   "DspBankBatchID":string,
      /**  Amount of Credit Memo in CM Currency.  */  
   "DspCMAmount":number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  */  
   "DspDocTranAmt":number,
   "DspSalesOrderValue":number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  */  
   "DspTranAmt":number,
   "EnableAssignLegNum":boolean,
      /**  Indicates if the option to get the default account is enable.  */  
   "EnableGetDefaultAcct":boolean,
   "EnableTranDocType":boolean,
   "EnableTransactionDate":boolean,
   "EnableVoidLegNum":boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  */  
   "FullyPaid":boolean,
   "GLRefCodeDescription":string,
   "HasLegNumCnfg":boolean,
      /**  The InvcHead legal number  */  
   "InvcLegalNumber":string,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
   "LegalNumberDsp":string,
   "LegalNumMessage":string,
      /**  Copied from OrderHed.LockRate  */  
   "LockRate":boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
   "ManualTaxAdj":boolean,
      /**  MXCancellationID  */  
   "MXCancellationID":string,
   "MXCancellationStatus":string,
      /**  MXECEPXml  */  
   "MXECEPXml":string,
      /**  Mexico Calculated field - shows Check Reference number of the original Receipt being corrected  */  
   "MXOriginalRefNum":string,
      /**  Host Address for the Paygate Hosted Token Service.  */  
   "PayGateHostAddress":string,
      /**  NameSpace for the Paygate Hosted Token Service.  */  
   "PayGateNameSpace":string,
      /**  Public Key for the Paygate Hosted Token Service EWA component.  */  
   "PayGatePublicKey":string,
      /**  This column is used within cash receipt tracker to show either the receipt date or the source/ original receipt date if the cash receipt has been adjusted.  */  
   "ReceiptDate":string,
      /**  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  */  
   "ReferencePNRef":string,
   "Rpt1AllocDepBal":number,
      /**  Transaction Amount less Tax Amount  */  
   "Rpt1TranTaxAmt":number,
   "Rpt1WhldTax":number,
   "Rpt2AllocDepBal":number,
      /**  Transaction Amount less Tax Amount  */  
   "Rpt2TranTaxAmt":number,
   "Rpt2WhldTax":number,
   "Rpt3AllocDepBal":number,
      /**  Transaction Amount less Tax Amount  */  
   "Rpt3TranTaxAmt":number,
   "Rpt3WhldTax":number,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
   "SalesOrderValue":number,
   "SettlementXRateLabel":string,
      /**  Name of the Sold To customer if this is a Deposit (created using an OrderHed).  */  
   "SoldToCustomerName":string,
   "SystemTranType":string,
      /**  Sum of all rounding differences of the payments for one Cash Receipt and one Check  */  
   "TotalRoundDiff":number,
      /**  Transaction Amount less Tax Amount  */  
   "TranTaxAmt":number,
      /**  Description of TranType  */  
   "TranTypeDesc":string,
      /**  Yes if Cash Receipt has Unapplied amount but credit memo is applied.  */  
   "UnappliedAmountApplied":boolean,
   "WhldTax":number,
   "XRateLabel":string,
      /**  Displays the customer ID.  */  
   "AdjustmentCustID":string,
   "ReferenceTranDate":string,
   "ReferenceTranNum":number,
   "ReferenceTranTime":number,
      /**  Displays the address of the customer that paid the receipt with newline delimiter.  */  
   "CustFullAddrFormatted":string,
      /**  Indicates if the user can manually modify the applied withholding tax of the invoice. Used in Apply Credit Memo when withholding tax was not posted through an interim account.  */  
   "EnableManualWHTax":boolean,
      /**  Indicates if the withholding tax was manually modified.  */  
   "WHTaxManualChange":boolean,
      /**  Payment type description, displayed in the Details page header.  */  
   "TranTypeDescCaption":string,
   "AdjustmentCustAddress":string,
      /**  Substitution Cash Receipt Group ID  */  
   "MXSubstGroupId":string,
      /**  Substitution Cash Receipt CheckRef  */  
   "MXSubstCheckRef":string,
      /**  Substitution Cash Receipt UUID  */  
   "MXSubstFiscalFolio":string,
   "BitFlag":number,
   "BankAcctIDDescription":string,
   "BankAcctIDBankName":string,
   "CardTypeDescription":string,
   "CashBHedPosted":boolean,
   "CashBHedCashBookNum":number,
   "CashbookLineDescription":string,
   "CMCurrencyCodeDocumentDesc":string,
   "CMCurrencyCodeCurrName":string,
   "CMCurrencyCodeCurrSymbol":string,
   "CMCurrencyCodeCurrDesc":string,
   "CMCurrencyCodeCurrencyID":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrDesc":string,
   "CustNumInactive":boolean,
   "CustNumName":string,
   "CustNumBTName":string,
   "CustNumCustID":string,
   "InvoiceNumTermsCode":string,
   "InvoiceNumCardMemberName":string,
   "OrderNumCardMemberName":string,
   "OrderNumCurrencyCode":string,
   "PCashDocDirection":string,
   "PMUIDName":string,
   "PMUIDMXSATCode":string,
   "PMUIDSummarizePerCustomer":boolean,
   "PMUIDType":number,
   "RateGrpDescription":string,
   "RcptCurrencyCodeCurrencyID":string,
   "RcptCurrencyCodeDocumentDesc":string,
   "RcptCurrencyCodeCurrDesc":string,
   "RcptCurrencyCodeCurrSymbol":string,
   "RcptCurrencyCodeCurrName":string,
   "ReverseMXCancelReasonCode":string,
   "ReverseMXCancellationMode":string,
   "SourceTranDateTranDate":string,
   "TaxRegionCodeDescription":string,
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
      @param groupID
      @param headNum
   */  
export interface DeleteByID_input{
   groupID:string,
   headNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_CashHeadListAttchRow{
   Company:string,
   GroupID:string,
   HeadNum:number,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:number,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashHeadListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Displays the ID of the group the transaction is assigned to.  */  
   GroupID:string,
      /**  Displays the receipt header number used for internal reference.  */  
   HeadNum:number,
      /**  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   Posted:boolean,
      /**  Displays the transaction type.  */  
   TranType:string,
      /**  Displays the number of the check.  */  
   CheckRef:string,
      /**  Sales Order #.  This is only used by the PrePay transaction. It must be a valid order found in OrderHed.  */  
   OrderNum:number,
      /**  The invoice # that is to be adjusted or the invoice number of a credit memo that is to be applied. This field is only used when TranType = CMemo or Adjust. It must be a valid open invoice memo found in the InvcHead file.  */  
   InvoiceNum:number,
      /**  Displays the transaction amount.  */  
   TranAmt:number,
      /**  Displays the transaction amount in customer currency.  */  
   DocTranAmt:number,
      /**  Displays the customer ID.  */  
   CustID:string,
      /**  Displays the date of the transaction.  */  
   TranDate:string,
      /**  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  */  
   CustNum:number,
      /**  Displays the unapplied amount.  */  
   UnAppliedAmt:number,
      /**  Displays the unapplied amount in base currency.  */  
   DocUnAppliedAmt:number,
      /**  Displays the amount applied to invoices.  */  
   AppliedAmt:number,
      /**  Displays the amount in document currency applied to invoices.  */  
   DocAppliedAmt:number,
      /**  Displays the fiscal year that the check is posted to.  */  
   FiscalYear:number,
      /**  Displays the fiscal period that the check is posted to.  */  
   FiscalPeriod:number,
      /**  Displays any reference.  */  
   Reference:string,
      /**  Indicates if this transaction has been posted.  */  
   GLPosted:boolean,
      /**  The invoice number that was used to create the credit memo for the unapplied cash receipt. This is updated during the cash receipt posting process and is used to link to the invchead.  */  
   CreditMemoNum:number,
      /**  Displays the customer currency.  */  
   CurrencyCode:string,
      /**  Displays the exchange rate that is used for this check.  */  
   ExchangeRate:number,
      /**  The Tax Region for this payment.  */  
   TaxRegionCode:string,
      /**  Total Tax Amount.  */  
   TaxAmt:number,
      /**  Displays the tax amount.  */  
   DocTaxAmt:number,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  This field identifies a line of a bankslip.  */  
   CashbookLine:number,
      /**  Displays the legal number of the check.  */  
   LegalNumber:string,
      /**  External ID  */  
   ExternalID:string,
      /**  Link to the related GLRefTyp.RefType.  */  
   GLRefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   GLRefCode:string,
      /**  The member's name on the credit card.  */  
   CardMemberName:string,
      /**  The credit card account identifier.  */  
   CardNumber:string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   CardType:string,
      /**  The expiration month of the credit card.  */  
   ExpirationMonth:number,
      /**  The expiration year of the credit card.  */  
   ExpirationYear:number,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  */  
   CardID:string,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   CardmemberReference:string,
      /**  Stores the encrypted credit card number  */  
   ProcessCard:string,
      /**  Credit Transaction Amount, makes up part of CCTotal  */  
   CCAmount:number,
      /**  Credit Card transaction freight amount, part of CCTotal  */  
   CCFreight:number,
      /**  Credit Card Transaction Tax amount, part of CCTotal  */  
   CCTax:number,
      /**  Total amount being sent to the credit card processor  */  
   CCTotal:number,
      /**  See CCAmount  */  
   CCDocAmount:number,
      /**  See CCFreight  */  
   CCDocFreight:number,
      /**  See CCTax  */  
   CCDocTax:number,
      /**  See CCTotal  */  
   CCDocTotal:number,
      /**  Address used during AVS validation for credit transactions  */  
   CCStreetAddr:string,
      /**  Zip used during AVS validation in credit transactions  */  
   CCZip:string,
      /**  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available. If this flag is yes the check amount is 0 (no cash processed) and the check number is not assigned by the user.  */  
   DebNoteOnly:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1AppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2AppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3AppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnAppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnAppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnAppliedAmt:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Amount of deposit applied  */  
   DocDepApplied:number,
      /**  See CCAmount  */  
   Rpt1CCAmount:number,
      /**  See CCAmount  */  
   Rpt2CCAmount:number,
      /**  See CCAmount  */  
   Rpt3CCAmount:number,
      /**  See CCFreight  */  
   Rpt1CCFreight:number,
      /**  See CCFreight  */  
   Rpt2CCFreight:number,
      /**  See CCFreight  */  
   Rpt3CCFreight:number,
      /**  See CCTax  */  
   Rpt1CCTax:number,
      /**  See CCTax  */  
   Rpt2CCTax:number,
      /**  See CCTax  */  
   Rpt3CCTax:number,
      /**  See CCTotal  */  
   Rpt1CCTotal:number,
      /**  See CCTotal  */  
   Rpt2CCTotal:number,
      /**  See CCTotal  */  
   Rpt3CCTotal:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  Withholding Tax Amount.  */  
   WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   DocWithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt1WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt2WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt3WithholdAmt:number,
      /**  Self Assessment Tax Amount.  */  
   SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   DocSelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt1SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt2SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt3SelfAssessAmt:number,
      /**  The unique code of Receipt Currency.  */  
   ReceiptCurrencyCode:string,
      /**  Amount of Receipt in Receipt Currency.  */  
   ReceiptAmt:number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Bank Currency.  */  
   BankRcptExchangeRate:number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Settlement Currency.  */  
   SettlementExchangeRate:number,
      /**  The unique Currency code for Credit Memo.  */  
   CMCurrencyCode:string,
      /**  Amount of Credit Memo in CM Currency.  */  
   CMAmount:number,
      /**  Reference to cash receipt which had been reversed.  */  
   ReverseRef:number,
      /**  Date when cash receipt had been reversed  */  
   ReverseDate:string,
      /**  Bank Account ID  */  
   BankAcctID:string,
      /**  Withhold Tax  */  
   TaxWhld:number,
      /**  Dsicount Date  */  
   DiscountDate:string,
      /**  Calculate Withhold Tax  */  
   TaxWhldCalc:number,
      /**  Addition to Contract  */  
   ContractDate:string,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   Plant:string,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Base currency.  */  
   UnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Document currency.  */  
   DocUnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt1 currency.  */  
   Rpt1UnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt2 currency.  */  
   Rpt2UnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt3 currency.  */  
   Rpt3UnallocatedAmt:number,
      /**  Number of the unallocated deposit payment to be apply.  */  
   ApplyHeadNum:number,
      /**  Used during the allocation process of the unallocated deposit payment. Base currency.  */  
   AllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Document currency.  */  
   DocAllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt1 currency.  */  
   Rpt1AllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt2 currency.  */  
   Rpt2AllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt3 currency.  */  
   Rpt3AllocatedAmt:number,
      /**  Comments related to the cash receipt.  */  
   Comment:string,
      /**  Payment Method Unique Identifier  */  
   PMUID:number,
      /**  Unique identifier of Petty Cash Desk  */  
   PCashDeskID:string,
      /**  ID Given by the Bank assigned during matching  */  
   BankTranID:string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   PCashRefNum:number,
      /**  Transaction Document Type for the record.  */  
   TranDocTypeID:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**  Site Code  */  
   SiteCode:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Invoice Date  */  
   InvoiceDate:string,
      /**  Tax Remarks  */  
   TaxRemarks:string,
      /**  Non Deductable Code  */  
   NonDeductCode:string,
      /**  Non Deductable Amount  */  
   NonDeductAmt:number,
      /**  Non Deductable Doc Amount  */  
   NonDeductDocAmt:number,
      /**  Non Deductable Rpt1 Amount  */  
   NonDeductRpt1Amt:number,
      /**  Non Deductable Rpt2 Amount  */  
   NonDeductRpt2Amt:number,
      /**  Non Deductable Rpt3 Amount  */  
   NonDeductRpt3Amt:number,
      /**  Asset Type Code  */  
   AssetTypeCode:string,
      /**  Cash  */  
   Cash:boolean,
      /**  Credit Card  */  
   CreditCard:boolean,
      /**  Normal  */  
   Normal:boolean,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  Bank Transaction Date  */  
   BankTransDate:string,
      /**  Payee  */  
   Payee:string,
      /**  AccountNumber  */  
   AccountNumber:string,
      /**  OtherDetails  */  
   OtherDetails:string,
      /**  MandateReference  */  
   MandateReference:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  SEPADDExportDate  */  
   SEPADDExportDate:string,
      /**  BOE Invoice Number  */  
   BOEInvoiceNum:number,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  OwnReference  */  
   OwnReference:string,
      /**  DocumentType  */  
   DocumentType:string,
      /**  ABTUID  */  
   ABTUID:string,
      /**  BankRcptExchangeRate10D  */  
   BankRcptExchangeRate10D:number,
      /**  SettlementExchangeRate10D  */  
   SettlementExchangeRate10D:number,
      /**  Indicates that cash receipt is currently excluded from batch in Bank Statement Processing.  */  
   BankBatchExcluded:boolean,
      /**  BankBatchSysRowID  */  
   BankBatchSysRowID:string,
      /**  PayMethodReference  */  
   PayMethodReference:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  OnAccount  */  
   OnAccount:boolean,
      /**  MX Receipt’s Fiscal Folio (UUID)  */  
   MXFiscalFolio:string,
      /**  For TranType = "PayInv" it is true only if ARSyst.AllowSettlementInDiffCurr is true. For other types it is true always.  */  
   AllowUpdSettlementCurr:boolean,
   ApplyDate:string,
      /**  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   AVSAddr:string,
      /**  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   AVSZip:string,
   BankAcctDesc:string,
      /**  The Bank's full name.  */  
   BankAcctIDBankName:string,
      /**  Bank Currency Value  */  
   BankAmount:number,
   BankBaseXRateLabel:string,
   BankCurrencyCode:string,
      /**  Bank Currency Symbol  */  
   BankCurrSymbol:string,
   BankExchangeRate:number,
   BankRcptXRateLabel:string,
   BaseCurrencyCode:string,
   BaseCurrSymbol:string,
      /**  Bill To Name  */  
   BillToName:string,
      /**  Indicates if rate was calculated from TranAmt fields instead of CurrExRate table  */  
   calcRate:boolean,
      /**  Stored Credit Card Number  */  
   CardStore:string,
      /**  The credit card description. For example, American Express, Visa, Master Card, Discover, etc.  */  
   CardTypeDescription:string,
      /**  Description  */  
   CashbookLineDescription:string,
      /**  Field to enable/disable the Sale and Deposit Buttons in the Credit Card Tab. This button will depend in the status of the AllowDepPay in CreditCardProc.  */  
   CCAllowSales:boolean,
   CCApprovalNum:string,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  */  
   CCCSCID:string,
      /**  Field to enable/disable the Customer Address fields in the Credit Card Tab. This button will depend in the status of the UseAVSin CreditCardProc.  */  
   CCEnableAddress:boolean,
      /**  s fields in the Credit Card Tab. This button will depend in the status of the UseCSC in CreditCardProc.  */  
   CCEnableCSC:boolean,
      /**  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  */  
   CCResponse:string,
      /**  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  */  
   CCTranID:string,
      /**  Credit Card Transaction Type  */  
   CCTranType:string,
      /**  Description of the currency  */  
   CMCurrencyCodeCurrDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CMCurrencyCodeCurrencyID:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CMCurrencyCodeCurrName:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CMCurrencyCodeCurrSymbol:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CMCurrencyCodeDocumentDesc:string,
      /**  Customer Credit Hold flag  */  
   CreditHold:boolean,
      /**  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   CSCResult:string,
      /**  Description of the currency  */  
   CurrencyCodeCurrDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCodeCurrencyID:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCodeCurrName:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCodeCurrSymbol:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyCodeDocumentDesc:string,
   CurrencySwitch:boolean,
   CustFullAddr:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustNumBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustNumCustID:string,
      /**  The full name of the customer.  */  
   CustNumName:string,
   CustomerName:string,
      /**  Display GL Account  */  
   DispGLAcct:string,
   DocDiscount:number,
   DocReceipt:number,
      /**  Transaction Amount less Tax Amount  */  
   DocTranTaxAmt:number,
      /**  Document number: Invoice Number if source document is AR Invoice or HeadNum if source document is Deposit Payment.  */  
   DocumentNum:number,
      /**  Amount of Credit Memo in CM Currency.  */  
   DspCMAmount:number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user enters this amount and then it is used as a limit/control when applying it to the invoices.  */  
   DspDocTranAmt:number,
   DspSalesOrderValue:number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  */  
   DspTranAmt:number,
   EnableTransactionDate:boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  */  
   FullyPaid:boolean,
      /**  The InvcHead legal number  */  
   InvcLegalNumber:string,
      /**  The member's name on the credit card.  */  
   InvoiceNumCardMemberName:string,
      /**  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   InvoiceNumTermsCode:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
   LegalNumberDsp:string,
   LegalNumMessage:string,
      /**  Copied from OrderHed.LockRate  */  
   LockRate:boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  The member's name on the credit card.  */  
   OrderNumCardMemberName:string,
      /**  A unique code that identifies the currency.  */  
   OrderNumCurrencyCode:string,
   PaymentMethod:string,
      /**  Description  */  
   RateGrpDescription:string,
      /**  Description of the currency  */  
   RcptCurrencyCodeCurrDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   RcptCurrencyCodeCurrencyID:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   RcptCurrencyCodeCurrName:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   RcptCurrencyCodeCurrSymbol:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   RcptCurrencyCodeDocumentDesc:string,
      /**  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  */  
   ReferencePNRef:string,
      /**  Transaction Amount less Tax Amount  */  
   Rpt1TranTaxAmt:number,
      /**  Transaction Amount less Tax Amount  */  
   Rpt2TranTaxAmt:number,
      /**  Transaction Amount less Tax Amount  */  
   Rpt3TranTaxAmt:number,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
   SalesOrderValue:number,
   SettlementXRateLabel:string,
      /**  Name of the Sold To customer if this is a Deposit (created using an OrderHed).  */  
   SoldToCustomerName:string,
      /**  Full description for the Tax Region.  */  
   TaxRegionCodeDescription:string,
      /**  Sum of all rounding differences of the payments for one Cash Receipt and one Check  */  
   TotalRoundDiff:number,
      /**  Transaction Amount less Tax Amount  */  
   TranTaxAmt:number,
      /**  Description of TranType  */  
   TranTypeDesc:string,
      /**  Yes if Cash Receipt has Unapplied amount but credit memo is applied.  */  
   UnappliedAmountApplied:boolean,
   XRateLabel:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Displays the ID of the group the transaction is assigned to.  */  
   GroupID:string,
      /**  Displays the receipt header number used for internal reference.  */  
   HeadNum:number,
      /**  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   Posted:boolean,
      /**  Displays the transaction type.  */  
   TranType:string,
      /**  Displays the number of the check.  */  
   CheckRef:string,
      /**  Sales Order #.  This is only used by the PrePay transaction. It must be a valid order found in OrderHed.  */  
   OrderNum:number,
      /**  The invoice # that is to be adjusted or the invoice number of a credit memo that is to be applied. This field is only used when TranType = CMemo or Adjust. It must be a valid open invoice memo found in the InvcHead file.  */  
   InvoiceNum:number,
      /**  Displays the transaction amount.  */  
   TranAmt:number,
      /**  Displays the transaction amount in customer currency.  */  
   DocTranAmt:number,
      /**  Displays the customer ID.  */  
   CustID:string,
      /**  Displays the date of the transaction.  */  
   TranDate:string,
      /**  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  */  
   CustNum:number,
      /**  Displays the unapplied amount.  */  
   UnAppliedAmt:number,
      /**  Displays the unapplied amount in base currency.  */  
   DocUnAppliedAmt:number,
      /**  Displays the amount applied to invoices.  */  
   AppliedAmt:number,
      /**  Displays the amount in document currency applied to invoices.  */  
   DocAppliedAmt:number,
      /**  Displays the fiscal year that the check is posted to.  */  
   FiscalYear:number,
      /**  Displays the fiscal period that the check is posted to.  */  
   FiscalPeriod:number,
      /**  Displays any reference.  */  
   Reference:string,
      /**  Indicates if this transaction has been posted.  */  
   GLPosted:boolean,
      /**  The invoice number that was used to create the credit memo for the unapplied cash receipt. This is updated during the cash receipt posting process and is used to link to the invchead.  */  
   CreditMemoNum:number,
      /**  Displays the customer currency.  */  
   CurrencyCode:string,
      /**  Displays the exchange rate that is used for this check.  */  
   ExchangeRate:number,
      /**  The Tax Region for this payment.  */  
   TaxRegionCode:string,
      /**  Total Tax Amount.  */  
   TaxAmt:number,
      /**  Displays the tax amount.  */  
   DocTaxAmt:number,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  This field identifies a line of a bankslip.  */  
   CashbookLine:number,
      /**  Displays the legal number of the check.  */  
   LegalNumber:string,
      /**  External ID  */  
   ExternalID:string,
      /**  Link to the related GLRefTyp.RefType.  */  
   GLRefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   GLRefCode:string,
      /**  The member's name on the credit card.  */  
   CardMemberName:string,
      /**  The credit card account identifier.  */  
   CardNumber:string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   CardType:string,
      /**  The expiration month of the credit card.  */  
   ExpirationMonth:number,
      /**  The expiration year of the credit card.  */  
   ExpirationYear:number,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  */  
   CardID:string,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   CardmemberReference:string,
      /**  Stores the encrypted credit card number  */  
   ProcessCard:string,
      /**  Credit Transaction Amount, makes up part of CCTotal  */  
   CCAmount:number,
      /**  Credit Card transaction freight amount, part of CCTotal  */  
   CCFreight:number,
      /**  Credit Card Transaction Tax amount, part of CCTotal  */  
   CCTax:number,
      /**  Total amount being sent to the credit card processor  */  
   CCTotal:number,
      /**  See CCAmount  */  
   CCDocAmount:number,
      /**  See CCFreight  */  
   CCDocFreight:number,
      /**  See CCTax  */  
   CCDocTax:number,
      /**  See CCTotal  */  
   CCDocTotal:number,
      /**  Address used during AVS validation for credit transactions  */  
   CCStreetAddr:string,
      /**  Zip used during AVS validation in credit transactions  */  
   CCZip:string,
      /**  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available. If this flag is yes the check amount is 0 (no cash processed) and the check number is not assigned by the user.  */  
   DebNoteOnly:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1AppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2AppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3AppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnAppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnAppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnAppliedAmt:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Amount of deposit applied  */  
   DocDepApplied:number,
      /**  See CCAmount  */  
   Rpt1CCAmount:number,
      /**  See CCAmount  */  
   Rpt2CCAmount:number,
      /**  See CCAmount  */  
   Rpt3CCAmount:number,
      /**  See CCFreight  */  
   Rpt1CCFreight:number,
      /**  See CCFreight  */  
   Rpt2CCFreight:number,
      /**  See CCFreight  */  
   Rpt3CCFreight:number,
      /**  See CCTax  */  
   Rpt1CCTax:number,
      /**  See CCTax  */  
   Rpt2CCTax:number,
      /**  See CCTax  */  
   Rpt3CCTax:number,
      /**  See CCTotal  */  
   Rpt1CCTotal:number,
      /**  See CCTotal  */  
   Rpt2CCTotal:number,
      /**  See CCTotal  */  
   Rpt3CCTotal:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  Withholding Tax Amount.  */  
   WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   DocWithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt1WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt2WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt3WithholdAmt:number,
      /**  Self Assessment Tax Amount.  */  
   SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   DocSelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt1SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt2SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt3SelfAssessAmt:number,
      /**  The unique code of Receipt Currency.  */  
   ReceiptCurrencyCode:string,
      /**  Amount of Receipt in Receipt Currency.  */  
   ReceiptAmt:number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Bank Currency.  */  
   BankRcptExchangeRate:number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Settlement Currency.  */  
   SettlementExchangeRate:number,
      /**  The unique Currency code for Credit Memo.  */  
   CMCurrencyCode:string,
      /**  Amount of Credit Memo in CM Currency.  */  
   CMAmount:number,
      /**  Reference to cash receipt which had been reversed.  */  
   ReverseRef:number,
      /**  Date when cash receipt had been reversed  */  
   ReverseDate:string,
      /**  Bank Account ID  */  
   BankAcctID:string,
      /**  Withhold Tax  */  
   TaxWhld:number,
      /**  Dsicount Date  */  
   DiscountDate:string,
      /**  Calculate Withhold Tax  */  
   TaxWhldCalc:number,
      /**  Addition to Contract  */  
   ContractDate:string,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   Plant:string,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Base currency.  */  
   UnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Document currency.  */  
   DocUnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt1 currency.  */  
   Rpt1UnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt2 currency.  */  
   Rpt2UnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt3 currency.  */  
   Rpt3UnallocatedAmt:number,
      /**  Number of the unallocated deposit payment to be apply.  */  
   ApplyHeadNum:number,
      /**  Used during the allocation process of the unallocated deposit payment. Base currency.  */  
   AllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Document currency.  */  
   DocAllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt1 currency.  */  
   Rpt1AllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt2 currency.  */  
   Rpt2AllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt3 currency.  */  
   Rpt3AllocatedAmt:number,
      /**  Comments related to the cash receipt.  */  
   Comment:string,
      /**  Payment Method Unique Identifier  */  
   PMUID:number,
      /**  Unique identifier of Petty Cash Desk  */  
   PCashDeskID:string,
      /**  ID Given by the Bank assigned during matching  */  
   BankTranID:string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   PCashRefNum:number,
      /**  Transaction Document Type for the record.  */  
   TranDocTypeID:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**  Site Code  */  
   SiteCode:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Invoice Date  */  
   InvoiceDate:string,
      /**  Tax Remarks  */  
   TaxRemarks:string,
      /**  Non Deductable Code  */  
   NonDeductCode:string,
      /**  Non Deductable Amount  */  
   NonDeductAmt:number,
      /**  Non Deductable Doc Amount  */  
   NonDeductDocAmt:number,
      /**  Non Deductable Rpt1 Amount  */  
   NonDeductRpt1Amt:number,
      /**  Non Deductable Rpt2 Amount  */  
   NonDeductRpt2Amt:number,
      /**  Non Deductable Rpt3 Amount  */  
   NonDeductRpt3Amt:number,
      /**  Asset Type Code  */  
   AssetTypeCode:string,
      /**  Cash  */  
   Cash:boolean,
      /**  Credit Card  */  
   CreditCard:boolean,
      /**  Normal  */  
   Normal:boolean,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  Bank Transaction Date  */  
   BankTransDate:string,
      /**  Payee  */  
   Payee:string,
      /**  AccountNumber  */  
   AccountNumber:string,
      /**  OtherDetails  */  
   OtherDetails:string,
      /**  MandateReference  */  
   MandateReference:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  SEPADDExportDate  */  
   SEPADDExportDate:string,
      /**  BOE Invoice Number  */  
   BOEInvoiceNum:number,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  OwnReference  */  
   OwnReference:string,
      /**  DocumentType  */  
   DocumentType:string,
      /**  ABTUID  */  
   ABTUID:string,
      /**  BankRcptExchangeRate10D  */  
   BankRcptExchangeRate10D:number,
      /**  SettlementExchangeRate10D  */  
   SettlementExchangeRate10D:number,
      /**  Indicates that cash receipt is currently excluded from batch in Bank Statement Processing.  */  
   BankBatchExcluded:boolean,
      /**  BankBatchSysRowID  */  
   BankBatchSysRowID:string,
      /**  PayMethodReference  */  
   PayMethodReference:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  OnAccount  */  
   OnAccount:boolean,
      /**  The amount of the cash receipt applied to invoices in receipt currency  */  
   RcptCurAppliedAmt:number,
      /**  The amount of the cash receipt that is unapplied in receipt currency  */  
   RcptCurUnAppliedAmt:number,
      /**  MXAccountNumber  */  
   MXAccountNumber:string,
      /**  MX Method of Payment: single, multiple, etc.  */  
   MXPaidAs:string,
      /**  If TRUE then MX Electronic Payment XML is required  */  
   MXPaySupplementFlag:boolean,
      /**  LockboxID  */  
   LockboxID:string,
      /**  MX Receipt’s Fiscal Folio (UUID)  */  
   MXFiscalFolio:string,
      /**  MX UUID of the original Receipt being corrected  */  
   MXOriginalCheckRef:string,
      /**  MX Confirmation Code for special Cash Receipts  */  
   MXConfirmationCode:string,
      /**  MX Customer’s Bank ID  */  
   MXBankID:string,
      /**  Text entered by the user to indicate the reason Cash receipt was Reversed.  */  
   ReversedReason:string,
      /**  Credit Card Holder City.  */  
   CCCity:string,
      /**  Credit Card Holder State.  */  
   CCState:string,
      /**  ccToken  */  
   ccToken:string,
      /**  DepositBalance  */  
   DepositBalance:number,
      /**  DocDepositBalance  */  
   DocDepositBalance:number,
      /**  Rpt1DepositBalance  */  
   Rpt1DepositBalance:number,
      /**  Rpt2DepositBalance  */  
   Rpt2DepositBalance:number,
      /**  Rpt3DepositBalance  */  
   Rpt3DepositBalance:number,
      /**  Indicates this record is an adjustment CashHead.  */  
   Adjustment:boolean,
      /**  Reference to cash receipt which had been adjusted.  */  
   AdjustmentRef:number,
      /**  The reason for the adjustment entered by the user  */  
   AdjustmentReason:string,
      /**  Total Check Write Off Amount  */  
   WriteOffAmount:number,
      /**  DocWriteOffAmount  */  
   DocWriteOffAmount:number,
      /**  Rpt1WriteOffAmount  */  
   Rpt1WriteOffAmount:number,
      /**  Rpt2WriteOffAmount  */  
   Rpt2WriteOffAmount:number,
      /**  Rpt3WriteOffAmount  */  
   Rpt3WriteOffAmount:number,
      /**  Mexico Certified Timestamp  */  
   MXCertifiedTimestamp:string,
      /**  Mexico SAT Seal  */  
   MXSATSeal:string,
      /**  Mexico Digital Seal  */  
   MXDigitalSeal:string,
      /**  Mexico SAT Certificate Serial Number  */  
   MXSATCertificateSN:string,
      /**  Mexico Original String Timbre Fiscal Digital  */  
   MXOriginalStringTFD:string,
      /**  Mexico Certificate  */  
   MXCertificate:string,
      /**  Mexico Certificate Serial Number  */  
   MXCertificateSN:string,
      /**  SourceGroupID  */  
   SourceGroupID:string,
      /**  SourceHeadNum  */  
   SourceHeadNum:number,
      /**  Standard Entry Class Code  */  
   SEC:string,
      /**  ACH Transaction Code  */  
   ACHTranCode:number,
      /**  ID of the Customer's bank.  */  
   CustomerBankID:string,
      /**  The Bank account number for the Customer.  */  
   CustomerBankAcctNumber:string,
      /**  CustomerBankSwiftNum  */  
   CustomerBankSwiftNum:string,
      /**  The Bank account IBAN Code  */  
   CustomerBankIBANCode:string,
      /**  Name on the Bank Account.  */  
   CustomerBankNameOnAccount:string,
      /**  First address line of customer bank.  */  
   CustomerBankAddress1:string,
      /**  Second address line of customer bank.  */  
   CustomerBankAddress2:string,
      /**  Third address line of customer bank.  */  
   CustomerBankAddress3:string,
      /**  Bank City  */  
   CustomerBankCity:string,
      /**  Bank State/Prov  */  
   CustomerBankState:string,
      /**  Postal Code or zip code  */  
   CustomerBankPostalCode:string,
      /**  Bank account Country Number.  */  
   CustomerBankCountryNum:number,
      /**  ARRemittanceSlipPrinted  */  
   ARRemittanceSlipPrinted:boolean,
      /**  Customer Bank Name  */  
   CustomerBankName:string,
      /**  MXPostedTimeStamp  */  
   MXPostedTimeStamp:string,
      /**  MXSerie  */  
   MXSerie:string,
      /**  MXFolio  */  
   MXFolio:string,
      /**  MXEPaymentType  */  
   MXEPaymentType:string,
      /**  MXEPaymentCertificateNumber  */  
   MXEPaymentCertificateNumber:string,
      /**  MXEPaymentOriginalString  */  
   MXEPaymentOriginalString:string,
      /**  MXEPaymentDigitalSeal  */  
   MXEPaymentDigitalSeal:string,
      /**  Source  */  
   Source:string,
      /**  Id of the netting transaction that generated this document.  */  
   NettingID:number,
      /**  GL Description for the Reverse process  */  
   RevDescription:string,
      /**  GL Description for AR - Apply Credit Memo  */  
   CMDescription:string,
      /**  Receipt Amount in Bank Currency  */  
   BankReceiptAmt:number,
      /**  MXCancelReasonCode  */  
   MXCancelReasonCode:string,
      /**  MXSubstHeadNum  */  
   MXSubstHeadNum:number,
      /**  MXCancellationMode  */  
   MXCancellationMode:string,
      /**  E-invoice error description.  */  
   ELIEInvException:string,
      /**  EInvoice ID  */  
   ELIEInvID:string,
      /**  E-invoice  */  
   ELIEInvoice:boolean,
      /**  E-invoice Service Provider Status  */  
   ELIEInvServiceProviderStatus:number,
      /**  E-invoice Status  */  
   ELIEInvStatus:number,
      /**  User Id of the person generated E-invoice.  */  
   ELIEInvUpdatedBy:string,
      /**  E-invoice Updated On  */  
   ELIEInvUpdatedOn:string,
      /**  Adjustment Customer Name  */  
   AdjustmentCustName:string,
      /**  Customer to which the new invoices will be applied.  */  
   AdjustmentCustNum:number,
      /**  Date the adjustment was made.  */  
   AdjustmentDate:string,
      /**  Displays the amount available to apply to the invoices.  */  
   AdjustmentDocUnAppliedAmt:number,
      /**  On Account  */  
   AdjustmentOnAccount:boolean,
      /**  Temp TranDocTypeID used when adjusting a Cash Rececipt  */  
   AdjustmentTranDocTypeID:string,
   AllocDepBal:number,
   AllowChgAfterPrint:boolean,
      /**  For TranType = "PayInv" it is true only if ARSyst.AllowSettlementInDiffCurr is true. For other types it is true always.  */  
   AllowUpdSettlementCurr:boolean,
      /**  Amount to Allocate  */  
   AmtToAlloc:number,
   ApplyDate:string,
      /**  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   AVSAddr:string,
      /**  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   AVSZip:string,
      /**  Bank Currency Value  */  
   BankAmount:number,
   BankBaseXRateLabel:string,
   BankCurrencyCode:string,
      /**  Bank Currency Symbol  */  
   BankCurrSymbol:string,
   BankExchangeRate:number,
   BankRcptXRateLabel:string,
   BaseCurrencyCode:string,
      /**  Base Currency Symbol  */  
   BaseCurrSymbol:string,
      /**  Bill To Name  */  
   BillToName:string,
      /**  Indicates if rate was calculated from TranAmt fields instead of CurrExRate table  */  
   calcRate:boolean,
      /**  Stored Credit Card Number  */  
   CardStore:string,
      /**  Field to enable/disable the Sale and Deposit Buttons in the Credit Card Tab. This button will depend in the status of the AllowDepPay in CreditCardProc.  */  
   CCAllowSales:boolean,
   CCApprovalNum:string,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  */  
   CCCSCID:string,
      /**  Tokenized value of CSCID  */  
   CCCSCIDToken:string,
      /**  Field to enable/disable the Customer Address fields in the Credit Card Tab. This button will depend in the status of the UseAVSin CreditCardProc.  */  
   CCEnableAddress:boolean,
      /**  s fields in the Credit Card Tab. This button will depend in the status of the UseCSC in CreditCardProc.  */  
   CCEnableCSC:boolean,
      /**   Indicates if the credit card setup will be using a testing Paygate instance for transactions.
Force requests to use Paygate test url: paygate-test1.eaglesoa.com  */  
   CCIsTraining:boolean,
      /**  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  */  
   CCResponse:string,
      /**  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  */  
   CCTranID:string,
      /**  Credit Card Transaction Type  */  
   CCTranType:string,
      /**  Check Box on the UI to filter records by Central Collection flag  */  
   CentralCollectionCheck:boolean,
      /**  If the user selects Credit Memo/Correction Invoice document type this flag indicates that this is Correction Invoice with negative amount  */  
   CorrectionInv:boolean,
      /**  Customer Credit Hold flag  */  
   CreditHold:boolean,
      /**  If the user selects Credit Memo/Correction Invoice document type this flag indicates that this is Credit Memo  */  
   CreditMemo:boolean,
      /**  CREProcessor is true when Credit Card Configuration is CRE Server.  */  
   CREProcessor:boolean,
      /**  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   CSCResult:string,
      /**  Current Amount Selected on Invoice Select Tab  */  
   CurrAmtSelected:number,
   CurrencySwitch:boolean,
      /**  Displays the address of the customer that paid the receipt.  */  
   CustFullAddr:string,
   CustomerName:string,
   DisableFieldsForPCashDoc:boolean,
      /**  Display GL Account  */  
   DispGLAcct:string,
   DocAllocDepBal:number,
      /**  Doc Amount to Allocate  */  
   DocAmtToAlloc:number,
      /**  Displays the discount applied to the receipt.  */  
   DocDiscount:number,
      /**  Displays the invoice amount paid by this receipt. The amount includes both discount and payment amounts.  */  
   DocReceipt:number,
      /**  Transaction Amount less Tax Amount  */  
   DocTranTaxAmt:number,
      /**  Document number: Invoice Number if source document is AR Invoice or HeadNum if source document is Deposit Payment.  */  
   DocumentNum:number,
   DocWhldTax:number,
   DspBankBatchID:string,
      /**  Amount of Credit Memo in CM Currency.  */  
   DspCMAmount:number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  */  
   DspDocTranAmt:number,
   DspSalesOrderValue:number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  */  
   DspTranAmt:number,
   EnableAssignLegNum:boolean,
      /**  Indicates if the option to get the default account is enable.  */  
   EnableGetDefaultAcct:boolean,
   EnableTranDocType:boolean,
   EnableTransactionDate:boolean,
   EnableVoidLegNum:boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  */  
   FullyPaid:boolean,
   GLRefCodeDescription:string,
   HasLegNumCnfg:boolean,
      /**  The InvcHead legal number  */  
   InvcLegalNumber:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
   LegalNumberDsp:string,
   LegalNumMessage:string,
      /**  Copied from OrderHed.LockRate  */  
   LockRate:boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
   ManualTaxAdj:boolean,
      /**  MXCancellationID  */  
   MXCancellationID:string,
   MXCancellationStatus:string,
      /**  MXECEPXml  */  
   MXECEPXml:string,
      /**  Mexico Calculated field - shows Check Reference number of the original Receipt being corrected  */  
   MXOriginalRefNum:string,
      /**  Host Address for the Paygate Hosted Token Service.  */  
   PayGateHostAddress:string,
      /**  NameSpace for the Paygate Hosted Token Service.  */  
   PayGateNameSpace:string,
      /**  Public Key for the Paygate Hosted Token Service EWA component.  */  
   PayGatePublicKey:string,
      /**  This column is used within cash receipt tracker to show either the receipt date or the source/ original receipt date if the cash receipt has been adjusted.  */  
   ReceiptDate:string,
      /**  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  */  
   ReferencePNRef:string,
   Rpt1AllocDepBal:number,
      /**  Transaction Amount less Tax Amount  */  
   Rpt1TranTaxAmt:number,
   Rpt1WhldTax:number,
   Rpt2AllocDepBal:number,
      /**  Transaction Amount less Tax Amount  */  
   Rpt2TranTaxAmt:number,
   Rpt2WhldTax:number,
   Rpt3AllocDepBal:number,
      /**  Transaction Amount less Tax Amount  */  
   Rpt3TranTaxAmt:number,
   Rpt3WhldTax:number,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
   SalesOrderValue:number,
   SettlementXRateLabel:string,
      /**  Name of the Sold To customer if this is a Deposit (created using an OrderHed).  */  
   SoldToCustomerName:string,
   SystemTranType:string,
      /**  Sum of all rounding differences of the payments for one Cash Receipt and one Check  */  
   TotalRoundDiff:number,
      /**  Transaction Amount less Tax Amount  */  
   TranTaxAmt:number,
      /**  Description of TranType  */  
   TranTypeDesc:string,
      /**  Yes if Cash Receipt has Unapplied amount but credit memo is applied.  */  
   UnappliedAmountApplied:boolean,
   WhldTax:number,
   XRateLabel:string,
      /**  Displays the customer ID.  */  
   AdjustmentCustID:string,
   ReferenceTranDate:string,
   ReferenceTranNum:number,
   ReferenceTranTime:number,
      /**  Displays the address of the customer that paid the receipt with newline delimiter.  */  
   CustFullAddrFormatted:string,
      /**  Indicates if the user can manually modify the applied withholding tax of the invoice. Used in Apply Credit Memo when withholding tax was not posted through an interim account.  */  
   EnableManualWHTax:boolean,
      /**  Indicates if the withholding tax was manually modified.  */  
   WHTaxManualChange:boolean,
      /**  Payment type description, displayed in the Details page header.  */  
   TranTypeDescCaption:string,
   AdjustmentCustAddress:string,
      /**  Substitution Cash Receipt Group ID  */  
   MXSubstGroupId:string,
      /**  Substitution Cash Receipt CheckRef  */  
   MXSubstCheckRef:string,
      /**  Substitution Cash Receipt UUID  */  
   MXSubstFiscalFolio:string,
   BitFlag:number,
   BankAcctIDDescription:string,
   BankAcctIDBankName:string,
   CardTypeDescription:string,
   CashBHedPosted:boolean,
   CashBHedCashBookNum:number,
   CashbookLineDescription:string,
   CMCurrencyCodeDocumentDesc:string,
   CMCurrencyCodeCurrName:string,
   CMCurrencyCodeCurrSymbol:string,
   CMCurrencyCodeCurrDesc:string,
   CMCurrencyCodeCurrencyID:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
   CustNumInactive:boolean,
   CustNumName:string,
   CustNumBTName:string,
   CustNumCustID:string,
   InvoiceNumTermsCode:string,
   InvoiceNumCardMemberName:string,
   OrderNumCardMemberName:string,
   OrderNumCurrencyCode:string,
   PCashDocDirection:string,
   PMUIDName:string,
   PMUIDMXSATCode:string,
   PMUIDSummarizePerCustomer:boolean,
   PMUIDType:number,
   RateGrpDescription:string,
   RcptCurrencyCodeCurrencyID:string,
   RcptCurrencyCodeDocumentDesc:string,
   RcptCurrencyCodeCurrDesc:string,
   RcptCurrencyCodeCurrSymbol:string,
   RcptCurrencyCodeCurrName:string,
   ReverseMXCancelReasonCode:string,
   ReverseMXCancellationMode:string,
   SourceTranDateTranDate:string,
   TaxRegionCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashHeadSearchListTableset{
   CashHeadList:Erp_Tablesets_CashHeadListRow[],
   CashHeadListAttch:Erp_Tablesets_CashHeadListAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CashHeadSearchTableset{
   CashHead:Erp_Tablesets_CashHeadRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtCashHeadSearchTableset{
   CashHead:Erp_Tablesets_CashHeadRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param groupID
      @param headNum
   */  
export interface GetByID_input{
   groupID:string,
   headNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CashHeadSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CashHeadSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CashHeadSearchTableset[],
}

   /** Required : 
      @param groupID
      @param headNum
      @param maxNumOfCards
   */  
export interface GetCashReceiptRelationshipMap_input{
   groupID:string,
   headNum:number,
   maxNumOfCards:number,
}

export interface GetCashReceiptRelationshipMap_output{
   returnObj:string,
}

   /** Required : 
      @param checkRef
   */  
export interface GetGroupHeadQuery_input{
   checkRef:string,
}

export interface GetGroupHeadQuery_output{
   returnObj:Erp_Tablesets_CashHeadSearchListTableset[],
}

   /** Required : 
      @param whereClause
      @param startingAtValue
      @param pageSize
      @param absolutePage
   */  
export interface GetListByInvoiceWhereClause_input{
      /**  Full where clause  */  
   whereClause:string,
      /**  Value to filter the start of the results  */  
   startingAtValue:string,
      /**  Page Size  */  
   pageSize:number,
      /**  Absolute Page  */  
   absolutePage:number,
}

export interface GetListByInvoiceWhereClause_output{
   returnObj:Erp_Tablesets_CashHeadSearchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseVendorPP
      @param pmUID
      @param custId
      @param bankAcctID
      @param tranType
      @param fromDate
      @param toDate
      @param invoiceNum
      @param checkRef
      @param startingAt
      @param startingAtValue
      @param mandateRef
      @param pageSize
      @param absolutePage
      @param multipleChecks
   */  
export interface GetListByInvoice_input{
   whereClauseVendorPP:string,
   pmUID:number,
   custId:string,
   bankAcctID:string,
   tranType:string,
   fromDate:string,
   toDate:string,
   invoiceNum:number,
   checkRef:string,
   startingAt:string,
   startingAtValue:string,
   mandateRef:string,
   pageSize:number,
   absolutePage:number,
   multipleChecks:boolean,
}

export interface GetListByInvoice_output{
   returnObj:Erp_Tablesets_CashHeadSearchListTableset[],
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
   returnObj:Erp_Tablesets_CashHeadSearchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param groupID
   */  
export interface GetNewCashHead_input{
   ds:Erp_Tablesets_CashHeadSearchTableset[],
   groupID:string,
}

export interface GetNewCashHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashHeadSearchTableset,
}
}

   /** Required : 
      @param whereClauseCashHead
      @param invoiceNum
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForInvoice_input{
   whereClauseCashHead:string,
   invoiceNum:number,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsForInvoice_output{
   returnObj:Erp_Tablesets_CashHeadSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseCashHead
      @param quoteNum
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForQuote_input{
   whereClauseCashHead:string,
   quoteNum:number,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsForQuote_output{
   returnObj:Erp_Tablesets_CashHeadSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseCashHead
      @param orderNum
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForSalesOrder_input{
   whereClauseCashHead:string,
   orderNum:number,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsForSalesOrder_output{
   returnObj:Erp_Tablesets_CashHeadSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseCashHead
      @param packNum
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForShipment_input{
   whereClauseCashHead:string,
   packNum:number,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsForShipment_output{
   returnObj:Erp_Tablesets_CashHeadSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseCashHead
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCashHead:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CashHeadSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtCashHeadSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCashHeadSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CashHeadSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashHeadSearchTableset,
}
}

