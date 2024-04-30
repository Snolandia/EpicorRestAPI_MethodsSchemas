import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.CostPartSearchSvc
// Description: Cost Part Search
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/$metadata", {
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
   Description: Get CostPartSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CostPartSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CostPartRow
   */  
export function get_CostPartSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/CostPartSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CostPartSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CostPartRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CostPartRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CostPartSearches(requestBody:Erp_Tablesets_CostPartRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/CostPartSearches", {
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
   Summary: Calls GetByID to retrieve the CostPartSearch item
   Description: Calls GetByID to retrieve the CostPartSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CostPartSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CostPartRow
   */  
export function get_CostPartSearches_Company_GroupID_TypeCode_PartNum(Company:string, GroupID:string, TypeCode:string, PartNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CostPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/CostPartSearches(" + Company + "," + GroupID + "," + TypeCode + "," + PartNum + ")", {
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
         resolve(data as Erp_Tablesets_CostPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CostPartSearch for the service
   Description: Calls UpdateExt to update CostPartSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CostPartSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CostPartRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CostPartSearches_Company_GroupID_TypeCode_PartNum(Company:string, GroupID:string, TypeCode:string, PartNum:string, requestBody:Erp_Tablesets_CostPartRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/CostPartSearches(" + Company + "," + GroupID + "," + TypeCode + "," + PartNum + ")", {
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
   Summary: Call UpdateExt to delete CostPartSearch item
   Description: Call UpdateExt to delete CostPartSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CostPartSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CostPartSearches_Company_GroupID_TypeCode_PartNum(Company:string, GroupID:string, TypeCode:string, PartNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/CostPartSearches(" + Company + "," + GroupID + "," + TypeCode + "," + PartNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CostPartListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostPartListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostPartListRow)
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
export function get_GetRows(whereClauseCostPart:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCostPart!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCostPart=" + whereClauseCostPart
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/GetRows" + params, {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(groupID:string, typeCode:string, partNum:string, epicorHeaders?:Headers){
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
   if(typeof typeCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "typeCode=" + typeCode
   }
   if(typeof partNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "partNum=" + partNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewCostPart
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCostPart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCostPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCostPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCostPart(requestBody:GetNewCostPart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCostPart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/GetNewCostPart", {
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
         resolve(data as GetNewCostPart_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostPartSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostPartListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CostPartListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostPartRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CostPartRow,
}

export interface Erp_Tablesets_CostPartListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  */  
   "GroupID":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  An abbreviated part description field by which the user can search the Part file. During Part maintenance a change to the Part.Description field causes this field to be updated with the first 8 bytes of the Part.Description.  */  
   "SearchWord":string,
      /**  Describes the Part.  This field can not be blank.  */  
   "PartDescription":string,
      /**   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
Classes could be set up for different type of raw materials.  */  
   "ClassID":string,
      /**   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  */  
   "TypeCode":string,
      /**  Product Group ID for the Cost Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection.  */  
   "ProdCode":string,
      /**   Standard Unit Labor Cost. Standard costs are directly maintainable via the Part Maintenance Program or indirectly by Bill of Material cost rollup program.

(See AvgLaborCost for more info.)  */  
   "StdLaborCost":number,
      /**   Standard Burden Unit Cost.

( see StdLaborCost for more info )  */  
   "StdBurdenCost":number,
      /**   Standard Material Unit cost.

( see StdLaborCost for more info).  */  
   "StdMaterialCost":number,
      /**   Standard Subcontract Unit cost.
( see StdLaborCost for more info).  */  
   "StdSubContCost":number,
      /**   Standard Material Burden Unit cost.
( see StdLaborCost for more info).  */  
   "StdMtlBurCost":number,
      /**  Revision number which is used to uniquely identify the revision of the part.  This was the revision used when the rollup was run.  If this field is blank the part is not part of the rollup processing and will not be posted.  */  
   "RevisionNum":string,
      /**  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  */  
   "EffectiveDate":string,
      /**  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   "TLRLaborCost":number,
      /**   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "TLRBurdenCost":number,
      /**  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "TLRMaterialCost":number,
      /**  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "TLRSubcontractCost":number,
      /**  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "TLRMtlBurCost":number,
      /**  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   "TLRSetupLaborCost":number,
      /**   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "TLRSetupBurdenCost":number,
      /**  Lower Level Unit Labor Cost calculated by the BOM Cost rollup routine. Lower level cost excludes costs from sub assemblies.  */  
   "LLRLaborCost":number,
      /**   Lower Level Unit Burden Cost calculated by the BOM Cost rollup routine. "Lower level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "LLRBurdenCost":number,
      /**  Lower Level Unit Material Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  */  
   "LLRMaterialCost":number,
      /**  Lower Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  */  
   "LLRSubcontractCost":number,
      /**  Lower Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  */  
   "LLRMtlBurCost":number,
      /**  Lower Level Setup Labor Cost calculated by the BOM Cost rollup routine. Lower level cost excludes costs from sub assemblies.  */  
   "LLRSetupLaborCost":number,
      /**   Lower Level Setup Burden Cost calculated by the BOM Cost rollup routine. "Lower level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "LLRSetupBurdenCost":number,
      /**  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  */  
   "RollupDate":string,
      /**  Alternate Routing method to be used for this revision.  */  
   "AltMethod":string,
      /**  For display purposes only.  Indicates if the record is linked to any of the manufactured parts in the CostPart table (CostPart.TypeCode = M).  CostPart, CostBurden, and CostLabor records are created based on the method of manufacturing of a part, but they can also be created regardless of the method of manufacturing.  A record is considered linked if it is used in the method of manufacturing structure of a manufactured part.  */  
   "Linked":boolean,
      /**  This is the lot size that is used when performing a BOM cost rollup to distribute setup costs.  */  
   "MfgLotSize":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "LastMaterialCost":number,
   "IsMethod":boolean,
   "ApprovedMethod":boolean,
   "CurrentRevisionNum":string,
   "CurrentRevDescription":string,
      /**  Description  */  
   "GroupIDDescription":string,
      /**  Full description of Product Group.  */  
   "ProdCodeDescription":string,
      /**  Short description of the revision. This is NOT the Part description.  */  
   "RevisionNumRevShortDesc":string,
      /**  The PartDescription from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  */  
   "RevisionNumPartDescription":string,
      /**  Used to enter a full description of the revision.  */  
   "RevisionNumRevDescription":string,
      /**  Full Description of the Type of task.  */  
   "TypeCodeTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CostPartRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  */  
   "GroupID":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  An abbreviated part description field by which the user can search the Part file. During Part maintenance a change to the Part.Description field causes this field to be updated with the first 8 bytes of the Part.Description.  */  
   "SearchWord":string,
      /**  Describes the Part.  This field can not be blank.  */  
   "PartDescription":string,
      /**   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
Classes could be set up for different type of raw materials.  */  
   "ClassID":string,
      /**   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  */  
   "TypeCode":string,
      /**  Product Group ID for the Cost Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection.  */  
   "ProdCode":string,
      /**   Standard Unit Labor Cost. Standard costs are directly maintainable via the Part Maintenance Program or indirectly by Bill of Material cost rollup program.

(See AvgLaborCost for more info.)  */  
   "StdLaborCost":number,
      /**   Standard Burden Unit Cost.

( see StdLaborCost for more info )  */  
   "StdBurdenCost":number,
      /**   Standard Material Unit cost.

( see StdLaborCost for more info).  */  
   "StdMaterialCost":number,
      /**   Standard Subcontract Unit cost.
( see StdLaborCost for more info).  */  
   "StdSubContCost":number,
      /**   Standard Material Burden Unit cost.
( see StdLaborCost for more info).  */  
   "StdMtlBurCost":number,
      /**  Revision number which is used to uniquely identify the revision of the part.  This was the revision used when the rollup was run.  If this field is blank the part is not part of the rollup processing and will not be posted.  */  
   "RevisionNum":string,
      /**  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  */  
   "EffectiveDate":string,
      /**  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   "TLRLaborCost":number,
      /**   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "TLRBurdenCost":number,
      /**  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "TLRMaterialCost":number,
      /**  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "TLRSubcontractCost":number,
      /**  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "TLRMtlBurCost":number,
      /**  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   "TLRSetupLaborCost":number,
      /**   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "TLRSetupBurdenCost":number,
      /**  Lower Level Unit Labor Cost calculated by the BOM Cost rollup routine. Lower level cost excludes costs from sub assemblies.  */  
   "LLRLaborCost":number,
      /**   Lower Level Unit Burden Cost calculated by the BOM Cost rollup routine. "Lower level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "LLRBurdenCost":number,
      /**  Lower Level Unit Material Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  */  
   "LLRMaterialCost":number,
      /**  Lower Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  */  
   "LLRSubcontractCost":number,
      /**  Lower Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  */  
   "LLRMtlBurCost":number,
      /**  Lower Level Setup Labor Cost calculated by the BOM Cost rollup routine. Lower level cost excludes costs from sub assemblies.  */  
   "LLRSetupLaborCost":number,
      /**   Lower Level Setup Burden Cost calculated by the BOM Cost rollup routine. "Lower level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "LLRSetupBurdenCost":number,
      /**  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  */  
   "RollupDate":string,
      /**  Alternate Routing method to be used for this revision.  */  
   "AltMethod":string,
      /**  For display purposes only.  Indicates if the record is linked to any of the manufactured parts in the CostPart table (CostPart.TypeCode = M).  CostPart, CostBurden, and CostLabor records are created based on the method of manufacturing of a part, but they can also be created regardless of the method of manufacturing.  A record is considered linked if it is used in the method of manufacturing structure of a manufactured part.  */  
   "Linked":boolean,
      /**  This is the lot size that is used when performing a BOM cost rollup to distribute setup costs.  */  
   "MfgLotSize":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PrimCostPart  */  
   "PrimCostPart":string,
      /**  PrimCostRev  */  
   "PrimCostRev":string,
      /**  PrimCostAltMethod  */  
   "PrimCostAltMethod":string,
      /**  CoPartsReqQty  */  
   "CoPartsReqQty":number,
      /**  MtlCostPct  */  
   "MtlCostPct":number,
      /**  LaborCostPct  */  
   "LaborCostPct":number,
      /**  OrigStdMaterialCost  */  
   "OrigStdMaterialCost":number,
      /**  OrigStdLaborCost  */  
   "OrigStdLaborCost":number,
      /**  OrigStdBurdenCost  */  
   "OrigStdBurdenCost":number,
      /**  OrigStdSubContCost  */  
   "OrigStdSubContCost":number,
      /**  OrigStdMtlBurCost  */  
   "OrigStdMtlBurCost":number,
      /**  IsTransferCostID  */  
   "IsTransferCostID":boolean,
   "ApprovedMethod":boolean,
   "CurrentRevDescription":string,
   "CurrentRevisionNum":string,
   "IsMethod":boolean,
   "LastMaterialCost":number,
   "BitFlag":number,
   "GroupIDDescription":string,
   "ProdCodeDescription":string,
   "RevisionNumRevDescription":string,
   "RevisionNumRevShortDesc":string,
   "RevisionNumPartDescription":string,
   "TypeCodeTypeDescription":string,
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
      @param typeCode
      @param partNum
   */  
export interface DeleteByID_input{
   groupID:string,
   typeCode:string,
   partNum:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_CostPartListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  */  
   GroupID:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  An abbreviated part description field by which the user can search the Part file. During Part maintenance a change to the Part.Description field causes this field to be updated with the first 8 bytes of the Part.Description.  */  
   SearchWord:string,
      /**  Describes the Part.  This field can not be blank.  */  
   PartDescription:string,
      /**   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
Classes could be set up for different type of raw materials.  */  
   ClassID:string,
      /**   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  */  
   TypeCode:string,
      /**  Product Group ID for the Cost Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection.  */  
   ProdCode:string,
      /**   Standard Unit Labor Cost. Standard costs are directly maintainable via the Part Maintenance Program or indirectly by Bill of Material cost rollup program.

(See AvgLaborCost for more info.)  */  
   StdLaborCost:number,
      /**   Standard Burden Unit Cost.

( see StdLaborCost for more info )  */  
   StdBurdenCost:number,
      /**   Standard Material Unit cost.

( see StdLaborCost for more info).  */  
   StdMaterialCost:number,
      /**   Standard Subcontract Unit cost.
( see StdLaborCost for more info).  */  
   StdSubContCost:number,
      /**   Standard Material Burden Unit cost.
( see StdLaborCost for more info).  */  
   StdMtlBurCost:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  This was the revision used when the rollup was run.  If this field is blank the part is not part of the rollup processing and will not be posted.  */  
   RevisionNum:string,
      /**  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  */  
   EffectiveDate:string,
      /**  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   TLRLaborCost:number,
      /**   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   TLRBurdenCost:number,
      /**  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   TLRMaterialCost:number,
      /**  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   TLRSubcontractCost:number,
      /**  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   TLRMtlBurCost:number,
      /**  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   TLRSetupLaborCost:number,
      /**   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   TLRSetupBurdenCost:number,
      /**  Lower Level Unit Labor Cost calculated by the BOM Cost rollup routine. Lower level cost excludes costs from sub assemblies.  */  
   LLRLaborCost:number,
      /**   Lower Level Unit Burden Cost calculated by the BOM Cost rollup routine. "Lower level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   LLRBurdenCost:number,
      /**  Lower Level Unit Material Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  */  
   LLRMaterialCost:number,
      /**  Lower Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  */  
   LLRSubcontractCost:number,
      /**  Lower Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  */  
   LLRMtlBurCost:number,
      /**  Lower Level Setup Labor Cost calculated by the BOM Cost rollup routine. Lower level cost excludes costs from sub assemblies.  */  
   LLRSetupLaborCost:number,
      /**   Lower Level Setup Burden Cost calculated by the BOM Cost rollup routine. "Lower level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   LLRSetupBurdenCost:number,
      /**  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  */  
   RollupDate:string,
      /**  Alternate Routing method to be used for this revision.  */  
   AltMethod:string,
      /**  For display purposes only.  Indicates if the record is linked to any of the manufactured parts in the CostPart table (CostPart.TypeCode = M).  CostPart, CostBurden, and CostLabor records are created based on the method of manufacturing of a part, but they can also be created regardless of the method of manufacturing.  A record is considered linked if it is used in the method of manufacturing structure of a manufactured part.  */  
   Linked:boolean,
      /**  This is the lot size that is used when performing a BOM cost rollup to distribute setup costs.  */  
   MfgLotSize:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   LastMaterialCost:number,
   IsMethod:boolean,
   ApprovedMethod:boolean,
   CurrentRevisionNum:string,
   CurrentRevDescription:string,
      /**  Description  */  
   GroupIDDescription:string,
      /**  Full description of Product Group.  */  
   ProdCodeDescription:string,
      /**  Short description of the revision. This is NOT the Part description.  */  
   RevisionNumRevShortDesc:string,
      /**  The PartDescription from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  */  
   RevisionNumPartDescription:string,
      /**  Used to enter a full description of the revision.  */  
   RevisionNumRevDescription:string,
      /**  Full Description of the Type of task.  */  
   TypeCodeTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CostPartListTableset{
   CostPartList:Erp_Tablesets_CostPartListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CostPartRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  */  
   GroupID:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  An abbreviated part description field by which the user can search the Part file. During Part maintenance a change to the Part.Description field causes this field to be updated with the first 8 bytes of the Part.Description.  */  
   SearchWord:string,
      /**  Describes the Part.  This field can not be blank.  */  
   PartDescription:string,
      /**   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
Classes could be set up for different type of raw materials.  */  
   ClassID:string,
      /**   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  */  
   TypeCode:string,
      /**  Product Group ID for the Cost Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection.  */  
   ProdCode:string,
      /**   Standard Unit Labor Cost. Standard costs are directly maintainable via the Part Maintenance Program or indirectly by Bill of Material cost rollup program.

(See AvgLaborCost for more info.)  */  
   StdLaborCost:number,
      /**   Standard Burden Unit Cost.

( see StdLaborCost for more info )  */  
   StdBurdenCost:number,
      /**   Standard Material Unit cost.

( see StdLaborCost for more info).  */  
   StdMaterialCost:number,
      /**   Standard Subcontract Unit cost.
( see StdLaborCost for more info).  */  
   StdSubContCost:number,
      /**   Standard Material Burden Unit cost.
( see StdLaborCost for more info).  */  
   StdMtlBurCost:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  This was the revision used when the rollup was run.  If this field is blank the part is not part of the rollup processing and will not be posted.  */  
   RevisionNum:string,
      /**  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  */  
   EffectiveDate:string,
      /**  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   TLRLaborCost:number,
      /**   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   TLRBurdenCost:number,
      /**  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   TLRMaterialCost:number,
      /**  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   TLRSubcontractCost:number,
      /**  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   TLRMtlBurCost:number,
      /**  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   TLRSetupLaborCost:number,
      /**   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   TLRSetupBurdenCost:number,
      /**  Lower Level Unit Labor Cost calculated by the BOM Cost rollup routine. Lower level cost excludes costs from sub assemblies.  */  
   LLRLaborCost:number,
      /**   Lower Level Unit Burden Cost calculated by the BOM Cost rollup routine. "Lower level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   LLRBurdenCost:number,
      /**  Lower Level Unit Material Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  */  
   LLRMaterialCost:number,
      /**  Lower Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  */  
   LLRSubcontractCost:number,
      /**  Lower Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  */  
   LLRMtlBurCost:number,
      /**  Lower Level Setup Labor Cost calculated by the BOM Cost rollup routine. Lower level cost excludes costs from sub assemblies.  */  
   LLRSetupLaborCost:number,
      /**   Lower Level Setup Burden Cost calculated by the BOM Cost rollup routine. "Lower level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   LLRSetupBurdenCost:number,
      /**  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  */  
   RollupDate:string,
      /**  Alternate Routing method to be used for this revision.  */  
   AltMethod:string,
      /**  For display purposes only.  Indicates if the record is linked to any of the manufactured parts in the CostPart table (CostPart.TypeCode = M).  CostPart, CostBurden, and CostLabor records are created based on the method of manufacturing of a part, but they can also be created regardless of the method of manufacturing.  A record is considered linked if it is used in the method of manufacturing structure of a manufactured part.  */  
   Linked:boolean,
      /**  This is the lot size that is used when performing a BOM cost rollup to distribute setup costs.  */  
   MfgLotSize:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PrimCostPart  */  
   PrimCostPart:string,
      /**  PrimCostRev  */  
   PrimCostRev:string,
      /**  PrimCostAltMethod  */  
   PrimCostAltMethod:string,
      /**  CoPartsReqQty  */  
   CoPartsReqQty:number,
      /**  MtlCostPct  */  
   MtlCostPct:number,
      /**  LaborCostPct  */  
   LaborCostPct:number,
      /**  OrigStdMaterialCost  */  
   OrigStdMaterialCost:number,
      /**  OrigStdLaborCost  */  
   OrigStdLaborCost:number,
      /**  OrigStdBurdenCost  */  
   OrigStdBurdenCost:number,
      /**  OrigStdSubContCost  */  
   OrigStdSubContCost:number,
      /**  OrigStdMtlBurCost  */  
   OrigStdMtlBurCost:number,
      /**  IsTransferCostID  */  
   IsTransferCostID:boolean,
   ApprovedMethod:boolean,
   CurrentRevDescription:string,
   CurrentRevisionNum:string,
   IsMethod:boolean,
   LastMaterialCost:number,
   BitFlag:number,
   GroupIDDescription:string,
   ProdCodeDescription:string,
   RevisionNumRevDescription:string,
   RevisionNumRevShortDesc:string,
   RevisionNumPartDescription:string,
   TypeCodeTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CostPartSearchTableset{
   CostPart:Erp_Tablesets_CostPartRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtCostPartSearchTableset{
   CostPart:Erp_Tablesets_CostPartRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param groupID
      @param typeCode
      @param partNum
   */  
export interface GetByID_input{
   groupID:string,
   typeCode:string,
   partNum:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CostPartSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CostPartSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CostPartSearchTableset[],
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
   returnObj:Erp_Tablesets_CostPartListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param groupID
      @param typeCode
   */  
export interface GetNewCostPart_input{
   ds:Erp_Tablesets_CostPartSearchTableset[],
   groupID:string,
   typeCode:string,
}

export interface GetNewCostPart_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostPartSearchTableset,
}
}

   /** Required : 
      @param whereClauseCostPart
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCostPart:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CostPartSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtCostPartSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCostPartSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CostPartSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostPartSearchTableset,
}
}

