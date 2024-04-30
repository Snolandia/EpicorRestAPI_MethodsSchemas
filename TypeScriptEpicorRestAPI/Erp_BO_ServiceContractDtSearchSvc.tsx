import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ServiceContractDtSearchSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/$metadata", {
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
   Description: Get ServiceContractDtSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ServiceContractDtSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSContDtRow
   */  
export function get_ServiceContractDtSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContDtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/ServiceContractDtSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContDtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ServiceContractDtSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSContDtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.FSContDtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ServiceContractDtSearches(requestBody:Erp_Tablesets_FSContDtRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/ServiceContractDtSearches", {
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
   Summary: Calls GetByID to retrieve the ServiceContractDtSearch item
   Description: Calls GetByID to retrieve the ServiceContractDtSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ServiceContractDtSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param ContractLine Desc: ContractLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.FSContDtRow
   */  
export function get_ServiceContractDtSearches_Company_ContractNum_ContractLine(Company:string, ContractNum:string, ContractLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FSContDtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/ServiceContractDtSearches(" + Company + "," + ContractNum + "," + ContractLine + ")", {
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
         resolve(data as Erp_Tablesets_FSContDtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ServiceContractDtSearch for the service
   Description: Calls UpdateExt to update ServiceContractDtSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ServiceContractDtSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param ContractLine Desc: ContractLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSContDtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ServiceContractDtSearches_Company_ContractNum_ContractLine(Company:string, ContractNum:string, ContractLine:string, requestBody:Erp_Tablesets_FSContDtRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/ServiceContractDtSearches(" + Company + "," + ContractNum + "," + ContractLine + ")", {
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
   Summary: Call UpdateExt to delete ServiceContractDtSearch item
   Description: Call UpdateExt to delete ServiceContractDtSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ServiceContractDtSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param ContractLine Desc: ContractLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ServiceContractDtSearches_Company_ContractNum_ContractLine(Company:string, ContractNum:string, ContractLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/ServiceContractDtSearches(" + Company + "," + ContractNum + "," + ContractLine + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSContDtListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContDtListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContDtListRow)
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
export function get_GetRows(whereClauseFSContDt:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseFSContDt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFSContDt=" + whereClauseFSContDt
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/GetRows" + params, {
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
export function get_GetByID(contractNum:string, contractLine:string, epicorHeaders?:Headers){
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
   if(typeof contractLine!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "contractLine=" + contractLine
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewFSContDt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSContDt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewFSContDt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSContDt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFSContDt(requestBody:GetNewFSContDt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewFSContDt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/GetNewFSContDt", {
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
         resolve(data as GetNewFSContDt_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContDtListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FSContDtListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContDtRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FSContDtRow,
}

export interface Erp_Tablesets_FSContDtListRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Contract Number of the Contract  */  
   "ContractNum":number,
      /**  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  */  
   "ContractLine":number,
      /**  A unique code that identifies the Contract  */  
   "ContractCode":string,
      /**  The PartNum field identifies the Part  */  
   "PartNum":string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   "RevisionNum":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "LineDesc":string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if its a valid Part.  */  
   "IUM":string,
      /**  Price per unit for the Contract in base currency.  Defaults from the FScontCd table  */  
   "PricePerUnit":number,
      /**  Price per unit for the Contract in customers currency.  Defaults from the FScontCd table  */  
   "DocPricePerUnit":number,
      /**  Total Contract Quantity for the line item.  */  
   "ContractQty":number,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   "ProdCode":string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   "XPartNum":string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   "XRevisionNum":string,
      /**  Used to establish invoice comments about the Contract line item. These will copied into the Invoice detail  file as defaults.  */  
   "InvoiceComment":string,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the FSContDt records for a specific customer.  */  
   "CustNum":number,
      /**  Contains the Order Number that ties this detail record back to an OrderHed record.  */  
   "OrderNum":number,
      /**  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   "OrderLine":number,
      /**  Project ID of the Project table record that this FSContDt record. Can be blank.  */  
   "ProjectID":string,
      /**  Editor widget for Contract comments.  */  
   "CommentText":string,
      /**   A value of "ORD-ENT" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.
(Duplicated from FSContHd for Browse)  */  
   "ContractType":string,
      /**  Contains comments about the detail contract line item. These will be printed on the Sales Acknowledgements and service contracts  */  
   "ContractComment":string,
      /**  Sold to Order Number  */  
   "SoldOrderNum":number,
      /**  Sold To Order line  */  
   "SoldOrderLine":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Reporting currency value of this field  */  
   "Rpt1PricePerUnit":number,
      /**  Reporting currency value of this field  */  
   "Rpt2PricePerUnit":number,
      /**  Reporting currency value of this field  */  
   "Rpt3PricePerUnit":number,
      /**  A value of Yes indicates the line is not part of the service contract agreement and it will not be included in the contract amounts.  */  
   "Inactive":boolean,
      /**  This is the date the contract line was set to inactive.  */  
   "DateInactivated":string,
      /**  This is the first date the contract line is considered for billing purposes.  */  
   "BillStartDate":string,
      /**  This is the last date the contract line is considered for billing.  */  
   "BillEndDate":string,
      /**  Indicates this line has been invoiced.  */  
   "Invoiced":boolean,
      /**  Date this line was invoiced.  */  
   "DateInvoiced":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "AllowUpdate":boolean,
   "CurrencySwitch":boolean,
   "BaseCurrSymbol":string,
   "ExtPrice":number,
   "DocExtPrice":number,
   "DisplayContractType":string,
      /**  Return Quantity used in the create RMA process.  */  
   "ReturnQty":number,
      /**  Indicates if the contract line is selected to create RMA for.  */  
   "SelectedforRMA":boolean,
   "HdCurrencyCode":string,
   "HdCurrencyCodeDesc":string,
      /**  Document currency symbol.  */  
   "DocCurrSymbol":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
      /**  Unit of Measure Description  */  
   "IUMDesc":string,
   "TrackSerialNumbers":boolean,
   "Rpt1ExtPrice":number,
   "Rpt2ExtPrice":number,
   "Rpt3ExtPrice":number,
      /**  Description of the service contract.  */  
   "ContractCodeContractDescription":string,
      /**  The full name of the customer.  */  
   "CustNumName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustNumBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustNumCustID":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "OrderLineLineDesc":string,
      /**  A unique code that identifies the currency.  */  
   "OrderNumCurrencyCode":string,
      /**  The member's name on the credit card.  */  
   "OrderNumCardMemberName":string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartNumTrackLots":boolean,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartNumSalesUM":string,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartNumSellingFactor":number,
      /**  Indicates if this part is serial number tracked  */  
   "PartNumTrackSerialNum":boolean,
      /**  Full description of Product Group.  */  
   "ProdCodeDescription":string,
      /**  Full description of Project Management Code.  */  
   "ProjectIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FSContDtRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Contract Number of the Contract  */  
   "ContractNum":number,
      /**  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  */  
   "ContractLine":number,
      /**  A unique code that identifies the Contract  */  
   "ContractCode":string,
      /**  The PartNum field identifies the Part  */  
   "PartNum":string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   "RevisionNum":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "LineDesc":string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if its a valid Part.  */  
   "IUM":string,
      /**  Price per unit for the Contract in base currency.  Defaults from the FScontCd table  */  
   "PricePerUnit":number,
      /**  Price per unit for the Contract in customers currency.  Defaults from the FScontCd table  */  
   "DocPricePerUnit":number,
      /**  Total Contract Quantity for the line item.  */  
   "ContractQty":number,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   "ProdCode":string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   "XPartNum":string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   "XRevisionNum":string,
      /**  Used to establish invoice comments about the Contract line item. These will copied into the Invoice detail  file as defaults.  */  
   "InvoiceComment":string,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the FSContDt records for a specific customer.  */  
   "CustNum":number,
      /**  Contains the Order Number that ties this detail record back to an OrderHed record.  */  
   "OrderNum":number,
      /**  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   "OrderLine":number,
      /**  Project ID of the Project table record that this FSContDt record. Can be blank.  */  
   "ProjectID":string,
      /**  Editor widget for Contract comments.  */  
   "CommentText":string,
      /**   A value of "ORD-ENT" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.
(Duplicated from FSContHd for Browse)  */  
   "ContractType":string,
      /**  Contains comments about the detail contract line item. These will be printed on the Sales Acknowledgements and service contracts  */  
   "ContractComment":string,
      /**  Sold to Order Number  */  
   "SoldOrderNum":number,
      /**  Sold To Order line  */  
   "SoldOrderLine":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Reporting currency value of this field  */  
   "Rpt1PricePerUnit":number,
      /**  Reporting currency value of this field  */  
   "Rpt2PricePerUnit":number,
      /**  Reporting currency value of this field  */  
   "Rpt3PricePerUnit":number,
      /**  A value of Yes indicates the line is not part of the service contract agreement and it will not be included in the contract amounts.  */  
   "Inactive":boolean,
      /**  This is the date the contract line was set to inactive.  */  
   "DateInactivated":string,
      /**  This is the first date the contract line is considered for billing purposes.  */  
   "BillStartDate":string,
      /**  This is the last date the contract line is considered for billing.  */  
   "BillEndDate":string,
      /**  Indicates this line has been invoiced.  */  
   "Invoiced":boolean,
      /**  Date this line was invoiced.  */  
   "DateInvoiced":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "AllowUpdate":boolean,
   "CurrencySwitch":boolean,
   "BaseCurrSymbol":string,
   "ExtPrice":number,
   "DocExtPrice":number,
   "DisplayContractType":string,
      /**  Return Quantity used in the create RMA process.  */  
   "ReturnQty":number,
      /**  Indicates if the contract line is selected to create RMA for.  */  
   "SelectedforRMA":boolean,
   "HdCurrencyCode":string,
   "HdCurrencyCodeDesc":string,
      /**  Document currency symbol.  */  
   "DocCurrSymbol":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
      /**  Unit of Measure Description  */  
   "IUMDesc":string,
   "TrackSerialNumbers":boolean,
   "Rpt1ExtPrice":number,
   "Rpt2ExtPrice":number,
   "Rpt3ExtPrice":number,
      /**  The calculated PriceMulti is based on the parent FSContHd record.  */  
   "PriceMulti":number,
      /**  Unique identifier of related integration record.  */  
   "IntExternalKey":string,
   "BitFlag":number,
   "ContractCodeContractDescription":string,
   "CustNumBTName":string,
   "CustNumCustID":string,
   "CustNumName":string,
   "OrderLineLineDesc":string,
   "OrderNumCurrencyCode":string,
   "OrderNumCardMemberName":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumPricePerCode":string,
   "PartNumSalesUM":string,
   "PartNumIUM":string,
   "PartNumSellingFactor":number,
   "PartNumTrackDimension":boolean,
   "PartNumPartDescription":string,
   "PartNumTrackLots":boolean,
   "ProdCodeDescription":string,
   "ProjectIDDescription":string,
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
      @param contractLine
   */  
export interface DeleteByID_input{
   contractNum:number,
   contractLine:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_FSContDtListRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Contract Number of the Contract  */  
   ContractNum:number,
      /**  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  */  
   ContractLine:number,
      /**  A unique code that identifies the Contract  */  
   ContractCode:string,
      /**  The PartNum field identifies the Part  */  
   PartNum:string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   RevisionNum:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if its a valid Part.  */  
   IUM:string,
      /**  Price per unit for the Contract in base currency.  Defaults from the FScontCd table  */  
   PricePerUnit:number,
      /**  Price per unit for the Contract in customers currency.  Defaults from the FScontCd table  */  
   DocPricePerUnit:number,
      /**  Total Contract Quantity for the line item.  */  
   ContractQty:number,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   XPartNum:string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   XRevisionNum:string,
      /**  Used to establish invoice comments about the Contract line item. These will copied into the Invoice detail  file as defaults.  */  
   InvoiceComment:string,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the FSContDt records for a specific customer.  */  
   CustNum:number,
      /**  Contains the Order Number that ties this detail record back to an OrderHed record.  */  
   OrderNum:number,
      /**  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   OrderLine:number,
      /**  Project ID of the Project table record that this FSContDt record. Can be blank.  */  
   ProjectID:string,
      /**  Editor widget for Contract comments.  */  
   CommentText:string,
      /**   A value of "ORD-ENT" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.
(Duplicated from FSContHd for Browse)  */  
   ContractType:string,
      /**  Contains comments about the detail contract line item. These will be printed on the Sales Acknowledgements and service contracts  */  
   ContractComment:string,
      /**  Sold to Order Number  */  
   SoldOrderNum:number,
      /**  Sold To Order line  */  
   SoldOrderLine:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Reporting currency value of this field  */  
   Rpt1PricePerUnit:number,
      /**  Reporting currency value of this field  */  
   Rpt2PricePerUnit:number,
      /**  Reporting currency value of this field  */  
   Rpt3PricePerUnit:number,
      /**  A value of Yes indicates the line is not part of the service contract agreement and it will not be included in the contract amounts.  */  
   Inactive:boolean,
      /**  This is the date the contract line was set to inactive.  */  
   DateInactivated:string,
      /**  This is the first date the contract line is considered for billing purposes.  */  
   BillStartDate:string,
      /**  This is the last date the contract line is considered for billing.  */  
   BillEndDate:string,
      /**  Indicates this line has been invoiced.  */  
   Invoiced:boolean,
      /**  Date this line was invoiced.  */  
   DateInvoiced:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   AllowUpdate:boolean,
   CurrencySwitch:boolean,
   BaseCurrSymbol:string,
   ExtPrice:number,
   DocExtPrice:number,
   DisplayContractType:string,
      /**  Return Quantity used in the create RMA process.  */  
   ReturnQty:number,
      /**  Indicates if the contract line is selected to create RMA for.  */  
   SelectedforRMA:boolean,
   HdCurrencyCode:string,
   HdCurrencyCodeDesc:string,
      /**  Document currency symbol.  */  
   DocCurrSymbol:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  Unit of Measure Description  */  
   IUMDesc:string,
   TrackSerialNumbers:boolean,
   Rpt1ExtPrice:number,
   Rpt2ExtPrice:number,
   Rpt3ExtPrice:number,
      /**  Description of the service contract.  */  
   ContractCodeContractDescription:string,
      /**  The full name of the customer.  */  
   CustNumName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustNumBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustNumCustID:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   OrderLineLineDesc:string,
      /**  A unique code that identifies the currency.  */  
   OrderNumCurrencyCode:string,
      /**  The member's name on the credit card.  */  
   OrderNumCardMemberName:string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartNumTrackLots:boolean,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartNumSellingFactor:number,
      /**  Indicates if this part is serial number tracked  */  
   PartNumTrackSerialNum:boolean,
      /**  Full description of Product Group.  */  
   ProdCodeDescription:string,
      /**  Full description of Project Management Code.  */  
   ProjectIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FSContDtListTableset{
   FSContDtList:Erp_Tablesets_FSContDtListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FSContDtRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Contract Number of the Contract  */  
   ContractNum:number,
      /**  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  */  
   ContractLine:number,
      /**  A unique code that identifies the Contract  */  
   ContractCode:string,
      /**  The PartNum field identifies the Part  */  
   PartNum:string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   RevisionNum:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if its a valid Part.  */  
   IUM:string,
      /**  Price per unit for the Contract in base currency.  Defaults from the FScontCd table  */  
   PricePerUnit:number,
      /**  Price per unit for the Contract in customers currency.  Defaults from the FScontCd table  */  
   DocPricePerUnit:number,
      /**  Total Contract Quantity for the line item.  */  
   ContractQty:number,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   XPartNum:string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   XRevisionNum:string,
      /**  Used to establish invoice comments about the Contract line item. These will copied into the Invoice detail  file as defaults.  */  
   InvoiceComment:string,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the FSContDt records for a specific customer.  */  
   CustNum:number,
      /**  Contains the Order Number that ties this detail record back to an OrderHed record.  */  
   OrderNum:number,
      /**  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   OrderLine:number,
      /**  Project ID of the Project table record that this FSContDt record. Can be blank.  */  
   ProjectID:string,
      /**  Editor widget for Contract comments.  */  
   CommentText:string,
      /**   A value of "ORD-ENT" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.
(Duplicated from FSContHd for Browse)  */  
   ContractType:string,
      /**  Contains comments about the detail contract line item. These will be printed on the Sales Acknowledgements and service contracts  */  
   ContractComment:string,
      /**  Sold to Order Number  */  
   SoldOrderNum:number,
      /**  Sold To Order line  */  
   SoldOrderLine:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Reporting currency value of this field  */  
   Rpt1PricePerUnit:number,
      /**  Reporting currency value of this field  */  
   Rpt2PricePerUnit:number,
      /**  Reporting currency value of this field  */  
   Rpt3PricePerUnit:number,
      /**  A value of Yes indicates the line is not part of the service contract agreement and it will not be included in the contract amounts.  */  
   Inactive:boolean,
      /**  This is the date the contract line was set to inactive.  */  
   DateInactivated:string,
      /**  This is the first date the contract line is considered for billing purposes.  */  
   BillStartDate:string,
      /**  This is the last date the contract line is considered for billing.  */  
   BillEndDate:string,
      /**  Indicates this line has been invoiced.  */  
   Invoiced:boolean,
      /**  Date this line was invoiced.  */  
   DateInvoiced:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   AllowUpdate:boolean,
   CurrencySwitch:boolean,
   BaseCurrSymbol:string,
   ExtPrice:number,
   DocExtPrice:number,
   DisplayContractType:string,
      /**  Return Quantity used in the create RMA process.  */  
   ReturnQty:number,
      /**  Indicates if the contract line is selected to create RMA for.  */  
   SelectedforRMA:boolean,
   HdCurrencyCode:string,
   HdCurrencyCodeDesc:string,
      /**  Document currency symbol.  */  
   DocCurrSymbol:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  Unit of Measure Description  */  
   IUMDesc:string,
   TrackSerialNumbers:boolean,
   Rpt1ExtPrice:number,
   Rpt2ExtPrice:number,
   Rpt3ExtPrice:number,
      /**  The calculated PriceMulti is based on the parent FSContHd record.  */  
   PriceMulti:number,
      /**  Unique identifier of related integration record.  */  
   IntExternalKey:string,
   BitFlag:number,
   ContractCodeContractDescription:string,
   CustNumBTName:string,
   CustNumCustID:string,
   CustNumName:string,
   OrderLineLineDesc:string,
   OrderNumCurrencyCode:string,
   OrderNumCardMemberName:string,
   PartNumTrackSerialNum:boolean,
   PartNumPricePerCode:string,
   PartNumSalesUM:string,
   PartNumIUM:string,
   PartNumSellingFactor:number,
   PartNumTrackDimension:boolean,
   PartNumPartDescription:string,
   PartNumTrackLots:boolean,
   ProdCodeDescription:string,
   ProjectIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ServiceContractDtSearchTableset{
   FSContDt:Erp_Tablesets_FSContDtRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtServiceContractDtSearchTableset{
   FSContDt:Erp_Tablesets_FSContDtRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param contractNum
      @param contractLine
   */  
export interface GetByID_input{
   contractNum:number,
   contractLine:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ServiceContractDtSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ServiceContractDtSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ServiceContractDtSearchTableset[],
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
   returnObj:Erp_Tablesets_FSContDtListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param contractNum
   */  
export interface GetNewFSContDt_input{
   ds:Erp_Tablesets_ServiceContractDtSearchTableset[],
   contractNum:number,
}

export interface GetNewFSContDt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractDtSearchTableset,
}
}

   /** Required : 
      @param whereClauseFSContDt
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseFSContDt:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ServiceContractDtSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtServiceContractDtSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtServiceContractDtSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ServiceContractDtSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractDtSearchTableset,
}
}

