import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.POSuggChgSvc
// Description: Purchase Order Changes
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/$metadata", {
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
   Description: Get POSuggChgs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_POSuggChgs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SugPOChgRow
   */  
export function get_POSuggChgs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SugPOChgRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/POSuggChgs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SugPOChgRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_POSuggChgs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SugPOChgRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.SugPOChgRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POSuggChgs(requestBody:Erp_Tablesets_SugPOChgRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/POSuggChgs", {
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
   Summary: Calls GetByID to retrieve the POSuggChg item
   Description: Calls GetByID to retrieve the POSuggChg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POSuggChg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param VendorChange Desc: VendorChange   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.SugPOChgRow
   */  
export function get_POSuggChgs_Company_PONum_POLine_PORelNum_VendorChange(Company:string, PONum:string, POLine:string, PORelNum:string, VendorChange:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SugPOChgRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/POSuggChgs(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + VendorChange + ")", {
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
         resolve(data as Erp_Tablesets_SugPOChgRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update POSuggChg for the service
   Description: Calls UpdateExt to update POSuggChg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_POSuggChg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param VendorChange Desc: VendorChange   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.SugPOChgRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_POSuggChgs_Company_PONum_POLine_PORelNum_VendorChange(Company:string, PONum:string, POLine:string, PORelNum:string, VendorChange:string, requestBody:Erp_Tablesets_SugPOChgRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/POSuggChgs(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + VendorChange + ")", {
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
   Summary: Call UpdateExt to delete POSuggChg item
   Description: Call UpdateExt to delete POSuggChg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_POSuggChg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param VendorChange Desc: VendorChange   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_POSuggChgs_Company_PONum_POLine_PORelNum_VendorChange(Company:string, PONum:string, POLine:string, PORelNum:string, VendorChange:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/POSuggChgs(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + VendorChange + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SugPOChgListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SugPOChgListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SugPOChgListRow)
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
export function get_GetRows(whereClauseSugPOChg:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseSugPOChg!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSugPOChg=" + whereClauseSugPOChg
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/GetRows" + params, {
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(poNum:string, poLine:string, poRelNum:string, vendorChange:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof poNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "poNum=" + poNum
   }
   if(typeof poLine!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "poLine=" + poLine
   }
   if(typeof poRelNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "poRelNum=" + poRelNum
   }
   if(typeof vendorChange!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "vendorChange=" + vendorChange
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/GetList" + params, {
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
   Summary: Invoke method MassAcceptSuggestionChanges
   Description: This methods will accept multiple PO Suggestion changes.
   OperationID: MassAcceptSuggestionChanges
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MassAcceptSuggestionChanges_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassAcceptSuggestionChanges_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MassAcceptSuggestionChanges(requestBody:MassAcceptSuggestionChanges_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MassAcceptSuggestionChanges_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/MassAcceptSuggestionChanges", {
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
         resolve(data as MassAcceptSuggestionChanges_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AcceptSuggestionChange
   Description: This methods will accept the PO Suggestion change.
   OperationID: AcceptSuggestionChange
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AcceptSuggestionChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AcceptSuggestionChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AcceptSuggestionChange(requestBody:AcceptSuggestionChange_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AcceptSuggestionChange_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/AcceptSuggestionChange", {
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
         resolve(data as AcceptSuggestionChange_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckTracker
   Description: This method does stuff .
   OperationID: CheckTracker
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckTracker(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckTracker_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/CheckTracker", {
          method: 'post',
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
         resolve(data as CheckTracker_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSugPOChgCount
   Description: This methods will return a count of Change PO Suggestions for the selected Buyer
   OperationID: GetSugPOChgCount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSugPOChgCount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSugPOChgCount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSugPOChgCount(requestBody:GetSugPOChgCount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSugPOChgCount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/GetSugPOChgCount", {
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
         resolve(data as GetSugPOChgCount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListPlant
   Description: Returns a list of rows that satisfy the where clause. Use in place of GetList
   OperationID: GetListPlant
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListPlant(requestBody:GetListPlant_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListPlant_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/GetListPlant", {
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
         resolve(data as GetListPlant_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsPlantByPart
   Description: Returns a dataset containing all rows that satisfy the where clauses. Whereclauses are split in case to sort by PartNum
   OperationID: GetRowsPlantByPart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsPlantByPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsPlantByPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsPlantByPart(requestBody:GetRowsPlantByPart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsPlantByPart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/GetRowsPlantByPart", {
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
         resolve(data as GetRowsPlantByPart_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsPlant
   Description: Returns a dataset containing all rows that satisfy the where clauses. use in place of GetRows
   OperationID: GetRowsPlant
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsPlant(requestBody:GetRowsPlant_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsPlant_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/GetRowsPlant", {
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
         resolve(data as GetRowsPlant_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewSugPOChg
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSugPOChg
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewSugPOChg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSugPOChg_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSugPOChg(requestBody:GetNewSugPOChg_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewSugPOChg_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/GetNewSugPOChg", {
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
         resolve(data as GetNewSugPOChg_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SugPOChgListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SugPOChgListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SugPOChgRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SugPOChgRow,
}

export interface Erp_Tablesets_SugPOChgListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Purchase order that this release record is related to.  */  
   "PONum":number,
      /**  The line # of  PoDetail record that the PORel record is related to.  */  
   "POLine":number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   "PORelNum":number,
      /**   Suggested action to be taken for this Purchase Order release.
"X" = Expedite, "P" = Postpone,  "C" = Cancel, "I"= increase qty, "R" = Reduce Qty, "S" for below safety and "Z" for below zero. This field is a 8 char. field it could contain "IP" increase and postpone.  */  
   "SuggestionCode":string,
      /**   The Buyer Id that is on the related PO.
Duplicate of POHeader.BuyerID  */  
   "BuyerID":string,
      /**  Requirement Due Date.  For suggested Cancels or Reduce Quantity this is set to Today.  */  
   "RequireDate":string,
      /**  Human formatted string that contains the original source document of this entry.  */  
   "SourceName":string,
      /**  New Suggested qty (in our UOM). This is the true amount suggested, not the difference between actual and suggested.  This only pertains to increase and reduce qty suggestions.  */  
   "SurplusQty":number,
      /**   Reason for "Cancel" suggestion.  Purchase for stock which
1. OverMax - Stock purchase which surpasses the maximum.
2. No Requirement - Job purchase no open job record.  */  
   "CancelReason":string,
      /**  Site Identifier. This field can not be blank.  */  
   "Plant":string,
      /**  Supplier contact linked to this record.  */  
   "ConNum":number,
      /**  Comment  */  
   "Comment":string,
      /**  Indicates that this suggestion was initiated from the supplier Wb.  It is a reference field on time phase and does not add or subtract from the balance.  */  
   "VendorChange":boolean,
      /**  Linked Inter-Company sales order.  */  
   "OrderNum":number,
      /**  Linked Inter-Company Sales order Line number that this order release is linked to.  */  
   "OrderLine":number,
      /**  The linked Inter-Company sale order release.  */  
   "OrderRelNum":number,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  ABC Code.  Valid values are "A" through "Z".  */  
   "ABCCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "brwPartNum":string,
   "Brw_Exception":string,
   "brwVendorID":string,
   "brwPurPoint":string,
   "Rels_OnOrderQty":number,
   "IUM":string,
   "DueDate":string,
   "JobSeqType":string,
   "CancelToggle":boolean,
   "ExpediteToggle":boolean,
   "IncreaseToggle":boolean,
   "PostponeToggle":boolean,
   "ReduceToggle":boolean,
   "VendorName":string,
   "BrwPartDesc":string,
      /**  Logical indicating whether or not the suggested update is valid for PO releases tied to a Container.  */  
   "ContainerAllowAccept":boolean,
   "SupplierQty":number,
   "PUM":string,
      /**  UOM for SurplusQty  */  
   "SurplusQtyUOM":string,
      /**  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  */  
   "BuyerIDName":string,
      /**  OUR internal Part number for this item.  */  
   "POLinePartNum":string,
      /**  Supplier Part Number  */  
   "POLineVenPartNum":string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   "POLineLineDesc":string,
      /**  The Short Description of the Attribute Set.  */  
   "brwAttributeSetShortDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SugPOChgRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Purchase order that this release record is related to.  */  
   "PONum":number,
      /**  The line # of  PoDetail record that the PORel record is related to.  */  
   "POLine":number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   "PORelNum":number,
      /**   Suggested action to be taken for this Purchase Order release.
"X" = Expedite, "P" = Postpone,  "C" = Cancel, "I"= increase qty, "R" = Reduce Qty, "S" for below safety and "Z" for below zero. This field is a 8 char. field it could contain "IP" increase and postpone.  */  
   "SuggestionCode":string,
      /**   The Buyer Id that is on the related PO.
Duplicate of POHeader.BuyerID  */  
   "BuyerID":string,
      /**  Requirement Due Date.  For suggested Cancels or Reduce Quantity this is set to Today.  */  
   "RequireDate":string,
      /**  Human formatted string that contains the original source document of this entry.  */  
   "SourceName":string,
      /**  New Suggested qty (in our UOM). This is the true amount suggested, not the difference between actual and suggested.  This only pertains to increase and reduce qty suggestions.  */  
   "SurplusQty":number,
      /**   Reason for "Cancel" suggestion.  Purchase for stock which
1. OverMax - Stock purchase which surpasses the maximum.
2. No Requirement - Job purchase no open job record.  */  
   "CancelReason":string,
      /**  Site Identifier. This field can not be blank.  */  
   "Plant":string,
      /**  Supplier contact linked to this record.  */  
   "ConNum":number,
      /**  Comment  */  
   "Comment":string,
      /**  Indicates that this suggestion was initiated from the supplier Wb.  It is a reference field on time phase and does not add or subtract from the balance.  */  
   "VendorChange":boolean,
      /**  Linked Inter-Company sales order.  */  
   "OrderNum":number,
      /**  Linked Inter-Company Sales order Line number that this order release is linked to.  */  
   "OrderLine":number,
      /**  The linked Inter-Company sale order release.  */  
   "OrderRelNum":number,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  ABC Code.  Valid values are "A" through "Z".  */  
   "ABCCode":string,
      /**  SuggestionStatus  */  
   "SuggestionStatus":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  A flag that is set by the user to indicate the suggestion has been reviewed.  This is only used to help filter suggestions.  */  
   "Review":boolean,
      /**  For suggested changes to Promise Date.  */  
   "ReqPromiseDate":string,
      /**  Date and time when this record was created.  */  
   "CreatedOn":string,
      /**  LockDate  */  
   "LockDate":boolean,
      /**  LockQty  */  
   "LockQty":boolean,
      /**  PO Release Arrived Qty (note cannot be a linked field as need to set UOM Properties)  */  
   "ArrivedQty":number,
   "Brw_Exception":string,
   "brwPartNum":string,
   "brwPurPoint":string,
   "brwVendorID":string,
   "CancelToggle":boolean,
      /**  Logical indicating whether or not the suggested update is valid for PO releases tied to a Container.  */  
   "ContainerAllowAccept":boolean,
   "DueDate":string,
   "ExpediteToggle":boolean,
   "IncreaseToggle":boolean,
   "IUM":string,
   "JobSeqType":string,
   "PostponeToggle":boolean,
   "PUM":string,
   "ReduceToggle":boolean,
   "Rels_OnOrderQty":number,
   "SupplierQty":number,
      /**  UOM for SurplusQty  */  
   "SurplusQtyUOM":string,
   "VendorName":string,
      /**  PO Release 'Our Quantity'  */  
   "XRelQty":number,
   "BrwPartDesc":string,
      /**  The Promise date set on the PO Release  */  
   "PromiseDate":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "brwAttributeSetID":number,
      /**  The Short Description of the Attribute Set.  */  
   "brwAttributeSetShortDescription":string,
      /**  The Full Description of the Attribute Set.  */  
   "brwAttributeSetDescription":string,
      /**  ID of parent Attribute Class  */  
   "brwAttrClassID":string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   "DispNumberOfPieces":number,
   "brwPartTrackInventoryByRevision":boolean,
   "brwRevisionNum":string,
   "PartClassID":string,
   "PartClassDescription":string,
   "Selected":boolean,
   "BitFlag":number,
   "BuyerIDName":string,
   "PlantName":string,
   "POLineVenPartNum":string,
   "POLineLineDesc":string,
   "POLinePartNum":string,
   "POLineRevisionNum":string,
   "PORelContractID":string,
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
      @param ipPONum
      @param ipPOLine
      @param ipPORelNum
      @param ipVendorChange
      @param ds
   */  
export interface AcceptSuggestionChange_input{
      /**  The po number.  */  
   ipPONum:number,
      /**  The po line number.  */  
   ipPOLine:number,
      /**  The po release number.  */  
   ipPORelNum:number,
      /**  The Vendir Change.  */  
   ipVendorChange:boolean,
   ds:Erp_Tablesets_POSuggChgTableset[],
}

export interface AcceptSuggestionChange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggChgTableset,
}
}

export interface CheckTracker_output{
parameters : {
      /**  output parameters  */  
   PartTrackerOK:boolean,
}
}

   /** Required : 
      @param poNum
      @param poLine
      @param poRelNum
      @param vendorChange
   */  
export interface DeleteByID_input{
   poNum:number,
   poLine:number,
   poRelNum:number,
   vendorChange:boolean,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_POSuggChgTableset{
   SugPOChg:Erp_Tablesets_SugPOChgRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SugPOChgListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Purchase order that this release record is related to.  */  
   PONum:number,
      /**  The line # of  PoDetail record that the PORel record is related to.  */  
   POLine:number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   PORelNum:number,
      /**   Suggested action to be taken for this Purchase Order release.
"X" = Expedite, "P" = Postpone,  "C" = Cancel, "I"= increase qty, "R" = Reduce Qty, "S" for below safety and "Z" for below zero. This field is a 8 char. field it could contain "IP" increase and postpone.  */  
   SuggestionCode:string,
      /**   The Buyer Id that is on the related PO.
Duplicate of POHeader.BuyerID  */  
   BuyerID:string,
      /**  Requirement Due Date.  For suggested Cancels or Reduce Quantity this is set to Today.  */  
   RequireDate:string,
      /**  Human formatted string that contains the original source document of this entry.  */  
   SourceName:string,
      /**  New Suggested qty (in our UOM). This is the true amount suggested, not the difference between actual and suggested.  This only pertains to increase and reduce qty suggestions.  */  
   SurplusQty:number,
      /**   Reason for "Cancel" suggestion.  Purchase for stock which
1. OverMax - Stock purchase which surpasses the maximum.
2. No Requirement - Job purchase no open job record.  */  
   CancelReason:string,
      /**  Site Identifier. This field can not be blank.  */  
   Plant:string,
      /**  Supplier contact linked to this record.  */  
   ConNum:number,
      /**  Comment  */  
   Comment:string,
      /**  Indicates that this suggestion was initiated from the supplier Wb.  It is a reference field on time phase and does not add or subtract from the balance.  */  
   VendorChange:boolean,
      /**  Linked Inter-Company sales order.  */  
   OrderNum:number,
      /**  Linked Inter-Company Sales order Line number that this order release is linked to.  */  
   OrderLine:number,
      /**  The linked Inter-Company sale order release.  */  
   OrderRelNum:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  ABC Code.  Valid values are "A" through "Z".  */  
   ABCCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   brwPartNum:string,
   Brw_Exception:string,
   brwVendorID:string,
   brwPurPoint:string,
   Rels_OnOrderQty:number,
   IUM:string,
   DueDate:string,
   JobSeqType:string,
   CancelToggle:boolean,
   ExpediteToggle:boolean,
   IncreaseToggle:boolean,
   PostponeToggle:boolean,
   ReduceToggle:boolean,
   VendorName:string,
   BrwPartDesc:string,
      /**  Logical indicating whether or not the suggested update is valid for PO releases tied to a Container.  */  
   ContainerAllowAccept:boolean,
   SupplierQty:number,
   PUM:string,
      /**  UOM for SurplusQty  */  
   SurplusQtyUOM:string,
      /**  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  */  
   BuyerIDName:string,
      /**  OUR internal Part number for this item.  */  
   POLinePartNum:string,
      /**  Supplier Part Number  */  
   POLineVenPartNum:string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   POLineLineDesc:string,
      /**  The Short Description of the Attribute Set.  */  
   brwAttributeSetShortDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SugPOChgListTableset{
   SugPOChgList:Erp_Tablesets_SugPOChgListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SugPOChgRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Purchase order that this release record is related to.  */  
   PONum:number,
      /**  The line # of  PoDetail record that the PORel record is related to.  */  
   POLine:number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   PORelNum:number,
      /**   Suggested action to be taken for this Purchase Order release.
"X" = Expedite, "P" = Postpone,  "C" = Cancel, "I"= increase qty, "R" = Reduce Qty, "S" for below safety and "Z" for below zero. This field is a 8 char. field it could contain "IP" increase and postpone.  */  
   SuggestionCode:string,
      /**   The Buyer Id that is on the related PO.
Duplicate of POHeader.BuyerID  */  
   BuyerID:string,
      /**  Requirement Due Date.  For suggested Cancels or Reduce Quantity this is set to Today.  */  
   RequireDate:string,
      /**  Human formatted string that contains the original source document of this entry.  */  
   SourceName:string,
      /**  New Suggested qty (in our UOM). This is the true amount suggested, not the difference between actual and suggested.  This only pertains to increase and reduce qty suggestions.  */  
   SurplusQty:number,
      /**   Reason for "Cancel" suggestion.  Purchase for stock which
1. OverMax - Stock purchase which surpasses the maximum.
2. No Requirement - Job purchase no open job record.  */  
   CancelReason:string,
      /**  Site Identifier. This field can not be blank.  */  
   Plant:string,
      /**  Supplier contact linked to this record.  */  
   ConNum:number,
      /**  Comment  */  
   Comment:string,
      /**  Indicates that this suggestion was initiated from the supplier Wb.  It is a reference field on time phase and does not add or subtract from the balance.  */  
   VendorChange:boolean,
      /**  Linked Inter-Company sales order.  */  
   OrderNum:number,
      /**  Linked Inter-Company Sales order Line number that this order release is linked to.  */  
   OrderLine:number,
      /**  The linked Inter-Company sale order release.  */  
   OrderRelNum:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  ABC Code.  Valid values are "A" through "Z".  */  
   ABCCode:string,
      /**  SuggestionStatus  */  
   SuggestionStatus:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  A flag that is set by the user to indicate the suggestion has been reviewed.  This is only used to help filter suggestions.  */  
   Review:boolean,
      /**  For suggested changes to Promise Date.  */  
   ReqPromiseDate:string,
      /**  Date and time when this record was created.  */  
   CreatedOn:string,
      /**  LockDate  */  
   LockDate:boolean,
      /**  LockQty  */  
   LockQty:boolean,
      /**  PO Release Arrived Qty (note cannot be a linked field as need to set UOM Properties)  */  
   ArrivedQty:number,
   Brw_Exception:string,
   brwPartNum:string,
   brwPurPoint:string,
   brwVendorID:string,
   CancelToggle:boolean,
      /**  Logical indicating whether or not the suggested update is valid for PO releases tied to a Container.  */  
   ContainerAllowAccept:boolean,
   DueDate:string,
   ExpediteToggle:boolean,
   IncreaseToggle:boolean,
   IUM:string,
   JobSeqType:string,
   PostponeToggle:boolean,
   PUM:string,
   ReduceToggle:boolean,
   Rels_OnOrderQty:number,
   SupplierQty:number,
      /**  UOM for SurplusQty  */  
   SurplusQtyUOM:string,
   VendorName:string,
      /**  PO Release 'Our Quantity'  */  
   XRelQty:number,
   BrwPartDesc:string,
      /**  The Promise date set on the PO Release  */  
   PromiseDate:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   brwAttributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   brwAttributeSetShortDescription:string,
      /**  The Full Description of the Attribute Set.  */  
   brwAttributeSetDescription:string,
      /**  ID of parent Attribute Class  */  
   brwAttrClassID:string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
   brwPartTrackInventoryByRevision:boolean,
   brwRevisionNum:string,
   PartClassID:string,
   PartClassDescription:string,
   Selected:boolean,
   BitFlag:number,
   BuyerIDName:string,
   PlantName:string,
   POLineVenPartNum:string,
   POLineLineDesc:string,
   POLinePartNum:string,
   POLineRevisionNum:string,
   PORelContractID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtPOSuggChgTableset{
   SugPOChg:Erp_Tablesets_SugPOChgRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param poNum
      @param poLine
      @param poRelNum
      @param vendorChange
   */  
export interface GetByID_input{
   poNum:number,
   poLine:number,
   poRelNum:number,
   vendorChange:boolean,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_POSuggChgTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_POSuggChgTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_POSuggChgTableset[],
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListPlant_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetListPlant_output{
   returnObj:Erp_Tablesets_SugPOChgListTableset[],
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
   returnObj:Erp_Tablesets_SugPOChgListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param poNum
      @param poLine
      @param poRelNum
   */  
export interface GetNewSugPOChg_input{
   ds:Erp_Tablesets_POSuggChgTableset[],
   poNum:number,
   poLine:number,
   poRelNum:number,
}

export interface GetNewSugPOChg_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggChgTableset,
}
}

   /** Required : 
      @param whereClauseSugPOChg
      @param partNum
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsPlantByPart_input{
      /**  whereClause for SugPOChg table  */  
   whereClauseSugPOChg:string,
      /**  whereClause for partNum  */  
   partNum:string,
      /**  pageSize  */  
   pageSize:number,
      /**  absolutePage  */  
   absolutePage:number,
}

export interface GetRowsPlantByPart_output{
   returnObj:Erp_Tablesets_POSuggChgTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseSugPOChg
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsPlant_input{
      /**  whereClause for SugPOChg table  */  
   whereClauseSugPOChg:string,
      /**  pageSize  */  
   pageSize:number,
      /**  absolutePage  */  
   absolutePage:number,
}

export interface GetRowsPlant_output{
   returnObj:Erp_Tablesets_POSuggChgTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseSugPOChg
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseSugPOChg:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_POSuggChgTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param buyerID
   */  
export interface GetSugPOChgCount_input{
      /**  buyerID  */  
   buyerID:string,
}

export interface GetSugPOChgCount_output{
      /**  Count  */  
   returnObj:number,
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
   */  
export interface MassAcceptSuggestionChanges_input{
   ds:Erp_Tablesets_POSuggChgTableset[],
}

export interface MassAcceptSuggestionChanges_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggChgTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPOSuggChgTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPOSuggChgTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_POSuggChgTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POSuggChgTableset,
}
}

