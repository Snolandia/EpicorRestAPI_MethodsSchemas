import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ECOOprSearchSvc
// Description: Add your summary for this object here
// Version: v1



//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Get ECOOprSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOOprSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprRow
   */  
export function get_ECOOprSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/ECOOprSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOOprSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOOprRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOOprRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ECOOprSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/ECOOprSearches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ECOOprSearch item
   Description: Calls GetByID to retrieve the ECOOprSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprRow
   */  
export function get_ECOOprSearches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ECOOprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/ECOOprSearches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ECOOprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ECOOprSearch for the service
   Description: Calls UpdateExt to update ECOOprSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOOprSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOOprRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ECOOprSearches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/ECOOprSearches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete ECOOprSearch item
   Description: Call UpdateExt to delete ECOOprSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOOprSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param OprSeq Desc: OprSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ECOOprSearches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq(Company:string, GroupID:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, OprSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/ECOOprSearches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseECOOpr:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseECOOpr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseECOOpr=" + whereClauseECOOpr
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(groupID:string, partNum:string, revisionNum:string, altMethod:string, processMfgID:string, oprSeq:string, epicorHeaders?:Headers){
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
   if(typeof oprSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "oprSeq=" + oprSeq
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewECOOpr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOOpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOOpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOOpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewECOOpr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/GetNewECOOpr", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ECOOprSearchSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECOOprListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ECOOprRow[],
}

export interface Erp_Tablesets_ECOOprListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   "OprSeq":number,
      /**   Operation Master Code - Links the JobOper  record with a OpMaster record. Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  */  
   "OpCode":string,
      /**   The Operation standard ID. This links the JobOPer to the OpStd master file. This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.
Valid for "inside operations" only.  */  
   "OpStdID":string,
      /**  The estimated set up hours. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours.  */  
   "EstSetHours":number,
      /**   The estimated Production run hours for internal operations (Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (RunQty / Std).
If StdFormat = "PM" then (RunQty / Std ) / 60.
If StdFormat = "OH" then (RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (RunQty/Basis) X Std.
If StdFormat = "MP" then ((RunQty/Basis) X Std) / 60.  */  
   "EstProdHours":number,
      /**   The production standard for the operation. It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours. A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  */  
   "ProdStandard":number,
      /**   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  */  
   "StdFormat":string,
      /**   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   "StdBasis":string,
      /**  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  */  
   "OpsPerPart":number,
      /**  Production Quantity per one of the Parent Item.  */  
   "QtyPer":number,
      /**  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  */  
   "Machines":number,
      /**  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to se tup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   "SetUpCrewSize":number,
      /**  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  */  
   "ProdCrewSize":number,
      /**  Estimated Scrap  */  
   "EstScrap":number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   "EstScrapType":string,
      /**  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  */  
   "SubContract":boolean,
      /**  Inventory UOM  */  
   "IUM":string,
      /**  Estimated Unit Cost for the SubContract operation.  Defaults from the Part table if valid PartNum.  */  
   "EstUnitCost":number,
      /**  Hours required is calculated as days * 8.  */  
   "DaysOut":number,
      /**  The PartNum to be shipped to the subcontract. Defaults as the Part number of the method to which it belongs (ECOOpr.PartNum).  */  
   "SubPartNum":string,
      /**  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  */  
   "VendorNum":number,
      /**  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  */  
   "PurPoint":string,
      /**  Editor widget for Job operation comments.  */  
   "CommentText":string,
      /**   Indicates the scheduling relationship between this and the preceding operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  */  
   "SchedRelation":string,
      /**  The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0. This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  */  
   "RunQty":number,
      /**  Additional Setup Hours that will be required after a certain quantity has been run for this operation. The quantity at which this occurs is established in AddSetupQty field. The system determines the setup hours as SetupHrs + (Max((RunQty - AddlSetupQty,0))/AddlSetUpQty) * AddlSetupHours. Any fractional results of the AddlSetUpQty calculations are rounded up to the next whole number before multiplying by the AddlSetUpHours.  */  
   "AddlSetupHours":number,
      /**  Additional Setup quantity indicates the quantity at which additional setup time will be incurred.  */  
   "AddlSetUpQty":number,
      /**  Indicates the operation that must precede this operation.  Mainly used to model one to many routing structures.  */  
   "APSPrepOp":number,
      /**  This is the next operation in the routing.  -1 makes this operation the last one in the routing so far; -2 makes it the first one in the routing so far; 0 means no successor.  */  
   "APSNextOp":number,
      /**  Specifies the operation for which this is an alternate.  */  
   "APSAltOp":number,
      /**  Used to assign an operation to a specific resource so that APS does not schedule it elsewhere.  Overrides APSCapability.  */  
   "APSSpecificResource":string,
      /**   Cycles per minute.
SQL:  IIF(CINT(JobOper.RunQty) = 0 OR JobOper.SubContract = TRUE, "0", JobOper.EstProdHours * 60 /  JobOper.RunQty)  */  
   "APSCycleTime":number,
      /**   Fixed time, in decimal minutes, to be added to the operation.  Can be used to represent cleanup time or model outsource time.
SQL: IFF(JobOper.SubContract = TRUE, (JobOper.DaysOut * 1440), "0")  */  
   "APSConstantTime":number,
      /**  Used to group operations to save on setups.  */  
   "APSSetupGroup":number,
      /**  Quantity of Part per cycle.  */  
   "APSMakeFactor":number,
      /**  Quantity that must be completed before the next operation can start (for overlap); quantity per batch (for batch resources); Auxiliary resource quantity.  */  
   "APSContainerSize":number,
      /**  Name of the APS Scheduler Module in which to schedule this operation.  */  
   "APSSchedulerName":string,
      /**  If the scheduled time exceeds this value then the operation is split into operations which do not exceed this length.  */  
   "APSMaxLength":number,
      /**  Time between the end of this operation and the start time of the successor operation.  */  
   "APSTransferTime":number,
      /**  Cycle time and constant times are divided by this value to get schedule times.  Zeros disable this feature.  */  
   "APSEffectiveness":number,
      /**  Type of Operation: P for Prep, D for Processing (Dispatchable in APS terminology).  */  
   "APSOperationClass":string,
      /**  Auxiliary resource requirements.   This is a comma and tilde delimited list of APSAuxResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  */  
   "APSAuxResource":string,
      /**  Additional resource requirements.   This is a comma and tilde delimited list of APSAddResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  For Additional Resources the Duration = 5 (entire Operation).  */  
   "APSAddResource":string,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  */  
   "LaborEntryMethod":string,
      /**  The quantity requested for first article inspection.  */  
   "FAQty":number,
      /**  A flag to indicate that this part operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  */  
   "RFQNeeded":boolean,
      /**  The number of vendor quotes that are required for this part subcontract operation.  Can be zero if RFQ(s) are not required.  */  
   "RFQVendQuotes":number,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   "GroupID":string,
      /**  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  */  
   "OrigOprSeq":number,
      /**  Used to group operation to save on setups.  */  
   "SetupGroup":string,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**   Identifies the primary ECOOpDtl to be used for setup.  The setup time for the operation is determined on the ECOOpDtl.
If <> 0, must identify a valid ECOOpDtl.  The ECOOpDtl needs to have a RequiredFor = S or B.  */  
   "PrimarySetupOpDtl":number,
      /**   Identifies the primary ECOOpDtl to be used for production.  The production run time for the operation is determined on the ECOOpDtl.
If <> 0, must identify a valid ECOOpDtl.  The ECOOpDtl needs to have a RequiredFor = P or B.  */  
   "PrimaryProdOpDtl":number,
      /**  Alternate Routing method for the part revision.  */  
   "AltMethod":string,
      /**  Operation Description.  */  
   "OpDesc":string,
      /**  The stage number of the operations.  Entered only when the related PartRev.UseStaging flag is true.  */  
   "StageNumber":string,
      /**  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  */  
   "BaseMethodOverridden":boolean,
      /**  Parent Alternate Routing method of this part operation.  */  
   "ParentAltMethod":string,
      /**  Indicates the parent operation sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  */  
   "ParentOprSeq":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty01":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty02":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty03":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty04":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty05":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty06":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty07":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty08":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty09":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty10":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost01":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost02":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost03":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost04":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost05":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost06":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost07":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost08":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost09":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost10":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate01":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate02":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate03":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate04":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate05":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate06":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate07":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate08":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate09":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate10":number,
      /**  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  */  
   "SNRequiredOpr":boolean,
      /**  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  */  
   "SNRequiredSubConShip":boolean,
      /**  Operation Weight defaulted from Part Master.  */  
   "Weight":number,
      /**  Operation Weight UOM defaulted from Part Master.  */  
   "WeightUOM":string,
      /**   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  */  
   "SendAheadType":string,
      /**   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  */  
   "SendAheadOffset":number,
      /**  Delimited list of PrjRoleCd codes that are allowed for this operation.  */  
   "PrjRoleList":string,
      /**  Allow use all Roles  */  
   "UseAllRoles":boolean,
      /**  Indicates the record is used with Machine MES  */  
   "ExternalMES":boolean,
      /**  PctReg  */  
   "PctReg":number,
      /**  SetupMaterial  */  
   "SetupMaterial":number,
      /**  MaterialColorRating  */  
   "MaterialColorRating":number,
      /**  MiscInfo1  */  
   "MiscInfo1":string,
      /**  MiscInfo2  */  
   "MiscInfo2":string,
      /**  SetupURL  */  
   "SetupURL":string,
      /**  ExpPctUp  */  
   "ExpPctUp":number,
      /**  ExpCycTm  */  
   "ExpCycTm":number,
      /**  ExpGood  */  
   "ExpGood":number,
      /**  NonProdLimit  */  
   "NonProdLimit":number,
      /**  AutoSpcEnable  */  
   "AutoSpcEnable":boolean,
      /**  AutoSpcPeriod  */  
   "AutoSpcPeriod":number,
      /**  PartQualEnable  */  
   "PartQualEnable":boolean,
      /**  AutoSpcSubgroup  */  
   "AutoSpcSubgroup":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PulsesPerCycle  */  
   "PulsesPerCycle":number,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   "QtyPerCycle":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Planning number of pieces for this attribute set.  */  
   "PlanningNumberOfPieces":number,
      /**  The identifier of related Process Manufacturing.  */  
   "ProcessMfgID":string,
      /**  TemplateID  */  
   "TemplateID":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "SubRevisionNum":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ECOOprRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   "OprSeq":number,
      /**   Operation Master Code - Links the JobOper  record with a OpMaster record. Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  */  
   "OpCode":string,
      /**   The Operation standard ID. This links the JobOPer to the OpStd master file. This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.
Valid for "inside operations" only.  */  
   "OpStdID":string,
      /**  The estimated set up hours. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours.  */  
   "EstSetHours":number,
      /**   The estimated Production run hours for internal operations (Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (RunQty / Std).
If StdFormat = "PM" then (RunQty / Std ) / 60.
If StdFormat = "OH" then (RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (RunQty/Basis) X Std.
If StdFormat = "MP" then ((RunQty/Basis) X Std) / 60.  */  
   "EstProdHours":number,
      /**   The production standard for the operation. It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours. A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  */  
   "ProdStandard":number,
      /**   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  */  
   "StdFormat":string,
      /**   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   "StdBasis":string,
      /**  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  */  
   "OpsPerPart":number,
      /**  Production Quantity per one of the Parent Item.  */  
   "QtyPer":number,
      /**  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  */  
   "Machines":number,
      /**  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to se tup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   "SetUpCrewSize":number,
      /**  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  */  
   "ProdCrewSize":number,
      /**  Estimated Scrap  */  
   "EstScrap":number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   "EstScrapType":string,
      /**  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  */  
   "SubContract":boolean,
      /**  Inventory UOM  */  
   "IUM":string,
      /**  Estimated Unit Cost for the SubContract operation.  Defaults from the Part table if valid PartNum.  */  
   "EstUnitCost":number,
      /**  Hours required is calculated as days * 8.  */  
   "DaysOut":number,
      /**  The PartNum to be shipped to the subcontract. Defaults as the Part number of the method to which it belongs (ECOOpr.PartNum).  */  
   "SubPartNum":string,
      /**  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  */  
   "VendorNum":number,
      /**  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  */  
   "PurPoint":string,
      /**  Editor widget for Job operation comments.  */  
   "CommentText":string,
      /**   Indicates the scheduling relationship between this and the preceding operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  */  
   "SchedRelation":string,
      /**  The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0. This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  */  
   "RunQty":number,
      /**  Additional Setup Hours that will be required after a certain quantity has been run for this operation. The quantity at which this occurs is established in AddSetupQty field. The system determines the setup hours as SetupHrs + (Max((RunQty - AddlSetupQty,0))/AddlSetUpQty) * AddlSetupHours. Any fractional results of the AddlSetUpQty calculations are rounded up to the next whole number before multiplying by the AddlSetUpHours.  */  
   "AddlSetupHours":number,
      /**  Additional Setup quantity indicates the quantity at which additional setup time will be incurred.  */  
   "AddlSetUpQty":number,
      /**  Indicates the operation that must precede this operation.  Mainly used to model one to many routing structures.  */  
   "APSPrepOp":number,
      /**  This is the next operation in the routing.  -1 makes this operation the last one in the routing so far; -2 makes it the first one in the routing so far; 0 means no successor.  */  
   "APSNextOp":number,
      /**  Specifies the operation for which this is an alternate.  */  
   "APSAltOp":number,
      /**  Used to assign an operation to a specific resource so that APS does not schedule it elsewhere.  Overrides APSCapability.  */  
   "APSSpecificResource":string,
      /**   Cycles per minute.
SQL:  IIF(CINT(JobOper.RunQty) = 0 OR JobOper.SubContract = TRUE, "0", JobOper.EstProdHours * 60 /  JobOper.RunQty)  */  
   "APSCycleTime":number,
      /**   Fixed time, in decimal minutes, to be added to the operation.  Can be used to represent cleanup time or model outsource time.
SQL: IFF(JobOper.SubContract = TRUE, (JobOper.DaysOut * 1440), "0")  */  
   "APSConstantTime":number,
      /**  Used to group operations to save on setups.  */  
   "APSSetupGroup":number,
      /**  Quantity of Part per cycle.  */  
   "APSMakeFactor":number,
      /**  Quantity that must be completed before the next operation can start (for overlap); quantity per batch (for batch resources); Auxiliary resource quantity.  */  
   "APSContainerSize":number,
      /**  Name of the APS Scheduler Module in which to schedule this operation.  */  
   "APSSchedulerName":string,
      /**  If the scheduled time exceeds this value then the operation is split into operations which do not exceed this length.  */  
   "APSMaxLength":number,
      /**  Time between the end of this operation and the start time of the successor operation.  */  
   "APSTransferTime":number,
      /**  Cycle time and constant times are divided by this value to get schedule times.  Zeros disable this feature.  */  
   "APSEffectiveness":number,
      /**  Type of Operation: P for Prep, D for Processing (Dispatchable in APS terminology).  */  
   "APSOperationClass":string,
      /**  Auxiliary resource requirements.   This is a comma and tilde delimited list of APSAuxResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  */  
   "APSAuxResource":string,
      /**  Additional resource requirements.   This is a comma and tilde delimited list of APSAddResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  For Additional Resources the Duration = 5 (entire Operation).  */  
   "APSAddResource":string,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  */  
   "LaborEntryMethod":string,
      /**  The quantity requested for first article inspection.  */  
   "FAQty":number,
      /**  A flag to indicate that this part operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  */  
   "RFQNeeded":boolean,
      /**  The number of vendor quotes that are required for this part subcontract operation.  Can be zero if RFQ(s) are not required.  */  
   "RFQVendQuotes":number,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   "GroupID":string,
      /**  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  */  
   "OrigOprSeq":number,
      /**  Used to group operation to save on setups.  */  
   "SetupGroup":string,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**   Identifies the primary ECOOpDtl to be used for setup.  The setup time for the operation is determined on the ECOOpDtl.
If <> 0, must identify a valid ECOOpDtl.  The ECOOpDtl needs to have a RequiredFor = S or B.  */  
   "PrimarySetupOpDtl":number,
      /**   Identifies the primary ECOOpDtl to be used for production.  The production run time for the operation is determined on the ECOOpDtl.
If <> 0, must identify a valid ECOOpDtl.  The ECOOpDtl needs to have a RequiredFor = P or B.  */  
   "PrimaryProdOpDtl":number,
      /**  Alternate Routing method for the part revision.  */  
   "AltMethod":string,
      /**  Operation Description.  */  
   "OpDesc":string,
      /**  The stage number of the operations.  Entered only when the related PartRev.UseStaging flag is true.  */  
   "StageNumber":string,
      /**  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  */  
   "BaseMethodOverridden":boolean,
      /**  Parent Alternate Routing method of this part operation.  */  
   "ParentAltMethod":string,
      /**  Indicates the parent operation sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  */  
   "ParentOprSeq":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty01":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty02":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty03":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty04":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty05":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty06":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty07":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty08":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty09":number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   "BrkQty10":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost01":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost02":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost03":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost04":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost05":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost06":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost07":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost08":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost09":number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   "PBrkCost10":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate01":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate02":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate03":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate04":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate05":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate06":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate07":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate08":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate09":number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   "PBrkStdRate10":number,
      /**  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  */  
   "SNRequiredOpr":boolean,
      /**  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  */  
   "SNRequiredSubConShip":boolean,
      /**  Operation Weight defaulted from Part Master.  */  
   "Weight":number,
      /**  Operation Weight UOM defaulted from Part Master.  */  
   "WeightUOM":string,
      /**   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  */  
   "SendAheadType":string,
      /**   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  */  
   "SendAheadOffset":number,
      /**  Delimited list of PrjRoleCd codes that are allowed for this operation.  */  
   "PrjRoleList":string,
      /**  Allow use all Roles  */  
   "UseAllRoles":boolean,
      /**  Indicates the record is used with Machine MES  */  
   "ExternalMES":boolean,
      /**  PctReg  */  
   "PctReg":number,
      /**  SetupMaterial  */  
   "SetupMaterial":number,
      /**  MaterialColorRating  */  
   "MaterialColorRating":number,
      /**  MiscInfo1  */  
   "MiscInfo1":string,
      /**  MiscInfo2  */  
   "MiscInfo2":string,
      /**  SetupURL  */  
   "SetupURL":string,
      /**  ExpPctUp  */  
   "ExpPctUp":number,
      /**  ExpCycTm  */  
   "ExpCycTm":number,
      /**  ExpGood  */  
   "ExpGood":number,
      /**  NonProdLimit  */  
   "NonProdLimit":number,
      /**  AutoSpcEnable  */  
   "AutoSpcEnable":boolean,
      /**  AutoSpcPeriod  */  
   "AutoSpcPeriod":number,
      /**  PartQualEnable  */  
   "PartQualEnable":boolean,
      /**  AutoSpcSubgroup  */  
   "AutoSpcSubgroup":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PulsesPerCycle  */  
   "PulsesPerCycle":number,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   "QtyPerCycle":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Planning number of pieces for this attribute set.  */  
   "PlanningNumberOfPieces":number,
      /**  The identifier of related Process Manufacturing.  */  
   "ProcessMfgID":string,
      /**  TemplateID  */  
   "TemplateID":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "SubRevisionNum":string,
      /**  The vendor's name and bill to address  */  
   "DspBillAddr":string,
      /**  Field used to control the flag on SNRequiredSubConShip field on UI screens.  */  
   "EnableSNReqSubConShip":boolean,
      /**  Used as a flag to enable controls on UI screens  */  
   "EnableSNRequiredOpr":boolean,
      /**  The final operation field  */  
   "FinalOpr":boolean,
      /**  Flag to let you know if you have price breaks.  */  
   "HasPriceBreaks":boolean,
      /**  Is this a PartOpr?  Used when building the tree to show PartOpr as ECOOpr.  */  
   "IsPartOpr":boolean,
      /**  The original or old OprSeq.  Used when changing the OprSeq.  */  
   "OldOprSeq":number,
   "OpStdDescription":string,
      /**  PML ID  */  
   "PLMChar03":string,
      /**  Primary Resource Group description  */  
   "PrimaryResourceGrpDesc":string,
      /**  The Resource Group ID of the primary production operation detail.  */  
   "PrimaryResourceGrpID":string,
      /**  Indicates if the scheduling resources should be refreshed when the op code changes.  */  
   "RefreshResources":boolean,
      /**  The setup hours per machines.  */  
   "SetHoursPerMach":number,
      /**  The standard format description.  */  
   "StdFrmtDesc":string,
      /**  The value of the ecorev.usestaging field for UI purposes  */  
   "UseStaging":boolean,
      /**  The auto receive field  */  
   "AutoReceive":boolean,
   "EnableAttributeSetSearch":boolean,
   "PrimaryProdOpDtlDesc":string,
   "PrimarySetupOpDtlDesc":string,
   "BitFlag":number,
   "AnalysisCdDescription":string,
   "APSSchedulerNameAPSSchedulerName":string,
   "DynAttrValueSetShortDescription":string,
   "DynAttrValueSetDescription":string,
   "GroupIDDescription":string,
   "OpCodeOpDesc":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumIUM":string,
   "PartNumTrackDimension":boolean,
   "PartNumTrackLots":boolean,
   "PartNumSellingFactor":number,
   "PartNumTrackSerialNum":boolean,
   "PartNumPricePerCode":string,
   "PartNumPartDescription":string,
   "PartNumSalesUM":string,
   "PrimaryProdOpDtlOpDtlDesc":string,
   "PrimarySetupOpDtlOpDtlDesc":string,
   "RevisionNumRevShortDesc":string,
   "RevisionNumRevDescription":string,
   "RevisionNumPartDescription":string,
   "SetupGroupDescription":string,
   "StageNoDescription":string,
   "SubPartNumTrackInventoryAttributes":boolean,
   "SubPartNumPricePerCode":string,
   "SubPartNumTrackDimension":boolean,
   "SubPartNumTrackSerialNum":boolean,
   "SubPartNumSellingFactor":number,
   "SubPartNumTrackLots":boolean,
   "SubPartNumSalesUM":string,
   "SubPartNumPartDescription":string,
   "SubPartNumIUM":string,
   "SubPartNumAttrClassID":string,
   "SubPartNumTrackInventoryByRevision":boolean,
   "VendorNumDefaultFOB":string,
   "VendorNumCurrencyCode":string,
   "VendorNumCity":string,
   "VendorNumVendorID":string,
   "VendorNumName":string,
   "VendorNumState":string,
   "VendorNumAddress1":string,
   "VendorNumZIP":string,
   "VendorNumTermsCode":string,
   "VendorNumAddress3":string,
   "VendorNumAddress2":string,
   "VendorNumCountry":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
      @param oprSeq
   */  
export interface DeleteByID_input{
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
   oprSeq:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ECOOprListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   OprSeq:number,
      /**   Operation Master Code - Links the JobOper  record with a OpMaster record. Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  */  
   OpCode:string,
      /**   The Operation standard ID. This links the JobOPer to the OpStd master file. This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.
Valid for "inside operations" only.  */  
   OpStdID:string,
      /**  The estimated set up hours. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours.  */  
   EstSetHours:number,
      /**   The estimated Production run hours for internal operations (Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (RunQty / Std).
If StdFormat = "PM" then (RunQty / Std ) / 60.
If StdFormat = "OH" then (RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (RunQty/Basis) X Std.
If StdFormat = "MP" then ((RunQty/Basis) X Std) / 60.  */  
   EstProdHours:number,
      /**   The production standard for the operation. It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours. A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  */  
   ProdStandard:number,
      /**   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  */  
   StdFormat:string,
      /**   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   StdBasis:string,
      /**  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  */  
   OpsPerPart:number,
      /**  Production Quantity per one of the Parent Item.  */  
   QtyPer:number,
      /**  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  */  
   Machines:number,
      /**  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to se tup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   SetUpCrewSize:number,
      /**  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  */  
   ProdCrewSize:number,
      /**  Estimated Scrap  */  
   EstScrap:number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   EstScrapType:string,
      /**  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  */  
   SubContract:boolean,
      /**  Inventory UOM  */  
   IUM:string,
      /**  Estimated Unit Cost for the SubContract operation.  Defaults from the Part table if valid PartNum.  */  
   EstUnitCost:number,
      /**  Hours required is calculated as days * 8.  */  
   DaysOut:number,
      /**  The PartNum to be shipped to the subcontract. Defaults as the Part number of the method to which it belongs (ECOOpr.PartNum).  */  
   SubPartNum:string,
      /**  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  */  
   PurPoint:string,
      /**  Editor widget for Job operation comments.  */  
   CommentText:string,
      /**   Indicates the scheduling relationship between this and the preceding operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  */  
   SchedRelation:string,
      /**  The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0. This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  */  
   RunQty:number,
      /**  Additional Setup Hours that will be required after a certain quantity has been run for this operation. The quantity at which this occurs is established in AddSetupQty field. The system determines the setup hours as SetupHrs + (Max((RunQty - AddlSetupQty,0))/AddlSetUpQty) * AddlSetupHours. Any fractional results of the AddlSetUpQty calculations are rounded up to the next whole number before multiplying by the AddlSetUpHours.  */  
   AddlSetupHours:number,
      /**  Additional Setup quantity indicates the quantity at which additional setup time will be incurred.  */  
   AddlSetUpQty:number,
      /**  Indicates the operation that must precede this operation.  Mainly used to model one to many routing structures.  */  
   APSPrepOp:number,
      /**  This is the next operation in the routing.  -1 makes this operation the last one in the routing so far; -2 makes it the first one in the routing so far; 0 means no successor.  */  
   APSNextOp:number,
      /**  Specifies the operation for which this is an alternate.  */  
   APSAltOp:number,
      /**  Used to assign an operation to a specific resource so that APS does not schedule it elsewhere.  Overrides APSCapability.  */  
   APSSpecificResource:string,
      /**   Cycles per minute.
SQL:  IIF(CINT(JobOper.RunQty) = 0 OR JobOper.SubContract = TRUE, "0", JobOper.EstProdHours * 60 /  JobOper.RunQty)  */  
   APSCycleTime:number,
      /**   Fixed time, in decimal minutes, to be added to the operation.  Can be used to represent cleanup time or model outsource time.
SQL: IFF(JobOper.SubContract = TRUE, (JobOper.DaysOut * 1440), "0")  */  
   APSConstantTime:number,
      /**  Used to group operations to save on setups.  */  
   APSSetupGroup:number,
      /**  Quantity of Part per cycle.  */  
   APSMakeFactor:number,
      /**  Quantity that must be completed before the next operation can start (for overlap); quantity per batch (for batch resources); Auxiliary resource quantity.  */  
   APSContainerSize:number,
      /**  Name of the APS Scheduler Module in which to schedule this operation.  */  
   APSSchedulerName:string,
      /**  If the scheduled time exceeds this value then the operation is split into operations which do not exceed this length.  */  
   APSMaxLength:number,
      /**  Time between the end of this operation and the start time of the successor operation.  */  
   APSTransferTime:number,
      /**  Cycle time and constant times are divided by this value to get schedule times.  Zeros disable this feature.  */  
   APSEffectiveness:number,
      /**  Type of Operation: P for Prep, D for Processing (Dispatchable in APS terminology).  */  
   APSOperationClass:string,
      /**  Auxiliary resource requirements.   This is a comma and tilde delimited list of APSAuxResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  */  
   APSAuxResource:string,
      /**  Additional resource requirements.   This is a comma and tilde delimited list of APSAddResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  For Additional Resources the Duration = 5 (entire Operation).  */  
   APSAddResource:string,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  */  
   LaborEntryMethod:string,
      /**  The quantity requested for first article inspection.  */  
   FAQty:number,
      /**  A flag to indicate that this part operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  */  
   RFQNeeded:boolean,
      /**  The number of vendor quotes that are required for this part subcontract operation.  Can be zero if RFQ(s) are not required.  */  
   RFQVendQuotes:number,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   GroupID:string,
      /**  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  */  
   OrigOprSeq:number,
      /**  Used to group operation to save on setups.  */  
   SetupGroup:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**   Identifies the primary ECOOpDtl to be used for setup.  The setup time for the operation is determined on the ECOOpDtl.
If <> 0, must identify a valid ECOOpDtl.  The ECOOpDtl needs to have a RequiredFor = S or B.  */  
   PrimarySetupOpDtl:number,
      /**   Identifies the primary ECOOpDtl to be used for production.  The production run time for the operation is determined on the ECOOpDtl.
If <> 0, must identify a valid ECOOpDtl.  The ECOOpDtl needs to have a RequiredFor = P or B.  */  
   PrimaryProdOpDtl:number,
      /**  Alternate Routing method for the part revision.  */  
   AltMethod:string,
      /**  Operation Description.  */  
   OpDesc:string,
      /**  The stage number of the operations.  Entered only when the related PartRev.UseStaging flag is true.  */  
   StageNumber:string,
      /**  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  */  
   BaseMethodOverridden:boolean,
      /**  Parent Alternate Routing method of this part operation.  */  
   ParentAltMethod:string,
      /**  Indicates the parent operation sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  */  
   ParentOprSeq:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty01:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty02:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty03:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty04:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty05:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty06:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty07:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty08:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty09:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty10:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost01:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost02:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost03:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost04:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost05:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost06:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost07:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost08:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost09:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost10:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate01:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate02:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate03:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate04:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate05:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate06:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate07:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate08:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate09:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate10:number,
      /**  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  */  
   SNRequiredOpr:boolean,
      /**  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  */  
   SNRequiredSubConShip:boolean,
      /**  Operation Weight defaulted from Part Master.  */  
   Weight:number,
      /**  Operation Weight UOM defaulted from Part Master.  */  
   WeightUOM:string,
      /**   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  */  
   SendAheadType:string,
      /**   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  */  
   SendAheadOffset:number,
      /**  Delimited list of PrjRoleCd codes that are allowed for this operation.  */  
   PrjRoleList:string,
      /**  Allow use all Roles  */  
   UseAllRoles:boolean,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  PctReg  */  
   PctReg:number,
      /**  SetupMaterial  */  
   SetupMaterial:number,
      /**  MaterialColorRating  */  
   MaterialColorRating:number,
      /**  MiscInfo1  */  
   MiscInfo1:string,
      /**  MiscInfo2  */  
   MiscInfo2:string,
      /**  SetupURL  */  
   SetupURL:string,
      /**  ExpPctUp  */  
   ExpPctUp:number,
      /**  ExpCycTm  */  
   ExpCycTm:number,
      /**  ExpGood  */  
   ExpGood:number,
      /**  NonProdLimit  */  
   NonProdLimit:number,
      /**  AutoSpcEnable  */  
   AutoSpcEnable:boolean,
      /**  AutoSpcPeriod  */  
   AutoSpcPeriod:number,
      /**  PartQualEnable  */  
   PartQualEnable:boolean,
      /**  AutoSpcSubgroup  */  
   AutoSpcSubgroup:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PulsesPerCycle  */  
   PulsesPerCycle:number,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   QtyPerCycle:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  The identifier of related Process Manufacturing.  */  
   ProcessMfgID:string,
      /**  TemplateID  */  
   TemplateID:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   SubRevisionNum:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ECOOprListTableset{
   ECOOprList:Erp_Tablesets_ECOOprListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ECOOprRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   OprSeq:number,
      /**   Operation Master Code - Links the JobOper  record with a OpMaster record. Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  */  
   OpCode:string,
      /**   The Operation standard ID. This links the JobOPer to the OpStd master file. This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.
Valid for "inside operations" only.  */  
   OpStdID:string,
      /**  The estimated set up hours. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours.  */  
   EstSetHours:number,
      /**   The estimated Production run hours for internal operations (Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (RunQty / Std).
If StdFormat = "PM" then (RunQty / Std ) / 60.
If StdFormat = "OH" then (RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (RunQty/Basis) X Std.
If StdFormat = "MP" then ((RunQty/Basis) X Std) / 60.  */  
   EstProdHours:number,
      /**   The production standard for the operation. It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours. A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  */  
   ProdStandard:number,
      /**   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  */  
   StdFormat:string,
      /**   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   StdBasis:string,
      /**  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  */  
   OpsPerPart:number,
      /**  Production Quantity per one of the Parent Item.  */  
   QtyPer:number,
      /**  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  */  
   Machines:number,
      /**  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to se tup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   SetUpCrewSize:number,
      /**  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  */  
   ProdCrewSize:number,
      /**  Estimated Scrap  */  
   EstScrap:number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   EstScrapType:string,
      /**  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  */  
   SubContract:boolean,
      /**  Inventory UOM  */  
   IUM:string,
      /**  Estimated Unit Cost for the SubContract operation.  Defaults from the Part table if valid PartNum.  */  
   EstUnitCost:number,
      /**  Hours required is calculated as days * 8.  */  
   DaysOut:number,
      /**  The PartNum to be shipped to the subcontract. Defaults as the Part number of the method to which it belongs (ECOOpr.PartNum).  */  
   SubPartNum:string,
      /**  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  */  
   PurPoint:string,
      /**  Editor widget for Job operation comments.  */  
   CommentText:string,
      /**   Indicates the scheduling relationship between this and the preceding operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  */  
   SchedRelation:string,
      /**  The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0. This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  */  
   RunQty:number,
      /**  Additional Setup Hours that will be required after a certain quantity has been run for this operation. The quantity at which this occurs is established in AddSetupQty field. The system determines the setup hours as SetupHrs + (Max((RunQty - AddlSetupQty,0))/AddlSetUpQty) * AddlSetupHours. Any fractional results of the AddlSetUpQty calculations are rounded up to the next whole number before multiplying by the AddlSetUpHours.  */  
   AddlSetupHours:number,
      /**  Additional Setup quantity indicates the quantity at which additional setup time will be incurred.  */  
   AddlSetUpQty:number,
      /**  Indicates the operation that must precede this operation.  Mainly used to model one to many routing structures.  */  
   APSPrepOp:number,
      /**  This is the next operation in the routing.  -1 makes this operation the last one in the routing so far; -2 makes it the first one in the routing so far; 0 means no successor.  */  
   APSNextOp:number,
      /**  Specifies the operation for which this is an alternate.  */  
   APSAltOp:number,
      /**  Used to assign an operation to a specific resource so that APS does not schedule it elsewhere.  Overrides APSCapability.  */  
   APSSpecificResource:string,
      /**   Cycles per minute.
SQL:  IIF(CINT(JobOper.RunQty) = 0 OR JobOper.SubContract = TRUE, "0", JobOper.EstProdHours * 60 /  JobOper.RunQty)  */  
   APSCycleTime:number,
      /**   Fixed time, in decimal minutes, to be added to the operation.  Can be used to represent cleanup time or model outsource time.
SQL: IFF(JobOper.SubContract = TRUE, (JobOper.DaysOut * 1440), "0")  */  
   APSConstantTime:number,
      /**  Used to group operations to save on setups.  */  
   APSSetupGroup:number,
      /**  Quantity of Part per cycle.  */  
   APSMakeFactor:number,
      /**  Quantity that must be completed before the next operation can start (for overlap); quantity per batch (for batch resources); Auxiliary resource quantity.  */  
   APSContainerSize:number,
      /**  Name of the APS Scheduler Module in which to schedule this operation.  */  
   APSSchedulerName:string,
      /**  If the scheduled time exceeds this value then the operation is split into operations which do not exceed this length.  */  
   APSMaxLength:number,
      /**  Time between the end of this operation and the start time of the successor operation.  */  
   APSTransferTime:number,
      /**  Cycle time and constant times are divided by this value to get schedule times.  Zeros disable this feature.  */  
   APSEffectiveness:number,
      /**  Type of Operation: P for Prep, D for Processing (Dispatchable in APS terminology).  */  
   APSOperationClass:string,
      /**  Auxiliary resource requirements.   This is a comma and tilde delimited list of APSAuxResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  */  
   APSAuxResource:string,
      /**  Additional resource requirements.   This is a comma and tilde delimited list of APSAddResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  For Additional Resources the Duration = 5 (entire Operation).  */  
   APSAddResource:string,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  */  
   LaborEntryMethod:string,
      /**  The quantity requested for first article inspection.  */  
   FAQty:number,
      /**  A flag to indicate that this part operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  */  
   RFQNeeded:boolean,
      /**  The number of vendor quotes that are required for this part subcontract operation.  Can be zero if RFQ(s) are not required.  */  
   RFQVendQuotes:number,
      /**  The Group ID is the unique identifier for the ECO Group  */  
   GroupID:string,
      /**  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  */  
   OrigOprSeq:number,
      /**  Used to group operation to save on setups.  */  
   SetupGroup:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**   Identifies the primary ECOOpDtl to be used for setup.  The setup time for the operation is determined on the ECOOpDtl.
If <> 0, must identify a valid ECOOpDtl.  The ECOOpDtl needs to have a RequiredFor = S or B.  */  
   PrimarySetupOpDtl:number,
      /**   Identifies the primary ECOOpDtl to be used for production.  The production run time for the operation is determined on the ECOOpDtl.
If <> 0, must identify a valid ECOOpDtl.  The ECOOpDtl needs to have a RequiredFor = P or B.  */  
   PrimaryProdOpDtl:number,
      /**  Alternate Routing method for the part revision.  */  
   AltMethod:string,
      /**  Operation Description.  */  
   OpDesc:string,
      /**  The stage number of the operations.  Entered only when the related PartRev.UseStaging flag is true.  */  
   StageNumber:string,
      /**  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  */  
   BaseMethodOverridden:boolean,
      /**  Parent Alternate Routing method of this part operation.  */  
   ParentAltMethod:string,
      /**  Indicates the parent operation sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  */  
   ParentOprSeq:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty01:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty02:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty03:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty04:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty05:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty06:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty07:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty08:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty09:number,
      /**  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty10:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost01:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost02:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost03:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost04:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost05:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost06:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost07:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost08:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost09:number,
      /**  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  */  
   PBrkCost10:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate01:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate02:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate03:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate04:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate05:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate06:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate07:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate08:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate09:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  */  
   PBrkStdRate10:number,
      /**  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  */  
   SNRequiredOpr:boolean,
      /**  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  */  
   SNRequiredSubConShip:boolean,
      /**  Operation Weight defaulted from Part Master.  */  
   Weight:number,
      /**  Operation Weight UOM defaulted from Part Master.  */  
   WeightUOM:string,
      /**   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  */  
   SendAheadType:string,
      /**   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  */  
   SendAheadOffset:number,
      /**  Delimited list of PrjRoleCd codes that are allowed for this operation.  */  
   PrjRoleList:string,
      /**  Allow use all Roles  */  
   UseAllRoles:boolean,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  PctReg  */  
   PctReg:number,
      /**  SetupMaterial  */  
   SetupMaterial:number,
      /**  MaterialColorRating  */  
   MaterialColorRating:number,
      /**  MiscInfo1  */  
   MiscInfo1:string,
      /**  MiscInfo2  */  
   MiscInfo2:string,
      /**  SetupURL  */  
   SetupURL:string,
      /**  ExpPctUp  */  
   ExpPctUp:number,
      /**  ExpCycTm  */  
   ExpCycTm:number,
      /**  ExpGood  */  
   ExpGood:number,
      /**  NonProdLimit  */  
   NonProdLimit:number,
      /**  AutoSpcEnable  */  
   AutoSpcEnable:boolean,
      /**  AutoSpcPeriod  */  
   AutoSpcPeriod:number,
      /**  PartQualEnable  */  
   PartQualEnable:boolean,
      /**  AutoSpcSubgroup  */  
   AutoSpcSubgroup:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PulsesPerCycle  */  
   PulsesPerCycle:number,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   QtyPerCycle:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  The identifier of related Process Manufacturing.  */  
   ProcessMfgID:string,
      /**  TemplateID  */  
   TemplateID:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   SubRevisionNum:string,
      /**  The vendor's name and bill to address  */  
   DspBillAddr:string,
      /**  Field used to control the flag on SNRequiredSubConShip field on UI screens.  */  
   EnableSNReqSubConShip:boolean,
      /**  Used as a flag to enable controls on UI screens  */  
   EnableSNRequiredOpr:boolean,
      /**  The final operation field  */  
   FinalOpr:boolean,
      /**  Flag to let you know if you have price breaks.  */  
   HasPriceBreaks:boolean,
      /**  Is this a PartOpr?  Used when building the tree to show PartOpr as ECOOpr.  */  
   IsPartOpr:boolean,
      /**  The original or old OprSeq.  Used when changing the OprSeq.  */  
   OldOprSeq:number,
   OpStdDescription:string,
      /**  PML ID  */  
   PLMChar03:string,
      /**  Primary Resource Group description  */  
   PrimaryResourceGrpDesc:string,
      /**  The Resource Group ID of the primary production operation detail.  */  
   PrimaryResourceGrpID:string,
      /**  Indicates if the scheduling resources should be refreshed when the op code changes.  */  
   RefreshResources:boolean,
      /**  The setup hours per machines.  */  
   SetHoursPerMach:number,
      /**  The standard format description.  */  
   StdFrmtDesc:string,
      /**  The value of the ecorev.usestaging field for UI purposes  */  
   UseStaging:boolean,
      /**  The auto receive field  */  
   AutoReceive:boolean,
   EnableAttributeSetSearch:boolean,
   PrimaryProdOpDtlDesc:string,
   PrimarySetupOpDtlDesc:string,
   BitFlag:number,
   AnalysisCdDescription:string,
   APSSchedulerNameAPSSchedulerName:string,
   DynAttrValueSetShortDescription:string,
   DynAttrValueSetDescription:string,
   GroupIDDescription:string,
   OpCodeOpDesc:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumIUM:string,
   PartNumTrackDimension:boolean,
   PartNumTrackLots:boolean,
   PartNumSellingFactor:number,
   PartNumTrackSerialNum:boolean,
   PartNumPricePerCode:string,
   PartNumPartDescription:string,
   PartNumSalesUM:string,
   PrimaryProdOpDtlOpDtlDesc:string,
   PrimarySetupOpDtlOpDtlDesc:string,
   RevisionNumRevShortDesc:string,
   RevisionNumRevDescription:string,
   RevisionNumPartDescription:string,
   SetupGroupDescription:string,
   StageNoDescription:string,
   SubPartNumTrackInventoryAttributes:boolean,
   SubPartNumPricePerCode:string,
   SubPartNumTrackDimension:boolean,
   SubPartNumTrackSerialNum:boolean,
   SubPartNumSellingFactor:number,
   SubPartNumTrackLots:boolean,
   SubPartNumSalesUM:string,
   SubPartNumPartDescription:string,
   SubPartNumIUM:string,
   SubPartNumAttrClassID:string,
   SubPartNumTrackInventoryByRevision:boolean,
   VendorNumDefaultFOB:string,
   VendorNumCurrencyCode:string,
   VendorNumCity:string,
   VendorNumVendorID:string,
   VendorNumName:string,
   VendorNumState:string,
   VendorNumAddress1:string,
   VendorNumZIP:string,
   VendorNumTermsCode:string,
   VendorNumAddress3:string,
   VendorNumAddress2:string,
   VendorNumCountry:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ECOOprSearchTableset{
   ECOOpr:Erp_Tablesets_ECOOprRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtECOOprSearchTableset{
   ECOOpr:Erp_Tablesets_ECOOprRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param groupID
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
      @param oprSeq
   */  
export interface GetByID_input{
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
   oprSeq:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ECOOprSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ECOOprSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ECOOprSearchTableset[],
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
   returnObj:Erp_Tablesets_ECOOprListTableset[],
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
      @param processMfgID
   */  
export interface GetNewECOOpr_input{
   ds:Erp_Tablesets_ECOOprSearchTableset[],
   groupID:string,
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
}

export interface GetNewECOOpr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ECOOprSearchTableset[],
}
}

   /** Required : 
      @param whereClauseECOOpr
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseECOOpr:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ECOOprSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtECOOprSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtECOOprSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ECOOprSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ECOOprSearchTableset[],
}
}

