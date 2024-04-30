import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.CreditTranSvc
// Description: Credit Transaction Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/$metadata", {
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
   Description: Get CreditTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CreditTrans
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CreditTranRow
   */  
export function get_CreditTrans(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/CreditTrans", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CreditTrans
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CreditTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CreditTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreditTrans(requestBody:Erp_Tablesets_CreditTranRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/CreditTrans", {
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
   Summary: Calls GetByID to retrieve the CreditTran item
   Description: Calls GetByID to retrieve the CreditTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CreditTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranDate Desc: TranDate   Required: True   Allow empty value : True
      @param TranTime Desc: TranTime   Required: True
      @param TranNum Desc: TranNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CreditTranRow
   */  
export function get_CreditTrans_Company_TranDate_TranTime_TranNum(Company:string, TranDate:string, TranTime:string, TranNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CreditTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/CreditTrans(" + Company + "," + TranDate + "," + TranTime + "," + TranNum + ")", {
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
         resolve(data as Erp_Tablesets_CreditTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CreditTran for the service
   Description: Calls UpdateExt to update CreditTran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CreditTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranDate Desc: TranDate   Required: True   Allow empty value : True
      @param TranTime Desc: TranTime   Required: True
      @param TranNum Desc: TranNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CreditTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CreditTrans_Company_TranDate_TranTime_TranNum(Company:string, TranDate:string, TranTime:string, TranNum:string, requestBody:Erp_Tablesets_CreditTranRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/CreditTrans(" + Company + "," + TranDate + "," + TranTime + "," + TranNum + ")", {
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
   Summary: Call UpdateExt to delete CreditTran item
   Description: Call UpdateExt to delete CreditTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CreditTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranDate Desc: TranDate   Required: True   Allow empty value : True
      @param TranTime Desc: TranTime   Required: True
      @param TranNum Desc: TranNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CreditTrans_Company_TranDate_TranTime_TranNum(Company:string, TranDate:string, TranTime:string, TranNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/CreditTrans(" + Company + "," + TranDate + "," + TranTime + "," + TranNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CreditTranListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditTranListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditTranListRow)
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
export function get_GetRows(whereClauseCreditTran:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCreditTran!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCreditTran=" + whereClauseCreditTran
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/GetRows" + params, {
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(tranDate:string, tranTime:string, tranNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof tranDate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tranDate=" + tranDate
   }
   if(typeof tranTime!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tranTime=" + tranTime
   }
   if(typeof tranNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tranNum=" + tranNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/GetList" + params, {
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
   Summary: Invoke method GetRowsContactTracker
   Description: Called from Contact tracker instead of GetRows for better performance
   OperationID: GetRowsContactTracker
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsContactTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsContactTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsContactTracker(requestBody:GetRowsContactTracker_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsContactTracker_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/GetRowsContactTracker", {
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
         resolve(data as GetRowsContactTracker_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsForCreditCard
   Description: Filter by Credit Card Fields
   OperationID: GetRowsForCreditCard
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsForCreditCard_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForCreditCard_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForCreditCard(requestBody:GetRowsForCreditCard_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsForCreditCard_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/GetRowsForCreditCard", {
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
         resolve(data as GetRowsForCreditCard_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListForApplyCreditMemo
   Description: Returns a list Dataset containing the Deposit and Sale transactions with remaining balance.
The Transaction balance is calculated by subtracting Credit transactions (TranType = C) to TranAmt.
It is used for ApplyCM.
   OperationID: GetListForApplyCreditMemo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListForApplyCreditMemo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForApplyCreditMemo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListForApplyCreditMemo(requestBody:GetListForApplyCreditMemo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListForApplyCreditMemo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/GetListForApplyCreditMemo", {
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
         resolve(data as GetListForApplyCreditMemo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCardNumbers
   Description: Returns a list Dataset containing the valid credit card numbers already used
for the current customer and currency code.
It is used in Sales Order and Cash Receipt for Credit Card Number search grid.
   OperationID: GetCardNumbers
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCardNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCardNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCardNumbers(requestBody:GetCardNumbers_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCardNumbers_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/GetCardNumbers", {
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
         resolve(data as GetCardNumbers_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCreditTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCreditTran
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCreditTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCreditTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCreditTran(requestBody:GetNewCreditTran_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCreditTran_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/GetNewCreditTran", {
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
         resolve(data as GetNewCreditTran_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditTranListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CreditTranListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditTranRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CreditTranRow,
}

export interface Erp_Tablesets_CreditTranListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Transaction Date  */  
   "TranDate":string,
      /**  Part of the unique key  */  
   "TranTime":number,
      /**  Transaction Number  */  
   "TranNum":number,
      /**  Transaction Type  */  
   "TranType":string,
      /**  Transaction Total in base currency.  */  
   "TranTotal":number,
      /**  Transaction Total in document currency.  */  
   "DocTranTotal":number,
      /**  Processing company's Reference ID, unique to each transaction  */  
   "PNRef":string,
      /**  Autherisation Code  */  
   "AuthCode":string,
      /**  Error code returned by processing company  */  
   "Result":string,
      /**  Response Message  */  
   "ResponseMsg":string,
      /**  result of the address verification  */  
   "AVSAddr":string,
      /**  Result of the address zip verification  */  
   "AVSZip":string,
      /**  Result of the credit security code check  */  
   "CSCMatch":string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   "OrderNum":number,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   "InvoiceNum":number,
      /**  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   "HeadNum":number,
      /**  A unique identifier for a specific credit card type assigned by the user.  */  
   "CardType":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Transaction Type Description  */  
   "TranTypeDesc":string,
      /**  The member's name on the credit card.  */  
   "CardMemberName":string,
      /**  The expiration month of the credit card.  */  
   "ExpMonth":number,
      /**  The expiration year of the credit card.  */  
   "ExpYear":number,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   "CardmemberReference":string,
      /**  The credit card account identifier.  */  
   "CardNumber":string,
      /**  ST Link Address  */  
   "StAddress":string,
      /**  The zip or postal code portion of the customer's main address.  */  
   "Zip":string,
      /**  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  */  
   "ReferencePNRef":string,
      /**  Flag to indicate that a prior process has used this authorization  */  
   "AuthUsed":boolean,
      /**  Encrypted Credit Card Number  */  
   "CardStore":string,
      /**  Freight Charges in base currency  */  
   "Freight":number,
      /**  Freight Charges in document currency  */  
   "DocFreight":number,
      /**  Tax amount in base currency.  */  
   "Tax":number,
      /**  Tax amount in document currency.  */  
   "DocTax":number,
      /**  Transaction Amount in base currency.  */  
   "Amount":number,
      /**  Transaction Amount in document currency.  */  
   "DocAmount":number,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   "CustNum":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Amount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Amount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Amount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Freight":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Freight":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Freight":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Tax":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Tax":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Tax":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TranTotal":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TranTotal":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TranTotal":number,
      /**  Userid of user who made the credit transaction  */  
   "CreatedBy":string,
      /**  STLink Identifier  */  
   "StrId":string,
      /**  Result of CVN checl  */  
   "CVNCode":number,
      /**  SVN verification message  */  
   "CVNMessage":string,
      /**  Referrer Code  */  
   "ReferrerCode":string,
      /**  Order Number created by PaymentTrust if not supplied by process  */  
   "PTOrderNum":string,
      /**  Authorisation Entity  */  
   "AuthEntity":string,
      /**  Indicates if transaction was successful or not  */  
   "TranSuccess":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CustomerName":string,
   "ShipToNum":string,
   "ShipToName":string,
      /**  The primary contact for the related order.  */  
   "PrcConNum":number,
      /**  The shipping contact number for the order.  */  
   "ShpConNum":number,
   "CustID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CreditTranRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Transaction Date  */  
   "TranDate":string,
      /**  Part of the unique key  */  
   "TranTime":number,
      /**  Transaction Number  */  
   "TranNum":number,
      /**  Transaction Type  */  
   "TranType":string,
      /**  Transaction Total in base currency.  */  
   "TranTotal":number,
      /**  Transaction Total in document currency.  */  
   "DocTranTotal":number,
      /**  Processing company's Reference ID, unique to each transaction  */  
   "PNRef":string,
      /**  Autherisation Code  */  
   "AuthCode":string,
      /**  Error code returned by processing company  */  
   "Result":string,
      /**  Response Message  */  
   "ResponseMsg":string,
      /**  result of the address verification  */  
   "AVSAddr":string,
      /**  Result of the address zip verification  */  
   "AVSZip":string,
      /**  Result of the credit security code check  */  
   "CSCMatch":string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   "OrderNum":number,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   "InvoiceNum":number,
      /**  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   "HeadNum":number,
      /**  A unique identifier for a specific credit card type assigned by the user.  */  
   "CardType":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Transaction Type Description  */  
   "TranTypeDesc":string,
      /**  The member's name on the credit card.  */  
   "CardMemberName":string,
      /**  The expiration month of the credit card.  */  
   "ExpMonth":number,
      /**  The expiration year of the credit card.  */  
   "ExpYear":number,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   "CardmemberReference":string,
      /**  The credit card account identifier.  */  
   "CardNumber":string,
      /**  ST Link Address  */  
   "StAddress":string,
      /**  The zip or postal code portion of the customer's main address.  */  
   "Zip":string,
      /**  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  */  
   "ReferencePNRef":string,
      /**  Flag to indicate that a prior process has used this authorization  */  
   "AuthUsed":boolean,
      /**  Encrypted Credit Card Number  */  
   "CardStore":string,
      /**  Freight Charges in base currency  */  
   "Freight":number,
      /**  Freight Charges in document currency  */  
   "DocFreight":number,
      /**  Tax amount in base currency.  */  
   "Tax":number,
      /**  Tax amount in document currency.  */  
   "DocTax":number,
      /**  Transaction Amount in base currency.  */  
   "Amount":number,
      /**  Transaction Amount in document currency.  */  
   "DocAmount":number,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   "CustNum":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Amount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Amount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Amount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Freight":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Freight":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Freight":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Tax":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Tax":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Tax":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TranTotal":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TranTotal":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TranTotal":number,
      /**  Userid of user who made the credit transaction  */  
   "CreatedBy":string,
      /**  STLink Identifier  */  
   "StrId":string,
      /**  Result of CVN checl  */  
   "CVNCode":number,
      /**  SVN verification message  */  
   "CVNMessage":string,
      /**  Referrer Code  */  
   "ReferrerCode":string,
      /**  Order Number created by PaymentTrust if not supplied by process  */  
   "PTOrderNum":string,
      /**  Authorisation Entity  */  
   "AuthEntity":string,
      /**  Indicates if transaction was successful or not  */  
   "TranSuccess":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  CCCity  */  
   "CCCity":string,
      /**  CCState  */  
   "CCState":string,
      /**  FDMS Reference Data used in Deposit and Void transaction.  */  
   "FDMSReferenceData":string,
      /**  Processor  */  
   "Processor":string,
      /**  ISOCurrCode  */  
   "ISOCurrCode":string,
      /**  The customer ID.  */  
   "CustID":string,
      /**  The full name for customer.  */  
   "CustomerName":string,
   "ShipToNum":string,
      /**  The shipping contact number for the order.  */  
   "ShpConNum":number,
      /**  The primary contact for the related order.  */  
   "PrcConNum":number,
      /**  The name for the ship to location.  */  
   "ShipToName":string,
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
      @param tranDate
      @param tranTime
      @param tranNum
   */  
export interface DeleteByID_input{
   tranDate:string,
   tranTime:number,
   tranNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_CreditTranListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Transaction Date  */  
   TranDate:string,
      /**  Part of the unique key  */  
   TranTime:number,
      /**  Transaction Number  */  
   TranNum:number,
      /**  Transaction Type  */  
   TranType:string,
      /**  Transaction Total in base currency.  */  
   TranTotal:number,
      /**  Transaction Total in document currency.  */  
   DocTranTotal:number,
      /**  Processing company's Reference ID, unique to each transaction  */  
   PNRef:string,
      /**  Autherisation Code  */  
   AuthCode:string,
      /**  Error code returned by processing company  */  
   Result:string,
      /**  Response Message  */  
   ResponseMsg:string,
      /**  result of the address verification  */  
   AVSAddr:string,
      /**  Result of the address zip verification  */  
   AVSZip:string,
      /**  Result of the credit security code check  */  
   CSCMatch:string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   OrderNum:number,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   InvoiceNum:number,
      /**  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  A unique identifier for a specific credit card type assigned by the user.  */  
   CardType:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Transaction Type Description  */  
   TranTypeDesc:string,
      /**  The member's name on the credit card.  */  
   CardMemberName:string,
      /**  The expiration month of the credit card.  */  
   ExpMonth:number,
      /**  The expiration year of the credit card.  */  
   ExpYear:number,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   CardmemberReference:string,
      /**  The credit card account identifier.  */  
   CardNumber:string,
      /**  ST Link Address  */  
   StAddress:string,
      /**  The zip or postal code portion of the customer's main address.  */  
   Zip:string,
      /**  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  */  
   ReferencePNRef:string,
      /**  Flag to indicate that a prior process has used this authorization  */  
   AuthUsed:boolean,
      /**  Encrypted Credit Card Number  */  
   CardStore:string,
      /**  Freight Charges in base currency  */  
   Freight:number,
      /**  Freight Charges in document currency  */  
   DocFreight:number,
      /**  Tax amount in base currency.  */  
   Tax:number,
      /**  Tax amount in document currency.  */  
   DocTax:number,
      /**  Transaction Amount in base currency.  */  
   Amount:number,
      /**  Transaction Amount in document currency.  */  
   DocAmount:number,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   CustNum:number,
      /**  Reporting currency value of this field  */  
   Rpt1Amount:number,
      /**  Reporting currency value of this field  */  
   Rpt2Amount:number,
      /**  Reporting currency value of this field  */  
   Rpt3Amount:number,
      /**  Reporting currency value of this field  */  
   Rpt1Freight:number,
      /**  Reporting currency value of this field  */  
   Rpt2Freight:number,
      /**  Reporting currency value of this field  */  
   Rpt3Freight:number,
      /**  Reporting currency value of this field  */  
   Rpt1Tax:number,
      /**  Reporting currency value of this field  */  
   Rpt2Tax:number,
      /**  Reporting currency value of this field  */  
   Rpt3Tax:number,
      /**  Reporting currency value of this field  */  
   Rpt1TranTotal:number,
      /**  Reporting currency value of this field  */  
   Rpt2TranTotal:number,
      /**  Reporting currency value of this field  */  
   Rpt3TranTotal:number,
      /**  Userid of user who made the credit transaction  */  
   CreatedBy:string,
      /**  STLink Identifier  */  
   StrId:string,
      /**  Result of CVN checl  */  
   CVNCode:number,
      /**  SVN verification message  */  
   CVNMessage:string,
      /**  Referrer Code  */  
   ReferrerCode:string,
      /**  Order Number created by PaymentTrust if not supplied by process  */  
   PTOrderNum:string,
      /**  Authorisation Entity  */  
   AuthEntity:string,
      /**  Indicates if transaction was successful or not  */  
   TranSuccess:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CustomerName:string,
   ShipToNum:string,
   ShipToName:string,
      /**  The primary contact for the related order.  */  
   PrcConNum:number,
      /**  The shipping contact number for the order.  */  
   ShpConNum:number,
   CustID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CreditTranListTableset{
   CreditTranList:Erp_Tablesets_CreditTranListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CreditTranRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Transaction Date  */  
   TranDate:string,
      /**  Part of the unique key  */  
   TranTime:number,
      /**  Transaction Number  */  
   TranNum:number,
      /**  Transaction Type  */  
   TranType:string,
      /**  Transaction Total in base currency.  */  
   TranTotal:number,
      /**  Transaction Total in document currency.  */  
   DocTranTotal:number,
      /**  Processing company's Reference ID, unique to each transaction  */  
   PNRef:string,
      /**  Autherisation Code  */  
   AuthCode:string,
      /**  Error code returned by processing company  */  
   Result:string,
      /**  Response Message  */  
   ResponseMsg:string,
      /**  result of the address verification  */  
   AVSAddr:string,
      /**  Result of the address zip verification  */  
   AVSZip:string,
      /**  Result of the credit security code check  */  
   CSCMatch:string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   OrderNum:number,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   InvoiceNum:number,
      /**  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  A unique identifier for a specific credit card type assigned by the user.  */  
   CardType:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Transaction Type Description  */  
   TranTypeDesc:string,
      /**  The member's name on the credit card.  */  
   CardMemberName:string,
      /**  The expiration month of the credit card.  */  
   ExpMonth:number,
      /**  The expiration year of the credit card.  */  
   ExpYear:number,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   CardmemberReference:string,
      /**  The credit card account identifier.  */  
   CardNumber:string,
      /**  ST Link Address  */  
   StAddress:string,
      /**  The zip or postal code portion of the customer's main address.  */  
   Zip:string,
      /**  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  */  
   ReferencePNRef:string,
      /**  Flag to indicate that a prior process has used this authorization  */  
   AuthUsed:boolean,
      /**  Encrypted Credit Card Number  */  
   CardStore:string,
      /**  Freight Charges in base currency  */  
   Freight:number,
      /**  Freight Charges in document currency  */  
   DocFreight:number,
      /**  Tax amount in base currency.  */  
   Tax:number,
      /**  Tax amount in document currency.  */  
   DocTax:number,
      /**  Transaction Amount in base currency.  */  
   Amount:number,
      /**  Transaction Amount in document currency.  */  
   DocAmount:number,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   CustNum:number,
      /**  Reporting currency value of this field  */  
   Rpt1Amount:number,
      /**  Reporting currency value of this field  */  
   Rpt2Amount:number,
      /**  Reporting currency value of this field  */  
   Rpt3Amount:number,
      /**  Reporting currency value of this field  */  
   Rpt1Freight:number,
      /**  Reporting currency value of this field  */  
   Rpt2Freight:number,
      /**  Reporting currency value of this field  */  
   Rpt3Freight:number,
      /**  Reporting currency value of this field  */  
   Rpt1Tax:number,
      /**  Reporting currency value of this field  */  
   Rpt2Tax:number,
      /**  Reporting currency value of this field  */  
   Rpt3Tax:number,
      /**  Reporting currency value of this field  */  
   Rpt1TranTotal:number,
      /**  Reporting currency value of this field  */  
   Rpt2TranTotal:number,
      /**  Reporting currency value of this field  */  
   Rpt3TranTotal:number,
      /**  Userid of user who made the credit transaction  */  
   CreatedBy:string,
      /**  STLink Identifier  */  
   StrId:string,
      /**  Result of CVN checl  */  
   CVNCode:number,
      /**  SVN verification message  */  
   CVNMessage:string,
      /**  Referrer Code  */  
   ReferrerCode:string,
      /**  Order Number created by PaymentTrust if not supplied by process  */  
   PTOrderNum:string,
      /**  Authorisation Entity  */  
   AuthEntity:string,
      /**  Indicates if transaction was successful or not  */  
   TranSuccess:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CCCity  */  
   CCCity:string,
      /**  CCState  */  
   CCState:string,
      /**  FDMS Reference Data used in Deposit and Void transaction.  */  
   FDMSReferenceData:string,
      /**  Processor  */  
   Processor:string,
      /**  ISOCurrCode  */  
   ISOCurrCode:string,
      /**  The customer ID.  */  
   CustID:string,
      /**  The full name for customer.  */  
   CustomerName:string,
   ShipToNum:string,
      /**  The shipping contact number for the order.  */  
   ShpConNum:number,
      /**  The primary contact for the related order.  */  
   PrcConNum:number,
      /**  The name for the ship to location.  */  
   ShipToName:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CreditTranTableset{
   CreditTran:Erp_Tablesets_CreditTranRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtCreditTranTableset{
   CreditTran:Erp_Tablesets_CreditTranRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param tranDate
      @param tranTime
      @param tranNum
   */  
export interface GetByID_input{
   tranDate:string,
   tranTime:number,
   tranNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CreditTranTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CreditTranTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CreditTranTableset[],
}

   /** Required : 
      @param custNum
      @param currencyCode
   */  
export interface GetCardNumbers_input{
      /**  CustNum  */  
   custNum:number,
      /**  CurrencyCode  */  
   currencyCode:string,
}

export interface GetCardNumbers_output{
   returnObj:Erp_Tablesets_CreditTranListTableset[],
}

   /** Required : 
      @param whereClause
      @param custNum
      @param pageSize
      @param absolutePage
   */  
export interface GetListForApplyCreditMemo_input{
      /**  whereClause  */  
   whereClause:string,
   custNum:number,
   pageSize:number,
   absolutePage:number,
}

export interface GetListForApplyCreditMemo_output{
   returnObj:Erp_Tablesets_CreditTranListTableset[],
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
   returnObj:Erp_Tablesets_CreditTranListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param tranDate
      @param tranTime
   */  
export interface GetNewCreditTran_input{
   ds:Erp_Tablesets_CreditTranTableset[],
   tranDate:string,
   tranTime:number,
}

export interface GetNewCreditTran_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CreditTranTableset,
}
}

   /** Required : 
      @param whereClauseCreditTran
      @param whereClauseOrderHed
      @param contactName
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsContactTracker_input{
      /**  Where clause for HDCase table.  */  
   whereClauseCreditTran:string,
      /**  Where clause for OrderHed table.  */  
   whereClauseOrderHed:string,
      /**  The contact to return data for.  */  
   contactName:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsContactTracker_output{
   returnObj:Erp_Tablesets_CreditTranTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param WhereClause
      @param inGroupID
      @param inHeadNum
      @param inOrderNum
      @param inCardProcess
      @param PageSize
      @param AbsolutePage
   */  
export interface GetRowsForCreditCard_input{
      /**  The where clause.  */  
   WhereClause:string,
      /**  CashHead.GroupID field if available  */  
   inGroupID:string,
      /**  CashHead.HeadNum field if available  */  
   inHeadNum:number,
      /**  CashHead.OrderNum field if available  */  
   inOrderNum:number,
      /**  Encrypted Credit Card.  */  
   inCardProcess:string,
      /**  Page size.  */  
   PageSize:number,
      /**  Absolute page.  */  
   AbsolutePage:number,
}

export interface GetRowsForCreditCard_output{
   returnObj:Erp_Tablesets_CreditTranTableset[],
parameters : {
      /**  output parameters  */  
   MorePages:boolean,
}
}

   /** Required : 
      @param whereClauseCreditTran
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCreditTran:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CreditTranTableset[],
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
   ds:Erp_Tablesets_UpdExtCreditTranTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCreditTranTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CreditTranTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CreditTranTableset,
}
}

