import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.AccountBudgetSvc
// Description: class AccountBudgetSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/$metadata", {
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
   Description: Get AccountBudgets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AccountBudgets
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBudgetHdRow
   */  
export function get_AccountBudgets(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBudgetHdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/AccountBudgets", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBudgetHdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AccountBudgets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLBudgetHdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLBudgetHdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AccountBudgets(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/AccountBudgets", {
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
   Summary: Calls GetByID to retrieve the AccountBudget item
   Description: Calls GetByID to retrieve the AccountBudget item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AccountBudget
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param BalanceAcct Desc: BalanceAcct   Required: True   Allow empty value : True
      @param BalanceType Desc: BalanceType   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param BudgetCodeID Desc: BudgetCodeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBudgetHdRow
   */  
export function get_AccountBudgets_Company_BookID_BalanceAcct_BalanceType_FiscalYear_FiscalYearSuffix_FiscalCalendarID_BudgetCodeID(Company:string, BookID:string, BalanceAcct:string, BalanceType:string, FiscalYear:string, FiscalYearSuffix:string, FiscalCalendarID:string, BudgetCodeID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLBudgetHdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/AccountBudgets(" + Company + "," + BookID + "," + BalanceAcct + "," + BalanceType + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalCalendarID + "," + BudgetCodeID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GLBudgetHdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AccountBudget for the service
   Description: Calls UpdateExt to update AccountBudget. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AccountBudget
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param BalanceAcct Desc: BalanceAcct   Required: True   Allow empty value : True
      @param BalanceType Desc: BalanceType   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param BudgetCodeID Desc: BudgetCodeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLBudgetHdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AccountBudgets_Company_BookID_BalanceAcct_BalanceType_FiscalYear_FiscalYearSuffix_FiscalCalendarID_BudgetCodeID(Company:string, BookID:string, BalanceAcct:string, BalanceType:string, FiscalYear:string, FiscalYearSuffix:string, FiscalCalendarID:string, BudgetCodeID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/AccountBudgets(" + Company + "," + BookID + "," + BalanceAcct + "," + BalanceType + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalCalendarID + "," + BudgetCodeID + ")", {
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
   Summary: Call UpdateExt to delete AccountBudget item
   Description: Call UpdateExt to delete AccountBudget item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AccountBudget
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param BalanceAcct Desc: BalanceAcct   Required: True   Allow empty value : True
      @param BalanceType Desc: BalanceType   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param BudgetCodeID Desc: BudgetCodeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AccountBudgets_Company_BookID_BalanceAcct_BalanceType_FiscalYear_FiscalYearSuffix_FiscalCalendarID_BudgetCodeID(Company:string, BookID:string, BalanceAcct:string, BalanceType:string, FiscalYear:string, FiscalYearSuffix:string, FiscalCalendarID:string, BudgetCodeID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/AccountBudgets(" + Company + "," + BookID + "," + BalanceAcct + "," + BalanceType + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalCalendarID + "," + BudgetCodeID + ")", {
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
   Description: Get GLBudgetDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLBudgetDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param BalanceAcct Desc: BalanceAcct   Required: True   Allow empty value : True
      @param BalanceType Desc: BalanceType   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param BudgetCodeID Desc: BudgetCodeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBudgetDtlRow
   */  
export function get_AccountBudgets_Company_BookID_BalanceAcct_BalanceType_FiscalYear_FiscalYearSuffix_FiscalCalendarID_BudgetCodeID_GLBudgetDtls(Company:string, BookID:string, BalanceAcct:string, BalanceType:string, FiscalYear:string, FiscalYearSuffix:string, FiscalCalendarID:string, BudgetCodeID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBudgetDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/AccountBudgets(" + Company + "," + BookID + "," + BalanceAcct + "," + BalanceType + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalCalendarID + "," + BudgetCodeID + ")/GLBudgetDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBudgetDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the GLBudgetDtl item
   Description: Calls GetByID to retrieve the GLBudgetDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBudgetDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param BalanceAcct Desc: BalanceAcct   Required: True   Allow empty value : True
      @param BalanceType Desc: BalanceType   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param BudgetCodeID Desc: BudgetCodeID   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBudgetDtlRow
   */  
export function get_AccountBudgets_Company_BookID_BalanceAcct_BalanceType_FiscalYear_FiscalYearSuffix_FiscalCalendarID_BudgetCodeID_GLBudgetDtls_Company_BookID_BalanceAcct_BalanceType_FiscalYear_FiscalYearSuffix_FiscalPeriod_FiscalCalendarID_BudgetCodeID(Company:string, BookID:string, BalanceAcct:string, BalanceType:string, FiscalYear:string, FiscalYearSuffix:string, FiscalCalendarID:string, BudgetCodeID:string, FiscalPeriod:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLBudgetDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/AccountBudgets(" + Company + "," + BookID + "," + BalanceAcct + "," + BalanceType + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalCalendarID + "," + BudgetCodeID + ")/GLBudgetDtls(" + Company + "," + BookID + "," + BalanceAcct + "," + BalanceType + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + FiscalCalendarID + "," + BudgetCodeID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GLBudgetDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get GLBudgetDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLBudgetDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBudgetDtlRow
   */  
export function get_GLBudgetDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBudgetDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/GLBudgetDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBudgetDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLBudgetDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLBudgetDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLBudgetDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLBudgetDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/GLBudgetDtls", {
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
   Summary: Calls GetByID to retrieve the GLBudgetDtl item
   Description: Calls GetByID to retrieve the GLBudgetDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBudgetDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param BalanceAcct Desc: BalanceAcct   Required: True   Allow empty value : True
      @param BalanceType Desc: BalanceType   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param BudgetCodeID Desc: BudgetCodeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBudgetDtlRow
   */  
export function get_GLBudgetDtls_Company_BookID_BalanceAcct_BalanceType_FiscalYear_FiscalYearSuffix_FiscalPeriod_FiscalCalendarID_BudgetCodeID(Company:string, BookID:string, BalanceAcct:string, BalanceType:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, FiscalCalendarID:string, BudgetCodeID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLBudgetDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/GLBudgetDtls(" + Company + "," + BookID + "," + BalanceAcct + "," + BalanceType + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + FiscalCalendarID + "," + BudgetCodeID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GLBudgetDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLBudgetDtl for the service
   Description: Calls UpdateExt to update GLBudgetDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLBudgetDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param BalanceAcct Desc: BalanceAcct   Required: True   Allow empty value : True
      @param BalanceType Desc: BalanceType   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param BudgetCodeID Desc: BudgetCodeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLBudgetDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLBudgetDtls_Company_BookID_BalanceAcct_BalanceType_FiscalYear_FiscalYearSuffix_FiscalPeriod_FiscalCalendarID_BudgetCodeID(Company:string, BookID:string, BalanceAcct:string, BalanceType:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, FiscalCalendarID:string, BudgetCodeID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/GLBudgetDtls(" + Company + "," + BookID + "," + BalanceAcct + "," + BalanceType + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + FiscalCalendarID + "," + BudgetCodeID + ")", {
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
   Summary: Call UpdateExt to delete GLBudgetDtl item
   Description: Call UpdateExt to delete GLBudgetDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLBudgetDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param BalanceAcct Desc: BalanceAcct   Required: True   Allow empty value : True
      @param BalanceType Desc: BalanceType   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param BudgetCodeID Desc: BudgetCodeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLBudgetDtls_Company_BookID_BalanceAcct_BalanceType_FiscalYear_FiscalYearSuffix_FiscalPeriod_FiscalCalendarID_BudgetCodeID(Company:string, BookID:string, BalanceAcct:string, BalanceType:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, FiscalCalendarID:string, BudgetCodeID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/GLBudgetDtls(" + Company + "," + BookID + "," + BalanceAcct + "," + BalanceType + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + FiscalCalendarID + "," + BudgetCodeID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBudgetHdListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBudgetHdListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBudgetHdListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseGLBudgetHd:string, whereClauseGLBudgetDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseGLBudgetHd!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLBudgetHd=" + whereClauseGLBudgetHd
   }
   if(typeof whereClauseGLBudgetDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLBudgetDtl=" + whereClauseGLBudgetDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(bookID:string, balanceAcct:string, balanceType:string, fiscalYear:string, fiscalYearSuffix:string, fiscalCalendarID:string, budgetCodeID:string, epicorHeaders?:Headers){
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
   if(typeof fiscalCalendarID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "fiscalCalendarID=" + fiscalCalendarID
   }
   if(typeof budgetCodeID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "budgetCodeID=" + budgetCodeID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/GetList" + params, {
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
   Summary: Invoke method GetNewGLBudgetHdEx
   Description: GetNewGLBudgetHd with all key parameters
   OperationID: GetNewGLBudgetHdEx
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLBudgetHdEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLBudgetHdEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLBudgetHdEx(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/GetNewGLBudgetHdEx", {
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
   Summary: Invoke method DeleteBudget
   Description: This method deletes the entire Budget of a valid fiscal year.
   OperationID: DeleteBudget
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteBudget_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteBudget_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteBudget(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/DeleteBudget", {
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
   Summary: Invoke method ChangeDtlBudgetAmt
   Description: This method updates the DispTotalBudgetAmt and the BudgetAmt of the GLBudgetHd
when the GLBudgetDtl.BudgetAmt changes.
   OperationID: ChangeDtlBudgetAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlBudgetAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlBudgetAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDtlBudgetAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/ChangeDtlBudgetAmt", {
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
   Summary: Invoke method ChangeDtlBudgetStatAmt
   Description: This method updates the DispTotalBudgetStatAmt and the BudgetStatAmt of the GLBudgetHd
when the GLBudgetDtl.BudgetStatAmt changes.
   OperationID: ChangeDtlBudgetStatAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlBudgetStatAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlBudgetStatAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDtlBudgetStatAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/ChangeDtlBudgetStatAmt", {
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
   Summary: Invoke method ChangePerCodeOrAmount
   Description: This method updates the DispTotalBudgetAmt when the BudgetPerCode or BudgetAmt or BudgetStatAmt changes.
   OperationID: ChangePerCodeOrAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePerCodeOrAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePerCodeOrAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePerCodeOrAmount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/ChangePerCodeOrAmount", {
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
   Summary: Invoke method ChangeBalanceAcct
   Description: This method updates the StatUOM information when BalanceAcct is changed.
   OperationID: ChangeBalanceAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBalanceAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBalanceAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeBalanceAcct(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/ChangeBalanceAcct", {
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
   Summary: Invoke method ValidateGLAccount
   Description: Validate account and budget
   OperationID: ValidateGLAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateGLAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateGLAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateGLAccount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/ValidateGLAccount", {
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
   Summary: Invoke method ValidateGLBook
   Description: ValidateGLBook
   OperationID: ValidateGLBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateGLBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateGLBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateGLBook(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/ValidateGLBook", {
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
   Summary: Invoke method ValidateBudgetCode
   Description: Validate BudgetCode
   OperationID: ValidateBudgetCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateBudgetCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBudgetCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateBudgetCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/ValidateBudgetCode", {
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
   Summary: Invoke method GetTargetBudgetCode
   Description: Return target budget code
   OperationID: GetTargetBudgetCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTargetBudgetCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTargetBudgetCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTargetBudgetCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/GetTargetBudgetCode", {
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
   Summary: Invoke method GetNewGLBudgetHd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLBudgetHd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLBudgetHd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLBudgetHd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLBudgetHd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/GetNewGLBudgetHd", {
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
   Summary: Invoke method GetNewGLBudgetDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLBudgetDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLBudgetDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLBudgetDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLBudgetDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/GetNewGLBudgetDtl", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBudgetDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLBudgetDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBudgetHdListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLBudgetHdListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBudgetHdRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLBudgetHdRow[],
}

export interface Erp_Tablesets_GLBudgetDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  GLBook ID  */  
   "BookID":string,
      /**  The budget GL Account.  Only balance accounts can have a budget.  */  
   "BalanceAcct":string,
      /**  Identifies the type of balance stored on this record.  S = Summary Balance.  D = Detail Balance.  B = Both a Summary and Detail Balance.  */  
   "BalanceType":string,
      /**  The fiscal year of this period balance record  */  
   "FiscalYear":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal period number in the fiscal year.  */  
   "FiscalPeriod":number,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Identifier of Budget Code  */  
   "BudgetCodeID":string,
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
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Budget amount.  Credits are negative,  Debits are positive.  */  
   "BudgetAmt":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Budget statistical amount.  Credits are negative,  Debits are positive.  */  
   "BudgetStatAmt":number,
   "CurrencyCode":string,
   "BitFlag":number,
   "BudgetCodeInactive":boolean,
   "BudgetCodeIsDefault":boolean,
   "BudgetCodeBudgetCodeDesc":string,
   "GLAcctDispGLAcctDisp":string,
   "GLAcctDispGLShortAcct":string,
   "GLAcctDispAccountDesc":string,
   "GLBookCurrencyCode":string,
   "GLBookDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLBudgetHdListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  GLBook ID  */  
   "BookID":string,
      /**  The budget GL Account.  Only balance accounts can have a budget.  */  
   "BalanceAcct":string,
      /**  Identifies the type of balance stored on this record.  S = Summary Balance.  D = Detail Balance.  B = Both a Summary and Detail Balance.  */  
   "BalanceType":string,
      /**  The fiscal year of this period balance record  */  
   "FiscalYear":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Identifier of Budget Code  */  
   "BudgetCodeID":string,
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
      /**  Total Budget amount for the fiscal year.  This is a summary of GLBudgetDtl.BudgetAmt. Indirectly maintained via GLBudgetDtl write trigger.  Credits are negative,  Debits are positive.  */  
   "TotalBudgetAmt":number,
      /**  Indicates if the budget amount is period or annual amount.  */  
   "BudgetPerCode":string,
      /**  Whether or not to include in the Cash Flow Analysis  .  */  
   "CashFlow":boolean,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  */  
   "PerBalFmt":string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  */  
   "TBBalFmt":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BudgetAmt":number,
   "DispTotalBudgetAmt":number,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   "GLAcctDispGLAcctDisp":string,
      /**  Optional field that may be used for reporting purpose when the GL Account exceeds the space available on a printed document.  It is a shortened version of the 200 character GL Account that displays on reports.  The value of this field is the concatenation of the first three controlled display order segments.  For example, if a chart has 5 controlled segments that are displayed in the following order: seg5->seg3->seg4->seg2->seg1, this field contains the concatention of seg5->seg3->seg4 up to th  */  
   "GLAcctDispGLShortAcct":string,
      /**  Text that describes the account.  */  
   "GLAcctDispAccountDesc":string,
      /**  Indicates the base currency for the book  */  
   "GLBookCurrencyCode":string,
      /**  Descripiton of Book  */  
   "GLBookDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLBudgetHdRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  GLBook ID  */  
   "BookID":string,
      /**  The budget GL Account.  Only balance accounts can have a budget.  */  
   "BalanceAcct":string,
      /**  Identifies the type of balance stored on this record.  S = Summary Balance.  D = Detail Balance.  B = Both a Summary and Detail Balance.  */  
   "BalanceType":string,
      /**  The fiscal year of this period balance record  */  
   "FiscalYear":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Identifier of Budget Code  */  
   "BudgetCodeID":string,
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
      /**  Total Budget amount for the fiscal year.  This is a summary of GLBudgetDtl.BudgetAmt. Indirectly maintained via GLBudgetDtl write trigger.  Credits are negative,  Debits are positive.  */  
   "TotalBudgetAmt":number,
      /**  Indicates if the budget amount is period or annual amount.  */  
   "BudgetPerCode":string,
      /**  Whether or not to include in the Cash Flow Analysis  .  */  
   "CashFlow":boolean,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  */  
   "PerBalFmt":string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  */  
   "TBBalFmt":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Total Budget Statistical amount for the fiscal year.  This is a summary of GLBudgetDtl.BudgetStatAmt. Indirectly maintained via GLBudgetDtl write trigger.  Credits are negative,  Debits are positive.  */  
   "TotalBudgetStatAmt":number,
   "BudgetStatAmt":number,
   "CurrencyCode":string,
   "DispTotalBudgetAmt":number,
   "DispTotalBudgetStatAmt":number,
   "Statistical":number,
   "StatUOMCode":string,
   "StatUOMDesc":string,
   "StatUOMNumOfDec":number,
   "BudgetAmt":number,
   "TreeViewField":string,
   "BitFlag":number,
   "BudgetCodeInactive":boolean,
   "BudgetCodeBudgetCodeDesc":string,
   "BudgetCodeIsDefault":boolean,
   "GLAcctDispGLShortAcct":string,
   "GLAcctDispAccountDesc":string,
   "GLAcctDispGLAcctDisp":string,
   "GLBookDescription":string,
   "GLBookCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ds
   */  
export interface ChangeBalanceAcct_input{
   ds:Erp_Tablesets_AccountBudgetTableset[],
}

export interface ChangeBalanceAcct_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AccountBudgetTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeDtlBudgetAmt_input{
   ds:Erp_Tablesets_AccountBudgetTableset[],
}

export interface ChangeDtlBudgetAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AccountBudgetTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeDtlBudgetStatAmt_input{
   ds:Erp_Tablesets_AccountBudgetTableset[],
}

export interface ChangeDtlBudgetStatAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AccountBudgetTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangePerCodeOrAmount_input{
   ds:Erp_Tablesets_AccountBudgetTableset[],
}

export interface ChangePerCodeOrAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AccountBudgetTableset[],
}
}

   /** Required : 
      @param inpBookID
      @param inpBudgetCodeID
      @param inpFiscalYear
      @param inpFiscalYearSuffix
   */  
export interface DeleteBudget_input{
      /**  The Book ID of the Budget to delete.  */  
   inpBookID:string,
      /**  The Budget Code ID of the Budget to delete.  */  
   inpBudgetCodeID:string,
      /**  The Fiscal Year of the Budget to delete.  */  
   inpFiscalYear:number,
      /**  The Fiscal Year Suffix of the Budget to delete.  */  
   inpFiscalYearSuffix:string,
}

export interface DeleteBudget_output{
   returnObj:Erp_Tablesets_AccountBudgetTableset[],
}

   /** Required : 
      @param bookID
      @param balanceAcct
      @param balanceType
      @param fiscalYear
      @param fiscalYearSuffix
      @param fiscalCalendarID
      @param budgetCodeID
   */  
export interface DeleteByID_input{
   bookID:string,
   balanceAcct:string,
   balanceType:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   fiscalCalendarID:string,
   budgetCodeID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_AccountBudgetTableset{
   GLBudgetHd:Erp_Tablesets_GLBudgetHdRow[],
   GLBudgetDtl:Erp_Tablesets_GLBudgetDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GLBudgetDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  GLBook ID  */  
   BookID:string,
      /**  The budget GL Account.  Only balance accounts can have a budget.  */  
   BalanceAcct:string,
      /**  Identifies the type of balance stored on this record.  S = Summary Balance.  D = Detail Balance.  B = Both a Summary and Detail Balance.  */  
   BalanceType:string,
      /**  The fiscal year of this period balance record  */  
   FiscalYear:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal period number in the fiscal year.  */  
   FiscalPeriod:number,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Identifier of Budget Code  */  
   BudgetCodeID:string,
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
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Budget amount.  Credits are negative,  Debits are positive.  */  
   BudgetAmt:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Budget statistical amount.  Credits are negative,  Debits are positive.  */  
   BudgetStatAmt:number,
   CurrencyCode:string,
   BitFlag:number,
   BudgetCodeInactive:boolean,
   BudgetCodeIsDefault:boolean,
   BudgetCodeBudgetCodeDesc:string,
   GLAcctDispGLAcctDisp:string,
   GLAcctDispGLShortAcct:string,
   GLAcctDispAccountDesc:string,
   GLBookCurrencyCode:string,
   GLBookDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLBudgetHdListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  GLBook ID  */  
   BookID:string,
      /**  The budget GL Account.  Only balance accounts can have a budget.  */  
   BalanceAcct:string,
      /**  Identifies the type of balance stored on this record.  S = Summary Balance.  D = Detail Balance.  B = Both a Summary and Detail Balance.  */  
   BalanceType:string,
      /**  The fiscal year of this period balance record  */  
   FiscalYear:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Identifier of Budget Code  */  
   BudgetCodeID:string,
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
      /**  Total Budget amount for the fiscal year.  This is a summary of GLBudgetDtl.BudgetAmt. Indirectly maintained via GLBudgetDtl write trigger.  Credits are negative,  Debits are positive.  */  
   TotalBudgetAmt:number,
      /**  Indicates if the budget amount is period or annual amount.  */  
   BudgetPerCode:string,
      /**  Whether or not to include in the Cash Flow Analysis  .  */  
   CashFlow:boolean,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  */  
   PerBalFmt:string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  */  
   TBBalFmt:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BudgetAmt:number,
   DispTotalBudgetAmt:number,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   GLAcctDispGLAcctDisp:string,
      /**  Optional field that may be used for reporting purpose when the GL Account exceeds the space available on a printed document.  It is a shortened version of the 200 character GL Account that displays on reports.  The value of this field is the concatenation of the first three controlled display order segments.  For example, if a chart has 5 controlled segments that are displayed in the following order: seg5->seg3->seg4->seg2->seg1, this field contains the concatention of seg5->seg3->seg4 up to th  */  
   GLAcctDispGLShortAcct:string,
      /**  Text that describes the account.  */  
   GLAcctDispAccountDesc:string,
      /**  Indicates the base currency for the book  */  
   GLBookCurrencyCode:string,
      /**  Descripiton of Book  */  
   GLBookDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLBudgetHdListTableset{
   GLBudgetHdList:Erp_Tablesets_GLBudgetHdListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GLBudgetHdRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  GLBook ID  */  
   BookID:string,
      /**  The budget GL Account.  Only balance accounts can have a budget.  */  
   BalanceAcct:string,
      /**  Identifies the type of balance stored on this record.  S = Summary Balance.  D = Detail Balance.  B = Both a Summary and Detail Balance.  */  
   BalanceType:string,
      /**  The fiscal year of this period balance record  */  
   FiscalYear:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Identifier of Budget Code  */  
   BudgetCodeID:string,
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
      /**  Total Budget amount for the fiscal year.  This is a summary of GLBudgetDtl.BudgetAmt. Indirectly maintained via GLBudgetDtl write trigger.  Credits are negative,  Debits are positive.  */  
   TotalBudgetAmt:number,
      /**  Indicates if the budget amount is period or annual amount.  */  
   BudgetPerCode:string,
      /**  Whether or not to include in the Cash Flow Analysis  .  */  
   CashFlow:boolean,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  */  
   PerBalFmt:string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  */  
   TBBalFmt:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Total Budget Statistical amount for the fiscal year.  This is a summary of GLBudgetDtl.BudgetStatAmt. Indirectly maintained via GLBudgetDtl write trigger.  Credits are negative,  Debits are positive.  */  
   TotalBudgetStatAmt:number,
   BudgetStatAmt:number,
   CurrencyCode:string,
   DispTotalBudgetAmt:number,
   DispTotalBudgetStatAmt:number,
   Statistical:number,
   StatUOMCode:string,
   StatUOMDesc:string,
   StatUOMNumOfDec:number,
   BudgetAmt:number,
   TreeViewField:string,
   BitFlag:number,
   BudgetCodeInactive:boolean,
   BudgetCodeBudgetCodeDesc:string,
   BudgetCodeIsDefault:boolean,
   GLAcctDispGLShortAcct:string,
   GLAcctDispAccountDesc:string,
   GLAcctDispGLAcctDisp:string,
   GLBookDescription:string,
   GLBookCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtAccountBudgetTableset{
   GLBudgetHd:Erp_Tablesets_GLBudgetHdRow[],
   GLBudgetDtl:Erp_Tablesets_GLBudgetDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param bookID
      @param balanceAcct
      @param balanceType
      @param fiscalYear
      @param fiscalYearSuffix
      @param fiscalCalendarID
      @param budgetCodeID
   */  
export interface GetByID_input{
   bookID:string,
   balanceAcct:string,
   balanceType:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   fiscalCalendarID:string,
   budgetCodeID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_AccountBudgetTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_AccountBudgetTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_AccountBudgetTableset[],
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
   returnObj:Erp_Tablesets_GLBudgetHdListTableset[],
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
      @param fiscalCalendarID
   */  
export interface GetNewGLBudgetDtl_input{
   ds:Erp_Tablesets_AccountBudgetTableset[],
   bookID:string,
   balanceAcct:string,
   balanceType:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   fiscalPeriod:number,
   fiscalCalendarID:string,
}

export interface GetNewGLBudgetDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AccountBudgetTableset[],
}
}

   /** Required : 
      @param ds
      @param bookID
      @param balanceAcct
      @param balanceType
      @param fiscalYear
      @param fiscalYearSuffix
      @param fiscalCalendarID
      @param budgetCodeID
   */  
export interface GetNewGLBudgetHdEx_input{
   ds:Erp_Tablesets_AccountBudgetTableset[],
   bookID:string,
   balanceAcct:string,
   balanceType:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   fiscalCalendarID:string,
   budgetCodeID:string,
}

export interface GetNewGLBudgetHdEx_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AccountBudgetTableset[],
}
}

   /** Required : 
      @param ds
      @param bookID
      @param balanceAcct
      @param balanceType
      @param fiscalYear
      @param fiscalYearSuffix
      @param fiscalCalendarID
   */  
export interface GetNewGLBudgetHd_input{
   ds:Erp_Tablesets_AccountBudgetTableset[],
   bookID:string,
   balanceAcct:string,
   balanceType:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   fiscalCalendarID:string,
}

export interface GetNewGLBudgetHd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AccountBudgetTableset[],
}
}

   /** Required : 
      @param whereClauseGLBudgetHd
      @param whereClauseGLBudgetDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseGLBudgetHd:string,
   whereClauseGLBudgetDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_AccountBudgetTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param sourceBudget
   */  
export interface GetTargetBudgetCode_input{
      /**  Source Budget Code  */  
   sourceBudget:string,
}

export interface GetTargetBudgetCode_output{
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
   ds:Erp_Tablesets_UpdExtAccountBudgetTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtAccountBudgetTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_AccountBudgetTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AccountBudgetTableset[],
}
}

   /** Required : 
      @param budgetCode
      @param throwEx
   */  
export interface ValidateBudgetCode_input{
   budgetCode:string,
   throwEx:boolean,
}

export interface ValidateBudgetCode_output{
}

   /** Required : 
      @param bookID
      @param budgetCodeID
      @param account
      @param balanceType
      @param fiscalYear
      @param fiscalYearSuffix
      @param budgetAmt
      @param budgetStatAmt
   */  
export interface ValidateGLAccount_input{
      /**  Book ID  */  
   bookID:string,
      /**  Budget Code ID  */  
   budgetCodeID:string,
      /**  New value Balance Account  */  
   account:string,
      /**  Balance Type  */  
   balanceType:string,
      /**  Fiscal Year  */  
   fiscalYear:number,
      /**  Fiscal Year Suffix  */  
   fiscalYearSuffix:string,
      /**  Current Budget Amount  */  
   budgetAmt:number,
      /**  Current Budget Statistical Amount  */  
   budgetStatAmt:number,
}

export interface ValidateGLAccount_output{
}

   /** Required : 
      @param bookID
   */  
export interface ValidateGLBook_input{
      /**  bookID  */  
   bookID:string,
}

export interface ValidateGLBook_output{
}

