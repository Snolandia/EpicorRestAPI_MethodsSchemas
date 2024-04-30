import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ContractRenewalSearchSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/$metadata", {
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
   Description: Get ContractRenewalSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContractRenewalSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContractRenewalSearchRow
   */  
export function get_ContractRenewalSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContractRenewalSearchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/ContractRenewalSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContractRenewalSearchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContractRenewalSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ContractRenewalSearchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ContractRenewalSearchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ContractRenewalSearches(requestBody:Erp_Tablesets_ContractRenewalSearchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/ContractRenewalSearches", {
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
   Summary: Calls GetByID to retrieve the ContractRenewalSearch item
   Description: Calls GetByID to retrieve the ContractRenewalSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContractRenewalSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param RenewalNbr Desc: RenewalNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ContractRenewalSearchRow
   */  
export function get_ContractRenewalSearches_Company_ContractNum_RenewalNbr(Company:string, ContractNum:string, RenewalNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ContractRenewalSearchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/ContractRenewalSearches(" + Company + "," + ContractNum + "," + RenewalNbr + ")", {
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
         resolve(data as Erp_Tablesets_ContractRenewalSearchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ContractRenewalSearch for the service
   Description: Calls UpdateExt to update ContractRenewalSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContractRenewalSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param RenewalNbr Desc: RenewalNbr   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ContractRenewalSearchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ContractRenewalSearches_Company_ContractNum_RenewalNbr(Company:string, ContractNum:string, RenewalNbr:string, requestBody:Erp_Tablesets_ContractRenewalSearchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/ContractRenewalSearches(" + Company + "," + ContractNum + "," + RenewalNbr + ")", {
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
   Summary: Call UpdateExt to delete ContractRenewalSearch item
   Description: Call UpdateExt to delete ContractRenewalSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContractRenewalSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param RenewalNbr Desc: RenewalNbr   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ContractRenewalSearches_Company_ContractNum_RenewalNbr(Company:string, ContractNum:string, RenewalNbr:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/ContractRenewalSearches(" + Company + "," + ContractNum + "," + RenewalNbr + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContractRenewalSearchListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContractRenewalSearchListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContractRenewalSearchListRow)
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
export function get_GetRows(whereClauseContractRenewalSearch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseContractRenewalSearch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseContractRenewalSearch=" + whereClauseContractRenewalSearch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/GetRows" + params, {
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
export function get_GetByID(contractNum:string, renewalNbr:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof contractNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "contractNum=" + contractNum
   }
   if(typeof renewalNbr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "renewalNbr=" + renewalNbr
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetRenewals
   Description: Returns the renewals
   OperationID: GetRenewals
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRenewals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRenewals_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRenewals(requestBody:GetRenewals_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRenewals_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/GetRenewals", {
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
         resolve(data as GetRenewals_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewContractRenewalSearch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContractRenewalSearch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewContractRenewalSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContractRenewalSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewContractRenewalSearch(requestBody:GetNewContractRenewalSearch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewContractRenewalSearch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/GetNewContractRenewalSearch", {
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
         resolve(data as GetNewContractRenewalSearch_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContractRenewalSearchListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ContractRenewalSearchListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContractRenewalSearchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ContractRenewalSearchRow,
}

export interface Erp_Tablesets_ContractRenewalSearchListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   "ContractNum":number,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   "RenewalNbr":number,
      /**  Indicates if the renwal will automatically generate a quote.  */  
   "QuotedRenewal":boolean,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   "QuoteNum":number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   "QuoteLine":number,
      /**  Indicates the Quote has been accepted.  */  
   "QuoteAccepted":boolean,
      /**  This is the contract code assigned to the renewal.  */  
   "RenewalCode":string,
      /**  Defaulted from the service contract code.  Determines whether or not the renewal can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  */  
   "ShipRenewal":boolean,
      /**  Revenue Amortization Code.  */  
   "RACode":string,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   "DeferredRev":boolean,
      /**  Starting date the revenue is deferred.  */  
   "DefRevStart":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  */  
   "Invoiced":boolean,
      /**  The invoice number of the last recurring invoice.  */  
   "InvoiceNum":number,
      /**  Packing slip number that this detail record is linked with.  */  
   "PackNum":number,
      /**  An integer that Ties the Contract record to a packing slip detail line  */  
   "PackLine":number,
      /**  Indicates that Service Contract with this Code will generate recurring invoices.  */  
   "RecurringInv":boolean,
      /**  The frequency that recurring invoices are generated only 'monthly' for now.  */  
   "RecurringFreq":string,
      /**  This flag is set to TRUE after the last recurring invoice is generated for the contract.  */  
   "LastInvGen":boolean,
      /**  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  */  
   "ReadyToInvoice":boolean,
      /**  The Sales order that this contract is linked to.  */  
   "OrderNum":number,
      /**  The line number of the sales order that this contract is linked to  */  
   "OrderLine":number,
      /**  Duration of Contract  */  
   "Duration":number,
      /**  Date when the renewal begins.  */  
   "RenewEffDate":string,
      /**  Date the renewal ends.  */  
   "RenewedUntil":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CustNum":number,
   "CustID":string,
   "CustName":string,
   "CustBTName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ContractRenewalSearchRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   "ContractNum":number,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   "RenewalNbr":number,
      /**  Indicates if the renwal will automatically generate a quote.  */  
   "QuotedRenewal":boolean,
      /**  Unique identifier of the task set assigned by the user.  */  
   "TaskSetID":string,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   "QuoteNum":number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   "QuoteLine":number,
      /**  Indicates the Quote has been accepted.  */  
   "QuoteAccepted":boolean,
      /**  This is the contract code assigned to the renewal.  */  
   "RenewalCode":string,
      /**  Defaulted from the service contract code.  Determines whether or not the renewal can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  */  
   "ShipRenewal":boolean,
      /**  Revenue Amortization Code.  */  
   "RACode":string,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   "DeferredRev":boolean,
      /**  Starting date the revenue is deferred.  */  
   "DefRevStart":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this Contract.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   "LockRate":boolean,
      /**   This is used as one of the selection parameters on the Service Contract entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   "EntryPerson":string,
      /**  Date the renewal was created.  */  
   "EntryDate":string,
      /**  Coverage  for material  */  
   "Material":boolean,
      /**  Coverage for Labor  */  
   "Labor":boolean,
      /**  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  */  
   "Misc":boolean,
      /**  This contract covers on site visits  */  
   "OnSite":boolean,
      /**  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  */  
   "Invoiced":boolean,
      /**  The invoice number of the last recurring invoice.  */  
   "InvoiceNum":number,
      /**  Packing slip number that this detail record is linked with.  */  
   "PackNum":number,
      /**  An integer that Ties the Contract record to a packing slip detail line  */  
   "PackLine":number,
      /**  Indicates that Service Contract with this Code will generate recurring invoices.  */  
   "RecurringInv":boolean,
      /**  The frequency that recurring invoices are generated only 'monthly' for now.  */  
   "RecurringFreq":string,
      /**  Price modifier for unit price field Daily, monthly, Contract(Full length of the contract)  */  
   "PricePer":string,
      /**  This flag is set to TRUE after the last recurring invoice is generated for the contract.  */  
   "LastInvGen":boolean,
      /**  Indicates the Tax Category for this record.  */  
   "TaxCatID":string,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  */  
   "ReadyToInvoice":boolean,
      /**  The Sales order that this contract is linked to.  */  
   "OrderNum":number,
      /**  The line number of the sales order that this contract is linked to  */  
   "OrderLine":number,
      /**  Duration of Contract  */  
   "Duration":number,
      /**  Used to establish invoice comments about the overall Renewal.  */  
   "RenewalComment":string,
      /**  Date when the renewal begins.  */  
   "RenewEffDate":string,
      /**  Date the renewal ends.  */  
   "RenewedUntil":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  InvcTiming  */  
   "InvcTiming":string,
      /**  It is the same as the contract type but applied to renewals  */  
   "ContractCode":string,
      /**  The unit of measure of time that the renewal contract lasts.  */  
   "Modifier":string,
      /**  Indicates how often an invoice is generated for the contract  */  
   "FiscalCalendarID":string,
      /**  Indicates if the service contract is valid for renewal  */  
   "Renewable":boolean,
   "CustID":string,
   "CustName":string,
   "CustNum":number,
   "CustBTName":string,
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
      @param contractNum
      @param renewalNbr
   */  
export interface DeleteByID_input{
   contractNum:number,
   renewalNbr:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ContractRenewalSearchListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   ContractNum:number,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
      /**  Indicates if the renwal will automatically generate a quote.  */  
   QuotedRenewal:boolean,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   QuoteLine:number,
      /**  Indicates the Quote has been accepted.  */  
   QuoteAccepted:boolean,
      /**  This is the contract code assigned to the renewal.  */  
   RenewalCode:string,
      /**  Defaulted from the service contract code.  Determines whether or not the renewal can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  */  
   ShipRenewal:boolean,
      /**  Revenue Amortization Code.  */  
   RACode:string,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   DeferredRev:boolean,
      /**  Starting date the revenue is deferred.  */  
   DefRevStart:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  */  
   Invoiced:boolean,
      /**  The invoice number of the last recurring invoice.  */  
   InvoiceNum:number,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  An integer that Ties the Contract record to a packing slip detail line  */  
   PackLine:number,
      /**  Indicates that Service Contract with this Code will generate recurring invoices.  */  
   RecurringInv:boolean,
      /**  The frequency that recurring invoices are generated only 'monthly' for now.  */  
   RecurringFreq:string,
      /**  This flag is set to TRUE after the last recurring invoice is generated for the contract.  */  
   LastInvGen:boolean,
      /**  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  */  
   ReadyToInvoice:boolean,
      /**  The Sales order that this contract is linked to.  */  
   OrderNum:number,
      /**  The line number of the sales order that this contract is linked to  */  
   OrderLine:number,
      /**  Duration of Contract  */  
   Duration:number,
      /**  Date when the renewal begins.  */  
   RenewEffDate:string,
      /**  Date the renewal ends.  */  
   RenewedUntil:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CustNum:number,
   CustID:string,
   CustName:string,
   CustBTName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContractRenewalSearchListTableset{
   ContractRenewalSearchList:Erp_Tablesets_ContractRenewalSearchListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ContractRenewalSearchRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   ContractNum:number,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
      /**  Indicates if the renwal will automatically generate a quote.  */  
   QuotedRenewal:boolean,
      /**  Unique identifier of the task set assigned by the user.  */  
   TaskSetID:string,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   QuoteLine:number,
      /**  Indicates the Quote has been accepted.  */  
   QuoteAccepted:boolean,
      /**  This is the contract code assigned to the renewal.  */  
   RenewalCode:string,
      /**  Defaulted from the service contract code.  Determines whether or not the renewal can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  */  
   ShipRenewal:boolean,
      /**  Revenue Amortization Code.  */  
   RACode:string,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   DeferredRev:boolean,
      /**  Starting date the revenue is deferred.  */  
   DefRevStart:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this Contract.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**   This is used as one of the selection parameters on the Service Contract entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   EntryPerson:string,
      /**  Date the renewal was created.  */  
   EntryDate:string,
      /**  Coverage  for material  */  
   Material:boolean,
      /**  Coverage for Labor  */  
   Labor:boolean,
      /**  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  */  
   Misc:boolean,
      /**  This contract covers on site visits  */  
   OnSite:boolean,
      /**  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  */  
   Invoiced:boolean,
      /**  The invoice number of the last recurring invoice.  */  
   InvoiceNum:number,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  An integer that Ties the Contract record to a packing slip detail line  */  
   PackLine:number,
      /**  Indicates that Service Contract with this Code will generate recurring invoices.  */  
   RecurringInv:boolean,
      /**  The frequency that recurring invoices are generated only 'monthly' for now.  */  
   RecurringFreq:string,
      /**  Price modifier for unit price field Daily, monthly, Contract(Full length of the contract)  */  
   PricePer:string,
      /**  This flag is set to TRUE after the last recurring invoice is generated for the contract.  */  
   LastInvGen:boolean,
      /**  Indicates the Tax Category for this record.  */  
   TaxCatID:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  */  
   ReadyToInvoice:boolean,
      /**  The Sales order that this contract is linked to.  */  
   OrderNum:number,
      /**  The line number of the sales order that this contract is linked to  */  
   OrderLine:number,
      /**  Duration of Contract  */  
   Duration:number,
      /**  Used to establish invoice comments about the overall Renewal.  */  
   RenewalComment:string,
      /**  Date when the renewal begins.  */  
   RenewEffDate:string,
      /**  Date the renewal ends.  */  
   RenewedUntil:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  InvcTiming  */  
   InvcTiming:string,
      /**  It is the same as the contract type but applied to renewals  */  
   ContractCode:string,
      /**  The unit of measure of time that the renewal contract lasts.  */  
   Modifier:string,
      /**  Indicates how often an invoice is generated for the contract  */  
   FiscalCalendarID:string,
      /**  Indicates if the service contract is valid for renewal  */  
   Renewable:boolean,
   CustID:string,
   CustName:string,
   CustNum:number,
   CustBTName:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContractRenewalSearchTableset{
   ContractRenewalSearch:Erp_Tablesets_ContractRenewalSearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtContractRenewalSearchTableset{
   ContractRenewalSearch:Erp_Tablesets_ContractRenewalSearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param contractNum
      @param renewalNbr
   */  
export interface GetByID_input{
   contractNum:number,
   renewalNbr:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ContractRenewalSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ContractRenewalSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ContractRenewalSearchTableset[],
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
   returnObj:Erp_Tablesets_ContractRenewalSearchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param contractNum
   */  
export interface GetNewContractRenewalSearch_input{
   ds:Erp_Tablesets_ContractRenewalSearchTableset[],
   contractNum:number,
}

export interface GetNewContractRenewalSearch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContractRenewalSearchTableset,
}
}

   /** Required : 
      @param customerNum
      @param WhereClause
      @param SortByClause
      @param pageSize
      @param absolutePage
   */  
export interface GetRenewals_input{
      /**  customer number to return renewals for  */  
   customerNum:number,
      /**  WhereClause to filter the Parent records.  */  
   WhereClause:string,
      /**  To sort by the detail records.  */  
   SortByClause:string,
      /**  Page Size.  */  
   pageSize:number,
      /**  Absolute Page  */  
   absolutePage:number,
}

export interface GetRenewals_output{
   returnObj:Erp_Tablesets_ContractRenewalSearchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseContractRenewalSearch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseContractRenewalSearch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ContractRenewalSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtContractRenewalSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtContractRenewalSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ContractRenewalSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ContractRenewalSearchTableset,
}
}

