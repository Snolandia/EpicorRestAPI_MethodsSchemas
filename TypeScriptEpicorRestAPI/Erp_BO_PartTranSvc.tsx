import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PartTranSvc
// Description: Part activity transactions. This includes issues, PO receipts, Mfg receipts, Adjustments,
Transfers, Physical count adjustments, Cost replace. These are for all parts regardless
of being defined in the part master file.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/$metadata", {
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
   Description: Get PartTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartTrans
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartTranRow
   */  
export function get_PartTrans(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/PartTrans", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartTrans
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PartTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartTrans(requestBody:Erp_Tablesets_PartTranRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/PartTrans", {
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
   Summary: Calls GetByID to retrieve the PartTran item
   Description: Calls GetByID to retrieve the PartTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SysDate Desc: SysDate   Required: True   Allow empty value : True
      @param SysTime Desc: SysTime   Required: True
      @param TranNum Desc: TranNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PartTranRow
   */  
export function get_PartTrans_Company_SysDate_SysTime_TranNum(Company:string, SysDate:string, SysTime:string, TranNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/PartTrans(" + Company + "," + SysDate + "," + SysTime + "," + TranNum + ")", {
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
         resolve(data as Erp_Tablesets_PartTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PartTran for the service
   Description: Calls UpdateExt to update PartTran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SysDate Desc: SysDate   Required: True   Allow empty value : True
      @param SysTime Desc: SysTime   Required: True
      @param TranNum Desc: TranNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PartTrans_Company_SysDate_SysTime_TranNum(Company:string, SysDate:string, SysTime:string, TranNum:string, requestBody:Erp_Tablesets_PartTranRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/PartTrans(" + Company + "," + SysDate + "," + SysTime + "," + TranNum + ")", {
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
   Summary: Call UpdateExt to delete PartTran item
   Description: Call UpdateExt to delete PartTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SysDate Desc: SysDate   Required: True   Allow empty value : True
      @param SysTime Desc: SysTime   Required: True
      @param TranNum Desc: TranNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PartTrans_Company_SysDate_SysTime_TranNum(Company:string, SysDate:string, SysTime:string, TranNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/PartTrans(" + Company + "," + SysDate + "," + SysTime + "," + TranNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartTranListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranListRow)
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
export function get_GetRows(whereClausePartTran:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePartTran!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartTran=" + whereClausePartTran
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/GetRows" + params, {
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
export function get_GetByID(sysDate:string, sysTime:string, tranNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof sysDate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "sysDate=" + sysDate
   }
   if(typeof sysTime!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "sysTime=" + sysTime
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/GetList" + params, {
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
   Summary: Invoke method GetWhereClause
   Description: Get Where Clause for transaction log based on Mode
   OperationID: GetWhereClause
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetWhereClause(requestBody:GetWhereClause_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetWhereClause_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/GetWhereClause", {
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
         resolve(data as GetWhereClause_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPartTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartTran
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPartTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartTran(requestBody:GetNewPartTran_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPartTran_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/GetNewPartTran", {
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
         resolve(data as GetNewPartTran_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartTranListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartTranRow,
}

export interface Erp_Tablesets_PartTranListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  System date at time that record was created.  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   "SysTime":number,
      /**  A number which is used to allow create a unique key for the file.  */  
   "TranNum":number,
      /**  Part Number that this transaction is for.  */  
   "PartNum":string,
      /**  Warehouse that transaction is applied to  */  
   "WareHouseCode":string,
      /**  Identifies the Bin location that this transaction affected.  */  
   "BinNum":string,
      /**   Transaction Class...A-adjustment, D-DMR, I-issue, R-receipt, S-Shipment X-Job Adjustment. A character field which classifies PartTran records.  This is a higher level of classification of the TransType field. Their relationships are;
 R = DMR-STK, INS-MTL, INS-STK, INS-SUB, MFG-PLT, MFG-STK, MFG-WIP, PLT-STK, PUR-INS, PUR-MTL, PUR-STK, PUR-SUB, PUR-UKN, RMA-INS, STK-DMR, SVG-STK
I = ASM-INS, INS-ASM, INS-REJ, MTL-INS, PLT-ASM, PLT-MTL, STK-ASM, STK-INS, STK-MTL, STK-SRV, STK-UKN, SUB-DMR, SUB-INS,WIP-MFG
A = ADJ-CST, ADJ-PUR, ADJ-QTY, MFG-VAR, STK-PLT, STK-STK
S = MFG-CUS, MFG-VEN, STK-CUS
D = DMR-MTL, DMR-REJ, DMR-SUB, INS-DMR, MTL-DMR
X = ADJ-MTL, ADJ-SUB
Intended to  be used for record selection purposes.  */  
   "TranClass":string,
      /**   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  */  
   "TranType":string,
      /**  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  */  
   "InventoryTrans":boolean,
      /**  date of transaction.  */  
   "TranDate":string,
      /**   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  */  
   "TranQty":number,
      /**  Unit of Measure.  (part primary inventory uom)  */  
   "UM":string,
      /**  Material Unit Cost  */  
   "MtlUnitCost":number,
      /**  Labor Unit Cost  */  
   "LbrUnitCost":number,
      /**  Burden Unit Cost  */  
   "BurUnitCost":number,
      /**  Subcontract Unit Cost  */  
   "SubUnitCost":number,
      /**  Material Burden Unit Cost  */  
   "MtlBurUnitCost":number,
      /**   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  */  
   "ExtCost":number,
      /**  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the Part.CostMethod.  */  
   "CostMethod":string,
      /**  Job Number that transaction is associated with.  */  
   "JobNum":string,
      /**  Assembly Sequence #  */  
   "AssemblySeq":number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl),  "S" = SubContract Operation (JobOper) or "O" = Inside Operation(JobOper)
(FYI: Non-Coformance/Inspection transactions, ASM-INS, INS-ASM, INS-DMR, DMR-ASM are the only ones which create "O" types  */  
   "JobSeqType":string,
      /**  Seq # of specific material or subcontract operation record.  */  
   "JobSeq":number,
      /**  Indicates the type of Packing Slip... "C" = Customer (related to ShipDtl), "M" = Miscellaneous(MscShpDt),  "S" = Subcontractor (SubShipd) "TO" = (Transfer Order). This field, used along with PackNum/PackLine can be used to find the related shipping document record.  */  
   "PackType":string,
      /**  Packing slip number.  */  
   "PackNum":number,
      /**   The packing slip line # that this transaction is linked to.
Note: This field is used for both  a shipment to customer packing slip  or a receipt from vendor packing slip.  */  
   "PackLine":number,
      /**  Created by Purchase Order Receipt Process.  */  
   "PONum":number,
      /**  The line # of detail record on the purchase order.  */  
   "POLine":number,
      /**  Purchase Order Release # of the POSched record that this transaction is for.  */  
   "PORelNum":number,
      /**  Transfer "From/To" warehouse code. This is used for the warehouse transfer transactions. For the Issue side of the transaction it identifies the "transfer to" warehouse. For the receipt side of the transaction it identifies the "transfer from" warehouse.  */  
   "WareHouse2":string,
      /**  This value only exists for the warehouse transaction. TranSrc = "4".  For the Issue side of the transaction it identifies the Bin location that the quantity is transferred in to. On the Receipt side of the transaction it identifies the Bin location that the quantity was transferred from.  */  
   "BinNum2":string,
      /**   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  */  
   "OrderNum":number,
      /**  The sales order line that this transaction is associated with.  */  
   "OrderLine":number,
      /**  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  */  
   "OrderRelNum":number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  */  
   "EntryPerson":string,
      /**  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  */  
   "TranReference":string,
      /**  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   "PartDescription":string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part, JobOPer, JobMtl, ShipDtl,  SubShipD ....  */  
   "RevisionNum":string,
      /**  The internal key that along with PurPoint is used to tie back to the VendorPP master file. Applicable for shipments to subcontractors (MFG-VEN) and receipts (PUR-STK, PUR-MTL, PUR-SUB, PUR-UKN).  */  
   "VendorNum":number,
      /**  Vendor purchase point ID. (see VendorNum)  */  
   "PurPoint":string,
      /**  Quantity received against a purchase order in the vendors unit of measure.  */  
   "POReceiptQty":number,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the PO detail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the MtlUnitCost field which is used as cost to job or stock.  */  
   "POUnitCost":number,
      /**  Vendors Packing Slip #.  */  
   "PackSlip":string,
      /**  Invoice Number from corresponding APInvHed record. Applicable only with the purchase variance adjustment record (TranType = "ADJ-PUR") generated via A/P invoice posting.  */  
   "InvoiceNum":string,
      /**  Used along with InvoiceNum to relate to the corresponding APInvDtl record that generated this PartTran record. (see PartTran.InvoiceNum)  */  
   "InvoiceLine":number,
      /**  Inventory Adjustment Source for ADJ-QTY, ADJ-CST transaction types only.  "P" = Physical Inventory Count, "C" = Cycle Inventory Count, "O" = Other Adjustment  */  
   "InvAdjSrc":string,
      /**  Used for Inventory Adjustment Source "Other" OR MTL-DMR, STK-DMR, SUB-DMR, or INS-DMR transaction types.  Refers to the Reason table.  */  
   "InvAdjReason":string,
      /**  Lot Number  */  
   "LotNum":string,
      /**  Unique dimension code for the part.  */  
   "DimCode":string,
      /**  Dimension unit of measure.  */  
   "DUM":string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   "DimConvFactor":number,
      /**  Transfer "From/To" lot number.  */  
   "LotNum2":string,
      /**  Transfer "From/To" Part Dimension  */  
   "DimCode2":string,
      /**  Transfer "From/To" Dimension unit of measure.  */  
   "DUM2":string,
      /**  Transfer "From/To" Dimension conversion factor.  */  
   "DimConvFactor2":number,
      /**  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  For example: Adj-Cst for other than the parts costing method are not posted to G/L.  */  
   "GLTrans":boolean,
      /**  Indicates if transaction was posted to G/L.  Transactions are posted in summary form via the Job Management Capture COS/WIP process .  */  
   "PostedToGL":boolean,
      /**   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  */  
   "FiscalYear":number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "FiscalPeriod":number,
      /**   Journal number that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "JournalNum":number,
      /**  The "Costed" field indicates if the Capture COS/Wip Activity has run on that part transaction. If "Yes" the transaction costs cant be changed anymore.  */  
   "Costed":boolean,
      /**  DMR number used to identify the related DMR record.  */  
   "DMRNum":number,
      /**  DMR action number  */  
   "ActionNum":number,
      /**  RMA Number  */  
   "RMANum":number,
      /**   If the amount of this PartTran was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped, its costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  */  
   "COSPostingReqd":boolean,
      /**  Journal Code of the related GLJrnDtl.  */  
   "JournalCode":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Site Identifier.  */  
   "Plant2":string,
      /**  Reference to the service call that the material is being issued for.  */  
   "CallNum":number,
      /**  Reference to the service call line  that the material is being issued for.  */  
   "CallLine":number,
      /**  Reference to the service call line Material sequence that the material is being issued for.  */  
   "MatNum":number,
      /**  Job Number of transfer source/target.  */  
   "JobNum2":string,
      /**  Assembly Sequence  of transfer source/target.  */  
   "AssemblySeq2":number,
      /**  Seq # of transfer source/target.  */  
   "JobSeq2":number,
      /**   NOTE: Applies only to the RMA-INS transactions.
Contains the system internal customer number of the related customer record. 
Not directly updateable, updated via the RmaRcpt write trigger.  */  
   "CustNum":number,
      /**  Line number of the related RMADtl record.  */  
   "RMALine":number,
      /**  RMA Receipt  */  
   "RMAReceipt":number,
      /**  RMA Disposition  */  
   "RMADisp":number,
      /**  Other division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of Site transaction costs.  OtherDivValue only applies to Site to Site transactions (TranType="PLT-" and Site <> S  */  
   "OtherDivValue":number,
      /**  Site Transaction Number  */  
   "PlantTranNum":number,
      /**  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  */  
   "NonConfID":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlMtlUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlLabUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlSubUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   "MtlBurdenUnitCost":number,
      /**  Link to the related GLRefTyp.RefType.  */  
   "RefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "RefCode":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  On Hand Quantity before the part costing calculations were run.  */  
   "BeginQty":number,
      /**  On Hand Quantity after part costing calculation were run.  */  
   "AfterQty":number,
      /**  Burden Unit cost before the part costing calculation was run  */  
   "BegBurUnitCost":number,
      /**  Labor Unit cost before the costing calculation was run  */  
   "BegLbrUnitCost":number,
      /**  Material Burden Unit Cost before the costing calculation was run  */  
   "BegMtlBurUnitCost":number,
      /**  Material Unit Cost before the costing calculation was run  */  
   "BegMtlUnitCost":number,
      /**  Sub Contract Unit Cost before the costing calculation was run  */  
   "BegSubUnitCost":number,
      /**  Burden Unit cost after the part costing calculation was run  */  
   "AfterBurUnitCost":number,
      /**  Labor Unit Cost after the costing calculation was run  */  
   "AfterLbrUnitCost":number,
      /**  Material Burden Unit Cost after the costing calculation was run  */  
   "AfterMtlBurUnitCost":number,
      /**  Material Unit Cost after the costing calculation was run  */  
   "AfterMtlUnitCost":number,
      /**  Sub Contract Unit Cost after the costing calculation was run  */  
   "AfterSubUnitCost":number,
      /**  To Site division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of To Site transaction costs.  SiteCostValue only applies to Site to Site transactions (TranType="PLT-" and Site  */  
   "PlantCostValue":number,
      /**  The Shop Employee ID of the user that created this transaction.  */  
   "EmpID":string,
      /**  The unique identifier of the DemandReconcile that created this PartTran record.  */  
   "ReconcileNum":number,
      /**  Id to the Cost Set Group that is used as the default CostGrp.  */  
   "CostID":string,
      /**  For FIFO costed part, use this date to find the FIFO cost queue record affected by this transaction.  */  
   "FIFODate":string,
      /**  For FIFO costed part, use this sequence number to find the FIFO cost queue record affected by this transaction.  */  
   "FIFOSeq":number,
      /**   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  */  
   "ActTranQty":number,
      /**  Actual Unit of Measure of the ActTransQty.  */  
   "ActTransUOM":string,
      /**  The Inventory Tracking Unit of Measure that transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  */  
   "InvtyUOM":string,
      /**  The Inventory Tracking Unit of Measure that inventory transfer transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  */  
   "InvtyUOM2":string,
      /**   Internal flag to indicate what type of FIFO update is needed.  Valid values are: (A/U/D)
"A" - Add new FIFO cost queue
"U" - Update existing FIFO cost queue
"D" - Delete existing FIFO cost queue (Technically, this is more of voiding/deactivating the FIFO since we don't delete historical FIFO records).  */  
   "FIFOAction":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  */  
   "BinType":string,
      /**  Calendar year of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  */  
   "CCYear":number,
      /**  Calendar month of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl..  */  
   "CCMonth":number,
      /**  CycleSeq of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  */  
   "CycleSeq":number,
      /**  GUID - reference on PE ABT.  */  
   "ABTUID":string,
      /**  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the PartSite.CostMethod or Part.CostMethod  */  
   "BaseCostMethod":string,
      /**   Revert Status field, with following values:
0.	Not reverted (default initial value)
1.	Reverted  */  
   "RevertStatus":number,
      /**  Reference on revert line  by SySRowID.  */  
   "RevertID":string,
      /**  Drop shipment Packing Slip.  */  
   "DropShipPackSlip":string,
      /**   PartTran.VarTarget, with following values:
'JOB' ? Use Job Expense Account
'STK' ? Use Inventory Account
'VAR' ? Use Purchase Variance Account
'INS' ? Use Inspection Account
'UKN' ? Expense Account (Miscellaneous receipt)
'MTL' ? Use WIP Material Account
'SUB' ? Use WIP Subcontract account
'DMR' ? Use DMR account
'REJ' ? Use DMR Write off Account
'ACA' ? Use Actual Cost Account  */  
   "VarTarget":string,
      /**  The FIFO subsequence number of the related PartFIFOCost record.  */  
   "FIFOSubSeq":number,
      /**  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltMtlUnitCost":number,
      /**  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltLbrUnitCost":number,
      /**  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltBurUnitCost":number,
      /**  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltSubUnitCost":number,
      /**  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltMtlBurUnitCost":number,
      /**  Alternate FIFO Extended Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltExtCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlMtlUnitCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlLabUnitCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlSubUnitCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlBurdenUnitCost":number,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Invoice Number from Progress Billing Invoice preparation  */  
   "PBInvNum":number,
      /**   This is only relevant for TranType MFG-MFG.
Valid types are '' , 'L', and 'B'.  
For Transfers, set to ''.
For Loans and Repayment of Loans set PartTran. LoanType to either 'L' or 'B' based on PartTran.JobNum.  If PartTran.JobNum is the job who is making the loan (or who made the loan, in the case of a repayment), then set to 'L' (loaner).  If PartTran.JobNum is the job who originally received the loan or who is receiving a loan set to 'B' (borrower).  */  
   "LoanFlag":string,
      /**  Unique identifier of the Asset.  */  
   "AssetNum":string,
      /**  Unique number to identify the Addition activity of an asset.  */  
   "AdditionNum":number,
      /**  Unique number to identify the Disposal activity of an asset.  */  
   "DisposalNum":number,
      /**  Logical field to indicate if this record has been read by project analysis process.  */  
   "ProjProcessed":boolean,
      /**  Used by Project Analysis process.  */  
   "AsOfDate":string,
      /**  Used By Project Analysis Process  */  
   "AsOfSeq":number,
      /**  Like RcvMisc.MscNum. Filled only for ADJ-PUR transactions created from late costs.  */  
   "MscNum":number,
      /**  ODC Unit Cost  */  
   "ODCUnitCost":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  TranRefType  */  
   "TranRefType":number,
      /**  PCID  */  
   "PCID":string,
      /**  PCIDCollapseCounter  */  
   "PCIDCollapseCounter":number,
      /**  PCID2  */  
   "PCID2":string,
      /**  ContractID  */  
   "ContractID":string,
      /**  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  */  
   "LCFlag":boolean,
      /**  ExtMtlCost  */  
   "ExtMtlCost":number,
      /**  ExtLbrCost  */  
   "ExtLbrCost":number,
      /**  ExtBurCost  */  
   "ExtBurCost":number,
      /**  ExtSubCost  */  
   "ExtSubCost":number,
      /**  ExtMtlBurCost  */  
   "ExtMtlBurCost":number,
      /**  ExtMtlMtlCost  */  
   "ExtMtlMtlCost":number,
      /**  ExtMtlLabCost  */  
   "ExtMtlLabCost":number,
      /**  ExtMtlSubCost  */  
   "ExtMtlSubCost":number,
      /**  ExtMtlBurdenCost  */  
   "ExtMtlBurdenCost":number,
      /**  MYImportNum  */  
   "MYImportNum":string,
      /**  AutoReverse  */  
   "AutoReverse":boolean,
      /**  RevTranNum  */  
   "RevTranNum":number,
      /**  RevSysDate  */  
   "RevSysDate":string,
      /**  RevSysTime  */  
   "RevSysTime":number,
      /**  The Non Recoverable Tax that has been included on the Extended Cost.  This will be calculated from the Receipt Header and Receipt Line tax records by subtracting the total deductable tax from the total tax.  */  
   "ExtNonRecoverableCost":number,
      /**  True if transaction is related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  WIPPCID  */  
   "WIPPCID":string,
      /**  WIPPCID2  */  
   "WIPPCID2":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "JobNumPartDescription":string,
   "JobSubUnitCost":number,
   "LegalNumberNumber":string,
   "LegalNumberPrefix":string,
   "LegalNumberPrefixList":string,
   "LegalNumberReadOnlyFields":string,
   "LegalNumberYear":number,
   "MtlLbrUnitCost":number,
   "MtlQueueRowId":string,
      /**  Used/Set only by MfgReceipts - Indicates if Job has multiple end parts.  */  
   "MultiEndParts":boolean,
   "OnHandQty":number,
      /**  The member's name on the credit card.  */  
   "OrderNumCardMemberName":string,
      /**  A unique code that identifies the currency.  */  
   "OrderNumCurrencyCode":string,
      /**  Override Costs.  Set to yes if the user chooses to override the cost.  */  
   "OverRideCosts":boolean,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  */  
   "PackNumName":string,
   "PartDescriptionAsm":string,
   "PartDescriptionJH":string,
   "PartDescriptionMS":string,
   "PartDescriptionSP":string,
      /**  Optional lot number description.  */  
   "PartLotPartLotDescription":string,
   "PartNumAsm":string,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
   "PartNumJH":string,
   "PartNumMS":string,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartNumSalesUM":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartNumSellingFactor":number,
   "PartNumSP":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartNumTrackLots":boolean,
      /**  Indicates if this part is serial number tracked  */  
   "PartNumTrackSerialNum":boolean,
      /**  The Plant name. Used on shipping reports.  */  
   "PlantName":string,
   "QtyAvailToComplete":number,
   "QtyBearing":boolean,
      /**  Quantity Completed  */  
   "QtyCompleted":number,
   "RevisionNumRevDescription":string,
   "RevisionNumRevShortDesc":string,
   "SalvageQtyToDate":number,
   "SerialNoTempTranID":number,
   "ThisTranQty":number,
   "TreeDisplay":string,
      /**  First address line of the Supplier  */  
   "VendorNumAddress1":string,
      /**  Second address line of the Supplier  */  
   "VendorNumAddress2":string,
      /**  Third address line of the Supplier  */  
   "VendorNumAddress3":string,
      /**  City portion of the address of the Supplier  */  
   "VendorNumCity":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorNumCountry":string,
      /**  A unique code that identifies the currency.  */  
   "VendorNumCurrencyCode":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNumDefaultFOB":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorNumName":string,
      /**  Can be blank.  */  
   "VendorNumState":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorNumVendorID":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNumZIP":string,
      /**  First address line  */  
   "VendorPPNumAddress1":string,
      /**  Second address line  */  
   "VendorPPNumAddress2":string,
      /**  Third address line  */  
   "VendorPPNumAddress3":string,
      /**  City portion of the address  */  
   "VendorPPNumCity":string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   "VendorPPNumCountry":string,
      /**  Purchase Point Name...can't be blank.  */  
   "VendorPPNumName":string,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   "VendorPPNumPrimPCon":number,
      /**  State portion of the address  */  
   "VendorPPNumState":string,
      /**  Postal Code or Zip code portion of the address  */  
   "VendorPPNumZip":string,
      /**  Description.  */  
   "WarehouseDescription":string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   "BinNumDescription":string,
   "CostMethodDisplay":string,
      /**  Description for the dimension code.  */  
   "DimCodeDimCodeDescription":string,
   "DIMDescription":string,
      /**  Part field objects must be enabled when the Final Assembly (0) is selected and the Job has multiple end parts.  */  
   "DisableFieldPart":boolean,
      /**  Display format of System Time in Hrs:Min.  */  
   "DispSysTime":string,
   "DispUOM":string,
      /**  Describes the Part.  System maintained, not user modifiable.  */  
   "DMRNumPartDescription":string,
   "dummyKeyField":string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   "FromBinDescription":string,
      /**  The Plant name. Used on shipping reports.  */  
   "FromPlantName":string,
      /**  Description.  */  
   "FromWareHouseDescription":string,
      /**  If InvAdjSrc = "P", then this field is true, InvAdjSrc = "C", then this field is false  */  
   "FullPhysical":boolean,
      /**  GL Journal Source Transaction Amount  */  
   "GLTranAmt":number,
      /**  GL Journal Source Transaction Date  */  
   "GLTranDate":string,
      /**  Inventory subcontract unit cost  */  
   "InvBurUnitCost":number,
      /**  Inventory Labor unit cost.  */  
   "InvLbrUnitCost":number,
      /**  Inventory burden unit cost  */  
   "InvMtlBurUnitCost":number,
      /**  Inventory material unit cost  */  
   "InvMtlUnitCost":number,
      /**  Inventory subcontract unit cost.  */  
   "InvSubUnitCost":number,
   "IssuedComplete":boolean,
   "JobBurUnitCost":number,
   "JobLbrUnitCost":number,
   "JobMtlBurUnitCost":number,
   "JobMtlUnitCost":number,
   "Selected":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartTranRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  System date at time that record was created.  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   "SysTime":number,
      /**  A number which is used to allow create a unique key for the file.  */  
   "TranNum":number,
      /**  Part Number that this transaction is for.  */  
   "PartNum":string,
      /**  Warehouse that transaction is applied to  */  
   "WareHouseCode":string,
      /**  Identifies the Bin location that this transaction affected.  */  
   "BinNum":string,
      /**   Transaction Class...A-adjustment, D-DMR, I-issue, R-receipt, S-Shipment X-Job Adjustment. A character field which classifies PartTran records.  This is a higher level of classification of the TransType field. Their relationships are;
 R = DMR-STK, INS-MTL, INS-STK, INS-SUB, MFG-PLT, MFG-STK, MFG-WIP, PLT-STK, PUR-INS, PUR-MTL, PUR-STK, PUR-SUB, PUR-UKN, RMA-INS, STK-DMR, SVG-STK
I = ASM-INS, INS-ASM, INS-REJ, MTL-INS, PLT-ASM, PLT-MTL, STK-ASM, STK-INS, STK-MTL, STK-SRV, STK-UKN, SUB-DMR, SUB-INS,WIP-MFG
A = ADJ-CST, ADJ-PUR, ADJ-QTY, MFG-VAR, STK-PLT, STK-STK
S = MFG-CUS, MFG-VEN, STK-CUS
D = DMR-MTL, DMR-REJ, DMR-SUB, INS-DMR, MTL-DMR
X = ADJ-MTL, ADJ-SUB
Intended to  be used for record selection purposes.  */  
   "TranClass":string,
      /**   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  */  
   "TranType":string,
      /**  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  */  
   "InventoryTrans":boolean,
      /**  date of transaction.  */  
   "TranDate":string,
      /**   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  */  
   "TranQty":number,
      /**  Unit of Measure.  (part primary inventory uom)  */  
   "UM":string,
      /**  Material Unit Cost  */  
   "MtlUnitCost":number,
      /**  Labor Unit Cost  */  
   "LbrUnitCost":number,
      /**  Burden Unit Cost  */  
   "BurUnitCost":number,
      /**  Subcontract Unit Cost  */  
   "SubUnitCost":number,
      /**  Material Burden Unit Cost  */  
   "MtlBurUnitCost":number,
      /**   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  */  
   "ExtCost":number,
      /**  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the Part.CostMethod.  */  
   "CostMethod":string,
      /**  Job Number that transaction is associated with.  */  
   "JobNum":string,
      /**  Assembly Sequence #  */  
   "AssemblySeq":number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl),  "S" = SubContract Operation (JobOper) or "O" = Inside Operation(JobOper)
(FYI: Non-Coformance/Inspection transactions, ASM-INS, INS-ASM, INS-DMR, DMR-ASM are the only ones which create "O" types  */  
   "JobSeqType":string,
      /**  Seq # of specific material or subcontract operation record.  */  
   "JobSeq":number,
      /**  Indicates the type of Packing Slip... "C" = Customer (related to ShipDtl), "M" = Miscellaneous(MscShpDt),  "S" = Subcontractor (SubShipd) "TO" = (Transfer Order). This field, used along with PackNum/PackLine can be used to find the related shipping document record.  */  
   "PackType":string,
      /**  Packing slip number.  */  
   "PackNum":number,
      /**   The packing slip line # that this transaction is linked to.
Note: This field is used for both  a shipment to customer packing slip  or a receipt from vendor packing slip.  */  
   "PackLine":number,
      /**  Created by Purchase Order Receipt Process.  */  
   "PONum":number,
      /**  The line # of detail record on the purchase order.  */  
   "POLine":number,
      /**  Purchase Order Release # of the POSched record that this transaction is for.  */  
   "PORelNum":number,
      /**  Transfer "From/To" warehouse code. This is used for the warehouse transfer transactions. For the Issue side of the transaction it identifies the "transfer to" warehouse. For the receipt side of the transaction it identifies the "transfer from" warehouse.  */  
   "WareHouse2":string,
      /**  This value only exists for the warehouse transaction. TranSrc = "4".  For the Issue side of the transaction it identifies the Bin location that the quantity is transferred in to. On the Receipt side of the transaction it identifies the Bin location that the quantity was transferred from.  */  
   "BinNum2":string,
      /**   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  */  
   "OrderNum":number,
      /**  The sales order line that this transaction is associated with.  */  
   "OrderLine":number,
      /**  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  */  
   "OrderRelNum":number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  */  
   "EntryPerson":string,
      /**  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  */  
   "TranReference":string,
      /**  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   "PartDescription":string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part, JobOPer, JobMtl, ShipDtl,  SubShipD ....  */  
   "RevisionNum":string,
      /**  The internal key that along with PurPoint is used to tie back to the VendorPP master file. Applicable for shipments to subcontractors (MFG-VEN) and receipts (PUR-STK, PUR-MTL, PUR-SUB, PUR-UKN).  */  
   "VendorNum":number,
      /**  Vendor purchase point ID. (see VendorNum)  */  
   "PurPoint":string,
      /**  Quantity received against a purchase order in the vendors unit of measure.  */  
   "POReceiptQty":number,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the PO detail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the MtlUnitCost field which is used as cost to job or stock.  */  
   "POUnitCost":number,
      /**  Vendors Packing Slip #.  */  
   "PackSlip":string,
      /**  Invoice Number from corresponding APInvHed record. Applicable only with the purchase variance adjustment record (TranType = "ADJ-PUR") generated via A/P invoice posting.  */  
   "InvoiceNum":string,
      /**  Used along with InvoiceNum to relate to the corresponding APInvDtl record that generated this PartTran record. (see PartTran.InvoiceNum)  */  
   "InvoiceLine":number,
      /**  Inventory Adjustment Source for ADJ-QTY, ADJ-CST transaction types only.  "P" = Physical Inventory Count, "C" = Cycle Inventory Count, "O" = Other Adjustment  */  
   "InvAdjSrc":string,
      /**  Used for Inventory Adjustment Source "Other" OR MTL-DMR, STK-DMR, SUB-DMR, or INS-DMR transaction types.  Refers to the Reason table.  */  
   "InvAdjReason":string,
      /**  Lot Number  */  
   "LotNum":string,
      /**  Unique dimension code for the part.  */  
   "DimCode":string,
      /**  Dimension unit of measure.  */  
   "DUM":string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   "DimConvFactor":number,
      /**  Transfer "From/To" lot number.  */  
   "LotNum2":string,
      /**  Transfer "From/To" Part Dimension  */  
   "DimCode2":string,
      /**  Transfer "From/To" Dimension unit of measure.  */  
   "DUM2":string,
      /**  Transfer "From/To" Dimension conversion factor.  */  
   "DimConvFactor2":number,
      /**  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  For example: Adj-Cst for other than the parts costing method are not posted to G/L.  */  
   "GLTrans":boolean,
      /**  Indicates if transaction was posted to G/L.  Transactions are posted in summary form via the Job Management Capture COS/WIP process .  */  
   "PostedToGL":boolean,
      /**   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  */  
   "FiscalYear":number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "FiscalPeriod":number,
      /**   Journal number that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "JournalNum":number,
      /**  The "Costed" field indicates if the Capture COS/Wip Activity has run on that part transaction. If "Yes" the transaction costs cant be changed anymore.  */  
   "Costed":boolean,
      /**  DMR number used to identify the related DMR record.  */  
   "DMRNum":number,
      /**  DMR action number  */  
   "ActionNum":number,
      /**  RMA Number  */  
   "RMANum":number,
      /**   If the amount of this PartTran was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped, its costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  */  
   "COSPostingReqd":boolean,
      /**  Journal Code of the related GLJrnDtl.  */  
   "JournalCode":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Site Identifier.  */  
   "Plant2":string,
      /**  Reference to the service call that the material is being issued for.  */  
   "CallNum":number,
      /**  Reference to the service call line  that the material is being issued for.  */  
   "CallLine":number,
      /**  Reference to the service call line Material sequence that the material is being issued for.  */  
   "MatNum":number,
      /**  Job Number of transfer source/target.  */  
   "JobNum2":string,
      /**  Assembly Sequence  of transfer source/target.  */  
   "AssemblySeq2":number,
      /**  Seq # of transfer source/target.  */  
   "JobSeq2":number,
      /**   NOTE: Applies only to the RMA-INS transactions.
Contains the system internal customer number of the related customer record. 
Not directly updateable, updated via the RmaRcpt write trigger.  */  
   "CustNum":number,
      /**  Line number of the related RMADtl record.  */  
   "RMALine":number,
      /**  RMA Receipt  */  
   "RMAReceipt":number,
      /**  RMA Disposition  */  
   "RMADisp":number,
      /**  Other division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of Site transaction costs.  OtherDivValue only applies to Site to Site transactions (TranType="PLT-" and Site <> S  */  
   "OtherDivValue":number,
      /**  Site Transaction Number  */  
   "PlantTranNum":number,
      /**  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  */  
   "NonConfID":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlMtlUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlLabUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlSubUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   "MtlBurdenUnitCost":number,
      /**  Link to the related GLRefTyp.RefType.  */  
   "RefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "RefCode":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  On Hand Quantity before the part costing calculations were run.  */  
   "BeginQty":number,
      /**  On Hand Quantity after part costing calculation were run.  */  
   "AfterQty":number,
      /**  Burden Unit cost before the part costing calculation was run  */  
   "BegBurUnitCost":number,
      /**  Labor Unit cost before the costing calculation was run  */  
   "BegLbrUnitCost":number,
      /**  Material Burden Unit Cost before the costing calculation was run  */  
   "BegMtlBurUnitCost":number,
      /**  Material Unit Cost before the costing calculation was run  */  
   "BegMtlUnitCost":number,
      /**  Sub Contract Unit Cost before the costing calculation was run  */  
   "BegSubUnitCost":number,
      /**  Burden Unit cost after the part costing calculation was run  */  
   "AfterBurUnitCost":number,
      /**  Labor Unit Cost after the costing calculation was run  */  
   "AfterLbrUnitCost":number,
      /**  Material Burden Unit Cost after the costing calculation was run  */  
   "AfterMtlBurUnitCost":number,
      /**  Material Unit Cost after the costing calculation was run  */  
   "AfterMtlUnitCost":number,
      /**  Sub Contract Unit Cost after the costing calculation was run  */  
   "AfterSubUnitCost":number,
      /**  To Site division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of To Site transaction costs.  SiteCostValue only applies to Site to Site transactions (TranType="PLT-" and Site  */  
   "PlantCostValue":number,
      /**  The Shop Employee ID of the user that created this transaction.  */  
   "EmpID":string,
      /**  The unique identifier of the DemandReconcile that created this PartTran record.  */  
   "ReconcileNum":number,
      /**  Id to the Cost Set Group that is used as the default CostGrp.  */  
   "CostID":string,
      /**  For FIFO costed part, use this date to find the FIFO cost queue record affected by this transaction.  */  
   "FIFODate":string,
      /**  For FIFO costed part, use this sequence number to find the FIFO cost queue record affected by this transaction.  */  
   "FIFOSeq":number,
      /**   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  */  
   "ActTranQty":number,
      /**  Actual Unit of Measure of the ActTransQty.  */  
   "ActTransUOM":string,
      /**  The Inventory Tracking Unit of Measure that transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  */  
   "InvtyUOM":string,
      /**  The Inventory Tracking Unit of Measure that inventory transfer transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  */  
   "InvtyUOM2":string,
      /**   Internal flag to indicate what type of FIFO update is needed.  Valid values are: (A/U/D)
"A" - Add new FIFO cost queue
"U" - Update existing FIFO cost queue
"D" - Delete existing FIFO cost queue (Technically, this is more of voiding/deactivating the FIFO since we don't delete historical FIFO records).  */  
   "FIFOAction":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  */  
   "BinType":string,
      /**  Calendar year of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  */  
   "CCYear":number,
      /**  Calendar month of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl..  */  
   "CCMonth":number,
      /**  CycleSeq of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  */  
   "CycleSeq":number,
      /**  GUID - reference on PE ABT.  */  
   "ABTUID":string,
      /**  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the PartSite.CostMethod or Part.CostMethod  */  
   "BaseCostMethod":string,
      /**   Revert Status field, with following values:
0.	Not reverted (default initial value)
1.	Reverted  */  
   "RevertStatus":number,
      /**  Reference on revert line  by SySRowID.  */  
   "RevertID":string,
      /**  Drop shipment Packing Slip.  */  
   "DropShipPackSlip":string,
      /**   PartTran.VarTarget, with following values:
'JOB' ? Use Job Expense Account
'STK' ? Use Inventory Account
'VAR' ? Use Purchase Variance Account
'INS' ? Use Inspection Account
'UKN' ? Expense Account (Miscellaneous receipt)
'MTL' ? Use WIP Material Account
'SUB' ? Use WIP Subcontract account
'DMR' ? Use DMR account
'REJ' ? Use DMR Write off Account
'ACA' ? Use Actual Cost Account  */  
   "VarTarget":string,
      /**  The FIFO subsequence number of the related PartFIFOCost record.  */  
   "FIFOSubSeq":number,
      /**  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltMtlUnitCost":number,
      /**  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltLbrUnitCost":number,
      /**  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltBurUnitCost":number,
      /**  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltSubUnitCost":number,
      /**  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltMtlBurUnitCost":number,
      /**  Alternate FIFO Extended Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltExtCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlMtlUnitCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlLabUnitCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlSubUnitCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlBurdenUnitCost":number,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Invoice Number from Progress Billing Invoice preparation  */  
   "PBInvNum":number,
      /**   This is only relevant for TranType MFG-MFG.
Valid types are '' , 'L', and 'B'.  
For Transfers, set to ''.
For Loans and Repayment of Loans set PartTran. LoanType to either 'L' or 'B' based on PartTran.JobNum.  If PartTran.JobNum is the job who is making the loan (or who made the loan, in the case of a repayment), then set to 'L' (loaner).  If PartTran.JobNum is the job who originally received the loan or who is receiving a loan set to 'B' (borrower).  */  
   "LoanFlag":string,
      /**  Unique identifier of the Asset.  */  
   "AssetNum":string,
      /**  Unique number to identify the Addition activity of an asset.  */  
   "AdditionNum":number,
      /**  Unique number to identify the Disposal activity of an asset.  */  
   "DisposalNum":number,
      /**  Logical field to indicate if this record has been read by project analysis process.  */  
   "ProjProcessed":boolean,
      /**  Used by Project Analysis process.  */  
   "AsOfDate":string,
      /**  Used By Project Analysis Process  */  
   "AsOfSeq":number,
      /**  Like RcvMisc.MscNum. Filled only for ADJ-PUR transactions created from late costs.  */  
   "MscNum":number,
      /**  ODC Unit Cost  */  
   "ODCUnitCost":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  TranRefType  */  
   "TranRefType":number,
      /**  PCID  */  
   "PCID":string,
      /**  PCIDCollapseCounter  */  
   "PCIDCollapseCounter":number,
      /**  PCID2  */  
   "PCID2":string,
      /**  ContractID  */  
   "ContractID":string,
      /**  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  */  
   "LCFlag":boolean,
      /**  ExtMtlCost  */  
   "ExtMtlCost":number,
      /**  ExtLbrCost  */  
   "ExtLbrCost":number,
      /**  ExtBurCost  */  
   "ExtBurCost":number,
      /**  ExtSubCost  */  
   "ExtSubCost":number,
      /**  ExtMtlBurCost  */  
   "ExtMtlBurCost":number,
      /**  ExtMtlMtlCost  */  
   "ExtMtlMtlCost":number,
      /**  ExtMtlLabCost  */  
   "ExtMtlLabCost":number,
      /**  ExtMtlSubCost  */  
   "ExtMtlSubCost":number,
      /**  ExtMtlBurdenCost  */  
   "ExtMtlBurdenCost":number,
      /**  MYImportNum  */  
   "MYImportNum":string,
      /**  AutoReverse  */  
   "AutoReverse":boolean,
      /**  RevTranNum  */  
   "RevTranNum":number,
      /**  RevSysDate  */  
   "RevSysDate":string,
      /**  RevSysTime  */  
   "RevSysTime":number,
      /**  The Non Recoverable Tax that has been included on the Extended Cost.  This will be calculated from the Receipt Header and Receipt Line tax records by subtracting the total deductable tax from the total tax.  */  
   "ExtNonRecoverableCost":number,
      /**  True if transaction is related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  WIPPCID  */  
   "WIPPCID":string,
      /**  WIPPCID2  */  
   "WIPPCID2":string,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   "CallCode":string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   "ContractCode":string,
   "DIMDescription":string,
      /**  Part field objects must be enabled when the Final Assembly (0) is selected and the Job has multiple end parts.  */  
   "DisableFieldPart":boolean,
      /**  Display format of System Time in Hrs:Min.  */  
   "DispSysTime":string,
   "DispUOM":string,
   "dummyKeyField":string,
   "EnableSerialNumbers":boolean,
      /**  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  */  
   "FSAAction":string,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   "FSACallCode":string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   "FSAContractCode":string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   "FSAContractNum":number,
      /**  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  */  
   "FSAEmpID":string,
      /**  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  */  
   "FSAEquipmentInstallID":number,
      /**  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  */  
   "FSAEquipmentPartNum":string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderNum":number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderResourceNum":number,
      /**  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  */  
   "FSAWarrantyCode":string,
      /**  If InvAdjSrc = "P", then this field is true, InvAdjSrc = "C", then this field is false  */  
   "FullPhysical":boolean,
      /**  GL Journal Source Transaction Amount  */  
   "GLTranAmt":number,
      /**  GL Journal Source Transaction Date  */  
   "GLTranDate":string,
      /**  Inventory subcontract unit cost  */  
   "InvBurUnitCost":number,
      /**  Inventory Labor unit cost.  */  
   "InvLbrUnitCost":number,
      /**  Inventory burden unit cost  */  
   "InvMtlBurUnitCost":number,
      /**  Inventory material unit cost  */  
   "InvMtlUnitCost":number,
      /**  Inventory subcontract unit cost.  */  
   "InvSubUnitCost":number,
   "IssuedComplete":boolean,
   "JobBurUnitCost":number,
   "JobLbrUnitCost":number,
   "JobMtlBurUnitCost":number,
   "JobMtlUnitCost":number,
   "JobSubUnitCost":number,
   "LegalNumberNumber":string,
   "LegalNumberPrefix":string,
   "LegalNumberPrefixList":string,
   "LegalNumberReadOnlyFields":string,
   "LegalNumberYear":number,
   "MtlLbrUnitCost":number,
   "MtlQueueRowId":string,
      /**  Used/Set only by MfgReceipts - Indicates if Job has multiple end parts.  */  
   "MultiEndParts":boolean,
   "OnHandQty":number,
      /**  Override Costs.  Set to yes if the user chooses to override the cost.  */  
   "OverRideCosts":boolean,
   "PartDescriptionAsm":string,
   "PartDescriptionJH":string,
   "PartDescriptionMS":string,
   "PartDescriptionSP":string,
   "PartNumAsm":string,
   "PartNumJH":string,
   "PartNumMS":string,
   "PartNumSP":string,
   "QtyAvailToComplete":number,
   "QtyBearing":boolean,
      /**  Quantity Completed  */  
   "QtyCompleted":number,
   "RevisionNumRevDescription":string,
   "RevisionNumRevShortDesc":string,
   "SalvageQtyToDate":number,
   "SerialNoTempTranID":number,
   "ThisTranQty":number,
      /**  Transaction Amount  */  
   "TranAmount":number,
   "TreeDisplay":string,
      /**  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  */  
   "WarrantyCode":string,
      /**  Contract Created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   "ContractNum":number,
   "CostMethodDisplay":string,
      /**  Number of pieces for inventory attribute tracked parts  */  
   "DispNumberOfPieces":number,
   "RevisionNumAsm":string,
   "RevisionNumMS":string,
   "RevisionNumSP":string,
   "PlantConfCtrlEnablePackageControl":boolean,
      /**  Description for AttributeSetID associated with PartNumMS  */  
   "AttributeSetDescriptionMS":string,
      /**  AttributeSetID associated with PartNumMS  */  
   "AttributeSetIDMS":number,
      /**  AttributeSetShortDescription associated with PartNumMS  */  
   "AttributeSetShortDescriptionMS":string,
   "BitFlag":number,
   "AssemblySeqDescription":string,
   "BinNumDescription":string,
   "CallLineLineDesc":string,
   "CustNumCustID":string,
   "CustNumBTName":string,
   "CustNumName":string,
   "DimCodeDimCodeDescription":string,
   "DMRNumPartDescription":string,
   "FromBinDescription":string,
   "FromPlantName":string,
   "FromWareHouseDescription":string,
   "InvoiceNumDescription":string,
   "JobNumPartDescription":string,
   "MatNumLineDesc":string,
   "OrderLineLineDesc":string,
   "OrderNumCardMemberName":string,
   "OrderNumCurrencyCode":string,
   "PackLineLineDesc":string,
   "PackNumName":string,
   "PartLotPartLotDescription":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumSellingFactor":number,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumTrackLots":boolean,
   "PartNumIUM":string,
   "PartNumPartDescription":string,
   "PartNumSalesUM":string,
   "PartNumPricePerCode":string,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumAttrClassID":string,
   "PlantName":string,
   "POLineVenPartNum":string,
   "POLinePartNum":string,
   "POLineLineDesc":string,
   "RMALineLineDesc":string,
   "VendorNumName":string,
   "VendorNumAddress3":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCurrencyCode":string,
   "VendorNumState":string,
   "VendorNumAddress1":string,
   "VendorNumAddress2":string,
   "VendorNumVendorID":string,
   "VendorNumCountry":string,
   "VendorNumCity":string,
   "VendorNumZIP":string,
   "VendorNumTermsCode":string,
   "VendorPPNumAddress1":string,
   "VendorPPNumAddress2":string,
   "VendorPPNumPrimPCon":number,
   "VendorPPNumAddress3":string,
   "VendorPPNumCountry":string,
   "VendorPPNumState":string,
   "VendorPPNumZip":string,
   "VendorPPNumCity":string,
   "VendorPPNumName":string,
   "WarehouseDescription":string,
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
      @param sysDate
      @param sysTime
      @param tranNum
   */  
export interface DeleteByID_input{
   sysDate:string,
   sysTime:number,
   tranNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PartTranListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   SysTime:number,
      /**  A number which is used to allow create a unique key for the file.  */  
   TranNum:number,
      /**  Part Number that this transaction is for.  */  
   PartNum:string,
      /**  Warehouse that transaction is applied to  */  
   WareHouseCode:string,
      /**  Identifies the Bin location that this transaction affected.  */  
   BinNum:string,
      /**   Transaction Class...A-adjustment, D-DMR, I-issue, R-receipt, S-Shipment X-Job Adjustment. A character field which classifies PartTran records.  This is a higher level of classification of the TransType field. Their relationships are;
 R = DMR-STK, INS-MTL, INS-STK, INS-SUB, MFG-PLT, MFG-STK, MFG-WIP, PLT-STK, PUR-INS, PUR-MTL, PUR-STK, PUR-SUB, PUR-UKN, RMA-INS, STK-DMR, SVG-STK
I = ASM-INS, INS-ASM, INS-REJ, MTL-INS, PLT-ASM, PLT-MTL, STK-ASM, STK-INS, STK-MTL, STK-SRV, STK-UKN, SUB-DMR, SUB-INS,WIP-MFG
A = ADJ-CST, ADJ-PUR, ADJ-QTY, MFG-VAR, STK-PLT, STK-STK
S = MFG-CUS, MFG-VEN, STK-CUS
D = DMR-MTL, DMR-REJ, DMR-SUB, INS-DMR, MTL-DMR
X = ADJ-MTL, ADJ-SUB
Intended to  be used for record selection purposes.  */  
   TranClass:string,
      /**   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  */  
   TranType:string,
      /**  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  */  
   InventoryTrans:boolean,
      /**  date of transaction.  */  
   TranDate:string,
      /**   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  */  
   TranQty:number,
      /**  Unit of Measure.  (part primary inventory uom)  */  
   UM:string,
      /**  Material Unit Cost  */  
   MtlUnitCost:number,
      /**  Labor Unit Cost  */  
   LbrUnitCost:number,
      /**  Burden Unit Cost  */  
   BurUnitCost:number,
      /**  Subcontract Unit Cost  */  
   SubUnitCost:number,
      /**  Material Burden Unit Cost  */  
   MtlBurUnitCost:number,
      /**   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  */  
   ExtCost:number,
      /**  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the Part.CostMethod.  */  
   CostMethod:string,
      /**  Job Number that transaction is associated with.  */  
   JobNum:string,
      /**  Assembly Sequence #  */  
   AssemblySeq:number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl),  "S" = SubContract Operation (JobOper) or "O" = Inside Operation(JobOper)
(FYI: Non-Coformance/Inspection transactions, ASM-INS, INS-ASM, INS-DMR, DMR-ASM are the only ones which create "O" types  */  
   JobSeqType:string,
      /**  Seq # of specific material or subcontract operation record.  */  
   JobSeq:number,
      /**  Indicates the type of Packing Slip... "C" = Customer (related to ShipDtl), "M" = Miscellaneous(MscShpDt),  "S" = Subcontractor (SubShipd) "TO" = (Transfer Order). This field, used along with PackNum/PackLine can be used to find the related shipping document record.  */  
   PackType:string,
      /**  Packing slip number.  */  
   PackNum:number,
      /**   The packing slip line # that this transaction is linked to.
Note: This field is used for both  a shipment to customer packing slip  or a receipt from vendor packing slip.  */  
   PackLine:number,
      /**  Created by Purchase Order Receipt Process.  */  
   PONum:number,
      /**  The line # of detail record on the purchase order.  */  
   POLine:number,
      /**  Purchase Order Release # of the POSched record that this transaction is for.  */  
   PORelNum:number,
      /**  Transfer "From/To" warehouse code. This is used for the warehouse transfer transactions. For the Issue side of the transaction it identifies the "transfer to" warehouse. For the receipt side of the transaction it identifies the "transfer from" warehouse.  */  
   WareHouse2:string,
      /**  This value only exists for the warehouse transaction. TranSrc = "4".  For the Issue side of the transaction it identifies the Bin location that the quantity is transferred in to. On the Receipt side of the transaction it identifies the Bin location that the quantity was transferred from.  */  
   BinNum2:string,
      /**   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  */  
   OrderNum:number,
      /**  The sales order line that this transaction is associated with.  */  
   OrderLine:number,
      /**  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  */  
   OrderRelNum:number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  */  
   EntryPerson:string,
      /**  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  */  
   TranReference:string,
      /**  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   PartDescription:string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part, JobOPer, JobMtl, ShipDtl,  SubShipD ....  */  
   RevisionNum:string,
      /**  The internal key that along with PurPoint is used to tie back to the VendorPP master file. Applicable for shipments to subcontractors (MFG-VEN) and receipts (PUR-STK, PUR-MTL, PUR-SUB, PUR-UKN).  */  
   VendorNum:number,
      /**  Vendor purchase point ID. (see VendorNum)  */  
   PurPoint:string,
      /**  Quantity received against a purchase order in the vendors unit of measure.  */  
   POReceiptQty:number,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the PO detail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the MtlUnitCost field which is used as cost to job or stock.  */  
   POUnitCost:number,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  Invoice Number from corresponding APInvHed record. Applicable only with the purchase variance adjustment record (TranType = "ADJ-PUR") generated via A/P invoice posting.  */  
   InvoiceNum:string,
      /**  Used along with InvoiceNum to relate to the corresponding APInvDtl record that generated this PartTran record. (see PartTran.InvoiceNum)  */  
   InvoiceLine:number,
      /**  Inventory Adjustment Source for ADJ-QTY, ADJ-CST transaction types only.  "P" = Physical Inventory Count, "C" = Cycle Inventory Count, "O" = Other Adjustment  */  
   InvAdjSrc:string,
      /**  Used for Inventory Adjustment Source "Other" OR MTL-DMR, STK-DMR, SUB-DMR, or INS-DMR transaction types.  Refers to the Reason table.  */  
   InvAdjReason:string,
      /**  Lot Number  */  
   LotNum:string,
      /**  Unique dimension code for the part.  */  
   DimCode:string,
      /**  Dimension unit of measure.  */  
   DUM:string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   DimConvFactor:number,
      /**  Transfer "From/To" lot number.  */  
   LotNum2:string,
      /**  Transfer "From/To" Part Dimension  */  
   DimCode2:string,
      /**  Transfer "From/To" Dimension unit of measure.  */  
   DUM2:string,
      /**  Transfer "From/To" Dimension conversion factor.  */  
   DimConvFactor2:number,
      /**  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  For example: Adj-Cst for other than the parts costing method are not posted to G/L.  */  
   GLTrans:boolean,
      /**  Indicates if transaction was posted to G/L.  Transactions are posted in summary form via the Job Management Capture COS/WIP process .  */  
   PostedToGL:boolean,
      /**   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  */  
   FiscalYear:number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   FiscalPeriod:number,
      /**   Journal number that entry was posted to.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  The "Costed" field indicates if the Capture COS/Wip Activity has run on that part transaction. If "Yes" the transaction costs cant be changed anymore.  */  
   Costed:boolean,
      /**  DMR number used to identify the related DMR record.  */  
   DMRNum:number,
      /**  DMR action number  */  
   ActionNum:number,
      /**  RMA Number  */  
   RMANum:number,
      /**   If the amount of this PartTran was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped, its costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  */  
   COSPostingReqd:boolean,
      /**  Journal Code of the related GLJrnDtl.  */  
   JournalCode:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Site Identifier.  */  
   Plant2:string,
      /**  Reference to the service call that the material is being issued for.  */  
   CallNum:number,
      /**  Reference to the service call line  that the material is being issued for.  */  
   CallLine:number,
      /**  Reference to the service call line Material sequence that the material is being issued for.  */  
   MatNum:number,
      /**  Job Number of transfer source/target.  */  
   JobNum2:string,
      /**  Assembly Sequence  of transfer source/target.  */  
   AssemblySeq2:number,
      /**  Seq # of transfer source/target.  */  
   JobSeq2:number,
      /**   NOTE: Applies only to the RMA-INS transactions.
Contains the system internal customer number of the related customer record. 
Not directly updateable, updated via the RmaRcpt write trigger.  */  
   CustNum:number,
      /**  Line number of the related RMADtl record.  */  
   RMALine:number,
      /**  RMA Receipt  */  
   RMAReceipt:number,
      /**  RMA Disposition  */  
   RMADisp:number,
      /**  Other division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of Site transaction costs.  OtherDivValue only applies to Site to Site transactions (TranType="PLT-" and Site <> S  */  
   OtherDivValue:number,
      /**  Site Transaction Number  */  
   PlantTranNum:number,
      /**  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  */  
   NonConfID:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlMtlUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlLabUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlSubUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   MtlBurdenUnitCost:number,
      /**  Link to the related GLRefTyp.RefType.  */  
   RefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  On Hand Quantity before the part costing calculations were run.  */  
   BeginQty:number,
      /**  On Hand Quantity after part costing calculation were run.  */  
   AfterQty:number,
      /**  Burden Unit cost before the part costing calculation was run  */  
   BegBurUnitCost:number,
      /**  Labor Unit cost before the costing calculation was run  */  
   BegLbrUnitCost:number,
      /**  Material Burden Unit Cost before the costing calculation was run  */  
   BegMtlBurUnitCost:number,
      /**  Material Unit Cost before the costing calculation was run  */  
   BegMtlUnitCost:number,
      /**  Sub Contract Unit Cost before the costing calculation was run  */  
   BegSubUnitCost:number,
      /**  Burden Unit cost after the part costing calculation was run  */  
   AfterBurUnitCost:number,
      /**  Labor Unit Cost after the costing calculation was run  */  
   AfterLbrUnitCost:number,
      /**  Material Burden Unit Cost after the costing calculation was run  */  
   AfterMtlBurUnitCost:number,
      /**  Material Unit Cost after the costing calculation was run  */  
   AfterMtlUnitCost:number,
      /**  Sub Contract Unit Cost after the costing calculation was run  */  
   AfterSubUnitCost:number,
      /**  To Site division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of To Site transaction costs.  SiteCostValue only applies to Site to Site transactions (TranType="PLT-" and Site  */  
   PlantCostValue:number,
      /**  The Shop Employee ID of the user that created this transaction.  */  
   EmpID:string,
      /**  The unique identifier of the DemandReconcile that created this PartTran record.  */  
   ReconcileNum:number,
      /**  Id to the Cost Set Group that is used as the default CostGrp.  */  
   CostID:string,
      /**  For FIFO costed part, use this date to find the FIFO cost queue record affected by this transaction.  */  
   FIFODate:string,
      /**  For FIFO costed part, use this sequence number to find the FIFO cost queue record affected by this transaction.  */  
   FIFOSeq:number,
      /**   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  */  
   ActTranQty:number,
      /**  Actual Unit of Measure of the ActTransQty.  */  
   ActTransUOM:string,
      /**  The Inventory Tracking Unit of Measure that transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  */  
   InvtyUOM:string,
      /**  The Inventory Tracking Unit of Measure that inventory transfer transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  */  
   InvtyUOM2:string,
      /**   Internal flag to indicate what type of FIFO update is needed.  Valid values are: (A/U/D)
"A" - Add new FIFO cost queue
"U" - Update existing FIFO cost queue
"D" - Delete existing FIFO cost queue (Technically, this is more of voiding/deactivating the FIFO since we don't delete historical FIFO records).  */  
   FIFOAction:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  */  
   BinType:string,
      /**  Calendar year of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  */  
   CCYear:number,
      /**  Calendar month of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl..  */  
   CCMonth:number,
      /**  CycleSeq of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  */  
   CycleSeq:number,
      /**  GUID - reference on PE ABT.  */  
   ABTUID:string,
      /**  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the PartSite.CostMethod or Part.CostMethod  */  
   BaseCostMethod:string,
      /**   Revert Status field, with following values:
0.	Not reverted (default initial value)
1.	Reverted  */  
   RevertStatus:number,
      /**  Reference on revert line  by SySRowID.  */  
   RevertID:string,
      /**  Drop shipment Packing Slip.  */  
   DropShipPackSlip:string,
      /**   PartTran.VarTarget, with following values:
'JOB' ? Use Job Expense Account
'STK' ? Use Inventory Account
'VAR' ? Use Purchase Variance Account
'INS' ? Use Inspection Account
'UKN' ? Expense Account (Miscellaneous receipt)
'MTL' ? Use WIP Material Account
'SUB' ? Use WIP Subcontract account
'DMR' ? Use DMR account
'REJ' ? Use DMR Write off Account
'ACA' ? Use Actual Cost Account  */  
   VarTarget:string,
      /**  The FIFO subsequence number of the related PartFIFOCost record.  */  
   FIFOSubSeq:number,
      /**  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltMtlUnitCost:number,
      /**  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltLbrUnitCost:number,
      /**  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltBurUnitCost:number,
      /**  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltSubUnitCost:number,
      /**  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltMtlBurUnitCost:number,
      /**  Alternate FIFO Extended Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltExtCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlMtlUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlLabUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlSubUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlBurdenUnitCost:number,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Invoice Number from Progress Billing Invoice preparation  */  
   PBInvNum:number,
      /**   This is only relevant for TranType MFG-MFG.
Valid types are '' , 'L', and 'B'.  
For Transfers, set to ''.
For Loans and Repayment of Loans set PartTran. LoanType to either 'L' or 'B' based on PartTran.JobNum.  If PartTran.JobNum is the job who is making the loan (or who made the loan, in the case of a repayment), then set to 'L' (loaner).  If PartTran.JobNum is the job who originally received the loan or who is receiving a loan set to 'B' (borrower).  */  
   LoanFlag:string,
      /**  Unique identifier of the Asset.  */  
   AssetNum:string,
      /**  Unique number to identify the Addition activity of an asset.  */  
   AdditionNum:number,
      /**  Unique number to identify the Disposal activity of an asset.  */  
   DisposalNum:number,
      /**  Logical field to indicate if this record has been read by project analysis process.  */  
   ProjProcessed:boolean,
      /**  Used by Project Analysis process.  */  
   AsOfDate:string,
      /**  Used By Project Analysis Process  */  
   AsOfSeq:number,
      /**  Like RcvMisc.MscNum. Filled only for ADJ-PUR transactions created from late costs.  */  
   MscNum:number,
      /**  ODC Unit Cost  */  
   ODCUnitCost:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  TranRefType  */  
   TranRefType:number,
      /**  PCID  */  
   PCID:string,
      /**  PCIDCollapseCounter  */  
   PCIDCollapseCounter:number,
      /**  PCID2  */  
   PCID2:string,
      /**  ContractID  */  
   ContractID:string,
      /**  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  */  
   LCFlag:boolean,
      /**  ExtMtlCost  */  
   ExtMtlCost:number,
      /**  ExtLbrCost  */  
   ExtLbrCost:number,
      /**  ExtBurCost  */  
   ExtBurCost:number,
      /**  ExtSubCost  */  
   ExtSubCost:number,
      /**  ExtMtlBurCost  */  
   ExtMtlBurCost:number,
      /**  ExtMtlMtlCost  */  
   ExtMtlMtlCost:number,
      /**  ExtMtlLabCost  */  
   ExtMtlLabCost:number,
      /**  ExtMtlSubCost  */  
   ExtMtlSubCost:number,
      /**  ExtMtlBurdenCost  */  
   ExtMtlBurdenCost:number,
      /**  MYImportNum  */  
   MYImportNum:string,
      /**  AutoReverse  */  
   AutoReverse:boolean,
      /**  RevTranNum  */  
   RevTranNum:number,
      /**  RevSysDate  */  
   RevSysDate:string,
      /**  RevSysTime  */  
   RevSysTime:number,
      /**  The Non Recoverable Tax that has been included on the Extended Cost.  This will be calculated from the Receipt Header and Receipt Line tax records by subtracting the total deductable tax from the total tax.  */  
   ExtNonRecoverableCost:number,
      /**  True if transaction is related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  WIPPCID  */  
   WIPPCID:string,
      /**  WIPPCID2  */  
   WIPPCID2:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   JobNumPartDescription:string,
   JobSubUnitCost:number,
   LegalNumberNumber:string,
   LegalNumberPrefix:string,
   LegalNumberPrefixList:string,
   LegalNumberReadOnlyFields:string,
   LegalNumberYear:number,
   MtlLbrUnitCost:number,
   MtlQueueRowId:string,
      /**  Used/Set only by MfgReceipts - Indicates if Job has multiple end parts.  */  
   MultiEndParts:boolean,
   OnHandQty:number,
      /**  The member's name on the credit card.  */  
   OrderNumCardMemberName:string,
      /**  A unique code that identifies the currency.  */  
   OrderNumCurrencyCode:string,
      /**  Override Costs.  Set to yes if the user chooses to override the cost.  */  
   OverRideCosts:boolean,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  */  
   PackNumName:string,
   PartDescriptionAsm:string,
   PartDescriptionJH:string,
   PartDescriptionMS:string,
   PartDescriptionSP:string,
      /**  Optional lot number description.  */  
   PartLotPartLotDescription:string,
   PartNumAsm:string,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
   PartNumJH:string,
   PartNumMS:string,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartNumSellingFactor:number,
   PartNumSP:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartNumTrackLots:boolean,
      /**  Indicates if this part is serial number tracked  */  
   PartNumTrackSerialNum:boolean,
      /**  The Plant name. Used on shipping reports.  */  
   PlantName:string,
   QtyAvailToComplete:number,
   QtyBearing:boolean,
      /**  Quantity Completed  */  
   QtyCompleted:number,
   RevisionNumRevDescription:string,
   RevisionNumRevShortDesc:string,
   SalvageQtyToDate:number,
   SerialNoTempTranID:number,
   ThisTranQty:number,
   TreeDisplay:string,
      /**  First address line of the Supplier  */  
   VendorNumAddress1:string,
      /**  Second address line of the Supplier  */  
   VendorNumAddress2:string,
      /**  Third address line of the Supplier  */  
   VendorNumAddress3:string,
      /**  City portion of the address of the Supplier  */  
   VendorNumCity:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorNumCountry:string,
      /**  A unique code that identifies the currency.  */  
   VendorNumCurrencyCode:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNumDefaultFOB:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorNumName:string,
      /**  Can be blank.  */  
   VendorNumState:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorNumVendorID:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNumZIP:string,
      /**  First address line  */  
   VendorPPNumAddress1:string,
      /**  Second address line  */  
   VendorPPNumAddress2:string,
      /**  Third address line  */  
   VendorPPNumAddress3:string,
      /**  City portion of the address  */  
   VendorPPNumCity:string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   VendorPPNumCountry:string,
      /**  Purchase Point Name...can't be blank.  */  
   VendorPPNumName:string,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   VendorPPNumPrimPCon:number,
      /**  State portion of the address  */  
   VendorPPNumState:string,
      /**  Postal Code or Zip code portion of the address  */  
   VendorPPNumZip:string,
      /**  Description.  */  
   WarehouseDescription:string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   BinNumDescription:string,
   CostMethodDisplay:string,
      /**  Description for the dimension code.  */  
   DimCodeDimCodeDescription:string,
   DIMDescription:string,
      /**  Part field objects must be enabled when the Final Assembly (0) is selected and the Job has multiple end parts.  */  
   DisableFieldPart:boolean,
      /**  Display format of System Time in Hrs:Min.  */  
   DispSysTime:string,
   DispUOM:string,
      /**  Describes the Part.  System maintained, not user modifiable.  */  
   DMRNumPartDescription:string,
   dummyKeyField:string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   FromBinDescription:string,
      /**  The Plant name. Used on shipping reports.  */  
   FromPlantName:string,
      /**  Description.  */  
   FromWareHouseDescription:string,
      /**  If InvAdjSrc = "P", then this field is true, InvAdjSrc = "C", then this field is false  */  
   FullPhysical:boolean,
      /**  GL Journal Source Transaction Amount  */  
   GLTranAmt:number,
      /**  GL Journal Source Transaction Date  */  
   GLTranDate:string,
      /**  Inventory subcontract unit cost  */  
   InvBurUnitCost:number,
      /**  Inventory Labor unit cost.  */  
   InvLbrUnitCost:number,
      /**  Inventory burden unit cost  */  
   InvMtlBurUnitCost:number,
      /**  Inventory material unit cost  */  
   InvMtlUnitCost:number,
      /**  Inventory subcontract unit cost.  */  
   InvSubUnitCost:number,
   IssuedComplete:boolean,
   JobBurUnitCost:number,
   JobLbrUnitCost:number,
   JobMtlBurUnitCost:number,
   JobMtlUnitCost:number,
   Selected:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartTranListTableset{
   PartTranList:Erp_Tablesets_PartTranListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartTranRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   SysTime:number,
      /**  A number which is used to allow create a unique key for the file.  */  
   TranNum:number,
      /**  Part Number that this transaction is for.  */  
   PartNum:string,
      /**  Warehouse that transaction is applied to  */  
   WareHouseCode:string,
      /**  Identifies the Bin location that this transaction affected.  */  
   BinNum:string,
      /**   Transaction Class...A-adjustment, D-DMR, I-issue, R-receipt, S-Shipment X-Job Adjustment. A character field which classifies PartTran records.  This is a higher level of classification of the TransType field. Their relationships are;
 R = DMR-STK, INS-MTL, INS-STK, INS-SUB, MFG-PLT, MFG-STK, MFG-WIP, PLT-STK, PUR-INS, PUR-MTL, PUR-STK, PUR-SUB, PUR-UKN, RMA-INS, STK-DMR, SVG-STK
I = ASM-INS, INS-ASM, INS-REJ, MTL-INS, PLT-ASM, PLT-MTL, STK-ASM, STK-INS, STK-MTL, STK-SRV, STK-UKN, SUB-DMR, SUB-INS,WIP-MFG
A = ADJ-CST, ADJ-PUR, ADJ-QTY, MFG-VAR, STK-PLT, STK-STK
S = MFG-CUS, MFG-VEN, STK-CUS
D = DMR-MTL, DMR-REJ, DMR-SUB, INS-DMR, MTL-DMR
X = ADJ-MTL, ADJ-SUB
Intended to  be used for record selection purposes.  */  
   TranClass:string,
      /**   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  */  
   TranType:string,
      /**  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  */  
   InventoryTrans:boolean,
      /**  date of transaction.  */  
   TranDate:string,
      /**   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  */  
   TranQty:number,
      /**  Unit of Measure.  (part primary inventory uom)  */  
   UM:string,
      /**  Material Unit Cost  */  
   MtlUnitCost:number,
      /**  Labor Unit Cost  */  
   LbrUnitCost:number,
      /**  Burden Unit Cost  */  
   BurUnitCost:number,
      /**  Subcontract Unit Cost  */  
   SubUnitCost:number,
      /**  Material Burden Unit Cost  */  
   MtlBurUnitCost:number,
      /**   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  */  
   ExtCost:number,
      /**  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the Part.CostMethod.  */  
   CostMethod:string,
      /**  Job Number that transaction is associated with.  */  
   JobNum:string,
      /**  Assembly Sequence #  */  
   AssemblySeq:number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl),  "S" = SubContract Operation (JobOper) or "O" = Inside Operation(JobOper)
(FYI: Non-Coformance/Inspection transactions, ASM-INS, INS-ASM, INS-DMR, DMR-ASM are the only ones which create "O" types  */  
   JobSeqType:string,
      /**  Seq # of specific material or subcontract operation record.  */  
   JobSeq:number,
      /**  Indicates the type of Packing Slip... "C" = Customer (related to ShipDtl), "M" = Miscellaneous(MscShpDt),  "S" = Subcontractor (SubShipd) "TO" = (Transfer Order). This field, used along with PackNum/PackLine can be used to find the related shipping document record.  */  
   PackType:string,
      /**  Packing slip number.  */  
   PackNum:number,
      /**   The packing slip line # that this transaction is linked to.
Note: This field is used for both  a shipment to customer packing slip  or a receipt from vendor packing slip.  */  
   PackLine:number,
      /**  Created by Purchase Order Receipt Process.  */  
   PONum:number,
      /**  The line # of detail record on the purchase order.  */  
   POLine:number,
      /**  Purchase Order Release # of the POSched record that this transaction is for.  */  
   PORelNum:number,
      /**  Transfer "From/To" warehouse code. This is used for the warehouse transfer transactions. For the Issue side of the transaction it identifies the "transfer to" warehouse. For the receipt side of the transaction it identifies the "transfer from" warehouse.  */  
   WareHouse2:string,
      /**  This value only exists for the warehouse transaction. TranSrc = "4".  For the Issue side of the transaction it identifies the Bin location that the quantity is transferred in to. On the Receipt side of the transaction it identifies the Bin location that the quantity was transferred from.  */  
   BinNum2:string,
      /**   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  */  
   OrderNum:number,
      /**  The sales order line that this transaction is associated with.  */  
   OrderLine:number,
      /**  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  */  
   OrderRelNum:number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  */  
   EntryPerson:string,
      /**  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  */  
   TranReference:string,
      /**  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   PartDescription:string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part, JobOPer, JobMtl, ShipDtl,  SubShipD ....  */  
   RevisionNum:string,
      /**  The internal key that along with PurPoint is used to tie back to the VendorPP master file. Applicable for shipments to subcontractors (MFG-VEN) and receipts (PUR-STK, PUR-MTL, PUR-SUB, PUR-UKN).  */  
   VendorNum:number,
      /**  Vendor purchase point ID. (see VendorNum)  */  
   PurPoint:string,
      /**  Quantity received against a purchase order in the vendors unit of measure.  */  
   POReceiptQty:number,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the PO detail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the MtlUnitCost field which is used as cost to job or stock.  */  
   POUnitCost:number,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  Invoice Number from corresponding APInvHed record. Applicable only with the purchase variance adjustment record (TranType = "ADJ-PUR") generated via A/P invoice posting.  */  
   InvoiceNum:string,
      /**  Used along with InvoiceNum to relate to the corresponding APInvDtl record that generated this PartTran record. (see PartTran.InvoiceNum)  */  
   InvoiceLine:number,
      /**  Inventory Adjustment Source for ADJ-QTY, ADJ-CST transaction types only.  "P" = Physical Inventory Count, "C" = Cycle Inventory Count, "O" = Other Adjustment  */  
   InvAdjSrc:string,
      /**  Used for Inventory Adjustment Source "Other" OR MTL-DMR, STK-DMR, SUB-DMR, or INS-DMR transaction types.  Refers to the Reason table.  */  
   InvAdjReason:string,
      /**  Lot Number  */  
   LotNum:string,
      /**  Unique dimension code for the part.  */  
   DimCode:string,
      /**  Dimension unit of measure.  */  
   DUM:string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   DimConvFactor:number,
      /**  Transfer "From/To" lot number.  */  
   LotNum2:string,
      /**  Transfer "From/To" Part Dimension  */  
   DimCode2:string,
      /**  Transfer "From/To" Dimension unit of measure.  */  
   DUM2:string,
      /**  Transfer "From/To" Dimension conversion factor.  */  
   DimConvFactor2:number,
      /**  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  For example: Adj-Cst for other than the parts costing method are not posted to G/L.  */  
   GLTrans:boolean,
      /**  Indicates if transaction was posted to G/L.  Transactions are posted in summary form via the Job Management Capture COS/WIP process .  */  
   PostedToGL:boolean,
      /**   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  */  
   FiscalYear:number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   FiscalPeriod:number,
      /**   Journal number that entry was posted to.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  The "Costed" field indicates if the Capture COS/Wip Activity has run on that part transaction. If "Yes" the transaction costs cant be changed anymore.  */  
   Costed:boolean,
      /**  DMR number used to identify the related DMR record.  */  
   DMRNum:number,
      /**  DMR action number  */  
   ActionNum:number,
      /**  RMA Number  */  
   RMANum:number,
      /**   If the amount of this PartTran was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped, its costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  */  
   COSPostingReqd:boolean,
      /**  Journal Code of the related GLJrnDtl.  */  
   JournalCode:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Site Identifier.  */  
   Plant2:string,
      /**  Reference to the service call that the material is being issued for.  */  
   CallNum:number,
      /**  Reference to the service call line  that the material is being issued for.  */  
   CallLine:number,
      /**  Reference to the service call line Material sequence that the material is being issued for.  */  
   MatNum:number,
      /**  Job Number of transfer source/target.  */  
   JobNum2:string,
      /**  Assembly Sequence  of transfer source/target.  */  
   AssemblySeq2:number,
      /**  Seq # of transfer source/target.  */  
   JobSeq2:number,
      /**   NOTE: Applies only to the RMA-INS transactions.
Contains the system internal customer number of the related customer record. 
Not directly updateable, updated via the RmaRcpt write trigger.  */  
   CustNum:number,
      /**  Line number of the related RMADtl record.  */  
   RMALine:number,
      /**  RMA Receipt  */  
   RMAReceipt:number,
      /**  RMA Disposition  */  
   RMADisp:number,
      /**  Other division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of Site transaction costs.  OtherDivValue only applies to Site to Site transactions (TranType="PLT-" and Site <> S  */  
   OtherDivValue:number,
      /**  Site Transaction Number  */  
   PlantTranNum:number,
      /**  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  */  
   NonConfID:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlMtlUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlLabUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlSubUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   MtlBurdenUnitCost:number,
      /**  Link to the related GLRefTyp.RefType.  */  
   RefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  On Hand Quantity before the part costing calculations were run.  */  
   BeginQty:number,
      /**  On Hand Quantity after part costing calculation were run.  */  
   AfterQty:number,
      /**  Burden Unit cost before the part costing calculation was run  */  
   BegBurUnitCost:number,
      /**  Labor Unit cost before the costing calculation was run  */  
   BegLbrUnitCost:number,
      /**  Material Burden Unit Cost before the costing calculation was run  */  
   BegMtlBurUnitCost:number,
      /**  Material Unit Cost before the costing calculation was run  */  
   BegMtlUnitCost:number,
      /**  Sub Contract Unit Cost before the costing calculation was run  */  
   BegSubUnitCost:number,
      /**  Burden Unit cost after the part costing calculation was run  */  
   AfterBurUnitCost:number,
      /**  Labor Unit Cost after the costing calculation was run  */  
   AfterLbrUnitCost:number,
      /**  Material Burden Unit Cost after the costing calculation was run  */  
   AfterMtlBurUnitCost:number,
      /**  Material Unit Cost after the costing calculation was run  */  
   AfterMtlUnitCost:number,
      /**  Sub Contract Unit Cost after the costing calculation was run  */  
   AfterSubUnitCost:number,
      /**  To Site division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of To Site transaction costs.  SiteCostValue only applies to Site to Site transactions (TranType="PLT-" and Site  */  
   PlantCostValue:number,
      /**  The Shop Employee ID of the user that created this transaction.  */  
   EmpID:string,
      /**  The unique identifier of the DemandReconcile that created this PartTran record.  */  
   ReconcileNum:number,
      /**  Id to the Cost Set Group that is used as the default CostGrp.  */  
   CostID:string,
      /**  For FIFO costed part, use this date to find the FIFO cost queue record affected by this transaction.  */  
   FIFODate:string,
      /**  For FIFO costed part, use this sequence number to find the FIFO cost queue record affected by this transaction.  */  
   FIFOSeq:number,
      /**   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  */  
   ActTranQty:number,
      /**  Actual Unit of Measure of the ActTransQty.  */  
   ActTransUOM:string,
      /**  The Inventory Tracking Unit of Measure that transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  */  
   InvtyUOM:string,
      /**  The Inventory Tracking Unit of Measure that inventory transfer transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  */  
   InvtyUOM2:string,
      /**   Internal flag to indicate what type of FIFO update is needed.  Valid values are: (A/U/D)
"A" - Add new FIFO cost queue
"U" - Update existing FIFO cost queue
"D" - Delete existing FIFO cost queue (Technically, this is more of voiding/deactivating the FIFO since we don't delete historical FIFO records).  */  
   FIFOAction:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  */  
   BinType:string,
      /**  Calendar year of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  */  
   CCYear:number,
      /**  Calendar month of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl..  */  
   CCMonth:number,
      /**  CycleSeq of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  */  
   CycleSeq:number,
      /**  GUID - reference on PE ABT.  */  
   ABTUID:string,
      /**  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the PartSite.CostMethod or Part.CostMethod  */  
   BaseCostMethod:string,
      /**   Revert Status field, with following values:
0.	Not reverted (default initial value)
1.	Reverted  */  
   RevertStatus:number,
      /**  Reference on revert line  by SySRowID.  */  
   RevertID:string,
      /**  Drop shipment Packing Slip.  */  
   DropShipPackSlip:string,
      /**   PartTran.VarTarget, with following values:
'JOB' ? Use Job Expense Account
'STK' ? Use Inventory Account
'VAR' ? Use Purchase Variance Account
'INS' ? Use Inspection Account
'UKN' ? Expense Account (Miscellaneous receipt)
'MTL' ? Use WIP Material Account
'SUB' ? Use WIP Subcontract account
'DMR' ? Use DMR account
'REJ' ? Use DMR Write off Account
'ACA' ? Use Actual Cost Account  */  
   VarTarget:string,
      /**  The FIFO subsequence number of the related PartFIFOCost record.  */  
   FIFOSubSeq:number,
      /**  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltMtlUnitCost:number,
      /**  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltLbrUnitCost:number,
      /**  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltBurUnitCost:number,
      /**  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltSubUnitCost:number,
      /**  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltMtlBurUnitCost:number,
      /**  Alternate FIFO Extended Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltExtCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlMtlUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlLabUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlSubUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlBurdenUnitCost:number,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Invoice Number from Progress Billing Invoice preparation  */  
   PBInvNum:number,
      /**   This is only relevant for TranType MFG-MFG.
Valid types are '' , 'L', and 'B'.  
For Transfers, set to ''.
For Loans and Repayment of Loans set PartTran. LoanType to either 'L' or 'B' based on PartTran.JobNum.  If PartTran.JobNum is the job who is making the loan (or who made the loan, in the case of a repayment), then set to 'L' (loaner).  If PartTran.JobNum is the job who originally received the loan or who is receiving a loan set to 'B' (borrower).  */  
   LoanFlag:string,
      /**  Unique identifier of the Asset.  */  
   AssetNum:string,
      /**  Unique number to identify the Addition activity of an asset.  */  
   AdditionNum:number,
      /**  Unique number to identify the Disposal activity of an asset.  */  
   DisposalNum:number,
      /**  Logical field to indicate if this record has been read by project analysis process.  */  
   ProjProcessed:boolean,
      /**  Used by Project Analysis process.  */  
   AsOfDate:string,
      /**  Used By Project Analysis Process  */  
   AsOfSeq:number,
      /**  Like RcvMisc.MscNum. Filled only for ADJ-PUR transactions created from late costs.  */  
   MscNum:number,
      /**  ODC Unit Cost  */  
   ODCUnitCost:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  TranRefType  */  
   TranRefType:number,
      /**  PCID  */  
   PCID:string,
      /**  PCIDCollapseCounter  */  
   PCIDCollapseCounter:number,
      /**  PCID2  */  
   PCID2:string,
      /**  ContractID  */  
   ContractID:string,
      /**  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  */  
   LCFlag:boolean,
      /**  ExtMtlCost  */  
   ExtMtlCost:number,
      /**  ExtLbrCost  */  
   ExtLbrCost:number,
      /**  ExtBurCost  */  
   ExtBurCost:number,
      /**  ExtSubCost  */  
   ExtSubCost:number,
      /**  ExtMtlBurCost  */  
   ExtMtlBurCost:number,
      /**  ExtMtlMtlCost  */  
   ExtMtlMtlCost:number,
      /**  ExtMtlLabCost  */  
   ExtMtlLabCost:number,
      /**  ExtMtlSubCost  */  
   ExtMtlSubCost:number,
      /**  ExtMtlBurdenCost  */  
   ExtMtlBurdenCost:number,
      /**  MYImportNum  */  
   MYImportNum:string,
      /**  AutoReverse  */  
   AutoReverse:boolean,
      /**  RevTranNum  */  
   RevTranNum:number,
      /**  RevSysDate  */  
   RevSysDate:string,
      /**  RevSysTime  */  
   RevSysTime:number,
      /**  The Non Recoverable Tax that has been included on the Extended Cost.  This will be calculated from the Receipt Header and Receipt Line tax records by subtracting the total deductable tax from the total tax.  */  
   ExtNonRecoverableCost:number,
      /**  True if transaction is related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  WIPPCID  */  
   WIPPCID:string,
      /**  WIPPCID2  */  
   WIPPCID2:string,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   CallCode:string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   ContractCode:string,
   DIMDescription:string,
      /**  Part field objects must be enabled when the Final Assembly (0) is selected and the Job has multiple end parts.  */  
   DisableFieldPart:boolean,
      /**  Display format of System Time in Hrs:Min.  */  
   DispSysTime:string,
   DispUOM:string,
   dummyKeyField:string,
   EnableSerialNumbers:boolean,
      /**  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  */  
   FSAAction:string,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   FSACallCode:string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   FSAContractCode:string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   FSAContractNum:number,
      /**  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  */  
   FSAEmpID:string,
      /**  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  */  
   FSAEquipmentInstallID:number,
      /**  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  */  
   FSAEquipmentPartNum:string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderNum:number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderResourceNum:number,
      /**  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  */  
   FSAWarrantyCode:string,
      /**  If InvAdjSrc = "P", then this field is true, InvAdjSrc = "C", then this field is false  */  
   FullPhysical:boolean,
      /**  GL Journal Source Transaction Amount  */  
   GLTranAmt:number,
      /**  GL Journal Source Transaction Date  */  
   GLTranDate:string,
      /**  Inventory subcontract unit cost  */  
   InvBurUnitCost:number,
      /**  Inventory Labor unit cost.  */  
   InvLbrUnitCost:number,
      /**  Inventory burden unit cost  */  
   InvMtlBurUnitCost:number,
      /**  Inventory material unit cost  */  
   InvMtlUnitCost:number,
      /**  Inventory subcontract unit cost.  */  
   InvSubUnitCost:number,
   IssuedComplete:boolean,
   JobBurUnitCost:number,
   JobLbrUnitCost:number,
   JobMtlBurUnitCost:number,
   JobMtlUnitCost:number,
   JobSubUnitCost:number,
   LegalNumberNumber:string,
   LegalNumberPrefix:string,
   LegalNumberPrefixList:string,
   LegalNumberReadOnlyFields:string,
   LegalNumberYear:number,
   MtlLbrUnitCost:number,
   MtlQueueRowId:string,
      /**  Used/Set only by MfgReceipts - Indicates if Job has multiple end parts.  */  
   MultiEndParts:boolean,
   OnHandQty:number,
      /**  Override Costs.  Set to yes if the user chooses to override the cost.  */  
   OverRideCosts:boolean,
   PartDescriptionAsm:string,
   PartDescriptionJH:string,
   PartDescriptionMS:string,
   PartDescriptionSP:string,
   PartNumAsm:string,
   PartNumJH:string,
   PartNumMS:string,
   PartNumSP:string,
   QtyAvailToComplete:number,
   QtyBearing:boolean,
      /**  Quantity Completed  */  
   QtyCompleted:number,
   RevisionNumRevDescription:string,
   RevisionNumRevShortDesc:string,
   SalvageQtyToDate:number,
   SerialNoTempTranID:number,
   ThisTranQty:number,
      /**  Transaction Amount  */  
   TranAmount:number,
   TreeDisplay:string,
      /**  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  */  
   WarrantyCode:string,
      /**  Contract Created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   ContractNum:number,
   CostMethodDisplay:string,
      /**  Number of pieces for inventory attribute tracked parts  */  
   DispNumberOfPieces:number,
   RevisionNumAsm:string,
   RevisionNumMS:string,
   RevisionNumSP:string,
   PlantConfCtrlEnablePackageControl:boolean,
      /**  Description for AttributeSetID associated with PartNumMS  */  
   AttributeSetDescriptionMS:string,
      /**  AttributeSetID associated with PartNumMS  */  
   AttributeSetIDMS:number,
      /**  AttributeSetShortDescription associated with PartNumMS  */  
   AttributeSetShortDescriptionMS:string,
   BitFlag:number,
   AssemblySeqDescription:string,
   BinNumDescription:string,
   CallLineLineDesc:string,
   CustNumCustID:string,
   CustNumBTName:string,
   CustNumName:string,
   DimCodeDimCodeDescription:string,
   DMRNumPartDescription:string,
   FromBinDescription:string,
   FromPlantName:string,
   FromWareHouseDescription:string,
   InvoiceNumDescription:string,
   JobNumPartDescription:string,
   MatNumLineDesc:string,
   OrderLineLineDesc:string,
   OrderNumCardMemberName:string,
   OrderNumCurrencyCode:string,
   PackLineLineDesc:string,
   PackNumName:string,
   PartLotPartLotDescription:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumSellingFactor:number,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   PartNumTrackLots:boolean,
   PartNumIUM:string,
   PartNumPartDescription:string,
   PartNumSalesUM:string,
   PartNumPricePerCode:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumAttrClassID:string,
   PlantName:string,
   POLineVenPartNum:string,
   POLinePartNum:string,
   POLineLineDesc:string,
   RMALineLineDesc:string,
   VendorNumName:string,
   VendorNumAddress3:string,
   VendorNumDefaultFOB:string,
   VendorNumCurrencyCode:string,
   VendorNumState:string,
   VendorNumAddress1:string,
   VendorNumAddress2:string,
   VendorNumVendorID:string,
   VendorNumCountry:string,
   VendorNumCity:string,
   VendorNumZIP:string,
   VendorNumTermsCode:string,
   VendorPPNumAddress1:string,
   VendorPPNumAddress2:string,
   VendorPPNumPrimPCon:number,
   VendorPPNumAddress3:string,
   VendorPPNumCountry:string,
   VendorPPNumState:string,
   VendorPPNumZip:string,
   VendorPPNumCity:string,
   VendorPPNumName:string,
   WarehouseDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartTranTableset{
   PartTran:Erp_Tablesets_PartTranRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPartTranTableset{
   PartTran:Erp_Tablesets_PartTranRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param sysDate
      @param sysTime
      @param tranNum
   */  
export interface GetByID_input{
   sysDate:string,
   sysTime:number,
   tranNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PartTranTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PartTranTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PartTranTableset[],
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
   returnObj:Erp_Tablesets_PartTranListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param sysDate
      @param sysTime
   */  
export interface GetNewPartTran_input{
   ds:Erp_Tablesets_PartTranTableset[],
   sysDate:string,
   sysTime:number,
}

export interface GetNewPartTran_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartTranTableset,
}
}

   /** Required : 
      @param whereClausePartTran
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePartTran:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PartTranTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param mode
   */  
export interface GetWhereClause_input{
   mode:string,
}

export interface GetWhereClause_output{
   returnObj:string,
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
   ds:Erp_Tablesets_UpdExtPartTranTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPartTranTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PartTranTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartTranTableset,
}
}

