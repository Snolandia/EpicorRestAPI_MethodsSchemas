import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ShopWrnSvc
// Description: Labor warning for a specific labor detail or header record -
           used with shop Tracker and data collection, labor entry, labor edit list
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/$metadata", {
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
   Description: Get ShopWrns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShopWrns
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShopWrnRow
   */  
export function get_ShopWrns(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShopWrnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/ShopWrns", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShopWrnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShopWrns
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShopWrnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ShopWrnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ShopWrns(requestBody:Erp_Tablesets_ShopWrnRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/ShopWrns", {
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
   Summary: Calls GetByID to retrieve the ShopWrn item
   Description: Calls GetByID to retrieve the ShopWrn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShopWrn
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param WarnType Desc: WarnType   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param LabWarnNum Desc: LabWarnNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ShopWrnRow
   */  
export function get_ShopWrns_Company_WarnType_LaborHedSeq_LaborDtlSeq_LabWarnNum(Company:string, WarnType:string, LaborHedSeq:string, LaborDtlSeq:string, LabWarnNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShopWrnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/ShopWrns(" + Company + "," + WarnType + "," + LaborHedSeq + "," + LaborDtlSeq + "," + LabWarnNum + ")", {
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
         resolve(data as Erp_Tablesets_ShopWrnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ShopWrn for the service
   Description: Calls UpdateExt to update ShopWrn. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShopWrn
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param WarnType Desc: WarnType   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param LabWarnNum Desc: LabWarnNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShopWrnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ShopWrns_Company_WarnType_LaborHedSeq_LaborDtlSeq_LabWarnNum(Company:string, WarnType:string, LaborHedSeq:string, LaborDtlSeq:string, LabWarnNum:string, requestBody:Erp_Tablesets_ShopWrnRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/ShopWrns(" + Company + "," + WarnType + "," + LaborHedSeq + "," + LaborDtlSeq + "," + LabWarnNum + ")", {
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
   Summary: Call UpdateExt to delete ShopWrn item
   Description: Call UpdateExt to delete ShopWrn item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShopWrn
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param WarnType Desc: WarnType   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param LabWarnNum Desc: LabWarnNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ShopWrns_Company_WarnType_LaborHedSeq_LaborDtlSeq_LabWarnNum(Company:string, WarnType:string, LaborHedSeq:string, LaborDtlSeq:string, LabWarnNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/ShopWrns(" + Company + "," + WarnType + "," + LaborHedSeq + "," + LaborDtlSeq + "," + LabWarnNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShopWrnListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShopWrnListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShopWrnListRow)
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
export function get_GetRows(whereClauseShopWrn:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseShopWrn!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseShopWrn=" + whereClauseShopWrn
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/GetRows" + params, {
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
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(warnType:string, laborHedSeq:string, laborDtlSeq:string, labWarnNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof warnType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "warnType=" + warnType
   }
   if(typeof laborHedSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "laborHedSeq=" + laborHedSeq
   }
   if(typeof laborDtlSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "laborDtlSeq=" + laborDtlSeq
   }
   if(typeof labWarnNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "labWarnNum=" + labWarnNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/GetList" + params, {
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
   Summary: Invoke method MoveToHistory
   Description: Set MoveToHistory flag
   OperationID: MoveToHistory
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MoveToHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveToHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MoveToHistory(requestBody:MoveToHistory_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MoveToHistory_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/MoveToHistory", {
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
         resolve(data as MoveToHistory_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MoveAllToHistory
   Description: Set MoveAllToHistory flag
This is just for Kinetic UI
   OperationID: MoveAllToHistory
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MoveAllToHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveAllToHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MoveAllToHistory(requestBody:MoveAllToHistory_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MoveAllToHistory_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/MoveAllToHistory", {
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
         resolve(data as MoveAllToHistory_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MoveAllToHistoryTrackerNoDataSet
   Description: Set CurrWarn flag to false for all records in Shop Tracker
without passing a dataset
This is just for Kinetic UI
   OperationID: MoveAllToHistoryTrackerNoDataSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveAllToHistoryTrackerNoDataSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MoveAllToHistoryTrackerNoDataSet(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MoveAllToHistoryTrackerNoDataSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/MoveAllToHistoryTrackerNoDataSet", {
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
         resolve(data as MoveAllToHistoryTrackerNoDataSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewShopWrn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShopWrn
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewShopWrn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShopWrn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewShopWrn(requestBody:GetNewShopWrn_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewShopWrn_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/GetNewShopWrn", {
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
         resolve(data as GetNewShopWrn_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShopWrnSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShopWrnListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ShopWrnListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShopWrnRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ShopWrnRow,
}

export interface Erp_Tablesets_ShopWrnListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  An integer assigned by the system to uniquely identify the LaborHed record. This integer is created by using the database sequence "LaborHedSeq".  */  
   "LaborHedSeq":number,
      /**  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  */  
   "LaborDtlSeq":number,
      /**  Identifies a Labor warning  */  
   "LabWarnNum":number,
      /**  Shop Tracker viewed warnings are initially set to True for easy review; all others are set to False.  */  
   "CurrWarn":boolean,
      /**  The Date the event that created the warning occurred  */  
   "EventDate":string,
      /**  The Time the event was created in seconds since midnight.  */  
   "EventTime":number,
      /**  Message warning text(e.g. with scrap/rework reason etc.)  */  
   "MsgText":string,
      /**  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  */  
   "JobNum":string,
      /**  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  */  
   "AssemblySeq":number,
      /**   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  */  
   "EmployeeNum":string,
      /**   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  */  
   "OprSeq":number,
      /**   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group master.
For production labor (LaborType = "S" or "P") the default is from the JobOper.WcCode.
For indirect labor (LaborType = I) there is no default.  */  
   "ResourceGrpID":string,
      /**   The percentage that this operation varied. Greater than the limit
from the Warning table.  */  
   "VariancePct":number,
      /**  Indicates if this is a labor or Material warning  */  
   "WarnType":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Employee's full name  */  
   "EmployeeNumName":string,
      /**  Employee Supervisor name  */  
   "EmployeeNumSupervisorName":string,
      /**  The EventTime converted to HH:MM:SS  */  
   "DspEventTime":string,
      /**  Translated message text  */  
   "TransMsgText":string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   "AssemblySeqDescription":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "JobNumPartDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ShopWrnRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  An integer assigned by the system to uniquely identify the LaborHed record. This integer is created by using the database sequence "LaborHedSeq".  */  
   "LaborHedSeq":number,
      /**  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  */  
   "LaborDtlSeq":number,
      /**  Identifies a Labor warning  */  
   "LabWarnNum":number,
      /**  Shop Tracker viewed warnings are initially set to True for easy review; all others are set to False.  */  
   "CurrWarn":boolean,
      /**  The Date the event that created the warning occurred  */  
   "EventDate":string,
      /**  The Time the event was created in seconds since midnight.  */  
   "EventTime":number,
      /**  Message warning text(e.g. with scrap/rework reason etc.)  */  
   "MsgText":string,
      /**  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  */  
   "JobNum":string,
      /**  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  */  
   "AssemblySeq":number,
      /**   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  */  
   "EmployeeNum":string,
      /**   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  */  
   "OprSeq":number,
      /**   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group master.
For production labor (LaborType = "S" or "P") the default is from the JobOper.WcCode.
For indirect labor (LaborType = I) there is no default.  */  
   "ResourceGrpID":string,
      /**   The percentage that this operation varied. Greater than the limit
from the Warning table.  */  
   "VariancePct":number,
      /**  Indicates if this is a labor or Material warning  */  
   "WarnType":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Employee's full name  */  
   "EmployeeNumName":string,
      /**  Employee Supervisor name  */  
   "EmployeeNumSupervisorName":string,
      /**  The EventTime converted to HH:MM:SS  */  
   "DspEventTime":string,
      /**  Translated message text  */  
   "TransMsgText":string,
   "BitFlag":number,
   "AssemblySeqDescription":string,
   "EmpBasicNameSupervisorID":string,
   "EmpBasicNameName":string,
   "JobNumPartDescription":string,
   "WarningRptShpTracker":boolean,
   "WarningRptDataCollect":boolean,
   "WarningRptLbrEnt":boolean,
   "WarningRptLbrEdit":boolean,
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
      @param warnType
      @param laborHedSeq
      @param laborDtlSeq
      @param labWarnNum
   */  
export interface DeleteByID_input{
   warnType:string,
   laborHedSeq:number,
   laborDtlSeq:number,
   labWarnNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ShopWrnListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  An integer assigned by the system to uniquely identify the LaborHed record. This integer is created by using the database sequence "LaborHedSeq".  */  
   LaborHedSeq:number,
      /**  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  */  
   LaborDtlSeq:number,
      /**  Identifies a Labor warning  */  
   LabWarnNum:number,
      /**  Shop Tracker viewed warnings are initially set to True for easy review; all others are set to False.  */  
   CurrWarn:boolean,
      /**  The Date the event that created the warning occurred  */  
   EventDate:string,
      /**  The Time the event was created in seconds since midnight.  */  
   EventTime:number,
      /**  Message warning text(e.g. with scrap/rework reason etc.)  */  
   MsgText:string,
      /**  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  */  
   JobNum:string,
      /**  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  */  
   AssemblySeq:number,
      /**   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  */  
   EmployeeNum:string,
      /**   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  */  
   OprSeq:number,
      /**   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group master.
For production labor (LaborType = "S" or "P") the default is from the JobOper.WcCode.
For indirect labor (LaborType = I) there is no default.  */  
   ResourceGrpID:string,
      /**   The percentage that this operation varied. Greater than the limit
from the Warning table.  */  
   VariancePct:number,
      /**  Indicates if this is a labor or Material warning  */  
   WarnType:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Employee's full name  */  
   EmployeeNumName:string,
      /**  Employee Supervisor name  */  
   EmployeeNumSupervisorName:string,
      /**  The EventTime converted to HH:MM:SS  */  
   DspEventTime:string,
      /**  Translated message text  */  
   TransMsgText:string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   AssemblySeqDescription:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   JobNumPartDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ShopWrnListTableset{
   ShopWrnList:Erp_Tablesets_ShopWrnListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ShopWrnRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  An integer assigned by the system to uniquely identify the LaborHed record. This integer is created by using the database sequence "LaborHedSeq".  */  
   LaborHedSeq:number,
      /**  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  */  
   LaborDtlSeq:number,
      /**  Identifies a Labor warning  */  
   LabWarnNum:number,
      /**  Shop Tracker viewed warnings are initially set to True for easy review; all others are set to False.  */  
   CurrWarn:boolean,
      /**  The Date the event that created the warning occurred  */  
   EventDate:string,
      /**  The Time the event was created in seconds since midnight.  */  
   EventTime:number,
      /**  Message warning text(e.g. with scrap/rework reason etc.)  */  
   MsgText:string,
      /**  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  */  
   JobNum:string,
      /**  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  */  
   AssemblySeq:number,
      /**   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  */  
   EmployeeNum:string,
      /**   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  */  
   OprSeq:number,
      /**   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group master.
For production labor (LaborType = "S" or "P") the default is from the JobOper.WcCode.
For indirect labor (LaborType = I) there is no default.  */  
   ResourceGrpID:string,
      /**   The percentage that this operation varied. Greater than the limit
from the Warning table.  */  
   VariancePct:number,
      /**  Indicates if this is a labor or Material warning  */  
   WarnType:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Employee's full name  */  
   EmployeeNumName:string,
      /**  Employee Supervisor name  */  
   EmployeeNumSupervisorName:string,
      /**  The EventTime converted to HH:MM:SS  */  
   DspEventTime:string,
      /**  Translated message text  */  
   TransMsgText:string,
   BitFlag:number,
   AssemblySeqDescription:string,
   EmpBasicNameSupervisorID:string,
   EmpBasicNameName:string,
   JobNumPartDescription:string,
   WarningRptShpTracker:boolean,
   WarningRptDataCollect:boolean,
   WarningRptLbrEnt:boolean,
   WarningRptLbrEdit:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ShopWrnTableset{
   ShopWrn:Erp_Tablesets_ShopWrnRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtShopWrnTableset{
   ShopWrn:Erp_Tablesets_ShopWrnRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param warnType
      @param laborHedSeq
      @param laborDtlSeq
      @param labWarnNum
   */  
export interface GetByID_input{
   warnType:string,
   laborHedSeq:number,
   laborDtlSeq:number,
   labWarnNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ShopWrnTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ShopWrnTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ShopWrnTableset[],
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
   returnObj:Erp_Tablesets_ShopWrnListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param warnType
      @param laborHedSeq
      @param laborDtlSeq
   */  
export interface GetNewShopWrn_input{
   ds:Erp_Tablesets_ShopWrnTableset[],
   warnType:string,
   laborHedSeq:number,
   laborDtlSeq:number,
}

export interface GetNewShopWrn_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ShopWrnTableset,
}
}

   /** Required : 
      @param whereClauseShopWrn
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseShopWrn:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ShopWrnTableset[],
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

export interface MoveAllToHistoryTrackerNoDataSet_output{
}

   /** Required : 
      @param ds
   */  
export interface MoveAllToHistory_input{
   ds:Erp_Tablesets_ShopWrnTableset[],
}

export interface MoveAllToHistory_output{
}

   /** Required : 
      @param ds
   */  
export interface MoveToHistory_input{
   ds:Erp_Tablesets_ShopWrnTableset[],
}

export interface MoveToHistory_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ShopWrnTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtShopWrnTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtShopWrnTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ShopWrnTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ShopWrnTableset,
}
}

