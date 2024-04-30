import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ACTTypeRevisionSvc
// Description: ACTType Revision business object.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/$metadata", {
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
   Description: Get ACTTypeRevisions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ACTTypeRevisions
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ACTTypeRevisionRow
   */  
export function get_ACTTypeRevisions(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTTypeRevisionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/ACTTypeRevisions", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTTypeRevisionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ACTTypeRevisions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ACTTypeRevisionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ACTTypeRevisionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ACTTypeRevisions(requestBody:Erp_Tablesets_ACTTypeRevisionRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/ACTTypeRevisions", {
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
   Summary: Calls GetByID to retrieve the ACTTypeRevision item
   Description: Calls GetByID to retrieve the ACTTypeRevision item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ACTTypeRevision
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ACTTypeRevisionRow
   */  
export function get_ACTTypeRevisions_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ACTTypeRevisionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/ACTTypeRevisions(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_ACTTypeRevisionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ACTTypeRevision for the service
   Description: Calls UpdateExt to update ACTTypeRevision. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ACTTypeRevision
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ACTTypeRevisionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ACTTypeRevisions_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_ACTTypeRevisionRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/ACTTypeRevisions(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete ACTTypeRevision item
   Description: Call UpdateExt to delete ACTTypeRevision item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ACTTypeRevision
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ACTTypeRevisions_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/ACTTypeRevisions(" + SysRowID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ACTTypeRevisionListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTTypeRevisionListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTTypeRevisionListRow)
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
export function get_GetRows(whereClauseACTTypeRevision:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseACTTypeRevision!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseACTTypeRevision=" + whereClauseACTTypeRevision
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/GetRows" + params, {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(sysRowID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof sysRowID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "sysRowID=" + sysRowID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/GetList" + params, {
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
   Summary: Invoke method GetListOfRevisions
   Description: Gets List of revisions available for Export/Delete.
   OperationID: GetListOfRevisions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListOfRevisions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfRevisions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListOfRevisions(requestBody:GetListOfRevisions_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListOfRevisions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/GetListOfRevisions", {
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
         resolve(data as GetListOfRevisions_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRevisionsDataInStringFormat
   Description: Get set of parameters lists in string format.
   OperationID: GetRevisionsDataInStringFormat
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRevisionsDataInStringFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRevisionsDataInStringFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRevisionsDataInStringFormat(requestBody:GetRevisionsDataInStringFormat_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRevisionsDataInStringFormat_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/GetRevisionsDataInStringFormat", {
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
         resolve(data as GetRevisionsDataInStringFormat_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FillRevisionsTableForImport
   Description: Get the list of revisions for import (system revisions).
   OperationID: FillRevisionsTableForImport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FillRevisionsTableForImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FillRevisionsTableForImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FillRevisionsTableForImport(requestBody:FillRevisionsTableForImport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FillRevisionsTableForImport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/FillRevisionsTableForImport", {
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
         resolve(data as FillRevisionsTableForImport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FillTempTableForImportFromFile
   Description: Returns dataset with the list of revisions loaded form file.
   OperationID: FillTempTableForImportFromFile
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FillTempTableForImportFromFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FillTempTableForImportFromFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FillTempTableForImportFromFile(requestBody:FillTempTableForImportFromFile_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FillTempTableForImportFromFile_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/FillTempTableForImportFromFile", {
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
         resolve(data as FillTempTableForImportFromFile_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRevisionsStatus
   Description: Change status for all revisions.
   OperationID: ChangeRevisionsStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRevisionsStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRevisionsStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRevisionsStatus(requestBody:ChangeRevisionsStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRevisionsStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/ChangeRevisionsStatus", {
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
         resolve(data as ChangeRevisionsStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadBookMap
   Description: Get Book/Segment mapping data.
   OperationID: LoadBookMap
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadBookMap_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadBookMap_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadBookMap(requestBody:LoadBookMap_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadBookMap_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/LoadBookMap", {
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
         resolve(data as LoadBookMap_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateBookMappingInfo
   Description: Update Book Mapping Data.
   OperationID: UpdateBookMappingInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateBookMappingInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateBookMappingInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateBookMappingInfo(requestBody:UpdateBookMappingInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateBookMappingInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/UpdateBookMappingInfo", {
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
         resolve(data as UpdateBookMappingInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckBooksExistsRevisionUsedBothBooks
   Description: Check that books exist.
   OperationID: CheckBooksExistsRevisionUsedBothBooks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckBooksExistsRevisionUsedBothBooks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBooksExistsRevisionUsedBothBooks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckBooksExistsRevisionUsedBothBooks(requestBody:CheckBooksExistsRevisionUsedBothBooks_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckBooksExistsRevisionUsedBothBooks_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/CheckBooksExistsRevisionUsedBothBooks", {
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
         resolve(data as CheckBooksExistsRevisionUsedBothBooks_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckSourceBooksExistsRevisionUsedBothBooks
   Description: Check Source Books Exists.
   OperationID: CheckSourceBooksExistsRevisionUsedBothBooks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckSourceBooksExistsRevisionUsedBothBooks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSourceBooksExistsRevisionUsedBothBooks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckSourceBooksExistsRevisionUsedBothBooks(requestBody:CheckSourceBooksExistsRevisionUsedBothBooks_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckSourceBooksExistsRevisionUsedBothBooks_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/CheckSourceBooksExistsRevisionUsedBothBooks", {
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
         resolve(data as CheckSourceBooksExistsRevisionUsedBothBooks_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateMapBookForAll
   Description: Update Mapping Book ds on ColumnChanged event for Map Book.
   OperationID: UpdateMapBookForAll
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateMapBookForAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateMapBookForAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateMapBookForAll(requestBody:UpdateMapBookForAll_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateMapBookForAll_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/UpdateMapBookForAll", {
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
         resolve(data as UpdateMapBookForAll_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckNoBookingRule
   Description: Check there is no booking rules for the mapped book.
   OperationID: CheckNoBookingRule
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckNoBookingRule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckNoBookingRule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckNoBookingRule(requestBody:CheckNoBookingRule_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckNoBookingRule_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/CheckNoBookingRule", {
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
         resolve(data as CheckNoBookingRule_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsValidBookMapping
   Description: Checks that Book Mapping is valid.
   OperationID: IsValidBookMapping
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsValidBookMapping_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsValidBookMapping_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsValidBookMapping(requestBody:IsValidBookMapping_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsValidBookMapping_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/IsValidBookMapping", {
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
         resolve(data as IsValidBookMapping_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method createAdditionalBooksForAll
   Description: Create additional books for all mapped books.
   OperationID: createAdditionalBooksForAll
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/createAdditionalBooksForAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/createAdditionalBooksForAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_createAdditionalBooksForAll(requestBody:createAdditionalBooksForAll_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<createAdditionalBooksForAll_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/createAdditionalBooksForAll", {
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
         resolve(data as createAdditionalBooksForAll_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method btnAddMappedBook_OnClick
   Description: Creates additional Mapped book on btnAddMappedBook click.
   OperationID: btnAddMappedBook_OnClick
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/btnAddMappedBook_OnClick_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/btnAddMappedBook_OnClick_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_btnAddMappedBook_OnClick(requestBody:btnAddMappedBook_OnClick_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<btnAddMappedBook_OnClick_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/btnAddMappedBook_OnClick", {
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
         resolve(data as btnAddMappedBook_OnClick_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMapSegmentsTableFilter
   Description: Get filter for the Map Segments list.
   OperationID: GetMapSegmentsTableFilter
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetMapSegmentsTableFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMapSegmentsTableFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMapSegmentsTableFilter(requestBody:GetMapSegmentsTableFilter_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetMapSegmentsTableFilter_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/GetMapSegmentsTableFilter", {
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
         resolve(data as GetMapSegmentsTableFilter_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ClearBooksForAllTypes
   Description: Clear books data for all types.
   OperationID: ClearBooksForAllTypes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ClearBooksForAllTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearBooksForAllTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClearBooksForAllTypes(requestBody:ClearBooksForAllTypes_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ClearBooksForAllTypes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/ClearBooksForAllTypes", {
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
         resolve(data as ClearBooksForAllTypes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetMapSegments
   Description: Upadate Table with Map Segments on the Book Mapping panel after Target Book changes in table of mapping books.
   OperationID: SetMapSegments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetMapSegments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetMapSegments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetMapSegments(requestBody:SetMapSegments_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetMapSegments_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/SetMapSegments", {
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
         resolve(data as SetMapSegments_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckImportedBookPackages
   Description: Check imported book packages.
   OperationID: CheckImportedBookPackages
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckImportedBookPackages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckImportedBookPackages_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckImportedBookPackages(requestBody:CheckImportedBookPackages_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckImportedBookPackages_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/CheckImportedBookPackages", {
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
         resolve(data as CheckImportedBookPackages_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SinchronizeDataAfterABTVerValidation
   Description: Include changes after ABTVer Validation.
   OperationID: SinchronizeDataAfterABTVerValidation
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SinchronizeDataAfterABTVerValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SinchronizeDataAfterABTVerValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SinchronizeDataAfterABTVerValidation(requestBody:SinchronizeDataAfterABTVerValidation_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SinchronizeDataAfterABTVerValidation_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/SinchronizeDataAfterABTVerValidation", {
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
         resolve(data as SinchronizeDataAfterABTVerValidation_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTTypeRevisionListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ACTTypeRevisionListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTTypeRevisionRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ACTTypeRevisionRow,
}

export interface Erp_Tablesets_ACTTypeRevisionListRow{
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates that record is selected.  */  
   "Selected":boolean,
      /**  A user-defined code of revision (unique within one account transaction type).  */  
   "RevisionCode":string,
      /**   Status of the Revision. Allowed values are: "Active", "Draft", "Blocked". 
Active - indicates that exactly this Revision of an GL Transaction Type will be used when functional module initiates a corresponding business event. As soon as a Revision becomes "Active", it should become read-only for user. Only one Revision for each GL Transaction Type may be "Active".
 
Draft -  indicates a newly created Revision, which will not be used in any run-time processing. Each newly created Revision should automatically be put into "Draft" status. "Draft" Revision is open for editing. Each GL Transaction Type may have any number of Draft Revisions.
Blocked - indicates a Revision which was previously "Active" but is not anymore and is stored for traceability purposes. The "Blocked" Revision should be read-only.  */  
   "RevisionStatus":string,
      /**  Standard or Exteded  */  
   "RType":string,
   "SegmentsForMap":string,
   "ACTTypeName":string,
      /**  Reference to the GL Transaction Type.  */  
   "ACTTypeUID":number,
      /**  Indicates if current revision is selected to be deleted or not.  */  
   "DelRev":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ACTTypeRevisionRow{
      /**  Version of VBD Stucture. If version is changed , VBD Structure merge process will be started during conversion.  */  
   "ABTVer":string,
   "Activate":boolean,
   "ACTTypeName":string,
      /**  Reference to the GL Transaction Type.  */  
   "ACTTypeUID":number,
   "BooksForMap":string,
      /**  Indicates if current revision is selected to be deleted or not.  */  
   "DelRev":boolean,
   "FileName":string,
      /**  Import ABT.  */  
   "ImportABT":boolean,
   "ImportBR":boolean,
      /**  New Revision Code.  */  
   "NewCode":string,
   "PackageList":string,
      /**  Patch VBD Version  */  
   "PatchABTVer":string,
   "ReplaceExisting":boolean,
      /**  A user-defined code of revision (unique within one account transaction type).  */  
   "RevisionCode":string,
      /**   Status of the Revision. Allowed values are: "Active", "Draft", "Blocked". 
Active - indicates that exactly this Revision of an GL Transaction Type will be used when functional module initiates a corresponding business event. As soon as a Revision becomes "Active", it should become read-only for user. Only one Revision for each GL Transaction Type may be "Active".
 
Draft -  indicates a newly created Revision, which will not be used in any run-time processing. Each newly created Revision should automatically be put into "Draft" status. "Draft" Revision is open for editing. Each GL Transaction Type may have any number of Draft Revisions.
Blocked - indicates a Revision which was previously "Active" but is not anymore and is stored for traceability purposes. The "Blocked" Revision should be read-only.  */  
   "RevisionStatus":string,
      /**  Standard or Exteded  */  
   "RType":string,
   "SegmentsForMap":string,
      /**  Indicates that record is selected.  */  
   "Selected":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates Update mode.  */  
   "UseUpdateMode":boolean,
   "XMLData":string,
   "ChangeStatusSelected":boolean,
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
      @param selectionMode
      @param status
      @param newRevName
      @param ds
   */  
export interface ChangeRevisionsStatus_input{
   selectionMode:string,
   status:boolean,
   newRevName:string,
   ds:Erp_Tablesets_ACTTypeRevisionTableset[],
}

export interface ChangeRevisionsStatus_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeRevisionTableset,
}
}

   /** Required : 
      @param mapBook
      @param company
      @param importBook
      @param package
      @param rowIdent
      @param ds
   */  
export interface CheckBooksExistsRevisionUsedBothBooks_input{
   mapBook:string,
   company:string,
   importBook:string,
   package:string,
   rowIdent:string,
   ds:Erp_Tablesets_BookMappingTableset[],
}

export interface CheckBooksExistsRevisionUsedBothBooks_output{
parameters : {
      /**  output parameters  */  
   errorMessage:string,
   ds:Erp_Tablesets_BookMappingTableset,
}
}

   /** Required : 
      @param CurrentCompany
      @param CompaniesList
      @param xml_ACTTypeRevision
      @param xml_MappingInfo
   */  
export interface CheckImportedBookPackages_input{
   CurrentCompany:string,
   CompaniesList:string,
   xml_ACTTypeRevision:string,
   xml_MappingInfo:string,
}

export interface CheckImportedBookPackages_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   warnMess:string,
}
}

   /** Required : 
      @param chkAllTypes
      @param currentBookID
      @param ds
   */  
export interface CheckNoBookingRule_input{
   chkAllTypes:boolean,
   currentBookID:string,
   ds:Erp_Tablesets_BookMappingTableset[],
}

export interface CheckNoBookingRule_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BookMappingTableset,
}
}

   /** Required : 
      @param company
      @param importBook
      @param package
      @param rowIdent
      @param ds
   */  
export interface CheckSourceBooksExistsRevisionUsedBothBooks_input{
   company:string,
   importBook:string,
   package:string,
   rowIdent:string,
   ds:Erp_Tablesets_BookMappingTableset[],
}

export interface CheckSourceBooksExistsRevisionUsedBothBooks_output{
parameters : {
      /**  output parameters  */  
   errorMessage:string,
   ds:Erp_Tablesets_BookMappingTableset,
}
}

   /** Required : 
      @param chkAllTypes
      @param CompaniesList
      @param ds
   */  
export interface ClearBooksForAllTypes_input{
   chkAllTypes:boolean,
   CompaniesList:string,
   ds:Erp_Tablesets_BookMappingTableset[],
}

export interface ClearBooksForAllTypes_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BookMappingTableset,
}
}

export interface Erp_Tablesets_ACTTypeRevisionListRow{
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates that record is selected.  */  
   Selected:boolean,
      /**  A user-defined code of revision (unique within one account transaction type).  */  
   RevisionCode:string,
      /**   Status of the Revision. Allowed values are: "Active", "Draft", "Blocked". 
Active - indicates that exactly this Revision of an GL Transaction Type will be used when functional module initiates a corresponding business event. As soon as a Revision becomes "Active", it should become read-only for user. Only one Revision for each GL Transaction Type may be "Active".
 
Draft -  indicates a newly created Revision, which will not be used in any run-time processing. Each newly created Revision should automatically be put into "Draft" status. "Draft" Revision is open for editing. Each GL Transaction Type may have any number of Draft Revisions.
Blocked - indicates a Revision which was previously "Active" but is not anymore and is stored for traceability purposes. The "Blocked" Revision should be read-only.  */  
   RevisionStatus:string,
      /**  Standard or Exteded  */  
   RType:string,
   SegmentsForMap:string,
   ACTTypeName:string,
      /**  Reference to the GL Transaction Type.  */  
   ACTTypeUID:number,
      /**  Indicates if current revision is selected to be deleted or not.  */  
   DelRev:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ACTTypeRevisionListTableset{
   ACTTypeRevisionList:Erp_Tablesets_ACTTypeRevisionListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ACTTypeRevisionRow{
      /**  Version of VBD Stucture. If version is changed , VBD Structure merge process will be started during conversion.  */  
   ABTVer:string,
   Activate:boolean,
   ACTTypeName:string,
      /**  Reference to the GL Transaction Type.  */  
   ACTTypeUID:number,
   BooksForMap:string,
      /**  Indicates if current revision is selected to be deleted or not.  */  
   DelRev:boolean,
   FileName:string,
      /**  Import ABT.  */  
   ImportABT:boolean,
   ImportBR:boolean,
      /**  New Revision Code.  */  
   NewCode:string,
   PackageList:string,
      /**  Patch VBD Version  */  
   PatchABTVer:string,
   ReplaceExisting:boolean,
      /**  A user-defined code of revision (unique within one account transaction type).  */  
   RevisionCode:string,
      /**   Status of the Revision. Allowed values are: "Active", "Draft", "Blocked". 
Active - indicates that exactly this Revision of an GL Transaction Type will be used when functional module initiates a corresponding business event. As soon as a Revision becomes "Active", it should become read-only for user. Only one Revision for each GL Transaction Type may be "Active".
 
Draft -  indicates a newly created Revision, which will not be used in any run-time processing. Each newly created Revision should automatically be put into "Draft" status. "Draft" Revision is open for editing. Each GL Transaction Type may have any number of Draft Revisions.
Blocked - indicates a Revision which was previously "Active" but is not anymore and is stored for traceability purposes. The "Blocked" Revision should be read-only.  */  
   RevisionStatus:string,
      /**  Standard or Exteded  */  
   RType:string,
   SegmentsForMap:string,
      /**  Indicates that record is selected.  */  
   Selected:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates Update mode.  */  
   UseUpdateMode:boolean,
   XMLData:string,
   ChangeStatusSelected:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ACTTypeRevisionTableset{
   ACTTypeRevision:Erp_Tablesets_ACTTypeRevisionRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_BookMappingRow{
      /**  Version of VBD Stucture. If version is changed , VBD Structure merge process will be started during conversion.  */  
   ABTVer:string,
   ACTTypeName:string,
   AdditionalMapBook:boolean,
      /**  Company.  */  
   Company:string,
   FilterColumn:string,
   ForAllTypes:string,
   FromXML:boolean,
      /**  flag if has empty Data.  */  
   HasEmptyData:boolean,
      /**  Import Book ID.  */  
   ImportBook:string,
   MapBook:string,
   MappedFrom:string,
   Package:string,
      /**  Patch VBD Version  */  
   PatchABTVer:string,
   PatchRulesetVer:string,
      /**  Revision Name.  */  
   RevisionName:string,
   RulesetVer:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BookMappingTableset{
   BookMapping:Erp_Tablesets_BookMappingRow[],
   MapComp:Erp_Tablesets_MapCompRow[],
   MapRevision:Erp_Tablesets_MapRevisionRow[],
   SegmentMapping:Erp_Tablesets_SegmentMappingRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MapCompRow{
      /**  Company.  */  
   Company:string,
   FilterColumn:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MapRevisionRow{
   ACTTypeName:string,
      /**  Company.  */  
   Company:string,
   Description:string,
   FilterColumn:string,
   HasEmptyData:boolean,
      /**  Revision Name.  */  
   RevisionName:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SegmentMappingRow{
   ACTTypeName:string,
   AdditionalMapBook:boolean,
      /**  Company.  */  
   Company:string,
   DispMapSegmentNum:number,
   FilterColumn:string,
   ForAllTypes:string,
      /**  Import Book ID.  */  
   ImportBook:string,
      /**  Name of source segment.  */  
   ImportSegmentName:string,
      /**  Number of source segment.  */  
   ImportSegmentNum:number,
   MapBook:string,
      /**  Name of target segment.  */  
   MapSegmentName:string,
      /**  Number of target segment.  */  
   MapSegmentNum:number,
      /**  Package ID.  */  
   Package:string,
      /**  Revision Name.  */  
   RevisionName:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtACTTypeRevisionTableset{
   ACTTypeRevision:Erp_Tablesets_ACTTypeRevisionRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param package
      @param glTranType
      @param import
      @param inUpdateMode
      @param replaceExisting
      @param activate
      @param newName
      @param ds
   */  
export interface FillRevisionsTableForImport_input{
   package:string,
   glTranType:string,
   import_:boolean,
   inUpdateMode:boolean,
   replaceExisting:boolean,
   activate:boolean,
   newName:string,
   ds:Erp_Tablesets_ACTTypeRevisionTableset[],
}

export interface FillRevisionsTableForImport_output{
parameters : {
      /**  output parameters  */  
   opwarningAboutSkippedRevisions:string,
   ds:Erp_Tablesets_ACTTypeRevisionTableset,
}
}

   /** Required : 
      @param fileName
      @param import
      @param inUpdateMode
      @param replaceExisting
      @param activate
      @param newName
      @param ds
   */  
export interface FillTempTableForImportFromFile_input{
   fileName:string,
   import_:boolean,
   inUpdateMode:boolean,
   replaceExisting:boolean,
   activate:boolean,
   newName:string,
   ds:Erp_Tablesets_ACTTypeRevisionTableset[],
}

export interface FillTempTableForImportFromFile_output{
parameters : {
      /**  output parameters  */  
   opwarningAboutSkippedRevisions:string,
   ds:Erp_Tablesets_ACTTypeRevisionTableset,
}
}

   /** Required : 
      @param sysRowID
   */  
export interface GetByID_input{
   sysRowID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ACTTypeRevisionTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ACTTypeRevisionTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ACTTypeRevisionTableset[],
}

   /** Required : 
      @param ipDelRev
      @param ds
   */  
export interface GetListOfRevisions_input{
   ipDelRev:boolean,
   ds:Erp_Tablesets_ACTTypeRevisionTableset[],
}

export interface GetListOfRevisions_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeRevisionTableset,
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
   returnObj:Erp_Tablesets_ACTTypeRevisionListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param chkAllTypes
      @param ACTTypeName
      @param RevisionName
      @param Package
      @param Company
      @param ImportBook
      @param MapBook
   */  
export interface GetMapSegmentsTableFilter_input{
   chkAllTypes:boolean,
   ACTTypeName:string,
   RevisionName:string,
   Package:string,
   Company:string,
   ImportBook:string,
   MapBook:string,
}

export interface GetMapSegmentsTableFilter_output{
parameters : {
      /**  output parameters  */  
   newfilter:string,
}
}

   /** Required : 
      @param ds
   */  
export interface GetRevisionsDataInStringFormat_input{
   ds:Erp_Tablesets_ACTTypeRevisionTableset[],
}

export interface GetRevisionsDataInStringFormat_output{
parameters : {
      /**  output parameters  */  
   opListOfACTTypeNames:string,
   opListOfACTTypeUIDs:string,
   opListOfFileNames:string,
   opListOfNewCodes:string,
   opListOfRevisionCodes:string,
   opListSelectedToDelete:string,
   opListSelectedToExport:string,
   ds:Erp_Tablesets_ACTTypeRevisionTableset,
}
}

   /** Required : 
      @param whereClauseACTTypeRevision
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseACTTypeRevision:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ACTTypeRevisionTableset[],
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
      @param chkAllTypes
      @param ds
   */  
export interface IsValidBookMapping_input{
   chkAllTypes:boolean,
   ds:Erp_Tablesets_BookMappingTableset[],
}

export interface IsValidBookMapping_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   errMessage:string,
   ds:Erp_Tablesets_BookMappingTableset,
}
}

   /** Required : 
      @param manualSelectionBooks
      @param CompaniesList
      @param ds
      @param bm_ds
   */  
export interface LoadBookMap_input{
   manualSelectionBooks:boolean,
   CompaniesList:string,
   ds:Erp_Tablesets_ACTTypeRevisionTableset[],
   bm_ds:Erp_Tablesets_BookMappingTableset[],
}

export interface LoadBookMap_output{
parameters : {
      /**  output parameters  */  
   xmlACTTypeRevisionsInfo:string,
   xmlMappingInfo:string,
   ds:Erp_Tablesets_ACTTypeRevisionTableset,
   bm_ds:Erp_Tablesets_BookMappingTableset,
}
}

   /** Required : 
      @param chkAllTypes
      @param bookSysRowID
      @param company
      @param bookID
      @param coaCode
      @param CompaniesList
      @param existsEmptyData
      @param ds
   */  
export interface SetMapSegments_input{
   chkAllTypes:boolean,
   bookSysRowID:string,
   company:string,
   bookID:string,
   coaCode:string,
   CompaniesList:string,
   existsEmptyData:boolean,
   ds:Erp_Tablesets_BookMappingTableset[],
}

export interface SetMapSegments_output{
parameters : {
      /**  output parameters  */  
   existsEmptyData:boolean,
   ds:Erp_Tablesets_BookMappingTableset,
}
}

   /** Required : 
      @param xml_ACTTypeRevision
      @param ds
   */  
export interface SinchronizeDataAfterABTVerValidation_input{
   xml_ACTTypeRevision:string,
   ds:Erp_Tablesets_ACTTypeRevisionTableset[],
}

export interface SinchronizeDataAfterABTVerValidation_output{
parameters : {
      /**  output parameters  */  
   xml_ACTTypeRevision:string,
   isAnyRevsToImport:boolean,
   ds:Erp_Tablesets_ACTTypeRevisionTableset,
}
}

   /** Required : 
      @param xmlMappingInfo
      @param ds
      @param bm_ds
   */  
export interface UpdateBookMappingInfo_input{
   xmlMappingInfo:string,
   ds:Erp_Tablesets_ACTTypeRevisionTableset[],
   bm_ds:Erp_Tablesets_BookMappingTableset[],
}

export interface UpdateBookMappingInfo_output{
parameters : {
      /**  output parameters  */  
   xmlMappingInfoUpdated:string,
   ds:Erp_Tablesets_ACTTypeRevisionTableset,
   bm_ds:Erp_Tablesets_BookMappingTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtACTTypeRevisionTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtACTTypeRevisionTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param company
      @param prevMapBook
      @param importBook
      @param newMapBookID
      @param package
      @param ds
   */  
export interface UpdateMapBookForAll_input{
   company:string,
   prevMapBook:string,
   importBook:string,
   newMapBookID:string,
   package:string,
   ds:Erp_Tablesets_BookMappingTableset[],
}

export interface UpdateMapBookForAll_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BookMappingTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ACTTypeRevisionTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ACTTypeRevisionTableset,
}
}

   /** Required : 
      @param curBookID
      @param chkAllTypes
      @param ManualSelectionBooks
      @param ds
   */  
export interface btnAddMappedBook_OnClick_input{
   curBookID:string,
   chkAllTypes:boolean,
   ManualSelectionBooks:boolean,
   ds:Erp_Tablesets_BookMappingTableset[],
}

export interface btnAddMappedBook_OnClick_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BookMappingTableset,
}
}

   /** Required : 
      @param ManualSelectionBooks
      @param ds
   */  
export interface createAdditionalBooksForAll_input{
   ManualSelectionBooks:boolean,
   ds:Erp_Tablesets_BookMappingTableset[],
}

export interface createAdditionalBooksForAll_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BookMappingTableset,
}
}

