import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.MaterialQueueSvc
// Description: Here are some brief notes regarding how to accomplish in Sonoma
the features found in the v6.10 Vantage program Material Request Queue.
            
1) The three tab folders each show Material Queue (MtlQueue) records.
1a) The Unselected tab dataset rows can be obtained with a call to
MaterialQueue.GetRows(), whereClauseMtlQueue = 'ttMtlQueue.SelectedByEmpID = ""'
            
1b) The My Selections tab dataset rows can be obtained with a call to
MaterialQueue.GetRows(), whereClauseMtlQueue = 'ttMtlQueue.SelectedByEmpID = {currentEmpId}'
            
1c) The Others Selections tab dataset rows can be obtained with a call to
MaterialQueue.GetRows(), whereClauseMtlQueue = 'ttMtlQueue.SelectedByEmpID < > ""
and ttMtlQueue.SelectedByEmpID < > {currentEmpId}'
2) The Select button should merely write the currentEmpId into ttMtlQueue.SelectedByEmpID
and then call MaterialQueue.Update().
            
3) The Deselect button should merely clear the ttMtlQueue.SelectedByEmpID and
then call MaterialQueue.Update().
            
4) The Delete button should merely call MaterialQueue.DeleteById().
            
5) The button with the bar-code image on it should call the MtlTag print routine.
I don't know what object and method(s) are involved, but there are many examples
throughout Sonoma.
            
6) The Process button is more complicated.  First, check the value of
ttMtlQueue.OkToProcess.  If that is false, disable the button.
Otherwise, you will need to look to ttMtlQueue.TranType to determine what
application to pop up for user entry:
When ttMtlQueue.TranType is MFG-STK, MFG-WIP or SVG-STK, you need to run
the Receipts From Manufacturing program.
When ttMtlQueue.TranType is anything else, you need to run
the Move Material program.
I think there is substantial work involved in setting up these calls--they
each use different datasets.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/$metadata", {
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
   Description: Get MaterialQueues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MaterialQueues
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MtlQueueRow
   */  
