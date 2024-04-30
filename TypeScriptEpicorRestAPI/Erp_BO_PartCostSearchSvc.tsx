import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PartCostSearchSvc
// Description: PartCostSearch retrieves the information about Part Costs
           Used to retrieve the Part Costs and its Totals
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/$metadata", {
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
   Description: Get PartCostSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartCostSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartCostRow
   */  
export function get_PartCostSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartCostRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/PartCostSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartCostRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartCostSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartCostRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PartCostRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartCostSearches(requestBody:Erp_Tablesets_PartCostRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/PartCostSearches", {
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
   Summary: Calls GetByID to retrieve the PartCostSearch item
   Description: Calls GetByID to retrieve the PartCostSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartCostSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param CostID Desc: CostID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PartCostRow
   */  
export function get_PartCostSearches_Company_PartNum_CostID(Company:string, PartNum:string, CostID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartCostRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/PartCostSearches(" + Company + "," + PartNum + "," + CostID + ")", {
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
         resolve(data as Erp_Tablesets_PartCostRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PartCostSearch for the service
   Description: Calls UpdateExt to update PartCostSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartCostSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param CostID Desc: CostID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartCostRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PartCostSearches_Company_PartNum_CostID(Company:string, PartNum:string, CostID:string, requestBody:Erp_Tablesets_PartCostRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/PartCostSearches(" + Company + "," + PartNum + "," + CostID + ")", {
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
   Summary: Call UpdateExt to delete PartCostSearch item
   Description: Call UpdateExt to delete PartCostSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartCostSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param CostID Desc: CostID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PartCostSearches_Company_PartNum_CostID(Company:string, PartNum:string, CostID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/PartCostSearches(" + Company + "," + PartNum + "," + CostID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartCostListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartCostListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartCostListRow)
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
export function get_GetRows(whereClausePartCost:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePartCost!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartCost=" + whereClausePartCost
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/GetRows" + params, {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(partNum:string, costID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof partNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "partNum=" + partNum
   }
   if(typeof costID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "costID=" + costID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewPartCost
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartCost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPartCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartCost(requestBody:GetNewPartCost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPartCost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/GetNewPartCost", {
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
         resolve(data as GetNewPartCost_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartCostListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartCostListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartCostRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartCostRow,
}

export interface Erp_Tablesets_PartCostListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique part number that identifies this part.  */  
   "PartNum":string,
      /**  Included in the unique index this value allows the Part to have different costs in different Sites.  Default value for CostID = 1.  */  
   "CostID":string,
      /**   Average Unit Labor Cost of the Part. This is an optional field. It is directly updated by Part Maintenance, indirectly by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program. Purchased Part receipts will roll this cost into average material cost and then set it to zeros.  Basically when updating an average cost the following logic is used.
 NEW AVG COST = ((ONHAND QTY * AVG COST) + TOTAL RECPT COST) / (ONHAND QTY + RECPT QTY).  Exceptions to this formula are if the onhand qty begins as a negative, then its value is not included in the calculations.  If the receipt transaction is of negative value then the average cost will not be changed.
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the Part record are used as default cost in job material detail. The system is configurable to use either Average, Standard or Last unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  */  
   "AvgLaborCost":number,
      /**  Average burden unit cost. This is updated directly by Part Maintenance. It is indirectly updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the AvgLaborCost for the formula for calculating average unit costs.  */  
   "AvgBurdenCost":number,
      /**  Average Material Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  */  
   "AvgMaterialCost":number,
      /**  Average Subcontract Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  */  
   "AvgSubContCost":number,
      /**  Average Material Burden Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  */  
   "AvgMtlBurCost":number,
      /**   Standard Unit Labor Cost. Standard costs are directly maintainable via the Part Maintenance Program or indirectly by Bill of Material cost rollup program.
(See AvgLaborCost for more info.)  */  
   "StdLaborCost":number,
      /**  Standard Burden Unit Cost.
( see StdLaborCost for more info )  */  
   "StdBurdenCost":number,
      /**  Standard Material Unit cost. ( see StdLaborCost for more info).  */  
   "StdMaterialCost":number,
      /**   Standard Subcontract Unit cost.
( see StdLaborCost for more info).  */  
   "StdSubContCost":number,
      /**   Standard Material Burden Unit cost.
( see StdLaborCost for more info).  */  
   "StdMtlBurCost":number,
      /**  Last Labor cost. Directly updated via the Part Master Maintenance program. Indirectly via Purchase Part receipts, Manufactured receipts or inventory cost adjustments if cost method is "last cost" .  The last costs are overlaid by the most recent receipt cost.  Both LastLaborCost and LastBurdenCost are set to zero when updated by a Purchased Part Receipt transaction.  */  
   "LastLaborCost":number,
      /**   Last Burden Unit Cost.
( see LastLaborCost for more info )  */  
   "LastBurdenCost":number,
      /**  Last Material unit cost. ( see LastLaborCost for more info. )  */  
   "LastMaterialCost":number,
      /**   Last Subcontract unit cost.
( see LastLaborCost for more info. )  */  
   "LastSubContCost":number,
      /**   Last Material Burden unit cost.
( see LastLaborCost for more info. )  */  
   "LastMtlBurCost":number,
      /**   FIFO Average Unit Labor Cost of the Part and updated only if the cost method is FIFO. This is an optional field. It is directly updated by Part Maintenance, indirectly by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program. Basically when updating a FIFO average cost the following logic is used.
 NEW FIFO AVG COST = sum of all (FIFO OnHandQty * FIFO Costs).
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the PartCost record are used as default cost in job material detail. The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part and CostID combination. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  */  
   "FIFOAvgLaborCost":number,
      /**  FIFO Average burden unit cost. This is updated directly by Part Maintenance. It is indirectly updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the FIFOAvgLaborCost for the formula for calculating FIFO average unit costs.  */  
   "FIFOAvgBurdenCost":number,
      /**  FIFO Average Material Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOAvgLaborCost description for explanation of updating with the receipts cost.  */  
   "FIFOAvgMaterialCost":number,
      /**  FIFO Average Subcontract Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOAvgLaborCost description for explanation of updating with the receipts cost.  */  
   "FIFOAvgSubContCost":number,
      /**  FIFOAverage Material Burden Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOAvgLaborCost description for explanation of updating with the receipts cost.  */  
   "FIFOAvgMtlBurCost":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The sum of AvgBurdenCost, AvgLaborCost, AvgMaterialCost, AvgMtlBurCost and AvgSubContCost  */  
   "AvgTotalCost":number,
      /**  The sum of StdBurdenCost, StdLaborCost, StdMaterialCost, StdMtlBurCost and StdSubContCost  */  
   "StdTotalCost":number,
      /**  The sum of LastBurdenCost, LastLaborCost, LastMaterialCost, LastMtlBurCost and LastSubContCost  */  
   "LastTotalCost":number,
   "PrimaryPlant":string,
      /**  used to display Cost Method description  */  
   "CostMethodDisplay":string,
      /**  The sum of FIFOAvgBurdenCost, FIFOAvgLaborCost, FIFOAvgMaterialCost, FIFOAvgMtlBurCost and FIFOAvgSubContCost  */  
   "FIFOAvgTotalCost":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartCostRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique part number that identifies this part.  */  
   "PartNum":string,
      /**  Included in the unique index this value allows the Part to have different costs in different Sites.  Default value for CostID = 1.  */  
   "CostID":string,
      /**   Average Unit Labor Cost of the Part. This is an optional field. It is directly updated by Part Maintenance, indirectly by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program. Purchased Part receipts will roll this cost into average material cost and then set it to zeros.  Basically when updating an average cost the following logic is used.
 NEW AVG COST = ((ONHAND QTY * AVG COST) + TOTAL RECPT COST) / (ONHAND QTY + RECPT QTY).  Exceptions to this formula are if the onhand qty begins as a negative, then its value is not included in the calculations.  If the receipt transaction is of negative value then the average cost will not be changed.
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the Part record are used as default cost in job material detail. The system is configurable to use either Average, Standard or Last unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  */  
   "AvgLaborCost":number,
      /**  Average burden unit cost. This is updated directly by Part Maintenance. It is indirectly updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the AvgLaborCost for the formula for calculating average unit costs.  */  
   "AvgBurdenCost":number,
      /**  Average Material Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  */  
   "AvgMaterialCost":number,
      /**  Average Subcontract Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  */  
   "AvgSubContCost":number,
      /**  Average Material Burden Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  */  
   "AvgMtlBurCost":number,
      /**   Standard Unit Labor Cost. Standard costs are directly maintainable via the Part Maintenance Program or indirectly by Bill of Material cost rollup program.
(See AvgLaborCost for more info.)  */  
   "StdLaborCost":number,
      /**  Standard Burden Unit Cost.
( see StdLaborCost for more info )  */  
   "StdBurdenCost":number,
      /**  Standard Material Unit cost. ( see StdLaborCost for more info).  */  
   "StdMaterialCost":number,
      /**   Standard Subcontract Unit cost.
( see StdLaborCost for more info).  */  
   "StdSubContCost":number,
      /**   Standard Material Burden Unit cost.
( see StdLaborCost for more info).  */  
   "StdMtlBurCost":number,
      /**  Last Labor cost. Directly updated via the Part Master Maintenance program. Indirectly via Purchase Part receipts, Manufactured receipts or inventory cost adjustments if cost method is "last cost" .  The last costs are overlaid by the most recent receipt cost.  Both LastLaborCost and LastBurdenCost are set to zero when updated by a Purchased Part Receipt transaction.  */  
   "LastLaborCost":number,
      /**   Last Burden Unit Cost.
( see LastLaborCost for more info )  */  
   "LastBurdenCost":number,
      /**  Last Material unit cost. ( see LastLaborCost for more info. )  */  
   "LastMaterialCost":number,
      /**   Last Subcontract unit cost.
( see LastLaborCost for more info. )  */  
   "LastSubContCost":number,
      /**   Last Material Burden unit cost.
( see LastLaborCost for more info. )  */  
   "LastMtlBurCost":number,
      /**   FIFO Average Unit Labor Cost of the Part and updated only if the cost method is FIFO. This is an optional field. It is directly updated by Part Maintenance, indirectly by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program. Basically when updating a FIFO average cost the following logic is used.
 NEW FIFO AVG COST = sum of all (FIFO OnHandQty * FIFO Costs).
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the PartCost record are used as default cost in job material detail. The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part and CostID combination. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  */  
   "FIFOAvgLaborCost":number,
      /**  FIFO Average burden unit cost. This is updated directly by Part Maintenance. It is indirectly updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the FIFOAvgLaborCost for the formula for calculating FIFO average unit costs.  */  
   "FIFOAvgBurdenCost":number,
      /**  FIFO Average Material Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOAvgLaborCost description for explanation of updating with the receipts cost.  */  
   "FIFOAvgMaterialCost":number,
      /**  FIFO Average Subcontract Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOAvgLaborCost description for explanation of updating with the receipts cost.  */  
   "FIFOAvgSubContCost":number,
      /**  FIFOAverage Material Burden Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOAvgLaborCost description for explanation of updating with the receipts cost.  */  
   "FIFOAvgMtlBurCost":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Total OnHand Quantity used specific for Average Costing calculations  */  
   "TotalQtyAvg":number,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   "ExternalMESSyncRequired":boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   "ExternalMESLastSync":string,
      /**  used to display Cost Method description  */  
   "CostMethodDisplay":string,
      /**  The sum of FIFOAvgBurdenCost, FIFOAvgLaborCost, FIFOAvgMaterialCost, FIFOAvgMtlBurCost and FIFOAvgSubContCost  */  
   "FIFOAvgTotalCost":number,
      /**  The sum of LastBurdenCost, LastLaborCost, LastMaterialCost, LastMtlBurCost and LastSubContCost  */  
   "LastTotalCost":number,
   "PrimaryPlant":string,
      /**  The sum of StdBurdenCost, StdLaborCost, StdMaterialCost, StdMtlBurCost and StdSubContCost  */  
   "StdTotalCost":number,
      /**  The sum of AvgBurdenCost, AvgLaborCost, AvgMaterialCost, AvgMtlBurCost and AvgSubContCost  */  
   "AvgTotalCost":number,
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
      @param partNum
      @param costID
   */  
export interface DeleteByID_input{
   partNum:string,
   costID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PartCostListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  Included in the unique index this value allows the Part to have different costs in different Sites.  Default value for CostID = 1.  */  
   CostID:string,
      /**   Average Unit Labor Cost of the Part. This is an optional field. It is directly updated by Part Maintenance, indirectly by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program. Purchased Part receipts will roll this cost into average material cost and then set it to zeros.  Basically when updating an average cost the following logic is used.
 NEW AVG COST = ((ONHAND QTY * AVG COST) + TOTAL RECPT COST) / (ONHAND QTY + RECPT QTY).  Exceptions to this formula are if the onhand qty begins as a negative, then its value is not included in the calculations.  If the receipt transaction is of negative value then the average cost will not be changed.
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the Part record are used as default cost in job material detail. The system is configurable to use either Average, Standard or Last unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  */  
   AvgLaborCost:number,
      /**  Average burden unit cost. This is updated directly by Part Maintenance. It is indirectly updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the AvgLaborCost for the formula for calculating average unit costs.  */  
   AvgBurdenCost:number,
      /**  Average Material Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  */  
   AvgMaterialCost:number,
      /**  Average Subcontract Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  */  
   AvgSubContCost:number,
      /**  Average Material Burden Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  */  
   AvgMtlBurCost:number,
      /**   Standard Unit Labor Cost. Standard costs are directly maintainable via the Part Maintenance Program or indirectly by Bill of Material cost rollup program.
(See AvgLaborCost for more info.)  */  
   StdLaborCost:number,
      /**  Standard Burden Unit Cost.
( see StdLaborCost for more info )  */  
   StdBurdenCost:number,
      /**  Standard Material Unit cost. ( see StdLaborCost for more info).  */  
   StdMaterialCost:number,
      /**   Standard Subcontract Unit cost.
( see StdLaborCost for more info).  */  
   StdSubContCost:number,
      /**   Standard Material Burden Unit cost.
( see StdLaborCost for more info).  */  
   StdMtlBurCost:number,
      /**  Last Labor cost. Directly updated via the Part Master Maintenance program. Indirectly via Purchase Part receipts, Manufactured receipts or inventory cost adjustments if cost method is "last cost" .  The last costs are overlaid by the most recent receipt cost.  Both LastLaborCost and LastBurdenCost are set to zero when updated by a Purchased Part Receipt transaction.  */  
   LastLaborCost:number,
      /**   Last Burden Unit Cost.
( see LastLaborCost for more info )  */  
   LastBurdenCost:number,
      /**  Last Material unit cost. ( see LastLaborCost for more info. )  */  
   LastMaterialCost:number,
      /**   Last Subcontract unit cost.
( see LastLaborCost for more info. )  */  
   LastSubContCost:number,
      /**   Last Material Burden unit cost.
( see LastLaborCost for more info. )  */  
   LastMtlBurCost:number,
      /**   FIFO Average Unit Labor Cost of the Part and updated only if the cost method is FIFO. This is an optional field. It is directly updated by Part Maintenance, indirectly by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program. Basically when updating a FIFO average cost the following logic is used.
 NEW FIFO AVG COST = sum of all (FIFO OnHandQty * FIFO Costs).
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the PartCost record are used as default cost in job material detail. The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part and CostID combination. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  */  
   FIFOAvgLaborCost:number,
      /**  FIFO Average burden unit cost. This is updated directly by Part Maintenance. It is indirectly updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the FIFOAvgLaborCost for the formula for calculating FIFO average unit costs.  */  
   FIFOAvgBurdenCost:number,
      /**  FIFO Average Material Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOAvgLaborCost description for explanation of updating with the receipts cost.  */  
   FIFOAvgMaterialCost:number,
      /**  FIFO Average Subcontract Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOAvgLaborCost description for explanation of updating with the receipts cost.  */  
   FIFOAvgSubContCost:number,
      /**  FIFOAverage Material Burden Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOAvgLaborCost description for explanation of updating with the receipts cost.  */  
   FIFOAvgMtlBurCost:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The sum of AvgBurdenCost, AvgLaborCost, AvgMaterialCost, AvgMtlBurCost and AvgSubContCost  */  
   AvgTotalCost:number,
      /**  The sum of StdBurdenCost, StdLaborCost, StdMaterialCost, StdMtlBurCost and StdSubContCost  */  
   StdTotalCost:number,
      /**  The sum of LastBurdenCost, LastLaborCost, LastMaterialCost, LastMtlBurCost and LastSubContCost  */  
   LastTotalCost:number,
   PrimaryPlant:string,
      /**  used to display Cost Method description  */  
   CostMethodDisplay:string,
      /**  The sum of FIFOAvgBurdenCost, FIFOAvgLaborCost, FIFOAvgMaterialCost, FIFOAvgMtlBurCost and FIFOAvgSubContCost  */  
   FIFOAvgTotalCost:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartCostListTableset{
   PartCostList:Erp_Tablesets_PartCostListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartCostRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  Included in the unique index this value allows the Part to have different costs in different Sites.  Default value for CostID = 1.  */  
   CostID:string,
      /**   Average Unit Labor Cost of the Part. This is an optional field. It is directly updated by Part Maintenance, indirectly by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program. Purchased Part receipts will roll this cost into average material cost and then set it to zeros.  Basically when updating an average cost the following logic is used.
 NEW AVG COST = ((ONHAND QTY * AVG COST) + TOTAL RECPT COST) / (ONHAND QTY + RECPT QTY).  Exceptions to this formula are if the onhand qty begins as a negative, then its value is not included in the calculations.  If the receipt transaction is of negative value then the average cost will not be changed.
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the Part record are used as default cost in job material detail. The system is configurable to use either Average, Standard or Last unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  */  
   AvgLaborCost:number,
      /**  Average burden unit cost. This is updated directly by Part Maintenance. It is indirectly updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the AvgLaborCost for the formula for calculating average unit costs.  */  
   AvgBurdenCost:number,
      /**  Average Material Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  */  
   AvgMaterialCost:number,
      /**  Average Subcontract Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  */  
   AvgSubContCost:number,
      /**  Average Material Burden Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  */  
   AvgMtlBurCost:number,
      /**   Standard Unit Labor Cost. Standard costs are directly maintainable via the Part Maintenance Program or indirectly by Bill of Material cost rollup program.
(See AvgLaborCost for more info.)  */  
   StdLaborCost:number,
      /**  Standard Burden Unit Cost.
( see StdLaborCost for more info )  */  
   StdBurdenCost:number,
      /**  Standard Material Unit cost. ( see StdLaborCost for more info).  */  
   StdMaterialCost:number,
      /**   Standard Subcontract Unit cost.
( see StdLaborCost for more info).  */  
   StdSubContCost:number,
      /**   Standard Material Burden Unit cost.
( see StdLaborCost for more info).  */  
   StdMtlBurCost:number,
      /**  Last Labor cost. Directly updated via the Part Master Maintenance program. Indirectly via Purchase Part receipts, Manufactured receipts or inventory cost adjustments if cost method is "last cost" .  The last costs are overlaid by the most recent receipt cost.  Both LastLaborCost and LastBurdenCost are set to zero when updated by a Purchased Part Receipt transaction.  */  
   LastLaborCost:number,
      /**   Last Burden Unit Cost.
( see LastLaborCost for more info )  */  
   LastBurdenCost:number,
      /**  Last Material unit cost. ( see LastLaborCost for more info. )  */  
   LastMaterialCost:number,
      /**   Last Subcontract unit cost.
( see LastLaborCost for more info. )  */  
   LastSubContCost:number,
      /**   Last Material Burden unit cost.
( see LastLaborCost for more info. )  */  
   LastMtlBurCost:number,
      /**   FIFO Average Unit Labor Cost of the Part and updated only if the cost method is FIFO. This is an optional field. It is directly updated by Part Maintenance, indirectly by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program. Basically when updating a FIFO average cost the following logic is used.
 NEW FIFO AVG COST = sum of all (FIFO OnHandQty * FIFO Costs).
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the PartCost record are used as default cost in job material detail. The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part and CostID combination. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  */  
   FIFOAvgLaborCost:number,
      /**  FIFO Average burden unit cost. This is updated directly by Part Maintenance. It is indirectly updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the FIFOAvgLaborCost for the formula for calculating FIFO average unit costs.  */  
   FIFOAvgBurdenCost:number,
      /**  FIFO Average Material Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOAvgLaborCost description for explanation of updating with the receipts cost.  */  
   FIFOAvgMaterialCost:number,
      /**  FIFO Average Subcontract Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOAvgLaborCost description for explanation of updating with the receipts cost.  */  
   FIFOAvgSubContCost:number,
      /**  FIFOAverage Material Burden Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOAvgLaborCost description for explanation of updating with the receipts cost.  */  
   FIFOAvgMtlBurCost:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Total OnHand Quantity used specific for Average Costing calculations  */  
   TotalQtyAvg:number,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
      /**  used to display Cost Method description  */  
   CostMethodDisplay:string,
      /**  The sum of FIFOAvgBurdenCost, FIFOAvgLaborCost, FIFOAvgMaterialCost, FIFOAvgMtlBurCost and FIFOAvgSubContCost  */  
   FIFOAvgTotalCost:number,
      /**  The sum of LastBurdenCost, LastLaborCost, LastMaterialCost, LastMtlBurCost and LastSubContCost  */  
   LastTotalCost:number,
   PrimaryPlant:string,
      /**  The sum of StdBurdenCost, StdLaborCost, StdMaterialCost, StdMtlBurCost and StdSubContCost  */  
   StdTotalCost:number,
      /**  The sum of AvgBurdenCost, AvgLaborCost, AvgMaterialCost, AvgMtlBurCost and AvgSubContCost  */  
   AvgTotalCost:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartCostSearchTableset{
   PartCost:Erp_Tablesets_PartCostRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPartCostSearchTableset{
   PartCost:Erp_Tablesets_PartCostRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param partNum
      @param costID
   */  
export interface GetByID_input{
   partNum:string,
   costID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PartCostSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PartCostSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PartCostSearchTableset[],
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
   returnObj:Erp_Tablesets_PartCostListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param partNum
   */  
export interface GetNewPartCost_input{
   ds:Erp_Tablesets_PartCostSearchTableset[],
   partNum:string,
}

export interface GetNewPartCost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartCostSearchTableset,
}
}

   /** Required : 
      @param whereClausePartCost
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePartCost:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PartCostSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtPartCostSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPartCostSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PartCostSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartCostSearchTableset,
}
}

