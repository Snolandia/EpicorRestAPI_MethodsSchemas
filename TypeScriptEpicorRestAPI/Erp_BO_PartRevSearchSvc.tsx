import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PartRevSearchSvc
// Description: PartRev search
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/$metadata", {
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
   Description: Get PartRevSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartRevSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartRevRow
   */  
export function get_PartRevSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartRevRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/PartRevSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartRevRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartRevSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartRevRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PartRevRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartRevSearches(requestBody:Erp_Tablesets_PartRevRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/PartRevSearches", {
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
   Summary: Calls GetByID to retrieve the PartRevSearch item
   Description: Calls GetByID to retrieve the PartRevSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartRevSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PartRevRow
   */  
export function get_PartRevSearches_Company_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartRevRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/PartRevSearches(" + Company + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")", {
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
         resolve(data as Erp_Tablesets_PartRevRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PartRevSearch for the service
   Description: Calls UpdateExt to update PartRevSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartRevSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param AltMethod Desc: AltMethod   Required: True   Allow empty value : True
      @param ProcessMfgID Desc: ProcessMfgID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartRevRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PartRevSearches_Company_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, requestBody:Erp_Tablesets_PartRevRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/PartRevSearches(" + Company + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")", {
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
   Summary: Call UpdateExt to delete PartRevSearch item
   Description: Call UpdateExt to delete PartRevSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartRevSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
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
export function delete_PartRevSearches_Company_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company:string, PartNum:string, RevisionNum:string, AltMethod:string, ProcessMfgID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/PartRevSearches(" + Company + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartRevListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartRevListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartRevListRow)
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
export function get_GetRows(whereClausePartRev:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePartRev!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartRev=" + whereClausePartRev
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/GetRows" + params, {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(partNum:string, revisionNum:string, altMethod:string, processMfgID:string, epicorHeaders?:Headers){
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/GetList" + params, {
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
   Summary: Invoke method PartRevionsExists
   Description: Determine id a part revision exists
   OperationID: PartRevionsExists
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PartRevionsExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartRevionsExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartRevionsExists(requestBody:PartRevionsExists_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PartRevionsExists_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/PartRevionsExists", {
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
         resolve(data as PartRevionsExists_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FindRevsionRecord
   Description: Find first part revision based on criteria.
   OperationID: FindRevsionRecord
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FindRevsionRecord_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindRevsionRecord_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FindRevsionRecord(requestBody:FindRevsionRecord_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FindRevsionRecord_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/FindRevsionRecord", {
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
         resolve(data as FindRevsionRecord_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAltMethodByPlant
   Description: Get appropriate Part Revision (Alt Method) according to parameters.
If there are several methods with the same date and plant then get primary Atl Method
   OperationID: GetAltMethodByPlant
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAltMethodByPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAltMethodByPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAltMethodByPlant(requestBody:GetAltMethodByPlant_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAltMethodByPlant_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/GetAltMethodByPlant", {
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
         resolve(data as GetAltMethodByPlant_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPartRevListByConfigID
   OperationID: GetPartRevListByConfigID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPartRevListByConfigID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartRevListByConfigID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartRevListByConfigID(requestBody:GetPartRevListByConfigID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPartRevListByConfigID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/GetPartRevListByConfigID", {
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
         resolve(data as GetPartRevListByConfigID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFirstPartRevByDateDescending
   OperationID: GetFirstPartRevByDateDescending
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFirstPartRevByDateDescending_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFirstPartRevByDateDescending_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFirstPartRevByDateDescending(requestBody:GetFirstPartRevByDateDescending_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFirstPartRevByDateDescending_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/GetFirstPartRevByDateDescending", {
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
         resolve(data as GetFirstPartRevByDateDescending_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPartRev
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartRev
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPartRev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartRev_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartRev(requestBody:GetNewPartRev_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPartRev_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/GetNewPartRev", {
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
         resolve(data as GetNewPartRev_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartRevListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartRevListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartRevRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartRevRow,
}

export interface Erp_Tablesets_PartRevListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part and is used as part of the primary key.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  */  
   "RevisionNum":string,
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
      /**  An internal flag which indicates that this part revision contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   "Method":boolean,
      /**   The operation number PartOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   "AutoRecOpr":number,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   "FinalOpr":number,
      /**  Holds the internal object id of pdm parts.  */  
   "PDMObjID":string,
      /**  If true then the revision has a configuration defined for it.  This will be set when a configuration is approved.  */  
   "Configured":boolean,
      /**  If set to TRUE then the revision can be configured in StoreFront.  */  
   "WebConfigured":boolean,
      /**  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  */  
   "ShowInputPrice":boolean,
      /**  Alternate Routing method to be used for this revision, and is used as part of the primary key  */  
   "AltMethod":string,
      /**  The description of the alternate method.  */  
   "AltMethodDesc":string,
      /**  Site Identifier. This field cannot be blank.  */  
   "Plant":string,
      /**  The alternate method of the parent this method inherits from.  */  
   "ParentAltMethod":string,
      /**  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  */  
   "UseStaging":boolean,
      /**  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  */  
   "UseAltRevForParts":boolean,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   "OwnershipStatus":string,
      /**  External Configurator  */  
   "ExtConfig":boolean,
      /**  Validate Reference Designators.  */  
   "ValRefDes":boolean,
      /**  Is the part for this revision a global part  */  
   "PcGlobalPart":boolean,
      /**  If a configuration is created for this revision, is it marked as enterprise configurator  */  
   "PcEntprsConf":boolean,
      /**  Marks the Part Revision as a global Revision, available to be sent out to other companies  */  
   "GlobalRev":boolean,
      /**  Rough Cut Code.  Rough cut parameters to use when rough cut scheduling for the revision.  */  
   "RoughCutCode":string,
      /**  The inspection plan part number (configurator part number) to use for RMA processing for this part.  */  
   "RMAInspPlan":string,
      /**  The specification ID to use for RMA processing for this part.  */  
   "RMASpecID":string,
      /**  The default sample size to use for RMA processing for this part  */  
   "RMASampleSize":number,
      /**  Percentage of quantity to be inspected for RMA processing of this part  */  
   "RMASampleSizePct":number,
      /**  The part number used to identify the configured part number that this part revision was created from  */  
   "BasePartNum":string,
      /**  The revision number used to identify the configured part revision this part number was generated from.  */  
   "BaseRevisionNum":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The identifier of related Process Manufacturing.  */  
   "ProcessMfgID":string,
      /**  Last date that this Revison is effective.  (Next Rev Effective date - 1)  */  
   "vDate":string,
   "vQty":number,
   "ProdCode":string,
   "NonStock":boolean,
   "Class":string,
   "ParentAltMethodDesc":string,
      /**  Name of ECO Group that this part is checked out to  */  
   "ECOGroup":string,
   "DisableApproved":boolean,
   "SpecHedDescription":string,
      /**  The description of the inspection plan  */  
   "InspPlanDescription":string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartDescriptionPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartDescriptionTrackDimension":boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartDescriptionIUM":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartDescriptionSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartDescriptionTrackLots":boolean,
      /**  Describes the Part.  */  
   "PartDescriptionPartDescription":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartDescriptionSellingFactor":number,
      /**  Indicates if this part is serial number tracked  */  
   "PartDescriptionTrackSerialNum":boolean,
      /**  The Plant name. Used on shipping reports.  */  
   "PlantName":string,
      /**  Full description of the rough cut parameter set.  */  
   "RoughCutParamDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartRevRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part and is used as part of the primary key.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  */  
   "RevisionNum":string,
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
      /**  An internal flag which indicates that this part revision contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   "Method":boolean,
      /**   The operation number PartOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   "AutoRecOpr":number,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   "FinalOpr":number,
      /**  Holds the internal object id of pdm parts.  */  
   "PDMObjID":string,
      /**  If true then the revision has a configuration defined for it.  This will be set when a configuration is approved.  */  
   "Configured":boolean,
      /**  If set to TRUE then the revision can be configured in StoreFront.  */  
   "WebConfigured":boolean,
      /**  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  */  
   "ShowInputPrice":boolean,
      /**  Alternate Routing method to be used for this revision, and is used as part of the primary key  */  
   "AltMethod":string,
      /**  The description of the alternate method.  */  
   "AltMethodDesc":string,
      /**  Site Identifier. This field cannot be blank.  */  
   "Plant":string,
      /**  The alternate method of the parent this method inherits from.  */  
   "ParentAltMethod":string,
      /**  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  */  
   "UseStaging":boolean,
      /**  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  */  
   "UseAltRevForParts":boolean,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   "OwnershipStatus":string,
      /**  External Configurator  */  
   "ExtConfig":boolean,
      /**  Validate Reference Designators.  */  
   "ValRefDes":boolean,
      /**  Is the part for this revision a global part  */  
   "PcGlobalPart":boolean,
      /**  If a configuration is created for this revision, is it marked as enterprise configurator  */  
   "PcEntprsConf":boolean,
      /**  Marks the Part Revision as a global Revision, available to be sent out to other companies  */  
   "GlobalRev":boolean,
      /**  Rough Cut Code.  Rough cut parameters to use when rough cut scheduling for the revision.  */  
   "RoughCutCode":string,
      /**  The inspection plan part number (configurator part number) to use for RMA processing for this part.  */  
   "RMAInspPlan":string,
      /**  The specification ID to use for RMA processing for this part.  */  
   "RMASpecID":string,
      /**  The default sample size to use for RMA processing for this part  */  
   "RMASampleSize":number,
      /**  Percentage of quantity to be inspected for RMA processing of this part  */  
   "RMASampleSizePct":number,
      /**  The part number used to identify the configured part number that this part revision was created from  */  
   "BasePartNum":string,
      /**  The revision number used to identify the configured part revision this part number was generated from.  */  
   "BaseRevisionNum":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  RegenConfig  */  
   "RegenConfig":boolean,
      /**  SIValuesGroupSeq  */  
   "SIValuesGroupSeq":number,
      /**  SIValuesHeadNum  */  
   "SIValuesHeadNum":number,
      /**  Indicates the record is used with Machine MES  */  
   "ExternalMES":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates the way in which parts are made for Co-Part jobs.  There are two value “S” – Sequential and “C” – Concurrent.  Sequential is the default. This field is similar to the JobHead.ProcessMode field.  */  
   "ProcessMode":string,
      /**  DefaultConfigPart  */  
   "DefaultConfigPart":boolean,
      /**  Number of COPart required in the Revision  */  
   "CoPartsReqQty":number,
      /**  Material Cost Factor  */  
   "MtlCostPct":number,
      /**  Labor Cost Factor  */  
   "LaborCostPct":number,
      /**  Number of COParts per Operation  */  
   "CoPartsPerOp":number,
      /**  CreatedBy  */  
   "CreatedBy":string,
      /**  CreatedOn  */  
   "CreatedOn":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangedOn  */  
   "ChangedOn":string,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   "ExternalMESSyncRequired":boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   "ExternalMESLastSync":string,
      /**  Customs BOM  */  
   "CNCustomsBOM":boolean,
      /**  The identifier of related Process Manufacturing.  */  
   "ProcessMfgID":string,
      /**  Type of Process Manufacturing this revision is for: General, Site, Master.  */  
   "ProcessMfgType":string,
      /**  Description of Process Manufacturing revision.  */  
   "ProcessMfgDescription":string,
      /**  Indicates if this revision is to use Advanced Staging.  */  
   "UseAdvancedStaging":boolean,
      /**  The last Group to modify this Revision for Recipe Authoring.  */  
   "ProcessMfgLastGroupID":string,
      /**  Only Part Revisions marked as Connected Process Control (CPC) enable will be send to CPC.  */  
   "ECPCEnabled":boolean,
   "DisableApproved":boolean,
      /**  Name of ECO Group that this part is checked out to  */  
   "ECOGroup":string,
      /**  This field will be set to true if two or more ECOCoParts records exist for the revision.  */  
   "HasCoParts":boolean,
   "ParentAltMethodDesc":string,
      /**  Part Number of the Parent Part  */  
   "ParentPartNum":string,
      /**  Revision number  of Parent Part.  */  
   "ParentRevisionNum":string,
   "ProdCode":string,
      /**   Revision Status used to determina in the Revision of all the Materials are Effective As Of Date
Used to indicate the MAX MtlRevisionStatus of all its Materials/SubAssemblies.
If <= 2 the all its materials/subAssemblies's Revisions are Effective As Of Date  */  
   "RevStatusAsOfDate":number,
   "SpecHedDescription":string,
      /**  Last date that this Revison is effective.  (Next Rev Effective date - 1)  */  
   "vDate":string,
   "vQty":number,
   "Class":string,
   "NonStock":boolean,
      /**  Indicates that the PartRev is the root node in the tree  */  
   "IsRootNode":boolean,
      /**  Holds the ECORev Approved flag for the last ProcessMfgID specified against the PartRev  */  
   "EngineeringApproved":boolean,
   "BitFlag":number,
   "InspPlanDescription":string,
   "PartDescriptionTrackDimension":boolean,
   "PartDescriptionSellingFactor":number,
   "PartDescriptionPartDescription":string,
   "PartDescriptionIUM":string,
   "PartDescriptionTrackLots":boolean,
   "PartDescriptionPricePerCode":string,
   "PartDescriptionSalesUM":string,
   "PartDescriptionTrackSerialNum":boolean,
   "PartDescriptionTypeCode":string,
   "PcStatusConfigType":string,
   "PlantName":string,
   "RoughCutParamDescription":string,
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
      @param revisionNum
      @param altMethod
      @param processMfgID
   */  
export interface DeleteByID_input{
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PartRevListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as part of the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  */  
   RevisionNum:string,
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
      /**  An internal flag which indicates that this part revision contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   Method:boolean,
      /**   The operation number PartOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   AutoRecOpr:number,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   FinalOpr:number,
      /**  Holds the internal object id of pdm parts.  */  
   PDMObjID:string,
      /**  If true then the revision has a configuration defined for it.  This will be set when a configuration is approved.  */  
   Configured:boolean,
      /**  If set to TRUE then the revision can be configured in StoreFront.  */  
   WebConfigured:boolean,
      /**  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  */  
   ShowInputPrice:boolean,
      /**  Alternate Routing method to be used for this revision, and is used as part of the primary key  */  
   AltMethod:string,
      /**  The description of the alternate method.  */  
   AltMethodDesc:string,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  The alternate method of the parent this method inherits from.  */  
   ParentAltMethod:string,
      /**  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  */  
   UseStaging:boolean,
      /**  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  */  
   UseAltRevForParts:boolean,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   OwnershipStatus:string,
      /**  External Configurator  */  
   ExtConfig:boolean,
      /**  Validate Reference Designators.  */  
   ValRefDes:boolean,
      /**  Is the part for this revision a global part  */  
   PcGlobalPart:boolean,
      /**  If a configuration is created for this revision, is it marked as enterprise configurator  */  
   PcEntprsConf:boolean,
      /**  Marks the Part Revision as a global Revision, available to be sent out to other companies  */  
   GlobalRev:boolean,
      /**  Rough Cut Code.  Rough cut parameters to use when rough cut scheduling for the revision.  */  
   RoughCutCode:string,
      /**  The inspection plan part number (configurator part number) to use for RMA processing for this part.  */  
   RMAInspPlan:string,
      /**  The specification ID to use for RMA processing for this part.  */  
   RMASpecID:string,
      /**  The default sample size to use for RMA processing for this part  */  
   RMASampleSize:number,
      /**  Percentage of quantity to be inspected for RMA processing of this part  */  
   RMASampleSizePct:number,
      /**  The part number used to identify the configured part number that this part revision was created from  */  
   BasePartNum:string,
      /**  The revision number used to identify the configured part revision this part number was generated from.  */  
   BaseRevisionNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The identifier of related Process Manufacturing.  */  
   ProcessMfgID:string,
      /**  Last date that this Revison is effective.  (Next Rev Effective date - 1)  */  
   vDate:string,
   vQty:number,
   ProdCode:string,
   NonStock:boolean,
   Class:string,
   ParentAltMethodDesc:string,
      /**  Name of ECO Group that this part is checked out to  */  
   ECOGroup:string,
   DisableApproved:boolean,
   SpecHedDescription:string,
      /**  The description of the inspection plan  */  
   InspPlanDescription:string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartDescriptionPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartDescriptionTrackDimension:boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartDescriptionIUM:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartDescriptionSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartDescriptionTrackLots:boolean,
      /**  Describes the Part.  */  
   PartDescriptionPartDescription:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartDescriptionSellingFactor:number,
      /**  Indicates if this part is serial number tracked  */  
   PartDescriptionTrackSerialNum:boolean,
      /**  The Plant name. Used on shipping reports.  */  
   PlantName:string,
      /**  Full description of the rough cut parameter set.  */  
   RoughCutParamDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartRevListTableset{
   PartRevList:Erp_Tablesets_PartRevListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartRevRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as part of the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  */  
   RevisionNum:string,
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
      /**  An internal flag which indicates that this part revision contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   Method:boolean,
      /**   The operation number PartOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   AutoRecOpr:number,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   FinalOpr:number,
      /**  Holds the internal object id of pdm parts.  */  
   PDMObjID:string,
      /**  If true then the revision has a configuration defined for it.  This will be set when a configuration is approved.  */  
   Configured:boolean,
      /**  If set to TRUE then the revision can be configured in StoreFront.  */  
   WebConfigured:boolean,
      /**  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  */  
   ShowInputPrice:boolean,
      /**  Alternate Routing method to be used for this revision, and is used as part of the primary key  */  
   AltMethod:string,
      /**  The description of the alternate method.  */  
   AltMethodDesc:string,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  The alternate method of the parent this method inherits from.  */  
   ParentAltMethod:string,
      /**  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  */  
   UseStaging:boolean,
      /**  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  */  
   UseAltRevForParts:boolean,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   OwnershipStatus:string,
      /**  External Configurator  */  
   ExtConfig:boolean,
      /**  Validate Reference Designators.  */  
   ValRefDes:boolean,
      /**  Is the part for this revision a global part  */  
   PcGlobalPart:boolean,
      /**  If a configuration is created for this revision, is it marked as enterprise configurator  */  
   PcEntprsConf:boolean,
      /**  Marks the Part Revision as a global Revision, available to be sent out to other companies  */  
   GlobalRev:boolean,
      /**  Rough Cut Code.  Rough cut parameters to use when rough cut scheduling for the revision.  */  
   RoughCutCode:string,
      /**  The inspection plan part number (configurator part number) to use for RMA processing for this part.  */  
   RMAInspPlan:string,
      /**  The specification ID to use for RMA processing for this part.  */  
   RMASpecID:string,
      /**  The default sample size to use for RMA processing for this part  */  
   RMASampleSize:number,
      /**  Percentage of quantity to be inspected for RMA processing of this part  */  
   RMASampleSizePct:number,
      /**  The part number used to identify the configured part number that this part revision was created from  */  
   BasePartNum:string,
      /**  The revision number used to identify the configured part revision this part number was generated from.  */  
   BaseRevisionNum:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  RegenConfig  */  
   RegenConfig:boolean,
      /**  SIValuesGroupSeq  */  
   SIValuesGroupSeq:number,
      /**  SIValuesHeadNum  */  
   SIValuesHeadNum:number,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates the way in which parts are made for Co-Part jobs.  There are two value “S” – Sequential and “C” – Concurrent.  Sequential is the default. This field is similar to the JobHead.ProcessMode field.  */  
   ProcessMode:string,
      /**  DefaultConfigPart  */  
   DefaultConfigPart:boolean,
      /**  Number of COPart required in the Revision  */  
   CoPartsReqQty:number,
      /**  Material Cost Factor  */  
   MtlCostPct:number,
      /**  Labor Cost Factor  */  
   LaborCostPct:number,
      /**  Number of COParts per Operation  */  
   CoPartsPerOp:number,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangedOn  */  
   ChangedOn:string,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
      /**  Customs BOM  */  
   CNCustomsBOM:boolean,
      /**  The identifier of related Process Manufacturing.  */  
   ProcessMfgID:string,
      /**  Type of Process Manufacturing this revision is for: General, Site, Master.  */  
   ProcessMfgType:string,
      /**  Description of Process Manufacturing revision.  */  
   ProcessMfgDescription:string,
      /**  Indicates if this revision is to use Advanced Staging.  */  
   UseAdvancedStaging:boolean,
      /**  The last Group to modify this Revision for Recipe Authoring.  */  
   ProcessMfgLastGroupID:string,
      /**  Only Part Revisions marked as Connected Process Control (CPC) enable will be send to CPC.  */  
   ECPCEnabled:boolean,
   DisableApproved:boolean,
      /**  Name of ECO Group that this part is checked out to  */  
   ECOGroup:string,
      /**  This field will be set to true if two or more ECOCoParts records exist for the revision.  */  
   HasCoParts:boolean,
   ParentAltMethodDesc:string,
      /**  Part Number of the Parent Part  */  
   ParentPartNum:string,
      /**  Revision number  of Parent Part.  */  
   ParentRevisionNum:string,
   ProdCode:string,
      /**   Revision Status used to determina in the Revision of all the Materials are Effective As Of Date
Used to indicate the MAX MtlRevisionStatus of all its Materials/SubAssemblies.
If <= 2 the all its materials/subAssemblies's Revisions are Effective As Of Date  */  
   RevStatusAsOfDate:number,
   SpecHedDescription:string,
      /**  Last date that this Revison is effective.  (Next Rev Effective date - 1)  */  
   vDate:string,
   vQty:number,
   Class:string,
   NonStock:boolean,
      /**  Indicates that the PartRev is the root node in the tree  */  
   IsRootNode:boolean,
      /**  Holds the ECORev Approved flag for the last ProcessMfgID specified against the PartRev  */  
   EngineeringApproved:boolean,
   BitFlag:number,
   InspPlanDescription:string,
   PartDescriptionTrackDimension:boolean,
   PartDescriptionSellingFactor:number,
   PartDescriptionPartDescription:string,
   PartDescriptionIUM:string,
   PartDescriptionTrackLots:boolean,
   PartDescriptionPricePerCode:string,
   PartDescriptionSalesUM:string,
   PartDescriptionTrackSerialNum:boolean,
   PartDescriptionTypeCode:string,
   PcStatusConfigType:string,
   PlantName:string,
   RoughCutParamDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartRevSearchTableset{
   PartRev:Erp_Tablesets_PartRevRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPartRevSearchTableset{
   PartRev:Erp_Tablesets_PartRevRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param partnum
      @param revisionNum
      @param altMethod
   */  
export interface FindRevsionRecord_input{
   partnum:string,
   revisionNum:string,
   altMethod:string,
}

export interface FindRevsionRecord_output{
   returnObj:Erp_Tablesets_PartRevSearchTableset[],
}

   /** Required : 
      @param ipPartNum
      @param ipRevisionNum
      @param ipAsOfDate
      @param ipPlant
   */  
export interface GetAltMethodByPlant_input{
      /**  The Part Number to return data for.  */  
   ipPartNum:string,
      /**  The Revision Number to return data for.  */  
   ipRevisionNum:string,
      /**  The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  The Plant to return data for.  */  
   ipPlant:string,
}

export interface GetAltMethodByPlant_output{
parameters : {
      /**  output parameters  */  
   outAltMethod:string,
}
}

   /** Required : 
      @param partNum
      @param revisionNum
      @param altMethod
      @param processMfgID
   */  
export interface GetByID_input{
   partNum:string,
   revisionNum:string,
   altMethod:string,
   processMfgID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PartRevSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PartRevSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PartRevSearchTableset[],
}

   /** Required : 
      @param cPartNum
   */  
export interface GetFirstPartRevByDateDescending_input{
   cPartNum:string,
}

export interface GetFirstPartRevByDateDescending_output{
   returnObj:Erp_Tablesets_PartRevListTableset[],
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
   returnObj:Erp_Tablesets_PartRevListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param partNum
      @param revisionNum
      @param altMethod
   */  
export interface GetNewPartRev_input{
   ds:Erp_Tablesets_PartRevSearchTableset[],
   partNum:string,
   revisionNum:string,
   altMethod:string,
}

export interface GetNewPartRev_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartRevSearchTableset,
}
}

   /** Required : 
      @param WhereClause
      @param PartWhereClause
      @param PageSize
      @param AbsolutePage
   */  
export interface GetPartRevListByConfigID_input{
   WhereClause:string,
   PartWhereClause:string,
   PageSize:number,
   AbsolutePage:number,
}

export interface GetPartRevListByConfigID_output{
   returnObj:Erp_Tablesets_PartRevListTableset[],
parameters : {
      /**  output parameters  */  
   MorePages:boolean,
}
}

   /** Required : 
      @param whereClausePartRev
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePartRev:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PartRevSearchTableset[],
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
      @param partNum
   */  
export interface PartRevionsExists_input{
   partNum:string,
}

export interface PartRevionsExists_output{
   returnObj:boolean,
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPartRevSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPartRevSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PartRevSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartRevSearchTableset,
}
}

