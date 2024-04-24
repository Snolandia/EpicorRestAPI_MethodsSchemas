import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.RecurringJournalSvc
// Description: 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/$metadata", {
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
   Description: Get RecurringJournals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RecurringJournals
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRecHedRow
   */  
export function get_RecurringJournals(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRecHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/RecurringJournals", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRecHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RecurringJournals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLRecHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLRecHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RecurringJournals(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/RecurringJournals", {
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
   Summary: Calls GetByID to retrieve the RecurringJournal item
   Description: Calls GetByID to retrieve the RecurringJournal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RecurringJournal
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RecurNum Desc: RecurNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLRecHedRow
   */  
export function get_RecurringJournals_Company_RecurNum(Company:string, RecurNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLRecHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/RecurringJournals(" + Company + "," + RecurNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GLRecHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RecurringJournal for the service
   Description: Calls UpdateExt to update RecurringJournal. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RecurringJournal
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RecurNum Desc: RecurNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLRecHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RecurringJournals_Company_RecurNum(Company:string, RecurNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/RecurringJournals(" + Company + "," + RecurNum + ")", {
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
   Summary: Call UpdateExt to delete RecurringJournal item
   Description: Call UpdateExt to delete RecurringJournal item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RecurringJournal
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RecurNum Desc: RecurNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RecurringJournals_Company_RecurNum(Company:string, RecurNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/RecurringJournals(" + Company + "," + RecurNum + ")", {
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
   Summary: Calls GetByID for the service
   Description: Get GLRecDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLRecDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RecurNum Desc: RecurNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRecDtlRow
   */  
export function get_RecurringJournals_Company_RecurNum_GLRecDtls(Company:string, RecurNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRecDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/RecurringJournals(" + Company + "," + RecurNum + ")/GLRecDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRecDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the GLRecDtl item
   Description: Calls GetByID to retrieve the GLRecDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLRecDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RecurNum Desc: RecurNum   Required: True
      @param RecurLine Desc: RecurLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLRecDtlRow
   */  
export function get_RecurringJournals_Company_RecurNum_GLRecDtls_Company_RecurNum_RecurLine(Company:string, RecurNum:string, RecurLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLRecDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/RecurringJournals(" + Company + "," + RecurNum + ")/GLRecDtls(" + Company + "," + RecurNum + "," + RecurLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GLRecDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get GLRecScheds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLRecScheds1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RecurNum Desc: RecurNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRecSchedRow
   */  
export function get_RecurringJournals_Company_RecurNum_GLRecScheds(Company:string, RecurNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRecSchedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/RecurringJournals(" + Company + "," + RecurNum + ")/GLRecScheds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRecSchedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the GLRecSched item
   Description: Calls GetByID to retrieve the GLRecSched item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLRecSched1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RecurNum Desc: RecurNum   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLRecSchedRow
   */  
export function get_RecurringJournals_Company_RecurNum_GLRecScheds_Company_RecurNum_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company:string, RecurNum:string, FiscalCalendarID:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLRecSchedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/RecurringJournals(" + Company + "," + RecurNum + ")/GLRecScheds(" + Company + "," + RecurNum + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GLRecSchedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get GLRecDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLRecDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRecDtlRow
   */  
export function get_GLRecDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRecDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GLRecDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRecDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLRecDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLRecDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLRecDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLRecDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GLRecDtls", {
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
   Summary: Calls GetByID to retrieve the GLRecDtl item
   Description: Calls GetByID to retrieve the GLRecDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLRecDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RecurNum Desc: RecurNum   Required: True
      @param RecurLine Desc: RecurLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLRecDtlRow
   */  
export function get_GLRecDtls_Company_RecurNum_RecurLine(Company:string, RecurNum:string, RecurLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLRecDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GLRecDtls(" + Company + "," + RecurNum + "," + RecurLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GLRecDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLRecDtl for the service
   Description: Calls UpdateExt to update GLRecDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLRecDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RecurNum Desc: RecurNum   Required: True
      @param RecurLine Desc: RecurLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLRecDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLRecDtls_Company_RecurNum_RecurLine(Company:string, RecurNum:string, RecurLine:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GLRecDtls(" + Company + "," + RecurNum + "," + RecurLine + ")", {
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
   Summary: Call UpdateExt to delete GLRecDtl item
   Description: Call UpdateExt to delete GLRecDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLRecDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RecurNum Desc: RecurNum   Required: True
      @param RecurLine Desc: RecurLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLRecDtls_Company_RecurNum_RecurLine(Company:string, RecurNum:string, RecurLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GLRecDtls(" + Company + "," + RecurNum + "," + RecurLine + ")", {
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
   Summary: Calls GetRows for the service
   Description: Get GLRecScheds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLRecScheds
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRecSchedRow
   */  
export function get_GLRecScheds(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRecSchedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GLRecScheds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRecSchedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLRecScheds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLRecSchedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLRecSchedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLRecScheds(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GLRecScheds", {
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
   Summary: Calls GetByID to retrieve the GLRecSched item
   Description: Calls GetByID to retrieve the GLRecSched item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLRecSched
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RecurNum Desc: RecurNum   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLRecSchedRow
   */  
export function get_GLRecScheds_Company_RecurNum_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company:string, RecurNum:string, FiscalCalendarID:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLRecSchedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GLRecScheds(" + Company + "," + RecurNum + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GLRecSchedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLRecSched for the service
   Description: Calls UpdateExt to update GLRecSched. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLRecSched
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RecurNum Desc: RecurNum   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLRecSchedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLRecScheds_Company_RecurNum_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company:string, RecurNum:string, FiscalCalendarID:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GLRecScheds(" + Company + "," + RecurNum + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")", {
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
   Summary: Call UpdateExt to delete GLRecSched item
   Description: Call UpdateExt to delete GLRecSched item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLRecSched
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RecurNum Desc: RecurNum   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLRecScheds_Company_RecurNum_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company:string, RecurNum:string, FiscalCalendarID:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GLRecScheds(" + Company + "," + RecurNum + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRecHedListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRecHedListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRecHedListRow)
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseGLRecHed:string, whereClauseGLRecDtl:string, whereClauseGLRecSched:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseGLRecHed!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLRecHed=" + whereClauseGLRecHed
   }
   if(typeof whereClauseGLRecDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLRecDtl=" + whereClauseGLRecDtl
   }
   if(typeof whereClauseGLRecSched!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLRecSched=" + whereClauseGLRecSched
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GetRows" + params, {
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
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(recurNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof recurNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "recurNum=" + recurNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GetList" + params, {
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
   Summary: Invoke method AutoBalance
   Description: This method does Auto Balance for Recurring Journal record with number recurNum
and with line recurLine.
   OperationID: AutoBalance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoBalance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoBalance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AutoBalance(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/AutoBalance", {
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
   Summary: Invoke method ChangeBookID
   Description: This method updates the Fiscal Calendar when the book changes.  Book can be blank.
A blank book indicates use of the company fiscal calendar.
   OperationID: ChangeBookID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBookID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBookID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeBookID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/ChangeBookID", {
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
   Summary: Invoke method ChangeEntryMode
   Description: Method to call when changing the Entry Mode.
   OperationID: ChangeEntryMode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEntryMode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEntryMode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEntryMode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/ChangeEntryMode", {
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
   Summary: Invoke method ChangeGlAcct
   Description: This method resets the G/L Reference Type and Code when the G/L
Account changes.  Depending on the new GL account, the Reference Type/Code
can become mandatory or optional.  Make sure to call the GetMaskRefCodes method
of the GLRefTypBusiness Object to get the new list of all GL Reference Codes
related to the entered Account number.  This method will also return values for
GlRecDtl.RefCodeStatus and GlRecDtl.RefAcctDiv/RefAcctDept/RefAcctChart. Enable
update of GlRecDtl.GLRefCode if the value returned for RefCodeStatus is either "M"
for Mandatory or "O" for Optional.
   OperationID: ChangeGlAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeGlAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGlAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeGlAcct(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/ChangeGlAcct", {
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
   Summary: Invoke method ChangeRateType
   Description: Method to call when changing the Rate Type.
   OperationID: ChangeRateType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRateType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRateType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRateType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/ChangeRateType", {
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
   Summary: Invoke method CheckBalance
   Description: Before updating the GlRecHed record, CheckBalance will have to be called.
The CheckBalance method will check to make sure the TotCredit and TotDebit
fields are equal.
   OperationID: CheckBalance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBalance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBalance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckBalance(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/CheckBalance", {
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
   Summary: Invoke method CheckCurrencyAccount
   Description: This procudura validata if the Account is a currency Account
   OperationID: CheckCurrencyAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCurrencyAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCurrencyAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCurrencyAccount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/CheckCurrencyAccount", {
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
   Summary: Invoke method CheckCurrencyAccountExt
   Description: This procudure validate if the Account is a currency Account, define list of available currencies.
   OperationID: CheckCurrencyAccountExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCurrencyAccountExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCurrencyAccountExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCurrencyAccountExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/CheckCurrencyAccountExt", {
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
   Summary: Invoke method GetAvailableCurrencies
   Description: Return available currencies for account. It is for multicurrency accounts for public usage.
   OperationID: GetAvailableCurrencies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailableCurrencies_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableCurrencies_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailableCurrencies(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GetAvailableCurrencies", {
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
   Summary: Invoke method CheckStatUOMAccount
   Description: This procedure check selected account is a Statistical account
   OperationID: CheckStatUOMAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckStatUOMAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckStatUOMAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckStatUOMAccount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/CheckStatUOMAccount", {
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
   Summary: Invoke method CheckEAD
   Description: Validates if the passed date is not earlier than earliest apply date.
   OperationID: CheckEAD
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckEAD_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckEAD_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckEAD(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/CheckEAD", {
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
   Summary: Invoke method CheckGroupPrefixChange
   Description: This method checks if the group prefix on the recurring journal header changed
and if there are other recurring journals created for the book/multi-book.
If there are the group prefix on those records will be updated to the new value,
but check with user before performing this action.
   OperationID: CheckGroupPrefixChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckGroupPrefixChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckGroupPrefixChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckGroupPrefixChange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/CheckGroupPrefixChange", {
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
   Summary: Invoke method ConvertCreditAmount
   Description: This method convert the document currency to the journal currency.
   OperationID: ConvertCreditAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvertCreditAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertCreditAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConvertCreditAmount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/ConvertCreditAmount", {
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
   Summary: Invoke method ConvertDebitAmount
   Description: This method convert the document currency to the journal currency.
   OperationID: ConvertDebitAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvertDebitAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertDebitAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConvertDebitAmount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/ConvertDebitAmount", {
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
   Summary: Invoke method CreateSchedForYear
   Description: This method created GLRecSched records given a fiscal year.
   OperationID: CreateSchedForYear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateSchedForYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateSchedForYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateSchedForYear(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/CreateSchedForYear", {
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
   Summary: Invoke method GetGLRecSchedGenerate
   Description: This method returns the generate schedule dataset.
   OperationID: GetGLRecSchedGenerate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGLRecSchedGenerate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLRecSchedGenerate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGLRecSchedGenerate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GetGLRecSchedGenerate", {
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
   Summary: Invoke method Renumber
   Description: This method renumbers lines in Recurring Journal record with number recurNum.
   OperationID: Renumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Renumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Renumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Renumber(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/Renumber", {
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
   Summary: Invoke method ValidateCurrencyAccount
   Description: This procedure validate it the currency is allowed.
   OperationID: ValidateCurrencyAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCurrencyAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCurrencyAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateCurrencyAccount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/ValidateCurrencyAccount", {
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
   Summary: Invoke method GetCodeDescList
   Description: Gets the code/description list of the specified column translated to the user's language.
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GetCodeDescList", {
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
   Summary: Invoke method GetNewGLRecHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLRecHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLRecHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLRecHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLRecHed(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GetNewGLRecHed", {
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
   Summary: Invoke method GetNewGLRecDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLRecDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLRecDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLRecDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLRecDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GetNewGLRecDtl", {
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
   Summary: Invoke method GetNewGLRecSched
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLRecSched
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLRecSched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLRecSched_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLRecSched(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GetNewGLRecSched", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRecDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLRecDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRecHedListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLRecHedListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRecHedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLRecHedRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRecSchedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLRecSchedRow[],
}

export interface Erp_Tablesets_GLRecDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Number that is assigned by the system.  Defaults to ten(10) greater than the highest number (i.e. 10, 20, 30, etc.).  User can change number at any time, but GLRecDtl records must be kept in synchronization.  Cannot be zero(0).  */  
   "RecurNum":number,
      /**  Unique ID of entry within a Recur Number.  Allow user to change number at any time.  Defaults to ten(10) greater than the highest number (i.e. 10, 20, 30, etc.).  Cannot be zero(0).  */  
   "RecurLine":number,
      /**  Default from GLRecHed description.  */  
   "Description":string,
      /**  Zero/Positive = Debit, Negative = Credit.  */  
   "TranAmt":number,
      /**  Link to the related GLRefTyp.RefType.  */  
   "RefType":string,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "RefCode":string,
      /**  Flag that indicate if the account is a curency account  */  
   "CurrAcct":boolean,
      /**  Document Transaction amount.  */  
   "DocTransAmt":number,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCodeAcct":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   "GLAccount":string,
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
      /**  Used to create a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports.  */  
   "CorrAccUID":number,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   "Statistical":number,
      /**  Statistical UOM code.  */  
   "StatUOMCode":string,
      /**  This field shows Debit statistical amount.  */  
   "DebitStatAmt":number,
      /**  This field shows Credit statistical amount.  */  
   "CreditStatAmt":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "TotCredit":number,
   "TotDebit":number,
      /**  Reference Code Status  */  
   "RefCodeStatus":string,
   "RefAcctDiv":string,
   "RefAcctDept":string,
   "RefAcctChart":string,
   "TotCurrDebit":number,
   "TotCurrCredit":number,
      /**  Statistical Amount. UI display value.  */  
   "StatAmount":number,
   "StatisticalDesc":string,
   "CurrencyCodeAcctList":string,
   "BitFlag":number,
   "AcctCurrCurrName":string,
   "AcctCurrCurrencyID":string,
   "AcctCurrCurrSymbol":string,
   "AcctCurrCurrDesc":string,
   "AcctCurrDocumentDesc":string,
   "CurrencyCurrencyID":string,
   "CurrencyCurrDesc":string,
   "CurrencyCurrSymbol":string,
   "CurrencyCurrName":string,
   "CurrencyDocumentDesc":string,
   "GLGLAcctDisp":string,
   "GLAccountDesc":string,
   "GLGLShortAcct":string,
   "GlRefCodeDescRefCodeDesc":string,
   "RecurNumDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLRecHedListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Number that is assigned by the system.  Defaults to ten(10) greater than the highest number (i.e. 10, 20, 30, etc.).  User can change number at any time, but GLRecDtl and GLRecSched records must be kept in synchronization.  Cannot be zero(0).  */  
   "RecurNum":number,
      /**  Describes the Recurring Entry.  Used as a default for the GLRecDtl.Description field.  */  
   "Description":string,
      /**  The Total Debits.  A summary of the positive GLRecDtl.TranAmt in the related GLRecDtl records.  Primarily used for visual verification.  */  
   "TotDebit":number,
      /**  The Total Credit.  A summary of negative GLRecDtl.TranAmt in the related GLRecDtl records.  Primarily used for visual verification.  */  
   "TotCredit":number,
      /**  Indicates that this Recurring Entry set should create reversing entries for the next fiscal period when it is posted in G/L Journal Entry.  */  
   "Reverse":boolean,
      /**  Indicates that the recurring entry is active and will be selected during the next period close.  */  
   "ActiveEntry":boolean,
      /**  A LIST-DELIM delimited list of periods that the entry is to be selected in.  When this list is blank it means ALL periods are selected.  To set NO periods selected use the ActiveEntry flag.  */  
   "SelectedPeriodList":string,
      /**   A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.
NOT ACTIVE  AS OF 3.20RESERVED FOR FUTURE USE.  */  
   "JournalCode":string,
      /**  Indicates what mode the GL transactions will be entered. Valid values are (S) for Single Book and (M) for Multi-Book.  */  
   "BookMode":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  The prefix of the group (GLJrnGrp) created for recurring journal entries.  */  
   "GroupPrefix":string,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Statistical UOM code.  */  
   "StatUOMCode":string,
      /**  The id of the fiscal calendar.  */  
   "FiscalCalendarID":string,
      /**  This field shows the Total Debit statistical amount.  */  
   "DebitStatAmt":number,
      /**  Default is the first date of the next period. A date entered in this fields should be greater than the journal?s apply date.  */  
   "ReverseDate":string,
      /**  This field shows the Total Credit statistical amount.  */  
   "CreditStatAmt":number,
      /**  Flag that indicates if correspondence accounting is set-up for the journal.  */  
   "CorrAccounting":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "SelectedToggleBoxes":string,
      /**  TotDebit - TotCredit = Balance  */  
   "Balance":number,
      /**  Displays the Total Credit as positive.  */  
   "DispTotCredit":number,
      /**  Displays the Total Debit.  */  
   "DispTotDebit":number,
   "MultipleBooks":boolean,
      /**  Flag that indicates if correspondence accounting is set-up for the book.  */  
   "BookIDCorrAccounting":boolean,
      /**  Descripiton of Book  */  
   "BookIDDescription":string,
      /**  Indicates the base currency for the book  */  
   "BookIDCurrencyCode":string,
      /**  Calendar description.  */  
   "FiscalCalDescription":string,
      /**  Descripiton of Book  */  
   "GLBookDescription":string,
      /**  Indicates the base currency for the book  */  
   "GLBookCurrencyCode":string,
      /**  Journal  Description.  */  
   "JournalCodeJrnlDescription":string,
      /**  Description  */  
   "RateGrpCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLRecHedRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Number that is assigned by the system.  Defaults to ten(10) greater than the highest number (i.e. 10, 20, 30, etc.).  User can change number at any time, but GLRecDtl and GLRecSched records must be kept in synchronization.  Cannot be zero(0).  */  
   "RecurNum":number,
      /**  Describes the Recurring Entry.  Used as a default for the GLRecDtl.Description field.  */  
   "Description":string,
      /**  The Total Debits.  A summary of the positive GLRecDtl.TranAmt in the related GLRecDtl records.  Primarily used for visual verification.  */  
   "TotDebit":number,
      /**  The Total Credit.  A summary of negative GLRecDtl.TranAmt in the related GLRecDtl records.  Primarily used for visual verification.  */  
   "TotCredit":number,
      /**  Indicates that this Recurring Entry set should create reversing entries for the next fiscal period when it is posted in G/L Journal Entry.  */  
   "Reverse":boolean,
      /**  Indicates that the recurring entry is active and will be selected during the next period close.  */  
   "ActiveEntry":boolean,
      /**  A LIST-DELIM delimited list of periods that the entry is to be selected in.  When this list is blank it means ALL periods are selected.  To set NO periods selected use the ActiveEntry flag.  */  
   "SelectedPeriodList":string,
      /**   A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.
NOT ACTIVE  AS OF 3.20RESERVED FOR FUTURE USE.  */  
   "JournalCode":string,
      /**  Indicates what mode the GL transactions will be entered. Valid values are (S) for Single Book and (M) for Multi-Book.  */  
   "BookMode":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  The prefix of the group (GLJrnGrp) created for recurring journal entries.  */  
   "GroupPrefix":string,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Statistical UOM code.  */  
   "StatUOMCode":string,
      /**  The id of the fiscal calendar.  */  
   "FiscalCalendarID":string,
      /**  This field shows the Total Debit statistical amount.  */  
   "DebitStatAmt":number,
      /**  Default is the first date of the next period. A date entered in this fields should be greater than the journal?s apply date.  */  
   "ReverseDate":string,
      /**  This field shows the Total Credit statistical amount.  */  
   "CreditStatAmt":number,
      /**  Flag that indicates if correspondence accounting is set-up for the journal.  */  
   "CorrAccounting":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "SelectedToggleBoxes":string,
      /**  TotDebit - TotCredit = Balance  */  
   "Balance":number,
      /**  Displays the Total Credit as positive.  */  
   "DispTotCredit":number,
      /**  Displays the Total Debit.  */  
   "DispTotDebit":number,
   "MultipleBooks":boolean,
   "BitFlag":number,
   "BookIDCorrAccounting":boolean,
   "BookIDDescription":string,
   "BookIDCurrencyCode":string,
   "CurrencyCurrName":string,
   "CurrencyCurrSymbol":string,
   "CurrencyDocumentDesc":string,
   "CurrencyCurrencyID":string,
   "CurrencyCurrDesc":string,
   "FiscalCalDescription":string,
   "GLBookDescription":string,
   "GLBookCurrencyCode":string,
   "JournalCodeJrnlDescription":string,
   "RateGrpCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLRecSchedRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Identifier of GLRecHed.  */  
   "RecurNum":number,
      /**  The id of the fiscal calendar.  */  
   "FiscalCalendarID":string,
      /**  The fiscal year.  */  
   "FiscalYear":number,
      /**  The fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal period number.  */  
   "FiscalPeriod":number,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  The date to apply the entry to GL.  */  
   "ApplyDate":string,
      /**  The date the reversal is applied to GL.  */  
   "ReversalApplyDate":string,
      /**  The date this entry is scheduled to create the journal entry record.  */  
   "ScheduleDate":string,
      /**  The date the journal entry record was created.  System assigned.  */  
   "ActualDate":string,
      /**   Scheduled status.  Assigned by the user.  Values are:
S = Scheduled
NS = Not Scheduled  */  
   "SchedStatus":string,
      /**   Indicates the processing status.  System assigned.  Values are:
D = Done.  Record has been processed and converted into a journal detail.
I = Ignored.  Record was ignored during apply recurring journal process.
F = Fail.  An error occurred on this record during the apply recurring journal process.  */  
   "ProcStatus":string,
      /**  Indicates the reason a gl journal entry record could not be created for the year/period.  Assigned by the system.  Will be populated only when Status = "Fail".  */  
   "FailureReason":string,
      /**  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  */  
   "CloseFiscalPeriod":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param recurNum
      @param recurLine
      @param ds
   */  
export interface AutoBalance_input{
      /**  Recurring Journal record number  */  
   recurNum:number,
      /**  Recurring Journal record line number  */  
   recurLine:number,
   ds:Erp_Tablesets_RecurringJournalTableset[],
}

export interface AutoBalance_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RecurringJournalTableset[],
}
}

   /** Required : 
      @param ProposedBookID
      @param ds
   */  
export interface ChangeBookID_input{
      /**  The proposed Book  */  
   ProposedBookID:string,
   ds:Erp_Tablesets_RecurringJournalTableset[],
}

export interface ChangeBookID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RecurringJournalTableset[],
}
}

   /** Required : 
      @param proposedBookMode
      @param ds
   */  
export interface ChangeEntryMode_input{
      /**  The proposed Entry Mode  */  
   proposedBookMode:string,
   ds:Erp_Tablesets_RecurringJournalTableset[],
}

export interface ChangeEntryMode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RecurringJournalTableset[],
}
}

   /** Required : 
      @param ProposedDispAcct
      @param ds
   */  
export interface ChangeGlAcct_input{
      /**  The proposed G/L Display Account  */  
   ProposedDispAcct:string,
   ds:Erp_Tablesets_RecurringJournalTableset[],
}

export interface ChangeGlAcct_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RecurringJournalTableset[],
}
}

   /** Required : 
      @param proposedRateType
      @param ds
   */  
export interface ChangeRateType_input{
      /**  The proposed Rate Type  */  
   proposedRateType:string,
   ds:Erp_Tablesets_RecurringJournalTableset[],
}

export interface ChangeRateType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RecurringJournalTableset[],
}
}

   /** Required : 
      @param ds
      @param RecurNum
   */  
export interface CheckBalance_input{
   ds:Erp_Tablesets_RecurringJournalTableset[],
      /**  The current recurring journal number  */  
   RecurNum:number,
}

export interface CheckBalance_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RecurringJournalTableset[],
}
}

   /** Required : 
      @param ds
      @param iLineNum
   */  
export interface CheckCurrencyAccountExt_input{
   ds:Erp_Tablesets_RecurringJournalTableset[],
      /**  lineNum  */  
   iLineNum:number,
}

export interface CheckCurrencyAccountExt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RecurringJournalTableset[],
}
}

   /** Required : 
      @param ipCOACode
      @param ipSegValue
   */  
export interface CheckCurrencyAccount_input{
      /**  The current COACode  */  
   ipCOACode:string,
      /**  The current segment value one  */  
   ipSegValue:string,
}

export interface CheckCurrencyAccount_output{
parameters : {
      /**  output parameters  */  
   opCurr:boolean,
}
}

   /** Required : 
      @param ipDate
   */  
export interface CheckEAD_input{
      /**  The date to validate  */  
   ipDate:string,
}

export interface CheckEAD_output{
}

   /** Required : 
      @param inRecurNum
      @param inBookID
      @param inGroupPrefix
   */  
export interface CheckGroupPrefixChange_input{
      /**  The recurring journal entry number  */  
   inRecurNum:number,
      /**  The book id  */  
   inBookID:string,
      /**  The proposed group prefix  */  
   inGroupPrefix:string,
}

export interface CheckGroupPrefixChange_output{
parameters : {
      /**  output parameters  */  
   outMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CheckStatUOMAccount_input{
   ds:Erp_Tablesets_RecurringJournalTableset[],
}

export interface CheckStatUOMAccount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RecurringJournalTableset[],
}
}

   /** Required : 
      @param proposedAmount
      @param ds
   */  
export interface ConvertCreditAmount_input{
      /**  The proposed  Amount  */  
   proposedAmount:number,
   ds:Erp_Tablesets_RecurringJournalTableset[],
}

export interface ConvertCreditAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RecurringJournalTableset[],
}
}

   /** Required : 
      @param proposedAmount
      @param ds
   */  
export interface ConvertDebitAmount_input{
      /**  The proposed  Amount  */  
   proposedAmount:number,
   ds:Erp_Tablesets_RecurringJournalTableset[],
}

export interface ConvertDebitAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RecurringJournalTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface CreateSchedForYear_input{
   ds:Erp_Tablesets_GLRecSchedGenerateTableset[],
}

export interface CreateSchedForYear_output{
   returnObj:Erp_Tablesets_RecurringJournalTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLRecSchedGenerateTableset[],
   cOutMessage:string,
}
}

   /** Required : 
      @param recurNum
   */  
export interface DeleteByID_input{
   recurNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_GLRecDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Number that is assigned by the system.  Defaults to ten(10) greater than the highest number (i.e. 10, 20, 30, etc.).  User can change number at any time, but GLRecDtl records must be kept in synchronization.  Cannot be zero(0).  */  
   RecurNum:number,
      /**  Unique ID of entry within a Recur Number.  Allow user to change number at any time.  Defaults to ten(10) greater than the highest number (i.e. 10, 20, 30, etc.).  Cannot be zero(0).  */  
   RecurLine:number,
      /**  Default from GLRecHed description.  */  
   Description:string,
      /**  Zero/Positive = Debit, Negative = Credit.  */  
   TranAmt:number,
      /**  Link to the related GLRefTyp.RefType.  */  
   RefType:string,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  Flag that indicate if the account is a curency account  */  
   CurrAcct:boolean,
      /**  Document Transaction amount.  */  
   DocTransAmt:number,
      /**  A unique code that identifies the currency.  */  
   CurrencyCodeAcct:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   GLAccount:string,
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
      /**  Used to create a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports.  */  
   CorrAccUID:number,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   Statistical:number,
      /**  Statistical UOM code.  */  
   StatUOMCode:string,
      /**  This field shows Debit statistical amount.  */  
   DebitStatAmt:number,
      /**  This field shows Credit statistical amount.  */  
   CreditStatAmt:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   TotCredit:number,
   TotDebit:number,
      /**  Reference Code Status  */  
   RefCodeStatus:string,
   RefAcctDiv:string,
   RefAcctDept:string,
   RefAcctChart:string,
   TotCurrDebit:number,
   TotCurrCredit:number,
      /**  Statistical Amount. UI display value.  */  
   StatAmount:number,
   StatisticalDesc:string,
   CurrencyCodeAcctList:string,
   BitFlag:number,
   AcctCurrCurrName:string,
   AcctCurrCurrencyID:string,
   AcctCurrCurrSymbol:string,
   AcctCurrCurrDesc:string,
   AcctCurrDocumentDesc:string,
   CurrencyCurrencyID:string,
   CurrencyCurrDesc:string,
   CurrencyCurrSymbol:string,
   CurrencyCurrName:string,
   CurrencyDocumentDesc:string,
   GLGLAcctDisp:string,
   GLAccountDesc:string,
   GLGLShortAcct:string,
   GlRefCodeDescRefCodeDesc:string,
   RecurNumDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLRecHedListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Number that is assigned by the system.  Defaults to ten(10) greater than the highest number (i.e. 10, 20, 30, etc.).  User can change number at any time, but GLRecDtl and GLRecSched records must be kept in synchronization.  Cannot be zero(0).  */  
   RecurNum:number,
      /**  Describes the Recurring Entry.  Used as a default for the GLRecDtl.Description field.  */  
   Description:string,
      /**  The Total Debits.  A summary of the positive GLRecDtl.TranAmt in the related GLRecDtl records.  Primarily used for visual verification.  */  
   TotDebit:number,
      /**  The Total Credit.  A summary of negative GLRecDtl.TranAmt in the related GLRecDtl records.  Primarily used for visual verification.  */  
   TotCredit:number,
      /**  Indicates that this Recurring Entry set should create reversing entries for the next fiscal period when it is posted in G/L Journal Entry.  */  
   Reverse:boolean,
      /**  Indicates that the recurring entry is active and will be selected during the next period close.  */  
   ActiveEntry:boolean,
      /**  A LIST-DELIM delimited list of periods that the entry is to be selected in.  When this list is blank it means ALL periods are selected.  To set NO periods selected use the ActiveEntry flag.  */  
   SelectedPeriodList:string,
      /**   A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.
NOT ACTIVE  AS OF 3.20RESERVED FOR FUTURE USE.  */  
   JournalCode:string,
      /**  Indicates what mode the GL transactions will be entered. Valid values are (S) for Single Book and (M) for Multi-Book.  */  
   BookMode:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  The prefix of the group (GLJrnGrp) created for recurring journal entries.  */  
   GroupPrefix:string,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Statistical UOM code.  */  
   StatUOMCode:string,
      /**  The id of the fiscal calendar.  */  
   FiscalCalendarID:string,
      /**  This field shows the Total Debit statistical amount.  */  
   DebitStatAmt:number,
      /**  Default is the first date of the next period. A date entered in this fields should be greater than the journal?s apply date.  */  
   ReverseDate:string,
      /**  This field shows the Total Credit statistical amount.  */  
   CreditStatAmt:number,
      /**  Flag that indicates if correspondence accounting is set-up for the journal.  */  
   CorrAccounting:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   SelectedToggleBoxes:string,
      /**  TotDebit - TotCredit = Balance  */  
   Balance:number,
      /**  Displays the Total Credit as positive.  */  
   DispTotCredit:number,
      /**  Displays the Total Debit.  */  
   DispTotDebit:number,
   MultipleBooks:boolean,
      /**  Flag that indicates if correspondence accounting is set-up for the book.  */  
   BookIDCorrAccounting:boolean,
      /**  Descripiton of Book  */  
   BookIDDescription:string,
      /**  Indicates the base currency for the book  */  
   BookIDCurrencyCode:string,
      /**  Calendar description.  */  
   FiscalCalDescription:string,
      /**  Descripiton of Book  */  
   GLBookDescription:string,
      /**  Indicates the base currency for the book  */  
   GLBookCurrencyCode:string,
      /**  Journal  Description.  */  
   JournalCodeJrnlDescription:string,
      /**  Description  */  
   RateGrpCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLRecHedListTableset{
   GLRecHedList:Erp_Tablesets_GLRecHedListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GLRecHedRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Number that is assigned by the system.  Defaults to ten(10) greater than the highest number (i.e. 10, 20, 30, etc.).  User can change number at any time, but GLRecDtl and GLRecSched records must be kept in synchronization.  Cannot be zero(0).  */  
   RecurNum:number,
      /**  Describes the Recurring Entry.  Used as a default for the GLRecDtl.Description field.  */  
   Description:string,
      /**  The Total Debits.  A summary of the positive GLRecDtl.TranAmt in the related GLRecDtl records.  Primarily used for visual verification.  */  
   TotDebit:number,
      /**  The Total Credit.  A summary of negative GLRecDtl.TranAmt in the related GLRecDtl records.  Primarily used for visual verification.  */  
   TotCredit:number,
      /**  Indicates that this Recurring Entry set should create reversing entries for the next fiscal period when it is posted in G/L Journal Entry.  */  
   Reverse:boolean,
      /**  Indicates that the recurring entry is active and will be selected during the next period close.  */  
   ActiveEntry:boolean,
      /**  A LIST-DELIM delimited list of periods that the entry is to be selected in.  When this list is blank it means ALL periods are selected.  To set NO periods selected use the ActiveEntry flag.  */  
   SelectedPeriodList:string,
      /**   A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.
NOT ACTIVE  AS OF 3.20RESERVED FOR FUTURE USE.  */  
   JournalCode:string,
      /**  Indicates what mode the GL transactions will be entered. Valid values are (S) for Single Book and (M) for Multi-Book.  */  
   BookMode:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  The prefix of the group (GLJrnGrp) created for recurring journal entries.  */  
   GroupPrefix:string,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Statistical UOM code.  */  
   StatUOMCode:string,
      /**  The id of the fiscal calendar.  */  
   FiscalCalendarID:string,
      /**  This field shows the Total Debit statistical amount.  */  
   DebitStatAmt:number,
      /**  Default is the first date of the next period. A date entered in this fields should be greater than the journal?s apply date.  */  
   ReverseDate:string,
      /**  This field shows the Total Credit statistical amount.  */  
   CreditStatAmt:number,
      /**  Flag that indicates if correspondence accounting is set-up for the journal.  */  
   CorrAccounting:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   SelectedToggleBoxes:string,
      /**  TotDebit - TotCredit = Balance  */  
   Balance:number,
      /**  Displays the Total Credit as positive.  */  
   DispTotCredit:number,
      /**  Displays the Total Debit.  */  
   DispTotDebit:number,
   MultipleBooks:boolean,
   BitFlag:number,
   BookIDCorrAccounting:boolean,
   BookIDDescription:string,
   BookIDCurrencyCode:string,
   CurrencyCurrName:string,
   CurrencyCurrSymbol:string,
   CurrencyDocumentDesc:string,
   CurrencyCurrencyID:string,
   CurrencyCurrDesc:string,
   FiscalCalDescription:string,
   GLBookDescription:string,
   GLBookCurrencyCode:string,
   JournalCodeJrnlDescription:string,
   RateGrpCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLRecSchedGenerateRow{
   Company:string,
   RecurNum:number,
   FiscalCalendarID:string,
   FiscalYear:number,
   FiscalYearSuffix:string,
   CalendarDescription:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLRecSchedGenerateTableset{
   GLRecSchedGenerate:Erp_Tablesets_GLRecSchedGenerateRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GLRecSchedRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Identifier of GLRecHed.  */  
   RecurNum:number,
      /**  The id of the fiscal calendar.  */  
   FiscalCalendarID:string,
      /**  The fiscal year.  */  
   FiscalYear:number,
      /**  The fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal period number.  */  
   FiscalPeriod:number,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  The date to apply the entry to GL.  */  
   ApplyDate:string,
      /**  The date the reversal is applied to GL.  */  
   ReversalApplyDate:string,
      /**  The date this entry is scheduled to create the journal entry record.  */  
   ScheduleDate:string,
      /**  The date the journal entry record was created.  System assigned.  */  
   ActualDate:string,
      /**   Scheduled status.  Assigned by the user.  Values are:
S = Scheduled
NS = Not Scheduled  */  
   SchedStatus:string,
      /**   Indicates the processing status.  System assigned.  Values are:
D = Done.  Record has been processed and converted into a journal detail.
I = Ignored.  Record was ignored during apply recurring journal process.
F = Fail.  An error occurred on this record during the apply recurring journal process.  */  
   ProcStatus:string,
      /**  Indicates the reason a gl journal entry record could not be created for the year/period.  Assigned by the system.  Will be populated only when Status = "Fail".  */  
   FailureReason:string,
      /**  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  */  
   CloseFiscalPeriod:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RecurringJournalTableset{
   GLRecHed:Erp_Tablesets_GLRecHedRow[],
   GLRecDtl:Erp_Tablesets_GLRecDtlRow[],
   GLRecSched:Erp_Tablesets_GLRecSchedRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtRecurringJournalTableset{
   GLRecHed:Erp_Tablesets_GLRecHedRow[],
   GLRecDtl:Erp_Tablesets_GLRecDtlRow[],
   GLRecSched:Erp_Tablesets_GLRecSchedRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ipCOACode
      @param ipSegValue
   */  
export interface GetAvailableCurrencies_input{
   ipCOACode:string,
   ipSegValue:string,
}

export interface GetAvailableCurrencies_output{
   returnObj:string,
}

   /** Required : 
      @param recurNum
   */  
export interface GetByID_input{
   recurNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_RecurringJournalTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_RecurringJournalTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_RecurringJournalTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
      /**  The name of the table.  */  
   tableName:string,
      /**  The name of the column.  */  
   fieldName:string,
}

export interface GetCodeDescList_output{
      /**  Empty string is returned if the column is not found.  */  
   returnObj:string,
}

   /** Required : 
      @param inRecurNum
   */  
export interface GetGLRecSchedGenerate_input{
      /**  The GLRecHed number  */  
   inRecurNum:number,
}

export interface GetGLRecSchedGenerate_output{
   returnObj:Erp_Tablesets_GLRecSchedGenerateTableset[],
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
   returnObj:Erp_Tablesets_GLRecHedListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param recurNum
   */  
export interface GetNewGLRecDtl_input{
   ds:Erp_Tablesets_RecurringJournalTableset[],
   recurNum:number,
}

export interface GetNewGLRecDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RecurringJournalTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewGLRecHed_input{
   ds:Erp_Tablesets_RecurringJournalTableset[],
}

export interface GetNewGLRecHed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RecurringJournalTableset[],
}
}

   /** Required : 
      @param ds
      @param recurNum
      @param fiscalCalendarID
      @param fiscalYear
      @param fiscalYearSuffix
   */  
export interface GetNewGLRecSched_input{
   ds:Erp_Tablesets_RecurringJournalTableset[],
   recurNum:number,
   fiscalCalendarID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
}

export interface GetNewGLRecSched_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RecurringJournalTableset[],
}
}

   /** Required : 
      @param whereClauseGLRecHed
      @param whereClauseGLRecDtl
      @param whereClauseGLRecSched
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseGLRecHed:string,
   whereClauseGLRecDtl:string,
   whereClauseGLRecSched:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_RecurringJournalTableset[],
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
      @param recurNum
   */  
export interface Renumber_input{
      /**  Recurring Journal record number  */  
   recurNum:number,
}

export interface Renumber_output{
   returnObj:Erp_Tablesets_RecurringJournalTableset[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtRecurringJournalTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtRecurringJournalTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_RecurringJournalTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RecurringJournalTableset[],
}
}

   /** Required : 
      @param ds
      @param ipCurrency
      @param lineNum
   */  
export interface ValidateCurrencyAccount_input{
   ds:Erp_Tablesets_RecurringJournalTableset[],
      /**  The proposed Currency value  */  
   ipCurrency:string,
      /**  Lournal Line  */  
   lineNum:number,
}

export interface ValidateCurrencyAccount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RecurringJournalTableset[],
   message:string,
}
}

