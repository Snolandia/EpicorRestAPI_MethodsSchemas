import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.APTranSearchSvc
// Description: bo/APTranSearch
           APTran records for AR/AP Invoice Tracker
           Jennifer Johnson
           07/27/04
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/$metadata", {
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
   Description: Get APTranSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APTranSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APTranSearchRow
   */  
export function get_APTranSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranSearchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/APTranSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranSearchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APTranSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APTranSearchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.APTranSearchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APTranSearches(requestBody:Erp_Tablesets_APTranSearchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/APTranSearches", {
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
   Summary: Calls GetByID to retrieve the APTranSearch item
   Description: Calls GetByID to retrieve the APTranSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APTranSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param Voided Desc: Voided   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APTranSearchRow
   */  
export function get_APTranSearches_Company_HeadNum_APTranNo_InvoiceNum_Voided(Company:string, HeadNum:string, APTranNo:string, InvoiceNum:string, Voided:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APTranSearchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/APTranSearches(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")", {
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
         resolve(data as Erp_Tablesets_APTranSearchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APTranSearch for the service
   Description: Calls UpdateExt to update APTranSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APTranSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param Voided Desc: Voided   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.APTranSearchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APTranSearches_Company_HeadNum_APTranNo_InvoiceNum_Voided(Company:string, HeadNum:string, APTranNo:string, InvoiceNum:string, Voided:string, requestBody:Erp_Tablesets_APTranSearchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/APTranSearches(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")", {
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
   Summary: Call UpdateExt to delete APTranSearch item
   Description: Call UpdateExt to delete APTranSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APTranSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param Voided Desc: Voided   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APTranSearches_Company_HeadNum_APTranNo_InvoiceNum_Voided(Company:string, HeadNum:string, APTranNo:string, InvoiceNum:string, Voided:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/APTranSearches(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")", {
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
   Summary: Calls GetRows for the service
   Description: Get PaymentTotals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PaymentTotals
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PaymentTotalsRow
   */  
export function get_PaymentTotals(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PaymentTotalsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/PaymentTotals", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PaymentTotalsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PaymentTotals
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PaymentTotalsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PaymentTotalsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PaymentTotals(requestBody:Erp_Tablesets_PaymentTotalsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/PaymentTotals", {
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
   Summary: Calls GetByID to retrieve the PaymentTotal item
   Description: Calls GetByID to retrieve the PaymentTotal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PaymentTotal
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PaymentTotalsRow
   */  
export function get_PaymentTotals_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PaymentTotalsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/PaymentTotals(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_PaymentTotalsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PaymentTotal for the service
   Description: Calls UpdateExt to update PaymentTotal. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PaymentTotal
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PaymentTotalsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PaymentTotals_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_PaymentTotalsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/PaymentTotals(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete PaymentTotal item
   Description: Call UpdateExt to delete PaymentTotal item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PaymentTotal
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PaymentTotals_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/PaymentTotals(" + SysRowID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APTranSearchListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranSearchListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranSearchListRow)
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
   Required: True   Allow empty value : True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseAPTranSearch:string, whereClausePaymentTotals:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseAPTranSearch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPTranSearch=" + whereClauseAPTranSearch
   }
   if(typeof whereClausePaymentTotals!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePaymentTotals=" + whereClausePaymentTotals
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(headNum:string, apTranNo:string, invoiceNum:string, voided:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof headNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "headNum=" + headNum
   }
   if(typeof apTranNo!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "apTranNo=" + apTranNo
   }
   if(typeof invoiceNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "invoiceNum=" + invoiceNum
   }
   if(typeof voided!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "voided=" + voided
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetRowsForPO
   Description: Invokes GetRows filtering on invoices for the specified PONum
   OperationID: GetRowsForPO
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsForPO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForPO_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForPO(requestBody:GetRowsForPO_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsForPO_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/GetRowsForPO", {
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
         resolve(data as GetRowsForPO_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsForReceipt
   Description: Invokes GetRows filtering on invoices for the specified Pack slip
   OperationID: GetRowsForReceipt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsForReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForReceipt(requestBody:GetRowsForReceipt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsForReceipt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/GetRowsForReceipt", {
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
         resolve(data as GetRowsForReceipt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method KineticGetRows
   Description: bo/APTranSearch
           GetRows to be run from Kinetic UI to also populate pymtTotals
           rather than populating in the client code.
   OperationID: KineticGetRows
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/KineticGetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/KineticGetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_KineticGetRows(requestBody:KineticGetRows_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<KineticGetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/KineticGetRows", {
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
         resolve(data as KineticGetRows_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPaymentData
   Description: bo/APTranSearch
           GetPaymentData to be run from Kinetic UI to populate grid and pymtTotals
           rather than populating in the client code.
   OperationID: GetPaymentData
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPaymentData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPaymentData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPaymentData(requestBody:GetPaymentData_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPaymentData_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/GetPaymentData", {
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
         resolve(data as GetPaymentData_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAPTranSearch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPTranSearch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAPTranSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPTranSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPTranSearch(requestBody:GetNewAPTranSearch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAPTranSearch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/GetNewAPTranSearch", {
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
         resolve(data as GetNewAPTranSearch_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranSearchListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APTranSearchListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranSearchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APTranSearchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PaymentTotalsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PaymentTotalsRow,
}

export interface Erp_Tablesets_APTranSearchListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  An internal flag which identifies the type of transaction. Valid types are "Pay" or "Adj".  */  
   "TranType":string,
      /**  If TranType = "Pay" or "ADJ" for a currency gain/loss  then this is a duplicate of the related CheckHed.HeadNum,  otherwise it is set to zero.  */  
   "HeadNum":number,
      /**  Integer assigned by the system which is used as one of the fields to uniquely identify the APTran record.  If (TranType = "Pay"  and InvoiceNum = "") or (TranType = "Adj") it is assigned a unique #  using the database sequence "APTranNo", for Void checks it is a duplicate of the related APTran.APTranNo, else it is set to zero.  */  
   "APTranNo":number,
      /**  Invoice Number that is being paid or adjusted. This is blank in the case of paying a non-payables expense. Otherwise it DOES have to be valid in the APInvHed file.  */  
   "InvoiceNum":string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process. This is only applicable for TranType = "Pay".  */  
   "Posted":boolean,
      /**  Transaction Amount. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  */  
   "TranAmt":number,
      /**  Transaction Amount in the vendor's currency. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  */  
   "DocTranAmt":number,
      /**  Prompt Payment discount. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  */  
   "DiscAmt":number,
      /**  Prompt Payment discount in Vendors currency. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  */  
   "DocDiscAmt":number,
      /**  In the case of payment details this description is printed on the check stub. If referencing a invoice the APInvHed.Description is used as a default.  */  
   "Description":string,
      /**  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   "BankAcctID":string,
      /**  Check number of the related CheckHed.  */  
   "CheckNum":number,
      /**  Transaction Date. This may be the CheckDate, Void date, or adjustment date. Check dates are duplicated from the CheckHed.CheckDate during the Check printing process. Void date is entered by the user and the void check program duplicates it into each APTran record it generates for the check. Adjustment dates are directly entered by the user.  */  
   "TranDate":string,
      /**   Fiscal Year that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYear during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year to each record on the TranDate  */  
   "FiscalYear":number,
      /**  G\L fiscal period that this transaction is posted to. Updated by the check printing process for system printed checks or by the user for manually printed checks.  If entered must be valid in the Fiscal master.  */  
   "FiscalPeriod":number,
      /**  Indicates if this transaction has been posted to the General Ledger.  This is set during the G/L transfer process.  */  
   "GLPosted":boolean,
      /**   An internal flag indicating if this is a Void payment transaction.
This is set by the A/P void check program. Void payments are duplicates of their original APTran payment record with the exception of having the signs on TranAmt and DiscAmt fields flipped.  */  
   "Voided":boolean,
      /**  UserID that created this APTran record.  */  
   "EntryPerson":string,
      /**  Vendor number. The foreign key that relates the record to the Vendor master record. For TranType = "Pay" it is set equal to CheckHed.VendorNum. For TranType = "Adj" it is captured from the Vendor.VendorNum field.  */  
   "VendorNum":number,
      /**  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adj".  */  
   "Comment":string,
      /**  The Tax Region for this payment.  */  
   "TaxRegionCode":string,
      /**  Sales Tax Amount.  */  
   "TaxAmt":number,
      /**  Tax Amount in the vendors currency.  */  
   "DocTaxAmt":number,
      /**  Link to the related GLRefTyp.RefType.  */  
   "RefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "RefCode":string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   "RefCodeDesc":string,
      /**  Rounding difference arises when invoice in one currency are settled in another currency  */  
   "RoundDiff":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TranAmt":number,
      /**   Fiscal Year Suffix that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYearSuffix during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year suffix to each record on the TranDate  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
      /**  The Legal Number for the record.  */  
   "LegalNumber":string,
      /**  Withholding Tax Amount.  */  
   "WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "DocWithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt1WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt2WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt3WithholdAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "DocSelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt1SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt2SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt3SelfAssessAmt":number,
      /**  Red Storno Flag  */  
   "RedStorno":boolean,
      /**  Indicates that this is prepayment.  */  
   "PrePayment":boolean,
      /**  Free form Reference (e.g. Contract Number or other reference specified by user) In case Ref PO is specified, default reference is 'PO: 99999', but can be changed by user.  */  
   "ContractRef":string,
      /**  Reference Date (e.g. Contract Date, PO Date or other related date) In case Ref PO is specified, default is PO date, and but be changed by user.  */  
   "ContractRefDate":string,
      /**  Reference Purchase Order Number for Prepayments.  */  
   "RefPONum":number,
      /**  Tax Receipt Date (Thailand Localization)  */  
   "TaxReceiptDate":string,
      /**  Tax Receipt Number (Thailand Localization)  */  
   "TaxReceiptNo":string,
      /**  Withholding Tax Certificate Date (Thailand Localization)  */  
   "WHTCertificateDate":string,
      /**  Withholding Tax Certificate Number (Thailand Localization)  */  
   "WHTCertificateNo":string,
      /**  Unique identifier of Petty Cash Desk  */  
   "PCashDeskID":string,
      /**  "R" for realized or "U" for unrealized Gain/Loss  */  
   "GainLossType":string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   "PCashRefNum":number,
      /**  Indicates if it's a reversing Gain/Loss adjustment  */  
   "ReverseGL":boolean,
      /**  Revaluation date that generated the gain/loss record  */  
   "RevalueDate":string,
      /**  Invoice Balance at the time of revaluation  */  
   "RevalueBal":number,
      /**  Document currency Invoice Balance at the time of revaluation  */  
   "DocRevalueBal":number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   "Rpt1RevalueBal":number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   "Rpt2RevalueBal":number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   "Rpt3RevalueBal":number,
      /**  Unique ID of the vendor's bank.  */  
   "BankID":string,
      /**  Amount Bank Paid  */  
   "BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "DocBankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt1BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt2BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt3BankPaidAmt":number,
      /**  Legal Number for the adjustment.  */  
   "AdjLegalNumber":string,
      /**  Transaction Document Type for the adjustment.  */  
   "AdjTranDocTypeID":string,
      /**  Indicates the transaction document type for the record. A document type links a system transaction to a unique legal number.  */  
   "TranDocTypeID":string,
      /**  Main Site  */  
   "MainSite":boolean,
      /**  Site Code  */  
   "SiteCode":string,
      /**  Branch ID  */  
   "BranchID":string,
      /**  Invoice Date  */  
   "InvoiceDate":string,
      /**  Remarks  */  
   "Remarks":string,
      /**  Asset Type Code  */  
   "AssetTypeCode":string,
      /**  Cash  */  
   "Cash":boolean,
      /**  Credit Card  */  
   "CreditCard":boolean,
      /**  Normal  */  
   "Normal":boolean,
      /**  Card ID  */  
   "CardID":string,
      /**  Card Holder Tax ID  */  
   "CardHolderTaxID":string,
      /**  Card Member Name  */  
   "CardMemberName":string,
      /**  Excluded  */  
   "Excluded":boolean,
      /**  Deferred  */  
   "Deferred":boolean,
      /**  Non Deductable Amount  */  
   "NonDeductAmt":number,
      /**  Non Deductable Doc Amount  */  
   "NonDeductDocAmt":number,
      /**  Non Deductable Rpt1 Amount  */  
   "NonDeductRpt1Amt":number,
      /**  Non Deductable Rpt2 Amount  */  
   "NonDeductRpt2Amt":number,
      /**  Non Deductable Rpt3 Amount  */  
   "NonDeductRpt3Amt":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Generation 1099 Date  */  
   "Gen1099Date":string,
      /**  Invoice Currency Symbol  */  
   "InvCurrSymbol":string,
      /**  TranType Description  */  
   "TranDesc":string,
      /**  True if user has security to see Check Payment Details  */  
   "CheckAccess":boolean,
   "CheckAmt":number,
   "InvoiceAmt":number,
   "InvoiceDiscount":number,
      /**  Either Debit Memo or Invoice or blank  */  
   "InvType":string,
      /**  The reference Check number paid by the Corporate for the CPay invoice.  */  
   "CPayCheckNum":number,
      /**  The reference Check Date of the latest payment made by the Corporate for the CPay invoice.  */  
   "CPayCheckDate":string,
      /**  The latest invoice balance of the CPay invoice.  */  
   "CPayBalance":number,
      /**  The latest invoice balance (in Vendor currrency) of the CPay invoice.  */  
   "CPayDocBalance":number,
      /**  Flag to indicate if the CPay invoice got created successfully at the corporate.  */  
   "CPayIMReceived":boolean,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
      /**  Full description of the bank account.  */  
   "BankAcctDescription":string,
      /**  The Bank's full name.  */  
   "BankAcctBankName":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCurrSymbol":string,
      /**  Description of the currency  */  
   "CurrencyCurrDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCurrName":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorTermsCode":string,
      /**  Second address line of the Supplier  */  
   "VendorAddress2":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorCountry":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorName":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorVendorID":string,
      /**  Third address line of the Supplier  */  
   "VendorAddress3":string,
      /**  A unique code that identifies the currency.  */  
   "VendorCurrencyCode":string,
      /**  Can be blank.  */  
   "VendorState":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorZIP":string,
      /**  First address line of the Supplier  */  
   "VendorAddress1":string,
      /**  City portion of the address of the Supplier  */  
   "VendorCity":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorDefaultFOB":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_APTranSearchRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  An internal flag which identifies the type of transaction. Valid types are "Pay" or "Adj".  */  
   "TranType":string,
      /**  If TranType = "Pay" or "ADJ" for a currency gain/loss  then this is a duplicate of the related CheckHed.HeadNum,  otherwise it is set to zero.  */  
   "HeadNum":number,
      /**  Integer assigned by the system which is used as one of the fields to uniquely identify the APTran record.  If (TranType = "Pay"  and InvoiceNum = "") or (TranType = "Adj") it is assigned a unique #  using the database sequence "APTranNo", for Void checks it is a duplicate of the related APTran.APTranNo, else it is set to zero.  */  
   "APTranNo":number,
      /**  Invoice Number that is being paid or adjusted. This is blank in the case of paying a non-payables expense. Otherwise it DOES have to be valid in the APInvHed file.  */  
   "InvoiceNum":string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process. This is only applicable for TranType = "Pay".  */  
   "Posted":boolean,
      /**  Transaction Amount. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  */  
   "TranAmt":number,
      /**  Transaction Amount in the vendor's currency. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  */  
   "DocTranAmt":number,
      /**  Prompt Payment discount. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  */  
   "DiscAmt":number,
      /**  Prompt Payment discount in Vendors currency. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  */  
   "DocDiscAmt":number,
      /**  In the case of payment details this description is printed on the check stub. If referencing a invoice the APInvHed.Description is used as a default.  */  
   "Description":string,
      /**  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   "BankAcctID":string,
      /**  Check number of the related CheckHed.  */  
   "CheckNum":number,
      /**  Transaction Date. This may be the CheckDate, Void date, or adjustment date. Check dates are duplicated from the CheckHed.CheckDate during the Check printing process. Void date is entered by the user and the void check program duplicates it into each APTran record it generates for the check. Adjustment dates are directly entered by the user.  */  
   "TranDate":string,
      /**   Fiscal Year that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYear during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year to each record on the TranDate  */  
   "FiscalYear":number,
      /**  G\L fiscal period that this transaction is posted to. Updated by the check printing process for system printed checks or by the user for manually printed checks.  If entered must be valid in the Fiscal master.  */  
   "FiscalPeriod":number,
      /**  Indicates if this transaction has been posted to the General Ledger.  This is set during the G/L transfer process.  */  
   "GLPosted":boolean,
      /**   An internal flag indicating if this is a Void payment transaction.
This is set by the A/P void check program. Void payments are duplicates of their original APTran payment record with the exception of having the signs on TranAmt and DiscAmt fields flipped.  */  
   "Voided":boolean,
      /**  UserID that created this APTran record.  */  
   "EntryPerson":string,
      /**  Vendor number. The foreign key that relates the record to the Vendor master record. For TranType = "Pay" it is set equal to CheckHed.VendorNum. For TranType = "Adj" it is captured from the Vendor.VendorNum field.  */  
   "VendorNum":number,
      /**  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adj".  */  
   "Comment":string,
      /**  The Tax Region for this payment.  */  
   "TaxRegionCode":string,
      /**  Sales Tax Amount.  */  
   "TaxAmt":number,
      /**  Tax Amount in the vendors currency.  */  
   "DocTaxAmt":number,
      /**  Link to the related GLRefTyp.RefType.  */  
   "RefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "RefCode":string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   "RefCodeDesc":string,
      /**  Rounding difference arises when invoice in one currency are settled in another currency  */  
   "RoundDiff":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TranAmt":number,
      /**   Fiscal Year Suffix that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYearSuffix during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year suffix to each record on the TranDate  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
      /**  The Legal Number for the record.  */  
   "LegalNumber":string,
      /**  Withholding Tax Amount.  */  
   "WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "DocWithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt1WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt2WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt3WithholdAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "DocSelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt1SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt2SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt3SelfAssessAmt":number,
      /**  Red Storno Flag  */  
   "RedStorno":boolean,
      /**  Indicates that this is prepayment.  */  
   "PrePayment":boolean,
      /**  Free form Reference (e.g. Contract Number or other reference specified by user) In case Ref PO is specified, default reference is 'PO: 99999', but can be changed by user.  */  
   "ContractRef":string,
      /**  Reference Date (e.g. Contract Date, PO Date or other related date) In case Ref PO is specified, default is PO date, and but be changed by user.  */  
   "ContractRefDate":string,
      /**  Reference Purchase Order Number for Prepayments.  */  
   "RefPONum":number,
      /**  Tax Receipt Date (Thailand Localization)  */  
   "TaxReceiptDate":string,
      /**  Tax Receipt Number (Thailand Localization)  */  
   "TaxReceiptNo":string,
      /**  Withholding Tax Certificate Date (Thailand Localization)  */  
   "WHTCertificateDate":string,
      /**  Withholding Tax Certificate Number (Thailand Localization)  */  
   "WHTCertificateNo":string,
      /**  Unique identifier of Petty Cash Desk  */  
   "PCashDeskID":string,
      /**  "R" for realized or "U" for unrealized Gain/Loss  */  
   "GainLossType":string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   "PCashRefNum":number,
      /**  Indicates if it's a reversing Gain/Loss adjustment  */  
   "ReverseGL":boolean,
      /**  Revaluation date that generated the gain/loss record  */  
   "RevalueDate":string,
      /**  Invoice Balance at the time of revaluation  */  
   "RevalueBal":number,
      /**  Document currency Invoice Balance at the time of revaluation  */  
   "DocRevalueBal":number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   "Rpt1RevalueBal":number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   "Rpt2RevalueBal":number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   "Rpt3RevalueBal":number,
      /**  Unique ID of the vendor's bank.  */  
   "BankID":string,
      /**  Amount Bank Paid  */  
   "BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "DocBankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt1BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt2BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt3BankPaidAmt":number,
      /**  Legal Number for the adjustment.  */  
   "AdjLegalNumber":string,
      /**  Transaction Document Type for the adjustment.  */  
   "AdjTranDocTypeID":string,
      /**  Indicates the transaction document type for the record. A document type links a system transaction to a unique legal number.  */  
   "TranDocTypeID":string,
      /**  Main Site  */  
   "MainSite":boolean,
      /**  Site Code  */  
   "SiteCode":string,
      /**  Branch ID  */  
   "BranchID":string,
      /**  Invoice Date  */  
   "InvoiceDate":string,
      /**  Remarks  */  
   "Remarks":string,
      /**  Asset Type Code  */  
   "AssetTypeCode":string,
      /**  Cash  */  
   "Cash":boolean,
      /**  Credit Card  */  
   "CreditCard":boolean,
      /**  Normal  */  
   "Normal":boolean,
      /**  Card ID  */  
   "CardID":string,
      /**  Card Holder Tax ID  */  
   "CardHolderTaxID":string,
      /**  Card Member Name  */  
   "CardMemberName":string,
      /**  Excluded  */  
   "Excluded":boolean,
      /**  Deferred  */  
   "Deferred":boolean,
      /**  Non Deductable Amount  */  
   "NonDeductAmt":number,
      /**  Non Deductable Doc Amount  */  
   "NonDeductDocAmt":number,
      /**  Non Deductable Rpt1 Amount  */  
   "NonDeductRpt1Amt":number,
      /**  Non Deductable Rpt2 Amount  */  
   "NonDeductRpt2Amt":number,
      /**  Non Deductable Rpt3 Amount  */  
   "NonDeductRpt3Amt":number,
      /**  PaymentNumber  */  
   "PaymentNumber":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  UrgentPayment  */  
   "UrgentPayment":boolean,
      /**  InvoiceRef  */  
   "InvoiceRef":string,
      /**  Rate Group Code for transactions of type ADJ  */  
   "RateGrpCode":string,
      /**  CNCFICode  */  
   "CNCFICode":string,
      /**  Generation 1099 Date  */  
   "Gen1099Date":string,
      /**  NOTranReason  */  
   "NOTranReason":string,
      /**  PEIsDetractionPayment  */  
   "PEIsDetractionPayment":boolean,
      /**  Code1099ID  */  
   "Code1099ID":string,
      /**  FormTypeID  */  
   "FormTypeID":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  DocWhManAddAmt  */  
   "DocWhManAddAmt":number,
      /**  WhManAddAmt  */  
   "WhManAddAmt":number,
      /**  Rpt1WhManAddAmt  */  
   "Rpt1WhManAddAmt":number,
      /**  Rpt2WhManAddAmt  */  
   "Rpt2WhManAddAmt":number,
      /**  Rpt3WhManAddAmt  */  
   "Rpt3WhManAddAmt":number,
      /**  True if user has security to see Check Payment Details  */  
   "CheckAccess":boolean,
      /**  The latest invoice balance of the CPay invoice.  */  
   "CPayBalance":number,
      /**  The reference Check Date of the latest payment made by the Corporate for the CPay invoice.  */  
   "CPayCheckDate":string,
      /**  The reference Check number paid by the Corporate for the CPay invoice.  */  
   "CPayCheckNum":number,
      /**  The latest invoice balance (in Vendor currrency) of the CPay invoice.  */  
   "CPayDocBalance":number,
      /**  Flag to indicate if the CPay invoice got created successfully at the corporate.  */  
   "CPayIMReceived":boolean,
   "CurrDesc":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencyID":string,
   "CurrName":string,
   "CurrSymbol":string,
   "DocumentDesc":string,
      /**  Invoice Currency Symbol  */  
   "InvCurrSymbol":string,
   "InvoiceAmt":number,
   "InvoiceDiscount":number,
      /**  Either Debit Memo or Invoice or blank  */  
   "InvType":string,
      /**  TranType Description  */  
   "TranDesc":string,
      /**  (CSF Peru) Bill of Exchange Invoice Number  */  
   "BOEInvoiceNum":string,
   "CheckAmt":number,
      /**  Id of the netting transaction that generated this document.  */  
   "NettingID":number,
      /**  Site Code  */  
   "PayingSiteCode":string,
   "BitFlag":number,
   "BankAcctDescription":string,
   "BankAcctBankName":string,
   "VendorState":string,
   "VendorCity":string,
   "VendorName":string,
   "VendorZIP":string,
   "VendorTermsCode":string,
   "VendorVendorID":string,
   "VendorAddress2":string,
   "VendorAddress3":string,
   "VendorAddress1":string,
   "VendorDefaultFOB":string,
   "VendorCurrencyCode":string,
   "VendorCountry":string,
   "VendorBankBankName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PaymentTotalsRow{
   "CashRcv":number,
   "DocCashRcv":number,
   "DocDscTaken":number,
   "DocGainReal":number,
   "DocGainUnreal":number,
   "DscTaken":number,
   "GainReal":number,
   "GainUnreal":number,
   "RevalDate":string,
   "Rpt1CashRcv":number,
   "Rpt1DscTaken":number,
   "Rpt1GainReal":number,
   "Rpt1GainUnreal":number,
   "Rpt2CashRcv":number,
   "Rpt2DscTaken":number,
   "Rpt2GainReal":number,
   "Rpt2GainUnreal":number,
   "Rpt3CashRcv":number,
   "Rpt3DscTaken":number,
   "Rpt3GainReal":number,
   "Rpt3GainUnreal":number,
   "SysRowID":string,
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
      @param headNum
      @param apTranNo
      @param invoiceNum
      @param voided
   */  
export interface DeleteByID_input{
   headNum:number,
   apTranNo:number,
   invoiceNum:string,
   voided:boolean,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_APTranSearchListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  An internal flag which identifies the type of transaction. Valid types are "Pay" or "Adj".  */  
   TranType:string,
      /**  If TranType = "Pay" or "ADJ" for a currency gain/loss  then this is a duplicate of the related CheckHed.HeadNum,  otherwise it is set to zero.  */  
   HeadNum:number,
      /**  Integer assigned by the system which is used as one of the fields to uniquely identify the APTran record.  If (TranType = "Pay"  and InvoiceNum = "") or (TranType = "Adj") it is assigned a unique #  using the database sequence "APTranNo", for Void checks it is a duplicate of the related APTran.APTranNo, else it is set to zero.  */  
   APTranNo:number,
      /**  Invoice Number that is being paid or adjusted. This is blank in the case of paying a non-payables expense. Otherwise it DOES have to be valid in the APInvHed file.  */  
   InvoiceNum:string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process. This is only applicable for TranType = "Pay".  */  
   Posted:boolean,
      /**  Transaction Amount. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  */  
   TranAmt:number,
      /**  Transaction Amount in the vendor's currency. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  */  
   DocTranAmt:number,
      /**  Prompt Payment discount. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  */  
   DiscAmt:number,
      /**  Prompt Payment discount in Vendors currency. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  */  
   DocDiscAmt:number,
      /**  In the case of payment details this description is printed on the check stub. If referencing a invoice the APInvHed.Description is used as a default.  */  
   Description:string,
      /**  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   BankAcctID:string,
      /**  Check number of the related CheckHed.  */  
   CheckNum:number,
      /**  Transaction Date. This may be the CheckDate, Void date, or adjustment date. Check dates are duplicated from the CheckHed.CheckDate during the Check printing process. Void date is entered by the user and the void check program duplicates it into each APTran record it generates for the check. Adjustment dates are directly entered by the user.  */  
   TranDate:string,
      /**   Fiscal Year that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYear during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year to each record on the TranDate  */  
   FiscalYear:number,
      /**  G\L fiscal period that this transaction is posted to. Updated by the check printing process for system printed checks or by the user for manually printed checks.  If entered must be valid in the Fiscal master.  */  
   FiscalPeriod:number,
      /**  Indicates if this transaction has been posted to the General Ledger.  This is set during the G/L transfer process.  */  
   GLPosted:boolean,
      /**   An internal flag indicating if this is a Void payment transaction.
This is set by the A/P void check program. Void payments are duplicates of their original APTran payment record with the exception of having the signs on TranAmt and DiscAmt fields flipped.  */  
   Voided:boolean,
      /**  UserID that created this APTran record.  */  
   EntryPerson:string,
      /**  Vendor number. The foreign key that relates the record to the Vendor master record. For TranType = "Pay" it is set equal to CheckHed.VendorNum. For TranType = "Adj" it is captured from the Vendor.VendorNum field.  */  
   VendorNum:number,
      /**  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adj".  */  
   Comment:string,
      /**  The Tax Region for this payment.  */  
   TaxRegionCode:string,
      /**  Sales Tax Amount.  */  
   TaxAmt:number,
      /**  Tax Amount in the vendors currency.  */  
   DocTaxAmt:number,
      /**  Link to the related GLRefTyp.RefType.  */  
   RefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   RefCodeDesc:string,
      /**  Rounding difference arises when invoice in one currency are settled in another currency  */  
   RoundDiff:number,
      /**  Reporting currency value of this field  */  
   Rpt1DiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TranAmt:number,
      /**   Fiscal Year Suffix that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYearSuffix during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year suffix to each record on the TranDate  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  The Legal Number for the record.  */  
   LegalNumber:string,
      /**  Withholding Tax Amount.  */  
   WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   DocWithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt1WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt2WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt3WithholdAmt:number,
      /**  Self Assessment Tax Amount.  */  
   SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   DocSelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt1SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt2SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt3SelfAssessAmt:number,
      /**  Red Storno Flag  */  
   RedStorno:boolean,
      /**  Indicates that this is prepayment.  */  
   PrePayment:boolean,
      /**  Free form Reference (e.g. Contract Number or other reference specified by user) In case Ref PO is specified, default reference is 'PO: 99999', but can be changed by user.  */  
   ContractRef:string,
      /**  Reference Date (e.g. Contract Date, PO Date or other related date) In case Ref PO is specified, default is PO date, and but be changed by user.  */  
   ContractRefDate:string,
      /**  Reference Purchase Order Number for Prepayments.  */  
   RefPONum:number,
      /**  Tax Receipt Date (Thailand Localization)  */  
   TaxReceiptDate:string,
      /**  Tax Receipt Number (Thailand Localization)  */  
   TaxReceiptNo:string,
      /**  Withholding Tax Certificate Date (Thailand Localization)  */  
   WHTCertificateDate:string,
      /**  Withholding Tax Certificate Number (Thailand Localization)  */  
   WHTCertificateNo:string,
      /**  Unique identifier of Petty Cash Desk  */  
   PCashDeskID:string,
      /**  "R" for realized or "U" for unrealized Gain/Loss  */  
   GainLossType:string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   PCashRefNum:number,
      /**  Indicates if it's a reversing Gain/Loss adjustment  */  
   ReverseGL:boolean,
      /**  Revaluation date that generated the gain/loss record  */  
   RevalueDate:string,
      /**  Invoice Balance at the time of revaluation  */  
   RevalueBal:number,
      /**  Document currency Invoice Balance at the time of revaluation  */  
   DocRevalueBal:number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   Rpt1RevalueBal:number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   Rpt2RevalueBal:number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   Rpt3RevalueBal:number,
      /**  Unique ID of the vendor's bank.  */  
   BankID:string,
      /**  Amount Bank Paid  */  
   BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   DocBankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt1BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt2BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt3BankPaidAmt:number,
      /**  Legal Number for the adjustment.  */  
   AdjLegalNumber:string,
      /**  Transaction Document Type for the adjustment.  */  
   AdjTranDocTypeID:string,
      /**  Indicates the transaction document type for the record. A document type links a system transaction to a unique legal number.  */  
   TranDocTypeID:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**  Site Code  */  
   SiteCode:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Invoice Date  */  
   InvoiceDate:string,
      /**  Remarks  */  
   Remarks:string,
      /**  Asset Type Code  */  
   AssetTypeCode:string,
      /**  Cash  */  
   Cash:boolean,
      /**  Credit Card  */  
   CreditCard:boolean,
      /**  Normal  */  
   Normal:boolean,
      /**  Card ID  */  
   CardID:string,
      /**  Card Holder Tax ID  */  
   CardHolderTaxID:string,
      /**  Card Member Name  */  
   CardMemberName:string,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  Non Deductable Amount  */  
   NonDeductAmt:number,
      /**  Non Deductable Doc Amount  */  
   NonDeductDocAmt:number,
      /**  Non Deductable Rpt1 Amount  */  
   NonDeductRpt1Amt:number,
      /**  Non Deductable Rpt2 Amount  */  
   NonDeductRpt2Amt:number,
      /**  Non Deductable Rpt3 Amount  */  
   NonDeductRpt3Amt:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Generation 1099 Date  */  
   Gen1099Date:string,
      /**  Invoice Currency Symbol  */  
   InvCurrSymbol:string,
      /**  TranType Description  */  
   TranDesc:string,
      /**  True if user has security to see Check Payment Details  */  
   CheckAccess:boolean,
   CheckAmt:number,
   InvoiceAmt:number,
   InvoiceDiscount:number,
      /**  Either Debit Memo or Invoice or blank  */  
   InvType:string,
      /**  The reference Check number paid by the Corporate for the CPay invoice.  */  
   CPayCheckNum:number,
      /**  The reference Check Date of the latest payment made by the Corporate for the CPay invoice.  */  
   CPayCheckDate:string,
      /**  The latest invoice balance of the CPay invoice.  */  
   CPayBalance:number,
      /**  The latest invoice balance (in Vendor currrency) of the CPay invoice.  */  
   CPayDocBalance:number,
      /**  Flag to indicate if the CPay invoice got created successfully at the corporate.  */  
   CPayIMReceived:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  Full description of the bank account.  */  
   BankAcctDescription:string,
      /**  The Bank's full name.  */  
   BankAcctBankName:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCurrSymbol:string,
      /**  Description of the currency  */  
   CurrencyCurrDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCurrName:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorTermsCode:string,
      /**  Second address line of the Supplier  */  
   VendorAddress2:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorCountry:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorName:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorVendorID:string,
      /**  Third address line of the Supplier  */  
   VendorAddress3:string,
      /**  A unique code that identifies the currency.  */  
   VendorCurrencyCode:string,
      /**  Can be blank.  */  
   VendorState:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorZIP:string,
      /**  First address line of the Supplier  */  
   VendorAddress1:string,
      /**  City portion of the address of the Supplier  */  
   VendorCity:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorDefaultFOB:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APTranSearchListTableset{
   APTranSearchList:Erp_Tablesets_APTranSearchListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_APTranSearchRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  An internal flag which identifies the type of transaction. Valid types are "Pay" or "Adj".  */  
   TranType:string,
      /**  If TranType = "Pay" or "ADJ" for a currency gain/loss  then this is a duplicate of the related CheckHed.HeadNum,  otherwise it is set to zero.  */  
   HeadNum:number,
      /**  Integer assigned by the system which is used as one of the fields to uniquely identify the APTran record.  If (TranType = "Pay"  and InvoiceNum = "") or (TranType = "Adj") it is assigned a unique #  using the database sequence "APTranNo", for Void checks it is a duplicate of the related APTran.APTranNo, else it is set to zero.  */  
   APTranNo:number,
      /**  Invoice Number that is being paid or adjusted. This is blank in the case of paying a non-payables expense. Otherwise it DOES have to be valid in the APInvHed file.  */  
   InvoiceNum:string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process. This is only applicable for TranType = "Pay".  */  
   Posted:boolean,
      /**  Transaction Amount. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  */  
   TranAmt:number,
      /**  Transaction Amount in the vendor's currency. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  */  
   DocTranAmt:number,
      /**  Prompt Payment discount. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  */  
   DiscAmt:number,
      /**  Prompt Payment discount in Vendors currency. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  */  
   DocDiscAmt:number,
      /**  In the case of payment details this description is printed on the check stub. If referencing a invoice the APInvHed.Description is used as a default.  */  
   Description:string,
      /**  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   BankAcctID:string,
      /**  Check number of the related CheckHed.  */  
   CheckNum:number,
      /**  Transaction Date. This may be the CheckDate, Void date, or adjustment date. Check dates are duplicated from the CheckHed.CheckDate during the Check printing process. Void date is entered by the user and the void check program duplicates it into each APTran record it generates for the check. Adjustment dates are directly entered by the user.  */  
   TranDate:string,
      /**   Fiscal Year that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYear during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year to each record on the TranDate  */  
   FiscalYear:number,
      /**  G\L fiscal period that this transaction is posted to. Updated by the check printing process for system printed checks or by the user for manually printed checks.  If entered must be valid in the Fiscal master.  */  
   FiscalPeriod:number,
      /**  Indicates if this transaction has been posted to the General Ledger.  This is set during the G/L transfer process.  */  
   GLPosted:boolean,
      /**   An internal flag indicating if this is a Void payment transaction.
This is set by the A/P void check program. Void payments are duplicates of their original APTran payment record with the exception of having the signs on TranAmt and DiscAmt fields flipped.  */  
   Voided:boolean,
      /**  UserID that created this APTran record.  */  
   EntryPerson:string,
      /**  Vendor number. The foreign key that relates the record to the Vendor master record. For TranType = "Pay" it is set equal to CheckHed.VendorNum. For TranType = "Adj" it is captured from the Vendor.VendorNum field.  */  
   VendorNum:number,
      /**  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adj".  */  
   Comment:string,
      /**  The Tax Region for this payment.  */  
   TaxRegionCode:string,
      /**  Sales Tax Amount.  */  
   TaxAmt:number,
      /**  Tax Amount in the vendors currency.  */  
   DocTaxAmt:number,
      /**  Link to the related GLRefTyp.RefType.  */  
   RefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   RefCodeDesc:string,
      /**  Rounding difference arises when invoice in one currency are settled in another currency  */  
   RoundDiff:number,
      /**  Reporting currency value of this field  */  
   Rpt1DiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TranAmt:number,
      /**   Fiscal Year Suffix that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYearSuffix during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year suffix to each record on the TranDate  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  The Legal Number for the record.  */  
   LegalNumber:string,
      /**  Withholding Tax Amount.  */  
   WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   DocWithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt1WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt2WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt3WithholdAmt:number,
      /**  Self Assessment Tax Amount.  */  
   SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   DocSelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt1SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt2SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt3SelfAssessAmt:number,
      /**  Red Storno Flag  */  
   RedStorno:boolean,
      /**  Indicates that this is prepayment.  */  
   PrePayment:boolean,
      /**  Free form Reference (e.g. Contract Number or other reference specified by user) In case Ref PO is specified, default reference is 'PO: 99999', but can be changed by user.  */  
   ContractRef:string,
      /**  Reference Date (e.g. Contract Date, PO Date or other related date) In case Ref PO is specified, default is PO date, and but be changed by user.  */  
   ContractRefDate:string,
      /**  Reference Purchase Order Number for Prepayments.  */  
   RefPONum:number,
      /**  Tax Receipt Date (Thailand Localization)  */  
   TaxReceiptDate:string,
      /**  Tax Receipt Number (Thailand Localization)  */  
   TaxReceiptNo:string,
      /**  Withholding Tax Certificate Date (Thailand Localization)  */  
   WHTCertificateDate:string,
      /**  Withholding Tax Certificate Number (Thailand Localization)  */  
   WHTCertificateNo:string,
      /**  Unique identifier of Petty Cash Desk  */  
   PCashDeskID:string,
      /**  "R" for realized or "U" for unrealized Gain/Loss  */  
   GainLossType:string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   PCashRefNum:number,
      /**  Indicates if it's a reversing Gain/Loss adjustment  */  
   ReverseGL:boolean,
      /**  Revaluation date that generated the gain/loss record  */  
   RevalueDate:string,
      /**  Invoice Balance at the time of revaluation  */  
   RevalueBal:number,
      /**  Document currency Invoice Balance at the time of revaluation  */  
   DocRevalueBal:number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   Rpt1RevalueBal:number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   Rpt2RevalueBal:number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   Rpt3RevalueBal:number,
      /**  Unique ID of the vendor's bank.  */  
   BankID:string,
      /**  Amount Bank Paid  */  
   BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   DocBankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt1BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt2BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt3BankPaidAmt:number,
      /**  Legal Number for the adjustment.  */  
   AdjLegalNumber:string,
      /**  Transaction Document Type for the adjustment.  */  
   AdjTranDocTypeID:string,
      /**  Indicates the transaction document type for the record. A document type links a system transaction to a unique legal number.  */  
   TranDocTypeID:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**  Site Code  */  
   SiteCode:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Invoice Date  */  
   InvoiceDate:string,
      /**  Remarks  */  
   Remarks:string,
      /**  Asset Type Code  */  
   AssetTypeCode:string,
      /**  Cash  */  
   Cash:boolean,
      /**  Credit Card  */  
   CreditCard:boolean,
      /**  Normal  */  
   Normal:boolean,
      /**  Card ID  */  
   CardID:string,
      /**  Card Holder Tax ID  */  
   CardHolderTaxID:string,
      /**  Card Member Name  */  
   CardMemberName:string,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  Non Deductable Amount  */  
   NonDeductAmt:number,
      /**  Non Deductable Doc Amount  */  
   NonDeductDocAmt:number,
      /**  Non Deductable Rpt1 Amount  */  
   NonDeductRpt1Amt:number,
      /**  Non Deductable Rpt2 Amount  */  
   NonDeductRpt2Amt:number,
      /**  Non Deductable Rpt3 Amount  */  
   NonDeductRpt3Amt:number,
      /**  PaymentNumber  */  
   PaymentNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  UrgentPayment  */  
   UrgentPayment:boolean,
      /**  InvoiceRef  */  
   InvoiceRef:string,
      /**  Rate Group Code for transactions of type ADJ  */  
   RateGrpCode:string,
      /**  CNCFICode  */  
   CNCFICode:string,
      /**  Generation 1099 Date  */  
   Gen1099Date:string,
      /**  NOTranReason  */  
   NOTranReason:string,
      /**  PEIsDetractionPayment  */  
   PEIsDetractionPayment:boolean,
      /**  Code1099ID  */  
   Code1099ID:string,
      /**  FormTypeID  */  
   FormTypeID:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  DocWhManAddAmt  */  
   DocWhManAddAmt:number,
      /**  WhManAddAmt  */  
   WhManAddAmt:number,
      /**  Rpt1WhManAddAmt  */  
   Rpt1WhManAddAmt:number,
      /**  Rpt2WhManAddAmt  */  
   Rpt2WhManAddAmt:number,
      /**  Rpt3WhManAddAmt  */  
   Rpt3WhManAddAmt:number,
      /**  True if user has security to see Check Payment Details  */  
   CheckAccess:boolean,
      /**  The latest invoice balance of the CPay invoice.  */  
   CPayBalance:number,
      /**  The reference Check Date of the latest payment made by the Corporate for the CPay invoice.  */  
   CPayCheckDate:string,
      /**  The reference Check number paid by the Corporate for the CPay invoice.  */  
   CPayCheckNum:number,
      /**  The latest invoice balance (in Vendor currrency) of the CPay invoice.  */  
   CPayDocBalance:number,
      /**  Flag to indicate if the CPay invoice got created successfully at the corporate.  */  
   CPayIMReceived:boolean,
   CurrDesc:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencyID:string,
   CurrName:string,
   CurrSymbol:string,
   DocumentDesc:string,
      /**  Invoice Currency Symbol  */  
   InvCurrSymbol:string,
   InvoiceAmt:number,
   InvoiceDiscount:number,
      /**  Either Debit Memo or Invoice or blank  */  
   InvType:string,
      /**  TranType Description  */  
   TranDesc:string,
      /**  (CSF Peru) Bill of Exchange Invoice Number  */  
   BOEInvoiceNum:string,
   CheckAmt:number,
      /**  Id of the netting transaction that generated this document.  */  
   NettingID:number,
      /**  Site Code  */  
   PayingSiteCode:string,
   BitFlag:number,
   BankAcctDescription:string,
   BankAcctBankName:string,
   VendorState:string,
   VendorCity:string,
   VendorName:string,
   VendorZIP:string,
   VendorTermsCode:string,
   VendorVendorID:string,
   VendorAddress2:string,
   VendorAddress3:string,
   VendorAddress1:string,
   VendorDefaultFOB:string,
   VendorCurrencyCode:string,
   VendorCountry:string,
   VendorBankBankName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APTranSearchTableset{
   APTranSearch:Erp_Tablesets_APTranSearchRow[],
   PaymentTotals:Erp_Tablesets_PaymentTotalsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PaymentTotalsRow{
   CashRcv:number,
   DocCashRcv:number,
   DocDscTaken:number,
   DocGainReal:number,
   DocGainUnreal:number,
   DscTaken:number,
   GainReal:number,
   GainUnreal:number,
   RevalDate:string,
   Rpt1CashRcv:number,
   Rpt1DscTaken:number,
   Rpt1GainReal:number,
   Rpt1GainUnreal:number,
   Rpt2CashRcv:number,
   Rpt2DscTaken:number,
   Rpt2GainReal:number,
   Rpt2GainUnreal:number,
   Rpt3CashRcv:number,
   Rpt3DscTaken:number,
   Rpt3GainReal:number,
   Rpt3GainUnreal:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtAPTranSearchTableset{
   APTranSearch:Erp_Tablesets_APTranSearchRow[],
   PaymentTotals:Erp_Tablesets_PaymentTotalsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param headNum
      @param apTranNo
      @param invoiceNum
      @param voided
   */  
export interface GetByID_input{
   headNum:number,
   apTranNo:number,
   invoiceNum:string,
   voided:boolean,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_APTranSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_APTranSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_APTranSearchTableset[],
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
   returnObj:Erp_Tablesets_APTranSearchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param headNum
      @param apTranNo
      @param invoiceNum
   */  
export interface GetNewAPTranSearch_input{
   ds:Erp_Tablesets_APTranSearchTableset[],
   headNum:number,
   apTranNo:number,
   invoiceNum:string,
}

export interface GetNewAPTranSearch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APTranSearchTableset,
}
}

   /** Required : 
      @param vendorNum
      @param invoiceNum
   */  
export interface GetPaymentData_input{
   vendorNum:number,
   invoiceNum:string,
}

export interface GetPaymentData_output{
   returnObj:Erp_Tablesets_APTranSearchTableset[],
}

   /** Required : 
      @param whereClauseAPTranSearch
      @param poNum
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForPO_input{
   whereClauseAPTranSearch:string,
   poNum:number,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsForPO_output{
   returnObj:Erp_Tablesets_APTranSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseAPTranSearch
      @param vendorNum
      @param purPoint
      @param packSlip
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForReceipt_input{
   whereClauseAPTranSearch:string,
   vendorNum:number,
   purPoint:string,
   packSlip:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsForReceipt_output{
   returnObj:Erp_Tablesets_APTranSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseAPTranSearch
      @param whereClausePaymentTotals
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseAPTranSearch:string,
   whereClausePaymentTotals:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_APTranSearchTableset[],
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
      @param whereClauseAPTranSearch
   */  
export interface KineticGetRows_input{
   whereClauseAPTranSearch:string,
}

export interface KineticGetRows_output{
   returnObj:Erp_Tablesets_APTranSearchTableset[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtAPTranSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtAPTranSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_APTranSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APTranSearchTableset,
}
}

