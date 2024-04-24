import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.FASpreadCodeSvc
// Description: FASpreadCode Service
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/$metadata", {
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
   Description: Get FASpreadCodes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FASpreadCodes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FASpreadRow
   */  
export function get_FASpreadCodes(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FASpreadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/FASpreadCodes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FASpreadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FASpreadCodes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FASpreadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FASpreadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FASpreadCodes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/FASpreadCodes", {
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
   Summary: Calls GetByID to retrieve the FASpreadCode item
   Description: Calls GetByID to retrieve the FASpreadCode item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FASpreadCode
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SpreadCode Desc: SpreadCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FASpreadRow
   */  
export function get_FASpreadCodes_Company_SpreadCode(Company:string, SpreadCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FASpreadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/FASpreadCodes(" + Company + "," + SpreadCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FASpreadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FASpreadCode for the service
   Description: Calls UpdateExt to update FASpreadCode. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FASpreadCode
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SpreadCode Desc: SpreadCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FASpreadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FASpreadCodes_Company_SpreadCode(Company:string, SpreadCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/FASpreadCodes(" + Company + "," + SpreadCode + ")", {
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
   Summary: Call UpdateExt to delete FASpreadCode item
   Description: Call UpdateExt to delete FASpreadCode item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FASpreadCode
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SpreadCode Desc: SpreadCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FASpreadCodes_Company_SpreadCode(Company:string, SpreadCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/FASpreadCodes(" + Company + "," + SpreadCode + ")", {
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
   Description: Get FASprdDies items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FASprdDies1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SpreadCode Desc: SpreadCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FASprdDyRow
   */  
export function get_FASpreadCodes_Company_SpreadCode_FASprdDies(Company:string, SpreadCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FASprdDyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/FASpreadCodes(" + Company + "," + SpreadCode + ")/FASprdDies", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FASprdDyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FASprdDy item
   Description: Calls GetByID to retrieve the FASprdDy item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FASprdDy1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SpreadCode Desc: SpreadCode   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FASprdDyRow
   */  
export function get_FASpreadCodes_Company_SpreadCode_FASprdDies_Company_SpreadCode_FiscalYear_FiscalYearSuffix_FiscalPeriod_FiscalCalendarID(Company:string, SpreadCode:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, FiscalCalendarID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FASprdDyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/FASpreadCodes(" + Company + "," + SpreadCode + ")/FASprdDies(" + Company + "," + SpreadCode + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + FiscalCalendarID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FASprdDyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get FASprdDies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FASprdDies
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FASprdDyRow
   */  
export function get_FASprdDies(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FASprdDyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/FASprdDies", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FASprdDyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FASprdDies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FASprdDyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FASprdDyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FASprdDies(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/FASprdDies", {
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
   Summary: Calls GetByID to retrieve the FASprdDy item
   Description: Calls GetByID to retrieve the FASprdDy item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FASprdDy
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SpreadCode Desc: SpreadCode   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FASprdDyRow
   */  
export function get_FASprdDies_Company_SpreadCode_FiscalYear_FiscalYearSuffix_FiscalPeriod_FiscalCalendarID(Company:string, SpreadCode:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, FiscalCalendarID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FASprdDyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/FASprdDies(" + Company + "," + SpreadCode + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + FiscalCalendarID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FASprdDyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FASprdDy for the service
   Description: Calls UpdateExt to update FASprdDy. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FASprdDy
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SpreadCode Desc: SpreadCode   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FASprdDyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FASprdDies_Company_SpreadCode_FiscalYear_FiscalYearSuffix_FiscalPeriod_FiscalCalendarID(Company:string, SpreadCode:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, FiscalCalendarID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/FASprdDies(" + Company + "," + SpreadCode + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + FiscalCalendarID + ")", {
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
   Summary: Call UpdateExt to delete FASprdDy item
   Description: Call UpdateExt to delete FASprdDy item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FASprdDy
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SpreadCode Desc: SpreadCode   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FASprdDies_Company_SpreadCode_FiscalYear_FiscalYearSuffix_FiscalPeriod_FiscalCalendarID(Company:string, SpreadCode:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, FiscalCalendarID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/FASprdDies(" + Company + "," + SpreadCode + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + FiscalCalendarID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FASpreadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FASpreadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FASpreadListRow)
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
export function get_GetRows(whereClauseFASpread:string, whereClauseFASprdDy:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseFASpread!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFASpread=" + whereClauseFASpread
   }
   if(typeof whereClauseFASprdDy!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFASprdDy=" + whereClauseFASprdDy
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/GetRows" + params, {
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
export function get_GetByID(spreadCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof spreadCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "spreadCode=" + spreadCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/GetList" + params, {
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
   Summary: Invoke method DeleteFASprdDy
   Description: This is to delete ttFASprdDy record based on the SpreadCode, Fiscal Year and Period.
   OperationID: DeleteFASprdDy
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteFASprdDy_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteFASprdDy_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteFASprdDy(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/DeleteFASprdDy", {
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
   Summary: Invoke method ExportSpreadCode
   Description: Exports the Spread Code data to a CSV file.
   OperationID: ExportSpreadCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportSpreadCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportSpreadCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportSpreadCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/ExportSpreadCode", {
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
   Summary: Invoke method GenerateSprdDy
   Description: This procedure is to generate ttFASprdDy records based on the Spread Type and
the parameters entered by the user in the Generate Values form.
   OperationID: GenerateSprdDy
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateSprdDy_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateSprdDy_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateSprdDy(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/GenerateSprdDy", {
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
   Summary: Invoke method GetSelectList
   Description: Get list of descriptions for the Export combos.
   OperationID: GetSelectList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/GetSelectList", {
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
   Description: Get Code Desc List
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/GetCodeDescList", {
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
   Summary: Invoke method ImportSpreadCode
   Description: Imports the Spread Code data from a CSV file.
   OperationID: ImportSpreadCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportSpreadCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportSpreadCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportSpreadCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/ImportSpreadCode", {
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
   Summary: Invoke method SetDefaultsForGenerate
   Description: This procedure sets the Defalut values of the Parameters in the Generate Values form.
   OperationID: SetDefaultsForGenerate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetDefaultsForGenerate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetDefaultsForGenerate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetDefaultsForGenerate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/SetDefaultsForGenerate", {
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
   Summary: Invoke method ImportCall
   Description: Import Call
   OperationID: ImportCall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportCall(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/ImportCall", {
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
   Summary: Invoke method ExportCall
   Description: Export Call
   OperationID: ExportCall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportCall(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/ExportCall", {
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
   Summary: Invoke method GetNewFASpread
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFASpread
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFASpread_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFASpread_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFASpread(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/GetNewFASpread", {
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
   Summary: Invoke method GetNewFASprdDy
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFASprdDy
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFASprdDy_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFASprdDy_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFASprdDy(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/GetNewFASprdDy", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FASprdDyRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FASprdDyRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FASpreadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FASpreadListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FASpreadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FASpreadRow[],
}

export interface Erp_Tablesets_FASprdDyRow{
      /**  Company of the spread code spread days.  */  
   "Company":string,
      /**  Identifier of the spread code table.  */  
   "SpreadCode":string,
      /**  Fiscal year of the spread code.  */  
   "FiscalYear":number,
      /**  Fiscal period of the spread day.  */  
   "FiscalPeriod":number,
      /**  Day factor. The factor is used to calculate the fiscal periods depreciation amount from the year depreciation amount. When there are 200 working days in a year and 15 working days in a fiscal period then the depreciation amount of the fiscal period is 15 / 200 * year depreciation amount.  */  
   "Days":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  This could be the number of days, annual charge, period charge or any value that will be used to calculate the fiscal periods depreciation amount. This factor could be used in multiple scenarios but one common usage would be to calculate period depreciations from the year depreciation amount. When there are 200 working days in a year and 15 working days in a fiscal period then the depreciation amount of the fiscal period is 15 / 200 * year depreciation amount.  */  
   "SpreadValue":number,
      /**  Marks this FASprdDy as global, available to be sent out to other companies.  */  
   "GlobalFASprdDy":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "StartDate":string,
   "EndDate":string,
   "BitFlag":number,
   "SpreadCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FASpreadListRow{
      /**  Company of the spread code table.  */  
   "Company":string,
      /**  identifier of the spread code table.  */  
   "SpreadCode":string,
      /**  Description of the spread code.  */  
   "Description":string,
      /**  Identifies the type of Spread Code.  This will define whether the spread will be done over years or periods.  Valid values are: "PERIOD" or "ANNUAL"  */  
   "SpreadType":string,
      /**  Identifies the Asset Calendar used when posting asset activities.  */  
   "CalendarID":string,
      /**  Marks this FASpread as global, available to be sent out to other companies.  */  
   "GlobalFASpread":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Parameter for Spread Code Entry Generate Values to determine how the detail values are going to be generated. Valid values are: "NUMDAYS", "PROAMT" or NOTASSIGN.  */  
   "AssignValues":string,
      /**  Parameter for Spread Code Entry Generate Values that contains the amount entered by the user that is going to be prorated.  */  
   "AssignedValue":number,
      /**  Start Year parameter for Spread Code Entry Generate Values  */  
   "StartYear":number,
      /**  Start Year Suffix parameter for Spread Code Entry Generate Values  */  
   "StartYearSuffix":string,
      /**  End Year parameter for Spread Code Entry Generate Values  */  
   "EndYear":number,
      /**  End Year Suffix parameter for Spread Code Entry Generate Values  */  
   "EndYearSuffix":string,
      /**  Parameter for Spread Code Entry Generate Values that indicates if the already existin values are going to be overridden.  */  
   "OverrideValues":boolean,
      /**  Calendar description.  */  
   "FiscalCalDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FASpreadRow{
      /**  Company of the spread code table.  */  
   "Company":string,
      /**  identifier of the spread code table.  */  
   "SpreadCode":string,
      /**  Description of the spread code.  */  
   "Description":string,
      /**  Identifies the type of Spread Code.  This will define whether the spread will be done over years or periods.  Valid values are: "PERIOD" or "ANNUAL"  */  
   "SpreadType":string,
      /**  Identifies the Asset Calendar used when posting asset activities.  */  
   "CalendarID":string,
      /**  Marks this FASpread as global, available to be sent out to other companies.  */  
   "GlobalFASpread":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Parameter for Spread Code Entry Generate Values to determine how the detail values are going to be generated. Valid values are: "NUMDAYS", "PROAMT" or NOTASSIGN.  */  
   "AssignValues":string,
      /**  Parameter for Spread Code Entry Generate Values that contains the amount entered by the user that is going to be prorated.  */  
   "AssignedValue":number,
      /**  Start Year parameter for Spread Code Entry Generate Values  */  
   "StartYear":number,
      /**  Start Year Suffix parameter for Spread Code Entry Generate Values  */  
   "StartYearSuffix":string,
      /**  End Year parameter for Spread Code Entry Generate Values  */  
   "EndYear":number,
      /**  End Year Suffix parameter for Spread Code Entry Generate Values  */  
   "EndYearSuffix":string,
      /**  Parameter for Spread Code Entry Generate Values that indicates if the already existin values are going to be overridden.  */  
   "OverrideValues":boolean,
   "BitFlag":number,
   "FiscalCalDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param spreadCode
   */  
export interface DeleteByID_input{
   spreadCode:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param spreadCode
      @param fiscalYear
      @param fiscalYearSuffix
      @param fiscalPeriod
      @param ds
   */  
export interface DeleteFASprdDy_input{
      /**  SpreadCode of record that is being updated.  */  
   spreadCode:string,
      /**  FiscalYear of record that is being updated.  */  
   fiscalYear:number,
      /**  FiscalYearSuffix of record that is being updated.  */  
   fiscalYearSuffix:string,
      /**  FiscalPeriod of record that is being updated.  */  
   fiscalPeriod:number,
   ds:Erp_Tablesets_FASpreadCodeTableset[],
}

export interface DeleteFASprdDy_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FASpreadCodeTableset[],
}
}

export interface Erp_Tablesets_FASprdDyRow{
      /**  Company of the spread code spread days.  */  
   Company:string,
      /**  Identifier of the spread code table.  */  
   SpreadCode:string,
      /**  Fiscal year of the spread code.  */  
   FiscalYear:number,
      /**  Fiscal period of the spread day.  */  
   FiscalPeriod:number,
      /**  Day factor. The factor is used to calculate the fiscal periods depreciation amount from the year depreciation amount. When there are 200 working days in a year and 15 working days in a fiscal period then the depreciation amount of the fiscal period is 15 / 200 * year depreciation amount.  */  
   Days:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  This could be the number of days, annual charge, period charge or any value that will be used to calculate the fiscal periods depreciation amount. This factor could be used in multiple scenarios but one common usage would be to calculate period depreciations from the year depreciation amount. When there are 200 working days in a year and 15 working days in a fiscal period then the depreciation amount of the fiscal period is 15 / 200 * year depreciation amount.  */  
   SpreadValue:number,
      /**  Marks this FASprdDy as global, available to be sent out to other companies.  */  
   GlobalFASprdDy:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   StartDate:string,
   EndDate:string,
   BitFlag:number,
   SpreadCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FASpreadCodeTableset{
   FASpread:Erp_Tablesets_FASpreadRow[],
   FASprdDy:Erp_Tablesets_FASprdDyRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FASpreadImExDataTableset{
   FaSprdDyImEx:Erp_Tablesets_FaSprdDyImExRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FASpreadListRow{
      /**  Company of the spread code table.  */  
   Company:string,
      /**  identifier of the spread code table.  */  
   SpreadCode:string,
      /**  Description of the spread code.  */  
   Description:string,
      /**  Identifies the type of Spread Code.  This will define whether the spread will be done over years or periods.  Valid values are: "PERIOD" or "ANNUAL"  */  
   SpreadType:string,
      /**  Identifies the Asset Calendar used when posting asset activities.  */  
   CalendarID:string,
      /**  Marks this FASpread as global, available to be sent out to other companies.  */  
   GlobalFASpread:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Parameter for Spread Code Entry Generate Values to determine how the detail values are going to be generated. Valid values are: "NUMDAYS", "PROAMT" or NOTASSIGN.  */  
   AssignValues:string,
      /**  Parameter for Spread Code Entry Generate Values that contains the amount entered by the user that is going to be prorated.  */  
   AssignedValue:number,
      /**  Start Year parameter for Spread Code Entry Generate Values  */  
   StartYear:number,
      /**  Start Year Suffix parameter for Spread Code Entry Generate Values  */  
   StartYearSuffix:string,
      /**  End Year parameter for Spread Code Entry Generate Values  */  
   EndYear:number,
      /**  End Year Suffix parameter for Spread Code Entry Generate Values  */  
   EndYearSuffix:string,
      /**  Parameter for Spread Code Entry Generate Values that indicates if the already existin values are going to be overridden.  */  
   OverrideValues:boolean,
      /**  Calendar description.  */  
   FiscalCalDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FASpreadListTableset{
   FASpreadList:Erp_Tablesets_FASpreadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FASpreadRow{
      /**  Company of the spread code table.  */  
   Company:string,
      /**  identifier of the spread code table.  */  
   SpreadCode:string,
      /**  Description of the spread code.  */  
   Description:string,
      /**  Identifies the type of Spread Code.  This will define whether the spread will be done over years or periods.  Valid values are: "PERIOD" or "ANNUAL"  */  
   SpreadType:string,
      /**  Identifies the Asset Calendar used when posting asset activities.  */  
   CalendarID:string,
      /**  Marks this FASpread as global, available to be sent out to other companies.  */  
   GlobalFASpread:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Parameter for Spread Code Entry Generate Values to determine how the detail values are going to be generated. Valid values are: "NUMDAYS", "PROAMT" or NOTASSIGN.  */  
   AssignValues:string,
      /**  Parameter for Spread Code Entry Generate Values that contains the amount entered by the user that is going to be prorated.  */  
   AssignedValue:number,
      /**  Start Year parameter for Spread Code Entry Generate Values  */  
   StartYear:number,
      /**  Start Year Suffix parameter for Spread Code Entry Generate Values  */  
   StartYearSuffix:string,
      /**  End Year parameter for Spread Code Entry Generate Values  */  
   EndYear:number,
      /**  End Year Suffix parameter for Spread Code Entry Generate Values  */  
   EndYearSuffix:string,
      /**  Parameter for Spread Code Entry Generate Values that indicates if the already existin values are going to be overridden.  */  
   OverrideValues:boolean,
   BitFlag:number,
   FiscalCalDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FaSprdDyImExRow{
      /**  Company of the spread code spread days.  */  
   Company:string,
      /**  Identifier of the spread code table.  */  
   SpreadCode:string,
      /**  Fiscal year of the spread code.  */  
   FiscalYear:number,
      /**  Fiscal period of the spread day.  */  
   FiscalPeriod:number,
      /**  Day factor. The factor is used to calculate the fiscal periods depreciation amount from the year depreciation amount. When there are 200 working days in a year and 15 working days in a fiscal period then the depreciation amount of the fiscal period is 15 / 200 * year depreciation amount.  */  
   Days:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  This could be the number of days, annual charge, period charge or any value that will be used to calculate the fiscal periods depreciation amount. This factor could be used in multiple scenarios but one common usage would be to calculate period depreciations from the year depreciation amount. When there are 200 working days in a year and 15 working days in a fiscal period then the depreciation amount of the fiscal period is 15 / 200 * year depreciation amount.  */  
   SpreadValue:number,
      /**  Marks this FASprdDy as global, available to be sent out to other companies.  */  
   GlobalFASprdDy:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Identifies the type of Spread Code.  This will define whether the spread will be done over years or periods.  Valid values are: "PERIOD" or "YEAR"  */  
   SpreadType:string,
      /**  Description of the spread code.  */  
   Description:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtFASpreadCodeTableset{
   FASpread:Erp_Tablesets_FASpreadRow[],
   FASprdDy:Erp_Tablesets_FASprdDyRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param fileName
      @param inStartCode
      @param inEndCode
      @param inSelectBy
      @param inSelectType
   */  
export interface ExportCall_input{
   fileName:string,
   inStartCode:string,
   inEndCode:string,
   inSelectBy:string,
   inSelectType:string,
}

export interface ExportCall_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   msg:string,
}
}

   /** Required : 
      @param inStartCode
      @param inEndCode
      @param inSelectBy
      @param inSelectType
   */  
export interface ExportSpreadCode_input{
      /**  Starting Spread Code  */  
   inStartCode:string,
      /**  Ending Spread Code  */  
   inEndCode:string,
      /**  Select By option  */  
   inSelectBy:string,
      /**  Select Type option  */  
   inSelectType:string,
}

export interface ExportSpreadCode_output{
   returnObj:Erp_Tablesets_FASpreadImExDataTableset[],
}

   /** Required : 
      @param iPSpreadCode
      @param ds
   */  
export interface GenerateSprdDy_input{
      /**  SpreadCode of record that is being updated.  */  
   iPSpreadCode:string,
   ds:Erp_Tablesets_FASpreadCodeTableset[],
}

export interface GenerateSprdDy_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FASpreadCodeTableset[],
}
}

   /** Required : 
      @param spreadCode
   */  
export interface GetByID_input{
   spreadCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_FASpreadCodeTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_FASpreadCodeTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_FASpreadCodeTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
      /**  Table Name  */  
   tableName:string,
      /**  Field Name  */  
   fieldName:string,
}

export interface GetCodeDescList_output{
      /**  Code Description List  */  
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
   returnObj:Erp_Tablesets_FASpreadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param spreadCode
      @param fiscalYear
      @param fiscalYearSuffix
      @param fiscalPeriod
   */  
export interface GetNewFASprdDy_input{
   ds:Erp_Tablesets_FASpreadCodeTableset[],
   spreadCode:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   fiscalPeriod:number,
}

export interface GetNewFASprdDy_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FASpreadCodeTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewFASpread_input{
   ds:Erp_Tablesets_FASpreadCodeTableset[],
}

export interface GetNewFASpread_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FASpreadCodeTableset[],
}
}

   /** Required : 
      @param whereClauseFASpread
      @param whereClauseFASprdDy
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseFASpread:string,
   whereClauseFASprdDy:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_FASpreadCodeTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param inListType
   */  
export interface GetSelectList_input{
      /**  The type of list that is going to be returned  */  
   inListType:string,
}

export interface GetSelectList_output{
parameters : {
      /**  output parameters  */  
   selectList:string,
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
      @param fileName
   */  
export interface ImportCall_input{
   fileName:string,
}

export interface ImportCall_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   allImported:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface ImportSpreadCode_input{
   ds:Erp_Tablesets_FASpreadImExDataTableset[],
}

export interface ImportSpreadCode_output{
   returnObj:Erp_Tablesets_FASpreadCodeTableset[],
parameters : {
      /**  output parameters  */  
   allImported:boolean,
   ds:Erp_Tablesets_FASpreadImExDataTableset[],
}
}

   /** Required : 
      @param inCalendarID
      @param inSpreadType
   */  
export interface SetDefaultsForGenerate_input{
      /**  Fiscal Calendar ID  */  
   inCalendarID:string,
      /**  Spread Code Type  */  
   inSpreadType:string,
}

export interface SetDefaultsForGenerate_output{
parameters : {
      /**  output parameters  */  
   outCurrYear:number,
   outCurrYearSuffix:string,
   outLastYear:number,
   outLastYearSuffix:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtFASpreadCodeTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtFASpreadCodeTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_FASpreadCodeTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FASpreadCodeTableset[],
}
}

