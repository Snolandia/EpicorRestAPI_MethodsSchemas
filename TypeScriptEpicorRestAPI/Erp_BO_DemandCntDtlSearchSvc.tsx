import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.DemandCntDtlSearchSvc
// Description: Add your summary for this object here
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/$metadata", {
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
   Description: Get DemandCntDtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandCntDtlSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandContractDtlRow
   */  
export function get_DemandCntDtlSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandContractDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/DemandCntDtlSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandContractDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandCntDtlSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandContractDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.DemandContractDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DemandCntDtlSearches(requestBody:Erp_Tablesets_DemandContractDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/DemandCntDtlSearches", {
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
   Summary: Calls GetByID to retrieve the DemandCntDtlSearch item
   Description: Calls GetByID to retrieve the DemandCntDtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandCntDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandContractLine Desc: DemandContractLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DemandContractDtlRow
   */  
export function get_DemandCntDtlSearches_Company_DemandContractNum_DemandContractLine(Company:string, DemandContractNum:string, DemandContractLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemandContractDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/DemandCntDtlSearches(" + Company + "," + DemandContractNum + "," + DemandContractLine + ")", {
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
         resolve(data as Erp_Tablesets_DemandContractDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DemandCntDtlSearch for the service
   Description: Calls UpdateExt to update DemandCntDtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandCntDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandContractLine Desc: DemandContractLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandContractDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DemandCntDtlSearches_Company_DemandContractNum_DemandContractLine(Company:string, DemandContractNum:string, DemandContractLine:string, requestBody:Erp_Tablesets_DemandContractDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/DemandCntDtlSearches(" + Company + "," + DemandContractNum + "," + DemandContractLine + ")", {
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
   Summary: Call UpdateExt to delete DemandCntDtlSearch item
   Description: Call UpdateExt to delete DemandCntDtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandCntDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandContractLine Desc: DemandContractLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DemandCntDtlSearches_Company_DemandContractNum_DemandContractLine(Company:string, DemandContractNum:string, DemandContractLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/DemandCntDtlSearches(" + Company + "," + DemandContractNum + "," + DemandContractLine + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandContractDtlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandContractDtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandContractDtlListRow)
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
export function get_GetRows(whereClauseDemandContractDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseDemandContractDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDemandContractDtl=" + whereClauseDemandContractDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/GetRows" + params, {
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
export function get_GetByID(demandContractNum:string, demandContractLine:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof demandContractNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "demandContractNum=" + demandContractNum
   }
   if(typeof demandContractLine!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "demandContractLine=" + demandContractLine
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewDemandContractDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandContractDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDemandContractDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandContractDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDemandContractDtl(requestBody:GetNewDemandContractDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDemandContractDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/GetNewDemandContractDtl", {
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
         resolve(data as GetNewDemandContractDtl_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandContractDtlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DemandContractDtlListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandContractDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DemandContractDtlRow,
}

export interface Erp_Tablesets_DemandContractDtlListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  System assigned internal number to uniquely identify the demand contract record.  Is the link to the DemandContractHdr table.  */  
   "DemandContractNum":number,
      /**  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandContractDtl record for the contract and the adding 1 to it.  */  
   "DemandContractLine":number,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.
A default should be made when the DemandContractDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table.  */  
   "PartNum":string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   "XPartNum":string,
      /**  Determines whether or not this contract line is being run in a test mode. When contracts are first set up for EDI it is useful to send all documents in test mode so trading partners can verify the data before going into production mode.  */  
   "TestRecord":boolean,
      /**  The total selling quantity expected to be ordered for this line over the life of the contract.  */  
   "SellingTotalContractQty":number,
      /**  The total quantity expected to be ordered for this line over the life of the contract.  */  
   "TotalContractQty":number,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "LineDesc":string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   "IUM":string,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the Customer.DiscountPercent.  */  
   "DiscountPercent":number,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "UnitPrice":number,
      /**  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   "PricePerCode":string,
      /**  Project ID of the Project table record for this DemandContractDtl record. Can be blank.  */  
   "ProjectID":string,
      /**  This is the Price Group ID used to price the order line with.  */  
   "PriceGroupCode":string,
      /**  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   "SalesUM":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "SellingFactor":number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "SellingFactorDirection":string,
      /**  Comments about the demand detail line.  */  
   "DetailComments":string,
      /**  Use standard Epicor Price matrix/logic  */  
   "UsePriceList":boolean,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Total invoice amount of orders lines invoiced for this contract line in base currency. This field has a true sign. (credit memos are negative).  */  
   "TotalInvoiceAmt":number,
      /**  Total  amount of orders for this contract line in base currency. This field has a true sign. (credit memos are negative).  */  
   "TotalOrderAmt":number,
      /**  The total actual quantity ordered for this contract line. (credit memos may change it to negative).  */  
   "TotalOrderedQty":number,
      /**  The total actual quantity shipped for this contract line. (credit memos may change it to negative).  */  
   "TotalShippedQty":number,
      /**  The total actual quantity invoiced for this contract line. (credit memos may change it to negative).  */  
   "TotalInvoicedQty":number,
      /**  Indicates if current open Order Releases that have not been shipped and do not have a job should be deleted when processing the demand.  Provides the default value for DemandDetail.  */  
   "DeleteCurrentReleases":boolean,
      /**  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via Demand Contract entry if the CRM module is installed.  */  
   "MktgCampaignID":string,
      /**   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via demand contract entry if the CRM module is installed.  */  
   "MktgEvntSeq":number,
      /**  The mininum quantity that should be for each individual demand schedule record. If the schedule quantity is less than the minimum call off quantity, a warning will be issued but processing can continue.  */  
   "MinCallOffQty":number,
      /**  Optional field that contains the  part revision.  */  
   "RevisionNum":string,
      /**  Optional field that contains the customers revision.  */  
   "XRevisionNum":string,
      /**  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  */  
   "DemandPricing":string,
      /**   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "DocUnitPrice":number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   "Rpt1UnitPrice":number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   "Rpt2UnitPrice":number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   "Rpt3UnitPrice":number,
      /**  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  */  
   "OTSmartString":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates if this record has been selected to create a demand detail record.  Used for automatically creating DemandDetail records from contract lines.  */  
   "SelectedForDemand":boolean,
      /**  The unique identifier of the demand contract.  This must be unique for a customer.  */  
   "DemandCntHdrDemandContract":string,
      /**  The Plant name. Used on shipping reports.  */  
   "PlantName":string,
      /**  Full description of Project Management Code.  */  
   "ProjectIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DemandContractDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  System assigned internal number to uniquely identify the demand contract record.  Is the link to the DemandContractHdr table.  */  
   "DemandContractNum":number,
      /**  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandContractDtl record for the contract and the adding 1 to it.  */  
   "DemandContractLine":number,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.
A default should be made when the DemandContractDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table.  */  
   "PartNum":string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   "XPartNum":string,
      /**  Determines whether or not this contract line is being run in a test mode. When contracts are first set up for EDI it is useful to send all documents in test mode so trading partners can verify the data before going into production mode.  */  
   "TestRecord":boolean,
      /**  The total selling quantity expected to be ordered for this line over the life of the contract.  */  
   "SellingTotalContractQty":number,
      /**  The total quantity expected to be ordered for this line over the life of the contract.  */  
   "TotalContractQty":number,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "LineDesc":string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   "IUM":string,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the Customer.DiscountPercent.  */  
   "DiscountPercent":number,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "UnitPrice":number,
      /**  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   "PricePerCode":string,
      /**  Project ID of the Project table record for this DemandContractDtl record. Can be blank.  */  
   "ProjectID":string,
      /**  This is the Price Group ID used to price the order line with.  */  
   "PriceGroupCode":string,
      /**  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   "SalesUM":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "SellingFactor":number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "SellingFactorDirection":string,
      /**  Comments about the demand detail line.  */  
   "DetailComments":string,
      /**  Use standard Epicor Price matrix/logic  */  
   "UsePriceList":boolean,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Total invoice amount of orders lines invoiced for this contract line in base currency. This field has a true sign. (credit memos are negative).  */  
   "TotalInvoiceAmt":number,
      /**  Total  amount of orders for this contract line in base currency. This field has a true sign. (credit memos are negative).  */  
   "TotalOrderAmt":number,
      /**  The total actual quantity ordered for this contract line. (credit memos may change it to negative).  */  
   "TotalOrderedQty":number,
      /**  The total actual quantity shipped for this contract line. (credit memos may change it to negative).  */  
   "TotalShippedQty":number,
      /**  The total actual quantity invoiced for this contract line. (credit memos may change it to negative).  */  
   "TotalInvoicedQty":number,
      /**  Indicates if current open Order Releases that have not been shipped and do not have a job should be deleted when processing the demand.  Provides the default value for DemandDetail.  */  
   "DeleteCurrentReleases":boolean,
      /**  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via Demand Contract entry if the CRM module is installed.  */  
   "MktgCampaignID":string,
      /**   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via demand contract entry if the CRM module is installed.  */  
   "MktgEvntSeq":number,
      /**  The mininum quantity that should be for each individual demand schedule record. If the schedule quantity is less than the minimum call off quantity, a warning will be issued but processing can continue.  */  
   "MinCallOffQty":number,
      /**  Optional field that contains the  part revision.  */  
   "RevisionNum":string,
      /**  Optional field that contains the customers revision.  */  
   "XRevisionNum":string,
      /**  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  */  
   "DemandPricing":string,
      /**   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "DocUnitPrice":number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   "Rpt1UnitPrice":number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   "Rpt2UnitPrice":number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   "Rpt3UnitPrice":number,
      /**  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  */  
   "OTSmartString":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Total invoice amount of orders invoiced for this contract in document currency. This field has a true sign. (credit memos are negative).  */  
   "DocTotalInvoiceAmt":number,
      /**  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   "Rpt1TotalInvoiceAmt":number,
      /**  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   "Rpt2TotalInvoiceAmt":number,
      /**  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   "Rpt3TotalInvoiceAmt":number,
      /**  Total amount of orders for this contract in document currency. This field has a true sign. (credit memos are negative).  */  
   "DocTotalOrderAmt":number,
      /**  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   "Rpt1TotalOrderAmt":number,
      /**  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   "Rpt2TotalOrderAmt":number,
      /**  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   "Rpt3TotalOrderAmt":number,
      /**  Defines the tolerance for price difference validations.  */  
   "PriceTolerance":number,
      /**  Defines the tolerance for price difference validations in document currency.  */  
   "DocPriceTolerance":number,
      /**  Defines the tolerance for price difference validations in a report currency.  */  
   "Rpt1PriceTolerance":number,
      /**  Defines the tolerance for price difference validations in a report currency.  */  
   "Rpt2PriceTolerance":number,
      /**  Defines the tolerance for price difference validations in a report currency.  */  
   "Rpt3PriceTolerance":number,
      /**  Indicates if this record has been selected to create a demand detail record.  Used for automatically creating DemandDetail records from contract lines.  */  
   "SelectedForDemand":boolean,
   "BitFlag":number,
   "DemandCntHdrDemandContract":string,
   "PlantName":string,
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
      @param demandContractNum
      @param demandContractLine
   */  
export interface DeleteByID_input{
   demandContractNum:number,
   demandContractLine:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_DemandCntDtlSearchTableset{
   DemandContractDtl:Erp_Tablesets_DemandContractDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DemandContractDtlListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  System assigned internal number to uniquely identify the demand contract record.  Is the link to the DemandContractHdr table.  */  
   DemandContractNum:number,
      /**  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandContractDtl record for the contract and the adding 1 to it.  */  
   DemandContractLine:number,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.
A default should be made when the DemandContractDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table.  */  
   PartNum:string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   XPartNum:string,
      /**  Determines whether or not this contract line is being run in a test mode. When contracts are first set up for EDI it is useful to send all documents in test mode so trading partners can verify the data before going into production mode.  */  
   TestRecord:boolean,
      /**  The total selling quantity expected to be ordered for this line over the life of the contract.  */  
   SellingTotalContractQty:number,
      /**  The total quantity expected to be ordered for this line over the life of the contract.  */  
   TotalContractQty:number,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   IUM:string,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the Customer.DiscountPercent.  */  
   DiscountPercent:number,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   UnitPrice:number,
      /**  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   PricePerCode:string,
      /**  Project ID of the Project table record for this DemandContractDtl record. Can be blank.  */  
   ProjectID:string,
      /**  This is the Price Group ID used to price the order line with.  */  
   PriceGroupCode:string,
      /**  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   SalesUM:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingFactor:number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   SellingFactorDirection:string,
      /**  Comments about the demand detail line.  */  
   DetailComments:string,
      /**  Use standard Epicor Price matrix/logic  */  
   UsePriceList:boolean,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Total invoice amount of orders lines invoiced for this contract line in base currency. This field has a true sign. (credit memos are negative).  */  
   TotalInvoiceAmt:number,
      /**  Total  amount of orders for this contract line in base currency. This field has a true sign. (credit memos are negative).  */  
   TotalOrderAmt:number,
      /**  The total actual quantity ordered for this contract line. (credit memos may change it to negative).  */  
   TotalOrderedQty:number,
      /**  The total actual quantity shipped for this contract line. (credit memos may change it to negative).  */  
   TotalShippedQty:number,
      /**  The total actual quantity invoiced for this contract line. (credit memos may change it to negative).  */  
   TotalInvoicedQty:number,
      /**  Indicates if current open Order Releases that have not been shipped and do not have a job should be deleted when processing the demand.  Provides the default value for DemandDetail.  */  
   DeleteCurrentReleases:boolean,
      /**  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via Demand Contract entry if the CRM module is installed.  */  
   MktgCampaignID:string,
      /**   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via demand contract entry if the CRM module is installed.  */  
   MktgEvntSeq:number,
      /**  The mininum quantity that should be for each individual demand schedule record. If the schedule quantity is less than the minimum call off quantity, a warning will be issued but processing can continue.  */  
   MinCallOffQty:number,
      /**  Optional field that contains the  part revision.  */  
   RevisionNum:string,
      /**  Optional field that contains the customers revision.  */  
   XRevisionNum:string,
      /**  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  */  
   DemandPricing:string,
      /**   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   DocUnitPrice:number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   Rpt1UnitPrice:number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   Rpt2UnitPrice:number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   Rpt3UnitPrice:number,
      /**  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  */  
   OTSmartString:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if this record has been selected to create a demand detail record.  Used for automatically creating DemandDetail records from contract lines.  */  
   SelectedForDemand:boolean,
      /**  The unique identifier of the demand contract.  This must be unique for a customer.  */  
   DemandCntHdrDemandContract:string,
      /**  The Plant name. Used on shipping reports.  */  
   PlantName:string,
      /**  Full description of Project Management Code.  */  
   ProjectIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DemandContractDtlListTableset{
   DemandContractDtlList:Erp_Tablesets_DemandContractDtlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DemandContractDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  System assigned internal number to uniquely identify the demand contract record.  Is the link to the DemandContractHdr table.  */  
   DemandContractNum:number,
      /**  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandContractDtl record for the contract and the adding 1 to it.  */  
   DemandContractLine:number,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.
A default should be made when the DemandContractDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table.  */  
   PartNum:string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   XPartNum:string,
      /**  Determines whether or not this contract line is being run in a test mode. When contracts are first set up for EDI it is useful to send all documents in test mode so trading partners can verify the data before going into production mode.  */  
   TestRecord:boolean,
      /**  The total selling quantity expected to be ordered for this line over the life of the contract.  */  
   SellingTotalContractQty:number,
      /**  The total quantity expected to be ordered for this line over the life of the contract.  */  
   TotalContractQty:number,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   IUM:string,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the Customer.DiscountPercent.  */  
   DiscountPercent:number,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   UnitPrice:number,
      /**  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   PricePerCode:string,
      /**  Project ID of the Project table record for this DemandContractDtl record. Can be blank.  */  
   ProjectID:string,
      /**  This is the Price Group ID used to price the order line with.  */  
   PriceGroupCode:string,
      /**  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   SalesUM:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingFactor:number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   SellingFactorDirection:string,
      /**  Comments about the demand detail line.  */  
   DetailComments:string,
      /**  Use standard Epicor Price matrix/logic  */  
   UsePriceList:boolean,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Total invoice amount of orders lines invoiced for this contract line in base currency. This field has a true sign. (credit memos are negative).  */  
   TotalInvoiceAmt:number,
      /**  Total  amount of orders for this contract line in base currency. This field has a true sign. (credit memos are negative).  */  
   TotalOrderAmt:number,
      /**  The total actual quantity ordered for this contract line. (credit memos may change it to negative).  */  
   TotalOrderedQty:number,
      /**  The total actual quantity shipped for this contract line. (credit memos may change it to negative).  */  
   TotalShippedQty:number,
      /**  The total actual quantity invoiced for this contract line. (credit memos may change it to negative).  */  
   TotalInvoicedQty:number,
      /**  Indicates if current open Order Releases that have not been shipped and do not have a job should be deleted when processing the demand.  Provides the default value for DemandDetail.  */  
   DeleteCurrentReleases:boolean,
      /**  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via Demand Contract entry if the CRM module is installed.  */  
   MktgCampaignID:string,
      /**   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via demand contract entry if the CRM module is installed.  */  
   MktgEvntSeq:number,
      /**  The mininum quantity that should be for each individual demand schedule record. If the schedule quantity is less than the minimum call off quantity, a warning will be issued but processing can continue.  */  
   MinCallOffQty:number,
      /**  Optional field that contains the  part revision.  */  
   RevisionNum:string,
      /**  Optional field that contains the customers revision.  */  
   XRevisionNum:string,
      /**  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  */  
   DemandPricing:string,
      /**   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   DocUnitPrice:number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   Rpt1UnitPrice:number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   Rpt2UnitPrice:number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   Rpt3UnitPrice:number,
      /**  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  */  
   OTSmartString:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Total invoice amount of orders invoiced for this contract in document currency. This field has a true sign. (credit memos are negative).  */  
   DocTotalInvoiceAmt:number,
      /**  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   Rpt1TotalInvoiceAmt:number,
      /**  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   Rpt2TotalInvoiceAmt:number,
      /**  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   Rpt3TotalInvoiceAmt:number,
      /**  Total amount of orders for this contract in document currency. This field has a true sign. (credit memos are negative).  */  
   DocTotalOrderAmt:number,
      /**  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   Rpt1TotalOrderAmt:number,
      /**  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   Rpt2TotalOrderAmt:number,
      /**  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   Rpt3TotalOrderAmt:number,
      /**  Defines the tolerance for price difference validations.  */  
   PriceTolerance:number,
      /**  Defines the tolerance for price difference validations in document currency.  */  
   DocPriceTolerance:number,
      /**  Defines the tolerance for price difference validations in a report currency.  */  
   Rpt1PriceTolerance:number,
      /**  Defines the tolerance for price difference validations in a report currency.  */  
   Rpt2PriceTolerance:number,
      /**  Defines the tolerance for price difference validations in a report currency.  */  
   Rpt3PriceTolerance:number,
      /**  Indicates if this record has been selected to create a demand detail record.  Used for automatically creating DemandDetail records from contract lines.  */  
   SelectedForDemand:boolean,
   BitFlag:number,
   DemandCntHdrDemandContract:string,
   PlantName:string,
   ProjectIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtDemandCntDtlSearchTableset{
   DemandContractDtl:Erp_Tablesets_DemandContractDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param demandContractNum
      @param demandContractLine
   */  
export interface GetByID_input{
   demandContractNum:number,
   demandContractLine:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_DemandCntDtlSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_DemandCntDtlSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_DemandCntDtlSearchTableset[],
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
   returnObj:Erp_Tablesets_DemandContractDtlListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param demandContractNum
   */  
export interface GetNewDemandContractDtl_input{
   ds:Erp_Tablesets_DemandCntDtlSearchTableset[],
   demandContractNum:number,
}

export interface GetNewDemandContractDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandCntDtlSearchTableset,
}
}

   /** Required : 
      @param whereClauseDemandContractDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseDemandContractDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_DemandCntDtlSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtDemandCntDtlSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtDemandCntDtlSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_DemandCntDtlSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandCntDtlSearchTableset,
}
}

