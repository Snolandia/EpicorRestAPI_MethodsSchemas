import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ECORevSearchSvc
// Description: ECO Rev Search module
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/$metadata", {
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
   Description: Get ECORevSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECORevSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECORevRow
   */  
export function get_ECORevSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECORevRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/ECORevSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECORevRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECORevSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECORevRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ECORevRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECORevSearches(requestBody:Erp_Tablesets_ECORevRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/ECORevSearches", {
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
   Summary: Calls GetByID to retrieve the ECORevSearch item
   Description: Calls GetByID to retrieve the ECORevSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECORevSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ECORevRow
   */  
export function get_ECORevSearches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECORevRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/ECORevSearches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")", {
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
         resolve(data as Erp_Tablesets_ECORevRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECORevSearch for the service
   Description: Calls UpdateExt to update ECORevSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECORevSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECORevRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECORevSearches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, requestBody:Erp_Tablesets_ECORevRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/ECORevSearches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")", {
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
   Summary: Call UpdateExt to delete ECORevSearch item
   Description: Call UpdateExt to delete ECORevSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECORevSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECORevSearches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/ECORevSearches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECORevListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECORevListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECORevListRow)
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
export function get_GetRows(whereClauseECORev:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseECORev!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECORev=" + whereClauseECORev
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(groupID:string, partNum:string, revisionNum:string, altMethod:string, processMfgID:string, epicorHeaders?:Headers){
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
   if(typeof partNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "partNum=" + partNum
   }
   if(typeof revisionNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "revisionNum=" + revisionNum
   }
   if(typeof altMethod!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "altMethod=" + altMethod
   }
   if(typeof processMfgID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "processMfgID=" + processMfgID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewECORev
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECORev
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewECORev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECORev_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECORev(requestBody:GetNewECORev_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewECORev_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/GetNewECORev", {
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
         resolve(data as GetNewECORev_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECORevSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECORevListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECORevListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECORevRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECORevRow,
}

export interface Erp_Tablesets_ECORevListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Group ID for the ECO Group to which this ECORev belongs.  */  
   "GroupID":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Alternate Routing method for the part revision.  */  
   "AltMethod":string,
      /**  Short description of the revision. This is NOT the Part description.  */  
   "RevShortDesc":string,
      /**  Used to enter a full description of the revision.  */  
   "RevDescription":string,
      /**  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  */  
   "Approved":boolean,
      /**  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  */  
   "ApprovedDate":string,
      /**  UserID who approved the revision.  Not maintainable by the user.  */  
   "ApprovedBy":string,
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
      /**  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   "LLRLaborCost":number,
      /**   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "LLRBurdenCost":number,
      /**  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "LLRMaterialCost":number,
      /**  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "LLRSubcontractCost":number,
      /**  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "LLRMtlBurCost":number,
      /**  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   "LLRSetupLaborCost":number,
      /**   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "LLRSetupBurdenCost":number,
      /**  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  */  
   "RollupDate":string,
      /**  Engineering Drawing Number. An optional field.  */  
   "DrawNum":string,
      /**  Engineering Change Order Number. An optional field for reference.  */  
   "ECO":string,
      /**  An internal flag which indicates that this part revision contains Method of Manufacture details (ECOMtl/ECOOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   "Method":boolean,
      /**   The operation number ECOOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   "AutoRecOpr":number,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   "FinalOpr":number,
      /**  Revision number which will be used to check in the part.  This will only be used if the CheckIn Revision Number is different from the main RevisionNum field.  */  
   "CheckInRevisionNum":string,
      /**  The date that the revision is checked in.  */  
   "CheckInDate":string,
      /**  This flag determines if the ECORev record is currently checked out.  There should only be one checked out ECORev record for each Company-Part-Rev.  */  
   "CheckedOut":boolean,
      /**  The date that the Part-Rev was last checked out to the group.  */  
   "CheckOutDate":string,
      /**  UserID who checked out the revision.  Not maintainable by the user.  */  
   "CheckedOutBy":string,
      /**  An abbreviated part description field from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  */  
   "SearchWord":string,
      /**  The PartDescription from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  */  
   "PartDescription":string,
      /**  Holds the internal object id of pdm parts.  */  
   "PDMObjID":string,
      /**  Indicates if this ECO Revision is locked.  */  
   "RevLocked":boolean,
      /**  UserID that has the ECORev record locked.  */  
   "RevLockedBy":string,
      /**  Site Identifier. This field cannot be blank.  */  
   "Plant":string,
      /**  The alternate method of the parent this method inherits from.  */  
   "ParentAltMethod":string,
      /**  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  */  
   "UseStaging":boolean,
      /**  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  */  
   "UseAltRevForParts":boolean,
      /**  Validate Reference Designators.  */  
   "ValRefDes":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AltMethodDesc  */  
   "AltMethodDesc":string,
      /**  Is this a PartRev record?  Used for build of tree to display PartRevs as ECORev.  */  
   "IsPartRev":boolean,
      /**  Should the Lock menu option be enabled?  */  
   "EnableLock":boolean,
      /**  Should the UnLock menu option be enabled?  */  
   "EnableUnLock":boolean,
      /**  Is the revision updateable?  Used for menu options.  */  
   "EnableUpdateable":boolean,
      /**  Should the GetDetails menu options be enabled?  */  
   "EnableGetDetails":boolean,
      /**  The text description of the ECO Group  */  
   "GroupIDDescription":string,
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
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
      /**  The Plant name. Used on shipping reports.  */  
   "PlantName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ECORevRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Group ID for the ECO Group to which this ECORev belongs.  */  
   "GroupID":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Alternate Routing method for the part revision.  */  
   "AltMethod":string,
      /**  Short description of the revision. This is NOT the Part description.  */  
   "RevShortDesc":string,
      /**  Used to enter a full description of the revision.  */  
   "RevDescription":string,
      /**  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  */  
   "Approved":boolean,
      /**  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  */  
   "ApprovedDate":string,
      /**  UserID who approved the revision.  Not maintainable by the user.  */  
   "ApprovedBy":string,
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
      /**  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   "LLRLaborCost":number,
      /**   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "LLRBurdenCost":number,
      /**  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "LLRMaterialCost":number,
      /**  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "LLRSubcontractCost":number,
      /**  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "LLRMtlBurCost":number,
      /**  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   "LLRSetupLaborCost":number,
      /**   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "LLRSetupBurdenCost":number,
      /**  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  */  
   "RollupDate":string,
      /**  Engineering Drawing Number. An optional field.  */  
   "DrawNum":string,
      /**  Engineering Change Order Number. An optional field for reference.  */  
   "ECO":string,
      /**  An internal flag which indicates that this part revision contains Method of Manufacture details (ECOMtl/ECOOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   "Method":boolean,
      /**   The operation number ECOOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   "AutoRecOpr":number,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   "FinalOpr":number,
      /**  Revision number which will be used to check in the part.  This will only be used if the CheckIn Revision Number is different from the main RevisionNum field.  */  
   "CheckInRevisionNum":string,
      /**  The date that the revision is checked in.  */  
   "CheckInDate":string,
      /**  This flag determines if the ECORev record is currently checked out.  There should only be one checked out ECORev record for each Company-Part-Rev.  */  
   "CheckedOut":boolean,
      /**  The date that the Part-Rev was last checked out to the group.  */  
   "CheckOutDate":string,
      /**  UserID who checked out the revision.  Not maintainable by the user.  */  
   "CheckedOutBy":string,
      /**  An abbreviated part description field from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  */  
   "SearchWord":string,
      /**  The PartDescription from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  */  
   "PartDescription":string,
      /**  Holds the internal object id of pdm parts.  */  
   "PDMObjID":string,
      /**  Indicates if this ECO Revision is locked.  */  
   "RevLocked":boolean,
      /**  UserID that has the ECORev record locked.  */  
   "RevLockedBy":string,
      /**  Site Identifier. This field cannot be blank.  */  
   "Plant":string,
      /**  The alternate method of the parent this method inherits from.  */  
   "ParentAltMethod":string,
      /**  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  */  
   "UseStaging":boolean,
      /**  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  */  
   "UseAltRevForParts":boolean,
      /**  Validate Reference Designators.  */  
   "ValRefDes":boolean,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates the record is used with Machine MES  */  
   "ExternalMES":boolean,
      /**  Identifies whether the co-parts are to be produced concurrently or sequentially. The default is sequential. The selected value determines quantity reporting and costing.  */  
   "ProcessMode":string,
      /**  AltMethodDesc  */  
   "AltMethodDesc":string,
      /**  Customs Item Number  */  
   "CNCustomsItemNum":string,
      /**  The identifier of related Process Manufacturing.  */  
   "ProcessMfgID":string,
      /**  Type of Process Manufacturing this revision is for: Cleaning, General, Master and Site.  */  
   "ProcessMfgType":string,
      /**  Description of Process Manufacturing revision.  */  
   "ProcessMfgDescription":string,
      /**  ID of Revision Image.  */  
   "ImageID":string,
      /**  Indicates if this revision is to use Advanced Staging.  */  
   "UseAdvancedStaging":boolean,
      /**  Only Part Revisions marked as Connected Process Control (CPC) enable will be send to CPC.  */  
   "ECPCEnabled":boolean,
   "Configured":boolean,
      /**  Should the GetDetails menu options be enabled?  */  
   "EnableGetDetails":boolean,
      /**  Should the UnLock menu option be enabled?  */  
   "EnableUnLock":boolean,
      /**  Is the revision updateable?  Used for menu options.  */  
   "EnableUpdateable":boolean,
   "HasCoParts":boolean,
      /**  Is this a PartRev record?  Used for build of tree to display PartRevs as ECORev.  */  
   "IsPartRev":boolean,
      /**  Should the Lock menu option be enabled?  */  
   "EnableLock":boolean,
      /**  Handbook Line  */  
   "CNHandbookLine":string,
   "CNHandbookCode":string,
   "CNCustomsBOM":boolean,
   "isFromPartRevision":boolean,
      /**  AltMethod string with label for kinetic tree binding in EngWorkBenchEntry  */  
   "AltMethodDisplay":string,
   "BitFlag":number,
   "GroupIDDescription":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumPartDescription":string,
   "PartNumSalesUM":string,
   "PartNumTrackDimension":boolean,
   "PartNumPricePerCode":string,
   "PartNumIUM":string,
   "PartNumSellingFactor":number,
   "PartNumTrackLots":boolean,
   "PartNumTypeCode":string,
   "PartRevCreatedBy":string,
   "PartRevCreatedOn":string,
   "PartRevApproved":boolean,
   "PlantName":string,
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
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
   */  
export interface DeleteByID_input{
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ECORevListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Group ID for the ECO Group to which this ECORev belongs.  */  
   GroupID:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Alternate Routing method for the part revision.  */  
   AltMethod:string,
      /**  Short description of the revision. This is NOT the Part description.  */  
   RevShortDesc:string,
      /**  Used to enter a full description of the revision.  */  
   RevDescription:string,
      /**  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  */  
   Approved:boolean,
      /**  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  */  
   ApprovedDate:string,
      /**  UserID who approved the revision.  Not maintainable by the user.  */  
   ApprovedBy:string,
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
      /**  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   LLRLaborCost:number,
      /**   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   LLRBurdenCost:number,
      /**  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   LLRMaterialCost:number,
      /**  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   LLRSubcontractCost:number,
      /**  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   LLRMtlBurCost:number,
      /**  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   LLRSetupLaborCost:number,
      /**   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   LLRSetupBurdenCost:number,
      /**  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  */  
   RollupDate:string,
      /**  Engineering Drawing Number. An optional field.  */  
   DrawNum:string,
      /**  Engineering Change Order Number. An optional field for reference.  */  
   ECO:string,
      /**  An internal flag which indicates that this part revision contains Method of Manufacture details (ECOMtl/ECOOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   Method:boolean,
      /**   The operation number ECOOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   AutoRecOpr:number,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   FinalOpr:number,
      /**  Revision number which will be used to check in the part.  This will only be used if the CheckIn Revision Number is different from the main RevisionNum field.  */  
   CheckInRevisionNum:string,
      /**  The date that the revision is checked in.  */  
   CheckInDate:string,
      /**  This flag determines if the ECORev record is currently checked out.  There should only be one checked out ECORev record for each Company-Part-Rev.  */  
   CheckedOut:boolean,
      /**  The date that the Part-Rev was last checked out to the group.  */  
   CheckOutDate:string,
      /**  UserID who checked out the revision.  Not maintainable by the user.  */  
   CheckedOutBy:string,
      /**  An abbreviated part description field from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  */  
   SearchWord:string,
      /**  The PartDescription from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  */  
   PartDescription:string,
      /**  Holds the internal object id of pdm parts.  */  
   PDMObjID:string,
      /**  Indicates if this ECO Revision is locked.  */  
   RevLocked:boolean,
      /**  UserID that has the ECORev record locked.  */  
   RevLockedBy:string,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  The alternate method of the parent this method inherits from.  */  
   ParentAltMethod:string,
      /**  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  */  
   UseStaging:boolean,
      /**  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  */  
   UseAltRevForParts:boolean,
      /**  Validate Reference Designators.  */  
   ValRefDes:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AltMethodDesc  */  
   AltMethodDesc:string,
      /**  Is this a PartRev record?  Used for build of tree to display PartRevs as ECORev.  */  
   IsPartRev:boolean,
      /**  Should the Lock menu option be enabled?  */  
   EnableLock:boolean,
      /**  Should the UnLock menu option be enabled?  */  
   EnableUnLock:boolean,
      /**  Is the revision updateable?  Used for menu options.  */  
   EnableUpdateable:boolean,
      /**  Should the GetDetails menu options be enabled?  */  
   EnableGetDetails:boolean,
      /**  The text description of the ECO Group  */  
   GroupIDDescription:string,
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
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
      /**  The Plant name. Used on shipping reports.  */  
   PlantName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ECORevListTableset{
   ECORevList:Erp_Tablesets_ECORevListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ECORevRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Group ID for the ECO Group to which this ECORev belongs.  */  
   GroupID:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Alternate Routing method for the part revision.  */  
   AltMethod:string,
      /**  Short description of the revision. This is NOT the Part description.  */  
   RevShortDesc:string,
      /**  Used to enter a full description of the revision.  */  
   RevDescription:string,
      /**  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  */  
   Approved:boolean,
      /**  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  */  
   ApprovedDate:string,
      /**  UserID who approved the revision.  Not maintainable by the user.  */  
   ApprovedBy:string,
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
      /**  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   LLRLaborCost:number,
      /**   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   LLRBurdenCost:number,
      /**  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   LLRMaterialCost:number,
      /**  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   LLRSubcontractCost:number,
      /**  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   LLRMtlBurCost:number,
      /**  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   LLRSetupLaborCost:number,
      /**   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   LLRSetupBurdenCost:number,
      /**  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  */  
   RollupDate:string,
      /**  Engineering Drawing Number. An optional field.  */  
   DrawNum:string,
      /**  Engineering Change Order Number. An optional field for reference.  */  
   ECO:string,
      /**  An internal flag which indicates that this part revision contains Method of Manufacture details (ECOMtl/ECOOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   Method:boolean,
      /**   The operation number ECOOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   AutoRecOpr:number,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   FinalOpr:number,
      /**  Revision number which will be used to check in the part.  This will only be used if the CheckIn Revision Number is different from the main RevisionNum field.  */  
   CheckInRevisionNum:string,
      /**  The date that the revision is checked in.  */  
   CheckInDate:string,
      /**  This flag determines if the ECORev record is currently checked out.  There should only be one checked out ECORev record for each Company-Part-Rev.  */  
   CheckedOut:boolean,
      /**  The date that the Part-Rev was last checked out to the group.  */  
   CheckOutDate:string,
      /**  UserID who checked out the revision.  Not maintainable by the user.  */  
   CheckedOutBy:string,
      /**  An abbreviated part description field from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  */  
   SearchWord:string,
      /**  The PartDescription from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  */  
   PartDescription:string,
      /**  Holds the internal object id of pdm parts.  */  
   PDMObjID:string,
      /**  Indicates if this ECO Revision is locked.  */  
   RevLocked:boolean,
      /**  UserID that has the ECORev record locked.  */  
   RevLockedBy:string,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  The alternate method of the parent this method inherits from.  */  
   ParentAltMethod:string,
      /**  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  */  
   UseStaging:boolean,
      /**  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  */  
   UseAltRevForParts:boolean,
      /**  Validate Reference Designators.  */  
   ValRefDes:boolean,
      /**  ConfigID  */  
   ConfigID:string,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  Identifies whether the co-parts are to be produced concurrently or sequentially. The default is sequential. The selected value determines quantity reporting and costing.  */  
   ProcessMode:string,
      /**  AltMethodDesc  */  
   AltMethodDesc:string,
      /**  Customs Item Number  */  
   CNCustomsItemNum:string,
      /**  The identifier of related Process Manufacturing.  */  
   ProcessMfgID:string,
      /**  Type of Process Manufacturing this revision is for: Cleaning, General, Master and Site.  */  
   ProcessMfgType:string,
      /**  Description of Process Manufacturing revision.  */  
   ProcessMfgDescription:string,
      /**  ID of Revision Image.  */  
   ImageID:string,
      /**  Indicates if this revision is to use Advanced Staging.  */  
   UseAdvancedStaging:boolean,
      /**  Only Part Revisions marked as Connected Process Control (CPC) enable will be send to CPC.  */  
   ECPCEnabled:boolean,
   Configured:boolean,
      /**  Should the GetDetails menu options be enabled?  */  
   EnableGetDetails:boolean,
      /**  Should the UnLock menu option be enabled?  */  
   EnableUnLock:boolean,
      /**  Is the revision updateable?  Used for menu options.  */  
   EnableUpdateable:boolean,
   HasCoParts:boolean,
      /**  Is this a PartRev record?  Used for build of tree to display PartRevs as ECORev.  */  
   IsPartRev:boolean,
      /**  Should the Lock menu option be enabled?  */  
   EnableLock:boolean,
      /**  Handbook Line  */  
   CNHandbookLine:string,
   CNHandbookCode:string,
   CNCustomsBOM:boolean,
   isFromPartRevision:boolean,
      /**  AltMethod string with label for kinetic tree binding in EngWorkBenchEntry  */  
   AltMethodDisplay:string,
   BitFlag:number,
   GroupIDDescription:string,
   PartNumTrackSerialNum:boolean,
   PartNumPartDescription:string,
   PartNumSalesUM:string,
   PartNumTrackDimension:boolean,
   PartNumPricePerCode:string,
   PartNumIUM:string,
   PartNumSellingFactor:number,
   PartNumTrackLots:boolean,
   PartNumTypeCode:string,
   PartRevCreatedBy:string,
   PartRevCreatedOn:string,
   PartRevApproved:boolean,
   PlantName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ECORevSearchTableset{
   ECORev:Erp_Tablesets_ECORevRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtECORevSearchTableset{
   ECORev:Erp_Tablesets_ECORevRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
   */  
export interface GetByID_input{
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ECORevSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ECORevSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ECORevSearchTableset[],
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
   returnObj:Erp_Tablesets_ECORevListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
   */  
export interface GetNewECORev_input{
   ds:Erp_Tablesets_ECORevSearchTableset[],
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
}

export interface GetNewECORev_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ECORevSearchTableset,
}
}

   /** Required : 
      @param whereClauseECORev
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseECORev:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ECORevSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtECORevSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtECORevSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ECORevSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ECORevSearchTableset,
}
}

