import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.AssetClosePeriodSvc
// Description: This updates the FiscalPer table if used in Asset Register to close
fiscal periods used in asset activities.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/$metadata", {
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
   Description: Get AssetClosePeriods items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AssetClosePeriods
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FiscalPerRow
   */  
export function get_AssetClosePeriods(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalPerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/AssetClosePeriods", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalPerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AssetClosePeriods
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FiscalPerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.FiscalPerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssetClosePeriods(requestBody:Erp_Tablesets_FiscalPerRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/AssetClosePeriods", {
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
   Summary: Calls GetByID to retrieve the AssetClosePeriod item
   Description: Calls GetByID to retrieve the AssetClosePeriod item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AssetClosePeriod
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.FiscalPerRow
   */  
export function get_AssetClosePeriods_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company:string, FiscalCalendarID:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FiscalPerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/AssetClosePeriods(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")", {
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
         resolve(data as Erp_Tablesets_FiscalPerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AssetClosePeriod for the service
   Description: Calls UpdateExt to update AssetClosePeriod. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AssetClosePeriod
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.FiscalPerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AssetClosePeriods_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company:string, FiscalCalendarID:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, requestBody:Erp_Tablesets_FiscalPerRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/AssetClosePeriods(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")", {
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
   Summary: Call UpdateExt to delete AssetClosePeriod item
   Description: Call UpdateExt to delete AssetClosePeriod item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AssetClosePeriod
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AssetClosePeriods_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company:string, FiscalCalendarID:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/AssetClosePeriods(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FiscalPerListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalPerListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalPerListRow)
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
export function get_GetRows(whereClauseFiscalPer:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseFiscalPer!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFiscalPer=" + whereClauseFiscalPer
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(fiscalCalendarID:string, fiscalYear:string, fiscalYearSuffix:string, fiscalPeriod:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof fiscalCalendarID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "fiscalCalendarID=" + fiscalCalendarID
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

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/GetList" + params, {
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
   Summary: Invoke method CheckYearEndStatus
   Description: Returns a logical value to indicate if the Year End Process should be enabled.
   OperationID: CheckYearEndStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckYearEndStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckYearEndStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckYearEndStatus(requestBody:CheckYearEndStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckYearEndStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/CheckYearEndStatus", {
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
         resolve(data as CheckYearEndStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeFAClosedPeriod
   Description: Run when the FiscalPer.FAClosedPeriod field changes.
   OperationID: OnChangeFAClosedPeriod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeFAClosedPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFAClosedPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFAClosedPeriod(requestBody:OnChangeFAClosedPeriod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeFAClosedPeriod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/OnChangeFAClosedPeriod", {
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
         resolve(data as OnChangeFAClosedPeriod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeFiscalYear
   Description: Verifies if given Fiscal Year exists
   OperationID: OnChangeFiscalYear
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeFiscalYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFiscalYear(requestBody:OnChangeFiscalYear_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeFiscalYear_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/OnChangeFiscalYear", {
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
         resolve(data as OnChangeFiscalYear_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeFiscalYearSuffix
   Description: Verifies if given Fiscal Year Suffix exists
   OperationID: OnChangeFiscalYearSuffix
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeFiscalYearSuffix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFiscalYearSuffix_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFiscalYearSuffix(requestBody:OnChangeFiscalYearSuffix_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeFiscalYearSuffix_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/OnChangeFiscalYearSuffix", {
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
         resolve(data as OnChangeFiscalYearSuffix_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewFiscalPer
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFiscalPer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewFiscalPer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFiscalPer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFiscalPer(requestBody:GetNewFiscalPer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewFiscalPer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/GetNewFiscalPer", {
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
         resolve(data as GetNewFiscalPer_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalPerListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FiscalPerListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalPerRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FiscalPerRow,
}

export interface Erp_Tablesets_FiscalPerListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The id of the fiscal calendar this record is related to.  */  
   "FiscalCalendarID":string,
      /**  The fiscal year.  */  
   "FiscalYear":number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal period number in the fiscal year.  */  
   "FiscalPeriod":number,
      /**  The start date of the fiscal period.  */  
   "StartDate":string,
      /**  End date of the fiscal period  */  
   "EndDate":string,
      /**  Indicates if the Fixed Asset period is open or closed.  */  
   "FAClosedPeriod":boolean,
      /**  Additional Deductions to be claimed. User should calculate this value manually  */  
   "AdditionalDeductions":number,
      /**  Income Tax losses to be claimed. User should calculate this value manually  */  
   "LossesCredit":number,
      /**  Investments Credit to be claimed. User should calculate this value manually  */  
   "InvestmentCredit":number,
      /**  Inventories Credit to be claimed. User should calculate this value manually.  */  
   "InventoriesCredit":number,
      /**  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  */  
   "UpdateRate":number,
      /**  Flag to indicate if the fiscal period is a holiday period.  This flag will be used in the asset depreciation calculation process to skip calculation of preiod depreciation charge if it's a holiday.  */  
   "DepHoliday":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  JPYear  */  
   "JPYear":number,
      /**  Indicates if EndDate can be modified by the user.  */  
   "EnableEndDate":boolean,
      /**  Indicates if StartDate can be changed by the user.  */  
   "EnableStartDate":boolean,
      /**  Calendar description.  */  
   "FiscalCalDescription":string,
      /**  Fiscal year description.  */  
   "FiscalYrDescription":string,
      /**  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  */  
   "ITUpdateRate":number,
      /**  Number of days (EndDate - StartDate)  */  
   "NoOfDays":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FiscalPerRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The id of the fiscal calendar this record is related to.  */  
   "FiscalCalendarID":string,
      /**  The fiscal year.  */  
   "FiscalYear":number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal period number in the fiscal year.  */  
   "FiscalPeriod":number,
      /**  The start date of the fiscal period.  */  
   "StartDate":string,
      /**  End date of the fiscal period  */  
   "EndDate":string,
      /**  Indicates if the Fixed Asset period is open or closed.  */  
   "FAClosedPeriod":boolean,
      /**  Additional Deductions to be claimed. User should calculate this value manually  */  
   "AdditionalDeductions":number,
      /**  Income Tax losses to be claimed. User should calculate this value manually  */  
   "LossesCredit":number,
      /**  Investments Credit to be claimed. User should calculate this value manually  */  
   "InvestmentCredit":number,
      /**  Inventories Credit to be claimed. User should calculate this value manually.  */  
   "InventoriesCredit":number,
      /**  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  */  
   "UpdateRate":number,
      /**  Flag to indicate if the fiscal period is a holiday period.  This flag will be used in the asset depreciation calculation process to skip calculation of preiod depreciation charge if it's a holiday.  */  
   "DepHoliday":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  JPYear  */  
   "JPYear":number,
      /**  Indicates if StartDate can be changed by the user.  */  
   "EnableStartDate":boolean,
      /**  Indicates if EndDate can be modified by the user.  */  
   "EnableEndDate":boolean,
      /**  Number of days (EndDate - StartDate)  */  
   "NoOfDays":string,
      /**  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  */  
   "ITUpdateRate":number,
      /**  Used in Close Asset Period / Year process  */  
   "AssetRegCurrYear":number,
      /**  Used in Close Asset Period / Year process  */  
   "AssetRegCurrYearSuffix":string,
      /**  Used in Close Asset Period / Year process  */  
   "AssetRegCurrPeriod":number,
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
      @param ipCalendarID
      @param ipYear
      @param ipYearSuffix
   */  
export interface CheckYearEndStatus_input{
      /**  The input fiscal calendar ID  */  
   ipCalendarID:string,
      /**  The input fiscal year  */  
   ipYear:number,
      /**  The input fiscal year suffix  */  
   ipYearSuffix:string,
}

export interface CheckYearEndStatus_output{
parameters : {
      /**  output parameters  */  
   opAllowed:boolean,
}
}

   /** Required : 
      @param fiscalCalendarID
      @param fiscalYear
      @param fiscalYearSuffix
      @param fiscalPeriod
   */  
export interface DeleteByID_input{
   fiscalCalendarID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   fiscalPeriod:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_AssetClosePeriodTableset{
   FiscalPer:Erp_Tablesets_FiscalPerRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FiscalPerListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The id of the fiscal calendar this record is related to.  */  
   FiscalCalendarID:string,
      /**  The fiscal year.  */  
   FiscalYear:number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   FiscalYearSuffix:string,
      /**  The fiscal period number in the fiscal year.  */  
   FiscalPeriod:number,
      /**  The start date of the fiscal period.  */  
   StartDate:string,
      /**  End date of the fiscal period  */  
   EndDate:string,
      /**  Indicates if the Fixed Asset period is open or closed.  */  
   FAClosedPeriod:boolean,
      /**  Additional Deductions to be claimed. User should calculate this value manually  */  
   AdditionalDeductions:number,
      /**  Income Tax losses to be claimed. User should calculate this value manually  */  
   LossesCredit:number,
      /**  Investments Credit to be claimed. User should calculate this value manually  */  
   InvestmentCredit:number,
      /**  Inventories Credit to be claimed. User should calculate this value manually.  */  
   InventoriesCredit:number,
      /**  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  */  
   UpdateRate:number,
      /**  Flag to indicate if the fiscal period is a holiday period.  This flag will be used in the asset depreciation calculation process to skip calculation of preiod depreciation charge if it's a holiday.  */  
   DepHoliday:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  JPYear  */  
   JPYear:number,
      /**  Indicates if EndDate can be modified by the user.  */  
   EnableEndDate:boolean,
      /**  Indicates if StartDate can be changed by the user.  */  
   EnableStartDate:boolean,
      /**  Calendar description.  */  
   FiscalCalDescription:string,
      /**  Fiscal year description.  */  
   FiscalYrDescription:string,
      /**  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  */  
   ITUpdateRate:number,
      /**  Number of days (EndDate - StartDate)  */  
   NoOfDays:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FiscalPerListTableset{
   FiscalPerList:Erp_Tablesets_FiscalPerListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FiscalPerRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The id of the fiscal calendar this record is related to.  */  
   FiscalCalendarID:string,
      /**  The fiscal year.  */  
   FiscalYear:number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   FiscalYearSuffix:string,
      /**  The fiscal period number in the fiscal year.  */  
   FiscalPeriod:number,
      /**  The start date of the fiscal period.  */  
   StartDate:string,
      /**  End date of the fiscal period  */  
   EndDate:string,
      /**  Indicates if the Fixed Asset period is open or closed.  */  
   FAClosedPeriod:boolean,
      /**  Additional Deductions to be claimed. User should calculate this value manually  */  
   AdditionalDeductions:number,
      /**  Income Tax losses to be claimed. User should calculate this value manually  */  
   LossesCredit:number,
      /**  Investments Credit to be claimed. User should calculate this value manually  */  
   InvestmentCredit:number,
      /**  Inventories Credit to be claimed. User should calculate this value manually.  */  
   InventoriesCredit:number,
      /**  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  */  
   UpdateRate:number,
      /**  Flag to indicate if the fiscal period is a holiday period.  This flag will be used in the asset depreciation calculation process to skip calculation of preiod depreciation charge if it's a holiday.  */  
   DepHoliday:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  JPYear  */  
   JPYear:number,
      /**  Indicates if StartDate can be changed by the user.  */  
   EnableStartDate:boolean,
      /**  Indicates if EndDate can be modified by the user.  */  
   EnableEndDate:boolean,
      /**  Number of days (EndDate - StartDate)  */  
   NoOfDays:string,
      /**  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  */  
   ITUpdateRate:number,
      /**  Used in Close Asset Period / Year process  */  
   AssetRegCurrYear:number,
      /**  Used in Close Asset Period / Year process  */  
   AssetRegCurrYearSuffix:string,
      /**  Used in Close Asset Period / Year process  */  
   AssetRegCurrPeriod:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtAssetClosePeriodTableset{
   FiscalPer:Erp_Tablesets_FiscalPerRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param fiscalCalendarID
      @param fiscalYear
      @param fiscalYearSuffix
      @param fiscalPeriod
   */  
export interface GetByID_input{
   fiscalCalendarID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   fiscalPeriod:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_AssetClosePeriodTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_AssetClosePeriodTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_AssetClosePeriodTableset[],
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
   returnObj:Erp_Tablesets_FiscalPerListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param fiscalCalendarID
      @param fiscalYear
      @param fiscalYearSuffix
   */  
export interface GetNewFiscalPer_input{
   ds:Erp_Tablesets_AssetClosePeriodTableset[],
   fiscalCalendarID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
}

export interface GetNewFiscalPer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetClosePeriodTableset,
}
}

   /** Required : 
      @param whereClauseFiscalPer
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseFiscalPer:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_AssetClosePeriodTableset[],
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
      @param ipProposedValue
      @param ds
   */  
export interface OnChangeFAClosedPeriod_input{
      /**  Value that the user has entered  */  
   ipProposedValue:boolean,
   ds:Erp_Tablesets_AssetClosePeriodTableset[],
}

export interface OnChangeFAClosedPeriod_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   ds:Erp_Tablesets_AssetClosePeriodTableset,
}
}

   /** Required : 
      @param fiscalCalendarID
      @param fiscalYear
      @param fiscalYearSuffix
   */  
export interface OnChangeFiscalYearSuffix_input{
   fiscalCalendarID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
}

export interface OnChangeFiscalYearSuffix_output{
   returnObj:boolean,
}

   /** Required : 
      @param fiscalCalendarID
      @param fiscalYear
   */  
export interface OnChangeFiscalYear_input{
   fiscalCalendarID:string,
   fiscalYear:number,
}

export interface OnChangeFiscalYear_output{
   returnObj:boolean,
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtAssetClosePeriodTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtAssetClosePeriodTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_AssetClosePeriodTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetClosePeriodTableset,
}
}

