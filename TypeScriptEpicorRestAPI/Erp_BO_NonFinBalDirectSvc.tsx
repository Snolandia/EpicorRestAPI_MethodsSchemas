import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.NonFinBalDirectSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/$metadata", {
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
   Description: Get NonFinBalDirects items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_NonFinBalDirects
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnHedRow
   */  
export function get_NonFinBalDirects(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/NonFinBalDirects", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   OperationID: NewUpdateExt_NonFinBalDirects
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJrnHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLJrnHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NonFinBalDirects(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/NonFinBalDirects", {
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
   Summary: Calls GetByID to retrieve the NonFinBalDirect item
   Description: Calls GetByID to retrieve the NonFinBalDirect item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_NonFinBalDirect
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLJrnHedRow
   */  
export function get_NonFinBalDirects_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, FiscalCalendarID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLJrnHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/NonFinBalDirects(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GLJrnHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update NonFinBalDirect for the service
   Description: Calls UpdateExt to update NonFinBalDirect. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_NonFinBalDirect
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJrnHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_NonFinBalDirects_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, FiscalCalendarID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/NonFinBalDirects(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")", {
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
   Summary: Call UpdateExt to delete NonFinBalDirect item
   Description: Call UpdateExt to delete NonFinBalDirect item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_NonFinBalDirect
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_NonFinBalDirects_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, FiscalCalendarID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/NonFinBalDirects(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")", {
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
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlMnlRow
   */  
export function get_NonFinBalDirects_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID_GLJrnDtlMnls(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, FiscalCalendarID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/NonFinBalDirects(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")/GLJrnDtlMnls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlRow
   */  
export function get_NonFinBalDirects_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, FiscalCalendarID:string, JournalLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLJrnDtlMnlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/NonFinBalDirects(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Get GLJrnDtlMnlSims items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLJrnDtlMnlSims1
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlMnlSimRow
   */  
export function get_NonFinBalDirects_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID_GLJrnDtlMnlSims(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, FiscalCalendarID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlSimRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/NonFinBalDirects(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")/GLJrnDtlMnlSims", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlSimRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the GLJrnDtlMnlSim item
   Description: Calls GetByID to retrieve the GLJrnDtlMnlSim item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlMnlSim1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param JournalLine Desc: JournalLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlSimRow
   */  
export function get_NonFinBalDirects_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID_GLJrnDtlMnlSims_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, FiscalCalendarID:string, JournalLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLJrnDtlMnlSimRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/NonFinBalDirects(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")/GLJrnDtlMnlSims(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GLJrnDtlMnlSimRow)
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
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlMnlRow
   */  
export function get_GLJrnDtlMnls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GLJrnDtlMnls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLJrnDtlMnls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GLJrnDtlMnls", {
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
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlRow
   */  
export function get_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, FiscalCalendarID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLJrnDtlMnlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, FiscalCalendarID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")", {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")", {
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
   Description: Get GLJrnDtlMnlSims items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLJrnDtlMnlSims
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlMnlSimRow
   */  
export function get_GLJrnDtlMnlSims(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlSimRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GLJrnDtlMnlSims", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlSimRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLJrnDtlMnlSims
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlSimRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlSimRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLJrnDtlMnlSims(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GLJrnDtlMnlSims", {
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
   Summary: Calls GetByID to retrieve the GLJrnDtlMnlSim item
   Description: Calls GetByID to retrieve the GLJrnDtlMnlSim item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlMnlSim
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlSimRow
   */  
export function get_GLJrnDtlMnlSims_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, FiscalCalendarID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLJrnDtlMnlSimRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GLJrnDtlMnlSims(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GLJrnDtlMnlSimRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLJrnDtlMnlSim for the service
   Description: Calls UpdateExt to update GLJrnDtlMnlSim. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLJrnDtlMnlSim
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlSimRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLJrnDtlMnlSims_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, FiscalCalendarID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GLJrnDtlMnlSims(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")", {
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
   Summary: Call UpdateExt to delete GLJrnDtlMnlSim item
   Description: Call UpdateExt to delete GLJrnDtlMnlSim item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLJrnDtlMnlSim
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLJrnDtlMnlSims_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, FiscalCalendarID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GLJrnDtlMnlSims(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnHedListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnHedListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnHedListRow)
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
export function get_GetRows(whereClauseGLJrnHed:string, whereClauseGLJrnDtlMnl:string, whereClauseGLJrnDtlMnlSim:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
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
   if(typeof whereClauseGLJrnDtlMnl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLJrnDtlMnl=" + whereClauseGLJrnDtlMnl
   }
   if(typeof whereClauseGLJrnDtlMnlSim!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLJrnDtlMnlSim=" + whereClauseGLJrnDtlMnlSim
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GetRows" + params, {
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
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GetList" + params, {
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
   Summary: Invoke method GetNewGLJrnDtlMnlSim
   OperationID: GetNewGLJrnDtlMnlSim
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnDtlMnlSim_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnDtlMnlSim_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLJrnDtlMnlSim(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GetNewGLJrnDtlMnlSim", {
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
   Summary: Invoke method GetJournal
   Description: This method is called in place of the GetByID method, requiring only the
the GL Group ID.
   OperationID: GetJournal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJournal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJournal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetJournal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GetJournal", {
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
   Description: Method to call to get a Code Description list.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GetCodeDescList", {
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
   Summary: Invoke method OnChangeGLAccount
   OperationID: OnChangeGLAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeGLAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeGLAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeGLAccount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/OnChangeGLAccount", {
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
   Summary: Invoke method OnFormClose
   Description: Delete stat rows with zero amounts
   OperationID: OnFormClose
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnFormClose_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnFormClose_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnFormClose(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/OnFormClose", {
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
   Summary: Invoke method GetNewGLJrnDtlMnl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLJrnDtlMnl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnDtlMnl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnDtlMnl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLJrnDtlMnl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GetNewGLJrnDtlMnl", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLJrnDtlMnlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlSimRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLJrnDtlMnlSimRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnHedListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLJrnHedListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnHedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLJrnHedRow[],
}

export interface Erp_Tablesets_GLJrnDtlMnlRow{
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

export interface Erp_Tablesets_GLJrnDtlMnlSimRow{
   "Company":string,
   "GLAccount":string,
   "CurrStatBalance":number,
   "NewStatBalance":number,
   "StatUOMCode":string,
   "StatUOMDesc":string,
   "Reverse":boolean,
   "BookID":string,
   "JournalNum":number,
   "JournalLine":number,
   "JournalCode":string,
   "FiscalYear":number,
   "FiscalYearSuffix":string,
   "FiscalCalendarID":string,
   "COACode":string,
   "GLAccountDesc":string,
   "SegValue1":string,
   "Statistical":number,
   "GroupID":string,
   "JEDate":string,
   "SegValue2":string,
   "SegValue3":string,
   "SegValue4":string,
   "SegValue5":string,
   "SegValue6":string,
   "SegValue7":string,
   "SegValue8":string,
   "SegValue9":string,
   "SegValue10":string,
   "SegValue11":string,
   "SegValue12":string,
   "SegValue13":string,
   "SegValue14":string,
   "SegValue15":string,
   "SegValue16":string,
   "SegValue17":string,
   "SegValue18":string,
   "SegValue19":string,
   "SegValue20":string,
   "Description":string,
   "CreateDate":string,
   "FiscalPeriod":number,
   "CloseFiscalPeriod":number,
   "CurrencyCode":string,
      /**  Means this line is agglutinate from many lines with the same GL Account. Uses in statistical logic.  */  
   "Summarized":boolean,
   "SysRowID":string,
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




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
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

export interface Erp_Tablesets_GLJrnDtlMnlSimRow{
   Company:string,
   GLAccount:string,
   CurrStatBalance:number,
   NewStatBalance:number,
   StatUOMCode:string,
   StatUOMDesc:string,
   Reverse:boolean,
   BookID:string,
   JournalNum:number,
   JournalLine:number,
   JournalCode:string,
   FiscalYear:number,
   FiscalYearSuffix:string,
   FiscalCalendarID:string,
   COACode:string,
   GLAccountDesc:string,
   SegValue1:string,
   Statistical:number,
   GroupID:string,
   JEDate:string,
   SegValue2:string,
   SegValue3:string,
   SegValue4:string,
   SegValue5:string,
   SegValue6:string,
   SegValue7:string,
   SegValue8:string,
   SegValue9:string,
   SegValue10:string,
   SegValue11:string,
   SegValue12:string,
   SegValue13:string,
   SegValue14:string,
   SegValue15:string,
   SegValue16:string,
   SegValue17:string,
   SegValue18:string,
   SegValue19:string,
   SegValue20:string,
   Description:string,
   CreateDate:string,
   FiscalPeriod:number,
   CloseFiscalPeriod:number,
   CurrencyCode:string,
      /**  Means this line is agglutinate from many lines with the same GL Account. Uses in statistical logic.  */  
   Summarized:boolean,
   SysRowID:string,
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

export interface Erp_Tablesets_NonFinBalDirectTableset{
   GLJrnHed:Erp_Tablesets_GLJrnHedRow[],
   GLJrnDtlMnl:Erp_Tablesets_GLJrnDtlMnlRow[],
   GLJrnDtlMnlSim:Erp_Tablesets_GLJrnDtlMnlSimRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtNonFinBalDirectTableset{
   GLJrnHed:Erp_Tablesets_GLJrnHedRow[],
   GLJrnDtlMnl:Erp_Tablesets_GLJrnDtlMnlRow[],
   GLJrnDtlMnlSim:Erp_Tablesets_GLJrnDtlMnlSimRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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
   returnObj:Erp_Tablesets_NonFinBalDirectTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_NonFinBalDirectTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_NonFinBalDirectTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
      /**  The table name  */  
   tableName:string,
      /**  The field name.  */  
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param groupID
      @param journalNum
   */  
export interface GetJournal_input{
   groupID:string,
   journalNum:number,
}

export interface GetJournal_output{
   returnObj:Erp_Tablesets_NonFinBalDirectTableset[],
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
   */  
export interface GetNewGLJrnDtlMnlSim_input{
   ds:Erp_Tablesets_NonFinBalDirectTableset[],
   bookID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   journalCode:string,
   journalNum:number,
   journalLine:number,
}

export interface GetNewGLJrnDtlMnlSim_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonFinBalDirectTableset[],
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
   ds:Erp_Tablesets_NonFinBalDirectTableset[],
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
   ds:Erp_Tablesets_NonFinBalDirectTableset[],
}
}

   /** Required : 
      @param whereClauseGLJrnHed
      @param whereClauseGLJrnDtlMnl
      @param whereClauseGLJrnDtlMnlSim
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseGLJrnHed:string,
   whereClauseGLJrnDtlMnl:string,
   whereClauseGLJrnDtlMnlSim:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_NonFinBalDirectTableset[],
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
      @param glAccount
      @param ds
   */  
export interface OnChangeGLAccount_input{
   glAccount:string,
   ds:Erp_Tablesets_NonFinBalDirectTableset[],
}

export interface OnChangeGLAccount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonFinBalDirectTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnFormClose_input{
   ds:Erp_Tablesets_NonFinBalDirectTableset[],
}

export interface OnFormClose_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonFinBalDirectTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtNonFinBalDirectTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtNonFinBalDirectTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_NonFinBalDirectTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NonFinBalDirectTableset[],
}
}

