import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.GLPeriodBalSearchSvc
// Description: Add your summary for this object here
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLPeriodBalSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLPeriodBalSearchSvc/$metadata", {
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
   Description: Get GLPeriodBalSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLPeriodBalSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLPeriodBalRow
   */  
export function get_GLPeriodBalSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLPeriodBalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLPeriodBalSearchSvc/GLPeriodBalSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLPeriodBalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLPeriodBalSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLPeriodBalRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GLPeriodBalRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLPeriodBalSearches(requestBody:Erp_Tablesets_GLPeriodBalRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLPeriodBalSearchSvc/GLPeriodBalSearches", {
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
   Summary: Calls GetByID to retrieve the GLPeriodBalSearch item
   Description: Calls GetByID to retrieve the GLPeriodBalSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLPeriodBalSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param BalanceAcct Desc: BalanceAcct   Required: True   Allow empty value : True
      @param BalanceType Desc: BalanceType   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLPeriodBalRow
   */  
export function get_GLPeriodBalSearches_Company_BookID_BalanceAcct_BalanceType_FiscalYear_FiscalYearSuffix_FiscalPeriod_FiscalCalendarID(Company:string, BookID:string, BalanceAcct:string, BalanceType:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, FiscalCalendarID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLPeriodBalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLPeriodBalSearchSvc/GLPeriodBalSearches(" + Company + "," + BookID + "," + BalanceAcct + "," + BalanceType + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + FiscalCalendarID + ")", {
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
         resolve(data as Erp_Tablesets_GLPeriodBalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLPeriodBalSearch for the service
   Description: Calls UpdateExt to update GLPeriodBalSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLPeriodBalSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param BalanceAcct Desc: BalanceAcct   Required: True   Allow empty value : True
      @param BalanceType Desc: BalanceType   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLPeriodBalRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLPeriodBalSearches_Company_BookID_BalanceAcct_BalanceType_FiscalYear_FiscalYearSuffix_FiscalPeriod_FiscalCalendarID(Company:string, BookID:string, BalanceAcct:string, BalanceType:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, FiscalCalendarID:string, requestBody:Erp_Tablesets_GLPeriodBalRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLPeriodBalSearchSvc/GLPeriodBalSearches(" + Company + "," + BookID + "," + BalanceAcct + "," + BalanceType + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + FiscalCalendarID + ")", {
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
   Summary: Call UpdateExt to delete GLPeriodBalSearch item
   Description: Call UpdateExt to delete GLPeriodBalSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLPeriodBalSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param BalanceAcct Desc: BalanceAcct   Required: True   Allow empty value : True
      @param BalanceType Desc: BalanceType   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLPeriodBalSearches_Company_BookID_BalanceAcct_BalanceType_FiscalYear_FiscalYearSuffix_FiscalPeriod_FiscalCalendarID(Company:string, BookID:string, BalanceAcct:string, BalanceType:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, FiscalCalendarID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLPeriodBalSearchSvc/GLPeriodBalSearches(" + Company + "," + BookID + "," + BalanceAcct + "," + BalanceType + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + FiscalCalendarID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLPeriodBalListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLPeriodBalListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLPeriodBalSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLPeriodBalListRow)
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
export function get_GetRows(whereClauseGLPeriodBal:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseGLPeriodBal!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLPeriodBal=" + whereClauseGLPeriodBal
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLPeriodBalSearchSvc/GetRows" + params, {
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
   Required: True
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(bookID:string, balanceAcct:string, balanceType:string, fiscalYear:string, fiscalYearSuffix:string, fiscalPeriod:string, fiscalCalendarID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof bookID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "bookID=" + bookID
   }
   if(typeof balanceAcct!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "balanceAcct=" + balanceAcct
   }
   if(typeof balanceType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "balanceType=" + balanceType
   }
   if(typeof fiscalYear!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "fiscalYear=" + fiscalYear
   }
   if(typeof fiscalYearSuffix!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "fiscalYearSuffix=" + fiscalYearSuffix
   }
   if(typeof fiscalPeriod!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "fiscalPeriod=" + fiscalPeriod
   }
   if(typeof fiscalCalendarID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "fiscalCalendarID=" + fiscalCalendarID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLPeriodBalSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLPeriodBalSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewGLPeriodBal
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLPeriodBal
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGLPeriodBal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLPeriodBal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLPeriodBal(requestBody:GetNewGLPeriodBal_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGLPeriodBal_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLPeriodBalSearchSvc/GetNewGLPeriodBal", {
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
         resolve(data as GetNewGLPeriodBal_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLPeriodBalSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLPeriodBalSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLPeriodBalSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLPeriodBalSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLPeriodBalSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLPeriodBalListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLPeriodBalListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLPeriodBalRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLPeriodBalRow,
}

export interface Erp_Tablesets_GLPeriodBalListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  GLBook ID  */  
   "BookID":string,
      /**  The GL Account used to record balances.  */  
   "BalanceAcct":string,
      /**  Identifies the type of balance stored on this record.  S = Summary Balance.  D = Detail Balance.  B = Both a Summary and Detail Balance.  */  
   "BalanceType":string,
      /**  The fiscal year of this period balance record  */  
   "FiscalYear":number,
      /**  Fiscal period of the balance record.  Period 0 (zero) is reserved to record the opening and/or carry forward balance.  */  
   "FiscalPeriod":number,
      /**  Provides the ability to analyze revenue and cost independent of fiscal year and are used only with accounts that include a segment defined to keep an opening balance on an income statement account.  This is updated by the fiscal period close process.  */  
   "CarryForwardBalance":number,
      /**  The account's opening balance for the fiscal year.  This is only populated for period 0.  Updated by the fiscal period close process.  */  
   "OpenBalance":number,
      /**  The balance amount for this fiscal period.  The type of balance stored in this field is determined by the value of the BalanceType field.  */  
   "BalanceAmt":number,
      /**  Total debit amount that has been posted to the account for a specific fisccal year/period.  */  
   "DebitAmt":number,
      /**  Total Credit amount that has been posted to the account for a specific fiscal year/period.  */  
   "CreditAmt":number,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   "SegValue1":string,
      /**  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   "SegValue2":string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   "SegValue3":string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   "SegValue4":string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   "SegValue5":string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   "SegValue6":string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   "SegValue7":string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   "SegValue8":string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   "SegValue9":string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   "SegValue10":string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   "SegValue11":string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   "SegValue12":string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   "SegValue13":string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   "SegValue14":string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   "SegValue15":string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   "SegValue16":string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   "SegValue17":string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   "SegValue18":string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   "SegValue19":string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   "SegValue20":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Balance Account Description  */  
   "BalAcctDesc":string,
      /**  Balance Account in the display format.  */  
   "BalanceAcctDisp":string,
      /**  Category Description  */  
   "CategoryDesc":string,
      /**  COA Code  */  
   "COACode":string,
      /**  Normal Balance  */  
   "NormalBal":string,
      /**  Logical that is set to true when the catetory associated with segment 1 is an income type category or any of the segements in the balance account store balances for the P/L defined in COA defintion.  */  
   "CanUseCarryFwdBal":boolean,
      /**  Currency Account  */  
   "CurrAcct":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLPeriodBalRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  GLBook ID  */  
   "BookID":string,
      /**  The GL Account used to record balances.  */  
   "BalanceAcct":string,
      /**  Identifies the type of balance stored on this record.  S = Summary Balance.  D = Detail Balance.  B = Both a Summary and Detail Balance.  */  
   "BalanceType":string,
      /**  The fiscal year of this period balance record  */  
   "FiscalYear":number,
      /**  Fiscal period of the balance record.  Period 0 (zero) is reserved to record the opening and/or carry forward balance.  */  
   "FiscalPeriod":number,
      /**  Provides the ability to analyze revenue and cost independent of fiscal year and are used only with accounts that include a segment defined to keep an opening balance on an income statement account.  This is updated by the fiscal period close process.  */  
   "CarryForwardBalance":number,
      /**  The account's opening balance for the fiscal year.  This is only populated for period 0.  Updated by the fiscal period close process.  */  
   "OpenBalance":number,
      /**  The balance amount for this fiscal period.  The type of balance stored in this field is determined by the value of the BalanceType field.  */  
   "BalanceAmt":number,
      /**  Total debit amount that has been posted to the account for a specific fisccal year/period.  */  
   "DebitAmt":number,
      /**  Total Credit amount that has been posted to the account for a specific fiscal year/period.  */  
   "CreditAmt":number,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   "SegValue1":string,
      /**  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   "SegValue2":string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   "SegValue3":string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   "SegValue4":string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   "SegValue5":string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   "SegValue6":string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   "SegValue7":string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   "SegValue8":string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   "SegValue9":string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   "SegValue10":string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   "SegValue11":string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   "SegValue12":string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   "SegValue13":string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   "SegValue14":string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   "SegValue15":string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   "SegValue16":string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   "SegValue17":string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   "SegValue18":string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   "SegValue19":string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   "SegValue20":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  BalanceStatAmt  */  
   "BalanceStatAmt":number,
      /**  DebitStatAmt  */  
   "DebitStatAmt":number,
      /**  CreditStatAmt  */  
   "CreditStatAmt":number,
      /**  OpenBalanceStatAmt  */  
   "OpenBalanceStatAmt":number,
      /**  CarryForwardBalanceStatAmt  */  
   "CarryForwardBalanceStatAmt":number,
      /**  Category Description  */  
   "CategoryDesc":string,
      /**  COA Code  */  
   "COACode":string,
      /**  Currency Account  */  
   "CurrAcct":boolean,
      /**  Normal Balance  */  
   "NormalBal":string,
      /**  Balance Account Description  */  
   "BalAcctDesc":string,
      /**  Balance Account in the display format.  */  
   "BalanceAcctDisp":string,
   "BookCurrencyCode":string,
      /**  Logical that is set to true when the catetory associated with segment 1 is an income type category or any of the segements in the balance account store balances for the P/L defined in COA defintion.  */  
   "CanUseCarryFwdBal":boolean,
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
      @param bookID
      @param balanceAcct
      @param balanceType
      @param fiscalYear
      @param fiscalYearSuffix
      @param fiscalPeriod
      @param fiscalCalendarID
   */  
export interface DeleteByID_input{
   bookID:string,
   balanceAcct:string,
   balanceType:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   fiscalPeriod:number,
   fiscalCalendarID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_GLPeriodBalListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  GLBook ID  */  
   BookID:string,
      /**  The GL Account used to record balances.  */  
   BalanceAcct:string,
      /**  Identifies the type of balance stored on this record.  S = Summary Balance.  D = Detail Balance.  B = Both a Summary and Detail Balance.  */  
   BalanceType:string,
      /**  The fiscal year of this period balance record  */  
   FiscalYear:number,
      /**  Fiscal period of the balance record.  Period 0 (zero) is reserved to record the opening and/or carry forward balance.  */  
   FiscalPeriod:number,
      /**  Provides the ability to analyze revenue and cost independent of fiscal year and are used only with accounts that include a segment defined to keep an opening balance on an income statement account.  This is updated by the fiscal period close process.  */  
   CarryForwardBalance:number,
      /**  The account's opening balance for the fiscal year.  This is only populated for period 0.  Updated by the fiscal period close process.  */  
   OpenBalance:number,
      /**  The balance amount for this fiscal period.  The type of balance stored in this field is determined by the value of the BalanceType field.  */  
   BalanceAmt:number,
      /**  Total debit amount that has been posted to the account for a specific fisccal year/period.  */  
   DebitAmt:number,
      /**  Total Credit amount that has been posted to the account for a specific fiscal year/period.  */  
   CreditAmt:number,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   SegValue1:string,
      /**  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   SegValue2:string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   SegValue3:string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   SegValue4:string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   SegValue5:string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   SegValue6:string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   SegValue7:string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   SegValue8:string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   SegValue9:string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   SegValue10:string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   SegValue11:string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   SegValue12:string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   SegValue13:string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   SegValue14:string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   SegValue15:string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   SegValue16:string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   SegValue17:string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   SegValue18:string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   SegValue19:string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   SegValue20:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Balance Account Description  */  
   BalAcctDesc:string,
      /**  Balance Account in the display format.  */  
   BalanceAcctDisp:string,
      /**  Category Description  */  
   CategoryDesc:string,
      /**  COA Code  */  
   COACode:string,
      /**  Normal Balance  */  
   NormalBal:string,
      /**  Logical that is set to true when the catetory associated with segment 1 is an income type category or any of the segements in the balance account store balances for the P/L defined in COA defintion.  */  
   CanUseCarryFwdBal:boolean,
      /**  Currency Account  */  
   CurrAcct:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLPeriodBalListTableset{
   GLPeriodBalList:Erp_Tablesets_GLPeriodBalListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GLPeriodBalRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  GLBook ID  */  
   BookID:string,
      /**  The GL Account used to record balances.  */  
   BalanceAcct:string,
      /**  Identifies the type of balance stored on this record.  S = Summary Balance.  D = Detail Balance.  B = Both a Summary and Detail Balance.  */  
   BalanceType:string,
      /**  The fiscal year of this period balance record  */  
   FiscalYear:number,
      /**  Fiscal period of the balance record.  Period 0 (zero) is reserved to record the opening and/or carry forward balance.  */  
   FiscalPeriod:number,
      /**  Provides the ability to analyze revenue and cost independent of fiscal year and are used only with accounts that include a segment defined to keep an opening balance on an income statement account.  This is updated by the fiscal period close process.  */  
   CarryForwardBalance:number,
      /**  The account's opening balance for the fiscal year.  This is only populated for period 0.  Updated by the fiscal period close process.  */  
   OpenBalance:number,
      /**  The balance amount for this fiscal period.  The type of balance stored in this field is determined by the value of the BalanceType field.  */  
   BalanceAmt:number,
      /**  Total debit amount that has been posted to the account for a specific fisccal year/period.  */  
   DebitAmt:number,
      /**  Total Credit amount that has been posted to the account for a specific fiscal year/period.  */  
   CreditAmt:number,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   SegValue1:string,
      /**  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   SegValue2:string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   SegValue3:string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   SegValue4:string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   SegValue5:string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   SegValue6:string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   SegValue7:string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   SegValue8:string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   SegValue9:string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   SegValue10:string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   SegValue11:string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   SegValue12:string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   SegValue13:string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   SegValue14:string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   SegValue15:string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   SegValue16:string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   SegValue17:string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   SegValue18:string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   SegValue19:string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   SegValue20:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  BalanceStatAmt  */  
   BalanceStatAmt:number,
      /**  DebitStatAmt  */  
   DebitStatAmt:number,
      /**  CreditStatAmt  */  
   CreditStatAmt:number,
      /**  OpenBalanceStatAmt  */  
   OpenBalanceStatAmt:number,
      /**  CarryForwardBalanceStatAmt  */  
   CarryForwardBalanceStatAmt:number,
      /**  Category Description  */  
   CategoryDesc:string,
      /**  COA Code  */  
   COACode:string,
      /**  Currency Account  */  
   CurrAcct:boolean,
      /**  Normal Balance  */  
   NormalBal:string,
      /**  Balance Account Description  */  
   BalAcctDesc:string,
      /**  Balance Account in the display format.  */  
   BalanceAcctDisp:string,
   BookCurrencyCode:string,
      /**  Logical that is set to true when the catetory associated with segment 1 is an income type category or any of the segements in the balance account store balances for the P/L defined in COA defintion.  */  
   CanUseCarryFwdBal:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLPeriodBalSearchTableset{
   GLPeriodBal:Erp_Tablesets_GLPeriodBalRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtGLPeriodBalSearchTableset{
   GLPeriodBal:Erp_Tablesets_GLPeriodBalRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param bookID
      @param balanceAcct
      @param balanceType
      @param fiscalYear
      @param fiscalYearSuffix
      @param fiscalPeriod
      @param fiscalCalendarID
   */  
export interface GetByID_input{
   bookID:string,
   balanceAcct:string,
   balanceType:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   fiscalPeriod:number,
   fiscalCalendarID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_GLPeriodBalSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_GLPeriodBalSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_GLPeriodBalSearchTableset[],
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
   returnObj:Erp_Tablesets_GLPeriodBalListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param bookID
      @param balanceAcct
      @param balanceType
      @param fiscalYear
      @param fiscalYearSuffix
      @param fiscalPeriod
   */  
export interface GetNewGLPeriodBal_input{
   ds:Erp_Tablesets_GLPeriodBalSearchTableset[],
   bookID:string,
   balanceAcct:string,
   balanceType:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   fiscalPeriod:number,
}

export interface GetNewGLPeriodBal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLPeriodBalSearchTableset,
}
}

   /** Required : 
      @param whereClauseGLPeriodBal
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseGLPeriodBal:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_GLPeriodBalSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtGLPeriodBalSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtGLPeriodBalSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_GLPeriodBalSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLPeriodBalSearchTableset,
}
}

