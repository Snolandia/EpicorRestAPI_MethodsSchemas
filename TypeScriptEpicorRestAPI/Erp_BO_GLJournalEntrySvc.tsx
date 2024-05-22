import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.GLJournalEntrySvc
// Description: Business Object for Journal Entry
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/$metadata", {
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
   Description: Get GLJournalEntries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLJournalEntries
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnHedRow
   */  
export function get_GLJournalEntries(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJournalEntries", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLJournalEntries
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJrnHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GLJrnHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLJournalEntries(requestBody:Erp_Tablesets_GLJrnHedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJournalEntries", {
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
   Summary: Calls GetByID to retrieve the GLJournalEntry item
   Description: Calls GetByID to retrieve the GLJournalEntry item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJournalEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLJrnHedRow
   */  
export function get_GLJournalEntries_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, FiscalCalendarID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLJrnHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJournalEntries(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")", {
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
         resolve(data as Erp_Tablesets_GLJrnHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLJournalEntry for the service
   Description: Calls UpdateExt to update GLJournalEntry. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLJournalEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJrnHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLJournalEntries_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, FiscalCalendarID:string, requestBody:Erp_Tablesets_GLJrnHedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJournalEntries(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")", {
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
   Summary: Call UpdateExt to delete GLJournalEntry item
   Description: Call UpdateExt to delete GLJournalEntry item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLJournalEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLJournalEntries_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, FiscalCalendarID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJournalEntries(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")", {
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
   Summary: Calls GetByID for the service
   Description: Get GLJrnDtlMnls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLJrnDtlMnls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlMnlRow
   */  
export function get_GLJournalEntries_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID_GLJrnDtlMnls(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, FiscalCalendarID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJournalEntries(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")/GLJrnDtlMnls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the GLJrnDtlMnl item
   Description: Calls GetByID to retrieve the GLJrnDtlMnl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlMnl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param JournalLine Desc: JournalLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLJrnDtlMnlRow
   */  
export function get_GLJournalEntries_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, FiscalCalendarID:string, JournalLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLJrnDtlMnlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJournalEntries(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")", {
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
         resolve(data as Erp_Tablesets_GLJrnDtlMnlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get GLJrnHedAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLJrnHedAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnHedAttchRow
   */  
export function get_GLJournalEntries_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID_GLJrnHedAttches(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, FiscalCalendarID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnHedAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJournalEntries(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")/GLJrnHedAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnHedAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the GLJrnHedAttch item
   Description: Calls GetByID to retrieve the GLJrnHedAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnHedAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLJrnHedAttchRow
   */  
export function get_GLJournalEntries_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID_GLJrnHedAttches_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID_DrawingSeq(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, FiscalCalendarID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLJrnHedAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJournalEntries(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")/GLJrnHedAttches(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_GLJrnHedAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get GLJrnDtlMnls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLJrnDtlMnls
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlMnlRow
   */  
export function get_GLJrnDtlMnls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLJrnDtlMnls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GLJrnDtlMnlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLJrnDtlMnls(requestBody:Erp_Tablesets_GLJrnDtlMnlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnls", {
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
   Summary: Calls GetByID to retrieve the GLJrnDtlMnl item
   Description: Calls GetByID to retrieve the GLJrnDtlMnl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlMnl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLJrnDtlMnlRow
   */  
export function get_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, FiscalCalendarID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLJrnDtlMnlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")", {
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
         resolve(data as Erp_Tablesets_GLJrnDtlMnlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLJrnDtlMnl for the service
   Description: Calls UpdateExt to update GLJrnDtlMnl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLJrnDtlMnl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, FiscalCalendarID:string, requestBody:Erp_Tablesets_GLJrnDtlMnlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")", {
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
   Summary: Call UpdateExt to delete GLJrnDtlMnl item
   Description: Call UpdateExt to delete GLJrnDtlMnl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLJrnDtlMnl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, FiscalCalendarID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")", {
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
   Summary: Calls GetByID for the service
   Description: Get GLJrnDtlMnlDEASches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLJrnDtlMnlDEASches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlMnlDEASchRow
   */  
export function get_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID_GLJrnDtlMnlDEASches(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, FiscalCalendarID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlDEASchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")/GLJrnDtlMnlDEASches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlDEASchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the GLJrnDtlMnlDEASch item
   Description: Calls GetByID to retrieve the GLJrnDtlMnlDEASch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlMnlDEASch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param GLBookID Desc: GLBookID   Required: True   Allow empty value : True
      @param GLJournalNum Desc: GLJournalNum   Required: True
      @param AmortSeq Desc: AmortSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLJrnDtlMnlDEASchRow
   */  
export function get_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID_GLJrnDtlMnlDEASches_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_GLBookID_JournalCode_GLJournalNum_JournalLine_AmortSeq(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, FiscalCalendarID:string, GLBookID:string, GLJournalNum:string, AmortSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLJrnDtlMnlDEASchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")/GLJrnDtlMnlDEASches(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + GLBookID + "," + JournalCode + "," + GLJournalNum + "," + JournalLine + "," + AmortSeq + ")", {
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
         resolve(data as Erp_Tablesets_GLJrnDtlMnlDEASchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get GLJrnDtlMnlTranGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLJrnDtlMnlTranGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlMnlTranGLCRow
   */  
export function get_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID_GLJrnDtlMnlTranGLCs(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, FiscalCalendarID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlTranGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")/GLJrnDtlMnlTranGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlTranGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the GLJrnDtlMnlTranGLC item
   Description: Calls GetByID to retrieve the GLJrnDtlMnlTranGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlMnlTranGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLJrnDtlMnlTranGLCRow
   */  
export function get_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID_GLJrnDtlMnlTranGLCs_SysRowID(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, FiscalCalendarID:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLJrnDtlMnlTranGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")/GLJrnDtlMnlTranGLCs(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_GLJrnDtlMnlTranGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get GLJrnDtlMnlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLJrnDtlMnlAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlMnlAttchRow
   */  
export function get_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID_GLJrnDtlMnlAttches(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, FiscalCalendarID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")/GLJrnDtlMnlAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the GLJrnDtlMnlAttch item
   Description: Calls GetByID to retrieve the GLJrnDtlMnlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlMnlAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLJrnDtlMnlAttchRow
   */  
export function get_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID_GLJrnDtlMnlAttches_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID_DrawingSeq(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, FiscalCalendarID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLJrnDtlMnlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")/GLJrnDtlMnlAttches(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_GLJrnDtlMnlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get GLJrnDtlMnlDEASches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLJrnDtlMnlDEASches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlMnlDEASchRow
   */  
export function get_GLJrnDtlMnlDEASches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlDEASchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlDEASches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlDEASchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLJrnDtlMnlDEASches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlDEASchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GLJrnDtlMnlDEASchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLJrnDtlMnlDEASches(requestBody:Erp_Tablesets_GLJrnDtlMnlDEASchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlDEASches", {
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
   Summary: Calls GetByID to retrieve the GLJrnDtlMnlDEASch item
   Description: Calls GetByID to retrieve the GLJrnDtlMnlDEASch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlMnlDEASch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param GLBookID Desc: GLBookID   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param GLJournalNum Desc: GLJournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param AmortSeq Desc: AmortSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLJrnDtlMnlDEASchRow
   */  
export function get_GLJrnDtlMnlDEASches_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_GLBookID_JournalCode_GLJournalNum_JournalLine_AmortSeq(Company:string, FiscalCalendarID:string, FiscalYear:string, FiscalYearSuffix:string, GLBookID:string, JournalCode:string, GLJournalNum:string, JournalLine:string, AmortSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLJrnDtlMnlDEASchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlDEASches(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + GLBookID + "," + JournalCode + "," + GLJournalNum + "," + JournalLine + "," + AmortSeq + ")", {
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
         resolve(data as Erp_Tablesets_GLJrnDtlMnlDEASchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLJrnDtlMnlDEASch for the service
   Description: Calls UpdateExt to update GLJrnDtlMnlDEASch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLJrnDtlMnlDEASch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param GLBookID Desc: GLBookID   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param GLJournalNum Desc: GLJournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param AmortSeq Desc: AmortSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlDEASchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLJrnDtlMnlDEASches_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_GLBookID_JournalCode_GLJournalNum_JournalLine_AmortSeq(Company:string, FiscalCalendarID:string, FiscalYear:string, FiscalYearSuffix:string, GLBookID:string, JournalCode:string, GLJournalNum:string, JournalLine:string, AmortSeq:string, requestBody:Erp_Tablesets_GLJrnDtlMnlDEASchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlDEASches(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + GLBookID + "," + JournalCode + "," + GLJournalNum + "," + JournalLine + "," + AmortSeq + ")", {
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
   Summary: Call UpdateExt to delete GLJrnDtlMnlDEASch item
   Description: Call UpdateExt to delete GLJrnDtlMnlDEASch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLJrnDtlMnlDEASch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param GLBookID Desc: GLBookID   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param GLJournalNum Desc: GLJournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param AmortSeq Desc: AmortSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLJrnDtlMnlDEASches_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_GLBookID_JournalCode_GLJournalNum_JournalLine_AmortSeq(Company:string, FiscalCalendarID:string, FiscalYear:string, FiscalYearSuffix:string, GLBookID:string, JournalCode:string, GLJournalNum:string, JournalLine:string, AmortSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlDEASches(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + GLBookID + "," + JournalCode + "," + GLJournalNum + "," + JournalLine + "," + AmortSeq + ")", {
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
   Description: Get GLJrnDtlMnlTranGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLJrnDtlMnlTranGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlMnlTranGLCRow
   */  
export function get_GLJrnDtlMnlTranGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlTranGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlTranGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlTranGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLJrnDtlMnlTranGLCs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlTranGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GLJrnDtlMnlTranGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLJrnDtlMnlTranGLCs(requestBody:Erp_Tablesets_GLJrnDtlMnlTranGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlTranGLCs", {
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
   Summary: Calls GetByID to retrieve the GLJrnDtlMnlTranGLC item
   Description: Calls GetByID to retrieve the GLJrnDtlMnlTranGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlMnlTranGLC
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLJrnDtlMnlTranGLCRow
   */  
export function get_GLJrnDtlMnlTranGLCs_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLJrnDtlMnlTranGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlTranGLCs(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_GLJrnDtlMnlTranGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLJrnDtlMnlTranGLC for the service
   Description: Calls UpdateExt to update GLJrnDtlMnlTranGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLJrnDtlMnlTranGLC
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlTranGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLJrnDtlMnlTranGLCs_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_GLJrnDtlMnlTranGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlTranGLCs(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete GLJrnDtlMnlTranGLC item
   Description: Call UpdateExt to delete GLJrnDtlMnlTranGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLJrnDtlMnlTranGLC
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLJrnDtlMnlTranGLCs_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlTranGLCs(" + SysRowID + ")", {
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
   Description: Get GLJrnDtlMnlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLJrnDtlMnlAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlMnlAttchRow
   */  
export function get_GLJrnDtlMnlAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLJrnDtlMnlAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GLJrnDtlMnlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLJrnDtlMnlAttches(requestBody:Erp_Tablesets_GLJrnDtlMnlAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlAttches", {
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
   Summary: Calls GetByID to retrieve the GLJrnDtlMnlAttch item
   Description: Calls GetByID to retrieve the GLJrnDtlMnlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlMnlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLJrnDtlMnlAttchRow
   */  
export function get_GLJrnDtlMnlAttches_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID_DrawingSeq(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, FiscalCalendarID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLJrnDtlMnlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlAttches(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_GLJrnDtlMnlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLJrnDtlMnlAttch for the service
   Description: Calls UpdateExt to update GLJrnDtlMnlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLJrnDtlMnlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLJrnDtlMnlAttches_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID_DrawingSeq(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, FiscalCalendarID:string, DrawingSeq:string, requestBody:Erp_Tablesets_GLJrnDtlMnlAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlAttches(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete GLJrnDtlMnlAttch item
   Description: Call UpdateExt to delete GLJrnDtlMnlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLJrnDtlMnlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLJrnDtlMnlAttches_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID_DrawingSeq(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, FiscalCalendarID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlAttches(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + "," + DrawingSeq + ")", {
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
   Description: Get GLJrnHedAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLJrnHedAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnHedAttchRow
   */  
export function get_GLJrnHedAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnHedAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnHedAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnHedAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLJrnHedAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJrnHedAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GLJrnHedAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLJrnHedAttches(requestBody:Erp_Tablesets_GLJrnHedAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnHedAttches", {
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
   Summary: Calls GetByID to retrieve the GLJrnHedAttch item
   Description: Calls GetByID to retrieve the GLJrnHedAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnHedAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLJrnHedAttchRow
   */  
export function get_GLJrnHedAttches_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID_DrawingSeq(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, FiscalCalendarID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLJrnHedAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnHedAttches(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_GLJrnHedAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLJrnHedAttch for the service
   Description: Calls UpdateExt to update GLJrnHedAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLJrnHedAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJrnHedAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLJrnHedAttches_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID_DrawingSeq(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, FiscalCalendarID:string, DrawingSeq:string, requestBody:Erp_Tablesets_GLJrnHedAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnHedAttches(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete GLJrnHedAttch item
   Description: Call UpdateExt to delete GLJrnHedAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLJrnHedAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLJrnHedAttches_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID_DrawingSeq(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, FiscalCalendarID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnHedAttches(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + "," + DrawingSeq + ")", {
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
   Description: Get GlAllocations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlAllocations
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlAllocationsRow
   */  
export function get_GlAllocations(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlAllocationsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GlAllocations", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlAllocationsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlAllocations
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlAllocationsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GlAllocationsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GlAllocations(requestBody:Erp_Tablesets_GlAllocationsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GlAllocations", {
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
   Summary: Calls GetByID to retrieve the GlAllocation item
   Description: Calls GetByID to retrieve the GlAllocation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlAllocation
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GlAllocationsRow
   */  
export function get_GlAllocations_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GlAllocationsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GlAllocations(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_GlAllocationsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GlAllocation for the service
   Description: Calls UpdateExt to update GlAllocation. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlAllocation
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlAllocationsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GlAllocations_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_GlAllocationsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GlAllocations(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete GlAllocation item
   Description: Call UpdateExt to delete GlAllocation item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlAllocation
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GlAllocations_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GlAllocations(" + SysRowID + ")", {
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
   Description: Get LegalNumGenOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumGenOpts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumGenOptsRow
   */  
export function get_LegalNumGenOpts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/LegalNumGenOpts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumGenOpts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LegalNumGenOpts(requestBody:Erp_Tablesets_LegalNumGenOptsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/LegalNumGenOpts", {
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
   Summary: Calls GetByID to retrieve the LegalNumGenOpt item
   Description: Calls GetByID to retrieve the LegalNumGenOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumGenOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   */  
export function get_LegalNumGenOpts_Company_LegalNumberID(Company:string, LegalNumberID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LegalNumGenOptsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
         resolve(data as Erp_Tablesets_LegalNumGenOptsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LegalNumGenOpt for the service
   Description: Calls UpdateExt to update LegalNumGenOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumGenOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LegalNumGenOpts_Company_LegalNumberID(Company:string, LegalNumberID:string, requestBody:Erp_Tablesets_LegalNumGenOptsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
   Summary: Call UpdateExt to delete LegalNumGenOpt item
   Description: Call UpdateExt to delete LegalNumGenOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumGenOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LegalNumGenOpts_Company_LegalNumberID(Company:string, LegalNumberID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnHedListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnHedListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnHedListRow)
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
export function get_GetRows(whereClauseGLJrnHed:string, whereClauseGLJrnHedAttch:string, whereClauseGLJrnDtlMnl:string, whereClauseGLJrnDtlMnlAttch:string, whereClauseGLJrnDtlMnlDEASch:string, whereClauseGLJrnDtlMnlTranGLC:string, whereClauseGlAllocations:string, whereClauseLegalNumGenOpts:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseGLJrnHed!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLJrnHed=" + whereClauseGLJrnHed
   }
   if(typeof whereClauseGLJrnHedAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLJrnHedAttch=" + whereClauseGLJrnHedAttch
   }
   if(typeof whereClauseGLJrnDtlMnl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLJrnDtlMnl=" + whereClauseGLJrnDtlMnl
   }
   if(typeof whereClauseGLJrnDtlMnlAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLJrnDtlMnlAttch=" + whereClauseGLJrnDtlMnlAttch
   }
   if(typeof whereClauseGLJrnDtlMnlDEASch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLJrnDtlMnlDEASch=" + whereClauseGLJrnDtlMnlDEASch
   }
   if(typeof whereClauseGLJrnDtlMnlTranGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLJrnDtlMnlTranGLC=" + whereClauseGLJrnDtlMnlTranGLC
   }
   if(typeof whereClauseGlAllocations!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGlAllocations=" + whereClauseGlAllocations
   }
   if(typeof whereClauseLegalNumGenOpts!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLegalNumGenOpts=" + whereClauseLegalNumGenOpts
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(bookID:string, fiscalYear:string, fiscalYearSuffix:string, journalCode:string, journalNum:string, fiscalCalendarID:string, epicorHeaders?:Headers){
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
   if(typeof journalCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "journalCode=" + journalCode
   }
   if(typeof journalNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "journalNum=" + journalNum
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetList" + params, {
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
   Summary: Invoke method AutoBalance
   Description: This method will create a new line with the balancing figure defaulted
into the appropriate debit or credit column if the current line has a
non-zero balance.  If the current line has zero debit/credit values then
the debit/credit values of that line are updated with the balancing entry.
   OperationID: AutoBalance
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AutoBalance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoBalance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AutoBalance(requestBody:AutoBalance_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AutoBalance_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/AutoBalance", {
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
         resolve(data as AutoBalance_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AutoComplete
   Description: This method is called only for 'Tax Line' and will update current line in the following way:
- calculate tax amount using tax type, tax rate and taxable amount from 'Tax Options' and update correspondent amount (credit or debit);
- update account
   OperationID: AutoComplete
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AutoComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AutoComplete(requestBody:AutoComplete_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AutoComplete_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/AutoComplete", {
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
         resolve(data as AutoComplete_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CalculateAmountForTaxLineEx
   Description: This method calculates debit/credit amount if selected tax rate is applied to the taxable amount
   OperationID: CalculateAmountForTaxLineEx
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CalculateAmountForTaxLineEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateAmountForTaxLineEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalculateAmountForTaxLineEx(requestBody:CalculateAmountForTaxLineEx_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CalculateAmountForTaxLineEx_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/CalculateAmountForTaxLineEx", {
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
         resolve(data as CalculateAmountForTaxLineEx_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeExtCompanyID
   Description: This method resets the regular and Multi-Company G/L Accounts and the Reference Codes
when the External Company ID changes.
   OperationID: ChangeExtCompanyID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeExtCompanyID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeExtCompanyID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeExtCompanyID(requestBody:ChangeExtCompanyID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeExtCompanyID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/ChangeExtCompanyID", {
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
         resolve(data as ChangeExtCompanyID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeGlAcct1
   Description: This method calls Check StatUOMCoe and CheckCurrencyAccount instead 2 calls from UIs
   OperationID: ChangeGlAcct1
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeGlAcct1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGlAcct1_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeGlAcct1(requestBody:ChangeGlAcct1_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeGlAcct1_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/ChangeGlAcct1", {
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
         resolve(data as ChangeGlAcct1_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeExtGlAcct
   Description: This method calls Check if external G/L Account is valid
   OperationID: ChangeExtGlAcct
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeExtGlAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeExtGlAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeExtGlAcct(requestBody:ChangeExtGlAcct_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeExtGlAcct_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/ChangeExtGlAcct", {
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
         resolve(data as ChangeExtGlAcct_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeGlRefCode
   Description: This method updates the G/L Reference Type and Code Description when the
GL Reference Code changes.
   OperationID: ChangeGlRefCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeGlRefCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGlRefCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeGlRefCode(requestBody:ChangeGlRefCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeGlRefCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/ChangeGlRefCode", {
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
         resolve(data as ChangeGlRefCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeLinkedLineAmnts
   Description: This method updates amounts in the linked journal details.
   OperationID: ChangeLinkedLineAmnts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeLinkedLineAmnts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLinkedLineAmnts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeLinkedLineAmnts(requestBody:ChangeLinkedLineAmnts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeLinkedLineAmnts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/ChangeLinkedLineAmnts", {
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
         resolve(data as ChangeLinkedLineAmnts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeMultiCompany
   Description: This method resets the External Company ID, regular and Multi-Company G/L Accounts
and the Reference Codes when the Multi-Company flag changes.
   OperationID: ChangeMultiCompany
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeMultiCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMultiCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMultiCompany(requestBody:ChangeMultiCompany_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeMultiCompany_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/ChangeMultiCompany", {
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
         resolve(data as ChangeMultiCompany_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeReverse
   Description: This method defaults the Reverse Date when the Reverse flag is checked.
   OperationID: ChangeReverse
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeReverse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeReverse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeReverse(requestBody:ChangeReverse_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeReverse_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/ChangeReverse", {
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
         resolve(data as ChangeReverse_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTaxCode
   Description: This method gets the default Tax Rate for a Tax Code
   OperationID: ChangeTaxCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTaxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaxCode(requestBody:ChangeTaxCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTaxCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/ChangeTaxCode", {
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
         resolve(data as ChangeTaxCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckAllocations
   Description: This procudura validata if there is Allocations for the Journal Book
   OperationID: CheckAllocations
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckAllocations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAllocations_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckAllocations(requestBody:CheckAllocations_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckAllocations_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/CheckAllocations", {
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
         resolve(data as CheckAllocations_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckCurrencyAccount
   Description: This procedure validates if the Account is a currency Account
   OperationID: CheckCurrencyAccount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckCurrencyAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCurrencyAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCurrencyAccount(requestBody:CheckCurrencyAccount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckCurrencyAccount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/CheckCurrencyAccount", {
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
         resolve(data as CheckCurrencyAccount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckCurrencyAccountExt
   Description: This procedure validates if the Account is a currency Account, define list of available currencies.
   OperationID: CheckCurrencyAccountExt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckCurrencyAccountExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCurrencyAccountExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCurrencyAccountExt(requestBody:CheckCurrencyAccountExt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckCurrencyAccountExt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/CheckCurrencyAccountExt", {
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
         resolve(data as CheckCurrencyAccountExt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckStatUOMAccount
   Description: This
   OperationID: CheckStatUOMAccount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckStatUOMAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckStatUOMAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckStatUOMAccount(requestBody:CheckStatUOMAccount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckStatUOMAccount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/CheckStatUOMAccount", {
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
         resolve(data as CheckStatUOMAccount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckCurrencyAccount2
   Description: This procudura validate if the Account is a currency Account
   OperationID: CheckCurrencyAccount2
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckCurrencyAccount2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCurrencyAccount2_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCurrencyAccount2(requestBody:CheckCurrencyAccount2_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckCurrencyAccount2_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/CheckCurrencyAccount2", {
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
         resolve(data as CheckCurrencyAccount2_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckCurrencyAccountForTaxLine
   Description: This procudure validate if the Account is a currency Account for tax line with linked taxable line
   OperationID: CheckCurrencyAccountForTaxLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckCurrencyAccountForTaxLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCurrencyAccountForTaxLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCurrencyAccountForTaxLine(requestBody:CheckCurrencyAccountForTaxLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckCurrencyAccountForTaxLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/CheckCurrencyAccountForTaxLine", {
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
         resolve(data as CheckCurrencyAccountForTaxLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckDocumentIsLocked
   Description: Method to call when it is necessary to check if document is lock, before doing smth.
   OperationID: CheckDocumentIsLocked
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckDocumentIsLocked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDocumentIsLocked_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDocumentIsLocked(requestBody:CheckDocumentIsLocked_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckDocumentIsLocked_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/CheckDocumentIsLocked", {
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
         resolve(data as CheckDocumentIsLocked_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckDtlBeforeUpdate
   Description: Check that Journal Line is not linked from another External Company
   OperationID: CheckDtlBeforeUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckDtlBeforeUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDtlBeforeUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDtlBeforeUpdate(requestBody:CheckDtlBeforeUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckDtlBeforeUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/CheckDtlBeforeUpdate", {
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
         resolve(data as CheckDtlBeforeUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPartOfDual
   Description: This procudura checks In/Out value.
   OperationID: CheckPartOfDual
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckPartOfDual_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPartOfDual_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPartOfDual(requestBody:CheckPartOfDual_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckPartOfDual_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/CheckPartOfDual", {
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
         resolve(data as CheckPartOfDual_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckReportingModule
   Description: This procudura checks Reporting Module value.
   OperationID: CheckReportingModule
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckReportingModule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckReportingModule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckReportingModule(requestBody:CheckReportingModule_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckReportingModule_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/CheckReportingModule", {
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
         resolve(data as CheckReportingModule_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckTaxableLine
   Description: This procudura checks taxable line: it should exist and not a tax line.
   OperationID: CheckTaxableLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckTaxableLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTaxableLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckTaxableLine(requestBody:CheckTaxableLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckTaxableLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/CheckTaxableLine", {
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
         resolve(data as CheckTaxableLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckTaxAmountSign
   Description: This procudura checks whether sign of tax amount correspond to sign of taxable amount
   OperationID: CheckTaxAmountSign
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckTaxAmountSign_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTaxAmountSign_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckTaxAmountSign(requestBody:CheckTaxAmountSign_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckTaxAmountSign_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/CheckTaxAmountSign", {
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
         resolve(data as CheckTaxAmountSign_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckTaxLiability
   Description: This procudura checks Tax liability exists and not flagged as used in Tax Connect.
   OperationID: CheckTaxLiability
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckTaxLiability_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTaxLiability_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckTaxLiability(requestBody:CheckTaxLiability_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckTaxLiability_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/CheckTaxLiability", {
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
         resolve(data as CheckTaxLiability_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckTaxPointDate
   Description: This procudure checks whether Tax Point date is not later then tax rate Effective from date
   OperationID: CheckTaxPointDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckTaxPointDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTaxPointDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckTaxPointDate(requestBody:CheckTaxPointDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckTaxPointDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/CheckTaxPointDate", {
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
         resolve(data as CheckTaxPointDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckTaxRate
   Description: This procudura checks Tax Rate
   OperationID: CheckTaxRate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckTaxRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTaxRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckTaxRate(requestBody:CheckTaxRate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckTaxRate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/CheckTaxRate", {
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
         resolve(data as CheckTaxRate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckTaxType
   Description: This procudure checks Tax Type
   OperationID: CheckTaxType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckTaxType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTaxType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckTaxType(requestBody:CheckTaxType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckTaxType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/CheckTaxType", {
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
         resolve(data as CheckTaxType_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ConvertCreditAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertCreditAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConvertCreditAmount(requestBody:ConvertCreditAmount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ConvertCreditAmount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/ConvertCreditAmount", {
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
         resolve(data as ConvertCreditAmount_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ConvertDebitAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertDebitAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConvertDebitAmount(requestBody:ConvertDebitAmount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ConvertDebitAmount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/ConvertDebitAmount", {
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
         resolve(data as ConvertDebitAmount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateDetailLineFromAllocation
   Description: /// Call this method when the user clicks OK on the allocation sheet.  It
/// will create journal entries using the allocation information entered.
///
   OperationID: CreateDetailLineFromAllocation
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateDetailLineFromAllocation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateDetailLineFromAllocation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateDetailLineFromAllocation(requestBody:CreateDetailLineFromAllocation_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateDetailLineFromAllocation_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/CreateDetailLineFromAllocation", {
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
         resolve(data as CreateDetailLineFromAllocation_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenLegalNum
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method is called when the journal was created from recurring journal
and legal number is set as 'manual'.
   OperationID: GenLegalNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenLegalNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenLegalNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenLegalNum(requestBody:GenLegalNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenLegalNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GenLegalNum", {
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
         resolve(data as GenLegalNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByGroupID
   Description: This method is called in place of the GetByID method, requiring only the
the GL Group ID.
   OperationID: GetByGroupID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetByGroupID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByGroupID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByGroupID(requestBody:GetByGroupID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByGroupID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetByGroupID", {
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
         resolve(data as GetByGroupID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGlJrnHedTran
   Description: This method is called in place of the GetNewGlJrnHed method.  It allows
the input of the Current Group so that certian fields on the header
record can be defaulted from the group record.
   OperationID: GetNewGlJrnHedTran
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGlJrnHedTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlJrnHedTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGlJrnHedTran(requestBody:GetNewGlJrnHedTran_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGlJrnHedTran_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetNewGlJrnHedTran", {
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
         resolve(data as GetNewGlJrnHedTran_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewStatisticalGLJrnHed
   Description: Create Statistical Journal
   OperationID: GetNewStatisticalGLJrnHed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewStatisticalGLJrnHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewStatisticalGLJrnHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewStatisticalGLJrnHed(requestBody:GetNewStatisticalGLJrnHed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewStatisticalGLJrnHed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetNewStatisticalGLJrnHed", {
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
         resolve(data as GetNewStatisticalGLJrnHed_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTaxEntryMode
   Description: Get company value 'Tax Entry Mode in GL Journal'
   OperationID: GetTaxEntryMode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxEntryMode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTaxEntryMode(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTaxEntryMode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetTaxEntryMode", {
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
         resolve(data as GetTaxEntryMode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTaxRatesList
   Description: Get the list of tax rates, related to specified Tax Type
   OperationID: GetTaxRatesList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTaxRatesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxRatesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTaxRatesList(requestBody:GetTaxRatesList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTaxRatesList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetTaxRatesList", {
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
         resolve(data as GetTaxRatesList_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAvailableCurrencies_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableCurrencies_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailableCurrencies(requestBody:GetAvailableCurrencies_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAvailableCurrencies_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetAvailableCurrencies", {
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
         resolve(data as GetAvailableCurrencies_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTaxTypesList
   Description: Get where clause to select tax types, related to specified Tax Liability
   OperationID: GetTaxTypesList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTaxTypesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxTypesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTaxTypesList(requestBody:GetTaxTypesList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTaxTypesList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetTaxTypesList", {
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
         resolve(data as GetTaxTypesList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRefSourceJrnLineList
   Description: Gets SourceJrnLineList from current GL Journal
   OperationID: GetRefSourceJrnLineList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRefSourceJrnLineList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRefSourceJrnLineList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRefSourceJrnLineList(requestBody:GetRefSourceJrnLineList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRefSourceJrnLineList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetRefSourceJrnLineList", {
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
         resolve(data as GetRefSourceJrnLineList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTaxableLinesList
   Description: Gets TaxableLinesList from current GL Journal
   OperationID: GetTaxableLinesList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTaxableLinesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxableLinesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTaxableLinesList(requestBody:GetTaxableLinesList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTaxableLinesList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetTaxableLinesList", {
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
         resolve(data as GetTaxableLinesList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreGenLegalNum
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method is called when the journal was created from recurring journal
and legal number is set as 'manual'.
   OperationID: PreGenLegalNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreGenLegalNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreGenLegalNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreGenLegalNum(requestBody:PreGenLegalNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreGenLegalNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/PreGenLegalNum", {
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
         resolve(data as PreGenLegalNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreUpdate
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreUpdate(requestBody:PreUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/PreUpdate", {
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
         resolve(data as PreUpdate_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateCurrencyAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCurrencyAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateCurrencyAccount(requestBody:ValidateCurrencyAccount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateCurrencyAccount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/ValidateCurrencyAccount", {
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
         resolve(data as ValidateCurrencyAccount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateAccountForStatJournal
   Description: Validate Account For Statistical Journal
   OperationID: ValidateAccountForStatJournal
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateAccountForStatJournal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateAccountForStatJournal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateAccountForStatJournal(requestBody:ValidateAccountForStatJournal_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateAccountForStatJournal_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/ValidateAccountForStatJournal", {
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
         resolve(data as ValidateAccountForStatJournal_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateAccountForAllocation
   Description: Validate Account For Allocation
   OperationID: ValidateAccountForAllocation
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateAccountForAllocation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateAccountForAllocation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateAccountForAllocation(requestBody:ValidateAccountForAllocation_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateAccountForAllocation_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/ValidateAccountForAllocation", {
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
         resolve(data as ValidateAccountForAllocation_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeCurrencyAcct
   Description: This method should be called when book currency is changed
   OperationID: OnChangeCurrencyAcct
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeCurrencyAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCurrencyAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCurrencyAcct(requestBody:OnChangeCurrencyAcct_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeCurrencyAcct_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/OnChangeCurrencyAcct", {
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
         resolve(data as OnChangeCurrencyAcct_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTaxableAmntInTranCurr
   Description: This method should be called when Taxable amount in transactional currency is changed
   OperationID: OnChangeTaxableAmntInTranCurr
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTaxableAmntInTranCurr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxableAmntInTranCurr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTaxableAmntInTranCurr(requestBody:OnChangeTaxableAmntInTranCurr_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTaxableAmntInTranCurr_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/OnChangeTaxableAmntInTranCurr", {
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
         resolve(data as OnChangeTaxableAmntInTranCurr_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTaxableLine
   Description: This method should be called when Taxable Line is changed
   OperationID: OnChangeTaxableLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTaxableLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxableLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTaxableLine(requestBody:OnChangeTaxableLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTaxableLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/OnChangeTaxableLine", {
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
         resolve(data as OnChangeTaxableLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTaxLiability
   Description: This method should be called when Tax Liability is changed
   OperationID: OnChangeTaxLiability
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTaxLiability_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxLiability_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTaxLiability(requestBody:OnChangeTaxLiability_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTaxLiability_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/OnChangeTaxLiability", {
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
         resolve(data as OnChangeTaxLiability_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTaxRate
   Description: This method should be called when Tax Rate is changed
   OperationID: OnChangeTaxRate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTaxRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTaxRate(requestBody:OnChangeTaxRate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTaxRate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/OnChangeTaxRate", {
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
         resolve(data as OnChangeTaxRate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTaxType
   Description: This method should be called when Tax Type is changed
   OperationID: OnChangeTaxType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTaxType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTaxType(requestBody:OnChangeTaxType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTaxType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/OnChangeTaxType", {
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
         resolve(data as OnChangeTaxType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTranDocTypeID
   Description: Sets default values when the TranDocTypeID changes
   OperationID: OnChangeTranDocTypeID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTranDocTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTranDocTypeID(requestBody:OnChangeTranDocTypeID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTranDocTypeID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/OnChangeTranDocTypeID", {
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
         resolve(data as OnChangeTranDocTypeID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeLineReferenceHolder
   Description: This method should be called when Line Reference Holder is changed
   OperationID: OnChangeLineReferenceHolder
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeLineReferenceHolder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLineReferenceHolder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeLineReferenceHolder(requestBody:OnChangeLineReferenceHolder_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeLineReferenceHolder_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/OnChangeLineReferenceHolder", {
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
         resolve(data as OnChangeLineReferenceHolder_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeLineReference
   Description: This method should be called when Line Reference is changed
   OperationID: OnChangeLineReference
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeLineReference_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLineReference_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeLineReference(requestBody:OnChangeLineReference_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeLineReference_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/OnChangeLineReference", {
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
         resolve(data as OnChangeLineReference_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetDefaultsForTaxLine
   Description: Set default values if user check/uncheck 'Tax Line' option
   OperationID: SetDefaultsForTaxLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetDefaultsForTaxLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetDefaultsForTaxLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetDefaultsForTaxLine(requestBody:SetDefaultsForTaxLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetDefaultsForTaxLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/SetDefaultsForTaxLine", {
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
         resolve(data as SetDefaultsForTaxLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateAmountForTaxLine
   Description: This method updates debit/credit amount
   OperationID: UpdateAmountForTaxLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateAmountForTaxLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAmountForTaxLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateAmountForTaxLine(requestBody:UpdateAmountForTaxLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateAmountForTaxLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/UpdateAmountForTaxLine", {
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
         resolve(data as UpdateAmountForTaxLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VoidLegalNumber
   Description: Voids the legal number.
   OperationID: VoidLegalNumber
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/VoidLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VoidLegalNumber(requestBody:VoidLegalNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<VoidLegalNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/VoidLegalNumber", {
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
         resolve(data as VoidLegalNumber_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAllocations
   OperationID: GetAllocations
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAllocations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllocations_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAllocations(requestBody:GetAllocations_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAllocations_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetAllocations", {
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
         resolve(data as GetAllocations_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeLineDefferedExp
   Description: Occurs when Invoice Line Deferred Expense switch changed
   OperationID: OnChangeLineDefferedExp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeLineDefferedExp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLineDefferedExp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeLineDefferedExp(requestBody:OnChangeLineDefferedExp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeLineDefferedExp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/OnChangeLineDefferedExp", {
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
         resolve(data as OnChangeLineDefferedExp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeLineDEACode
   Description: Occurs when Invoice Line DEA Code changed
   OperationID: OnChangeLineDEACode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeLineDEACode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLineDEACode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeLineDEACode(requestBody:OnChangeLineDEACode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeLineDEACode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/OnChangeLineDEACode", {
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
         resolve(data as OnChangeLineDEACode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeLineDEAAccount
   Description: Occurs when GL Journal Line DEA Account changed
   OperationID: OnChangeLineDEAAccount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeLineDEAAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLineDEAAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeLineDEAAccount(requestBody:OnChangeLineDEAAccount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeLineDEAAccount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/OnChangeLineDEAAccount", {
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
         resolve(data as OnChangeLineDEAAccount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeLineDEAStartDate
   Description: Occurs when Invoice Line DEA Start Date changed
   OperationID: OnChangeLineDEAStartDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeLineDEAStartDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLineDEAStartDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeLineDEAStartDate(requestBody:OnChangeLineDEAStartDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeLineDEAStartDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/OnChangeLineDEAStartDate", {
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
         resolve(data as OnChangeLineDEAStartDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateAmortizationSchedule
   Description: Generates Amortization Schedule
   OperationID: GenerateAmortizationSchedule
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenerateAmortizationSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateAmortizationSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateAmortizationSchedule(requestBody:GenerateAmortizationSchedule_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenerateAmortizationSchedule_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GenerateAmortizationSchedule", {
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
         resolve(data as GenerateAmortizationSchedule_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteAmortizationSchedule
   Description: Deletes Amortization Schedule
   OperationID: DeleteAmortizationSchedule
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteAmortizationSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteAmortizationSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteAmortizationSchedule(requestBody:DeleteAmortizationSchedule_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteAmortizationSchedule_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/DeleteAmortizationSchedule", {
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
         resolve(data as DeleteAmortizationSchedule_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDEAScheduleLineAmount
   Description: Occurs when DEA Schedule Line Amortization Amount changed
   OperationID: OnChangeDEAScheduleLineAmount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDEAScheduleLineAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDEAScheduleLineAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDEAScheduleLineAmount(requestBody:OnChangeDEAScheduleLineAmount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDEAScheduleLineAmount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/OnChangeDEAScheduleLineAmount", {
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
         resolve(data as OnChangeDEAScheduleLineAmount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDEAScheduleLineFiscalPeriod
   Description: Occurs when DEA Schedule Line Fiscal Period changed
   OperationID: OnChangeDEAScheduleLineFiscalPeriod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDEAScheduleLineFiscalPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDEAScheduleLineFiscalPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDEAScheduleLineFiscalPeriod(requestBody:OnChangeDEAScheduleLineFiscalPeriod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDEAScheduleLineFiscalPeriod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/OnChangeDEAScheduleLineFiscalPeriod", {
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
         resolve(data as OnChangeDEAScheduleLineFiscalPeriod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AutocompleteAmortizationSchedule
   Description: Applies Remaining Amount to the last Schedule Line
   OperationID: AutocompleteAmortizationSchedule
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AutocompleteAmortizationSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutocompleteAmortizationSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AutocompleteAmortizationSchedule(requestBody:AutocompleteAmortizationSchedule_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AutocompleteAmortizationSchedule_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/AutocompleteAmortizationSchedule", {
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
         resolve(data as AutocompleteAmortizationSchedule_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CalculateAmortizationTotals
   Description: Calculates Deferred Expense Amortization Total Amounts
   OperationID: CalculateAmortizationTotals
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CalculateAmortizationTotals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateAmortizationTotals_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalculateAmortizationTotals(requestBody:CalculateAmortizationTotals_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CalculateAmortizationTotals_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/CalculateAmortizationTotals", {
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
         resolve(data as CalculateAmortizationTotals_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGLJrnDtlMnlDEASchPopulated
   Description: Inserts a new row into the DataSet with fields populated depending on parent Invoice Line
   OperationID: GetNewGLJrnDtlMnlDEASchPopulated
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnDtlMnlDEASchPopulated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnDtlMnlDEASchPopulated_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLJrnDtlMnlDEASchPopulated(requestBody:GetNewGLJrnDtlMnlDEASchPopulated_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGLJrnDtlMnlDEASchPopulated_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetNewGLJrnDtlMnlDEASchPopulated", {
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
         resolve(data as GetNewGLJrnDtlMnlDEASchPopulated_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaultAccount
   Description: Gets default Deferred Expense GL account for a line.
   OperationID: GetDefaultAccount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDefaultAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultAccount(requestBody:GetDefaultAccount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDefaultAccount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetDefaultAccount", {
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
         resolve(data as GetDefaultAccount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ResetMYIndustryCode
   Description: Resets MY Industry Code when Tax Line or Reporting Module is adjusted
   OperationID: ResetMYIndustryCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ResetMYIndustryCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetMYIndustryCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ResetMYIndustryCode(requestBody:ResetMYIndustryCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ResetMYIndustryCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/ResetMYIndustryCode", {
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
         resolve(data as ResetMYIndustryCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTaxableLinesListWithParams
   Description: Gets TaxableLinesList from current GL Journal
   OperationID: GetTaxableLinesListWithParams
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTaxableLinesListWithParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxableLinesListWithParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTaxableLinesListWithParams(requestBody:GetTaxableLinesListWithParams_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTaxableLinesListWithParams_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetTaxableLinesListWithParams", {
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
         resolve(data as GetTaxableLinesListWithParams_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTaxaHandlingList
   Description: Get list of available Tax Handling values.
   OperationID: GetTaxaHandlingList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTaxaHandlingList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxaHandlingList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTaxaHandlingList(requestBody:GetTaxaHandlingList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTaxaHandlingList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetTaxaHandlingList", {
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
         resolve(data as GetTaxaHandlingList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGLJrnHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLJrnHed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLJrnHed(requestBody:GetNewGLJrnHed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGLJrnHed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetNewGLJrnHed", {
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
         resolve(data as GetNewGLJrnHed_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGLJrnHedAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLJrnHedAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnHedAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnHedAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLJrnHedAttch(requestBody:GetNewGLJrnHedAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGLJrnHedAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetNewGLJrnHedAttch", {
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
         resolve(data as GetNewGLJrnHedAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGLJrnDtlMnl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLJrnDtlMnl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnDtlMnl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnDtlMnl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLJrnDtlMnl(requestBody:GetNewGLJrnDtlMnl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGLJrnDtlMnl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetNewGLJrnDtlMnl", {
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
         resolve(data as GetNewGLJrnDtlMnl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGLJrnDtlMnlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLJrnDtlMnlAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnDtlMnlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnDtlMnlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLJrnDtlMnlAttch(requestBody:GetNewGLJrnDtlMnlAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGLJrnDtlMnlAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetNewGLJrnDtlMnlAttch", {
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
         resolve(data as GetNewGLJrnDtlMnlAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGLJrnDtlMnlDEASch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLJrnDtlMnlDEASch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnDtlMnlDEASch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnDtlMnlDEASch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLJrnDtlMnlDEASch(requestBody:GetNewGLJrnDtlMnlDEASch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGLJrnDtlMnlDEASch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetNewGLJrnDtlMnlDEASch", {
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
         resolve(data as GetNewGLJrnDtlMnlDEASch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGLJrnDtlMnlTranGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLJrnDtlMnlTranGLC
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnDtlMnlTranGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnDtlMnlTranGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLJrnDtlMnlTranGLC(requestBody:GetNewGLJrnDtlMnlTranGLC_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGLJrnDtlMnlTranGLC_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetNewGLJrnDtlMnlTranGLC", {
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
         resolve(data as GetNewGLJrnDtlMnlTranGLC_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLJrnDtlMnlAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlDEASchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLJrnDtlMnlDEASchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLJrnDtlMnlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlTranGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLJrnDtlMnlTranGLCRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnHedAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLJrnHedAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnHedListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLJrnHedListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnHedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLJrnHedRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlAllocationsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GlAllocationsRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumGenOptsRow,
}

export interface Erp_Tablesets_GLJrnDtlMnlAttchRow{
   "Company":string,
   "BookID":string,
   "FiscalYear":number,
   "FiscalYearSuffix":string,
   "JournalCode":string,
   "JournalNum":number,
   "JournalLine":number,
   "FiscalCalendarID":string,
   "DrawingSeq":number,
   "XFileRefNum":number,
   "SysRevID":number,
   "SysRowID":string,
   "ForeignSysRowID":string,
   "DrawDesc":string,
   "FileName":string,
   "PDMDocID":string,
   "DocTypeID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLJrnDtlMnlDEASchRow{
      /**  Company  */  
   "Company":string,
      /**  FiscalCalendarID  */  
   "FiscalCalendarID":string,
      /**  FiscalYear  */  
   "FiscalYear":number,
      /**  FiscalYearSuffix  */  
   "FiscalYearSuffix":string,
      /**  BookID  */  
   "BookID":string,
      /**  JournalCode  */  
   "JournalCode":string,
      /**  JournalNum  */  
   "JournalNum":number,
      /**  JournalLine  */  
   "JournalLine":number,
      /**  AmortSeq  */  
   "AmortSeq":number,
      /**  SchFiscalCalendarID  */  
   "SchFiscalCalendarID":string,
      /**  SchFiscalYear  */  
   "SchFiscalYear":number,
      /**  SchFiscalYearSuffix  */  
   "SchFiscalYearSuffix":string,
      /**  SchFiscalPeriod  */  
   "SchFiscalPeriod":number,
      /**  AmortDate  */  
   "AmortDate":string,
      /**  AmortPercent  */  
   "AmortPercent":number,
      /**  AmortAmt  */  
   "AmortAmt":number,
      /**  DocAmortAmt  */  
   "DocAmortAmt":number,
      /**  Posted  */  
   "Posted":boolean,
      /**  PostedDate  */  
   "PostedDate":string,
      /**  TranDocTypeID  */  
   "TranDocTypeID":string,
      /**  LegalNumber  */  
   "LegalNumber":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Rpt1AmortAmt  */  
   "Rpt1AmortAmt":number,
   "GroupID":string,
      /**  Document currency  */  
   "CurrencyCode":string,
      /**  Rpt2AmortAmt  */  
   "Rpt2AmortAmt":number,
      /**  Rpt3AmortAmt  */  
   "Rpt3AmortAmt":number,
      /**  Used for Tracker only for records from GLJournalEntry. BookID in GLJrnDtl. The same as BookID field value for Single-book mode.  */  
   "GLBookID":string,
      /**  Used for Tracker only for records from GLJournalEntry. Journal Number in GLJrnDtl. The same as JournalNum field value for Single-book mode.  */  
   "GLJournalNum":number,
      /**  DispAmortAmt  */  
   "DispAmortAmt":number,
      /**  DispDocAmortAmt  */  
   "DispDocAmortAmt":number,
      /**  Indicates if this recognized Deferred Expense Amortization transaction has reverse lines  */  
   "HasReverseLines":boolean,
      /**  Account Currency  */  
   "CurrencyCodeAcct":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLJrnDtlMnlRow{
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
      /**  Company Identifier.  */  
   "Company":string,
      /**  Fiscal year that entry applies to.  */  
   "FiscalYear":number,
      /**  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  */  
   "JournalNum":number,
      /**  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  */  
   "JournalLine":number,
      /**  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  */  
   "Description":string,
      /**  Date for this journal transaction entry.  */  
   "JEDate":string,
      /**  Fiscal period that this journal entry applies to.  */  
   "FiscalPeriod":number,
      /**  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   "GroupID":string,
      /**  Transaction amount.  */  
   "TransAmt":number,
      /**  User ID that posted this translation.  */  
   "PostedBy":string,
      /**  Date that this transaction was posted to the G/L files.  */  
   "PostedDate":string,
      /**  Indicates if this entry has been posted to the G/L master balance files. Unposted entries are excluded from all G/L reports.  */  
   "Posted":boolean,
      /**   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  */  
   "SourceModule":string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   "VendorNum":number,
      /**  Vendor's invoice number.  */  
   "APInvoiceNum":string,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   "JournalCode":string,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   "ARInvoiceNum":number,
      /**  BankAcctId of the BankAcct master that this check was drawn  against.  */  
   "BankAcctID":string,
      /**  Check number.  */  
   "CheckNum":number,
      /**  Cash Receipts reference field.  */  
   "CRHeadNum":number,
      /**  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  */  
   "Reverse":boolean,
      /**  Bank Transaction Number.  Used when a transaction is a direct transfer from one bank account to another.  */  
   "BankTranNum":number,
      /**   The identifier of the Bank Slip document (bank statement).  The user enters a bank slip during the reconciliation process.  This is then written into the related GLJrnDtl records.
Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  */  
   "BankSlip":string,
      /**  Link to the related GLRefTyp.RefType.  */  
   "RefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "RefCode":string,
      /**  Flag that indicate if the account is a curency account  */  
   "CurrAcct":boolean,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  identifies the currency for the Currency Account.  */  
   "CurrencyCodeAcct":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Multi-Company G/L Reference Type from the external company.  This is used by the Multi-Company Journal.  */  
   "ExtRefType":string,
      /**  Multi-Company G/L Reference Code from the external company.  This is used by the Multi-Company Journal.  */  
   "ExtRefCode":string,
      /**  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  */  
   "GlbJournalNum":number,
      /**  The Journal Line assigned at the destination or target company when this Multi-Company Journal is created.  */  
   "GlbJournalLine":number,
      /**  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  */  
   "GlbJournalCode":string,
      /**  Global Vendor number.  Used by Multi-Company Journal.  */  
   "GlbVendorNum":number,
      /**  Global AP Invoice identifier.  Used by Multi-Company Journal.  */  
   "GlbAPInvoiceNum":string,
      /**  Flag to indicate that a separate journal entry will be created at the target company for the Multi-Company G/L Account entered in this journal line.  */  
   "MultiCompany":boolean,
      /**  Linked to a Multi-Company Journal.  */  
   "Linked":boolean,
      /**  Extended text to describe the journal line entry.  Defaults from GLJrnHed.CommentText.  */  
   "CommentText":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "GlbCompanyID":string,
      /**  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  */  
   "GlbFiscalYear":number,
      /**  Fiscal period from the external company that this journal entry applies to.  */  
   "GlbFiscalPeriod":number,
      /**  The data entry Group from the external company that the journal entry is assigned to.  */  
   "GlbGroupID":string,
      /**  External Segment Value 1  */  
   "ExtSegValue1":string,
      /**  External Segment Value 2  */  
   "ExtSegValue2":string,
      /**  External Segment Value 3  */  
   "ExtSegValue3":string,
      /**  External Segment Value 4  */  
   "ExtSegValue4":string,
      /**  External Segment Value 5  */  
   "ExtSegValue5":string,
      /**  External Segment Value 6  */  
   "ExtSegValue6":string,
      /**  External Segment Value 7  */  
   "ExtSegValue7":string,
      /**  External Segment Value 8  */  
   "ExtSegValue8":string,
      /**  External Segment Value 9  */  
   "ExtSegValue9":string,
      /**  External Segment Value 10  */  
   "ExtSegValue10":string,
      /**  External Segment Value 11  */  
   "ExtSegValue11":string,
      /**  External Segment Value 12  */  
   "ExtSegValue12":string,
      /**  External Segment Value 13  */  
   "ExtSegValue13":string,
      /**  External Segment Value 14  */  
   "ExtSegValue14":string,
      /**  External Segment Value 15  */  
   "ExtSegValue15":string,
      /**  External Segment Value 16  */  
   "ExtSegValue16":string,
      /**  External Segment Value 17  */  
   "ExtSegValue17":string,
      /**  External Segment Value 18  */  
   "ExtSegValue18":string,
      /**  External Segment Value 19  */  
   "ExtSegValue19":string,
      /**  External Segment Value 20  */  
   "ExtSegValue20":string,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Date record was created  */  
   "CreateDate":string,
      /**  Transaction amount in document currency.  */  
   "DocTransAmt":number,
      /**  A unique code that identifies the document currency.  */  
   "CurrencyCode":string,
      /**  Legal Number of source document  */  
   "LegalNumber":string,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   "PerBalFlag":boolean,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   "TBFlag":boolean,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   "DailyBalFlag":boolean,
      /**  if yes, the balance records are not updated for the GLJrnDtl even if the GL Account resolves to a valid GL Balance Account.  */  
   "SkipBalances":boolean,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Fiscal year suffix.  */  
   "GlbFiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "GlbFiscalCalendarID":string,
      /**  Identifies the journal entry as one processed by consolidation posting mode where the data transfer is immediate and an intermediate book is used.  */  
   "IntermediateProc":boolean,
      /**  Internal system calcualted sequence number not inteneded for external use.  */  
   "GenID":number,
      /**  Source Company Identifier.  Identifies the company where this GLJrnDtl originated from.  */  
   "SrcCompany":string,
      /**  Unique Book Identifier  This is the book that is being consolidated into a target book.  */  
   "SrcBook":string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   "SrcGLAccount":string,
      /**  Source Journal Code  */  
   "SrcJrnlCode":string,
      /**  Source Journal Number  */  
   "SrcJournalNum":number,
      /**  Source Journal Line  */  
   "SrcJournalLine":number,
      /**   P = derived from Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.  */  
   "SrcType":string,
      /**  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  */  
   "CloseFiscalPeriod":number,
      /**  Chart of Account ID  */  
   "ExtCOACode":string,
      /**  Full External GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the External GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   "ExtGLAccount":string,
      /**  This field shows Debit value of transaction  */  
   "DebitAmount":number,
      /**  This field shows Credit value of transaction  */  
   "CreditAmount":number,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
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
      /**  PaymentNumber  */  
   "PaymentNumber":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Possible values: 0`In~1`Out  */  
   "PartOfDual":string,
      /**  Tax Journal Line reporting module.  Possible values: 0`AP~1`AR  */  
   "ReportingModule":string,
      /**  Book Currency for Taxable Amount  */  
   "TaxableAmtBookCurr":string,
      /**  Transactional Currency for Taxable Amount  */  
   "TaxableAmtCurr":string,
      /**  Taxable Amount In Book Currency  */  
   "TaxableAmtInBookCurr":number,
      /**  Taxable Amount InTransactional Currency  */  
   "TaxableAmtInTranCurr":number,
      /**  Taxable Line. It is used for tax Jornal Line.  */  
   "TaxableLine":string,
      /**  Tax Liability. It is used for tax Jornal Line.  */  
   "TaxLiability":string,
      /**  Inducate that it is Tax Journal Line  */  
   "TaxLine":boolean,
      /**  Tax Percent. It is used for tax Jornal Line.  */  
   "TaxPercent":number,
      /**  Tax Point Date. It is used for tax Jornal Line.  */  
   "TaxPointDate":string,
      /**  Tax Rate. It is used for tax Jornal Line.  */  
   "TaxRate":string,
      /**  Tax Type. It is used for tax Jornal Line.  */  
   "TaxType":string,
      /**  OverrideGLAcct  */  
   "OverrideGLAcct":boolean,
      /**  OneTimeID  */  
   "COOneTimeID":string,
      /**  DeferredExp  */  
   "DeferredExp":boolean,
      /**  DEACode  */  
   "DEACode":string,
      /**  DEAStartDate  */  
   "DEAStartDate":string,
      /**  DEAEndDate  */  
   "DEAEndDate":string,
      /**  MovementNum  */  
   "MovementNum":number,
      /**  Malaysia Industry Code  */  
   "MYIndustryCode":string,
      /**  The Internal CustNum that ties back to the Customer master file.  */  
   "CustNum":number,
      /**  GL Journal Line Reference Type  */  
   "LineReferenceType":string,
      /**  SourcePlant  */  
   "SourcePlant":string,
      /**  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  */  
   "ExtSysType":string,
      /**  URL for drill back to an integrated external system  */  
   "ExtSysURL":string,
      /**  Colombia Loc Field.  */  
   "COLTaxTranType":string,
   "CurrencyCodeAcctList":string,
      /**  Is Deferred Expense Amortization Scheduled  */  
   "DEAScheduled":boolean,
      /**  DEA Distributed Amount  */  
   "Distributed":number,
      /**  DEA Distributed Amount in Doc Currency  */  
   "DocDistributed":number,
      /**  DEA Expense Amount in Doc Currency  */  
   "DocExpense":number,
      /**  DEA Recognized Amount in Doc Currency  */  
   "DocRecognized":number,
      /**  DEA Remaining Amount in Doc Currency  */  
   "DocRemaining":number,
      /**  DEA Unrecognized Amount in Doc Currency  */  
   "DocUnrecognized":number,
      /**  Display Fiscal Period  */  
   "DspFiscalPeriod":number,
      /**  Flag to indicate if the MultiCompany check box needs to be enabled.  */  
   "EnableMultiCompany":boolean,
      /**  DEA Expense Amount  */  
   "Expense":number,
   "ExtRefAcctChart":string,
   "ExtRefAcctDept":string,
   "ExtRefAcctDiv":string,
   "ExtRefCodeStatus":string,
   "GlbGLAccountDesc":string,
      /**  Flag: true - control In/Out is enabled, else disabled  */  
   "PartOfDualEnabled":boolean,
      /**  Colombia Loc Field.  */  
   "RateCode":string,
      /**  Colombia Loc Field.  */  
   "RateDescription":string,
      /**  DEA Recognized Amount  */  
   "Recognized":number,
   "RefAcctChart":string,
   "RefAcctDept":string,
   "RefAcctDiv":string,
   "RefCodeStatus":string,
      /**  DEA Remaining Amount  */  
   "Remaining":number,
      /**  Statistical Amount. UI display value.  */  
   "StatAmount":number,
      /**  Colombia Loc Field.  */  
   "TaxableAmt":number,
      /**  Used for Colombia CSF  */  
   "TaxCode":string,
   "TaxLiabilityDescr":string,
      /**  The list of tax codes for Tax Liability  */  
   "TaxLiabilityTaxCodes":string,
   "TaxRateDescr":string,
   "TaxTypeDescr":string,
      /**  The list of tax rates for Tax code  */  
   "TaxTypeTaxRates":string,
   "TotCredit":number,
   "TotCurrCredit":number,
   "TotCurrDebit":number,
   "TotDebit":number,
      /**  DEA Unrecognized Amount  */  
   "Unrecognized":number,
      /**  Colombia Loc Field.  */  
   "COIsTaxLn":boolean,
      /**  GL Journal Line Reference Holder.  */  
   "LineReferenceHolder":string,
      /**  GL Journal Line Reference Holder Name.  */  
   "LineReferenceHolderName":string,
      /**  GL Journal Line Reference.  */  
   "LineReference":string,
      /**  Source GL Journal Line to copy reference data.  */  
   "RefSourceJrnLine":string,
      /**  Result of account validation. False if account is valid.  */  
   "InvalidGLAccount":boolean,
      /**  Result of account validation. Empty if account is valid.  */  
   "InvalidGLAccountMessage":string,
      /**  Result of external account validation. False if account is valid.  */  
   "InvalidExtGLAccount":boolean,
      /**  Result of external account validation. Empty if account is valid.  */  
   "InvalidExtGLAccountMessage":string,
      /**  Calculated field for correspondence accounting journals. Determines if the current line an odd one.  */  
   "CorrAcctOddLine":boolean,
   "BitFlag":number,
   "AcctCurrCurrencyID":string,
   "AcctCurrCurrSymbol":string,
   "AcctCurrCurrDesc":string,
   "AcctCurrCurrName":string,
   "AcctCurrDocumentDesc":string,
   "BankAcctIDDescription":string,
   "BankAcctIDBankName":string,
   "CurrencyCurrName":string,
   "CurrencyCurrDesc":string,
   "CurrencyDocumentDesc":string,
   "CurrencyCurrSymbol":string,
   "CurrencyCurrencyID":string,
   "CustNumCustID":string,
   "CustNumName":string,
   "CustNumBTName":string,
   "DEACodeDescRADesc":string,
   "ExtRefCodeRefCodeDesc":string,
   "GLGLAcctDisp":string,
   "GLGLShortAcct":string,
   "GLAccountDesc":string,
   "GlRefCodeDescRefCodeDesc":string,
   "JournalCodeJrnlDescription":string,
   "StatUOMStatUOMDesc":string,
   "VendorNumCurrencyCode":string,
   "VendorNumCountry":string,
   "VendorNumAddress2":string,
   "VendorNumAddress1":string,
   "VendorNumVendorID":string,
   "VendorNumTermsCode":string,
   "VendorNumDefaultFOB":string,
   "VendorNumAddress3":string,
   "VendorNumName":string,
   "VendorNumState":string,
   "VendorNumZIP":string,
   "VendorNumCity":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLJrnDtlMnlTranGLCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  */  
   "Key2":string,
      /**  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  */  
   "Key3":string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key4":string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key5":string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key6":string,
      /**  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  */  
   "TGLCTranNum":number,
      /**  String identifier of the account context.  */  
   "GLAcctContext":string,
      /**  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  */  
   "BookID":string,
      /**  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  */  
   "COACode":string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   "GLAccount":string,
      /**  Indicates if the user can update or delete this record.  */  
   "UserCanModify":boolean,
      /**  Segement Value 1 of the account for this context.  */  
   "SegValue1":string,
      /**  Segement Value 2 of the account for this context.  */  
   "SegValue2":string,
      /**  Segement Value 3 of the account for this context.  */  
   "SegValue3":string,
      /**  Segement Value 4 of the account for this context.  */  
   "SegValue4":string,
      /**  Segement Value 5 of the account for this context.  */  
   "SegValue5":string,
      /**  Segement Value 6 of the account for this context.  */  
   "SegValue6":string,
      /**  Segement Value 7 of the account for this context.  */  
   "SegValue7":string,
      /**  Segement Value 8 of the account for this context.  */  
   "SegValue8":string,
      /**  Segement Value 9 of the account for this context.  */  
   "SegValue9":string,
      /**  Segement Value 10 of the account for this context.  */  
   "SegValue10":string,
      /**  Segement Value 11 of the account for this context.  */  
   "SegValue11":string,
      /**  Segement Value 12 of the account for this context.  */  
   "SegValue12":string,
      /**  Segement Value 13 of the account for this context.  */  
   "SegValue13":string,
      /**  Segement Value 14 of the account for this context.  */  
   "SegValue14":string,
      /**  Segement Value 15 of the account for this context.  */  
   "SegValue15":string,
      /**  Segement Value 16 of the account for this context.  */  
   "SegValue16":string,
      /**  Segement Value 17 of the account for this context.  */  
   "SegValue17":string,
      /**  Segement Value 18 of the account for this context.  */  
   "SegValue18":string,
      /**  Segement Value 19 of the account for this context.  */  
   "SegValue19":string,
      /**  Segement Value 20 of the account for this context.  */  
   "SegValue20":string,
      /**  Unique Identifier of the system GL Control Type.  */  
   "SysGLControlType":string,
      /**  System generated GL Control Identifier.  */  
   "SysGLControlCode":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   "IsExternalCompany":boolean,
      /**  Fiscal year of the related GLJrnDtl.  */  
   "FiscalYear":number,
      /**  JournalCode of the related GLJrnDtl.  */  
   "JournalCode":string,
      /**  Journal number of the related GLJrnDtl.  */  
   "JournalNum":number,
      /**  JournalLine of the related GLJrnDtl.  */  
   "JournalLine":number,
      /**  Transaction date of the transaction.  This is used in order to display the transactions in date order.  */  
   "TranDate":string,
      /**   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  */  
   "TranSource":string,
      /**  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  */  
   "LaborHedSeq":number,
      /**  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  */  
   "LaborDtlSeq":number,
      /**  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "SysDate":string,
      /**  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "SysTime":number,
      /**  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "TranNum":number,
      /**  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  */  
   "ARInvoiceNum":number,
      /**  Transaction amount that this transaction posted to the related GlJrnDtl.  */  
   "TransAmt":number,
      /**  Invoice Line Number associated with this GL Journal  */  
   "InvoiceLine":number,
      /**  The sequence number associated with this GL journal  */  
   "SeqNum":number,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   "VendorNum":number,
      /**  Vendor's invoice number.  */  
   "APInvoiceNum":string,
      /**  Date record was created  */  
   "CreateDate":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Credit Amount.  */  
   "CreditAmount":number,
      /**  Debit Amount.  */  
   "DebitAmount":number,
      /**  BookCreditAmount  */  
   "BookCreditAmount":number,
      /**  Book Debit Amount  */  
   "BookDebitAmount":number,
      /**  A unique code that identifies the document currency.  */  
   "CurrencyCode":string,
      /**   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  */  
   "RecordType":string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   "CorrAccUID":number,
      /**  this field equals ABTUID which was created during posting  */  
   "ABTUID":string,
      /**  Technical identifier.  */  
   "RuleUID":number,
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
      /**  IsModifiedByUser  */  
   "IsModifiedByUser":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MovementNum  */  
   "MovementNum":number,
      /**  MovementType  */  
   "MovementType":string,
      /**  Plant  */  
   "Plant":string,
   "GroupID":string,
   "BookMode":string,
   "BitFlag":number,
   "GLAccountGLAcctDisp":string,
   "GLAccountGLShortAcct":string,
   "GLAccountAccountDesc":string,
   "GLBookDescription":string,
   "GLBookCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLJrnHedAttchRow{
   "Company":string,
   "BookID":string,
   "FiscalYear":number,
   "FiscalYearSuffix":string,
   "JournalCode":string,
   "JournalNum":number,
   "FiscalCalendarID":string,
   "DrawingSeq":number,
   "XFileRefNum":number,
   "SysRevID":number,
   "SysRowID":string,
   "ForeignSysRowID":string,
   "DrawDesc":string,
   "FileName":string,
   "PDMDocID":string,
   "DocTypeID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLJrnHedListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The fiscal year for this journal transaction header. Assigned from GLJrnGrp.FiscalYear.  */  
   "FiscalYear":number,
      /**  Fiscal period that this journal entry applies to.  */  
   "FiscalPeriod":number,
      /**  Number that is assigned by the system.  The Journal Number is a way of relating the detail entries into a group that would normally balance.  When we need to assign a new number the system  finds the journalnum of the last record (GLJrnDtl) for the fiscal year and adds one.  When creating GLJrnDtl from other modules this number is assigned note that this find last is performed on the GLJrnDtl because the GLJrnHed records only exist until the group is posted.  */  
   "JournalNum":number,
      /**  Describes the journal transaction.  Used as a default for the GLJrnDtl.Description field.  */  
   "Description":string,
      /**  The Date for this journal transaction entry.  Defaulted from GLJrnGrp.JEDate.  Can be overridden during entry, but it must be a valid date for the fiscal period that is assigned to this group.  */  
   "JEDate":string,
      /**  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   "GroupID":string,
      /**  The Total Debits.  A summary of the positive GLJrnDtl.TranAmt in the related GLJrnDtl records.  Primarily used for visual verification.  */  
   "TotDebit":number,
      /**  The Total Credit.  A summary of negative GLJrnDtl.TranAmt in the related GLJrnDtl records.  Primarily used for visual verification.  */  
   "TotCredit":number,
      /**  Indicates that this is a non-balancing journal entry that the user indicated is valid to post.  */  
   "Override":boolean,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  User ID that created the record.  */  
   "EnteredBy":string,
      /**  Indicates that this journal transaction set should create reversing entries for the next fiscal period.  This happens during the posting process.  */  
   "Reverse":boolean,
      /**  Default is the first date of the next period. A date entered in this fields should be greater than the journal?s apply date.  */  
   "ReverseDate":string,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   "JournalCode":string,
      /**  Flag to indicate that journal lines appearing under this journal header may have multi-company journals entered at the target external company.  */  
   "MultiCompany":boolean,
      /**  Extended text to describe the journal header.  Defaults to all GLJrnDtl.CommentText.  */  
   "CommentText":string,
      /**  Date that this transaction was posted from the external company to the G/L files.  */  
   "GlbPostedDate":string,
      /**  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  */  
   "GlbJournalNum":number,
      /**  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  */  
   "GlbJournalCode":string,
      /**  Global Vendor number.  Used by Multi-Company Journal.  */  
   "GlbVendorNum":number,
      /**  Global AP Invoice identifier.  Used by Multi-Company Journal.  */  
   "GlbAPInvoiceNum":string,
      /**  Global Vendor ID.  Used by Multi-Company Journal.  */  
   "GlbVendorID":string,
      /**  Global Vendor Name.  Used by the Multi-Company Journal.  */  
   "GlbVendorName":string,
      /**  Legal Number used by the source AP Invoice.  Used by the Multi-Company Journal.  */  
   "GlbAPLegalNumber":string,
      /**  Global AP Invoice description.  Used by Multi-Company Journal.  */  
   "GlbAPInvDesc":string,
      /**  Linked to a Multi-Company Journal.  */  
   "Linked":boolean,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "GlbCompanyID":string,
      /**  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  */  
   "GlbFiscalYear":number,
      /**  Fiscal period from the external company that this journal entry applies to.  */  
   "GlbFiscalPeriod":number,
      /**  The data entry Group from the external company that the journal entry is assigned to.  */  
   "GlbGroupID":string,
      /**  Global Journal Code Description.  */  
   "GlbJournalCodeDesc":string,
      /**  User ID that created the Multi-Company Journal record from the source company.  This may not be a valid UserId in the target company.  Used by the Multi-Company GJ and AP.  */  
   "GlbEnteredBy":string,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Date record was created  */  
   "CreateDate":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Fiscal year suffix.  */  
   "GlbFiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "GlbFiscalCalendarID":string,
      /**  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  */  
   "CloseFiscalPeriod":number,
      /**  if yes it means that during posting for each line debit and credit amounts should be saved with opposite signs.  */  
   "RedStorno":boolean,
      /**  It is true, if the record was posted.  */  
   "Posted":boolean,
      /**  Date when record was posted.  */  
   "PostedDate":string,
      /**  This field shows Debit statistical amount.  */  
   "DebitStatAmt":number,
      /**  0 - Manual Entry; 1 - Revaluation Process; 2 - Consolidation Process.  */  
   "ProcessType":number,
      /**  This field shows Credit statistical amount.  */  
   "CreditStatAmt":number,
      /**  Flag that indicates if correspondence accounting is set-up for the journal.  */  
   "CorrAccounting":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  TotDebit - TotCredit = Balance  */  
   "Balance":number,
      /**  Display total debit.  */  
   "DispTotDebit":number,
      /**  Display total credit.  */  
   "DispTotCredit":number,
      /**  Flag to indicate if the MultiCompany check box needs to be enabled.  */  
   "EnableMultiCompany":boolean,
      /**  Display Fiscal Period  */  
   "DspFiscalPeriod":number,
   "LegalNumMessage":string,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
   "AllowUnbalancedEntries":boolean,
      /**  Calendar description.  */  
   "FiscalCalDescription":string,
      /**  Journal  Description.  */  
   "JournalCodeJrnlDescription":string,
      /**  Description  */  
   "RateGrpCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLJrnHedRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The fiscal year for this journal transaction header. Assigned from GLJrnGrp.FiscalYear.  */  
   "FiscalYear":number,
      /**  Fiscal period that this journal entry applies to.  */  
   "FiscalPeriod":number,
      /**  Number that is assigned by the system.  The Journal Number is a way of relating the detail entries into a group that would normally balance.  When we need to assign a new number the system  finds the journalnum of the last record (GLJrnDtl) for the fiscal year and adds one.  When creating GLJrnDtl from other modules this number is assigned note that this find last is performed on the GLJrnDtl because the GLJrnHed records only exist until the group is posted.  */  
   "JournalNum":number,
      /**  Describes the journal transaction.  Used as a default for the GLJrnDtl.Description field.  */  
   "Description":string,
      /**  The Date for this journal transaction entry.  Defaulted from GLJrnGrp.JEDate.  Can be overridden during entry, but it must be a valid date for the fiscal period that is assigned to this group.  */  
   "JEDate":string,
      /**  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   "GroupID":string,
      /**  The Total Debits.  A summary of the positive GLJrnDtl.TranAmt in the related GLJrnDtl records.  Primarily used for visual verification.  */  
   "TotDebit":number,
      /**  The Total Credit.  A summary of negative GLJrnDtl.TranAmt in the related GLJrnDtl records.  Primarily used for visual verification.  */  
   "TotCredit":number,
      /**  Indicates that this is a non-balancing journal entry that the user indicated is valid to post.  */  
   "Override":boolean,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  User ID that created the record.  */  
   "EnteredBy":string,
      /**  Indicates that this journal transaction set should create reversing entries for the next fiscal period.  This happens during the posting process.  */  
   "Reverse":boolean,
      /**  Default is the first date of the next period. A date entered in this fields should be greater than the journal?s apply date.  */  
   "ReverseDate":string,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   "JournalCode":string,
      /**  Flag to indicate that journal lines appearing under this journal header may have multi-company journals entered at the target external company.  */  
   "MultiCompany":boolean,
      /**  Extended text to describe the journal header.  Defaults to all GLJrnDtl.CommentText.  */  
   "CommentText":string,
      /**  Date that this transaction was posted from the external company to the G/L files.  */  
   "GlbPostedDate":string,
      /**  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  */  
   "GlbJournalNum":number,
      /**  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  */  
   "GlbJournalCode":string,
      /**  Global Vendor number.  Used by Multi-Company Journal.  */  
   "GlbVendorNum":number,
      /**  Global AP Invoice identifier.  Used by Multi-Company Journal.  */  
   "GlbAPInvoiceNum":string,
      /**  Global Vendor ID.  Used by Multi-Company Journal.  */  
   "GlbVendorID":string,
      /**  Global Vendor Name.  Used by the Multi-Company Journal.  */  
   "GlbVendorName":string,
      /**  Legal Number used by the source AP Invoice.  Used by the Multi-Company Journal.  */  
   "GlbAPLegalNumber":string,
      /**  Global AP Invoice description.  Used by Multi-Company Journal.  */  
   "GlbAPInvDesc":string,
      /**  Linked to a Multi-Company Journal.  */  
   "Linked":boolean,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "GlbCompanyID":string,
      /**  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  */  
   "GlbFiscalYear":number,
      /**  Fiscal period from the external company that this journal entry applies to.  */  
   "GlbFiscalPeriod":number,
      /**  The data entry Group from the external company that the journal entry is assigned to.  */  
   "GlbGroupID":string,
      /**  Global Journal Code Description.  */  
   "GlbJournalCodeDesc":string,
      /**  User ID that created the Multi-Company Journal record from the source company.  This may not be a valid UserId in the target company.  Used by the Multi-Company GJ and AP.  */  
   "GlbEnteredBy":string,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Date record was created  */  
   "CreateDate":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Fiscal year suffix.  */  
   "GlbFiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "GlbFiscalCalendarID":string,
      /**  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  */  
   "CloseFiscalPeriod":number,
      /**  if yes it means that during posting for each line debit and credit amounts should be saved with opposite signs.  */  
   "RedStorno":boolean,
      /**  It is true, if the record was posted.  */  
   "Posted":boolean,
      /**  Date when record was posted.  */  
   "PostedDate":string,
      /**  This field shows Debit statistical amount.  */  
   "DebitStatAmt":number,
      /**  0 - Manual Entry; 1 - Revaluation Process; 2 - Consolidation Process.  */  
   "ProcessType":number,
      /**  This field shows Credit statistical amount.  */  
   "CreditStatAmt":number,
      /**  Flag that indicates if correspondence accounting is set-up for the journal.  */  
   "CorrAccounting":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Tax Handling: 0 - No Tax; 1 - Journal Includes Taxes; 2 - Tax adlustment Journal  */  
   "TaxHandling":string,
      /**  Transaction Document Type for the record.  */  
   "TranDocTypeID":string,
      /**  Indicate, that this Journal can have only lines with Statistical Accounts. Legal Number creation for Statistical Journals should be skipped.  */  
   "Statistical":boolean,
      /**  TransferredToParent  */  
   "TransferredToParent":boolean,
      /**  TransferredDate  */  
   "TransferredDate":string,
      /**  TransferredPerson  */  
   "TransferredPerson":string,
      /**  MXFiscalFolio  */  
   "MXFiscalFolio":string,
      /**  MXRFC  */  
   "MXRFC":string,
      /**  If box is checked, this journal has been marked as on hold.  */  
   "JournalHeld":boolean,
      /**  SourcePlant  */  
   "SourcePlant":string,
      /**  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  */  
   "ExtSysType":string,
      /**  URL for drill back to an integrated external system  */  
   "ExtSysURL":string,
   "AllowChgAfterPrint":boolean,
      /**  Display total credit.  */  
   "DispTotCredit":number,
      /**  Display total debit.  */  
   "DispTotDebit":number,
      /**  Display Fiscal Period  */  
   "DspFiscalPeriod":number,
   "EnableAssignLegNum":boolean,
   "EnableCorrAccounting":boolean,
      /**  Flag to indicate if the MultiCompany check box needs to be enabled.  */  
   "EnableMultiCompany":boolean,
   "EnableTranDocType":boolean,
   "EnableVoidLegNum":boolean,
   "HasLegNumCnfg":boolean,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
   "LegalNumMessage":string,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
      /**  Used by UI to determine if the Red Storno checkbox is to be enabled.  */  
   "RedStornoOpt":string,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
      /**  The system transaction type - ARInvoice or CreditMemo.  Used to filter combo list for TranDocTypeID.  */  
   "SystemTranType":string,
   "AllowUnbalancedEntries":boolean,
      /**  TotDebit - TotCredit = Balance  */  
   "Balance":number,
   "CompanyTaxEntryMode":string,
      /**  Field used for Colombia CSF  */  
   "COOneTimeDtl":boolean,
      /**  Defines site entry allowed on journal  */  
   "AllowSiteEntry":boolean,
   "BitFlag":number,
   "CurrencyCurrName":string,
   "CurrencyCurrDesc":string,
   "CurrencyDocumentDesc":string,
   "CurrencyCurrencyID":string,
   "CurrencyCurrSymbol":string,
   "FiscalCalDescription":string,
   "JournalCodeJrnlDescription":string,
   "RateGrpCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GlAllocationsRow{
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   "GLAccount":string,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   "SegValue1":string,
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
      /**  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   "SegValue2":string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   "SegValue20":string,
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
   "AccountDesc":string,
   "BookID":string,
   "AllocID":string,
   "Amount":number,
   "Company":string,
   "Description":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LegalNumGenOptsRow{
   "Company":string,
   "LegalNumberID":string,
   "TransYear":number,
   "TransYearSuffix":string,
   "DspTransYear":string,
      /**  Indicates if DspTransYear should be displayed when prompting for a manual number.  */  
   "ShowDspTransYear":boolean,
   "Prefix":string,
      /**  The list of prefixes that can be selected by the user for manual numbers.  */  
   "PrefixList":string,
      /**  The suffix portion of the legal number.  */  
   "NumberSuffix":string,
      /**  Indicates if the prefix can be entered by the user.  */  
   "EnablePrefix":boolean,
      /**  Indicates if the suffix (number) can be entered by the user.  */  
   "EnableSuffix":boolean,
   "NumberOption":string,
   "DocumentDate":string,
   "GenerationType":string,
   "Description":string,
   "TransPeriod":number,
      /**  Prefix for the period  */  
   "PeriodPrefix":string,
   "ShowTransPeriod":boolean,
      /**  Used when the full legal number is entered  */  
   "LegalNumber":string,
   "TranDocTypeID":string,
   "TranDocTypeID2":string,
   "GenerationOption":string,
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
      @param GroupID
      @param JournalNum
      @param JournalLine
      @param ds
   */  
export interface AutoBalance_input{
      /**  The current group ID  */  
   GroupID:string,
      /**  The current Journal Number  */  
   JournalNum:number,
      /**  The current Journal Line  */  
   JournalLine:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface AutoBalance_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param iLineNum
      @param ds
   */  
export interface AutoComplete_input{
      /**  Journal line number  */  
   iLineNum:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface AutoComplete_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param fiscalCalendarID
      @param fiscalYear
      @param fiscalYearSuffix
      @param bookID
      @param journalCode
      @param journalNum
      @param journalLine
      @param ds
   */  
export interface AutocompleteAmortizationSchedule_input{
   fiscalCalendarID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   bookID:string,
   journalCode:string,
   journalNum:number,
   journalLine:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface AutocompleteAmortizationSchedule_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param fiscalCalendarID
      @param fiscalYear
      @param fiscalYearSuffix
      @param bookID
      @param journalCode
      @param journalNum
      @param journalLine
      @param ds
   */  
export interface CalculateAmortizationTotals_input{
   fiscalCalendarID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   bookID:string,
   journalCode:string,
   journalNum:number,
   journalLine:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface CalculateAmortizationTotals_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param ds
      @param iLineNum
   */  
export interface CalculateAmountForTaxLineEx_input{
   ds:Erp_Tablesets_GLJournalEntryTableset[],
      /**  Line number.  */  
   iLineNum:number,
}

export interface CalculateAmountForTaxLineEx_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
   dAmountInBookCurr:number,
   dAmountInTranCurr:number,
}
}

   /** Required : 
      @param ProposedExtCompID
      @param iLineNum
      @param ds
   */  
export interface ChangeExtCompanyID_input{
      /**  The proposed External Company ID  */  
   ProposedExtCompID:string,
      /**  Journal line number  */  
   iLineNum:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface ChangeExtCompanyID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param iLineNum
      @param ds
   */  
export interface ChangeExtGlAcct_input{
      /**  Journal line number  */  
   iLineNum:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface ChangeExtGlAcct_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param iLineNum
      @param ds
   */  
export interface ChangeGlAcct1_input{
      /**  Journal line number  */  
   iLineNum:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface ChangeGlAcct1_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
   currCodeChanged:boolean,
}
}

   /** Required : 
      @param ProposedRefCode
      @param iLineNum
      @param ds
   */  
export interface ChangeGlRefCode_input{
      /**  The proposed G/L Reference Code  */  
   ProposedRefCode:string,
      /**  Journal line number  */  
   iLineNum:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface ChangeGlRefCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param iLineNum
      @param updateTaxableOnly
      @param ds
   */  
export interface ChangeLinkedLineAmnts_input{
      /**  Journal line number  */  
   iLineNum:number,
      /**  Indicates if only the taxable amount will be updated  */  
   updateTaxableOnly:boolean,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface ChangeLinkedLineAmnts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param ProposedMulti
      @param iLineNum
      @param ds
   */  
export interface ChangeMultiCompany_input{
      /**  The proposed Multi-Company flag  */  
   ProposedMulti:boolean,
      /**  Journal line number  */  
   iLineNum:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface ChangeMultiCompany_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param ProposedReverse
      @param ds
   */  
export interface ChangeReverse_input{
      /**  The proposed Reverse value  */  
   ProposedReverse:boolean,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface ChangeReverse_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param ipTaxCode
   */  
export interface ChangeTaxCode_input{
      /**  TaxCode id  */  
   ipTaxCode:string,
}

export interface ChangeTaxCode_output{
parameters : {
      /**  output parameters  */  
   opRateCode:string,
   opRateDescription:string,
}
}

   /** Required : 
      @param ipBookID
   */  
export interface CheckAllocations_input{
      /**  The current COACode  */  
   ipBookID:string,
}

export interface CheckAllocations_output{
parameters : {
      /**  output parameters  */  
   opAlloc:boolean,
}
}

   /** Required : 
      @param ipCOACode
      @param ipSegValue
      @param ipCurrency
   */  
export interface CheckCurrencyAccount2_input{
      /**  COA code  */  
   ipCOACode:string,
      /**  Segment value  */  
   ipSegValue:string,
      /**  Transactional currency  */  
   ipCurrency:string,
}

export interface CheckCurrencyAccount2_output{
parameters : {
      /**  output parameters  */  
   opCurrAcct:boolean,
}
}

   /** Required : 
      @param ds
      @param iLineNum
   */  
export interface CheckCurrencyAccountExt_input{
   ds:Erp_Tablesets_GLJournalEntryTableset[],
      /**  lineNum  */  
   iLineNum:number,
}

export interface CheckCurrencyAccountExt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param ipBookID
      @param ipJournalCode
      @param ipFiscalYear
      @param ipFiscalYearSuffix
      @param ipFiscalCalendarID
      @param ipJournalNum
      @param ipCurrCode
      @param ipTaxableLine
      @param ipCOACode
      @param ipSegValue
      @param ipPublishEx
      @param ipGLAccount
   */  
export interface CheckCurrencyAccountForTaxLine_input{
      /**  Book ID  */  
   ipBookID:string,
      /**  Journal code  */  
   ipJournalCode:string,
      /**  Fiscal year  */  
   ipFiscalYear:number,
      /**  Fiscal year suffix  */  
   ipFiscalYearSuffix:string,
      /**  Fiscal Calendar  */  
   ipFiscalCalendarID:string,
      /**  Journal number  */  
   ipJournalNum:number,
      /**  Book currency code  */  
   ipCurrCode:string,
      /**  Taxable line number  */  
   ipTaxableLine:string,
      /**  COA code  */  
   ipCOACode:string,
      /**  Segment value  */  
   ipSegValue:string,
      /**  True - raise exeption if error  */  
   ipPublishEx:boolean,
      /**  GL Account  */  
   ipGLAccount:string,
}

export interface CheckCurrencyAccountForTaxLine_output{
parameters : {
      /**  output parameters  */  
   opCurrAcct:boolean,
   opTranCurrCode:string,
   opTranCurrDescr:string,
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
      @param keyValue
      @param keyValue2
      @param keyValue3
      @param keyValue4
      @param keyValue5
   */  
export interface CheckDocumentIsLocked_input{
      /**  GroupID  */  
   keyValue:string,
      /**  BookID  */  
   keyValue2:string,
      /**  FiscalYear  */  
   keyValue3:string,
      /**  JournalCode  */  
   keyValue4:string,
      /**  JournalNum  */  
   keyValue5:string,
}

export interface CheckDocumentIsLocked_output{
}

   /** Required : 
      @param iLineNum
      @param ds
   */  
export interface CheckDtlBeforeUpdate_input{
      /**  Journal Line Number  */  
   iLineNum:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface CheckDtlBeforeUpdate_output{
parameters : {
      /**  output parameters  */  
   OpMessage:string,
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param cPartOfDual
   */  
export interface CheckPartOfDual_input{
      /**  In/Out value  */  
   cPartOfDual:string,
}

export interface CheckPartOfDual_output{
}

   /** Required : 
      @param cReportingModule
      @param ipTaxLiability
   */  
export interface CheckReportingModule_input{
      /**  Reporting Module value  */  
   cReportingModule:string,
      /**  Tax Liability code  */  
   ipTaxLiability:string,
}

export interface CheckReportingModule_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CheckStatUOMAccount_input{
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface CheckStatUOMAccount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param ipBookID
      @param ipJournalCode
      @param ipFiscalYear
      @param ipFiscalYearSuffix
      @param ipFiscalCalendarID
      @param ipJournalNum
      @param ipJournalLine
      @param ipTaxType
      @param ipTaxRate
      @param ipPartOfDual
      @param ipTaxableLine
      @param ipTaxableAmountStatus
      @param ipTaxAmountStatus
   */  
export interface CheckTaxAmountSign_input{
      /**  Book ID value  */  
   ipBookID:string,
      /**  Jornal code  */  
   ipJournalCode:string,
      /**  Fiscal year  */  
   ipFiscalYear:number,
      /**  Fiscal year suffix  */  
   ipFiscalYearSuffix:string,
      /**  Fiscal calendar ID  */  
   ipFiscalCalendarID:string,
      /**  Journal number  */  
   ipJournalNum:number,
      /**  Journal line number  */  
   ipJournalLine:number,
      /**  Tax code  */  
   ipTaxType:string,
      /**  Tax rate code  */  
   ipTaxRate:string,
      /**  In/Out value  */  
   ipPartOfDual:string,
      /**  Taxable line number  */  
   ipTaxableLine:string,
      /**  Taxable amount status: -1(credit)/ 1(debit)/ 0(not calculated)  */  
   ipTaxableAmountStatus:number,
      /**  Tax amount status: -1(credit)/ 1(debit)/ 0(not calculated)  */  
   ipTaxAmountStatus:number,
}

export interface CheckTaxAmountSign_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param cTaxLiabilityCode
   */  
export interface CheckTaxLiability_input{
      /**  Tax Liability code  */  
   cTaxLiabilityCode:string,
}

export interface CheckTaxLiability_output{
}

   /** Required : 
      @param cTaxTypeCode
      @param cTaxRateCode
      @param dTaxPointDate
   */  
export interface CheckTaxPointDate_input{
      /**  Tax Type code  */  
   cTaxTypeCode:string,
      /**  Tax Rate code  */  
   cTaxRateCode:string,
      /**  Tax point date  */  
   dTaxPointDate:string,
}

export interface CheckTaxPointDate_output{
parameters : {
      /**  output parameters  */  
   cMessage:string,
}
}

   /** Required : 
      @param cTaxTypeCode
      @param cTaxRateCode
      @param dTaxPointDate
   */  
export interface CheckTaxRate_input{
      /**  Tax Type code  */  
   cTaxTypeCode:string,
      /**  ax Rate code  */  
   cTaxRateCode:string,
      /**  Tax point date  */  
   dTaxPointDate:string,
}

export interface CheckTaxRate_output{
}

   /** Required : 
      @param cTaxLiabilityCode
      @param cTaxTypeCode
   */  
export interface CheckTaxType_input{
      /**  Tax Liability code  */  
   cTaxLiabilityCode:string,
      /**  Tax Type code  */  
   cTaxTypeCode:string,
}

export interface CheckTaxType_output{
parameters : {
      /**  output parameters  */  
   cMessage:string,
}
}

   /** Required : 
      @param ipBookID
      @param ipJournalCode
      @param ipFiscalYear
      @param ipFiscalYearSuffix
      @param ipFiscalCalendarID
      @param ipJournalNum
      @param ipJournalLine
      @param ipCurrCode
      @param ipTaxableLine
      @param ipCOACode
      @param ipSegValue
      @param ipGLAccount
      @param ipTaxType
      @param ipTaxRate
      @param ipPartOfDual
      @param ipTaxAmountStatus
   */  
export interface CheckTaxableLine_input{
      /**  Book ID value  */  
   ipBookID:string,
      /**  Jornal code  */  
   ipJournalCode:string,
      /**  Fiscal year  */  
   ipFiscalYear:number,
      /**  Fiscal year suffix  */  
   ipFiscalYearSuffix:string,
      /**  Fiscal calendar ID  */  
   ipFiscalCalendarID:string,
      /**  Journal number  */  
   ipJournalNum:number,
      /**  Journal line number  */  
   ipJournalLine:number,
      /**  Book currency code  */  
   ipCurrCode:string,
      /**  Taxable line number  */  
   ipTaxableLine:string,
      /**  COA code  */  
   ipCOACode:string,
      /**  Segment value  */  
   ipSegValue:string,
      /**  GL Account  */  
   ipGLAccount:string,
      /**  Tax code  */  
   ipTaxType:string,
      /**  Tax rate code  */  
   ipTaxRate:string,
      /**  In/Out value  */  
   ipPartOfDual:string,
      /**  Tax amount status: -1(credit)/ 1(debit)/ 0(not calculated)  */  
   ipTaxAmountStatus:number,
}

export interface CheckTaxableLine_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param proposedAmount
      @param iLineNum
      @param ds
   */  
export interface ConvertCreditAmount_input{
      /**  The proposed  Amount  */  
   proposedAmount:number,
      /**  Journal Line Number  */  
   iLineNum:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface ConvertCreditAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param proposedAmount
      @param iLineNum
      @param ds
   */  
export interface ConvertDebitAmount_input{
      /**  The proposed  Amount  */  
   proposedAmount:number,
      /**  Journal Line Number  */  
   iLineNum:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface ConvertDebitAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param ds
      @param journalNum
      @param groupID
      @param allocID
      @param allocAmount
      @param allocGLAccount
   */  
export interface CreateDetailLineFromAllocation_input{
   ds:Erp_Tablesets_GLJournalEntryTableset[],
      /**  Current Journal Number  */  
   journalNum:number,
      /**  Current Group ID  */  
   groupID:string,
      /**  Selected Allocation ID  */  
   allocID:string,
      /**  Selected Allocation Amount  */  
   allocAmount:number,
      /**  Selected Allocation Account  */  
   allocGLAccount:string,
}

export interface CreateDetailLineFromAllocation_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param fiscalCalendarID
      @param fiscalYear
      @param fiscalYearSuffix
      @param bookID
      @param journalCode
      @param journalNum
      @param journalLine
      @param ds
   */  
export interface DeleteAmortizationSchedule_input{
   fiscalCalendarID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   bookID:string,
   journalCode:string,
   journalNum:number,
   journalLine:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface DeleteAmortizationSchedule_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param bookID
      @param fiscalYear
      @param fiscalYearSuffix
      @param journalCode
      @param journalNum
      @param fiscalCalendarID
   */  
export interface DeleteByID_input{
   bookID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   journalCode:string,
   journalNum:number,
   fiscalCalendarID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_GLJournalEntryTableset{
   GLJrnHed:Erp_Tablesets_GLJrnHedRow[],
   GLJrnHedAttch:Erp_Tablesets_GLJrnHedAttchRow[],
   GLJrnDtlMnl:Erp_Tablesets_GLJrnDtlMnlRow[],
   GLJrnDtlMnlAttch:Erp_Tablesets_GLJrnDtlMnlAttchRow[],
   GLJrnDtlMnlDEASch:Erp_Tablesets_GLJrnDtlMnlDEASchRow[],
   GLJrnDtlMnlTranGLC:Erp_Tablesets_GLJrnDtlMnlTranGLCRow[],
   GlAllocations:Erp_Tablesets_GlAllocationsRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GLJrnDtlMnlAttchRow{
   Company:string,
   BookID:string,
   FiscalYear:number,
   FiscalYearSuffix:string,
   JournalCode:string,
   JournalNum:number,
   JournalLine:number,
   FiscalCalendarID:string,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:number,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLJrnDtlMnlDEASchRow{
      /**  Company  */  
   Company:string,
      /**  FiscalCalendarID  */  
   FiscalCalendarID:string,
      /**  FiscalYear  */  
   FiscalYear:number,
      /**  FiscalYearSuffix  */  
   FiscalYearSuffix:string,
      /**  BookID  */  
   BookID:string,
      /**  JournalCode  */  
   JournalCode:string,
      /**  JournalNum  */  
   JournalNum:number,
      /**  JournalLine  */  
   JournalLine:number,
      /**  AmortSeq  */  
   AmortSeq:number,
      /**  SchFiscalCalendarID  */  
   SchFiscalCalendarID:string,
      /**  SchFiscalYear  */  
   SchFiscalYear:number,
      /**  SchFiscalYearSuffix  */  
   SchFiscalYearSuffix:string,
      /**  SchFiscalPeriod  */  
   SchFiscalPeriod:number,
      /**  AmortDate  */  
   AmortDate:string,
      /**  AmortPercent  */  
   AmortPercent:number,
      /**  AmortAmt  */  
   AmortAmt:number,
      /**  DocAmortAmt  */  
   DocAmortAmt:number,
      /**  Posted  */  
   Posted:boolean,
      /**  PostedDate  */  
   PostedDate:string,
      /**  TranDocTypeID  */  
   TranDocTypeID:string,
      /**  LegalNumber  */  
   LegalNumber:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Rpt1AmortAmt  */  
   Rpt1AmortAmt:number,
   GroupID:string,
      /**  Document currency  */  
   CurrencyCode:string,
      /**  Rpt2AmortAmt  */  
   Rpt2AmortAmt:number,
      /**  Rpt3AmortAmt  */  
   Rpt3AmortAmt:number,
      /**  Used for Tracker only for records from GLJournalEntry. BookID in GLJrnDtl. The same as BookID field value for Single-book mode.  */  
   GLBookID:string,
      /**  Used for Tracker only for records from GLJournalEntry. Journal Number in GLJrnDtl. The same as JournalNum field value for Single-book mode.  */  
   GLJournalNum:number,
      /**  DispAmortAmt  */  
   DispAmortAmt:number,
      /**  DispDocAmortAmt  */  
   DispDocAmortAmt:number,
      /**  Indicates if this recognized Deferred Expense Amortization transaction has reverse lines  */  
   HasReverseLines:boolean,
      /**  Account Currency  */  
   CurrencyCodeAcct:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLJrnDtlMnlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Fiscal year that entry applies to.  */  
   FiscalYear:number,
      /**  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  */  
   JournalNum:number,
      /**  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  */  
   JournalLine:number,
      /**  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  */  
   Description:string,
      /**  Date for this journal transaction entry.  */  
   JEDate:string,
      /**  Fiscal period that this journal entry applies to.  */  
   FiscalPeriod:number,
      /**  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   GroupID:string,
      /**  Transaction amount.  */  
   TransAmt:number,
      /**  User ID that posted this translation.  */  
   PostedBy:string,
      /**  Date that this transaction was posted to the G/L files.  */  
   PostedDate:string,
      /**  Indicates if this entry has been posted to the G/L master balance files. Unposted entries are excluded from all G/L reports.  */  
   Posted:boolean,
      /**   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  */  
   SourceModule:string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   APInvoiceNum:string,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   JournalCode:string,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   ARInvoiceNum:number,
      /**  BankAcctId of the BankAcct master that this check was drawn  against.  */  
   BankAcctID:string,
      /**  Check number.  */  
   CheckNum:number,
      /**  Cash Receipts reference field.  */  
   CRHeadNum:number,
      /**  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  */  
   Reverse:boolean,
      /**  Bank Transaction Number.  Used when a transaction is a direct transfer from one bank account to another.  */  
   BankTranNum:number,
      /**   The identifier of the Bank Slip document (bank statement).  The user enters a bank slip during the reconciliation process.  This is then written into the related GLJrnDtl records.
Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  */  
   BankSlip:string,
      /**  Link to the related GLRefTyp.RefType.  */  
   RefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  Flag that indicate if the account is a curency account  */  
   CurrAcct:boolean,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  identifies the currency for the Currency Account.  */  
   CurrencyCodeAcct:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Multi-Company G/L Reference Type from the external company.  This is used by the Multi-Company Journal.  */  
   ExtRefType:string,
      /**  Multi-Company G/L Reference Code from the external company.  This is used by the Multi-Company Journal.  */  
   ExtRefCode:string,
      /**  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  */  
   GlbJournalNum:number,
      /**  The Journal Line assigned at the destination or target company when this Multi-Company Journal is created.  */  
   GlbJournalLine:number,
      /**  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  */  
   GlbJournalCode:string,
      /**  Global Vendor number.  Used by Multi-Company Journal.  */  
   GlbVendorNum:number,
      /**  Global AP Invoice identifier.  Used by Multi-Company Journal.  */  
   GlbAPInvoiceNum:string,
      /**  Flag to indicate that a separate journal entry will be created at the target company for the Multi-Company G/L Account entered in this journal line.  */  
   MultiCompany:boolean,
      /**  Linked to a Multi-Company Journal.  */  
   Linked:boolean,
      /**  Extended text to describe the journal line entry.  Defaults from GLJrnHed.CommentText.  */  
   CommentText:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   GlbCompanyID:string,
      /**  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  */  
   GlbFiscalYear:number,
      /**  Fiscal period from the external company that this journal entry applies to.  */  
   GlbFiscalPeriod:number,
      /**  The data entry Group from the external company that the journal entry is assigned to.  */  
   GlbGroupID:string,
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
      /**  External Segment Value 1  */  
   ExtSegValue1:string,
      /**  External Segment Value 2  */  
   ExtSegValue2:string,
      /**  External Segment Value 3  */  
   ExtSegValue3:string,
      /**  External Segment Value 4  */  
   ExtSegValue4:string,
      /**  External Segment Value 5  */  
   ExtSegValue5:string,
      /**  External Segment Value 6  */  
   ExtSegValue6:string,
      /**  External Segment Value 7  */  
   ExtSegValue7:string,
      /**  External Segment Value 8  */  
   ExtSegValue8:string,
      /**  External Segment Value 9  */  
   ExtSegValue9:string,
      /**  External Segment Value 10  */  
   ExtSegValue10:string,
      /**  External Segment Value 11  */  
   ExtSegValue11:string,
      /**  External Segment Value 12  */  
   ExtSegValue12:string,
      /**  External Segment Value 13  */  
   ExtSegValue13:string,
      /**  External Segment Value 14  */  
   ExtSegValue14:string,
      /**  External Segment Value 15  */  
   ExtSegValue15:string,
      /**  External Segment Value 16  */  
   ExtSegValue16:string,
      /**  External Segment Value 17  */  
   ExtSegValue17:string,
      /**  External Segment Value 18  */  
   ExtSegValue18:string,
      /**  External Segment Value 19  */  
   ExtSegValue19:string,
      /**  External Segment Value 20  */  
   ExtSegValue20:string,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Date record was created  */  
   CreateDate:string,
      /**  Transaction amount in document currency.  */  
   DocTransAmt:number,
      /**  A unique code that identifies the document currency.  */  
   CurrencyCode:string,
      /**  Legal Number of source document  */  
   LegalNumber:string,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   PerBalFlag:boolean,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   TBFlag:boolean,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   DailyBalFlag:boolean,
      /**  if yes, the balance records are not updated for the GLJrnDtl even if the GL Account resolves to a valid GL Balance Account.  */  
   SkipBalances:boolean,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Fiscal year suffix.  */  
   GlbFiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   GlbFiscalCalendarID:string,
      /**  Identifies the journal entry as one processed by consolidation posting mode where the data transfer is immediate and an intermediate book is used.  */  
   IntermediateProc:boolean,
      /**  Internal system calcualted sequence number not inteneded for external use.  */  
   GenID:number,
      /**  Source Company Identifier.  Identifies the company where this GLJrnDtl originated from.  */  
   SrcCompany:string,
      /**  Unique Book Identifier  This is the book that is being consolidated into a target book.  */  
   SrcBook:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   SrcGLAccount:string,
      /**  Source Journal Code  */  
   SrcJrnlCode:string,
      /**  Source Journal Number  */  
   SrcJournalNum:number,
      /**  Source Journal Line  */  
   SrcJournalLine:number,
      /**   P = derived from Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.  */  
   SrcType:string,
      /**  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  */  
   CloseFiscalPeriod:number,
      /**  Chart of Account ID  */  
   ExtCOACode:string,
      /**  Full External GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the External GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   ExtGLAccount:string,
      /**  This field shows Debit value of transaction  */  
   DebitAmount:number,
      /**  This field shows Credit value of transaction  */  
   CreditAmount:number,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
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
      /**  PaymentNumber  */  
   PaymentNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Possible values: 0`In~1`Out  */  
   PartOfDual:string,
      /**  Tax Journal Line reporting module.  Possible values: 0`AP~1`AR  */  
   ReportingModule:string,
      /**  Book Currency for Taxable Amount  */  
   TaxableAmtBookCurr:string,
      /**  Transactional Currency for Taxable Amount  */  
   TaxableAmtCurr:string,
      /**  Taxable Amount In Book Currency  */  
   TaxableAmtInBookCurr:number,
      /**  Taxable Amount InTransactional Currency  */  
   TaxableAmtInTranCurr:number,
      /**  Taxable Line. It is used for tax Jornal Line.  */  
   TaxableLine:string,
      /**  Tax Liability. It is used for tax Jornal Line.  */  
   TaxLiability:string,
      /**  Inducate that it is Tax Journal Line  */  
   TaxLine:boolean,
      /**  Tax Percent. It is used for tax Jornal Line.  */  
   TaxPercent:number,
      /**  Tax Point Date. It is used for tax Jornal Line.  */  
   TaxPointDate:string,
      /**  Tax Rate. It is used for tax Jornal Line.  */  
   TaxRate:string,
      /**  Tax Type. It is used for tax Jornal Line.  */  
   TaxType:string,
      /**  OverrideGLAcct  */  
   OverrideGLAcct:boolean,
      /**  OneTimeID  */  
   COOneTimeID:string,
      /**  DeferredExp  */  
   DeferredExp:boolean,
      /**  DEACode  */  
   DEACode:string,
      /**  DEAStartDate  */  
   DEAStartDate:string,
      /**  DEAEndDate  */  
   DEAEndDate:string,
      /**  MovementNum  */  
   MovementNum:number,
      /**  Malaysia Industry Code  */  
   MYIndustryCode:string,
      /**  The Internal CustNum that ties back to the Customer master file.  */  
   CustNum:number,
      /**  GL Journal Line Reference Type  */  
   LineReferenceType:string,
      /**  SourcePlant  */  
   SourcePlant:string,
      /**  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  */  
   ExtSysType:string,
      /**  URL for drill back to an integrated external system  */  
   ExtSysURL:string,
      /**  Colombia Loc Field.  */  
   COLTaxTranType:string,
   CurrencyCodeAcctList:string,
      /**  Is Deferred Expense Amortization Scheduled  */  
   DEAScheduled:boolean,
      /**  DEA Distributed Amount  */  
   Distributed:number,
      /**  DEA Distributed Amount in Doc Currency  */  
   DocDistributed:number,
      /**  DEA Expense Amount in Doc Currency  */  
   DocExpense:number,
      /**  DEA Recognized Amount in Doc Currency  */  
   DocRecognized:number,
      /**  DEA Remaining Amount in Doc Currency  */  
   DocRemaining:number,
      /**  DEA Unrecognized Amount in Doc Currency  */  
   DocUnrecognized:number,
      /**  Display Fiscal Period  */  
   DspFiscalPeriod:number,
      /**  Flag to indicate if the MultiCompany check box needs to be enabled.  */  
   EnableMultiCompany:boolean,
      /**  DEA Expense Amount  */  
   Expense:number,
   ExtRefAcctChart:string,
   ExtRefAcctDept:string,
   ExtRefAcctDiv:string,
   ExtRefCodeStatus:string,
   GlbGLAccountDesc:string,
      /**  Flag: true - control In/Out is enabled, else disabled  */  
   PartOfDualEnabled:boolean,
      /**  Colombia Loc Field.  */  
   RateCode:string,
      /**  Colombia Loc Field.  */  
   RateDescription:string,
      /**  DEA Recognized Amount  */  
   Recognized:number,
   RefAcctChart:string,
   RefAcctDept:string,
   RefAcctDiv:string,
   RefCodeStatus:string,
      /**  DEA Remaining Amount  */  
   Remaining:number,
      /**  Statistical Amount. UI display value.  */  
   StatAmount:number,
      /**  Colombia Loc Field.  */  
   TaxableAmt:number,
      /**  Used for Colombia CSF  */  
   TaxCode:string,
   TaxLiabilityDescr:string,
      /**  The list of tax codes for Tax Liability  */  
   TaxLiabilityTaxCodes:string,
   TaxRateDescr:string,
   TaxTypeDescr:string,
      /**  The list of tax rates for Tax code  */  
   TaxTypeTaxRates:string,
   TotCredit:number,
   TotCurrCredit:number,
   TotCurrDebit:number,
   TotDebit:number,
      /**  DEA Unrecognized Amount  */  
   Unrecognized:number,
      /**  Colombia Loc Field.  */  
   COIsTaxLn:boolean,
      /**  GL Journal Line Reference Holder.  */  
   LineReferenceHolder:string,
      /**  GL Journal Line Reference Holder Name.  */  
   LineReferenceHolderName:string,
      /**  GL Journal Line Reference.  */  
   LineReference:string,
      /**  Source GL Journal Line to copy reference data.  */  
   RefSourceJrnLine:string,
      /**  Result of account validation. False if account is valid.  */  
   InvalidGLAccount:boolean,
      /**  Result of account validation. Empty if account is valid.  */  
   InvalidGLAccountMessage:string,
      /**  Result of external account validation. False if account is valid.  */  
   InvalidExtGLAccount:boolean,
      /**  Result of external account validation. Empty if account is valid.  */  
   InvalidExtGLAccountMessage:string,
      /**  Calculated field for correspondence accounting journals. Determines if the current line an odd one.  */  
   CorrAcctOddLine:boolean,
   BitFlag:number,
   AcctCurrCurrencyID:string,
   AcctCurrCurrSymbol:string,
   AcctCurrCurrDesc:string,
   AcctCurrCurrName:string,
   AcctCurrDocumentDesc:string,
   BankAcctIDDescription:string,
   BankAcctIDBankName:string,
   CurrencyCurrName:string,
   CurrencyCurrDesc:string,
   CurrencyDocumentDesc:string,
   CurrencyCurrSymbol:string,
   CurrencyCurrencyID:string,
   CustNumCustID:string,
   CustNumName:string,
   CustNumBTName:string,
   DEACodeDescRADesc:string,
   ExtRefCodeRefCodeDesc:string,
   GLGLAcctDisp:string,
   GLGLShortAcct:string,
   GLAccountDesc:string,
   GlRefCodeDescRefCodeDesc:string,
   JournalCodeJrnlDescription:string,
   StatUOMStatUOMDesc:string,
   VendorNumCurrencyCode:string,
   VendorNumCountry:string,
   VendorNumAddress2:string,
   VendorNumAddress1:string,
   VendorNumVendorID:string,
   VendorNumTermsCode:string,
   VendorNumDefaultFOB:string,
   VendorNumAddress3:string,
   VendorNumName:string,
   VendorNumState:string,
   VendorNumZIP:string,
   VendorNumCity:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLJrnDtlMnlTranGLCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  */  
   Key2:string,
      /**  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  */  
   Key3:string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key4:string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key5:string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key6:string,
      /**  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  */  
   TGLCTranNum:number,
      /**  String identifier of the account context.  */  
   GLAcctContext:string,
      /**  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  */  
   BookID:string,
      /**  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  */  
   COACode:string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   GLAccount:string,
      /**  Indicates if the user can update or delete this record.  */  
   UserCanModify:boolean,
      /**  Segement Value 1 of the account for this context.  */  
   SegValue1:string,
      /**  Segement Value 2 of the account for this context.  */  
   SegValue2:string,
      /**  Segement Value 3 of the account for this context.  */  
   SegValue3:string,
      /**  Segement Value 4 of the account for this context.  */  
   SegValue4:string,
      /**  Segement Value 5 of the account for this context.  */  
   SegValue5:string,
      /**  Segement Value 6 of the account for this context.  */  
   SegValue6:string,
      /**  Segement Value 7 of the account for this context.  */  
   SegValue7:string,
      /**  Segement Value 8 of the account for this context.  */  
   SegValue8:string,
      /**  Segement Value 9 of the account for this context.  */  
   SegValue9:string,
      /**  Segement Value 10 of the account for this context.  */  
   SegValue10:string,
      /**  Segement Value 11 of the account for this context.  */  
   SegValue11:string,
      /**  Segement Value 12 of the account for this context.  */  
   SegValue12:string,
      /**  Segement Value 13 of the account for this context.  */  
   SegValue13:string,
      /**  Segement Value 14 of the account for this context.  */  
   SegValue14:string,
      /**  Segement Value 15 of the account for this context.  */  
   SegValue15:string,
      /**  Segement Value 16 of the account for this context.  */  
   SegValue16:string,
      /**  Segement Value 17 of the account for this context.  */  
   SegValue17:string,
      /**  Segement Value 18 of the account for this context.  */  
   SegValue18:string,
      /**  Segement Value 19 of the account for this context.  */  
   SegValue19:string,
      /**  Segement Value 20 of the account for this context.  */  
   SegValue20:string,
      /**  Unique Identifier of the system GL Control Type.  */  
   SysGLControlType:string,
      /**  System generated GL Control Identifier.  */  
   SysGLControlCode:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   IsExternalCompany:boolean,
      /**  Fiscal year of the related GLJrnDtl.  */  
   FiscalYear:number,
      /**  JournalCode of the related GLJrnDtl.  */  
   JournalCode:string,
      /**  Journal number of the related GLJrnDtl.  */  
   JournalNum:number,
      /**  JournalLine of the related GLJrnDtl.  */  
   JournalLine:number,
      /**  Transaction date of the transaction.  This is used in order to display the transactions in date order.  */  
   TranDate:string,
      /**   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  */  
   TranSource:string,
      /**  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  */  
   LaborHedSeq:number,
      /**  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  */  
   LaborDtlSeq:number,
      /**  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   SysDate:string,
      /**  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   SysTime:number,
      /**  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   TranNum:number,
      /**  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  */  
   ARInvoiceNum:number,
      /**  Transaction amount that this transaction posted to the related GlJrnDtl.  */  
   TransAmt:number,
      /**  Invoice Line Number associated with this GL Journal  */  
   InvoiceLine:number,
      /**  The sequence number associated with this GL journal  */  
   SeqNum:number,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   APInvoiceNum:string,
      /**  Date record was created  */  
   CreateDate:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Credit Amount.  */  
   CreditAmount:number,
      /**  Debit Amount.  */  
   DebitAmount:number,
      /**  BookCreditAmount  */  
   BookCreditAmount:number,
      /**  Book Debit Amount  */  
   BookDebitAmount:number,
      /**  A unique code that identifies the document currency.  */  
   CurrencyCode:string,
      /**   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  */  
   RecordType:string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   CorrAccUID:number,
      /**  this field equals ABTUID which was created during posting  */  
   ABTUID:string,
      /**  Technical identifier.  */  
   RuleUID:number,
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
      /**  IsModifiedByUser  */  
   IsModifiedByUser:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MovementNum  */  
   MovementNum:number,
      /**  MovementType  */  
   MovementType:string,
      /**  Plant  */  
   Plant:string,
   GroupID:string,
   BookMode:string,
   BitFlag:number,
   GLAccountGLAcctDisp:string,
   GLAccountGLShortAcct:string,
   GLAccountAccountDesc:string,
   GLBookDescription:string,
   GLBookCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLJrnHedAttchRow{
   Company:string,
   BookID:string,
   FiscalYear:number,
   FiscalYearSuffix:string,
   JournalCode:string,
   JournalNum:number,
   FiscalCalendarID:string,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:number,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLJrnHedListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The fiscal year for this journal transaction header. Assigned from GLJrnGrp.FiscalYear.  */  
   FiscalYear:number,
      /**  Fiscal period that this journal entry applies to.  */  
   FiscalPeriod:number,
      /**  Number that is assigned by the system.  The Journal Number is a way of relating the detail entries into a group that would normally balance.  When we need to assign a new number the system  finds the journalnum of the last record (GLJrnDtl) for the fiscal year and adds one.  When creating GLJrnDtl from other modules this number is assigned note that this find last is performed on the GLJrnDtl because the GLJrnHed records only exist until the group is posted.  */  
   JournalNum:number,
      /**  Describes the journal transaction.  Used as a default for the GLJrnDtl.Description field.  */  
   Description:string,
      /**  The Date for this journal transaction entry.  Defaulted from GLJrnGrp.JEDate.  Can be overridden during entry, but it must be a valid date for the fiscal period that is assigned to this group.  */  
   JEDate:string,
      /**  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   GroupID:string,
      /**  The Total Debits.  A summary of the positive GLJrnDtl.TranAmt in the related GLJrnDtl records.  Primarily used for visual verification.  */  
   TotDebit:number,
      /**  The Total Credit.  A summary of negative GLJrnDtl.TranAmt in the related GLJrnDtl records.  Primarily used for visual verification.  */  
   TotCredit:number,
      /**  Indicates that this is a non-balancing journal entry that the user indicated is valid to post.  */  
   Override:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  User ID that created the record.  */  
   EnteredBy:string,
      /**  Indicates that this journal transaction set should create reversing entries for the next fiscal period.  This happens during the posting process.  */  
   Reverse:boolean,
      /**  Default is the first date of the next period. A date entered in this fields should be greater than the journal?s apply date.  */  
   ReverseDate:string,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   JournalCode:string,
      /**  Flag to indicate that journal lines appearing under this journal header may have multi-company journals entered at the target external company.  */  
   MultiCompany:boolean,
      /**  Extended text to describe the journal header.  Defaults to all GLJrnDtl.CommentText.  */  
   CommentText:string,
      /**  Date that this transaction was posted from the external company to the G/L files.  */  
   GlbPostedDate:string,
      /**  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  */  
   GlbJournalNum:number,
      /**  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  */  
   GlbJournalCode:string,
      /**  Global Vendor number.  Used by Multi-Company Journal.  */  
   GlbVendorNum:number,
      /**  Global AP Invoice identifier.  Used by Multi-Company Journal.  */  
   GlbAPInvoiceNum:string,
      /**  Global Vendor ID.  Used by Multi-Company Journal.  */  
   GlbVendorID:string,
      /**  Global Vendor Name.  Used by the Multi-Company Journal.  */  
   GlbVendorName:string,
      /**  Legal Number used by the source AP Invoice.  Used by the Multi-Company Journal.  */  
   GlbAPLegalNumber:string,
      /**  Global AP Invoice description.  Used by Multi-Company Journal.  */  
   GlbAPInvDesc:string,
      /**  Linked to a Multi-Company Journal.  */  
   Linked:boolean,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   GlbCompanyID:string,
      /**  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  */  
   GlbFiscalYear:number,
      /**  Fiscal period from the external company that this journal entry applies to.  */  
   GlbFiscalPeriod:number,
      /**  The data entry Group from the external company that the journal entry is assigned to.  */  
   GlbGroupID:string,
      /**  Global Journal Code Description.  */  
   GlbJournalCodeDesc:string,
      /**  User ID that created the Multi-Company Journal record from the source company.  This may not be a valid UserId in the target company.  Used by the Multi-Company GJ and AP.  */  
   GlbEnteredBy:string,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Date record was created  */  
   CreateDate:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Fiscal year suffix.  */  
   GlbFiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   GlbFiscalCalendarID:string,
      /**  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  */  
   CloseFiscalPeriod:number,
      /**  if yes it means that during posting for each line debit and credit amounts should be saved with opposite signs.  */  
   RedStorno:boolean,
      /**  It is true, if the record was posted.  */  
   Posted:boolean,
      /**  Date when record was posted.  */  
   PostedDate:string,
      /**  This field shows Debit statistical amount.  */  
   DebitStatAmt:number,
      /**  0 - Manual Entry; 1 - Revaluation Process; 2 - Consolidation Process.  */  
   ProcessType:number,
      /**  This field shows Credit statistical amount.  */  
   CreditStatAmt:number,
      /**  Flag that indicates if correspondence accounting is set-up for the journal.  */  
   CorrAccounting:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  TotDebit - TotCredit = Balance  */  
   Balance:number,
      /**  Display total debit.  */  
   DispTotDebit:number,
      /**  Display total credit.  */  
   DispTotCredit:number,
      /**  Flag to indicate if the MultiCompany check box needs to be enabled.  */  
   EnableMultiCompany:boolean,
      /**  Display Fiscal Period  */  
   DspFiscalPeriod:number,
   LegalNumMessage:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
   AllowUnbalancedEntries:boolean,
      /**  Calendar description.  */  
   FiscalCalDescription:string,
      /**  Journal  Description.  */  
   JournalCodeJrnlDescription:string,
      /**  Description  */  
   RateGrpCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLJrnHedListTableset{
   GLJrnHedList:Erp_Tablesets_GLJrnHedListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GLJrnHedRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The fiscal year for this journal transaction header. Assigned from GLJrnGrp.FiscalYear.  */  
   FiscalYear:number,
      /**  Fiscal period that this journal entry applies to.  */  
   FiscalPeriod:number,
      /**  Number that is assigned by the system.  The Journal Number is a way of relating the detail entries into a group that would normally balance.  When we need to assign a new number the system  finds the journalnum of the last record (GLJrnDtl) for the fiscal year and adds one.  When creating GLJrnDtl from other modules this number is assigned note that this find last is performed on the GLJrnDtl because the GLJrnHed records only exist until the group is posted.  */  
   JournalNum:number,
      /**  Describes the journal transaction.  Used as a default for the GLJrnDtl.Description field.  */  
   Description:string,
      /**  The Date for this journal transaction entry.  Defaulted from GLJrnGrp.JEDate.  Can be overridden during entry, but it must be a valid date for the fiscal period that is assigned to this group.  */  
   JEDate:string,
      /**  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   GroupID:string,
      /**  The Total Debits.  A summary of the positive GLJrnDtl.TranAmt in the related GLJrnDtl records.  Primarily used for visual verification.  */  
   TotDebit:number,
      /**  The Total Credit.  A summary of negative GLJrnDtl.TranAmt in the related GLJrnDtl records.  Primarily used for visual verification.  */  
   TotCredit:number,
      /**  Indicates that this is a non-balancing journal entry that the user indicated is valid to post.  */  
   Override:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  User ID that created the record.  */  
   EnteredBy:string,
      /**  Indicates that this journal transaction set should create reversing entries for the next fiscal period.  This happens during the posting process.  */  
   Reverse:boolean,
      /**  Default is the first date of the next period. A date entered in this fields should be greater than the journal?s apply date.  */  
   ReverseDate:string,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   JournalCode:string,
      /**  Flag to indicate that journal lines appearing under this journal header may have multi-company journals entered at the target external company.  */  
   MultiCompany:boolean,
      /**  Extended text to describe the journal header.  Defaults to all GLJrnDtl.CommentText.  */  
   CommentText:string,
      /**  Date that this transaction was posted from the external company to the G/L files.  */  
   GlbPostedDate:string,
      /**  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  */  
   GlbJournalNum:number,
      /**  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  */  
   GlbJournalCode:string,
      /**  Global Vendor number.  Used by Multi-Company Journal.  */  
   GlbVendorNum:number,
      /**  Global AP Invoice identifier.  Used by Multi-Company Journal.  */  
   GlbAPInvoiceNum:string,
      /**  Global Vendor ID.  Used by Multi-Company Journal.  */  
   GlbVendorID:string,
      /**  Global Vendor Name.  Used by the Multi-Company Journal.  */  
   GlbVendorName:string,
      /**  Legal Number used by the source AP Invoice.  Used by the Multi-Company Journal.  */  
   GlbAPLegalNumber:string,
      /**  Global AP Invoice description.  Used by Multi-Company Journal.  */  
   GlbAPInvDesc:string,
      /**  Linked to a Multi-Company Journal.  */  
   Linked:boolean,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   GlbCompanyID:string,
      /**  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  */  
   GlbFiscalYear:number,
      /**  Fiscal period from the external company that this journal entry applies to.  */  
   GlbFiscalPeriod:number,
      /**  The data entry Group from the external company that the journal entry is assigned to.  */  
   GlbGroupID:string,
      /**  Global Journal Code Description.  */  
   GlbJournalCodeDesc:string,
      /**  User ID that created the Multi-Company Journal record from the source company.  This may not be a valid UserId in the target company.  Used by the Multi-Company GJ and AP.  */  
   GlbEnteredBy:string,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Date record was created  */  
   CreateDate:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Fiscal year suffix.  */  
   GlbFiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   GlbFiscalCalendarID:string,
      /**  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  */  
   CloseFiscalPeriod:number,
      /**  if yes it means that during posting for each line debit and credit amounts should be saved with opposite signs.  */  
   RedStorno:boolean,
      /**  It is true, if the record was posted.  */  
   Posted:boolean,
      /**  Date when record was posted.  */  
   PostedDate:string,
      /**  This field shows Debit statistical amount.  */  
   DebitStatAmt:number,
      /**  0 - Manual Entry; 1 - Revaluation Process; 2 - Consolidation Process.  */  
   ProcessType:number,
      /**  This field shows Credit statistical amount.  */  
   CreditStatAmt:number,
      /**  Flag that indicates if correspondence accounting is set-up for the journal.  */  
   CorrAccounting:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Tax Handling: 0 - No Tax; 1 - Journal Includes Taxes; 2 - Tax adlustment Journal  */  
   TaxHandling:string,
      /**  Transaction Document Type for the record.  */  
   TranDocTypeID:string,
      /**  Indicate, that this Journal can have only lines with Statistical Accounts. Legal Number creation for Statistical Journals should be skipped.  */  
   Statistical:boolean,
      /**  TransferredToParent  */  
   TransferredToParent:boolean,
      /**  TransferredDate  */  
   TransferredDate:string,
      /**  TransferredPerson  */  
   TransferredPerson:string,
      /**  MXFiscalFolio  */  
   MXFiscalFolio:string,
      /**  MXRFC  */  
   MXRFC:string,
      /**  If box is checked, this journal has been marked as on hold.  */  
   JournalHeld:boolean,
      /**  SourcePlant  */  
   SourcePlant:string,
      /**  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  */  
   ExtSysType:string,
      /**  URL for drill back to an integrated external system  */  
   ExtSysURL:string,
   AllowChgAfterPrint:boolean,
      /**  Display total credit.  */  
   DispTotCredit:number,
      /**  Display total debit.  */  
   DispTotDebit:number,
      /**  Display Fiscal Period  */  
   DspFiscalPeriod:number,
   EnableAssignLegNum:boolean,
   EnableCorrAccounting:boolean,
      /**  Flag to indicate if the MultiCompany check box needs to be enabled.  */  
   EnableMultiCompany:boolean,
   EnableTranDocType:boolean,
   EnableVoidLegNum:boolean,
   HasLegNumCnfg:boolean,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
   LegalNumMessage:string,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  Used by UI to determine if the Red Storno checkbox is to be enabled.  */  
   RedStornoOpt:string,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
      /**  The system transaction type - ARInvoice or CreditMemo.  Used to filter combo list for TranDocTypeID.  */  
   SystemTranType:string,
   AllowUnbalancedEntries:boolean,
      /**  TotDebit - TotCredit = Balance  */  
   Balance:number,
   CompanyTaxEntryMode:string,
      /**  Field used for Colombia CSF  */  
   COOneTimeDtl:boolean,
      /**  Defines site entry allowed on journal  */  
   AllowSiteEntry:boolean,
   BitFlag:number,
   CurrencyCurrName:string,
   CurrencyCurrDesc:string,
   CurrencyDocumentDesc:string,
   CurrencyCurrencyID:string,
   CurrencyCurrSymbol:string,
   FiscalCalDescription:string,
   JournalCodeJrnlDescription:string,
   RateGrpCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlAllocationsRow{
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   GLAccount:string,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   SegValue1:string,
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
      /**  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   SegValue2:string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   SegValue20:string,
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
   AccountDesc:string,
   BookID:string,
   AllocID:string,
   Amount:number,
   Company:string,
   Description:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LegalNumGenOptsRow{
   Company:string,
   LegalNumberID:string,
   TransYear:number,
   TransYearSuffix:string,
   DspTransYear:string,
      /**  Indicates if DspTransYear should be displayed when prompting for a manual number.  */  
   ShowDspTransYear:boolean,
   Prefix:string,
      /**  The list of prefixes that can be selected by the user for manual numbers.  */  
   PrefixList:string,
      /**  The suffix portion of the legal number.  */  
   NumberSuffix:string,
      /**  Indicates if the prefix can be entered by the user.  */  
   EnablePrefix:boolean,
      /**  Indicates if the suffix (number) can be entered by the user.  */  
   EnableSuffix:boolean,
   NumberOption:string,
   DocumentDate:string,
   GenerationType:string,
   Description:string,
   TransPeriod:number,
      /**  Prefix for the period  */  
   PeriodPrefix:string,
   ShowTransPeriod:boolean,
      /**  Used when the full legal number is entered  */  
   LegalNumber:string,
   TranDocTypeID:string,
   TranDocTypeID2:string,
   GenerationOption:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtGLJournalEntryTableset{
   GLJrnHed:Erp_Tablesets_GLJrnHedRow[],
   GLJrnHedAttch:Erp_Tablesets_GLJrnHedAttchRow[],
   GLJrnDtlMnl:Erp_Tablesets_GLJrnDtlMnlRow[],
   GLJrnDtlMnlAttch:Erp_Tablesets_GLJrnDtlMnlAttchRow[],
   GLJrnDtlMnlDEASch:Erp_Tablesets_GLJrnDtlMnlDEASchRow[],
   GLJrnDtlMnlTranGLC:Erp_Tablesets_GLJrnDtlMnlTranGLCRow[],
   GlAllocations:Erp_Tablesets_GlAllocationsRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
   */  
export interface GenLegalNum_input{
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface GenLegalNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param fiscalCalendarID
      @param fiscalYear
      @param fiscalYearSuffix
      @param bookID
      @param journalCode
      @param journalNum
      @param journalLine
      @param ds
   */  
export interface GenerateAmortizationSchedule_input{
   fiscalCalendarID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   bookID:string,
   journalCode:string,
   journalNum:number,
   journalLine:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface GenerateAmortizationSchedule_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param bookID
      @param ds
   */  
export interface GetAllocations_input{
   bookID:string,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface GetAllocations_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
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
      @param GroupID
   */  
export interface GetByGroupID_input{
      /**  Current Group ID  */  
   GroupID:string,
}

export interface GetByGroupID_output{
   returnObj:Erp_Tablesets_GLJournalEntryTableset[],
}

   /** Required : 
      @param bookID
      @param fiscalYear
      @param fiscalYearSuffix
      @param journalCode
      @param journalNum
      @param fiscalCalendarID
   */  
export interface GetByID_input{
   bookID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   journalCode:string,
   journalNum:number,
   fiscalCalendarID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_GLJournalEntryTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_GLJournalEntryTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_GLJournalEntryTableset[],
}

   /** Required : 
      @param fiscalCalendarID
      @param fiscalYear
      @param fiscalYearSuffix
      @param bookID
      @param journalCode
      @param journalNum
      @param journalLine
      @param ds
   */  
export interface GetDefaultAccount_input{
   fiscalCalendarID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   bookID:string,
   journalCode:string,
   journalNum:number,
   journalLine:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface GetDefaultAccount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
   outMessage:string,
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
   returnObj:Erp_Tablesets_GLJrnHedListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param bookID
      @param fiscalYear
      @param fiscalYearSuffix
      @param journalCode
      @param journalNum
      @param journalLine
      @param fiscalCalendarID
   */  
export interface GetNewGLJrnDtlMnlAttch_input{
   ds:Erp_Tablesets_GLJournalEntryTableset[],
   bookID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   journalCode:string,
   journalNum:number,
   journalLine:number,
   fiscalCalendarID:string,
}

export interface GetNewGLJrnDtlMnlAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param ds
      @param fiscalCalendarID
      @param fiscalYear
      @param fiscalYearSuffix
      @param bookID
      @param journalCode
      @param journalNum
      @param journalLine
   */  
export interface GetNewGLJrnDtlMnlDEASchPopulated_input{
   ds:Erp_Tablesets_GLJournalEntryTableset[],
   fiscalCalendarID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   bookID:string,
   journalCode:string,
   journalNum:number,
   journalLine:number,
}

export interface GetNewGLJrnDtlMnlDEASchPopulated_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param ds
      @param fiscalCalendarID
      @param fiscalYear
      @param fiscalYearSuffix
      @param glBookID
      @param journalCode
      @param glJournalNum
      @param journalLine
   */  
export interface GetNewGLJrnDtlMnlDEASch_input{
   ds:Erp_Tablesets_GLJournalEntryTableset[],
   fiscalCalendarID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   glBookID:string,
   journalCode:string,
   glJournalNum:number,
   journalLine:number,
}

export interface GetNewGLJrnDtlMnlDEASch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewGLJrnDtlMnlTranGLC_input{
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface GetNewGLJrnDtlMnlTranGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param ds
      @param bookID
      @param fiscalYear
      @param fiscalYearSuffix
      @param journalCode
      @param journalNum
      @param journalLine
   */  
export interface GetNewGLJrnDtlMnl_input{
   ds:Erp_Tablesets_GLJournalEntryTableset[],
   bookID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   journalCode:string,
   journalNum:number,
   journalLine:number,
}

export interface GetNewGLJrnDtlMnl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param ds
      @param bookID
      @param fiscalYear
      @param fiscalYearSuffix
      @param journalCode
      @param journalNum
      @param fiscalCalendarID
   */  
export interface GetNewGLJrnHedAttch_input{
   ds:Erp_Tablesets_GLJournalEntryTableset[],
   bookID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   journalCode:string,
   journalNum:number,
   fiscalCalendarID:string,
}

export interface GetNewGLJrnHedAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param ds
      @param bookID
      @param fiscalYear
      @param fiscalYearSuffix
      @param journalCode
      @param journalNum
   */  
export interface GetNewGLJrnHed_input{
   ds:Erp_Tablesets_GLJournalEntryTableset[],
   bookID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   journalCode:string,
   journalNum:number,
}

export interface GetNewGLJrnHed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param ds
      @param GroupID
   */  
export interface GetNewGlJrnHedTran_input{
   ds:Erp_Tablesets_GLJournalEntryTableset[],
      /**  Current Group ID  */  
   GroupID:string,
}

export interface GetNewGlJrnHedTran_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param ds
      @param GroupID
   */  
export interface GetNewStatisticalGLJrnHed_input{
   ds:Erp_Tablesets_GLJournalEntryTableset[],
   GroupID:string,
}

export interface GetNewStatisticalGLJrnHed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param guid
   */  
export interface GetRefSourceJrnLineList_input{
      /**  Current Journal Line guid  */  
   guid:string,
}

export interface GetRefSourceJrnLineList_output{
   returnObj:string,
}

   /** Required : 
      @param whereClauseGLJrnHed
      @param whereClauseGLJrnHedAttch
      @param whereClauseGLJrnDtlMnl
      @param whereClauseGLJrnDtlMnlAttch
      @param whereClauseGLJrnDtlMnlDEASch
      @param whereClauseGLJrnDtlMnlTranGLC
      @param whereClauseGlAllocations
      @param whereClauseLegalNumGenOpts
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseGLJrnHed:string,
   whereClauseGLJrnHedAttch:string,
   whereClauseGLJrnDtlMnl:string,
   whereClauseGLJrnDtlMnlAttch:string,
   whereClauseGLJrnDtlMnlDEASch:string,
   whereClauseGLJrnDtlMnlTranGLC:string,
   whereClauseGlAllocations:string,
   whereClauseLegalNumGenOpts:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_GLJournalEntryTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetTaxEntryMode_output{
parameters : {
      /**  output parameters  */  
   cMode:string,
}
}

   /** Required : 
      @param cTaxType
      @param dTaxPointDate
   */  
export interface GetTaxRatesList_input{
      /**  Tax type  */  
   cTaxType:string,
      /**  Tax point date  */  
   dTaxPointDate:string,
}

export interface GetTaxRatesList_output{
parameters : {
      /**  output parameters  */  
   cTaxRatesList:string,
}
}

   /** Required : 
      @param cTaxLiability
   */  
export interface GetTaxTypesList_input{
      /**  Tax Liability.  */  
   cTaxLiability:string,
}

export interface GetTaxTypesList_output{
parameters : {
      /**  output parameters  */  
   cTaxTypesList:string,
}
}

   /** Required : 
      @param ipCompanyTaxEntryMode
   */  
export interface GetTaxaHandlingList_input{
   ipCompanyTaxEntryMode:string,
}

export interface GetTaxaHandlingList_output{
   returnObj:string,
}

   /** Required : 
      @param ipBookID
      @param ipFiscalYear
      @param ipFiscalYearSuffix
      @param ipJournalCode
      @param ipJournalNum
      @param ipJournalLine
      @param ipFiscalCalendarID
   */  
export interface GetTaxableLinesListWithParams_input{
   ipBookID:string,
   ipFiscalYear:number,
   ipFiscalYearSuffix:string,
   ipJournalCode:string,
   ipJournalNum:number,
   ipJournalLine:number,
   ipFiscalCalendarID:string,
}

export interface GetTaxableLinesListWithParams_output{
   returnObj:string,
}

   /** Required : 
      @param guid
   */  
export interface GetTaxableLinesList_input{
      /**  Current Journal Line guid  */  
   guid:string,
}

export interface GetTaxableLinesList_output{
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
      @param iLineNum
      @param ds
   */  
export interface OnChangeCurrencyAcct_input{
      /**  Journal Line Number  */  
   iLineNum:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface OnChangeCurrencyAcct_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param fiscalCalendarID
      @param fiscalYear
      @param fiscalYearSuffix
      @param bookID
      @param journalCode
      @param journalNum
      @param journalLine
      @param amortSeq
      @param srcField
      @param propValue
      @param ds
   */  
export interface OnChangeDEAScheduleLineAmount_input{
   fiscalCalendarID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   bookID:string,
   journalCode:string,
   journalNum:number,
   journalLine:number,
   amortSeq:number,
   srcField:string,
   propValue:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface OnChangeDEAScheduleLineAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param fiscalCalendarID
      @param fiscalYear
      @param fiscalYearSuffix
      @param bookID
      @param journalCode
      @param journalNum
      @param journalLine
      @param amortSeq
      @param srcField
      @param ds
   */  
export interface OnChangeDEAScheduleLineFiscalPeriod_input{
   fiscalCalendarID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   bookID:string,
   journalCode:string,
   journalNum:number,
   journalLine:number,
   amortSeq:number,
   srcField:string,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface OnChangeDEAScheduleLineFiscalPeriod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param glJournalDtlMnlSysRowID
      @param segValue1
      @param ds
   */  
export interface OnChangeLineDEAAccount_input{
   glJournalDtlMnlSysRowID:string,
   segValue1:string,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface OnChangeLineDEAAccount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param fiscalCalendarID
      @param fiscalYear
      @param fiscalYearSuffix
      @param bookID
      @param journalCode
      @param journalNum
      @param journalLine
      @param deaCode
      @param ds
   */  
export interface OnChangeLineDEACode_input{
   fiscalCalendarID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   bookID:string,
   journalCode:string,
   journalNum:number,
   journalLine:number,
   deaCode:string,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface OnChangeLineDEACode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param fiscalCalendarID
      @param fiscalYear
      @param fiscalYearSuffix
      @param bookID
      @param journalCode
      @param journalNum
      @param journalLine
      @param startDate
      @param ds
   */  
export interface OnChangeLineDEAStartDate_input{
   fiscalCalendarID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   bookID:string,
   journalCode:string,
   journalNum:number,
   journalLine:number,
   startDate:string,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface OnChangeLineDEAStartDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param fiscalCalendarID
      @param fiscalYear
      @param fiscalYearSuffix
      @param bookID
      @param journalCode
      @param journalNum
      @param journalLine
      @param ipDefExp
      @param ds
   */  
export interface OnChangeLineDefferedExp_input{
   fiscalCalendarID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   bookID:string,
   journalCode:string,
   journalNum:number,
   journalLine:number,
   ipDefExp:boolean,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface OnChangeLineDefferedExp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param proposedRefHolder
      @param iLineNum
      @param ds
   */  
export interface OnChangeLineReferenceHolder_input{
      /**  proposed Reference Holder  */  
   proposedRefHolder:string,
      /**  Journal Line Number  */  
   iLineNum:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface OnChangeLineReferenceHolder_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param proposedReference
      @param iLineNum
      @param ds
   */  
export interface OnChangeLineReference_input{
      /**  proposed Reference  */  
   proposedReference:string,
      /**  Journal Line Number  */  
   iLineNum:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface OnChangeLineReference_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param iLineNum
      @param ds
   */  
export interface OnChangeTaxLiability_input{
      /**  Journal Line Number  */  
   iLineNum:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface OnChangeTaxLiability_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param iLineNum
      @param ds
   */  
export interface OnChangeTaxRate_input{
      /**  Journal Line Number  */  
   iLineNum:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface OnChangeTaxRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param iLineNum
      @param ds
   */  
export interface OnChangeTaxType_input{
      /**  Journal Line Number  */  
   iLineNum:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface OnChangeTaxType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param iLineNum
      @param ds
   */  
export interface OnChangeTaxableAmntInTranCurr_input{
      /**  Journal Line Number  */  
   iLineNum:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface OnChangeTaxableAmntInTranCurr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param iLineNum
      @param ds
   */  
export interface OnChangeTaxableLine_input{
      /**  Journal Line Number  */  
   iLineNum:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface OnChangeTaxableLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param ipTranDocTypeID
      @param ds
   */  
export interface OnChangeTranDocTypeID_input{
      /**  TranDocTypeID supplied  */  
   ipTranDocTypeID:string,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface OnChangeTranDocTypeID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface PreGenLegalNum_input{
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface PreGenLegalNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
   RequiresUserInput:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface PreUpdate_input{
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface PreUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
   RequiresUserInput:boolean,
}
}

   /** Required : 
      @param iLineNum
      @param ds
   */  
export interface ResetMYIndustryCode_input{
      /**  Journal Line Number  */  
   iLineNum:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface ResetMYIndustryCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param iLineNum
      @param ds
   */  
export interface SetDefaultsForTaxLine_input{
      /**  Journal Line Number  */  
   iLineNum:number,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface SetDefaultsForTaxLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param ds
      @param iLineNum
      @param dAmountInBookCurr
      @param dAmountInTranCurr
   */  
export interface UpdateAmountForTaxLine_input{
   ds:Erp_Tablesets_GLJournalEntryTableset[],
      /**  Journal Line Number  */  
   iLineNum:number,
      /**  Line amount in book currency.  */  
   dAmountInBookCurr:number,
      /**  Line amount in transactional currency.  */  
   dAmountInTranCurr:number,
}

export interface UpdateAmountForTaxLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtGLJournalEntryTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtGLJournalEntryTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

   /** Required : 
      @param ipCOACode
      @param ipSegValue1
   */  
export interface ValidateAccountForAllocation_input{
      /**  COACode  */  
   ipCOACode:string,
      /**  SegValue1  */  
   ipSegValue1:string,
}

export interface ValidateAccountForAllocation_output{
}

   /** Required : 
      @param ipCOACode
      @param ipSegValue1
   */  
export interface ValidateAccountForStatJournal_input{
      /**  COACode  */  
   ipCOACode:string,
      /**  SegValue1  */  
   ipSegValue1:string,
}

export interface ValidateAccountForStatJournal_output{
}

   /** Required : 
      @param ds
      @param ipCurrency
      @param lineNum
   */  
export interface ValidateCurrencyAccount_input{
   ds:Erp_Tablesets_GLJournalEntryTableset[],
      /**  The proposed Currency value  */  
   ipCurrency:string,
      /**  Lournal Line  */  
   lineNum:number,
}

export interface ValidateCurrencyAccount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
   message:string,
}
}

   /** Required : 
      @param ipVoidedReason
      @param ds
   */  
export interface VoidLegalNumber_input{
      /**  Reason for the void  */  
   ipVoidedReason:string,
   ds:Erp_Tablesets_GLJournalEntryTableset[],
}

export interface VoidLegalNumber_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJournalEntryTableset,
}
}

