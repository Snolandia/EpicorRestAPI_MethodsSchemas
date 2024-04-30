import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.StockProvisionFormatSvc
// Description: BL logic for Stock Provision Format Maintenance
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/$metadata", {
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
   Description: Get StockProvisionFormats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_StockProvisionFormats
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.StockProvisionFormatRow
   */  
export function get_StockProvisionFormats(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_StockProvisionFormatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/StockProvisionFormats", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_StockProvisionFormatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_StockProvisionFormats
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.StockProvisionFormatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.StockProvisionFormatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_StockProvisionFormats(requestBody:Erp_Tablesets_StockProvisionFormatRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/StockProvisionFormats", {
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
   Summary: Calls GetByID to retrieve the StockProvisionFormat item
   Description: Calls GetByID to retrieve the StockProvisionFormat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_StockProvisionFormat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param StockProvFmtCode Desc: StockProvFmtCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.StockProvisionFormatRow
   */  
export function get_StockProvisionFormats_Company_StockProvFmtCode(Company:string, StockProvFmtCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_StockProvisionFormatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/StockProvisionFormats(" + Company + "," + StockProvFmtCode + ")", {
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
         resolve(data as Erp_Tablesets_StockProvisionFormatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update StockProvisionFormat for the service
   Description: Calls UpdateExt to update StockProvisionFormat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_StockProvisionFormat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param StockProvFmtCode Desc: StockProvFmtCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.StockProvisionFormatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_StockProvisionFormats_Company_StockProvFmtCode(Company:string, StockProvFmtCode:string, requestBody:Erp_Tablesets_StockProvisionFormatRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/StockProvisionFormats(" + Company + "," + StockProvFmtCode + ")", {
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
   Summary: Call UpdateExt to delete StockProvisionFormat item
   Description: Call UpdateExt to delete StockProvisionFormat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_StockProvisionFormat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param StockProvFmtCode Desc: StockProvFmtCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_StockProvisionFormats_Company_StockProvFmtCode(Company:string, StockProvFmtCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/StockProvisionFormats(" + Company + "," + StockProvFmtCode + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.StockProvisionFormatListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_StockProvisionFormatListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_StockProvisionFormatListRow)
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
export function get_GetRows(whereClauseStockProvisionFormat:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseStockProvisionFormat!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseStockProvisionFormat=" + whereClauseStockProvisionFormat
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/GetRows" + params, {
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
export function get_GetByID(stockProvFmtCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof stockProvFmtCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "stockProvFmtCode=" + stockProvFmtCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/GetList" + params, {
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
   Summary: Invoke method GetTranTypeList
   Description: This method provides a list of values and description for Tran Types.
   OperationID: GetTranTypeList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTranTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTranTypeList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTranTypeList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/GetTranTypeList", {
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
         resolve(data as GetTranTypeList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeActive
   Description: Purpose:
Parameters:  none
Notes:
<param name="ds">The StockProvisionFormat data set</param>
   OperationID: OnChangeActive
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeActive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeActive_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeActive(requestBody:OnChangeActive_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeActive_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/OnChangeActive", {
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
         resolve(data as OnChangeActive_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeType
   Description: This method validates the StockProvisionFormat.Type when changed in UI form.
           ///
   OperationID: OnChangeType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeType(requestBody:OnChangeType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/OnChangeType", {
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
         resolve(data as OnChangeType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTimeModifierCodeDescList
   Description: Purpose: Gets the list of codes/descriptions for Time Modifier combo-box
Parameters: none
   OperationID: GetTimeModifierCodeDescList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTimeModifierCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTimeModifierCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTimeModifierCodeDescList(requestBody:GetTimeModifierCodeDescList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTimeModifierCodeDescList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/GetTimeModifierCodeDescList", {
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
         resolve(data as GetTimeModifierCodeDescList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:GetCodeDescList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCodeDescList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/GetCodeDescList", {
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
         resolve(data as GetCodeDescList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadTranTypeDS
   Description: Seperates delimeted list into individual IDs
   OperationID: LoadTranTypeDS
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadTranTypeDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadTranTypeDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadTranTypeDS(requestBody:LoadTranTypeDS_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadTranTypeDS_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/LoadTranTypeDS", {
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
         resolve(data as LoadTranTypeDS_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewStockProvisionFormat
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewStockProvisionFormat
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewStockProvisionFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewStockProvisionFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewStockProvisionFormat(requestBody:GetNewStockProvisionFormat_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewStockProvisionFormat_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/GetNewStockProvisionFormat", {
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
         resolve(data as GetNewStockProvisionFormat_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_StockProvisionFormatListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_StockProvisionFormatListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_StockProvisionFormatRow{
   "odatametadata":string,
   "value":Erp_Tablesets_StockProvisionFormatRow,
}

export interface Erp_Tablesets_StockProvisionFormatListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The unique identifier for a stock provision format code. (PK)  */  
   "StockProvFmtCode":string,
      /**  Stock Provision report format description  */  
   "Description":string,
      /**  Indicates if the format is used on slow moving or excess or aging report. It can be "S" = Slow Moving, "E" = Excess or "A" = Aging  */  
   "Type":string,
      /**  Indicates if an excess report will be compared to consumption, forecast entries or future sales orders. . It can be C= Consumption, F= Forecast, S= Future sales orders  */  
   "ComparedTo":string,
      /**  Indicates if the time periods for the buckets are defines in days or months. It can be D= Days, M=Months  */  
   "TimeModifier":string,
      /**  Based on the time modifier, it indicates the starting date of the first bucket  */  
   "Bucket1Start":number,
      /**  Based on the time modifier, it indicates the ending date of the first bucket  */  
   "Bucket1End":number,
      /**  Indicates the rate to calculate the provision for the stock that falls in the first bucket.  */  
   "Bucket1Rate":number,
      /**  Contains the column heading used to describe the first bucket  */  
   "Bucket1Caption":string,
      /**  Flag which indicate if the second bucked will be used  */  
   "Bucket2Active":boolean,
      /**  Based on the ?time modifier?, it indicates the ending date of the second bucket  */  
   "Bucket2End":number,
      /**  Based on the time modifier, it indicates the ending date of the second bucket  */  
   "Bucket2Rate":number,
      /**  Contains the column heading used to describe the second bucket  */  
   "Bucket2Caption":string,
      /**  Flag which indicate if the third bucked will be used  */  
   "Bucket3Active":boolean,
      /**  Based on the time modifier, it indicates the ending date of the third bucket  */  
   "Bucket3End":number,
      /**  Indicates the rate to calculate the provision for the stock that falls in the third bucket.  */  
   "Bucket3Rate":number,
      /**  Contains the column heading used to describe the third bucket  */  
   "Bucket3Caption":string,
      /**  Flag which indicate if the fourth bucked will be used  */  
   "Bucket4Active":boolean,
      /**  Based on the time modifier, it indicates the ending date of the fourth bucket  */  
   "Bucket4End":number,
      /**  Indicates the rate to calculate the provision for the stock that falls in the fourth bucket.  */  
   "Bucket4Rate":number,
      /**  Contains the column heading used to describe the fourth bucket  */  
   "Bucket4Caption":string,
      /**  Flag which indicate if the fifth bucked will be used  */  
   "Bucket5Active":boolean,
      /**  Based on the time modifier, it indicates the ending date of the fifth bucket  */  
   "Bucket5End":number,
      /**  Indicates the rate to calculate the provision for the stock that falls in the fifth bucket.  */  
   "Bucket5Rate":number,
      /**  Contains the column heading used to describe the fifth bucket  */  
   "Bucket5Caption":string,
      /**  Flag which indicate if the sixth bucked will be used  */  
   "Bucket6Active":boolean,
      /**  Based on the time modifier, it indicates the ending date of the sixth bucket  */  
   "Bucket6End":number,
      /**  Indicates the rate to calculate the provision for the stock that falls in the sixth bucket.  */  
   "Bucket6Rate":number,
      /**  Contains the column heading used to describe the sixth bucket  */  
   "Bucket6Caption":string,
      /**  Delimited list of PartTran Transaction Types to be used for this Stock Provision Format to calculate last movement date.  */  
   "PartTranTypes":string,
      /**  Marks this StockProvisionFormat as global, available to be sent out to other companies.  */  
   "GlobalStockProvisionFormat":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates whether Type field should be enabled in the UI.  */  
   "EnableType":boolean,
      /**  Type description  */  
   "TypeDesc":string,
      /**  ComparedTo description  */  
   "ComparedToDesc":string,
      /**  TimeModifier description  */  
   "TimeModifierDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_StockProvisionFormatRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The unique identifier for a stock provision format code. (PK)  */  
   "StockProvFmtCode":string,
      /**  Stock Provision report format description  */  
   "Description":string,
      /**  Indicates if the format is used on slow moving or excess or aging report. It can be "S" = Slow Moving, "E" = Excess or "A" = Aging  */  
   "Type":string,
      /**  Indicates if an excess report will be compared to consumption, forecast entries or future sales orders. . It can be C= Consumption, F= Forecast, S= Future sales orders  */  
   "ComparedTo":string,
      /**  Indicates if the time periods for the buckets are defines in days or months. It can be D= Days, M=Months  */  
   "TimeModifier":string,
      /**  Based on the time modifier, it indicates the starting date of the first bucket  */  
   "Bucket1Start":number,
      /**  Based on the time modifier, it indicates the ending date of the first bucket  */  
   "Bucket1End":number,
      /**  Indicates the rate to calculate the provision for the stock that falls in the first bucket.  */  
   "Bucket1Rate":number,
      /**  Contains the column heading used to describe the first bucket  */  
   "Bucket1Caption":string,
      /**  Flag which indicate if the second bucked will be used  */  
   "Bucket2Active":boolean,
      /**  Based on the ?time modifier?, it indicates the ending date of the second bucket  */  
   "Bucket2End":number,
      /**  Based on the time modifier, it indicates the ending date of the second bucket  */  
   "Bucket2Rate":number,
      /**  Contains the column heading used to describe the second bucket  */  
   "Bucket2Caption":string,
      /**  Flag which indicate if the third bucked will be used  */  
   "Bucket3Active":boolean,
      /**  Based on the time modifier, it indicates the ending date of the third bucket  */  
   "Bucket3End":number,
      /**  Indicates the rate to calculate the provision for the stock that falls in the third bucket.  */  
   "Bucket3Rate":number,
      /**  Contains the column heading used to describe the third bucket  */  
   "Bucket3Caption":string,
      /**  Flag which indicate if the fourth bucked will be used  */  
   "Bucket4Active":boolean,
      /**  Based on the time modifier, it indicates the ending date of the fourth bucket  */  
   "Bucket4End":number,
      /**  Indicates the rate to calculate the provision for the stock that falls in the fourth bucket.  */  
   "Bucket4Rate":number,
      /**  Contains the column heading used to describe the fourth bucket  */  
   "Bucket4Caption":string,
      /**  Flag which indicate if the fifth bucked will be used  */  
   "Bucket5Active":boolean,
      /**  Based on the time modifier, it indicates the ending date of the fifth bucket  */  
   "Bucket5End":number,
      /**  Indicates the rate to calculate the provision for the stock that falls in the fifth bucket.  */  
   "Bucket5Rate":number,
      /**  Contains the column heading used to describe the fifth bucket  */  
   "Bucket5Caption":string,
      /**  Flag which indicate if the sixth bucked will be used  */  
   "Bucket6Active":boolean,
      /**  Based on the time modifier, it indicates the ending date of the sixth bucket  */  
   "Bucket6End":number,
      /**  Indicates the rate to calculate the provision for the stock that falls in the sixth bucket.  */  
   "Bucket6Rate":number,
      /**  Contains the column heading used to describe the sixth bucket  */  
   "Bucket6Caption":string,
      /**  Delimited list of PartTran Transaction Types to be used for this Stock Provision Format to calculate last movement date.  */  
   "PartTranTypes":string,
      /**  Marks this StockProvisionFormat as global, available to be sent out to other companies.  */  
   "GlobalStockProvisionFormat":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates whether Type field should be enabled in the UI.  */  
   "EnableType":boolean,
      /**  Type description  */  
   "TypeDesc":string,
      /**  ComparedTo description  */  
   "ComparedToDesc":string,
      /**  TimeModifier description  */  
   "TimeModifierDesc":string,
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
      @param stockProvFmtCode
   */  
export interface DeleteByID_input{
   stockProvFmtCode:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_StockProvisionFormatListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The unique identifier for a stock provision format code. (PK)  */  
   StockProvFmtCode:string,
      /**  Stock Provision report format description  */  
   Description:string,
      /**  Indicates if the format is used on slow moving or excess or aging report. It can be "S" = Slow Moving, "E" = Excess or "A" = Aging  */  
   Type:string,
      /**  Indicates if an excess report will be compared to consumption, forecast entries or future sales orders. . It can be C= Consumption, F= Forecast, S= Future sales orders  */  
   ComparedTo:string,
      /**  Indicates if the time periods for the buckets are defines in days or months. It can be D= Days, M=Months  */  
   TimeModifier:string,
      /**  Based on the time modifier, it indicates the starting date of the first bucket  */  
   Bucket1Start:number,
      /**  Based on the time modifier, it indicates the ending date of the first bucket  */  
   Bucket1End:number,
      /**  Indicates the rate to calculate the provision for the stock that falls in the first bucket.  */  
   Bucket1Rate:number,
      /**  Contains the column heading used to describe the first bucket  */  
   Bucket1Caption:string,
      /**  Flag which indicate if the second bucked will be used  */  
   Bucket2Active:boolean,
      /**  Based on the ?time modifier?, it indicates the ending date of the second bucket  */  
   Bucket2End:number,
      /**  Based on the time modifier, it indicates the ending date of the second bucket  */  
   Bucket2Rate:number,
      /**  Contains the column heading used to describe the second bucket  */  
   Bucket2Caption:string,
      /**  Flag which indicate if the third bucked will be used  */  
   Bucket3Active:boolean,
      /**  Based on the time modifier, it indicates the ending date of the third bucket  */  
   Bucket3End:number,
      /**  Indicates the rate to calculate the provision for the stock that falls in the third bucket.  */  
   Bucket3Rate:number,
      /**  Contains the column heading used to describe the third bucket  */  
   Bucket3Caption:string,
      /**  Flag which indicate if the fourth bucked will be used  */  
   Bucket4Active:boolean,
      /**  Based on the time modifier, it indicates the ending date of the fourth bucket  */  
   Bucket4End:number,
      /**  Indicates the rate to calculate the provision for the stock that falls in the fourth bucket.  */  
   Bucket4Rate:number,
      /**  Contains the column heading used to describe the fourth bucket  */  
   Bucket4Caption:string,
      /**  Flag which indicate if the fifth bucked will be used  */  
   Bucket5Active:boolean,
      /**  Based on the time modifier, it indicates the ending date of the fifth bucket  */  
   Bucket5End:number,
      /**  Indicates the rate to calculate the provision for the stock that falls in the fifth bucket.  */  
   Bucket5Rate:number,
      /**  Contains the column heading used to describe the fifth bucket  */  
   Bucket5Caption:string,
      /**  Flag which indicate if the sixth bucked will be used  */  
   Bucket6Active:boolean,
      /**  Based on the time modifier, it indicates the ending date of the sixth bucket  */  
   Bucket6End:number,
      /**  Indicates the rate to calculate the provision for the stock that falls in the sixth bucket.  */  
   Bucket6Rate:number,
      /**  Contains the column heading used to describe the sixth bucket  */  
   Bucket6Caption:string,
      /**  Delimited list of PartTran Transaction Types to be used for this Stock Provision Format to calculate last movement date.  */  
   PartTranTypes:string,
      /**  Marks this StockProvisionFormat as global, available to be sent out to other companies.  */  
   GlobalStockProvisionFormat:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates whether Type field should be enabled in the UI.  */  
   EnableType:boolean,
      /**  Type description  */  
   TypeDesc:string,
      /**  ComparedTo description  */  
   ComparedToDesc:string,
      /**  TimeModifier description  */  
   TimeModifierDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_StockProvisionFormatListTableset{
   StockProvisionFormatList:Erp_Tablesets_StockProvisionFormatListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_StockProvisionFormatRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The unique identifier for a stock provision format code. (PK)  */  
   StockProvFmtCode:string,
      /**  Stock Provision report format description  */  
   Description:string,
      /**  Indicates if the format is used on slow moving or excess or aging report. It can be "S" = Slow Moving, "E" = Excess or "A" = Aging  */  
   Type:string,
      /**  Indicates if an excess report will be compared to consumption, forecast entries or future sales orders. . It can be C= Consumption, F= Forecast, S= Future sales orders  */  
   ComparedTo:string,
      /**  Indicates if the time periods for the buckets are defines in days or months. It can be D= Days, M=Months  */  
   TimeModifier:string,
      /**  Based on the time modifier, it indicates the starting date of the first bucket  */  
   Bucket1Start:number,
      /**  Based on the time modifier, it indicates the ending date of the first bucket  */  
   Bucket1End:number,
      /**  Indicates the rate to calculate the provision for the stock that falls in the first bucket.  */  
   Bucket1Rate:number,
      /**  Contains the column heading used to describe the first bucket  */  
   Bucket1Caption:string,
      /**  Flag which indicate if the second bucked will be used  */  
   Bucket2Active:boolean,
      /**  Based on the ?time modifier?, it indicates the ending date of the second bucket  */  
   Bucket2End:number,
      /**  Based on the time modifier, it indicates the ending date of the second bucket  */  
   Bucket2Rate:number,
      /**  Contains the column heading used to describe the second bucket  */  
   Bucket2Caption:string,
      /**  Flag which indicate if the third bucked will be used  */  
   Bucket3Active:boolean,
      /**  Based on the time modifier, it indicates the ending date of the third bucket  */  
   Bucket3End:number,
      /**  Indicates the rate to calculate the provision for the stock that falls in the third bucket.  */  
   Bucket3Rate:number,
      /**  Contains the column heading used to describe the third bucket  */  
   Bucket3Caption:string,
      /**  Flag which indicate if the fourth bucked will be used  */  
   Bucket4Active:boolean,
      /**  Based on the time modifier, it indicates the ending date of the fourth bucket  */  
   Bucket4End:number,
      /**  Indicates the rate to calculate the provision for the stock that falls in the fourth bucket.  */  
   Bucket4Rate:number,
      /**  Contains the column heading used to describe the fourth bucket  */  
   Bucket4Caption:string,
      /**  Flag which indicate if the fifth bucked will be used  */  
   Bucket5Active:boolean,
      /**  Based on the time modifier, it indicates the ending date of the fifth bucket  */  
   Bucket5End:number,
      /**  Indicates the rate to calculate the provision for the stock that falls in the fifth bucket.  */  
   Bucket5Rate:number,
      /**  Contains the column heading used to describe the fifth bucket  */  
   Bucket5Caption:string,
      /**  Flag which indicate if the sixth bucked will be used  */  
   Bucket6Active:boolean,
      /**  Based on the time modifier, it indicates the ending date of the sixth bucket  */  
   Bucket6End:number,
      /**  Indicates the rate to calculate the provision for the stock that falls in the sixth bucket.  */  
   Bucket6Rate:number,
      /**  Contains the column heading used to describe the sixth bucket  */  
   Bucket6Caption:string,
      /**  Delimited list of PartTran Transaction Types to be used for this Stock Provision Format to calculate last movement date.  */  
   PartTranTypes:string,
      /**  Marks this StockProvisionFormat as global, available to be sent out to other companies.  */  
   GlobalStockProvisionFormat:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates whether Type field should be enabled in the UI.  */  
   EnableType:boolean,
      /**  Type description  */  
   TypeDesc:string,
      /**  ComparedTo description  */  
   ComparedToDesc:string,
      /**  TimeModifier description  */  
   TimeModifierDesc:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_StockProvisionFormatTableset{
   StockProvisionFormat:Erp_Tablesets_StockProvisionFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_TranTypeRow{
      /**  Transaction Type ID  */  
   TranID:string,
      /**  Description of the Transaction Type  */  
   Description:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TranTypeTableset{
   TranType:Erp_Tablesets_TranTypeRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtStockProvisionFormatTableset{
   StockProvisionFormat:Erp_Tablesets_StockProvisionFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param stockProvFmtCode
   */  
export interface GetByID_input{
   stockProvFmtCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_StockProvisionFormatTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_StockProvisionFormatTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_StockProvisionFormatTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
   tableName:string,
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
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
   returnObj:Erp_Tablesets_StockProvisionFormatListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewStockProvisionFormat_input{
   ds:Erp_Tablesets_StockProvisionFormatTableset[],
}

export interface GetNewStockProvisionFormat_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_StockProvisionFormatTableset,
}
}

   /** Required : 
      @param whereClauseStockProvisionFormat
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseStockProvisionFormat:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_StockProvisionFormatTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param typeValue
   */  
export interface GetTimeModifierCodeDescList_input{
   typeValue:string,
}

export interface GetTimeModifierCodeDescList_output{
      /**  List of Time Modifier codes/descriptions  */  
   returnObj:string,
}

export interface GetTranTypeList_output{
parameters : {
      /**  output parameters  */  
   TranTypeAndDesc:string,
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
      @param TranTypes
   */  
export interface LoadTranTypeDS_input{
      /**  Dataset of TranTypes Temp Table  */  
   TranTypes:string,
}

export interface LoadTranTypeDS_output{
   returnObj:Erp_Tablesets_TranTypeTableset[],
}

   /** Required : 
      @param ds
   */  
export interface OnChangeActive_input{
   ds:Erp_Tablesets_StockProvisionFormatTableset[],
}

export interface OnChangeActive_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_StockProvisionFormatTableset,
}
}

   /** Required : 
      @param ipType
      @param ds
   */  
export interface OnChangeType_input{
      /**  Proposed Type value  */  
   ipType:string,
   ds:Erp_Tablesets_StockProvisionFormatTableset[],
}

export interface OnChangeType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_StockProvisionFormatTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtStockProvisionFormatTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtStockProvisionFormatTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_StockProvisionFormatTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_StockProvisionFormatTableset,
}
}

