import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.VATTaxSvc
// Description: Vat Tax front end
           Notes: if tttaxreport.posted = yes, then user should not be able to update
           any fields. Only allow 'post' menu option to be run for  tttaxreport.posted = no taxreport records.
           user should not be able to update posted, postedby, postdate fields.
           on post vat tax report screen, fill in with default report date from tttaxreport.reportdate, allow user override.
// Version: v1



//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Get VATTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VATTaxes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxReportRow
   */  
export function get_VATTaxes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxReportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/VATTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxReportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VATTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxReportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxReportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VATTaxes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/VATTaxes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the VATTax item
   Description: Calls GetByID to retrieve the VATTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VATTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxReportRow
   */  
export function get_VATTaxes_Company_ReportID(Company:string, ReportID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxReportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/VATTaxes(" + Company + "," + ReportID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TaxReportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VATTax for the service
   Description: Calls UpdateExt to update VATTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VATTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxReportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VATTaxes_Company_ReportID(Company:string, ReportID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/VATTaxes(" + Company + "," + ReportID + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete VATTax item
   Description: Call UpdateExt to delete VATTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VATTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VATTaxes_Company_ReportID(Company:string, ReportID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/VATTaxes(" + Company + "," + ReportID + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxReportListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxReportListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxReportListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseTaxReport:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseTaxReport!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTaxReport=" + whereClauseTaxReport
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(reportID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof reportID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "reportID=" + reportID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckDates
   Description: Check Dates, return any warnings
   OperationID: CheckDates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDates_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDates(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/CheckDates", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreInitTaxRptDtl
   Description: Call this method to check if there are TaxRptDtl records that have been manually
updated or voided by the user.  This is to warn them that these records will not
be refreshed if they choose to continue with the InitializeTaxRptDtl method.
If the opMessage is not blank then show this to the user and let the user decide
whether to continue or not.  If the user answers yes then call InitializeTaxRptDtl.
   OperationID: PreInitTaxRptDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreInitTaxRptDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreInitTaxRptDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreInitTaxRptDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/PreInitTaxRptDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PrePostReport
   Description: Call this method to check if there are TaxRptDtl records that have been manually
updated or voided by the user.  This is to warn them that these records will not
be refreshed if they choose to continue with the InitializeTaxRptDtl method.
If the opMessage is not blank then show this to the user and let the user decide
whether to continue or not.  If the user answers yes then call InitializeTaxRptDtl.
   OperationID: PrePostReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePostReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePostReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrePostReport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/PrePostReport", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetFiscalDates
   Description: Fills From/To dates according selected calendar, year and period if that is possible.
   OperationID: SetFiscalDates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetFiscalDates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetFiscalDates_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetFiscalDates(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/SetFiscalDates", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateFiscalCal
   Description: Validates Fiscal Calendar ID.
   OperationID: ValidateFiscalCal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateFiscalCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFiscalCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateFiscalCal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/ValidateFiscalCal", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTaxReport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTaxReport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/GetNewTaxReport", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VATTaxSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxReportListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaxReportListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxReportRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaxReportRow[],
}

export interface Erp_Tablesets_TaxReportListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Sales tax report ID  */  
   "ReportID":string,
      /**  Description  */  
   "Description":string,
      /**  From Transaction Date Parameter  */  
   "FromTranDate":string,
      /**  To Transaction Date Parameter  */  
   "ToTranDate":string,
      /**  Sales tax report title  */  
   "ReportTitle":string,
      /**  Indicates if this report closed.  */  
   "Posted":boolean,
      /**  The user ID that Posted this report.  */  
   "PostedBy":string,
      /**  Posting Date Parameter  */  
   "PostDate":string,
      /**  Tax Report Date Parameter  */  
   "ReportDate":string,
      /**  Report Checksum.  */  
   "RptChecksum":string,
      /**  Indicates Reporting to AP  */  
   "IncludeAP":boolean,
      /**  Indicates reporting to AR  */  
   "IncludeAR":boolean,
      /**   0 = Domestic/Export
1 = Customer/Supplier
2 = Tax Type/ Rate Code
3 = Tax Liability
4 = Tax Jurisdiction
5 = Report Category  */  
   "SortBy":number,
      /**  Tax Type Filter  */  
   "TaxTypeList":string,
      /**  Tax Liability Filter  */  
   "TaxLiabilityList":string,
      /**  Tax Juridiction Filter  */  
   "TaxJurisList":string,
      /**  Report Category Filter  */  
   "ReportCategoryList":string,
      /**  Customer Filter  */  
   "CustomerList":string,
      /**  Supplier Filter  */  
   "SupplierList":string,
      /**  Balance To Credit (Mexico Localization field)  */  
   "MXBalanceToCredit":number,
      /**  Charge To Credit (Mexico Localization field)  */  
   "MXOnChargeToCredit":number,
      /**  Count To Credit (Mexico Localization field)  */  
   "MXOnCountToCredit":number,
      /**  Compensation (Mexico Localization field)  */  
   "MXCompesation":number,
      /**  Reimbursement (Mexico Localization field)  */  
   "MXReimbursement":number,
      /**  WHSelected (Mexico Localization field)  */  
   "MXWHSelected":number,
      /**  Total On Charge (Mexico Localization field)  */  
   "MXTotalOnCharge":number,
      /**  Total On Count (Mexico Localization field)  */  
   "MXTotalOnCount":number,
      /**  Withholding VAT (Mexico Localization field)  */  
   "MXWithholdingVAT":number,
      /**  Surplus Amount (Mexico Localization field)  */  
   "MXSurplusAmount":number,
      /**  Filters Ready (Mexico Localization field)  */  
   "MXFiltersReady":boolean,
      /**  All Proportion (Mexico Localization field)  */  
   "MXAllProportion":boolean,
      /**  Received Method (Mexico Localization field)  */  
   "MXReceiveMethod":string,
      /**  Proportion Type (Mexico Localization field)  */  
   "MXPropType":string,
      /**  Charge Amount (Mexico Localization field)  */  
   "MXChargeAmount":number,
      /**  On Count Amount  (Mexico Localization field)  */  
   "MXOnCountAmount":number,
      /**  Fiscal Calendar ID (Taiwan Localization field)  */  
   "FiscalCalendarID":string,
      /**  Fiscal Year Suffix  (Taiwan Localization field)  */  
   "FiscalYearSuffix":string,
      /**  Fiscal Year (Taiwan Localization field)  */  
   "FiscalYear":number,
      /**  Fiscal Period  (Taiwan Localization field)  */  
   "FiscalPeriod":number,
      /**  Proportion (Mexico Localization field)  */  
   "MXProportion":boolean,
      /**  Current Month (Mexico Localization field)  */  
   "MXCurrMonth":number,
      /**  Reverse Report Category Filter  */  
   "RevReportCategoryList":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates if the Tax Box feature should be enabled.  */  
   "EnableTaxBox":boolean,
      /**  Fiscal calendar description  */  
   "FiscalCalDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TaxReportRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Sales tax report ID  */  
   "ReportID":string,
      /**  Description  */  
   "Description":string,
      /**  From Transaction Date Parameter  */  
   "FromTranDate":string,
      /**  To Transaction Date Parameter  */  
   "ToTranDate":string,
      /**  Sales tax report title  */  
   "ReportTitle":string,
      /**  Indicates if this report closed.  */  
   "Posted":boolean,
      /**  The user ID that Posted this report.  */  
   "PostedBy":string,
      /**  Posting Date Parameter  */  
   "PostDate":string,
      /**  Tax Report Date Parameter  */  
   "ReportDate":string,
      /**  Report Checksum.  */  
   "RptChecksum":string,
      /**  Indicates Reporting to AP  */  
   "IncludeAP":boolean,
      /**  Indicates reporting to AR  */  
   "IncludeAR":boolean,
      /**   0 = Domestic/Export
1 = Customer/Supplier
2 = Tax Type/ Rate Code
3 = Tax Liability
4 = Tax Jurisdiction
5 = Report Category  */  
   "SortBy":number,
      /**  Tax Type Filter  */  
   "TaxTypeList":string,
      /**  Tax Liability Filter  */  
   "TaxLiabilityList":string,
      /**  Tax Juridiction Filter  */  
   "TaxJurisList":string,
      /**  Report Category Filter  */  
   "ReportCategoryList":string,
      /**  Customer Filter  */  
   "CustomerList":string,
      /**  Supplier Filter  */  
   "SupplierList":string,
      /**  Balance To Credit (Mexico Localization field)  */  
   "MXBalanceToCredit":number,
      /**  Charge To Credit (Mexico Localization field)  */  
   "MXOnChargeToCredit":number,
      /**  Count To Credit (Mexico Localization field)  */  
   "MXOnCountToCredit":number,
      /**  Compensation (Mexico Localization field)  */  
   "MXCompesation":number,
      /**  Reimbursement (Mexico Localization field)  */  
   "MXReimbursement":number,
      /**  WHSelected (Mexico Localization field)  */  
   "MXWHSelected":number,
      /**  Total On Charge (Mexico Localization field)  */  
   "MXTotalOnCharge":number,
      /**  Total On Count (Mexico Localization field)  */  
   "MXTotalOnCount":number,
      /**  Withholding VAT (Mexico Localization field)  */  
   "MXWithholdingVAT":number,
      /**  Surplus Amount (Mexico Localization field)  */  
   "MXSurplusAmount":number,
      /**  Filters Ready (Mexico Localization field)  */  
   "MXFiltersReady":boolean,
      /**  All Proportion (Mexico Localization field)  */  
   "MXAllProportion":boolean,
      /**  Received Method (Mexico Localization field)  */  
   "MXReceiveMethod":string,
      /**  Proportion Type (Mexico Localization field)  */  
   "MXPropType":string,
      /**  Charge Amount (Mexico Localization field)  */  
   "MXChargeAmount":number,
      /**  On Count Amount  (Mexico Localization field)  */  
   "MXOnCountAmount":number,
      /**  Fiscal Calendar ID (Taiwan Localization field)  */  
   "FiscalCalendarID":string,
      /**  Fiscal Year Suffix  (Taiwan Localization field)  */  
   "FiscalYearSuffix":string,
      /**  Fiscal Year (Taiwan Localization field)  */  
   "FiscalYear":number,
      /**  Fiscal Period  (Taiwan Localization field)  */  
   "FiscalPeriod":number,
      /**  Proportion (Mexico Localization field)  */  
   "MXProportion":boolean,
      /**  Current Month (Mexico Localization field)  */  
   "MXCurrMonth":number,
      /**  Reverse Report Category Filter  */  
   "RevReportCategoryList":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  DateBasis  */  
   "DateBasis":string,
      /**  Demand Payment (CSF Belgium)  */  
   "BEAskPayment":boolean,
      /**  Demand Restitution (CSF Belgium)  */  
   "BERestitution":boolean,
      /**  Add Customer List (CSF Belgium)  */  
   "BEClientListing":boolean,
      /**  Declaration Comment (CSF Belgium)  */  
   "BEDeclComment":string,
      /**  Declaration Language (CSF Belgium)  */  
   "BEDeclLanguage":string,
      /**  Electronic Interface  */  
   "EFTHeadUID":number,
      /**  Output File  */  
   "OutputFile":string,
      /**  BackDatedItems  */  
   "BackDatedItems":number,
      /**  Indicates if the Tax Box feature should be enabled.  */  
   "EnableTaxBox":boolean,
      /**  Fiscal calendar description  */  
   "FiscalCalDescription":string,
   "SupplierIDList":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ds
      @param ipReportID
   */  
export interface CheckDates_input{
   ds:Erp_Tablesets_VATTaxTableset[],
      /**  Report ID  */  
   ipReportID:string,
}

export interface CheckDates_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VATTaxTableset[],
   cMessageText:string,
}
}

   /** Required : 
      @param reportID
   */  
export interface DeleteByID_input{
   reportID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_TaxReportListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Sales tax report ID  */  
   ReportID:string,
      /**  Description  */  
   Description:string,
      /**  From Transaction Date Parameter  */  
   FromTranDate:string,
      /**  To Transaction Date Parameter  */  
   ToTranDate:string,
      /**  Sales tax report title  */  
   ReportTitle:string,
      /**  Indicates if this report closed.  */  
   Posted:boolean,
      /**  The user ID that Posted this report.  */  
   PostedBy:string,
      /**  Posting Date Parameter  */  
   PostDate:string,
      /**  Tax Report Date Parameter  */  
   ReportDate:string,
      /**  Report Checksum.  */  
   RptChecksum:string,
      /**  Indicates Reporting to AP  */  
   IncludeAP:boolean,
      /**  Indicates reporting to AR  */  
   IncludeAR:boolean,
      /**   0 = Domestic/Export
1 = Customer/Supplier
2 = Tax Type/ Rate Code
3 = Tax Liability
4 = Tax Jurisdiction
5 = Report Category  */  
   SortBy:number,
      /**  Tax Type Filter  */  
   TaxTypeList:string,
      /**  Tax Liability Filter  */  
   TaxLiabilityList:string,
      /**  Tax Juridiction Filter  */  
   TaxJurisList:string,
      /**  Report Category Filter  */  
   ReportCategoryList:string,
      /**  Customer Filter  */  
   CustomerList:string,
      /**  Supplier Filter  */  
   SupplierList:string,
      /**  Balance To Credit (Mexico Localization field)  */  
   MXBalanceToCredit:number,
      /**  Charge To Credit (Mexico Localization field)  */  
   MXOnChargeToCredit:number,
      /**  Count To Credit (Mexico Localization field)  */  
   MXOnCountToCredit:number,
      /**  Compensation (Mexico Localization field)  */  
   MXCompesation:number,
      /**  Reimbursement (Mexico Localization field)  */  
   MXReimbursement:number,
      /**  WHSelected (Mexico Localization field)  */  
   MXWHSelected:number,
      /**  Total On Charge (Mexico Localization field)  */  
   MXTotalOnCharge:number,
      /**  Total On Count (Mexico Localization field)  */  
   MXTotalOnCount:number,
      /**  Withholding VAT (Mexico Localization field)  */  
   MXWithholdingVAT:number,
      /**  Surplus Amount (Mexico Localization field)  */  
   MXSurplusAmount:number,
      /**  Filters Ready (Mexico Localization field)  */  
   MXFiltersReady:boolean,
      /**  All Proportion (Mexico Localization field)  */  
   MXAllProportion:boolean,
      /**  Received Method (Mexico Localization field)  */  
   MXReceiveMethod:string,
      /**  Proportion Type (Mexico Localization field)  */  
   MXPropType:string,
      /**  Charge Amount (Mexico Localization field)  */  
   MXChargeAmount:number,
      /**  On Count Amount  (Mexico Localization field)  */  
   MXOnCountAmount:number,
      /**  Fiscal Calendar ID (Taiwan Localization field)  */  
   FiscalCalendarID:string,
      /**  Fiscal Year Suffix  (Taiwan Localization field)  */  
   FiscalYearSuffix:string,
      /**  Fiscal Year (Taiwan Localization field)  */  
   FiscalYear:number,
      /**  Fiscal Period  (Taiwan Localization field)  */  
   FiscalPeriod:number,
      /**  Proportion (Mexico Localization field)  */  
   MXProportion:boolean,
      /**  Current Month (Mexico Localization field)  */  
   MXCurrMonth:number,
      /**  Reverse Report Category Filter  */  
   RevReportCategoryList:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if the Tax Box feature should be enabled.  */  
   EnableTaxBox:boolean,
      /**  Fiscal calendar description  */  
   FiscalCalDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaxReportListTableset{
   TaxReportList:Erp_Tablesets_TaxReportListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_TaxReportRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Sales tax report ID  */  
   ReportID:string,
      /**  Description  */  
   Description:string,
      /**  From Transaction Date Parameter  */  
   FromTranDate:string,
      /**  To Transaction Date Parameter  */  
   ToTranDate:string,
      /**  Sales tax report title  */  
   ReportTitle:string,
      /**  Indicates if this report closed.  */  
   Posted:boolean,
      /**  The user ID that Posted this report.  */  
   PostedBy:string,
      /**  Posting Date Parameter  */  
   PostDate:string,
      /**  Tax Report Date Parameter  */  
   ReportDate:string,
      /**  Report Checksum.  */  
   RptChecksum:string,
      /**  Indicates Reporting to AP  */  
   IncludeAP:boolean,
      /**  Indicates reporting to AR  */  
   IncludeAR:boolean,
      /**   0 = Domestic/Export
1 = Customer/Supplier
2 = Tax Type/ Rate Code
3 = Tax Liability
4 = Tax Jurisdiction
5 = Report Category  */  
   SortBy:number,
      /**  Tax Type Filter  */  
   TaxTypeList:string,
      /**  Tax Liability Filter  */  
   TaxLiabilityList:string,
      /**  Tax Juridiction Filter  */  
   TaxJurisList:string,
      /**  Report Category Filter  */  
   ReportCategoryList:string,
      /**  Customer Filter  */  
   CustomerList:string,
      /**  Supplier Filter  */  
   SupplierList:string,
      /**  Balance To Credit (Mexico Localization field)  */  
   MXBalanceToCredit:number,
      /**  Charge To Credit (Mexico Localization field)  */  
   MXOnChargeToCredit:number,
      /**  Count To Credit (Mexico Localization field)  */  
   MXOnCountToCredit:number,
      /**  Compensation (Mexico Localization field)  */  
   MXCompesation:number,
      /**  Reimbursement (Mexico Localization field)  */  
   MXReimbursement:number,
      /**  WHSelected (Mexico Localization field)  */  
   MXWHSelected:number,
      /**  Total On Charge (Mexico Localization field)  */  
   MXTotalOnCharge:number,
      /**  Total On Count (Mexico Localization field)  */  
   MXTotalOnCount:number,
      /**  Withholding VAT (Mexico Localization field)  */  
   MXWithholdingVAT:number,
      /**  Surplus Amount (Mexico Localization field)  */  
   MXSurplusAmount:number,
      /**  Filters Ready (Mexico Localization field)  */  
   MXFiltersReady:boolean,
      /**  All Proportion (Mexico Localization field)  */  
   MXAllProportion:boolean,
      /**  Received Method (Mexico Localization field)  */  
   MXReceiveMethod:string,
      /**  Proportion Type (Mexico Localization field)  */  
   MXPropType:string,
      /**  Charge Amount (Mexico Localization field)  */  
   MXChargeAmount:number,
      /**  On Count Amount  (Mexico Localization field)  */  
   MXOnCountAmount:number,
      /**  Fiscal Calendar ID (Taiwan Localization field)  */  
   FiscalCalendarID:string,
      /**  Fiscal Year Suffix  (Taiwan Localization field)  */  
   FiscalYearSuffix:string,
      /**  Fiscal Year (Taiwan Localization field)  */  
   FiscalYear:number,
      /**  Fiscal Period  (Taiwan Localization field)  */  
   FiscalPeriod:number,
      /**  Proportion (Mexico Localization field)  */  
   MXProportion:boolean,
      /**  Current Month (Mexico Localization field)  */  
   MXCurrMonth:number,
      /**  Reverse Report Category Filter  */  
   RevReportCategoryList:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  DateBasis  */  
   DateBasis:string,
      /**  Demand Payment (CSF Belgium)  */  
   BEAskPayment:boolean,
      /**  Demand Restitution (CSF Belgium)  */  
   BERestitution:boolean,
      /**  Add Customer List (CSF Belgium)  */  
   BEClientListing:boolean,
      /**  Declaration Comment (CSF Belgium)  */  
   BEDeclComment:string,
      /**  Declaration Language (CSF Belgium)  */  
   BEDeclLanguage:string,
      /**  Electronic Interface  */  
   EFTHeadUID:number,
      /**  Output File  */  
   OutputFile:string,
      /**  BackDatedItems  */  
   BackDatedItems:number,
      /**  Indicates if the Tax Box feature should be enabled.  */  
   EnableTaxBox:boolean,
      /**  Fiscal calendar description  */  
   FiscalCalDescription:string,
   SupplierIDList:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtVATTaxTableset{
   TaxReport:Erp_Tablesets_TaxReportRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_VATTaxTableset{
   TaxReport:Erp_Tablesets_TaxReportRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param reportID
   */  
export interface GetByID_input{
   reportID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_VATTaxTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_VATTaxTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_VATTaxTableset[],
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
   returnObj:Erp_Tablesets_TaxReportListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewTaxReport_input{
   ds:Erp_Tablesets_VATTaxTableset[],
}

export interface GetNewTaxReport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VATTaxTableset[],
}
}

   /** Required : 
      @param whereClauseTaxReport
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseTaxReport:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_VATTaxTableset[],
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
      @param ipReportID
   */  
export interface PreInitTaxRptDtl_input{
      /**  The VAT Tax Report ID.  */  
   ipReportID:string,
}

export interface PreInitTaxRptDtl_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param inputReportID
      @param inputUpdTaxRptDtl
   */  
export interface PrePostReport_input{
      /**  report id of report to be posted.  */  
   inputReportID:string,
      /**  Indicates if the TaxRptDtl will be updated or not.  */  
   inputUpdTaxRptDtl:boolean,
}

export interface PrePostReport_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface SetFiscalDates_input{
   ds:Erp_Tablesets_VATTaxTableset[],
}

export interface SetFiscalDates_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VATTaxTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtVATTaxTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtVATTaxTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_VATTaxTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VATTaxTableset[],
}
}

   /** Required : 
      @param ds
      @param fiscalCalID
   */  
export interface ValidateFiscalCal_input{
   ds:Erp_Tablesets_VATTaxTableset[],
      /**  The fiscal calendar ID  */  
   fiscalCalID:string,
}

export interface ValidateFiscalCal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VATTaxTableset[],
}
}