export function get_MaterialQueues(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MtlQueueRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/MaterialQueues", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MtlQueueRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MaterialQueues
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MtlQueueRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MtlQueueRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MaterialQueues(requestBody:Erp_Tablesets_MtlQueueRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/MaterialQueues", {
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
   Summary: Calls GetByID to retrieve the MaterialQueue item
   Description: Calls GetByID to retrieve the MaterialQueue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MaterialQueue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MtlQueueSeq Desc: MtlQueueSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MtlQueueRow
   */  
export function get_MaterialQueues_Company_MtlQueueSeq(Company:string, MtlQueueSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MtlQueueRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/MaterialQueues(" + Company + "," + MtlQueueSeq + ")", {
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
         resolve(data as Erp_Tablesets_MtlQueueRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MaterialQueue for the service
   Description: Calls UpdateExt to update MaterialQueue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MaterialQueue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MtlQueueSeq Desc: MtlQueueSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MtlQueueRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MaterialQueues_Company_MtlQueueSeq(Company:string, MtlQueueSeq:string, requestBody:Erp_Tablesets_MtlQueueRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/MaterialQueues(" + Company + "," + MtlQueueSeq + ")", {
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
   Summary: Call UpdateExt to delete MaterialQueue item
   Description: Call UpdateExt to delete MaterialQueue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MaterialQueue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MtlQueueSeq Desc: MtlQueueSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MaterialQueues_Company_MtlQueueSeq(Company:string, MtlQueueSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/MaterialQueues(" + Company + "," + MtlQueueSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MtlQueueListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MtlQueueListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MtlQueueListRow)
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
export function get_GetRows(whereClauseMtlQueue:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseMtlQueue!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMtlQueue=" + whereClauseMtlQueue
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/GetRows" + params, {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(mtlQueueSeq:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof mtlQueueSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "mtlQueueSeq=" + mtlQueueSeq
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/GetList" + params, {
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
   Summary: Invoke method AutoSelectTransactions
   Description: Retrieve material queue entry by company and by employee.
   OperationID: AutoSelectTransactions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AutoSelectTransactions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoSelectTransactions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AutoSelectTransactions(requestBody:AutoSelectTransactions_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AutoSelectTransactions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/AutoSelectTransactions", {
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
         resolve(data as AutoSelectTransactions_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMtlQueueByTranID
   Description: Retrieve material queue entry by company and by mtlQueueSeq.
   OperationID: GetMtlQueueByTranID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetMtlQueueByTranID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlQueueByTranID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMtlQueueByTranID(requestBody:GetMtlQueueByTranID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetMtlQueueByTranID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/GetMtlQueueByTranID", {
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
         resolve(data as GetMtlQueueByTranID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LockUnLockMtlQueForEmpID
   Description: Purpose:     Called by handheld (where Employee ID is entered and available on client)
Notes:
<param name="ipTranStatus">Transaction status</param><param name="ipMtlQueueSeq">Material Queue Sequence</param><param name="ipEmpID">Employee ID</param><param name="ds">The MaterialQueueDataSet.</param>
   OperationID: LockUnLockMtlQueForEmpID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LockUnLockMtlQueForEmpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockUnLockMtlQueForEmpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LockUnLockMtlQueForEmpID(requestBody:LockUnLockMtlQueForEmpID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LockUnLockMtlQueForEmpID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/LockUnLockMtlQueForEmpID", {
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
         resolve(data as LockUnLockMtlQueForEmpID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LockUnLockMtlQue
   Description: Purpose:     Called from the full client (where Employee ID has not been entered; must use ID associated with login)
Notes:
<param name="ipTranStatus">Transaction status</param><param name="ipMtlQueueSeq">Material Queue Sequence</param><param name="ds">The MaterialQueueDataSet.</param>
   OperationID: LockUnLockMtlQue
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LockUnLockMtlQue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockUnLockMtlQue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LockUnLockMtlQue(requestBody:LockUnLockMtlQue_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LockUnLockMtlQue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/LockUnLockMtlQue", {
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
         resolve(data as LockUnLockMtlQue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaultFilterSettings
   Description: Returns the PlantConfCtrl filter settings for the current company / plant
   OperationID: GetDefaultFilterSettings
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultFilterSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultFilterSettings(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDefaultFilterSettings_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/GetDefaultFilterSettings", {
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
         resolve(data as GetDefaultFilterSettings_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnlockAutoSelectTransactions
   Description: UnLockAutoSelectTransactions.
   OperationID: UnlockAutoSelectTransactions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UnlockAutoSelectTransactions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlockAutoSelectTransactions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnlockAutoSelectTransactions(requestBody:UnlockAutoSelectTransactions_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UnlockAutoSelectTransactions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/UnlockAutoSelectTransactions", {
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
         resolve(data as UnlockAutoSelectTransactions_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SortQueueByPriority
   Description: Return a flag to know if the records will be sorted by the PlantConfCtrl.SortQueuebyPriority filed
   OperationID: SortQueueByPriority
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/SortQueueByPriority_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SortQueueByPriority(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SortQueueByPriority_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/SortQueueByPriority", {
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
         resolve(data as SortQueueByPriority_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VerifyMtlQueueExists
   Description: VerifyMtlQueueExists - Returns true if MtlQueue still exists
   OperationID: VerifyMtlQueueExists
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/VerifyMtlQueueExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifyMtlQueueExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VerifyMtlQueueExists(requestBody:VerifyMtlQueueExists_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<VerifyMtlQueueExists_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/VerifyMtlQueueExists", {
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
         resolve(data as VerifyMtlQueueExists_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsCustom
   Description: GetRowsCustom
   OperationID: Get_GetRowsCustom
      @param delimitedFilterString Desc: Format is [FieldName]Value~[FieldName]Value~   Required: True   Allow empty value : True
      @param recordsPerPage Desc: Records per page or 0 for all rows   Required: True
      @param pageNum Desc: Page number defaults to page 1 if not specified   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRowsCustom(delimitedFilterString:string, recordsPerPage:string, pageNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof delimitedFilterString!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "delimitedFilterString=" + delimitedFilterString
   }
   if(typeof recordsPerPage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "recordsPerPage=" + recordsPerPage
   }
   if(typeof pageNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageNum=" + pageNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsCustom_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/GetRowsCustom" + params, {
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
         resolve(data as GetRowsCustom_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsCustomParams
   Description: GetRowsCustomParams
   OperationID: Get_GetRowsCustomParams
      @param whereClause Desc: Where Clause   Required: True   Allow empty value : True
      @param fromDate Desc: From Date   Required: True   Allow empty value : True
      @param toDate Desc: To Date   Required: True   Allow empty value : True
      @param fromWhse Desc: From Warehouse   Required: True   Allow empty value : True
      @param toWhse Desc: To Warehouse   Required: True   Allow empty value : True
      @param tranType Desc: TranType   Required: True   Allow empty value : True
      @param selectedByEmpID Desc: Select by emp ID   Required: True   Allow empty value : True
      @param excludeTransStatus Desc: Exclude tran status   Required: True   Allow empty value : True
      @param onlySelectedByEmp Desc: Only return rows selected by employee   Required: True
      @param onlyUnselected Desc: Only sreturn rows not selected by any employee   Required: True
      @param pageSize Desc: Page Size   Required: True
      @param absolutePage Desc: Absolute Page   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRowsCustomParams(whereClause:string, fromDate:string, toDate:string, fromWhse:string, toWhse:string, tranType:string, selectedByEmpID:string, excludeTransStatus:string, onlySelectedByEmp:string, onlyUnselected:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
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
   if(typeof fromDate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "fromDate=" + fromDate
   }
   if(typeof toDate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "toDate=" + toDate
   }
   if(typeof fromWhse!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "fromWhse=" + fromWhse
   }
   if(typeof toWhse!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "toWhse=" + toWhse
   }
   if(typeof tranType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tranType=" + tranType
   }
   if(typeof selectedByEmpID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "selectedByEmpID=" + selectedByEmpID
   }
   if(typeof excludeTransStatus!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "excludeTransStatus=" + excludeTransStatus
   }
   if(typeof onlySelectedByEmp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "onlySelectedByEmp=" + onlySelectedByEmp
   }
   if(typeof onlyUnselected!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "onlyUnselected=" + onlyUnselected
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

   return (new Promise<GetRowsCustomParams_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/GetRowsCustomParams" + params, {
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
         resolve(data as GetRowsCustomParams_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPCIDPrintParams
   Description: GetPCIDPrintParams - returns the number of labels, and report style information for the mtl queue PCID print
   OperationID: GetPCIDPrintParams
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPCIDPrintParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPCIDPrintParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPCIDPrintParams(requestBody:GetPCIDPrintParams_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPCIDPrintParams_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/GetPCIDPrintParams", {
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
         resolve(data as GetPCIDPrintParams_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPkgControlIDGenParams
   OperationID: GetPkgControlIDGenParams
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPkgControlIDGenParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPkgControlIDGenParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPkgControlIDGenParams(requestBody:GetPkgControlIDGenParams_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPkgControlIDGenParams_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/GetPkgControlIDGenParams", {
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
         resolve(data as GetPkgControlIDGenParams_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetParametersForMtlTags
   Description: Returns the string required to call the Print Mtl Tags UI
   OperationID: GetParametersForMtlTags
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetParametersForMtlTags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetParametersForMtlTags_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetParametersForMtlTags(requestBody:GetParametersForMtlTags_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetParametersForMtlTags_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/GetParametersForMtlTags", {
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
         resolve(data as GetParametersForMtlTags_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSelectedMtlQueueList
   Description: Returns a delimited list of selected material queue records
   OperationID: GetSelectedMtlQueueList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSelectedMtlQueueList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectedMtlQueueList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectedMtlQueueList(requestBody:GetSelectedMtlQueueList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSelectedMtlQueueList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/GetSelectedMtlQueueList", {
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
         resolve(data as GetSelectedMtlQueueList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDeleteConfirmationMessage
   Description: Returns a delete message that includes the list of MtlQueue records to be deleted
   OperationID: GetDeleteConfirmationMessage
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDeleteConfirmationMessage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDeleteConfirmationMessage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDeleteConfirmationMessage(requestBody:GetDeleteConfirmationMessage_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDeleteConfirmationMessage_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/GetDeleteConfirmationMessage", {
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
         resolve(data as GetDeleteConfirmationMessage_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaultToDate
   Description: Returns the default to date
   OperationID: GetDefaultToDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultToDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultToDate(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDefaultToDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/GetDefaultToDate", {
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
         resolve(data as GetDefaultToDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMtlQueue
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMtlQueue
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMtlQueue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMtlQueue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMtlQueue(requestBody:GetNewMtlQueue_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMtlQueue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/GetNewMtlQueue", {
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
         resolve(data as GetNewMtlQueue_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MtlQueueListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MtlQueueListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MtlQueueRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MtlQueueRow,
}

export interface Erp_Tablesets_MtlQueueListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  System date at time that record was created.  */  
   "SysDate":string,
      /**  System Time(seconds since midnight) when transaction was created.  */  
   "SysTime":number,
      /**  Number assigned by the system to uniquely identify the record.  Created by using the database sequence "MtlQueueSeq".  */  
   "MtlQueueSeq":number,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Part Number of item in the container.  */  
   "PartNum":string,
      /**  Quantity  */  
   "Quantity":number,
      /**   Internal flag to indicate the type of transaction that this request is for.  This will control which functions are invoked for processing.
The same codes as in PartTran are used.  However, there are some additional codes also. 
They are; GET-WIP,  RTN-WIP, RTN-MTL, PUT-MTL, PUT-WIP, PICK-SO, PICK-JOB, PICK-TFO, BIN-REPLENISH, BIN-CONSOLIDATE, PICK-SO-XDOCK, PICK-JOB-XDOCK, PICK-TFO-XDOCK  */  
   "TranType":string,
      /**   Used as a translatable prefix for the Reference field.
For example for a purchase receipt of stock it has "PS", (Packing Slip). For display purposes this is field is translated, then concatenated with the value in the Refernce field. 
Other values are "Job",  */  
   "ReferencePrefix":string,
      /**  Contains a reference about the request. May contain Job/Asm/Seq, WrkCtr,  Packing Slip #,  Sales Order, etc...depending on the TranType.  */  
   "Reference":string,
      /**  Employee ID that made the request.  */  
   "RequestedByEmpID":string,
      /**  Employee ID that has selected this record from the queue for processing.  */  
   "SelectedByEmpID":string,
      /**  Job Number that the request is related to.  This allows sorting by Job, which provides the user a method of working on all the requests for a specific job.  */  
   "JobNum":string,
      /**  Job Assembly Sequence.  */  
   "AssemblySeq":number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "O" = Job Operation (JobOper).  */  
   "JobSeqType":string,
      /**  Seq # of the related specific material or operation record.  For WIP parts it's the operation sequence that created the part. For raw materials it's the related JobMtl.MtlSeq.  */  
   "JobSeq":number,
      /**  Warehouse Code where item is to be found. For example a Get Raw Material request of a stocked part  would be the warehouse  the requirement was allocated against (JobMtl.WareHouseCode).  A "Move of a WIP part" will contain the Warehouse defined by the WrkCenter.PutWhse...  */  
   "FromWhse":string,
      /**  Warehouse bin where item is to be found. For example a Get Raw Material request of a stocked part  would be the Primary Bin of the part/warehouse, if no primary bin, then the first Bin in the warehouse which contains this part, else blank.  A "Move of a WIP part" will contain the bin defined by the WrkCenter.PutBin...  */  
   "FromBinNum":string,
      /**  Warehouse where item should be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputWhse).  */  
   "ToWhse":string,
      /**  Warehouse bin where item is to be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputBin).  */  
   "ToBinNum":string,
      /**  Assembly sequence of the operation that completed quantity of the job operation  will be moved to.  */  
   "NextAssemblySeq":number,
      /**  Sequence of the operation that completed quantity of the job operation will be moved to.  */  
   "NextJobSeq":number,
      /**  Date the this request is needed by.  Defaults, to current system date.  */  
   "NeedByDate":string,
      /**  Time (seconds since midnight) that request is need by.  */  
   "NeedByTime":number,
      /**  Vendor number of the related purchase receipt (RcvDtl).  Company,VendorNum, PurPoint, PackSlip,Packline are used to provide the link to the related RcvDtl record.  */  
   "VendorNum":number,
      /**  Vendor purchase point id of the related purchase receipt (RcvDtl).  */  
   "PurPoint":string,
      /**  Vendors Packing Slip # of the related RcvDtl.  */  
   "PackSlip":string,
      /**  Vendors Packing Slip line  # of the related RcvDtl.  */  
   "PackLine":number,
      /**   Order number job is making parts for. (See JobProd.OrderNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

OrderNum pertains only to "make to order" requirements.  
Provides relationship to the JobProd for "make to order" requirements.  */  
   "OrderNum":number,
      /**  Related Sales order line number.  */  
   "OrderLine":number,
      /**  Related sales order release number.  */  
   "OrderRelNum":number,
      /**   Job that this job is making parts for. (See JobProd.TargetJobNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

TargetJobNum pertains only to "make to job" requirements.  
Provides relationship to the JobProd for "make to Job" requirements.  */  
   "TargetJobNum":string,
      /**  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  */  
   "TargetAssemblySeq":number,
      /**  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  */  
   "TargetMtlSeq":number,
      /**  Part Revision number  */  
   "RevisionNum":string,
      /**  A description of the Part.  */  
   "PartDescription":string,
      /**  Internal unit of measure.  */  
   "IUM":string,
      /**  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  */  
   "PONum":number,
      /**  The PO line # which is being received. Only applicable for PO receipt transactions.  */  
   "POLine":number,
      /**  Purchase Order Release # which is being received.  */  
   "PORelNum":number,
      /**  Indicates if this MtlQueue is visible to the user on the Material Queue browse.  Set based on the users response to make a "move  request" when reporting quantities.  Set to true visible), if a move request is made.  This was implemented to keep track of labor quantity reported without making a move request.  The move request will then reflect the total quantity to move instead of what was reported on the labor transaction that requested the move.  Regardless of making a "Move Request" labor quantity reporting always creates/updates a MtlQueue record.  */  
   "Visible":boolean,
      /**  Return Material Authorization number of related RMAHead.  */  
   "RMANum":number,
      /**  Line number of the related RMADtl record.  */  
   "RMALine":number,
      /**  RMAReceipt number of the related RMARcpt record.  */  
   "RMAReceipt":number,
      /**  RMADisp number of the related RMADisp record.  */  
   "RMADisp":number,
      /**  The related NonConf.TranID number. Used to link the MtlQueue table to the NonConf table.  */  
   "NCTranID":number,
      /**  Lot Number of the part.  */  
   "LotNum":string,
      /**  Indicates this record has been locked by a Advanced Shipping user and is not available for processing by any other user.  */  
   "Lock":boolean,
      /**  Used by Advanced Shipping to designate which queue this record is in.  Advanced Shipping queues can prioritize and process records.  */  
   "QueueID":string,
      /**  Sequence of this record within an Advanced Shipping Queue.  */  
   "QueuePickSeq":number,
      /**  This is an internal sequence number for grouping MtlQueue records.  */  
   "ReleaseForPickingSeq":number,
      /**  Warehouse Group that was assigned to this transaction.  */  
   "WhseGroupCode":string,
      /**   The status of the transaction of the material.  Valid values:
MGMT-LOCK - Manager locked, RELEASED - Released, HOLD - On Hold, USER-LOCK - Locked for a user, ORDER-HOLD - On Hold for Order Based Picking, QUALITY-HOLD - On Hold for Quality Control, and PICK-PACK - Three step allocation Pick-Pack Method  */  
   "TranStatus":string,
      /**  The Wave that was assigned during the allocation process.  */  
   "WaveNum":number,
      /**  Transaction Priority.  Valid values are 1,2,3,4,5,6,7,8,9.  One is the highest priority.  */  
   "Priority":number,
      /**  Transaction Source  */  
   "TranSource":string,
      /**  When the TranStatus, AssignedToEmpID or Priority are modified, this value is updated with the ID of the Manager making the change.  */  
   "LastMgrChangeEmpID":string,
      /**  Employee ID that was selected by the Warehouse Manager to process record from the queue.  */  
   "AssignedToEmpID":string,
      /**  Transfer Order for which Demand is being satisfied.  */  
   "TargetTFOrdNum":string,
      /**  Transfer Order Line for which Demand is being satisfied.  */  
   "TargetTFOrdLine":number,
      /**  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  */  
   "PackStation":string,
      /**  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  */  
   "DistributionType":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Holds the result of checking sub-menu security.  NO indicates the current user does not have permission to carry out the indicated TranType.  */  
   "OkToProcess":boolean,
   "RequestedByEmpName":string,
   "SelectedByEmpName":string,
   "NeedByTimeDisp":string,
      /**  Is this material queue row part of the employees warehouse group  */  
   "SameWhseGroupEmp":boolean,
      /**  Sort priority from highest to lowest (1,2,3,4,5,6,7,8,9,0)  */  
   "SortByPriority":number,
      /**  Value is true if this mtlqueue record is related to a wave. False if it is not.  */  
   "WaveRelated":boolean,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   "AssemblySeqDescription":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "JobNumPartDescription":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "OrderLineLineDesc":string,
      /**  The member's name on the credit card.  */  
   "OrderNumCardMemberName":string,
      /**  A unique code that identifies the currency.  */  
   "OrderNumCurrencyCode":string,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartNumTrackLots":boolean,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartNumSalesUM":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartNumSellingFactor":number,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
      /**  Indicates if this part is serial number tracked  */  
   "PartNumTrackSerialNum":boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  OUR internal Part number for this item.  */  
   "POLinePartNum":string,
      /**  Supplier Part Number  */  
   "POLineVenPartNum":string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   "POLineLineDesc":string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   "PORelNumRefCodeDesc":string,
      /**  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  */  
   "RMALineLineDesc":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorNumCountry":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorNumName":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorNumVendorID":string,
      /**  Third address line of the Supplier  */  
   "VendorNumAddress3":string,
      /**  A unique code that identifies the currency.  */  
   "VendorNumCurrencyCode":string,
      /**  Can be blank.  */  
   "VendorNumState":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNumZIP":string,
      /**  First address line of the Supplier  */  
   "VendorNumAddress1":string,
      /**  City portion of the address of the Supplier  */  
   "VendorNumCity":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNumDefaultFOB":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
      /**  Second address line of the Supplier  */  
   "VendorNumAddress2":string,
      /**  Warehouse Group Description.  */  
   "WarehouseGroupCodeWhseGroupDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MtlQueueRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  System date at time that record was created.  */  
   "SysDate":string,
      /**  System Time(seconds since midnight) when transaction was created.  */  
   "SysTime":number,
      /**  Number assigned by the system to uniquely identify the record.  Created by using the database sequence "MtlQueueSeq".  */  
   "MtlQueueSeq":number,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Part Number of item in the container.  */  
   "PartNum":string,
      /**  Quantity  */  
   "Quantity":number,
      /**   Internal flag to indicate the type of transaction that this request is for.  This will control which functions are invoked for processing.
The same codes as in PartTran are used.  However, there are some additional codes also. 
They are; GET-WIP,  RTN-WIP, RTN-MTL, PUT-MTL, PUT-WIP, PICK-SO, PICK-JOB, PICK-TFO, BIN-REPLENISH, BIN-CONSOLIDATE, PICK-SO-XDOCK, PICK-JOB-XDOCK, PICK-TFO-XDOCK  */  
   "TranType":string,
      /**   Used as a translatable prefix for the Reference field.
For example for a purchase receipt of stock it has "PS", (Packing Slip). For display purposes this is field is translated, then concatenated with the value in the Refernce field. 
Other values are "Job",  */  
   "ReferencePrefix":string,
      /**  Contains a reference about the request. May contain Job/Asm/Seq, WrkCtr,  Packing Slip #,  Sales Order, etc...depending on the TranType.  */  
   "Reference":string,
      /**  Employee ID that made the request.  */  
   "RequestedByEmpID":string,
      /**  Employee ID that has selected this record from the queue for processing.  */  
   "SelectedByEmpID":string,
      /**  Job Number that the request is related to.  This allows sorting by Job, which provides the user a method of working on all the requests for a specific job.  */  
   "JobNum":string,
      /**  Job Assembly Sequence.  */  
   "AssemblySeq":number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "O" = Job Operation (JobOper).  */  
   "JobSeqType":string,
      /**  Seq # of the related specific material or operation record.  For WIP parts it's the operation sequence that created the part. For raw materials it's the related JobMtl.MtlSeq.  */  
   "JobSeq":number,
      /**  Warehouse Code where item is to be found. For example a Get Raw Material request of a stocked part  would be the warehouse  the requirement was allocated against (JobMtl.WareHouseCode).  A "Move of a WIP part" will contain the Warehouse defined by the WrkCenter.PutWhse...  */  
   "FromWhse":string,
      /**  Warehouse bin where item is to be found. For example a Get Raw Material request of a stocked part  would be the Primary Bin of the part/warehouse, if no primary bin, then the first Bin in the warehouse which contains this part, else blank.  A "Move of a WIP part" will contain the bin defined by the WrkCenter.PutBin...  */  
   "FromBinNum":string,
      /**  Warehouse where item should be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputWhse).  */  
   "ToWhse":string,
      /**  Warehouse bin where item is to be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputBin).  */  
   "ToBinNum":string,
      /**  Assembly sequence of the operation that completed quantity of the job operation  will be moved to.  */  
   "NextAssemblySeq":number,
      /**  Sequence of the operation that completed quantity of the job operation will be moved to.  */  
   "NextJobSeq":number,
      /**  Date the this request is needed by.  Defaults, to current system date.  */  
   "NeedByDate":string,
      /**  Time (seconds since midnight) that request is need by.  */  
   "NeedByTime":number,
      /**  Vendor number of the related purchase receipt (RcvDtl).  Company,VendorNum, PurPoint, PackSlip,Packline are used to provide the link to the related RcvDtl record.  */  
   "VendorNum":number,
      /**  Vendor purchase point id of the related purchase receipt (RcvDtl).  */  
   "PurPoint":string,
      /**  Vendors Packing Slip # of the related RcvDtl.  */  
   "PackSlip":string,
      /**  Vendors Packing Slip line  # of the related RcvDtl.  */  
   "PackLine":number,
      /**   Order number job is making parts for. (See JobProd.OrderNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

OrderNum pertains only to "make to order" requirements.  
Provides relationship to the JobProd for "make to order" requirements.  */  
   "OrderNum":number,
      /**  Related Sales order line number.  */  
   "OrderLine":number,
      /**  Related sales order release number.  */  
   "OrderRelNum":number,
      /**   Job that this job is making parts for. (See JobProd.TargetJobNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

TargetJobNum pertains only to "make to job" requirements.  
Provides relationship to the JobProd for "make to Job" requirements.  */  
   "TargetJobNum":string,
      /**  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  */  
   "TargetAssemblySeq":number,
      /**  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  */  
   "TargetMtlSeq":number,
      /**  Part Revision number  */  
   "RevisionNum":string,
      /**  A description of the Part.  */  
   "PartDescription":string,
      /**  Internal unit of measure.  */  
   "IUM":string,
      /**  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  */  
   "PONum":number,
      /**  The PO line # which is being received. Only applicable for PO receipt transactions.  */  
   "POLine":number,
      /**  Purchase Order Release # which is being received.  */  
   "PORelNum":number,
      /**  Indicates if this MtlQueue is visible to the user on the Material Queue browse.  Set based on the users response to make a "move  request" when reporting quantities.  Set to true visible), if a move request is made.  This was implemented to keep track of labor quantity reported without making a move request.  The move request will then reflect the total quantity to move instead of what was reported on the labor transaction that requested the move.  Regardless of making a "Move Request" labor quantity reporting always creates/updates a MtlQueue record.  */  
   "Visible":boolean,
      /**  Return Material Authorization number of related RMAHead.  */  
   "RMANum":number,
      /**  Line number of the related RMADtl record.  */  
   "RMALine":number,
      /**  RMAReceipt number of the related RMARcpt record.  */  
   "RMAReceipt":number,
      /**  RMADisp number of the related RMADisp record.  */  
   "RMADisp":number,
      /**  The related NonConf.TranID number. Used to link the MtlQueue table to the NonConf table.  */  
   "NCTranID":number,
      /**  Lot Number of the part.  */  
   "LotNum":string,
      /**  Indicates this record has been locked by a Advanced Shipping user and is not available for processing by any other user.  */  
   "Lock":boolean,
      /**  Used by Advanced Shipping to designate which queue this record is in.  Advanced Shipping queues can prioritize and process records.  */  
   "QueueID":string,
      /**  Sequence of this record within an Advanced Shipping Queue.  */  
   "QueuePickSeq":number,
      /**  This is an internal sequence number for grouping MtlQueue records.  */  
   "ReleaseForPickingSeq":number,
      /**  Warehouse Group that was assigned to this transaction.  */  
   "WhseGroupCode":string,
      /**   The status of the transaction of the material.  Valid values:
MGMT-LOCK - Manager locked, RELEASED - Released, HOLD - On Hold, USER-LOCK - Locked for a user, ORDER-HOLD - On Hold for Order Based Picking, QUALITY-HOLD - On Hold for Quality Control, and PICK-PACK - Three step allocation Pick-Pack Method  */  
   "TranStatus":string,
      /**  The Wave that was assigned during the allocation process.  */  
   "WaveNum":number,
      /**  Transaction Priority.  Valid values are 1,2,3,4,5,6,7,8,9.  One is the highest priority.  */  
   "Priority":number,
      /**  Transaction Source  */  
   "TranSource":string,
      /**  When the TranStatus, AssignedToEmpID or Priority are modified, this value is updated with the ID of the Manager making the change.  */  
   "LastMgrChangeEmpID":string,
      /**  Employee ID that was selected by the Warehouse Manager to process record from the queue.  */  
   "AssignedToEmpID":string,
      /**  Transfer Order for which Demand is being satisfied.  */  
   "TargetTFOrdNum":string,
      /**  Transfer Order Line for which Demand is being satisfied.  */  
   "TargetTFOrdLine":number,
      /**  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  */  
   "PackStation":string,
      /**  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  */  
   "DistributionType":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Package Control Identification Number  */  
   "PCID":string,
      /**  Related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  Last Used PCID on the selected line.  */  
   "LastUsedPCID":string,
      /**  The PCID from which the material movement will occur.  */  
   "FromPCID":string,
      /**  The PCID to which the material movement will occur.  */  
   "ToPCID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  AttributeValueSeq  */  
   "AttributeValueSeq":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
   "CustID":string,
   "CustTerritoryID":string,
      /**  Indicates whether Transfer Order Selector Flag should be disabled.  */  
   "DisableTO":boolean,
      /**  From Inventory Selector Flag  */  
   "FromInv":boolean,
      /**  From Manufacturing Selector Flag  */  
   "FromJob":boolean,
      /**  From Purchasing Selector Flag  */  
   "FromPO":boolean,
      /**  From Transfer Order Selector Flag  */  
   "FromTO":boolean,
   "FromWhseDesc":string,
      /**  Service Order Number from FSA. Only available in FSA Request Workbench.  */  
   "FSAServiceOrderNumber":number,
      /**  Service Order Resource Num from FSA. Only available in FSA Request Workbench.  */  
   "FSAServiceOrderResourceNum":number,
   "HoldStatus":boolean,
   "LeadTime":number,
   "MaxMfgLotSize":number,
   "MfgLeadTime":number,
   "MinMfgLotSize":number,
   "NeedByTimeDisp":string,
   "NonStock":boolean,
      /**  Holds the result of checking sub-menu security.  NO indicates the current user does not have permission to carry out the indicated TranType.  */  
   "OkToProcess":boolean,
   "OnHandQtySite":number,
   "OnHandQtyWhse":number,
   "PlantName":string,
   "PrimWhseCode":string,
   "PrimWhseDesc":string,
   "RequestedByEmpName":string,
      /**  Indicates whether an error occured in processing.  */  
   "RequestError":boolean,
      /**  Message used to return status information after processing.  */  
   "RequestMsg":string,
      /**  Is this material queue row part of the employees warehouse group  */  
   "SameWhseGroupEmp":boolean,
   "SelectedByEmpName":string,
      /**  Used by user to select rows for mass processing  */  
   "SelectedForProcessing":boolean,
   "ShipToCity":string,
   "ShipToCountry":string,
      /**  Customer Ship To Name  */  
   "ShipToName":string,
   "ShipToNum":string,
   "ShipToState":string,
   "ShipToZIP":string,
      /**  Sort priority from highest to lowest (1,2,3,4,5,6,7,8,9,0)  */  
   "SortByPriority":number,
      /**  Transfer, Sales Kit, Manufactured or Purchased.  */  
   "SourceTypeDesc":string,
   "ToWhseDesc":string,
   "TransferLeadTime":number,
   "TransferPlant":string,
      /**  Readable tran type (used in Replenishment Workbench)  */  
   "TranTypeDesc":string,
   "VendorNumName":string,
   "VendorNumVendorID":string,
      /**  Value is true if this mtlqueue record is related to a wave. False if it is not.  */  
   "WaveRelated":boolean,
      /**  Customer Sales Territory Region Code  */  
   "CustRegionCode":string,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  Display (decimal) number of pieces for inventory tracked parts.  */  
   "DispNumberOfPieces":number,
   "BitFlag":number,
   "AssemblySeqDescription":string,
   "JobNumPartDescription":string,
   "OrderLineLineDesc":string,
   "OrderNumCurrencyCode":string,
   "OrderNumCardMemberName":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumSalesUM":string,
   "PartNumPartDescription":string,
   "PartNumTrackLots":boolean,
   "PartNumPricePerCode":string,
   "PartNumSellingFactor":number,
   "PartNumIUM":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumAttrClassID":string,
   "POLinePartNum":string,
   "POLineVenPartNum":string,
   "POLineLineDesc":string,
   "RMALineLineDesc":string,
   "VendorNumAddress1":string,
   "VendorNumCity":string,
   "VendorNumAddress3":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCurrencyCode":string,
   "VendorNumTermsCode":string,
   "VendorNumCountry":string,
   "VendorNumVendorID_":string,
   "VendorNumState":string,
   "VendorNumZIP":string,
   "VendorNumName_":string,
   "VendorNumAddress2":string,
   "WarehouseGroupCodeWhseGroupDesc":string,
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
      @param ipEmpID
   */  
export interface AutoSelectTransactions_input{
      /**  Employee ID  */  
   ipEmpID:string,
}

export interface AutoSelectTransactions_output{
   returnObj:Erp_Tablesets_MaterialQueueTableset[],
}

   /** Required : 
      @param mtlQueueSeq
   */  
export interface DeleteByID_input{
   mtlQueueSeq:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_MaterialQueueTableset{
   MtlQueue:Erp_Tablesets_MtlQueueRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MtlQueueListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time(seconds since midnight) when transaction was created.  */  
   SysTime:number,
      /**  Number assigned by the system to uniquely identify the record.  Created by using the database sequence "MtlQueueSeq".  */  
   MtlQueueSeq:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Part Number of item in the container.  */  
   PartNum:string,
      /**  Quantity  */  
   Quantity:number,
      /**   Internal flag to indicate the type of transaction that this request is for.  This will control which functions are invoked for processing.
The same codes as in PartTran are used.  However, there are some additional codes also. 
They are; GET-WIP,  RTN-WIP, RTN-MTL, PUT-MTL, PUT-WIP, PICK-SO, PICK-JOB, PICK-TFO, BIN-REPLENISH, BIN-CONSOLIDATE, PICK-SO-XDOCK, PICK-JOB-XDOCK, PICK-TFO-XDOCK  */  
   TranType:string,
      /**   Used as a translatable prefix for the Reference field.
For example for a purchase receipt of stock it has "PS", (Packing Slip). For display purposes this is field is translated, then concatenated with the value in the Refernce field. 
Other values are "Job",  */  
   ReferencePrefix:string,
      /**  Contains a reference about the request. May contain Job/Asm/Seq, WrkCtr,  Packing Slip #,  Sales Order, etc...depending on the TranType.  */  
   Reference:string,
      /**  Employee ID that made the request.  */  
   RequestedByEmpID:string,
      /**  Employee ID that has selected this record from the queue for processing.  */  
   SelectedByEmpID:string,
      /**  Job Number that the request is related to.  This allows sorting by Job, which provides the user a method of working on all the requests for a specific job.  */  
   JobNum:string,
      /**  Job Assembly Sequence.  */  
   AssemblySeq:number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "O" = Job Operation (JobOper).  */  
   JobSeqType:string,
      /**  Seq # of the related specific material or operation record.  For WIP parts it's the operation sequence that created the part. For raw materials it's the related JobMtl.MtlSeq.  */  
   JobSeq:number,
      /**  Warehouse Code where item is to be found. For example a Get Raw Material request of a stocked part  would be the warehouse  the requirement was allocated against (JobMtl.WareHouseCode).  A "Move of a WIP part" will contain the Warehouse defined by the WrkCenter.PutWhse...  */  
   FromWhse:string,
      /**  Warehouse bin where item is to be found. For example a Get Raw Material request of a stocked part  would be the Primary Bin of the part/warehouse, if no primary bin, then the first Bin in the warehouse which contains this part, else blank.  A "Move of a WIP part" will contain the bin defined by the WrkCenter.PutBin...  */  
   FromBinNum:string,
      /**  Warehouse where item should be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputWhse).  */  
   ToWhse:string,
      /**  Warehouse bin where item is to be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputBin).  */  
   ToBinNum:string,
      /**  Assembly sequence of the operation that completed quantity of the job operation  will be moved to.  */  
   NextAssemblySeq:number,
      /**  Sequence of the operation that completed quantity of the job operation will be moved to.  */  
   NextJobSeq:number,
      /**  Date the this request is needed by.  Defaults, to current system date.  */  
   NeedByDate:string,
      /**  Time (seconds since midnight) that request is need by.  */  
   NeedByTime:number,
      /**  Vendor number of the related purchase receipt (RcvDtl).  Company,VendorNum, PurPoint, PackSlip,Packline are used to provide the link to the related RcvDtl record.  */  
   VendorNum:number,
      /**  Vendor purchase point id of the related purchase receipt (RcvDtl).  */  
   PurPoint:string,
      /**  Vendors Packing Slip # of the related RcvDtl.  */  
   PackSlip:string,
      /**  Vendors Packing Slip line  # of the related RcvDtl.  */  
   PackLine:number,
      /**   Order number job is making parts for. (See JobProd.OrderNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

OrderNum pertains only to "make to order" requirements.  
Provides relationship to the JobProd for "make to order" requirements.  */  
   OrderNum:number,
      /**  Related Sales order line number.  */  
   OrderLine:number,
      /**  Related sales order release number.  */  
   OrderRelNum:number,
      /**   Job that this job is making parts for. (See JobProd.TargetJobNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

TargetJobNum pertains only to "make to job" requirements.  
Provides relationship to the JobProd for "make to Job" requirements.  */  
   TargetJobNum:string,
      /**  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  */  
   TargetAssemblySeq:number,
      /**  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  */  
   TargetMtlSeq:number,
      /**  Part Revision number  */  
   RevisionNum:string,
      /**  A description of the Part.  */  
   PartDescription:string,
      /**  Internal unit of measure.  */  
   IUM:string,
      /**  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  */  
   PONum:number,
      /**  The PO line # which is being received. Only applicable for PO receipt transactions.  */  
   POLine:number,
      /**  Purchase Order Release # which is being received.  */  
   PORelNum:number,
      /**  Indicates if this MtlQueue is visible to the user on the Material Queue browse.  Set based on the users response to make a "move  request" when reporting quantities.  Set to true visible), if a move request is made.  This was implemented to keep track of labor quantity reported without making a move request.  The move request will then reflect the total quantity to move instead of what was reported on the labor transaction that requested the move.  Regardless of making a "Move Request" labor quantity reporting always creates/updates a MtlQueue record.  */  
   Visible:boolean,
      /**  Return Material Authorization number of related RMAHead.  */  
   RMANum:number,
      /**  Line number of the related RMADtl record.  */  
   RMALine:number,
      /**  RMAReceipt number of the related RMARcpt record.  */  
   RMAReceipt:number,
      /**  RMADisp number of the related RMADisp record.  */  
   RMADisp:number,
      /**  The related NonConf.TranID number. Used to link the MtlQueue table to the NonConf table.  */  
   NCTranID:number,
      /**  Lot Number of the part.  */  
   LotNum:string,
      /**  Indicates this record has been locked by a Advanced Shipping user and is not available for processing by any other user.  */  
   Lock:boolean,
      /**  Used by Advanced Shipping to designate which queue this record is in.  Advanced Shipping queues can prioritize and process records.  */  
   QueueID:string,
      /**  Sequence of this record within an Advanced Shipping Queue.  */  
   QueuePickSeq:number,
      /**  This is an internal sequence number for grouping MtlQueue records.  */  
   ReleaseForPickingSeq:number,
      /**  Warehouse Group that was assigned to this transaction.  */  
   WhseGroupCode:string,
      /**   The status of the transaction of the material.  Valid values:
MGMT-LOCK - Manager locked, RELEASED - Released, HOLD - On Hold, USER-LOCK - Locked for a user, ORDER-HOLD - On Hold for Order Based Picking, QUALITY-HOLD - On Hold for Quality Control, and PICK-PACK - Three step allocation Pick-Pack Method  */  
   TranStatus:string,
      /**  The Wave that was assigned during the allocation process.  */  
   WaveNum:number,
      /**  Transaction Priority.  Valid values are 1,2,3,4,5,6,7,8,9.  One is the highest priority.  */  
   Priority:number,
      /**  Transaction Source  */  
   TranSource:string,
      /**  When the TranStatus, AssignedToEmpID or Priority are modified, this value is updated with the ID of the Manager making the change.  */  
   LastMgrChangeEmpID:string,
      /**  Employee ID that was selected by the Warehouse Manager to process record from the queue.  */  
   AssignedToEmpID:string,
      /**  Transfer Order for which Demand is being satisfied.  */  
   TargetTFOrdNum:string,
      /**  Transfer Order Line for which Demand is being satisfied.  */  
   TargetTFOrdLine:number,
      /**  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  */  
   PackStation:string,
      /**  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  */  
   DistributionType:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Holds the result of checking sub-menu security.  NO indicates the current user does not have permission to carry out the indicated TranType.  */  
   OkToProcess:boolean,
   RequestedByEmpName:string,
   SelectedByEmpName:string,
   NeedByTimeDisp:string,
      /**  Is this material queue row part of the employees warehouse group  */  
   SameWhseGroupEmp:boolean,
      /**  Sort priority from highest to lowest (1,2,3,4,5,6,7,8,9,0)  */  
   SortByPriority:number,
      /**  Value is true if this mtlqueue record is related to a wave. False if it is not.  */  
   WaveRelated:boolean,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   AssemblySeqDescription:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   JobNumPartDescription:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   OrderLineLineDesc:string,
      /**  The member's name on the credit card.  */  
   OrderNumCardMemberName:string,
      /**  A unique code that identifies the currency.  */  
   OrderNumCurrencyCode:string,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartNumTrackLots:boolean,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartNumSellingFactor:number,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
      /**  Indicates if this part is serial number tracked  */  
   PartNumTrackSerialNum:boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  OUR internal Part number for this item.  */  
   POLinePartNum:string,
      /**  Supplier Part Number  */  
   POLineVenPartNum:string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   POLineLineDesc:string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   PORelNumRefCodeDesc:string,
      /**  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  */  
   RMALineLineDesc:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorNumCountry:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorNumName:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorNumVendorID:string,
      /**  Third address line of the Supplier  */  
   VendorNumAddress3:string,
      /**  A unique code that identifies the currency.  */  
   VendorNumCurrencyCode:string,
      /**  Can be blank.  */  
   VendorNumState:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNumZIP:string,
      /**  First address line of the Supplier  */  
   VendorNumAddress1:string,
      /**  City portion of the address of the Supplier  */  
   VendorNumCity:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNumDefaultFOB:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
      /**  Second address line of the Supplier  */  
   VendorNumAddress2:string,
      /**  Warehouse Group Description.  */  
   WarehouseGroupCodeWhseGroupDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MtlQueueListTableset{
   MtlQueueList:Erp_Tablesets_MtlQueueListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MtlQueueRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time(seconds since midnight) when transaction was created.  */  
   SysTime:number,
      /**  Number assigned by the system to uniquely identify the record.  Created by using the database sequence "MtlQueueSeq".  */  
   MtlQueueSeq:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Part Number of item in the container.  */  
   PartNum:string,
      /**  Quantity  */  
   Quantity:number,
      /**   Internal flag to indicate the type of transaction that this request is for.  This will control which functions are invoked for processing.
The same codes as in PartTran are used.  However, there are some additional codes also. 
They are; GET-WIP,  RTN-WIP, RTN-MTL, PUT-MTL, PUT-WIP, PICK-SO, PICK-JOB, PICK-TFO, BIN-REPLENISH, BIN-CONSOLIDATE, PICK-SO-XDOCK, PICK-JOB-XDOCK, PICK-TFO-XDOCK  */  
   TranType:string,
      /**   Used as a translatable prefix for the Reference field.
For example for a purchase receipt of stock it has "PS", (Packing Slip). For display purposes this is field is translated, then concatenated with the value in the Refernce field. 
Other values are "Job",  */  
   ReferencePrefix:string,
      /**  Contains a reference about the request. May contain Job/Asm/Seq, WrkCtr,  Packing Slip #,  Sales Order, etc...depending on the TranType.  */  
   Reference:string,
      /**  Employee ID that made the request.  */  
   RequestedByEmpID:string,
      /**  Employee ID that has selected this record from the queue for processing.  */  
   SelectedByEmpID:string,
      /**  Job Number that the request is related to.  This allows sorting by Job, which provides the user a method of working on all the requests for a specific job.  */  
   JobNum:string,
      /**  Job Assembly Sequence.  */  
   AssemblySeq:number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "O" = Job Operation (JobOper).  */  
   JobSeqType:string,
      /**  Seq # of the related specific material or operation record.  For WIP parts it's the operation sequence that created the part. For raw materials it's the related JobMtl.MtlSeq.  */  
   JobSeq:number,
      /**  Warehouse Code where item is to be found. For example a Get Raw Material request of a stocked part  would be the warehouse  the requirement was allocated against (JobMtl.WareHouseCode).  A "Move of a WIP part" will contain the Warehouse defined by the WrkCenter.PutWhse...  */  
   FromWhse:string,
      /**  Warehouse bin where item is to be found. For example a Get Raw Material request of a stocked part  would be the Primary Bin of the part/warehouse, if no primary bin, then the first Bin in the warehouse which contains this part, else blank.  A "Move of a WIP part" will contain the bin defined by the WrkCenter.PutBin...  */  
   FromBinNum:string,
      /**  Warehouse where item should be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputWhse).  */  
   ToWhse:string,
      /**  Warehouse bin where item is to be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputBin).  */  
   ToBinNum:string,
      /**  Assembly sequence of the operation that completed quantity of the job operation  will be moved to.  */  
   NextAssemblySeq:number,
      /**  Sequence of the operation that completed quantity of the job operation will be moved to.  */  
   NextJobSeq:number,
      /**  Date the this request is needed by.  Defaults, to current system date.  */  
   NeedByDate:string,
      /**  Time (seconds since midnight) that request is need by.  */  
   NeedByTime:number,
      /**  Vendor number of the related purchase receipt (RcvDtl).  Company,VendorNum, PurPoint, PackSlip,Packline are used to provide the link to the related RcvDtl record.  */  
   VendorNum:number,
      /**  Vendor purchase point id of the related purchase receipt (RcvDtl).  */  
   PurPoint:string,
      /**  Vendors Packing Slip # of the related RcvDtl.  */  
   PackSlip:string,
      /**  Vendors Packing Slip line  # of the related RcvDtl.  */  
   PackLine:number,
      /**   Order number job is making parts for. (See JobProd.OrderNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

OrderNum pertains only to "make to order" requirements.  
Provides relationship to the JobProd for "make to order" requirements.  */  
   OrderNum:number,
      /**  Related Sales order line number.  */  
   OrderLine:number,
      /**  Related sales order release number.  */  
   OrderRelNum:number,
      /**   Job that this job is making parts for. (See JobProd.TargetJobNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

TargetJobNum pertains only to "make to job" requirements.  
Provides relationship to the JobProd for "make to Job" requirements.  */  
   TargetJobNum:string,
      /**  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  */  
   TargetAssemblySeq:number,
      /**  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  */  
   TargetMtlSeq:number,
      /**  Part Revision number  */  
   RevisionNum:string,
      /**  A description of the Part.  */  
   PartDescription:string,
      /**  Internal unit of measure.  */  
   IUM:string,
      /**  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  */  
   PONum:number,
      /**  The PO line # which is being received. Only applicable for PO receipt transactions.  */  
   POLine:number,
      /**  Purchase Order Release # which is being received.  */  
   PORelNum:number,
      /**  Indicates if this MtlQueue is visible to the user on the Material Queue browse.  Set based on the users response to make a "move  request" when reporting quantities.  Set to true visible), if a move request is made.  This was implemented to keep track of labor quantity reported without making a move request.  The move request will then reflect the total quantity to move instead of what was reported on the labor transaction that requested the move.  Regardless of making a "Move Request" labor quantity reporting always creates/updates a MtlQueue record.  */  
   Visible:boolean,
      /**  Return Material Authorization number of related RMAHead.  */  
   RMANum:number,
      /**  Line number of the related RMADtl record.  */  
   RMALine:number,
      /**  RMAReceipt number of the related RMARcpt record.  */  
   RMAReceipt:number,
      /**  RMADisp number of the related RMADisp record.  */  
   RMADisp:number,
      /**  The related NonConf.TranID number. Used to link the MtlQueue table to the NonConf table.  */  
   NCTranID:number,
      /**  Lot Number of the part.  */  
   LotNum:string,
      /**  Indicates this record has been locked by a Advanced Shipping user and is not available for processing by any other user.  */  
   Lock:boolean,
      /**  Used by Advanced Shipping to designate which queue this record is in.  Advanced Shipping queues can prioritize and process records.  */  
   QueueID:string,
      /**  Sequence of this record within an Advanced Shipping Queue.  */  
   QueuePickSeq:number,
      /**  This is an internal sequence number for grouping MtlQueue records.  */  
   ReleaseForPickingSeq:number,
      /**  Warehouse Group that was assigned to this transaction.  */  
   WhseGroupCode:string,
      /**   The status of the transaction of the material.  Valid values:
MGMT-LOCK - Manager locked, RELEASED - Released, HOLD - On Hold, USER-LOCK - Locked for a user, ORDER-HOLD - On Hold for Order Based Picking, QUALITY-HOLD - On Hold for Quality Control, and PICK-PACK - Three step allocation Pick-Pack Method  */  
   TranStatus:string,
      /**  The Wave that was assigned during the allocation process.  */  
   WaveNum:number,
      /**  Transaction Priority.  Valid values are 1,2,3,4,5,6,7,8,9.  One is the highest priority.  */  
   Priority:number,
      /**  Transaction Source  */  
   TranSource:string,
      /**  When the TranStatus, AssignedToEmpID or Priority are modified, this value is updated with the ID of the Manager making the change.  */  
   LastMgrChangeEmpID:string,
      /**  Employee ID that was selected by the Warehouse Manager to process record from the queue.  */  
   AssignedToEmpID:string,
      /**  Transfer Order for which Demand is being satisfied.  */  
   TargetTFOrdNum:string,
      /**  Transfer Order Line for which Demand is being satisfied.  */  
   TargetTFOrdLine:number,
      /**  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  */  
   PackStation:string,
      /**  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  */  
   DistributionType:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Package Control Identification Number  */  
   PCID:string,
      /**  Related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  Last Used PCID on the selected line.  */  
   LastUsedPCID:string,
      /**  The PCID from which the material movement will occur.  */  
   FromPCID:string,
      /**  The PCID to which the material movement will occur.  */  
   ToPCID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  AttributeValueSeq  */  
   AttributeValueSeq:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
   CustID:string,
   CustTerritoryID:string,
      /**  Indicates whether Transfer Order Selector Flag should be disabled.  */  
   DisableTO:boolean,
      /**  From Inventory Selector Flag  */  
   FromInv:boolean,
      /**  From Manufacturing Selector Flag  */  
   FromJob:boolean,
      /**  From Purchasing Selector Flag  */  
   FromPO:boolean,
      /**  From Transfer Order Selector Flag  */  
   FromTO:boolean,
   FromWhseDesc:string,
      /**  Service Order Number from FSA. Only available in FSA Request Workbench.  */  
   FSAServiceOrderNumber:number,
      /**  Service Order Resource Num from FSA. Only available in FSA Request Workbench.  */  
   FSAServiceOrderResourceNum:number,
   HoldStatus:boolean,
   LeadTime:number,
   MaxMfgLotSize:number,
   MfgLeadTime:number,
   MinMfgLotSize:number,
   NeedByTimeDisp:string,
   NonStock:boolean,
      /**  Holds the result of checking sub-menu security.  NO indicates the current user does not have permission to carry out the indicated TranType.  */  
   OkToProcess:boolean,
   OnHandQtySite:number,
   OnHandQtyWhse:number,
   PlantName:string,
   PrimWhseCode:string,
   PrimWhseDesc:string,
   RequestedByEmpName:string,
      /**  Indicates whether an error occured in processing.  */  
   RequestError:boolean,
      /**  Message used to return status information after processing.  */  
   RequestMsg:string,
      /**  Is this material queue row part of the employees warehouse group  */  
   SameWhseGroupEmp:boolean,
   SelectedByEmpName:string,
      /**  Used by user to select rows for mass processing  */  
   SelectedForProcessing:boolean,
   ShipToCity:string,
   ShipToCountry:string,
      /**  Customer Ship To Name  */  
   ShipToName:string,
   ShipToNum:string,
   ShipToState:string,
   ShipToZIP:string,
      /**  Sort priority from highest to lowest (1,2,3,4,5,6,7,8,9,0)  */  
   SortByPriority:number,
      /**  Transfer, Sales Kit, Manufactured or Purchased.  */  
   SourceTypeDesc:string,
   ToWhseDesc:string,
   TransferLeadTime:number,
   TransferPlant:string,
      /**  Readable tran type (used in Replenishment Workbench)  */  
   TranTypeDesc:string,
   VendorNumName:string,
   VendorNumVendorID:string,
      /**  Value is true if this mtlqueue record is related to a wave. False if it is not.  */  
   WaveRelated:boolean,
      /**  Customer Sales Territory Region Code  */  
   CustRegionCode:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Display (decimal) number of pieces for inventory tracked parts.  */  
   DispNumberOfPieces:number,
   BitFlag:number,
   AssemblySeqDescription:string,
   JobNumPartDescription:string,
   OrderLineLineDesc:string,
   OrderNumCurrencyCode:string,
   OrderNumCardMemberName:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumSalesUM:string,
   PartNumPartDescription:string,
   PartNumTrackLots:boolean,
   PartNumPricePerCode:string,
   PartNumSellingFactor:number,
   PartNumIUM:string,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   PartNumAttrClassID:string,
   POLinePartNum:string,
   POLineVenPartNum:string,
   POLineLineDesc:string,
   RMALineLineDesc:string,
   VendorNumAddress1:string,
   VendorNumCity:string,
   VendorNumAddress3:string,
   VendorNumDefaultFOB:string,
   VendorNumCurrencyCode:string,
   VendorNumTermsCode:string,
   VendorNumCountry:string,
   VendorNumVendorID_:string,
   VendorNumState:string,
   VendorNumZIP:string,
   VendorNumName_:string,
   VendorNumAddress2:string,
   WarehouseGroupCodeWhseGroupDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PkgControlIDGeneratorRow{
      /**   This field will be like the field on the PCID Generate screen that is called from the Material Queue STK-SHP transaction.  The search button will allow searching & Selecting an Active Package Control ID Configuration having Label Print Controlled = False.
When a value is entered or selected, if the Package Code field is empty then the Package Code field should get populated with the Package Code on the selected control ID configuration  */  
   PkgControlIDCode:string,
      /**  Package code  */  
   PkgCode:string,
      /**  Package code description  */  
   PkgCodeDescription:string,
      /**  Part description  */  
   PartDescription:string,
   WarehseDesc:string,
   NumberToGenerate:number,
   TypeDescription:string,
      /**  Printer name  */  
   PrintName:string,
   Description:string,
   NumberOfLabelsToPrint:number,
   PrinterID:string,
   GenerateStagePCIDs:boolean,
   CheckAllowMixedParts:boolean,
   CheckAllowMixedUOMs:boolean,
   CheckAllowMixedLots:boolean,
   CheckAllowMultipleSerialNumsPerPCID:boolean,
   PrintLabels:boolean,
   PkgControlType:string,
   PartNum:string,
      /**   pulated with all the Warehouses owned or shared with the current site.  The Search will allow searching & selecting any Warehouse owned or shared with the current site.  Users can also enter a Warehouse ID
When a Warehouse is Entered/Selected, the Printer field should be populated with the Default Printer for the Warehouse  */  
   WarehouseCode:string,
   HHForm:boolean,
   PCIDSGenerated:string,
   DisableScreen:boolean,
   Plant:string,
      /**  Disable Warehouse in the PCID Generator screen if true as sometimes we require to pass in and force the warehouse to not be modified,  */  
   DisableWarehouse:boolean,
   SuppressPrintLabels:boolean,
   DisableNumberToGenerate:boolean,
   StyleNum:number,
   StyleDescription:string,
   DisableNumLblsRptStyle:boolean,
   PkgControlOutboundContainer:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PkgControlIDGeneratorTableset{
   PkgControlIDGenerator:Erp_Tablesets_PkgControlIDGeneratorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtMaterialQueueTableset{
   MtlQueue:Erp_Tablesets_MtlQueueRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param mtlQueueSeq
   */  
export interface GetByID_input{
   mtlQueueSeq:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_MaterialQueueTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_MaterialQueueTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_MaterialQueueTableset[],
}

export interface GetDefaultFilterSettings_output{
parameters : {
      /**  output parameters  */  
   mtlQueueMaxRowsToReturn:number,
   mtlQueueEndDaysOffset:number,
}
}

export interface GetDefaultToDate_output{
parameters : {
      /**  output parameters  */  
   defaultToDate:string,
}
}

   /** Required : 
      @param ds
   */  
export interface GetDeleteConfirmationMessage_input{
   ds:Erp_Tablesets_MaterialQueueTableset[],
}

export interface GetDeleteConfirmationMessage_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MaterialQueueTableset,
   deleteConfirmationMessage:string,
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
   returnObj:Erp_Tablesets_MtlQueueListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipMtlQueueSeq
   */  
export interface GetMtlQueueByTranID_input{
      /**  Material Queue Sequence  */  
   ipMtlQueueSeq:string,
}

export interface GetMtlQueueByTranID_output{
   returnObj:Erp_Tablesets_MaterialQueueTableset[],
}

   /** Required : 
      @param ds
   */  
export interface GetNewMtlQueue_input{
   ds:Erp_Tablesets_MaterialQueueTableset[],
}

export interface GetNewMtlQueue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MaterialQueueTableset,
}
}

   /** Required : 
      @param ipCompany
      @param ipPartNum
      @param ipPCID
      @param ipOrderNum
      @param ipOrderLine
      @param ipOrderRelNum
   */  
export interface GetPCIDPrintParams_input{
      /**  input company  */  
   ipCompany:string,
      /**  input part number  */  
   ipPartNum:string,
      /**  input pcid  */  
   ipPCID:string,
      /**  input order number  */  
   ipOrderNum:number,
      /**  input order line  */  
   ipOrderLine:number,
      /**  input order line  */  
   ipOrderRelNum:number,
}

export interface GetPCIDPrintParams_output{
parameters : {
      /**  output parameters  */  
   opNumLabelsToPrint:number,
   opPromptForReportStyle:boolean,
   opStyleNum:number,
}
}

   /** Required : 
      @param mtlQueueSysRowID
   */  
export interface GetParametersForMtlTags_input{
   mtlQueueSysRowID:string,
}

export interface GetParametersForMtlTags_output{
parameters : {
      /**  output parameters  */  
   mtlTagParameter:string,
}
}

   /** Required : 
      @param pkgControlIDCode
      @param partNum
      @param warehouseCode
      @param isHHForm
   */  
export interface GetPkgControlIDGenParams_input{
   pkgControlIDCode:string,
   partNum:string,
   warehouseCode:string,
   isHHForm:boolean,
}

export interface GetPkgControlIDGenParams_output{
   returnObj:Erp_Tablesets_PkgControlIDGeneratorTableset[],
}

   /** Required : 
      @param whereClause
      @param fromDate
      @param toDate
      @param fromWhse
      @param toWhse
      @param tranType
      @param selectedByEmpID
      @param excludeTransStatus
      @param onlySelectedByEmp
      @param onlyUnselected
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustomParams_input{
      /**  Where Clause  */  
   whereClause:string,
      /**  From Date  */  
   fromDate:string,
      /**  To Date  */  
   toDate:string,
      /**  From Warehouse  */  
   fromWhse:string,
      /**  To Warehouse  */  
   toWhse:string,
      /**  TranType  */  
   tranType:string,
      /**  Select by emp ID  */  
   selectedByEmpID:string,
      /**  Exclude tran status  */  
   excludeTransStatus:string,
      /**  Only return rows selected by employee  */  
   onlySelectedByEmp:boolean,
      /**  Only sreturn rows not selected by any employee  */  
   onlyUnselected:boolean,
      /**  Page Size  */  
   pageSize:number,
      /**  Absolute Page  */  
   absolutePage:number,
}

export interface GetRowsCustomParams_output{
   returnObj:Erp_Tablesets_MaterialQueueTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param delimitedFilterString
      @param recordsPerPage
      @param pageNum
   */  
export interface GetRowsCustom_input{
      /**  Format is [FieldName]Value~[FieldName]Value~  */  
   delimitedFilterString:string,
      /**  Records per page or 0 for all rows  */  
   recordsPerPage:number,
      /**  Page number defaults to page 1 if not specified  */  
   pageNum:number,
}

export interface GetRowsCustom_output{
   returnObj:Erp_Tablesets_MaterialQueueTableset[],
parameters : {
      /**  output parameters  */  
   rowCount:number,
}
}

   /** Required : 
      @param whereClauseMtlQueue
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseMtlQueue:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_MaterialQueueTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetSelectedMtlQueueList_input{
   ds:Erp_Tablesets_MaterialQueueTableset[],
}

export interface GetSelectedMtlQueueList_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MaterialQueueTableset,
   mtlQueueSelectedList:string,
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
      @param ipTranStatus
      @param ipMtlQueueSeq
      @param ipEmpID
      @param ds
   */  
export interface LockUnLockMtlQueForEmpID_input{
   ipTranStatus:string,
   ipMtlQueueSeq:number,
   ipEmpID:string,
   ds:Erp_Tablesets_MaterialQueueTableset[],
}

export interface LockUnLockMtlQueForEmpID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MaterialQueueTableset,
}
}

   /** Required : 
      @param ipTranStatus
      @param ipMtlQueueSeq
      @param ds
   */  
export interface LockUnLockMtlQue_input{
   ipTranStatus:string,
   ipMtlQueueSeq:number,
   ds:Erp_Tablesets_MaterialQueueTableset[],
}

export interface LockUnLockMtlQue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MaterialQueueTableset,
}
}

export interface SortQueueByPriority_output{
      /**  QueuePriority  */  
   returnObj:boolean,
}

   /** Required : 
      @param ipEmpID
   */  
export interface UnlockAutoSelectTransactions_input{
      /**  Employee ID  */  
   ipEmpID:string,
}

export interface UnlockAutoSelectTransactions_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtMaterialQueueTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtMaterialQueueTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_MaterialQueueTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MaterialQueueTableset,
}
}

   /** Required : 
      @param sysRowID
   */  
export interface VerifyMtlQueueExists_input{
   sysRowID:string,
}

export interface VerifyMtlQueueExists_output{
   returnObj:boolean,
}

