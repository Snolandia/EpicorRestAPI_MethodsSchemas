import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ServiceContractSearchSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/$metadata", {
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
   Description: Get ServiceContractSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ServiceContractSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ServiceContractSearchRow
   */  
export function get_ServiceContractSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ServiceContractSearchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/ServiceContractSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ServiceContractSearchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ServiceContractSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ServiceContractSearchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ServiceContractSearchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ServiceContractSearches(requestBody:Erp_Tablesets_ServiceContractSearchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/ServiceContractSearches", {
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
   Summary: Calls GetByID to retrieve the ServiceContractSearch item
   Description: Calls GetByID to retrieve the ServiceContractSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ServiceContractSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ServiceContractSearchRow
   */  
export function get_ServiceContractSearches_Company_ContractNum(Company:string, ContractNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ServiceContractSearchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/ServiceContractSearches(" + Company + "," + ContractNum + ")", {
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
         resolve(data as Erp_Tablesets_ServiceContractSearchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ServiceContractSearch for the service
   Description: Calls UpdateExt to update ServiceContractSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ServiceContractSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ServiceContractSearchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ServiceContractSearches_Company_ContractNum(Company:string, ContractNum:string, requestBody:Erp_Tablesets_ServiceContractSearchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/ServiceContractSearches(" + Company + "," + ContractNum + ")", {
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
   Summary: Call UpdateExt to delete ServiceContractSearch item
   Description: Call UpdateExt to delete ServiceContractSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ServiceContractSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ServiceContractSearches_Company_ContractNum(Company:string, ContractNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/ServiceContractSearches(" + Company + "," + ContractNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ServiceContractSearchListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ServiceContractSearchListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ServiceContractSearchListRow)
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
export function get_GetRows(whereClauseServiceContractSearch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseServiceContractSearch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseServiceContractSearch=" + whereClauseServiceContractSearch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/GetRows" + params, {
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
export function get_GetByID(contractNum:string, epicorHeaders?:Headers){
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

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetContractsRenewalsLP
   Description: Returns the service contracts as the GetRows does.
   OperationID: GetContractsRenewalsLP
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetContractsRenewalsLP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContractsRenewalsLP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContractsRenewalsLP(requestBody:GetContractsRenewalsLP_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetContractsRenewalsLP_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/GetContractsRenewalsLP", {
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
         resolve(data as GetContractsRenewalsLP_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetContractsRenewalsList
   Description: Returns the service contracts List  but with the option of filtering by the ones with renewals
   OperationID: GetContractsRenewalsList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetContractsRenewalsList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContractsRenewalsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContractsRenewalsList(requestBody:GetContractsRenewalsList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetContractsRenewalsList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/GetContractsRenewalsList", {
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
         resolve(data as GetContractsRenewalsList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetContractsRenewals
   Description: Returns the service contracts as the GetRows does but filtering them out by one with renewals
   OperationID: GetContractsRenewals
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetContractsRenewals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContractsRenewals_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContractsRenewals(requestBody:GetContractsRenewals_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetContractsRenewals_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/GetContractsRenewals", {
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
         resolve(data as GetContractsRenewals_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListCustom
   Description: Custom GetList method.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/GetListCustom", {
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
   Summary: Invoke method GetRowsCustom
   Description: Custom GetList method.
   OperationID: GetRowsCustom
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCustom(requestBody:GetRowsCustom_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsCustom_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/GetRowsCustom", {
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
         resolve(data as GetRowsCustom_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewServiceContractSearch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewServiceContractSearch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewServiceContractSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewServiceContractSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewServiceContractSearch(requestBody:GetNewServiceContractSearch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewServiceContractSearch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/GetNewServiceContractSearch", {
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
         resolve(data as GetNewServiceContractSearch_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ServiceContractSearchListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ServiceContractSearchListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ServiceContractSearchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ServiceContractSearchRow,
}

export interface Erp_Tablesets_ServiceContractSearchListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   "ContractNum":number,
      /**  A value of "Ord-Ent" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.  */  
   "ContractType":string,
      /**  Contains the Customer number that the Service Contract is for.  This must be valid in the Customer table.  */  
   "CustNum":number,
      /**  The Sales order that this contract is linked to.  */  
   "OrderNum":number,
      /**  The line number of the sales order that this contract is linked to  */  
   "OrderLine":number,
      /**  Same as OrderDate when SLSORD.  TODAY when CNTENT  */  
   "EntryDate":string,
      /**  A unique code that identifies the Contract  */  
   "ContractCode":string,
      /**  Contains comments about the overall Contract. These will be printed on the Service Contract.  */  
   "ContractComment":string,
      /**  Used to establish invoice comments about the overall Contract. These will copied into the Invoice detail file as defaults.  */  
   "InvoiceComment":string,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   "PrcConNum":number,
      /**  Indicates which customer ship to is to be used  for the Service Contract. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   "ShipToNum":string,
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
      /**  This Service Contract has been deactivated when TRUE  */  
   "ContVoid":boolean,
      /**  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service contract is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   "ShpConNum":number,
      /**   The date of the earliest FscontSp.activateDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed. This will always be the earliest activate date on this contract.  */  
   "ActiveDate":string,
      /**   The date of the Latest FscontSp.ExpirationDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed.  this will always be the Latest activate date on this contract.  */  
   "ExpireDate":string,
      /**  Duration of Contract  */  
   "Duration":number,
      /**  Whether the duration is for Days, Months, years.  */  
   "Modifier":string,
      /**  Coverage  for material  */  
   "Material":boolean,
      /**  Coverage for Labor  */  
   "Labor":boolean,
      /**  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  */  
   "Misc":boolean,
      /**  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  */  
   "Invoiced":boolean,
      /**  Packing slip number that this detail record is linked with.  */  
   "PackNum":number,
      /**  An integer that Ties the Contract record to a packing slip detail line  */  
   "PackLine":number,
      /**  This contract covers on site visits  */  
   "OnSite":boolean,
      /**  Indicates that Service Contract with this Code will generate recurring invoices.  */  
   "RecurringInv":boolean,
      /**  The frequency that recurring invoices are generated only 'monthly' for now.  */  
   "RecurringFreq":string,
      /**  Price modifier for unit price field Daily, monthly, Contract(Full length of the contract)  */  
   "PricePer":string,
      /**  This flag is set to TRUE after the last recurring invoice is generated for the contract.  */  
   "LastInvGen":boolean,
      /**  The invoice number of the last recurring invoice.  */  
   "InvoiceNum":number,
      /**  Indicates the Tax Category for this record.  */  
   "TaxCatID":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Bill To Customer Number  */  
   "BTCustNum":number,
      /**   Indicates if the One Time ShipTo information should be used instead of the standard ShipTo.  One Time ShipTo info is stored in this record in the fields prefixed with "OTS"
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
      /**  Full name of the contact.  */  
   "OTSContact":string,
      /**  Fax number for the One Time ShipTo.  */  
   "OTSFaxNum":string,
      /**  Phone number for the One Time ShipTo  */  
   "OTSPhoneNum":string,
      /**  One Time Shipping country Number.  */  
   "OTSCountryNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   "DeferredRev":boolean,
      /**  Revenue Amortization Code.  */  
   "RACode":string,
      /**  Starting date the revenue is deferred.  */  
   "DefRevStart":string,
      /**  Indicates if the contract has been suspended.  A suspended contract cannot have any calls linked to it.  */  
   "Suspended":boolean,
      /**  Indicates if the contrct will automatically generate a quote  */  
   "QuotedContract":boolean,
      /**  Defaulted from the service contract code.  Determines whether or not the contract can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  */  
   "ShipContract":boolean,
      /**  Unique identifier of the task set assigned by the user.  */  
   "TaskSetID":string,
      /**  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  */  
   "ReadyToInvoice":boolean,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   "QuoteNum":number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   "QuoteLine":number,
      /**  Indicates the Quote has been accepted  */  
   "QuoteAccepted":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "ContractLine":number,
   "ContractQty":number,
   "DocPricePerUnit":number,
   "IUM":string,
   "LineDesc":string,
   "PartNum":string,
   "PricePerUnit":number,
   "ProdCode":string,
   "ProjectID":string,
   "RevisionNum":string,
   "XPartNum":string,
   "XRevisionNum":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustomerBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustomerCustID":string,
      /**  The full name of the customer.  */  
   "CustomerName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ServiceContractSearchRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   "ContractNum":number,
      /**  A value of "Ord-Ent" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.  */  
   "ContractType":string,
      /**  Contains the Customer number that the Service Contract is for.  This must be valid in the Customer table.  */  
   "CustNum":number,
      /**  The Sales order that this contract is linked to.  */  
   "OrderNum":number,
      /**  The line number of the sales order that this contract is linked to  */  
   "OrderLine":number,
      /**  Same as OrderDate when SLSORD.  TODAY when CNTENT  */  
   "EntryDate":string,
      /**  A unique code that identifies the Contract  */  
   "ContractCode":string,
      /**  Contains comments about the overall Contract. These will be printed on the Service Contract.  */  
   "ContractComment":string,
      /**  Used to establish invoice comments about the overall Contract. These will copied into the Invoice detail file as defaults.  */  
   "InvoiceComment":string,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   "PrcConNum":number,
      /**  Indicates which customer ship to is to be used  for the Service Contract. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   "ShipToNum":string,
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
      /**  This Service Contract has been deactivated when TRUE  */  
   "ContVoid":boolean,
      /**  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service contract is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   "ShpConNum":number,
      /**   The date of the earliest FscontSp.activateDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed. This will always be the earliest activate date on this contract.  */  
   "ActiveDate":string,
      /**   The date of the Latest FscontSp.ExpirationDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed.  this will always be the Latest activate date on this contract.  */  
   "ExpireDate":string,
      /**  Duration of Contract  */  
   "Duration":number,
      /**  Whether the duration is for Days, Months, years.  */  
   "Modifier":string,
      /**  Coverage  for material  */  
   "Material":boolean,
      /**  Coverage for Labor  */  
   "Labor":boolean,
      /**  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  */  
   "Misc":boolean,
      /**  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  */  
   "Invoiced":boolean,
      /**  Packing slip number that this detail record is linked with.  */  
   "PackNum":number,
      /**  An integer that Ties the Contract record to a packing slip detail line  */  
   "PackLine":number,
      /**  This contract covers on site visits  */  
   "OnSite":boolean,
      /**  Indicates that Service Contract with this Code will generate recurring invoices.  */  
   "RecurringInv":boolean,
      /**  The frequency that recurring invoices are generated only 'monthly' for now.  */  
   "RecurringFreq":string,
      /**  Price modifier for unit price field Daily, monthly, Contract(Full length of the contract)  */  
   "PricePer":string,
      /**  This flag is set to TRUE after the last recurring invoice is generated for the contract.  */  
   "LastInvGen":boolean,
      /**  The invoice number of the last recurring invoice.  */  
   "InvoiceNum":number,
      /**  Indicates the Tax Category for this record.  */  
   "TaxCatID":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Bill To Customer Number  */  
   "BTCustNum":number,
      /**   Indicates if the One Time ShipTo information should be used instead of the standard ShipTo.  One Time ShipTo info is stored in this record in the fields prefixed with "OTS"
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
      /**  Full name of the contact.  */  
   "OTSContact":string,
      /**  Fax number for the One Time ShipTo.  */  
   "OTSFaxNum":string,
      /**  Phone number for the One Time ShipTo  */  
   "OTSPhoneNum":string,
      /**  One Time Shipping country Number.  */  
   "OTSCountryNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   "DeferredRev":boolean,
      /**  Revenue Amortization Code.  */  
   "RACode":string,
      /**  Starting date the revenue is deferred.  */  
   "DefRevStart":string,
      /**  Indicates if the contract has been suspended.  A suspended contract cannot have any calls linked to it.  */  
   "Suspended":boolean,
      /**  Indicates if the contrct will automatically generate a quote  */  
   "QuotedContract":boolean,
      /**  Defaulted from the service contract code.  Determines whether or not the contract can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  */  
   "ShipContract":boolean,
      /**  Unique identifier of the task set assigned by the user.  */  
   "TaskSetID":string,
      /**  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  */  
   "ReadyToInvoice":boolean,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   "QuoteNum":number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   "QuoteLine":number,
      /**  Indicates the Quote has been accepted  */  
   "QuoteAccepted":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  InvcTiming  */  
   "InvcTiming":string,
      /**  Indicates how often an invoice is generated for the contract.  */  
   "FiscalCalendarID":string,
      /**  Indicates if the service contract using is valid for renewal.  */  
   "Renewable":boolean,
      /**  Intrastat: Activates HS Commodity code retrieving in contract invoicing  */  
   "IncIntrastat":boolean,
      /**  Determines if the service contract has to be synchronized with Epicor FSA application.  */  
   "SendToFSA":boolean,
      /**  OTSTaxValidationStatus  */  
   "OTSTaxValidationStatus":number,
      /**  OTSTaxValidationDate  */  
   "OTSTaxValidationDate":string,
   "ContractQty":number,
   "DocPricePerUnit":number,
   "IUM":string,
   "LineDesc":string,
   "PartNum":string,
   "PricePerUnit":number,
   "ProdCode":string,
   "ProjectID":string,
   "RevisionNum":string,
   "XPartNum":string,
   "XRevisionNum":string,
   "ContractLine":number,
   "BitFlag":number,
   "CustomerName":string,
   "CustomerCustID":string,
   "CustomerBTName":string,
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
   */  
export interface DeleteByID_input{
   contractNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ServiceContractSearchListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   ContractNum:number,
      /**  A value of "Ord-Ent" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.  */  
   ContractType:string,
      /**  Contains the Customer number that the Service Contract is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  The Sales order that this contract is linked to.  */  
   OrderNum:number,
      /**  The line number of the sales order that this contract is linked to  */  
   OrderLine:number,
      /**  Same as OrderDate when SLSORD.  TODAY when CNTENT  */  
   EntryDate:string,
      /**  A unique code that identifies the Contract  */  
   ContractCode:string,
      /**  Contains comments about the overall Contract. These will be printed on the Service Contract.  */  
   ContractComment:string,
      /**  Used to establish invoice comments about the overall Contract. These will copied into the Invoice detail file as defaults.  */  
   InvoiceComment:string,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   PrcConNum:number,
      /**  Indicates which customer ship to is to be used  for the Service Contract. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   ShipToNum:string,
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
      /**  This Service Contract has been deactivated when TRUE  */  
   ContVoid:boolean,
      /**  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service contract is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   ShpConNum:number,
      /**   The date of the earliest FscontSp.activateDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed. This will always be the earliest activate date on this contract.  */  
   ActiveDate:string,
      /**   The date of the Latest FscontSp.ExpirationDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed.  this will always be the Latest activate date on this contract.  */  
   ExpireDate:string,
      /**  Duration of Contract  */  
   Duration:number,
      /**  Whether the duration is for Days, Months, years.  */  
   Modifier:string,
      /**  Coverage  for material  */  
   Material:boolean,
      /**  Coverage for Labor  */  
   Labor:boolean,
      /**  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  */  
   Misc:boolean,
      /**  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  */  
   Invoiced:boolean,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  An integer that Ties the Contract record to a packing slip detail line  */  
   PackLine:number,
      /**  This contract covers on site visits  */  
   OnSite:boolean,
      /**  Indicates that Service Contract with this Code will generate recurring invoices.  */  
   RecurringInv:boolean,
      /**  The frequency that recurring invoices are generated only 'monthly' for now.  */  
   RecurringFreq:string,
      /**  Price modifier for unit price field Daily, monthly, Contract(Full length of the contract)  */  
   PricePer:string,
      /**  This flag is set to TRUE after the last recurring invoice is generated for the contract.  */  
   LastInvGen:boolean,
      /**  The invoice number of the last recurring invoice.  */  
   InvoiceNum:number,
      /**  Indicates the Tax Category for this record.  */  
   TaxCatID:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**   Indicates if the One Time ShipTo information should be used instead of the standard ShipTo.  One Time ShipTo info is stored in this record in the fields prefixed with "OTS"
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
      /**  Full name of the contact.  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipping country Number.  */  
   OTSCountryNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   DeferredRev:boolean,
      /**  Revenue Amortization Code.  */  
   RACode:string,
      /**  Starting date the revenue is deferred.  */  
   DefRevStart:string,
      /**  Indicates if the contract has been suspended.  A suspended contract cannot have any calls linked to it.  */  
   Suspended:boolean,
      /**  Indicates if the contrct will automatically generate a quote  */  
   QuotedContract:boolean,
      /**  Defaulted from the service contract code.  Determines whether or not the contract can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  */  
   ShipContract:boolean,
      /**  Unique identifier of the task set assigned by the user.  */  
   TaskSetID:string,
      /**  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  */  
   ReadyToInvoice:boolean,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   QuoteLine:number,
      /**  Indicates the Quote has been accepted  */  
   QuoteAccepted:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   ContractLine:number,
   ContractQty:number,
   DocPricePerUnit:number,
   IUM:string,
   LineDesc:string,
   PartNum:string,
   PricePerUnit:number,
   ProdCode:string,
   ProjectID:string,
   RevisionNum:string,
   XPartNum:string,
   XRevisionNum:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustomerBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustomerCustID:string,
      /**  The full name of the customer.  */  
   CustomerName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ServiceContractSearchListTableset{
   ServiceContractSearchList:Erp_Tablesets_ServiceContractSearchListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ServiceContractSearchRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   ContractNum:number,
      /**  A value of "Ord-Ent" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.  */  
   ContractType:string,
      /**  Contains the Customer number that the Service Contract is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  The Sales order that this contract is linked to.  */  
   OrderNum:number,
      /**  The line number of the sales order that this contract is linked to  */  
   OrderLine:number,
      /**  Same as OrderDate when SLSORD.  TODAY when CNTENT  */  
   EntryDate:string,
      /**  A unique code that identifies the Contract  */  
   ContractCode:string,
      /**  Contains comments about the overall Contract. These will be printed on the Service Contract.  */  
   ContractComment:string,
      /**  Used to establish invoice comments about the overall Contract. These will copied into the Invoice detail file as defaults.  */  
   InvoiceComment:string,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   PrcConNum:number,
      /**  Indicates which customer ship to is to be used  for the Service Contract. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   ShipToNum:string,
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
      /**  This Service Contract has been deactivated when TRUE  */  
   ContVoid:boolean,
      /**  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service contract is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   ShpConNum:number,
      /**   The date of the earliest FscontSp.activateDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed. This will always be the earliest activate date on this contract.  */  
   ActiveDate:string,
      /**   The date of the Latest FscontSp.ExpirationDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed.  this will always be the Latest activate date on this contract.  */  
   ExpireDate:string,
      /**  Duration of Contract  */  
   Duration:number,
      /**  Whether the duration is for Days, Months, years.  */  
   Modifier:string,
      /**  Coverage  for material  */  
   Material:boolean,
      /**  Coverage for Labor  */  
   Labor:boolean,
      /**  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  */  
   Misc:boolean,
      /**  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  */  
   Invoiced:boolean,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  An integer that Ties the Contract record to a packing slip detail line  */  
   PackLine:number,
      /**  This contract covers on site visits  */  
   OnSite:boolean,
      /**  Indicates that Service Contract with this Code will generate recurring invoices.  */  
   RecurringInv:boolean,
      /**  The frequency that recurring invoices are generated only 'monthly' for now.  */  
   RecurringFreq:string,
      /**  Price modifier for unit price field Daily, monthly, Contract(Full length of the contract)  */  
   PricePer:string,
      /**  This flag is set to TRUE after the last recurring invoice is generated for the contract.  */  
   LastInvGen:boolean,
      /**  The invoice number of the last recurring invoice.  */  
   InvoiceNum:number,
      /**  Indicates the Tax Category for this record.  */  
   TaxCatID:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**   Indicates if the One Time ShipTo information should be used instead of the standard ShipTo.  One Time ShipTo info is stored in this record in the fields prefixed with "OTS"
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
      /**  Full name of the contact.  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipping country Number.  */  
   OTSCountryNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   DeferredRev:boolean,
      /**  Revenue Amortization Code.  */  
   RACode:string,
      /**  Starting date the revenue is deferred.  */  
   DefRevStart:string,
      /**  Indicates if the contract has been suspended.  A suspended contract cannot have any calls linked to it.  */  
   Suspended:boolean,
      /**  Indicates if the contrct will automatically generate a quote  */  
   QuotedContract:boolean,
      /**  Defaulted from the service contract code.  Determines whether or not the contract can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  */  
   ShipContract:boolean,
      /**  Unique identifier of the task set assigned by the user.  */  
   TaskSetID:string,
      /**  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  */  
   ReadyToInvoice:boolean,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   QuoteLine:number,
      /**  Indicates the Quote has been accepted  */  
   QuoteAccepted:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  InvcTiming  */  
   InvcTiming:string,
      /**  Indicates how often an invoice is generated for the contract.  */  
   FiscalCalendarID:string,
      /**  Indicates if the service contract using is valid for renewal.  */  
   Renewable:boolean,
      /**  Intrastat: Activates HS Commodity code retrieving in contract invoicing  */  
   IncIntrastat:boolean,
      /**  Determines if the service contract has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  OTSTaxValidationStatus  */  
   OTSTaxValidationStatus:number,
      /**  OTSTaxValidationDate  */  
   OTSTaxValidationDate:string,
   ContractQty:number,
   DocPricePerUnit:number,
   IUM:string,
   LineDesc:string,
   PartNum:string,
   PricePerUnit:number,
   ProdCode:string,
   ProjectID:string,
   RevisionNum:string,
   XPartNum:string,
   XRevisionNum:string,
   ContractLine:number,
   BitFlag:number,
   CustomerName:string,
   CustomerCustID:string,
   CustomerBTName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ServiceContractSearchTableset{
   ServiceContractSearch:Erp_Tablesets_ServiceContractSearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtServiceContractSearchTableset{
   ServiceContractSearch:Erp_Tablesets_ServiceContractSearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param contractNum
   */  
export interface GetByID_input{
   contractNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ServiceContractSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ServiceContractSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ServiceContractSearchTableset[],
}

   /** Required : 
      @param whereClause
      @param statusFilter
      @param renewalsOnly
      @param startingAt
      @param pageSize
      @param absolutePage
   */  
export interface GetContractsRenewalsLP_input{
      /**  The where clause used to filter the records.  */  
   whereClause:string,
      /**  Status Filter, options "All,Active, Expired"  */  
   statusFilter:string,
      /**  Indicates if only those contracts with renewals are returned  */  
   renewalsOnly:boolean,
      /**  The Starting At and Sort used in the Search.  */  
   startingAt:string,
      /**  Page Size  */  
   pageSize:number,
      /**  Absolute Page  */  
   absolutePage:number,
}

export interface GetContractsRenewalsLP_output{
   returnObj:Erp_Tablesets_ServiceContractSearchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ContractNumberFilter
      @param filter
      @param renewalsOnly
      @param parentWhereClause
      @param SortByClause
      @param PartDescContains
      @param pageSize
      @param absolutePage
   */  
export interface GetContractsRenewalsList_input{
      /**  To be use if no "SortBy" haven provided  */  
   ContractNumberFilter:string,
      /**  Status Filter, options "All,Active, Expired"  */  
   filter:string,
      /**  Indicates if only those contracts with renewals are returned  */  
   renewalsOnly:boolean,
      /**  WhereClause to filter the Parent records.  */  
   parentWhereClause:string,
      /**  To sort by the detail records.  */  
   SortByClause:string,
      /**  The part contains filter  */  
   PartDescContains:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetContractsRenewalsList_output{
   returnObj:Erp_Tablesets_ServiceContractSearchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param renewalsOnly
      @param WhereClause
      @param SortByClause
      @param PartDescContains
      @param pageSize
      @param absolutePage
   */  
export interface GetContractsRenewals_input{
      /**  Indicates if only those contracts with renewals are returned  */  
   renewalsOnly:boolean,
      /**  WhereClause to filter the Parent records.  */  
   WhereClause:string,
      /**  To sort by the detail records.  */  
   SortByClause:string,
      /**  The part contains filter  */  
   PartDescContains:string,
      /**  Page Size.  */  
   pageSize:number,
      /**  Absolute Page  */  
   absolutePage:number,
}

export interface GetContractsRenewals_output{
   returnObj:Erp_Tablesets_ServiceContractSearchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param WhereClause
      @param SortByClause
      @param PartDescContains
      @param pageSize
      @param absolutePage
   */  
export interface GetListCustom_input{
      /**  WhereClause to filter the Parent records.  */  
   WhereClause:string,
      /**  To sort by the detail records.  */  
   SortByClause:string,
      /**  The part contains filter  */  
   PartDescContains:string,
      /**  Page Size.  */  
   pageSize:number,
      /**  Absolute Page  */  
   absolutePage:number,
}

export interface GetListCustom_output{
   returnObj:Erp_Tablesets_ServiceContractSearchListTableset[],
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
   returnObj:Erp_Tablesets_ServiceContractSearchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewServiceContractSearch_input{
   ds:Erp_Tablesets_ServiceContractSearchTableset[],
}

export interface GetNewServiceContractSearch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractSearchTableset,
}
}

   /** Required : 
      @param WhereClause
      @param SortByClause
      @param PartDescContains
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustom_input{
      /**  WhereClause to filter the Parent records.  */  
   WhereClause:string,
      /**  To sort by the detail records.  */  
   SortByClause:string,
      /**  The part contains filter  */  
   PartDescContains:string,
      /**  Page Size.  */  
   pageSize:number,
      /**  Absolute Page  */  
   absolutePage:number,
}

export interface GetRowsCustom_output{
   returnObj:Erp_Tablesets_ServiceContractSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseServiceContractSearch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseServiceContractSearch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ServiceContractSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtServiceContractSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtServiceContractSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ServiceContractSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractSearchTableset,
}
}

