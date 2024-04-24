import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.EmpBasicSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/$metadata", {
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
   Description: Get EmpBasics items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EmpBasics
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpBasicRow
   */  
export function get_EmpBasics(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpBasicRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpBasicRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EmpBasics
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpBasicRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EmpBasicRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EmpBasics(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics", {
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
   Summary: Calls GetByID to retrieve the EmpBasic item
   Description: Calls GetByID to retrieve the EmpBasic item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpBasic
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpBasicRow
   */  
export function get_EmpBasics_Company_EmpID(Company:string, EmpID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EmpBasicRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EmpBasicRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EmpBasic for the service
   Description: Calls UpdateExt to update EmpBasic. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EmpBasic
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpBasicRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EmpBasics_Company_EmpID(Company:string, EmpID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")", {
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
   Summary: Call UpdateExt to delete EmpBasic item
   Description: Call UpdateExt to delete EmpBasic item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EmpBasic
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EmpBasics_Company_EmpID(Company:string, EmpID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")", {
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
   Description: Get EmpLabExpRates items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EmpLabExpRates1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpLabExpRateRow
   */  
export function get_EmpBasics_Company_EmpID_EmpLabExpRates(Company:string, EmpID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpLabExpRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")/EmpLabExpRates", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpLabExpRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EmpLabExpRate item
   Description: Calls GetByID to retrieve the EmpLabExpRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpLabExpRate1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param ExpenseCode Desc: ExpenseCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpLabExpRateRow
   */  
export function get_EmpBasics_Company_EmpID_EmpLabExpRates_Company_EmpID_ExpenseCode(Company:string, EmpID:string, ExpenseCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EmpLabExpRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")/EmpLabExpRates(" + Company + "," + EmpID + "," + ExpenseCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EmpLabExpRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get EmpCals items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EmpCals1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpCalRow
   */  
export function get_EmpBasics_Company_EmpID_EmpCals(Company:string, EmpID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpCalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")/EmpCals", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpCalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EmpCal item
   Description: Calls GetByID to retrieve the EmpCal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpCal1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param FromEffectiveDate Desc: FromEffectiveDate   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpCalRow
   */  
export function get_EmpBasics_Company_EmpID_EmpCals_Company_EmpID_CalendarID_FromEffectiveDate(Company:string, EmpID:string, CalendarID:string, FromEffectiveDate:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EmpCalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")/EmpCals(" + Company + "," + EmpID + "," + CalendarID + "," + FromEffectiveDate + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EmpCalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ResourceCals items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ResourceCals1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ResourceCalRow
   */  
export function get_EmpBasics_Company_EmpID_ResourceCals(Company:string, EmpID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceCalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")/ResourceCals", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceCalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ResourceCal item
   Description: Calls GetByID to retrieve the ResourceCal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ResourceCal1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param SpecialDay Desc: SpecialDay   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ResourceCalRow
   */  
export function get_EmpBasics_Company_EmpID_ResourceCals_Company_ResourceGrpID_ResourceID_SpecialDay(Company:string, EmpID:string, ResourceGrpID:string, ResourceID:string, SpecialDay:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ResourceCalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")/ResourceCals(" + Company + "," + ResourceGrpID + "," + ResourceID + "," + SpecialDay + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ResourceCalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get EmpRoles items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EmpRoles1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpRoleRow
   */  
export function get_EmpBasics_Company_EmpID_EmpRoles(Company:string, EmpID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpRoleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")/EmpRoles", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpRoleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EmpRole item
   Description: Calls GetByID to retrieve the EmpRole item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpRole1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param RoleCd Desc: RoleCd   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpRoleRow
   */  
export function get_EmpBasics_Company_EmpID_EmpRoles_Company_EmpID_RoleCd(Company:string, EmpID:string, RoleCd:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EmpRoleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")/EmpRoles(" + Company + "," + EmpID + "," + RoleCd + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EmpRoleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   */  
export function get_EmpBasics_Company_EmpID_EntityGLCs(Company:string, EmpID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")/EntityGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   */  
export function get_EmpBasics_Company_EmpID_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, EmpID:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get EmpBasicAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EmpBasicAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpBasicAttchRow
   */  
export function get_EmpBasics_Company_EmpID_EmpBasicAttches(Company:string, EmpID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpBasicAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")/EmpBasicAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpBasicAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EmpBasicAttch item
   Description: Calls GetByID to retrieve the EmpBasicAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpBasicAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpBasicAttchRow
   */  
export function get_EmpBasics_Company_EmpID_EmpBasicAttches_Company_EmpID_DrawingSeq(Company:string, EmpID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EmpBasicAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasics(" + Company + "," + EmpID + ")/EmpBasicAttches(" + Company + "," + EmpID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EmpBasicAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get EmpLabExpRates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EmpLabExpRates
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpLabExpRateRow
   */  
export function get_EmpLabExpRates(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpLabExpRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpLabExpRates", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpLabExpRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EmpLabExpRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpLabExpRateRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EmpLabExpRateRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EmpLabExpRates(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpLabExpRates", {
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
   Summary: Calls GetByID to retrieve the EmpLabExpRate item
   Description: Calls GetByID to retrieve the EmpLabExpRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpLabExpRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param ExpenseCode Desc: ExpenseCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpLabExpRateRow
   */  
export function get_EmpLabExpRates_Company_EmpID_ExpenseCode(Company:string, EmpID:string, ExpenseCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EmpLabExpRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpLabExpRates(" + Company + "," + EmpID + "," + ExpenseCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EmpLabExpRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EmpLabExpRate for the service
   Description: Calls UpdateExt to update EmpLabExpRate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EmpLabExpRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param ExpenseCode Desc: ExpenseCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpLabExpRateRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EmpLabExpRates_Company_EmpID_ExpenseCode(Company:string, EmpID:string, ExpenseCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpLabExpRates(" + Company + "," + EmpID + "," + ExpenseCode + ")", {
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
   Summary: Call UpdateExt to delete EmpLabExpRate item
   Description: Call UpdateExt to delete EmpLabExpRate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EmpLabExpRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param ExpenseCode Desc: ExpenseCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EmpLabExpRates_Company_EmpID_ExpenseCode(Company:string, EmpID:string, ExpenseCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpLabExpRates(" + Company + "," + EmpID + "," + ExpenseCode + ")", {
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
   Description: Get EmpCals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EmpCals
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpCalRow
   */  
export function get_EmpCals(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpCalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpCals", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpCalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EmpCals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpCalRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EmpCalRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EmpCals(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpCals", {
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
   Summary: Calls GetByID to retrieve the EmpCal item
   Description: Calls GetByID to retrieve the EmpCal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpCal
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param FromEffectiveDate Desc: FromEffectiveDate   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpCalRow
   */  
export function get_EmpCals_Company_EmpID_CalendarID_FromEffectiveDate(Company:string, EmpID:string, CalendarID:string, FromEffectiveDate:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EmpCalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpCals(" + Company + "," + EmpID + "," + CalendarID + "," + FromEffectiveDate + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EmpCalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EmpCal for the service
   Description: Calls UpdateExt to update EmpCal. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EmpCal
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param FromEffectiveDate Desc: FromEffectiveDate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpCalRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EmpCals_Company_EmpID_CalendarID_FromEffectiveDate(Company:string, EmpID:string, CalendarID:string, FromEffectiveDate:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpCals(" + Company + "," + EmpID + "," + CalendarID + "," + FromEffectiveDate + ")", {
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
   Summary: Call UpdateExt to delete EmpCal item
   Description: Call UpdateExt to delete EmpCal item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EmpCal
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param FromEffectiveDate Desc: FromEffectiveDate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EmpCals_Company_EmpID_CalendarID_FromEffectiveDate(Company:string, EmpID:string, CalendarID:string, FromEffectiveDate:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpCals(" + Company + "," + EmpID + "," + CalendarID + "," + FromEffectiveDate + ")", {
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
   Description: Get ResourceCals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ResourceCals
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ResourceCalRow
   */  
export function get_ResourceCals(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceCalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/ResourceCals", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceCalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ResourceCals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ResourceCalRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ResourceCalRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ResourceCals(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/ResourceCals", {
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
   Summary: Calls GetByID to retrieve the ResourceCal item
   Description: Calls GetByID to retrieve the ResourceCal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ResourceCal
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param SpecialDay Desc: SpecialDay   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ResourceCalRow
   */  
export function get_ResourceCals_Company_ResourceGrpID_ResourceID_SpecialDay(Company:string, ResourceGrpID:string, ResourceID:string, SpecialDay:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ResourceCalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/ResourceCals(" + Company + "," + ResourceGrpID + "," + ResourceID + "," + SpecialDay + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ResourceCalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ResourceCal for the service
   Description: Calls UpdateExt to update ResourceCal. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ResourceCal
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param SpecialDay Desc: SpecialDay   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ResourceCalRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ResourceCals_Company_ResourceGrpID_ResourceID_SpecialDay(Company:string, ResourceGrpID:string, ResourceID:string, SpecialDay:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/ResourceCals(" + Company + "," + ResourceGrpID + "," + ResourceID + "," + SpecialDay + ")", {
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
   Summary: Call UpdateExt to delete ResourceCal item
   Description: Call UpdateExt to delete ResourceCal item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ResourceCal
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param SpecialDay Desc: SpecialDay   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ResourceCals_Company_ResourceGrpID_ResourceID_SpecialDay(Company:string, ResourceGrpID:string, ResourceID:string, SpecialDay:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/ResourceCals(" + Company + "," + ResourceGrpID + "," + ResourceID + "," + SpecialDay + ")", {
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
   Description: Get EmpRoles items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EmpRoles
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpRoleRow
   */  
export function get_EmpRoles(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpRoleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpRoles", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpRoleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EmpRoles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpRoleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EmpRoleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EmpRoles(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpRoles", {
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
   Summary: Calls GetByID to retrieve the EmpRole item
   Description: Calls GetByID to retrieve the EmpRole item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpRole
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param RoleCd Desc: RoleCd   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpRoleRow
   */  
export function get_EmpRoles_Company_EmpID_RoleCd(Company:string, EmpID:string, RoleCd:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EmpRoleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpRoles(" + Company + "," + EmpID + "," + RoleCd + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EmpRoleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EmpRole for the service
   Description: Calls UpdateExt to update EmpRole. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EmpRole
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param RoleCd Desc: RoleCd   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpRoleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EmpRoles_Company_EmpID_RoleCd(Company:string, EmpID:string, RoleCd:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpRoles(" + Company + "," + EmpID + "," + RoleCd + ")", {
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
   Summary: Call UpdateExt to delete EmpRole item
   Description: Call UpdateExt to delete EmpRole item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EmpRole
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param RoleCd Desc: RoleCd   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EmpRoles_Company_EmpID_RoleCd(Company:string, EmpID:string, RoleCd:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpRoles(" + Company + "," + EmpID + "," + RoleCd + ")", {
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
   Description: Get EntityGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EntityGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   */  
export function get_EntityGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EntityGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EntityGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EntityGLCs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EntityGLCs", {
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
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   */  
export function get_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EntityGLC for the service
   Description: Calls UpdateExt to update EntityGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Summary: Call UpdateExt to delete EntityGLC item
   Description: Call UpdateExt to delete EntityGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Description: Get EmpBasicAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EmpBasicAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpBasicAttchRow
   */  
export function get_EmpBasicAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpBasicAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasicAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpBasicAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EmpBasicAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpBasicAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EmpBasicAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EmpBasicAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasicAttches", {
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
   Summary: Calls GetByID to retrieve the EmpBasicAttch item
   Description: Calls GetByID to retrieve the EmpBasicAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpBasicAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpBasicAttchRow
   */  
export function get_EmpBasicAttches_Company_EmpID_DrawingSeq(Company:string, EmpID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EmpBasicAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasicAttches(" + Company + "," + EmpID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EmpBasicAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EmpBasicAttch for the service
   Description: Calls UpdateExt to update EmpBasicAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EmpBasicAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpBasicAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EmpBasicAttches_Company_EmpID_DrawingSeq(Company:string, EmpID:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasicAttches(" + Company + "," + EmpID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete EmpBasicAttch item
   Description: Call UpdateExt to delete EmpBasicAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EmpBasicAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EmpBasicAttches_Company_EmpID_DrawingSeq(Company:string, EmpID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpBasicAttches(" + Company + "," + EmpID + "," + DrawingSeq + ")", {
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
   Description: Get Partners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Partners
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartnerRow
   */  
export function get_Partners(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartnerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/Partners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartnerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Partners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartnerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartnerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Partners(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/Partners", {
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
   Summary: Calls GetByID to retrieve the Partner item
   Description: Calls GetByID to retrieve the Partner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Partner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartnerNum Desc: PartnerNum   Required: True
      @param PartnerType Desc: PartnerType   Required: True
      @param PartnerID Desc: PartnerID   Required: True   Allow empty value : True
      @param SearchID Desc: SearchID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartnerRow
   */  
export function get_Partners_Company_PartnerNum_PartnerType_PartnerID_SearchID(Company:string, PartnerNum:string, PartnerType:string, PartnerID:string, SearchID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartnerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PartnerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Partner for the service
   Description: Calls UpdateExt to update Partner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Partner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartnerNum Desc: PartnerNum   Required: True
      @param PartnerType Desc: PartnerType   Required: True
      @param PartnerID Desc: PartnerID   Required: True   Allow empty value : True
      @param SearchID Desc: SearchID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartnerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Partners_Company_PartnerNum_PartnerType_PartnerID_SearchID(Company:string, PartnerNum:string, PartnerType:string, PartnerID:string, SearchID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")", {
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
   Summary: Call UpdateExt to delete Partner item
   Description: Call UpdateExt to delete Partner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Partner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartnerNum Desc: PartnerNum   Required: True
      @param PartnerType Desc: PartnerType   Required: True
      @param PartnerID Desc: PartnerID   Required: True   Allow empty value : True
      @param SearchID Desc: SearchID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Partners_Company_PartnerNum_PartnerType_PartnerID_SearchID(Company:string, PartnerNum:string, PartnerType:string, PartnerID:string, SearchID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")", {
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
   Description: Get EmpRoleRts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EmpRoleRts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpRoleRtRow
   */  
export function get_EmpRoleRts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpRoleRtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpRoleRts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpRoleRtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EmpRoleRts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpRoleRtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EmpRoleRtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EmpRoleRts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpRoleRts", {
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
   Summary: Calls GetByID to retrieve the EmpRoleRt item
   Description: Calls GetByID to retrieve the EmpRoleRt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpRoleRt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param RoleCd Desc: RoleCd   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpRoleRtRow
   */  
export function get_EmpRoleRts_Company_EmpID_RoleCd_Seq(Company:string, EmpID:string, RoleCd:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EmpRoleRtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpRoleRts(" + Company + "," + EmpID + "," + RoleCd + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EmpRoleRtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EmpRoleRt for the service
   Description: Calls UpdateExt to update EmpRoleRt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EmpRoleRt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param RoleCd Desc: RoleCd   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpRoleRtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EmpRoleRts_Company_EmpID_RoleCd_Seq(Company:string, EmpID:string, RoleCd:string, Seq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpRoleRts(" + Company + "," + EmpID + "," + RoleCd + "," + Seq + ")", {
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
   Summary: Call UpdateExt to delete EmpRoleRt item
   Description: Call UpdateExt to delete EmpRoleRt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EmpRoleRt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param RoleCd Desc: RoleCd   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EmpRoleRts_Company_EmpID_RoleCd_Seq(Company:string, EmpID:string, RoleCd:string, Seq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/EmpRoleRts(" + Company + "," + EmpID + "," + RoleCd + "," + Seq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpBasicListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpBasicListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpBasicListRow)
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
export function get_GetRows(whereClauseEmpBasic:string, whereClauseEmpBasicAttch:string, whereClauseEmpLabExpRate:string, whereClauseEmpCal:string, whereClausePartner:string, whereClauseResourceCal:string, whereClauseEmpRole:string, whereClauseEntityGLC:string, whereClauseEmpRoleRt:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseEmpBasic!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEmpBasic=" + whereClauseEmpBasic
   }
   if(typeof whereClauseEmpBasicAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEmpBasicAttch=" + whereClauseEmpBasicAttch
   }
   if(typeof whereClauseEmpLabExpRate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEmpLabExpRate=" + whereClauseEmpLabExpRate
   }
   if(typeof whereClauseEmpCal!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEmpCal=" + whereClauseEmpCal
   }
   if(typeof whereClausePartner!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartner=" + whereClausePartner
   }
   if(typeof whereClauseResourceCal!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseResourceCal=" + whereClauseResourceCal
   }
   if(typeof whereClauseEmpRole!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEmpRole=" + whereClauseEmpRole
   }
   if(typeof whereClauseEntityGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEntityGLC=" + whereClauseEntityGLC
   }
   if(typeof whereClauseEmpRoleRt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEmpRoleRt=" + whereClauseEmpRoleRt
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetRows" + params, {
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
export function get_GetByID(empID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof empID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "empID=" + empID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetList" + params, {
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
   Summary: Invoke method GetClientFileName
   OperationID: GetClientFileName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetClientFileName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetClientFileName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetClientFileName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetClientFileName", {
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
   Summary: Invoke method Mins2Int
   OperationID: Mins2Int
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Mins2Int_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Mins2Int_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Mins2Int(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/Mins2Int", {
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
   Summary: Invoke method Hours2Int
   OperationID: Hours2Int
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Hours2Int_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Hours2Int_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Hours2Int(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/Hours2Int", {
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
   Summary: Invoke method Date2Int
   OperationID: Date2Int
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Date2Int_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Date2Int_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Date2Int(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/Date2Int", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetCodeDescList", {
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
   Summary: Invoke method CheckShift
   Description: Check shift
   OperationID: CheckShift
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckShift_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckShift_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckShift(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/CheckShift", {
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
   Summary: Invoke method ClockIn
   Description: Clock In
   OperationID: ClockIn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClockIn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClockIn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClockIn(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/ClockIn", {
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
   Summary: Invoke method ClockOut
   Description: Clock Out
   OperationID: ClockOut
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClockOut_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClockOut_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClockOut(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/ClockOut", {
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
   Summary: Invoke method CustomizeResourceCal
   Description: This method will get a current ResourceCal record or create a temporary
ResourceCal record to be modified for a Employee.  The ProdHours will be
defaulted from the weekday of the selected date.  If any changes are made
to the ttResourceCal record, the UpdateResourceCal method will have to be
called to write the temporary ResourceCal record to the database.
   OperationID: CustomizeResourceCal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CustomizeResourceCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomizeResourceCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustomizeResourceCal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/CustomizeResourceCal", {
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
   Summary: Invoke method OnChangeWFGroup
   Description: Update the TaskSet fields according to the WF Group.
   OperationID: OnChangeWFGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWFGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWFGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeWFGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/OnChangeWFGroup", {
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
   Summary: Invoke method CheckClockInStatus
   Description: Called to check whether employee is clocked in and if so what shift they are clocked into.
   OperationID: CheckClockInStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckClockInStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckClockInStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckClockInStatus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/CheckClockInStatus", {
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
   Summary: Invoke method GetByIDForTE
   Description: Returns a DataSet given the primary key.  Contains special processing for
Time and Expense Entry.
   OperationID: GetByIDForTE
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDForTE_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDForTE_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDForTE(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetByIDForTE", {
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
   Summary: Invoke method GetByIDForTime
   Description: Returns a DataSet given the primary key.  Contains special processing for
Time Entry.
   OperationID: GetByIDForTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDForTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDForTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDForTime(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetByIDForTime", {
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
   Summary: Invoke method GetByIDForExpense
   Description: Returns a DataSet given the primary key.  Contains special processing for
Expense Entry.
   OperationID: GetByIDForExpense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDForExpense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDForExpense_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDForExpense(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetByIDForExpense", {
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
   Summary: Invoke method GetDefaultEmpID
   Description: Get Defaults Emp ID
   OperationID: GetDefaultEmpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultEmpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultEmpID(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetDefaultEmpID", {
          method: 'post',
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
   Summary: Invoke method GetListExpEmployees
   Description: Called to retrieve employees that can have expenses entered for them
   OperationID: GetListExpEmployees
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListExpEmployees_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListExpEmployees_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListExpEmployees(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetListExpEmployees", {
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
   Summary: Invoke method GetListForTE
   Description: Called to retrieve employees for Time and Expense Entry
   OperationID: GetListForTE
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForTE_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForTE_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListForTE(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetListForTE", {
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
   Summary: Invoke method GetListForExpense
   Description: Called to retrieve employees for Expense Entry
   OperationID: GetListForExpense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForExpense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForExpense_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListForExpense(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetListForExpense", {
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
   Summary: Invoke method GetListForTime
   Description: Called to retrieve employees for Time Entry
   OperationID: GetListForTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListForTime(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetListForTime", {
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
   Summary: Invoke method GetPerConData
   OperationID: GetPerConData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPerConData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPerConData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPerConData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetPerConData", {
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
   Summary: Invoke method GetRowsFromList
   Description: Get rows from list dataset
   OperationID: GetRowsFromList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsFromList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsFromList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsFromList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetRowsFromList", {
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
   Summary: Invoke method GetRowsWhoIsNotHere
   Description: Calls the normal GetRows method and then screens out only those employees who should be here but are not.
   OperationID: GetRowsWhoIsNotHere
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsWhoIsNotHere_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsWhoIsNotHere_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsWhoIsNotHere(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetRowsWhoIsNotHere", {
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
   Summary: Invoke method OnChangeCalendarID
   OperationID: OnChangeCalendarID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCalendarID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCalendarID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCalendarID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/OnChangeCalendarID", {
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
   Summary: Invoke method OnChangeCurrencyCode
   OperationID: OnChangeCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCurrencyCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/OnChangeCurrencyCode", {
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
   Summary: Invoke method OnChangeExpenseAllowed
   OperationID: OnChangeExpenseAllowed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeExpenseAllowed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeExpenseAllowed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeExpenseAllowed(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/OnChangeExpenseAllowed", {
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
   Summary: Invoke method OnChangeExpenseAutoApprove
   OperationID: OnChangeExpenseAutoApprove
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeExpenseAutoApprove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeExpenseAutoApprove_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeExpenseAutoApprove(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/OnChangeExpenseAutoApprove", {
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
   Summary: Invoke method OnChangeExpenseVendor
   OperationID: OnChangeExpenseVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeExpenseVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeExpenseVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeExpenseVendor(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/OnChangeExpenseVendor", {
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
   Summary: Invoke method OnChangeRateEffectiveDate
   OperationID: OnChangeRateEffectiveDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRateEffectiveDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRateEffectiveDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeRateEffectiveDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/OnChangeRateEffectiveDate", {
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
   Summary: Invoke method OnChangeRateEndDate
   OperationID: OnChangeRateEndDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRateEndDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRateEndDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeRateEndDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/OnChangeRateEndDate", {
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
   Summary: Invoke method OnChangeResource
   OperationID: OnChangeResource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeResource(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/OnChangeResource", {
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
   Summary: Invoke method OnChangeResourceGrp
   OperationID: OnChangeResourceGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeResourceGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeResourceGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeResourceGrp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/OnChangeResourceGrp", {
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
   Summary: Invoke method OnChangeRoleCd
   OperationID: OnChangeRoleCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRoleCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRoleCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeRoleCd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/OnChangeRoleCd", {
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
   Summary: Invoke method OnChangeTimeAutoApprove
   OperationID: OnChangeTimeAutoApprove
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTimeAutoApprove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTimeAutoApprove_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTimeAutoApprove(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/OnChangeTimeAutoApprove", {
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
   Summary: Invoke method OnChangeTimeTypeCode
   OperationID: OnChangeTimeTypeCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTimeTypeCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTimeTypeCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTimeTypeCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/OnChangeTimeTypeCode", {
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
   Summary: Invoke method DeleteCalendarException
   Description: This method will delete ResourceCal record.
   OperationID: DeleteCalendarException
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteCalendarException_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteCalendarException_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteCalendarException(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/DeleteCalendarException", {
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
   Summary: Invoke method UpdateResourceCal
   Description: This method will check to see if the current ttResourceCal record was modified.
If it is a special working day or non-working day then it save the ttResourceCal
record to the database.
   OperationID: UpdateResourceCal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateResourceCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateResourceCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateResourceCal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/UpdateResourceCal", {
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
   Summary: Invoke method FromEffDateOverlaps
   OperationID: FromEffDateOverlaps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FromEffDateOverlaps_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FromEffDateOverlaps_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FromEffDateOverlaps(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/FromEffDateOverlaps", {
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
   Summary: Invoke method GetEmpStatusCodeDescList
   OperationID: GetEmpStatusCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEmpStatusCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEmpStatusCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEmpStatusCodeDescList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetEmpStatusCodeDescList", {
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
   Summary: Invoke method getValidCompanyName
   OperationID: getValidCompanyName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getValidCompanyName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getValidCompanyName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_getValidCompanyName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/getValidCompanyName", {
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
   Summary: Invoke method GetIfCurrentSiteHasExternalMES
   Description: Purpose:
Parameters:  none
Notes:
   OperationID: GetIfCurrentSiteHasExternalMES
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIfCurrentSiteHasExternalMES_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetIfCurrentSiteHasExternalMES(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetIfCurrentSiteHasExternalMES", {
          method: 'post',
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
   Summary: Invoke method ModifySearchIDs
   Description: Modify Search ID.
   OperationID: ModifySearchIDs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ModifySearchIDs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ModifySearchIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ModifySearchIDs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/ModifySearchIDs", {
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
   Summary: Invoke method GetNewEmpBasic
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpBasic
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpBasic_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpBasic_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEmpBasic(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetNewEmpBasic", {
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
   Summary: Invoke method GetNewEmpBasicAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpBasicAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpBasicAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpBasicAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEmpBasicAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetNewEmpBasicAttch", {
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
   Summary: Invoke method GetNewEmpLabExpRate
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpLabExpRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpLabExpRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpLabExpRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEmpLabExpRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetNewEmpLabExpRate", {
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
   Summary: Invoke method GetNewEmpCal
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpCal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEmpCal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetNewEmpCal", {
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
   Summary: Invoke method GetNewPartner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetNewPartner", {
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
   Summary: Invoke method GetNewResourceCal
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewResourceCal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewResourceCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewResourceCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewResourceCal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetNewResourceCal", {
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
   Summary: Invoke method GetNewEmpRole
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpRole
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpRole_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpRole_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEmpRole(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetNewEmpRole", {
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
   Summary: Invoke method GetNewEntityGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEntityGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEntityGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEntityGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEntityGLC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetNewEntityGLC", {
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
   Summary: Invoke method GetNewEmpRoleRt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpRoleRt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpRoleRt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpRoleRt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEmpRoleRt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetNewEmpRoleRt", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpBasicSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpBasicAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EmpBasicAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpBasicListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EmpBasicListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpBasicRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EmpBasicRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpCalRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EmpCalRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpLabExpRateRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EmpLabExpRateRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpRoleRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EmpRoleRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpRoleRtRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EmpRoleRtRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EntityGLCRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartnerRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartnerRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceCalRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ResourceCalRow[],
}

export interface Erp_Tablesets_EmpBasicAttchRow{
   "Company":string,
   "EmpID":string,
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

export interface Erp_Tablesets_EmpBasicListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "EmpID":string,
      /**  First name of employee.  */  
   "FirstName":string,
      /**  Middle name of employee.  */  
   "MiddleInitial":string,
      /**  Last name of employee  */  
   "LastName":string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   "Name":string,
      /**  Home phone number  */  
   "Phone":string,
      /**  Normal work shift.  Value is to be defaulted from XASyst.DefaultShift (Production/Data Collection tab in Company Configuration) when available, otherwise it is not defaulted.  */  
   "Shift":number,
      /**  Labor rate that is used for Job Costing.  */  
   "LaborRate":number,
      /**  An internally assigned flag that Indicates if the employee needs to be established in payroll. (Existence of PREmpMas). This flag is used to allow payroll employee maintenance view new employees created by job costing that were flagged as being "Payroll" employees.  */  
   "PRSetupReq":boolean,
      /**  Indicates the employment status. Can be A-Active, I-InActive or T-Terminated.  */  
   "EmpStatus":string,
      /**  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  */  
   "PhotoFile":string,
      /**   The Job Department in which the employee works work was done. An optional field. If entered must be valid in JCDept table.
Used by data collection in the "Work Que" window to provide a default department to view.  */  
   "JCDept":string,
      /**   The ID of the Supervisor for the employee.  The Supervisor ID is actually the EmpID used for supervisor's PREmpMas record.
Validation: Can't be blank, if entered must be found in the PREmpMas file.  */  
   "SupervisorID":string,
      /**  This person usually goes out on service calls  */  
   "ServTech":boolean,
      /**   Links the employee to a UserID.  This link is used by the Shop Floor Menu(SFM).  In the SFM, the user signs on with their employee id instead of a User id. This link grants the menu security authorizations of the User to the employee. It also defines the language to be used.
Note: An employee can only be related to one UserFile record. Each UserFile, can be related to many employees.  Therefore, you might set up a few generic Users per language, or based on security levels or you might set up a user for each employee. Note: Many transactions, are stamped with the UserID, thus if you use generic users you will be tracking to the individual employee.
This field is OPTIONAL. However, employee will not be allowed to login to the SFM without a being linked to a UserID.  Also, the company of the employee must be an authorized company of the user. This is validated by the finding a record in UserComp table, using EmpBasic.Company, EmpBasic.DCDUserID.  */  
   "DcdUserID":string,
      /**  Indicates if this employee is a shop supervisor. This must be checked for employee to use the Shop Floor Menu Supervisor options.  */  
   "ShopSupervisor":boolean,
      /**  A warehouse manager has the access to the Manager's Queue tab in the Material Request Queue.  */  
   "WarehouseManager":boolean,
      /**  Resource Group ID for this employee, only allowed if the Project Billing module licensed.  */  
   "ResourceGrpID":string,
      /**  Resource D for this employee, only allowed if the Project Billing module licensed.  */  
   "ResourceID":string,
      /**  SupervisorName  */  
   "SupervisorName":string,
   "ShiftDescription":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "ResourceGroupDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_EmpBasicRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "EmpID":string,
      /**  First name of employee.  */  
   "FirstName":string,
      /**  Middle name of employee.  */  
   "MiddleInitial":string,
      /**  Last name of employee  */  
   "LastName":string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   "Name":string,
      /**  First Address Line  */  
   "Address":string,
      /**  Second Address Line  */  
   "Address2":string,
      /**  City portion of address  */  
   "City":string,
      /**  Home State. Can be blank.  */  
   "State":string,
      /**  Postal Code or Zip code portion of address  */  
   "ZIP":string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   "Country":string,
      /**  Home phone number  */  
   "Phone":string,
      /**  Emergency Phone number  */  
   "EmgPhone":string,
      /**  Normal work shift.  Value is to be defaulted from XASyst.DefaultShift (Production/Data Collection tab in Company Configuration) when available, otherwise it is not defaulted.  */  
   "Shift":number,
      /**  Labor rate that is used for Job Costing.  */  
   "LaborRate":number,
      /**   Indicates if this employee is should be paid through the Manufacturing System payroll module.  This does not mean they have been setup in payroll, only that they should be.
Once setup in payroll (existence of corresponding PREmpMas record) this field cannot be changed.  */  
   "Payroll":boolean,
      /**  An internally assigned flag that Indicates if the employee needs to be established in payroll. (Existence of PREmpMas). This flag is used to allow payroll employee maintenance view new employees created by job costing that were flagged as being "Payroll" employees.  */  
   "PRSetupReq":boolean,
      /**  Indicates the employment status. Can be A-Active, I-InActive or T-Terminated.  */  
   "EmpStatus":string,
      /**   The default expense code that will be for direct labor hours reported by this employee.  This must be valid in the LabExpCd master file.
This will be used unless labor is reported where the JobHead.ExpenseCode is not blank.  */  
   "ExpenseCode":string,
      /**  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  */  
   "PhotoFile":string,
      /**   The Job Department in which the employee works work was done. An optional field. If entered must be valid in JCDept table.
Used by data collection in the "Work Que" window to provide a default department to view.  */  
   "JCDept":string,
      /**  Emergency contact name.  */  
   "EmgContact":string,
      /**   The ID of the Supervisor for the employee.  The Supervisor ID is actually the EmpID used for supervisor's PREmpMas record.
Validation: Can't be blank, if entered must be found in the PREmpMas file.  */  
   "SupervisorID":string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  This person usually goes out on service calls  */  
   "ServTech":boolean,
      /**  Email address of the Employee.  */  
   "EMailAddress":string,
      /**   Links the employee to a UserID.  This link is used by the Shop Floor Menu(SFM).  In the SFM, the user signs on with their employee id instead of a User id. This link grants the menu security authorizations of the User to the employee. It also defines the language to be used.
Note: An employee can only be related to one UserFile record. Each UserFile, can be related to many employees.  Therefore, you might set up a few generic Users per language, or based on security levels or you might set up a user for each employee. Note: Many transactions, are stamped with the UserID, thus if you use generic users you will be tracking to the individual employee.
This field is OPTIONAL. However, employee will not be allowed to login to the SFM without a being linked to a UserID.  Also, the company of the employee must be an authorized company of the user. This is validated by the finding a record in UserComp table, using EmpBasic.Company, EmpBasic.DCDUserID.  */  
   "DcdUserID":string,
      /**  Indicates if this employee works on the manufacturing line. This must be checked for employee to use the Shop Floor Menu production options.  */  
   "ProductionWorker":boolean,
      /**  Indicates if this employee is a material handler. This must be checked for employee to use the Shop Floor Menu material handler options.  */  
   "MaterialHandler":boolean,
      /**  Indicates if this employee is a shop supervisor. This must be checked for employee to use the Shop Floor Menu Supervisor options.  */  
   "ShopSupervisor":boolean,
      /**   Pertains to Data Collection only.
Indicates if the employee is allowed report completed quantities.  */  
   "CanReportQty":boolean,
      /**   Pertains to Data Collection only.
Indicates if the job/asm/opr can be overriden when reporting completed quantity.  If NO, then they will only be allowed to report against a job/asm/opr that they are currently working on (active labordtl record ) or where the job is open and the operation is marked as "quantity only" reporting .  If YES, they can enter the quantity for any open job without first having to do a start activity function.
( See also EmpBasic.CanReportQty )  */  
   "CanOverrideJob":boolean,
      /**   Pertains to Data Collection/Advanced Material Management only.
Indicates if the employee is allowed make requests for materials.  */  
   "CanRequestMaterial":boolean,
      /**   Pertains to Data Collection only.
Indicates if the employee is allowed report scrap quantities.  */  
   "CanReportScrapQty":boolean,
      /**   Pertains to Data Collection only.
Indicates if the employee is allowed report nonconformance quantities.  */  
   "CanReportNCQty":boolean,
      /**  Indicates if this employee is a Shipping/Receiving worker. This must be checked for employee to use the Shop Floor Menu Shipping/Receiving options.  */  
   "ShipRecv":boolean,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "CnvEmpID":string,
      /**  A warehouse manager has the access to the Manager's Queue tab in the Material Request Queue.  */  
   "WarehouseManager":boolean,
      /**  Employee is able to override a hard allocation against inventory and select it from another Bin during the process of picking and packing orders, as long as it is not allocated to another Sales Order, Job or Transfer Order.  */  
   "CanOverrideAllocations":boolean,
      /**  If false the shop employee will not be allowed to book time to manufacturing jobs.  */  
   "AllowDirLbr":boolean,
      /**  True indicates that the shop employee is on contract rather than paid via the payroll. This flag is then used in the advanced billing invoice preparation process.  */  
   "ContractEmp":boolean,
      /**  Resource Group ID for this employee, only allowed if the Project Billing module licensed.  */  
   "ResourceGrpID":string,
      /**  Resource D for this employee, only allowed if the Project Billing module licensed.  */  
   "ResourceID":string,
      /**  Unique identifier of the workflow group for this employee's Time transactions.  */  
   "TimeWFGroupID":string,
      /**  This value will be true if the Employee is allowed to enter Expense.  */  
   "ExpenseEntryAllowed":boolean,
      /**  Unique identifier of the workflow group for this employee's Expense transactions.  */  
   "ExpenseWFGroupID":string,
      /**  The Supplier Number associated to the Employee for Expense entry.  */  
   "ExpenseVendorNum":number,
      /**  Unique identifier for a PerCon record.  */  
   "PerConID":number,
      /**  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  */  
   "SyncNameToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  */  
   "SyncAddressToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  */  
   "SyncPhoneToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  */  
   "SyncEmailToPerCon":boolean,
      /**   Pertains to Time Management.
Maintains whether the employee is allowed to enter Indirect time.  */  
   "CanEnterIndirectTime":boolean,
      /**   Pertains to Time Management.
Maintains whether the employee is allowed to enter Production time.  */  
   "CanEnterProductionTime":boolean,
      /**   Pertains to Time Management.
Maintains whether the employee is allowed to enter Project time.  */  
   "CanEnterProjectTime":boolean,
      /**   Pertains to Time Management.
Maintains whether the employee is allowed to enter Service time.  */  
   "CanEnterServiceTime":boolean,
      /**   Pertains to Time Management.
Maintains whether the employee is allowed to enter Setup time.  */  
   "CanEnterSetupTime":boolean,
      /**  Time transactions for the employee requiring employee approval logic will automatically be approved.  */  
   "TimeAutoApprove":boolean,
      /**  Expense transactions for the employee requiring employee approval logic will automatically be approved.  */  
   "ExpenseAutoApprove":boolean,
      /**  Mobile Password  */  
   "MobileUserPassword":string,
      /**  Default is True.  Determines if an employee can enter time with a labor type of Indirect.  If True, an employee may select Indirect labor type.  If false, employee may not select Indirect labor type in Time Entry.  */  
   "AllowIndirect":boolean,
      /**  Default is True.  Determines if an employee can enter time with a labor type of Production.  If True, an employee may select Production labor type.  If false, employee may not select Production labor type in Time Entry.  */  
   "AllowProduction":boolean,
      /**  Default is True.  Determines if an employee can enter time with a labor type of Project.  If True, an employee may select Project labor type.  If false, employee may not select Project labor type in Time Entry.  */  
   "AllowProject":boolean,
      /**  Default is True.  Determines if an employee can enter time with a labor type of Service.  If True, an employee may select Service labor type.  If false, employee may not select Service labor type in Time Entry.  */  
   "AllowService":boolean,
      /**  Default is True.  Determines if an employee can enter time with a labor type of Setup.  If True, an employee may select Setup labor type.  If false, employee may not select Setup labor type in Time Entry.  */  
   "AllowSetup":boolean,
      /**   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  */  
   "DefaultLaborTypePseudo":string,
      /**  Time Type Code  */  
   "DefaultTimeTypCd":string,
      /**  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  */  
   "DefaultIndirectCode":string,
      /**  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  */  
   "DefaultExpenseCode":string,
      /**   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  */  
   "DefaultResourceGrpID":string,
      /**  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  */  
   "DefaultResourceID":string,
      /**  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  */  
   "DefaultLaborHrs":number,
      /**  The currency the expense occurred in.  */  
   "DefaultExpCurrencyCode":string,
      /**  The currency the claim amounts are in.  */  
   "DefaultClaimCurrencyCode":string,
      /**  The payment method of the expense.  */  
   "DefaultPMUID":number,
      /**  The Tax Region for this expense.  */  
   "DefaultTaxRegionCode":string,
      /**  Indicates if the expense amount includes tax.  */  
   "DefaultTaxIncluded":boolean,
      /**  This value will be true if the Employee is allowed to enter Expense for advance requests.  */  
   "ExpenseAdvReqAllowed":boolean,
      /**  Unique identifier of the workflow group for this employee's Expense advance request transactions.  */  
   "ExpenseAdvReqWFGroupID":string,
      /**  Advance request expense transactions for the employee requiring employee approval logic will automatically be approved.  */  
   "ExpenseAdvReqAutoApprove":boolean,
      /**  MobileResourceID  */  
   "MobileResourceID":string,
      /**  AllowAsAltRemitTo  */  
   "AllowAsAltRemitTo":boolean,
      /**  UserNameInJDF  */  
   "UserNameInJDF":string,
      /**  Indicates the record is used with Machine MES  */  
   "ExternalMES":boolean,
      /**  PermitScrap  */  
   "PermitScrap":boolean,
      /**  PermitDown  */  
   "PermitDown":boolean,
      /**  PermitHelp  */  
   "PermitHelp":boolean,
      /**  PermitJobControl  */  
   "PermitJobControl":boolean,
      /**  PermitNextJobControl  */  
   "PermitNextJobControl":boolean,
      /**  PermitManualSqc  */  
   "PermitManualSqc":boolean,
      /**  PermitVariableSqc  */  
   "PermitVariableSqc":boolean,
      /**  PermitAttributeSqc  */  
   "PermitAttributeSqc":boolean,
      /**  PermitMaterialLot  */  
   "PermitMaterialLot":boolean,
      /**  PermitSetupMaterial  */  
   "PermitSetupMaterial":boolean,
      /**  PermitCavities  */  
   "PermitCavities":boolean,
      /**  PermitPercentRegrind  */  
   "PermitPercentRegrind":boolean,
      /**  PermitSaveProfile  */  
   "PermitSaveProfile":boolean,
      /**  PermitCalibration  */  
   "PermitCalibration":boolean,
      /**  PermitMachinePm  */  
   "PermitMachinePm":boolean,
      /**  PermitToolPm  */  
   "PermitToolPm":boolean,
      /**  PermitLanguage  */  
   "PermitLanguage":boolean,
      /**  PermitPreferences  */  
   "PermitPreferences":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The purpose of the flag is to disallow an employee to enter their own time in Time and Expense Entry  */  
   "DisallowTimeEntry":boolean,
      /**  Indicates that an employee can execute inbound related transactions on the shop floor. The default for the check box is unchecked.  */  
   "PkgInboundAllowed":boolean,
      /**  Indicates that an employee can execute outbound related transactions on the shop floor. The default for the check box is unchecked.  */  
   "PkgOutboundAllowed":boolean,
      /**  Indicates that an employee can execute inventory related transactions on the shop floor. The default for the check box is unchecked.  */  
   "PkgInventoryAllowed":boolean,
      /**  Indicates that an employee can execute manufacturing related transactions on the shop floor. The default for the check box is unchecked.  */  
   "PkgManufacturingAllowed":boolean,
      /**  Indicates that an employee can execute quality related transactions on the shop floor. The default for the check box is unchecked.  */  
   "PkgQualityAllowed":boolean,
      /**  ImageID  */  
   "ImageID":string,
      /**  Package Control Activity setting to indicate if the employee is allowed to print during the Master and MixedMaster.  */  
   "PkgMasterMixedPrint":boolean,
      /**  PkgSuppressPrintMessages  */  
   "PkgSuppressPrintMessages":boolean,
      /**  PayrollValuesForHCM  */  
   "PayrollValuesForHCM":string,
      /**  Determines if the employee has to be synchronized with Epicor FSA application.  */  
   "SendToFSA":boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   "ExternalMESSyncRequired":boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   "ExternalMESLastSync":string,
      /**  Identity Document  */  
   "IDDocument":string,
      /**  Birthdate  */  
   "BirthDate":string,
      /**  Sex  */  
   "Sex":string,
      /**  Department  */  
   "Department":string,
      /**  Enrollment Date  */  
   "EnrollmentDate":string,
      /**  Departure Date  */  
   "DepartureDate":string,
      /**  Should this employee receive email alert messages.  */  
   "AlertFlag":boolean,
      /**  Department Description  */  
   "DepartmentDescription":string,
      /**  external field for UI to use to know whether it should enable or disable the ExpenseVendorNumVendorID field.  */  
   "EnableExpenseSupplier":boolean,
      /**  Expense Description  */  
   "ExpenseDescription":string,
      /**  Indicates whether the user is allowed to create Expense transactions in Time and Expense Entry for another employee for which they are an Approver.  */  
   "ExpenseDisableCreate":boolean,
   "ExpenseRestrictEntry":boolean,
      /**  Payroll record has been found so changes to many fields are disallowed.  */  
   "FoundPayroll":boolean,
      /**  Payroll record has been found so changes to many fields are disallowed, but the user is in the employee's payroll class so can see the labor rate field  */  
   "FoundPayrollUserAllowed":boolean,
      /**  String value which contains the validations for the HCM Integration, possible values NON(Nothing configured), HDR (Header) DTL (Detail)  */  
   "HCMEnabledAt":string,
      /**  External field used on Employee Entry in order to enable/disable HCM configuration  */  
   "IsHCMAllowedByEmp":boolean,
      /**  Displays blank if "Allow Override Integrate Labor Pay Hours at Employee" checkbox in Site configuration is unchecked and Employee's value if checked.  */  
   "PayrollValuesForHCMDsp":string,
   "PerConName":string,
      /**  Path to the photo file if it exists.  */  
   "PhotoFilePath":string,
      /**  Flag used to indicate that the generate fill shop capacity process needs to be run to update the ShopCap records because new records won't be added due performance.  */  
   "SetShopLoad":boolean,
      /**  Shift end time in Hours:Minute format., used by Shop Tracker  */  
   "ShiftEndTime":string,
      /**  Shift start time in Hours:Minutes format  */  
   "ShiftStartTime":string,
      /**  SupervisorName  */  
   "SupervisorName":string,
      /**  Indicates whether the user is allowed to create a Time transaction in Time and Expense Entry for another employee for which they are an Approver.  */  
   "TimeDisableCreate":boolean,
   "TimeRestrictEntry":boolean,
      /**  User ID Name  */  
   "UserIDName":string,
   "CalendarID":string,
      /**  List of fields which are referenced by COA segments.  */  
   "COASegReferences":string,
      /**  This column used to display Time Approval Task tree in MetaUI  */  
   "TimeApprovalTasksTree":string,
      /**  This column used to display Time Approval Task tree in MetaUI  */  
   "ExpenseApprovalTasksTree":string,
   "ShiftLength":number,
   "BitFlag":number,
   "CompanySendToFSA":boolean,
   "CountryNumDescription":string,
   "ExpenseCodeDescription":string,
   "ExpenseVendorNumName":string,
   "ExpenseVendorNumCity":string,
   "ExpenseVendorNumTermsCode":string,
   "ExpenseVendorNumAddress3":string,
   "ExpenseVendorNumDefaultFOB":string,
   "ExpenseVendorNumCurrencyCode":string,
   "ExpenseVendorNumZIP":string,
   "ExpenseVendorNumVendorID":string,
   "ExpenseVendorNumAddress2":string,
   "ExpenseVendorNumAddress1":string,
   "ExpenseVendorNumCountry":string,
   "ExpenseVendorNumState":string,
   "JCDeptDescription":string,
   "MachineDescription":string,
   "ResourceDescription":string,
   "ResourceGroupDescription":string,
   "ShiftDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_EmpCalRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "EmpID":string,
      /**  Epmloyee Calendar ID  */  
   "CalendarID":string,
      /**  From Effective Date of this Calendar for this Employee.  The value must be unique per Company/Employee/Calendar.  This value cannot be changed after the initial save.  */  
   "FromEffectiveDate":string,
      /**  To Effective Date of this Calendar for this Employee.  Value is not required.  */  
   "ToEffectiveDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "CalendarIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_EmpLabExpRateRow{
      /**  Company  */  
   "Company":string,
      /**  EmpID  */  
   "EmpID":string,
      /**  ExpenseCode  */  
   "ExpenseCode":string,
      /**  RateType  */  
   "RateType":number,
      /**  RateMultiplier  */  
   "RateMultiplier":number,
      /**  FixedRate  */  
   "FixedRate":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
   "EmpBasicName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_EmpRoleRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "EmpID":string,
      /**  Project Role Code  */  
   "RoleCd":string,
      /**  Setting this to true defines this role code as the  primary Project Role for the employee.ONLY one role code can be defined as primary.  */  
   "Primary":boolean,
      /**  Determines if this Employee is a Time Approver through this Role.  */  
   "TimeApprover":boolean,
      /**  Determines if this Employee is a Expense Approver through this Role.  */  
   "ExpenseApprover":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "EmpBasicName":string,
   "EmpBasicFirstName":string,
   "EmpBasicLastName":string,
   "RoleCdRoleDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_EmpRoleRtRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "EmpID":string,
      /**  Project Role Code  */  
   "RoleCd":string,
      /**  The effective date of the project role code rate.  */  
   "RateEffDte":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Time Type Code  */  
   "TimeTypCd":string,
      /**  The charge rate for project role code expressed in the designated currency code.  */  
   "Rate":number,
      /**  The end date of the project role code rate.  */  
   "RateEndDte":string,
      /**  Sequence field used to keep the primary key unique  */  
   "Seq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "CurrencyCurrencyID":string,
   "CurrencyCurrSymbol":string,
   "CurrencyCurrDesc":string,
   "CurrencyDocumentDesc":string,
   "CurrencyCurrName":string,
   "EmpBasicFirstName":string,
   "EmpBasicName":string,
   "EmpBasicLastName":string,
   "RoleCdRoleDescription":string,
   "TimeTypCdDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_EntityGLCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  */  
   "Key2":string,
      /**   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
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
      /**  Identifier of the GL Control Type.  */  
   "GLControlType":string,
      /**  GL Control Identifier.  */  
   "GLControlCode":string,
      /**  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  */  
   "BusinessEntity":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   "IsExternalCompany":boolean,
      /**  Marks this EntityGLC as global, available to be sent out to other companies.  */  
   "GlobalEntityGLC":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  BankAcctID of the related BankAcct record.  */  
   "BankAcctID":string,
   "BankFeeID":string,
      /**  CallCode of the related FSCallCd record.  */  
   "CallCode":string,
   "ChargeCode":string,
      /**  ClassCode of the related FAClass record.  */  
   "ClassCode":string,
      /**  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  */  
   "ClassID":string,
      /**  ContractCode of the related FSContCd record.  */  
   "ContractCode":string,
      /**  CurrencyCode of the related Currency record.  */  
   "CurrencyCode":string,
      /**  CustNum of the related Customer record  */  
   "CustNum":number,
      /**  DeductionID of PRClsDed or PRDeduct.  */  
   "DeductionID":string,
      /**  EmpID of the related PREmpMas record.  */  
   "EmpID":string,
      /**  ExpenseCode of PayTLbr, LabExpCd  */  
   "ExpenseCode":string,
      /**  ExtSystemID of ExtCompany table  */  
   "ExtSystemID":string,
      /**  FromPlant value of the related PlntTranDef record.  */  
   "FromPlant":string,
      /**  GroupCode of the related FAGroup record.  */  
   "GroupCode":string,
   "GroupID":string,
   "HeadNum":number,
   "InvoiceNum":string,
      /**  JCDept of the related JCDept record.  */  
   "JCDept":string,
      /**  MiscCode of the related MiscChrg or PurMisc record.  */  
   "MiscCode":string,
      /**  PartNum of the related Part record.  */  
   "PartNum":string,
      /**  PayTypeID of PayType  */  
   "PayTypeID":string,
   "PerConName":string,
      /**  PI Status  */  
   "PIStatus":string,
      /**  Plant of the related PlantConfCtrl record.  */  
   "Plant":string,
      /**  ProdCode of the related ProdGrup record.  */  
   "ProdCode":string,
      /**  ProjectID of the related Project record.  */  
   "ProjectID":string,
      /**  PurchCode of the related GLPurch record.  */  
   "PurchCode":string,
      /**  RateCode of the related GLRate record.  */  
   "RateCode":string,
      /**  ReasonCode of the related Reason record.  */  
   "ReasonCode":string,
      /**  ReasonType of the related Reason record.  */  
   "ReasonType":string,
      /**  SalesCatID of the related SalesCat record.  */  
   "SalesCatID":string,
      /**  Shift value of the related JCShift record.  */  
   "Shift":number,
      /**  TaxCode of the related SalesTax record.  */  
   "TaxCode":string,
      /**  TaxTblID of PRTaxMas or PRClsTax.  */  
   "TaxTblID":string,
      /**  ToPlant value of the related PlntTranDef record.  */  
   "ToPlant":string,
      /**  TransferMethod of ExtCompany table  */  
   "TransferMethod":string,
      /**  Type ID  */  
   "TypeID":string,
      /**  VendorNum of the related Vendor record.  */  
   "VendorNum":number,
      /**  WarehouseCode of the related Warehse record.  */  
   "WarehouseCode":string,
   "ExpenseTypeCode":string,
   "IsFiltered":boolean,
   "OprTypeCode":string,
   "CashDeskID":string,
   "TIN":string,
   "ReclassCodeID":string,
   "BitFlag":number,
   "GLCntrlDescription":string,
   "GLCntrlTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartnerRow{
      /**  Company  */  
   "Company":string,
      /**  PartnerNum  */  
   "PartnerNum":number,
      /**  PartnerType  */  
   "PartnerType":number,
      /**  SearchID  */  
   "SearchID":string,
      /**  IsActive  */  
   "IsActive":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  PartnerID  */  
   "PartnerID":string,
   "DspSearchID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ResourceCalRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A code uniquely identifies a Resource Group.  */  
   "ResourceGrpID":string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource.  */  
   "ResourceID":string,
      /**  Exception Day  */  
   "SpecialDay":string,
      /**  ProdHour01  */  
   "ProdHour01":boolean,
      /**  ProdHour02  */  
   "ProdHour02":boolean,
      /**  ProdHour03  */  
   "ProdHour03":boolean,
      /**  ProdHour04  */  
   "ProdHour04":boolean,
      /**  ProdHour05  */  
   "ProdHour05":boolean,
      /**  ProdHour06  */  
   "ProdHour06":boolean,
      /**  ProdHour07  */  
   "ProdHour07":boolean,
      /**  ProdHour08  */  
   "ProdHour08":boolean,
      /**  ProdHour09  */  
   "ProdHour09":boolean,
      /**  ProdHour10  */  
   "ProdHour10":boolean,
      /**  ProdHour11  */  
   "ProdHour11":boolean,
      /**  ProdHour12  */  
   "ProdHour12":boolean,
      /**  ProdHour13  */  
   "ProdHour13":boolean,
      /**  ProdHour14  */  
   "ProdHour14":boolean,
      /**  ProdHour15  */  
   "ProdHour15":boolean,
      /**  ProdHour16  */  
   "ProdHour16":boolean,
      /**  ProdHour17  */  
   "ProdHour17":boolean,
      /**  ProdHour18  */  
   "ProdHour18":boolean,
      /**  ProdHour19  */  
   "ProdHour19":boolean,
      /**  ProdHour20  */  
   "ProdHour20":boolean,
      /**  ProdHour21  */  
   "ProdHour21":boolean,
      /**  ProdHour22  */  
   "ProdHour22":boolean,
      /**  ProdHour23  */  
   "ProdHour23":boolean,
      /**  ProdHour24  */  
   "ProdHour24":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ExceptionLabel  */  
   "ExceptionLabel":string,
      /**  Display Exception Label  */  
   "DispExceptionLabel":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param empID
   */  
export interface CheckClockInStatus_input{
      /**  Employee ID  */  
   empID:string,
}

export interface CheckClockInStatus_output{
   returnObj:Erp_Tablesets_EmpBasicTableset[],
parameters : {
      /**  output parameters  */  
   clockIn:boolean,
   shift:number,
   downtime:boolean,
   clockInTimeStr:string,
}
}

   /** Required : 
      @param ipEmpID
      @param ipLaborShift
   */  
export interface CheckShift_input{
      /**  Employee ID  */  
   ipEmpID:string,
      /**  Labor Shift  */  
   ipLaborShift:number,
}

export interface CheckShift_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param employeeID
      @param shift
   */  
export interface ClockIn_input{
      /**  Employee ID  */  
   employeeID:string,
      /**  Labor Shift  */  
   shift:number,
}

export interface ClockIn_output{
      /**  Clock in time and date as a formatted string  */  
   returnObj:string,
}

   /** Required : 
      @param employeeID
   */  
export interface ClockOut_input{
      /**  Employee ID  */  
   employeeID:string,
}

export interface ClockOut_output{
parameters : {
      /**  output parameters  */  
   employeeID:string,
}
}

   /** Required : 
      @param ipEmpID
      @param ipDate
      @param ds
   */  
export interface CustomizeResourceCal_input{
      /**  The current Employee ID  */  
   ipEmpID:string,
      /**  The selected date to be customized  */  
   ipDate:string,
   ds:Erp_Tablesets_EmpBasicTableset[],
}

export interface CustomizeResourceCal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param vBegTime
      @param vEndTime
      @param vDate
   */  
export interface Date2Int_input{
   vBegTime:string,
   vEndTime:string,
   vDate:string,
}

export interface Date2Int_output{
   returnObj:number,
}

   /** Required : 
      @param empID
   */  
export interface DeleteByID_input{
   empID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param ds
   */  
export interface DeleteCalendarException_input{
   ds:Erp_Tablesets_EmpBasicTableset[],
}

export interface DeleteCalendarException_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

export interface Erp_Tablesets_EmpBasicAttchRow{
   Company:string,
   EmpID:string,
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

export interface Erp_Tablesets_EmpBasicListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   EmpID:string,
      /**  First name of employee.  */  
   FirstName:string,
      /**  Middle name of employee.  */  
   MiddleInitial:string,
      /**  Last name of employee  */  
   LastName:string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   Name:string,
      /**  Home phone number  */  
   Phone:string,
      /**  Normal work shift.  Value is to be defaulted from XASyst.DefaultShift (Production/Data Collection tab in Company Configuration) when available, otherwise it is not defaulted.  */  
   Shift:number,
      /**  Labor rate that is used for Job Costing.  */  
   LaborRate:number,
      /**  An internally assigned flag that Indicates if the employee needs to be established in payroll. (Existence of PREmpMas). This flag is used to allow payroll employee maintenance view new employees created by job costing that were flagged as being "Payroll" employees.  */  
   PRSetupReq:boolean,
      /**  Indicates the employment status. Can be A-Active, I-InActive or T-Terminated.  */  
   EmpStatus:string,
      /**  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  */  
   PhotoFile:string,
      /**   The Job Department in which the employee works work was done. An optional field. If entered must be valid in JCDept table.
Used by data collection in the "Work Que" window to provide a default department to view.  */  
   JCDept:string,
      /**   The ID of the Supervisor for the employee.  The Supervisor ID is actually the EmpID used for supervisor's PREmpMas record.
Validation: Can't be blank, if entered must be found in the PREmpMas file.  */  
   SupervisorID:string,
      /**  This person usually goes out on service calls  */  
   ServTech:boolean,
      /**   Links the employee to a UserID.  This link is used by the Shop Floor Menu(SFM).  In the SFM, the user signs on with their employee id instead of a User id. This link grants the menu security authorizations of the User to the employee. It also defines the language to be used.
Note: An employee can only be related to one UserFile record. Each UserFile, can be related to many employees.  Therefore, you might set up a few generic Users per language, or based on security levels or you might set up a user for each employee. Note: Many transactions, are stamped with the UserID, thus if you use generic users you will be tracking to the individual employee.
This field is OPTIONAL. However, employee will not be allowed to login to the SFM without a being linked to a UserID.  Also, the company of the employee must be an authorized company of the user. This is validated by the finding a record in UserComp table, using EmpBasic.Company, EmpBasic.DCDUserID.  */  
   DcdUserID:string,
      /**  Indicates if this employee is a shop supervisor. This must be checked for employee to use the Shop Floor Menu Supervisor options.  */  
   ShopSupervisor:boolean,
      /**  A warehouse manager has the access to the Manager's Queue tab in the Material Request Queue.  */  
   WarehouseManager:boolean,
      /**  Resource Group ID for this employee, only allowed if the Project Billing module licensed.  */  
   ResourceGrpID:string,
      /**  Resource D for this employee, only allowed if the Project Billing module licensed.  */  
   ResourceID:string,
      /**  SupervisorName  */  
   SupervisorName:string,
   ShiftDescription:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   ResourceGroupDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_EmpBasicListTableset{
   EmpBasicList:Erp_Tablesets_EmpBasicListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_EmpBasicRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   EmpID:string,
      /**  First name of employee.  */  
   FirstName:string,
      /**  Middle name of employee.  */  
   MiddleInitial:string,
      /**  Last name of employee  */  
   LastName:string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   Name:string,
      /**  First Address Line  */  
   Address:string,
      /**  Second Address Line  */  
   Address2:string,
      /**  City portion of address  */  
   City:string,
      /**  Home State. Can be blank.  */  
   State:string,
      /**  Postal Code or Zip code portion of address  */  
   ZIP:string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   Country:string,
      /**  Home phone number  */  
   Phone:string,
      /**  Emergency Phone number  */  
   EmgPhone:string,
      /**  Normal work shift.  Value is to be defaulted from XASyst.DefaultShift (Production/Data Collection tab in Company Configuration) when available, otherwise it is not defaulted.  */  
   Shift:number,
      /**  Labor rate that is used for Job Costing.  */  
   LaborRate:number,
      /**   Indicates if this employee is should be paid through the Manufacturing System payroll module.  This does not mean they have been setup in payroll, only that they should be.
Once setup in payroll (existence of corresponding PREmpMas record) this field cannot be changed.  */  
   Payroll:boolean,
      /**  An internally assigned flag that Indicates if the employee needs to be established in payroll. (Existence of PREmpMas). This flag is used to allow payroll employee maintenance view new employees created by job costing that were flagged as being "Payroll" employees.  */  
   PRSetupReq:boolean,
      /**  Indicates the employment status. Can be A-Active, I-InActive or T-Terminated.  */  
   EmpStatus:string,
      /**   The default expense code that will be for direct labor hours reported by this employee.  This must be valid in the LabExpCd master file.
This will be used unless labor is reported where the JobHead.ExpenseCode is not blank.  */  
   ExpenseCode:string,
      /**  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  */  
   PhotoFile:string,
      /**   The Job Department in which the employee works work was done. An optional field. If entered must be valid in JCDept table.
Used by data collection in the "Work Que" window to provide a default department to view.  */  
   JCDept:string,
      /**  Emergency contact name.  */  
   EmgContact:string,
      /**   The ID of the Supervisor for the employee.  The Supervisor ID is actually the EmpID used for supervisor's PREmpMas record.
Validation: Can't be blank, if entered must be found in the PREmpMas file.  */  
   SupervisorID:string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  This person usually goes out on service calls  */  
   ServTech:boolean,
      /**  Email address of the Employee.  */  
   EMailAddress:string,
      /**   Links the employee to a UserID.  This link is used by the Shop Floor Menu(SFM).  In the SFM, the user signs on with their employee id instead of a User id. This link grants the menu security authorizations of the User to the employee. It also defines the language to be used.
Note: An employee can only be related to one UserFile record. Each UserFile, can be related to many employees.  Therefore, you might set up a few generic Users per language, or based on security levels or you might set up a user for each employee. Note: Many transactions, are stamped with the UserID, thus if you use generic users you will be tracking to the individual employee.
This field is OPTIONAL. However, employee will not be allowed to login to the SFM without a being linked to a UserID.  Also, the company of the employee must be an authorized company of the user. This is validated by the finding a record in UserComp table, using EmpBasic.Company, EmpBasic.DCDUserID.  */  
   DcdUserID:string,
      /**  Indicates if this employee works on the manufacturing line. This must be checked for employee to use the Shop Floor Menu production options.  */  
   ProductionWorker:boolean,
      /**  Indicates if this employee is a material handler. This must be checked for employee to use the Shop Floor Menu material handler options.  */  
   MaterialHandler:boolean,
      /**  Indicates if this employee is a shop supervisor. This must be checked for employee to use the Shop Floor Menu Supervisor options.  */  
   ShopSupervisor:boolean,
      /**   Pertains to Data Collection only.
Indicates if the employee is allowed report completed quantities.  */  
   CanReportQty:boolean,
      /**   Pertains to Data Collection only.
Indicates if the job/asm/opr can be overriden when reporting completed quantity.  If NO, then they will only be allowed to report against a job/asm/opr that they are currently working on (active labordtl record ) or where the job is open and the operation is marked as "quantity only" reporting .  If YES, they can enter the quantity for any open job without first having to do a start activity function.
( See also EmpBasic.CanReportQty )  */  
   CanOverrideJob:boolean,
      /**   Pertains to Data Collection/Advanced Material Management only.
Indicates if the employee is allowed make requests for materials.  */  
   CanRequestMaterial:boolean,
      /**   Pertains to Data Collection only.
Indicates if the employee is allowed report scrap quantities.  */  
   CanReportScrapQty:boolean,
      /**   Pertains to Data Collection only.
Indicates if the employee is allowed report nonconformance quantities.  */  
   CanReportNCQty:boolean,
      /**  Indicates if this employee is a Shipping/Receiving worker. This must be checked for employee to use the Shop Floor Menu Shipping/Receiving options.  */  
   ShipRecv:boolean,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   CnvEmpID:string,
      /**  A warehouse manager has the access to the Manager's Queue tab in the Material Request Queue.  */  
   WarehouseManager:boolean,
      /**  Employee is able to override a hard allocation against inventory and select it from another Bin during the process of picking and packing orders, as long as it is not allocated to another Sales Order, Job or Transfer Order.  */  
   CanOverrideAllocations:boolean,
      /**  If false the shop employee will not be allowed to book time to manufacturing jobs.  */  
   AllowDirLbr:boolean,
      /**  True indicates that the shop employee is on contract rather than paid via the payroll. This flag is then used in the advanced billing invoice preparation process.  */  
   ContractEmp:boolean,
      /**  Resource Group ID for this employee, only allowed if the Project Billing module licensed.  */  
   ResourceGrpID:string,
      /**  Resource D for this employee, only allowed if the Project Billing module licensed.  */  
   ResourceID:string,
      /**  Unique identifier of the workflow group for this employee's Time transactions.  */  
   TimeWFGroupID:string,
      /**  This value will be true if the Employee is allowed to enter Expense.  */  
   ExpenseEntryAllowed:boolean,
      /**  Unique identifier of the workflow group for this employee's Expense transactions.  */  
   ExpenseWFGroupID:string,
      /**  The Supplier Number associated to the Employee for Expense entry.  */  
   ExpenseVendorNum:number,
      /**  Unique identifier for a PerCon record.  */  
   PerConID:number,
      /**  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  */  
   SyncNameToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  */  
   SyncAddressToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  */  
   SyncPhoneToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  */  
   SyncEmailToPerCon:boolean,
      /**   Pertains to Time Management.
Maintains whether the employee is allowed to enter Indirect time.  */  
   CanEnterIndirectTime:boolean,
      /**   Pertains to Time Management.
Maintains whether the employee is allowed to enter Production time.  */  
   CanEnterProductionTime:boolean,
      /**   Pertains to Time Management.
Maintains whether the employee is allowed to enter Project time.  */  
   CanEnterProjectTime:boolean,
      /**   Pertains to Time Management.
Maintains whether the employee is allowed to enter Service time.  */  
   CanEnterServiceTime:boolean,
      /**   Pertains to Time Management.
Maintains whether the employee is allowed to enter Setup time.  */  
   CanEnterSetupTime:boolean,
      /**  Time transactions for the employee requiring employee approval logic will automatically be approved.  */  
   TimeAutoApprove:boolean,
      /**  Expense transactions for the employee requiring employee approval logic will automatically be approved.  */  
   ExpenseAutoApprove:boolean,
      /**  Mobile Password  */  
   MobileUserPassword:string,
      /**  Default is True.  Determines if an employee can enter time with a labor type of Indirect.  If True, an employee may select Indirect labor type.  If false, employee may not select Indirect labor type in Time Entry.  */  
   AllowIndirect:boolean,
      /**  Default is True.  Determines if an employee can enter time with a labor type of Production.  If True, an employee may select Production labor type.  If false, employee may not select Production labor type in Time Entry.  */  
   AllowProduction:boolean,
      /**  Default is True.  Determines if an employee can enter time with a labor type of Project.  If True, an employee may select Project labor type.  If false, employee may not select Project labor type in Time Entry.  */  
   AllowProject:boolean,
      /**  Default is True.  Determines if an employee can enter time with a labor type of Service.  If True, an employee may select Service labor type.  If false, employee may not select Service labor type in Time Entry.  */  
   AllowService:boolean,
      /**  Default is True.  Determines if an employee can enter time with a labor type of Setup.  If True, an employee may select Setup labor type.  If false, employee may not select Setup labor type in Time Entry.  */  
   AllowSetup:boolean,
      /**   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  */  
   DefaultLaborTypePseudo:string,
      /**  Time Type Code  */  
   DefaultTimeTypCd:string,
      /**  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  */  
   DefaultIndirectCode:string,
      /**  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  */  
   DefaultExpenseCode:string,
      /**   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  */  
   DefaultResourceGrpID:string,
      /**  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  */  
   DefaultResourceID:string,
      /**  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  */  
   DefaultLaborHrs:number,
      /**  The currency the expense occurred in.  */  
   DefaultExpCurrencyCode:string,
      /**  The currency the claim amounts are in.  */  
   DefaultClaimCurrencyCode:string,
      /**  The payment method of the expense.  */  
   DefaultPMUID:number,
      /**  The Tax Region for this expense.  */  
   DefaultTaxRegionCode:string,
      /**  Indicates if the expense amount includes tax.  */  
   DefaultTaxIncluded:boolean,
      /**  This value will be true if the Employee is allowed to enter Expense for advance requests.  */  
   ExpenseAdvReqAllowed:boolean,
      /**  Unique identifier of the workflow group for this employee's Expense advance request transactions.  */  
   ExpenseAdvReqWFGroupID:string,
      /**  Advance request expense transactions for the employee requiring employee approval logic will automatically be approved.  */  
   ExpenseAdvReqAutoApprove:boolean,
      /**  MobileResourceID  */  
   MobileResourceID:string,
      /**  AllowAsAltRemitTo  */  
   AllowAsAltRemitTo:boolean,
      /**  UserNameInJDF  */  
   UserNameInJDF:string,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  PermitScrap  */  
   PermitScrap:boolean,
      /**  PermitDown  */  
   PermitDown:boolean,
      /**  PermitHelp  */  
   PermitHelp:boolean,
      /**  PermitJobControl  */  
   PermitJobControl:boolean,
      /**  PermitNextJobControl  */  
   PermitNextJobControl:boolean,
      /**  PermitManualSqc  */  
   PermitManualSqc:boolean,
      /**  PermitVariableSqc  */  
   PermitVariableSqc:boolean,
      /**  PermitAttributeSqc  */  
   PermitAttributeSqc:boolean,
      /**  PermitMaterialLot  */  
   PermitMaterialLot:boolean,
      /**  PermitSetupMaterial  */  
   PermitSetupMaterial:boolean,
      /**  PermitCavities  */  
   PermitCavities:boolean,
      /**  PermitPercentRegrind  */  
   PermitPercentRegrind:boolean,
      /**  PermitSaveProfile  */  
   PermitSaveProfile:boolean,
      /**  PermitCalibration  */  
   PermitCalibration:boolean,
      /**  PermitMachinePm  */  
   PermitMachinePm:boolean,
      /**  PermitToolPm  */  
   PermitToolPm:boolean,
      /**  PermitLanguage  */  
   PermitLanguage:boolean,
      /**  PermitPreferences  */  
   PermitPreferences:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The purpose of the flag is to disallow an employee to enter their own time in Time and Expense Entry  */  
   DisallowTimeEntry:boolean,
      /**  Indicates that an employee can execute inbound related transactions on the shop floor. The default for the check box is unchecked.  */  
   PkgInboundAllowed:boolean,
      /**  Indicates that an employee can execute outbound related transactions on the shop floor. The default for the check box is unchecked.  */  
   PkgOutboundAllowed:boolean,
      /**  Indicates that an employee can execute inventory related transactions on the shop floor. The default for the check box is unchecked.  */  
   PkgInventoryAllowed:boolean,
      /**  Indicates that an employee can execute manufacturing related transactions on the shop floor. The default for the check box is unchecked.  */  
   PkgManufacturingAllowed:boolean,
      /**  Indicates that an employee can execute quality related transactions on the shop floor. The default for the check box is unchecked.  */  
   PkgQualityAllowed:boolean,
      /**  ImageID  */  
   ImageID:string,
      /**  Package Control Activity setting to indicate if the employee is allowed to print during the Master and MixedMaster.  */  
   PkgMasterMixedPrint:boolean,
      /**  PkgSuppressPrintMessages  */  
   PkgSuppressPrintMessages:boolean,
      /**  PayrollValuesForHCM  */  
   PayrollValuesForHCM:string,
      /**  Determines if the employee has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
      /**  Identity Document  */  
   IDDocument:string,
      /**  Birthdate  */  
   BirthDate:string,
      /**  Sex  */  
   Sex:string,
      /**  Department  */  
   Department:string,
      /**  Enrollment Date  */  
   EnrollmentDate:string,
      /**  Departure Date  */  
   DepartureDate:string,
      /**  Should this employee receive email alert messages.  */  
   AlertFlag:boolean,
      /**  Department Description  */  
   DepartmentDescription:string,
      /**  external field for UI to use to know whether it should enable or disable the ExpenseVendorNumVendorID field.  */  
   EnableExpenseSupplier:boolean,
      /**  Expense Description  */  
   ExpenseDescription:string,
      /**  Indicates whether the user is allowed to create Expense transactions in Time and Expense Entry for another employee for which they are an Approver.  */  
   ExpenseDisableCreate:boolean,
   ExpenseRestrictEntry:boolean,
      /**  Payroll record has been found so changes to many fields are disallowed.  */  
   FoundPayroll:boolean,
      /**  Payroll record has been found so changes to many fields are disallowed, but the user is in the employee's payroll class so can see the labor rate field  */  
   FoundPayrollUserAllowed:boolean,
      /**  String value which contains the validations for the HCM Integration, possible values NON(Nothing configured), HDR (Header) DTL (Detail)  */  
   HCMEnabledAt:string,
      /**  External field used on Employee Entry in order to enable/disable HCM configuration  */  
   IsHCMAllowedByEmp:boolean,
      /**  Displays blank if "Allow Override Integrate Labor Pay Hours at Employee" checkbox in Site configuration is unchecked and Employee's value if checked.  */  
   PayrollValuesForHCMDsp:string,
   PerConName:string,
      /**  Path to the photo file if it exists.  */  
   PhotoFilePath:string,
      /**  Flag used to indicate that the generate fill shop capacity process needs to be run to update the ShopCap records because new records won't be added due performance.  */  
   SetShopLoad:boolean,
      /**  Shift end time in Hours:Minute format., used by Shop Tracker  */  
   ShiftEndTime:string,
      /**  Shift start time in Hours:Minutes format  */  
   ShiftStartTime:string,
      /**  SupervisorName  */  
   SupervisorName:string,
      /**  Indicates whether the user is allowed to create a Time transaction in Time and Expense Entry for another employee for which they are an Approver.  */  
   TimeDisableCreate:boolean,
   TimeRestrictEntry:boolean,
      /**  User ID Name  */  
   UserIDName:string,
   CalendarID:string,
      /**  List of fields which are referenced by COA segments.  */  
   COASegReferences:string,
      /**  This column used to display Time Approval Task tree in MetaUI  */  
   TimeApprovalTasksTree:string,
      /**  This column used to display Time Approval Task tree in MetaUI  */  
   ExpenseApprovalTasksTree:string,
   ShiftLength:number,
   BitFlag:number,
   CompanySendToFSA:boolean,
   CountryNumDescription:string,
   ExpenseCodeDescription:string,
   ExpenseVendorNumName:string,
   ExpenseVendorNumCity:string,
   ExpenseVendorNumTermsCode:string,
   ExpenseVendorNumAddress3:string,
   ExpenseVendorNumDefaultFOB:string,
   ExpenseVendorNumCurrencyCode:string,
   ExpenseVendorNumZIP:string,
   ExpenseVendorNumVendorID:string,
   ExpenseVendorNumAddress2:string,
   ExpenseVendorNumAddress1:string,
   ExpenseVendorNumCountry:string,
   ExpenseVendorNumState:string,
   JCDeptDescription:string,
   MachineDescription:string,
   ResourceDescription:string,
   ResourceGroupDescription:string,
   ShiftDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_EmpBasicTableset{
   EmpBasic:Erp_Tablesets_EmpBasicRow[],
   EmpBasicAttch:Erp_Tablesets_EmpBasicAttchRow[],
   EmpLabExpRate:Erp_Tablesets_EmpLabExpRateRow[],
   EmpCal:Erp_Tablesets_EmpCalRow[],
   Partner:Erp_Tablesets_PartnerRow[],
   ResourceCal:Erp_Tablesets_ResourceCalRow[],
   EmpRole:Erp_Tablesets_EmpRoleRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   EmpRoleRt:Erp_Tablesets_EmpRoleRtRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_EmpCalRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   EmpID:string,
      /**  Epmloyee Calendar ID  */  
   CalendarID:string,
      /**  From Effective Date of this Calendar for this Employee.  The value must be unique per Company/Employee/Calendar.  This value cannot be changed after the initial save.  */  
   FromEffectiveDate:string,
      /**  To Effective Date of this Calendar for this Employee.  Value is not required.  */  
   ToEffectiveDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   CalendarIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_EmpLabExpRateRow{
      /**  Company  */  
   Company:string,
      /**  EmpID  */  
   EmpID:string,
      /**  ExpenseCode  */  
   ExpenseCode:string,
      /**  RateType  */  
   RateType:number,
      /**  RateMultiplier  */  
   RateMultiplier:number,
      /**  FixedRate  */  
   FixedRate:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
   EmpBasicName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_EmpRoleRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   EmpID:string,
      /**  Project Role Code  */  
   RoleCd:string,
      /**  Setting this to true defines this role code as the  primary Project Role for the employee.ONLY one role code can be defined as primary.  */  
   Primary:boolean,
      /**  Determines if this Employee is a Time Approver through this Role.  */  
   TimeApprover:boolean,
      /**  Determines if this Employee is a Expense Approver through this Role.  */  
   ExpenseApprover:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   EmpBasicName:string,
   EmpBasicFirstName:string,
   EmpBasicLastName:string,
   RoleCdRoleDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_EmpRoleRtRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   EmpID:string,
      /**  Project Role Code  */  
   RoleCd:string,
      /**  The effective date of the project role code rate.  */  
   RateEffDte:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Time Type Code  */  
   TimeTypCd:string,
      /**  The charge rate for project role code expressed in the designated currency code.  */  
   Rate:number,
      /**  The end date of the project role code rate.  */  
   RateEndDte:string,
      /**  Sequence field used to keep the primary key unique  */  
   Seq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   CurrencyCurrencyID:string,
   CurrencyCurrSymbol:string,
   CurrencyCurrDesc:string,
   CurrencyDocumentDesc:string,
   CurrencyCurrName:string,
   EmpBasicFirstName:string,
   EmpBasicName:string,
   EmpBasicLastName:string,
   RoleCdRoleDescription:string,
   TimeTypCdDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_EntityGLCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  */  
   Key2:string,
      /**   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
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
      /**  Identifier of the GL Control Type.  */  
   GLControlType:string,
      /**  GL Control Identifier.  */  
   GLControlCode:string,
      /**  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  */  
   BusinessEntity:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   IsExternalCompany:boolean,
      /**  Marks this EntityGLC as global, available to be sent out to other companies.  */  
   GlobalEntityGLC:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  BankAcctID of the related BankAcct record.  */  
   BankAcctID:string,
   BankFeeID:string,
      /**  CallCode of the related FSCallCd record.  */  
   CallCode:string,
   ChargeCode:string,
      /**  ClassCode of the related FAClass record.  */  
   ClassCode:string,
      /**  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  */  
   ClassID:string,
      /**  ContractCode of the related FSContCd record.  */  
   ContractCode:string,
      /**  CurrencyCode of the related Currency record.  */  
   CurrencyCode:string,
      /**  CustNum of the related Customer record  */  
   CustNum:number,
      /**  DeductionID of PRClsDed or PRDeduct.  */  
   DeductionID:string,
      /**  EmpID of the related PREmpMas record.  */  
   EmpID:string,
      /**  ExpenseCode of PayTLbr, LabExpCd  */  
   ExpenseCode:string,
      /**  ExtSystemID of ExtCompany table  */  
   ExtSystemID:string,
      /**  FromPlant value of the related PlntTranDef record.  */  
   FromPlant:string,
      /**  GroupCode of the related FAGroup record.  */  
   GroupCode:string,
   GroupID:string,
   HeadNum:number,
   InvoiceNum:string,
      /**  JCDept of the related JCDept record.  */  
   JCDept:string,
      /**  MiscCode of the related MiscChrg or PurMisc record.  */  
   MiscCode:string,
      /**  PartNum of the related Part record.  */  
   PartNum:string,
      /**  PayTypeID of PayType  */  
   PayTypeID:string,
   PerConName:string,
      /**  PI Status  */  
   PIStatus:string,
      /**  Plant of the related PlantConfCtrl record.  */  
   Plant:string,
      /**  ProdCode of the related ProdGrup record.  */  
   ProdCode:string,
      /**  ProjectID of the related Project record.  */  
   ProjectID:string,
      /**  PurchCode of the related GLPurch record.  */  
   PurchCode:string,
      /**  RateCode of the related GLRate record.  */  
   RateCode:string,
      /**  ReasonCode of the related Reason record.  */  
   ReasonCode:string,
      /**  ReasonType of the related Reason record.  */  
   ReasonType:string,
      /**  SalesCatID of the related SalesCat record.  */  
   SalesCatID:string,
      /**  Shift value of the related JCShift record.  */  
   Shift:number,
      /**  TaxCode of the related SalesTax record.  */  
   TaxCode:string,
      /**  TaxTblID of PRTaxMas or PRClsTax.  */  
   TaxTblID:string,
      /**  ToPlant value of the related PlntTranDef record.  */  
   ToPlant:string,
      /**  TransferMethod of ExtCompany table  */  
   TransferMethod:string,
      /**  Type ID  */  
   TypeID:string,
      /**  VendorNum of the related Vendor record.  */  
   VendorNum:number,
      /**  WarehouseCode of the related Warehse record.  */  
   WarehouseCode:string,
   ExpenseTypeCode:string,
   IsFiltered:boolean,
   OprTypeCode:string,
   CashDeskID:string,
   TIN:string,
   ReclassCodeID:string,
   BitFlag:number,
   GLCntrlDescription:string,
   GLCntrlTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartnerRow{
      /**  Company  */  
   Company:string,
      /**  PartnerNum  */  
   PartnerNum:number,
      /**  PartnerType  */  
   PartnerType:number,
      /**  SearchID  */  
   SearchID:string,
      /**  IsActive  */  
   IsActive:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  PartnerID  */  
   PartnerID:string,
   DspSearchID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ResourceCalRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A code uniquely identifies a Resource Group.  */  
   ResourceGrpID:string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource.  */  
   ResourceID:string,
      /**  Exception Day  */  
   SpecialDay:string,
      /**  ProdHour01  */  
   ProdHour01:boolean,
      /**  ProdHour02  */  
   ProdHour02:boolean,
      /**  ProdHour03  */  
   ProdHour03:boolean,
      /**  ProdHour04  */  
   ProdHour04:boolean,
      /**  ProdHour05  */  
   ProdHour05:boolean,
      /**  ProdHour06  */  
   ProdHour06:boolean,
      /**  ProdHour07  */  
   ProdHour07:boolean,
      /**  ProdHour08  */  
   ProdHour08:boolean,
      /**  ProdHour09  */  
   ProdHour09:boolean,
      /**  ProdHour10  */  
   ProdHour10:boolean,
      /**  ProdHour11  */  
   ProdHour11:boolean,
      /**  ProdHour12  */  
   ProdHour12:boolean,
      /**  ProdHour13  */  
   ProdHour13:boolean,
      /**  ProdHour14  */  
   ProdHour14:boolean,
      /**  ProdHour15  */  
   ProdHour15:boolean,
      /**  ProdHour16  */  
   ProdHour16:boolean,
      /**  ProdHour17  */  
   ProdHour17:boolean,
      /**  ProdHour18  */  
   ProdHour18:boolean,
      /**  ProdHour19  */  
   ProdHour19:boolean,
      /**  ProdHour20  */  
   ProdHour20:boolean,
      /**  ProdHour21  */  
   ProdHour21:boolean,
      /**  ProdHour22  */  
   ProdHour22:boolean,
      /**  ProdHour23  */  
   ProdHour23:boolean,
      /**  ProdHour24  */  
   ProdHour24:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ExceptionLabel  */  
   ExceptionLabel:string,
      /**  Display Exception Label  */  
   DispExceptionLabel:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtEmpBasicTableset{
   EmpBasic:Erp_Tablesets_EmpBasicRow[],
   EmpBasicAttch:Erp_Tablesets_EmpBasicAttchRow[],
   EmpLabExpRate:Erp_Tablesets_EmpLabExpRateRow[],
   EmpCal:Erp_Tablesets_EmpCalRow[],
   Partner:Erp_Tablesets_PartnerRow[],
   ResourceCal:Erp_Tablesets_ResourceCalRow[],
   EmpRole:Erp_Tablesets_EmpRoleRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   EmpRoleRt:Erp_Tablesets_EmpRoleRtRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param employeeID
      @param effDate
   */  
export interface FromEffDateOverlaps_input{
   employeeID:string,
   effDate:string,
}

export interface FromEffDateOverlaps_output{
   returnObj:boolean,
}

   /** Required : 
      @param inEmpID
   */  
export interface GetByIDForExpense_input{
   inEmpID:string,
}

export interface GetByIDForExpense_output{
   returnObj:Erp_Tablesets_EmpBasicTableset[],
}

   /** Required : 
      @param inEmpID
   */  
export interface GetByIDForTE_input{
   inEmpID:string,
}

export interface GetByIDForTE_output{
   returnObj:Erp_Tablesets_EmpBasicTableset[],
}

   /** Required : 
      @param inEmpID
   */  
export interface GetByIDForTime_input{
   inEmpID:string,
}

export interface GetByIDForTime_output{
   returnObj:Erp_Tablesets_EmpBasicTableset[],
}

   /** Required : 
      @param empID
   */  
export interface GetByID_input{
   empID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_EmpBasicTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_EmpBasicTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_EmpBasicTableset[],
}

   /** Required : 
      @param IP_ServerFileName
   */  
export interface GetClientFileName_input{
   IP_ServerFileName:string,
}

export interface GetClientFileName_output{
   returnObj:string,
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

export interface GetDefaultEmpID_output{
parameters : {
      /**  output parameters  */  
   defaultEmpID:string,
}
}

   /** Required : 
      @param TableName
      @param FieldName
      @param FoundPayroll
   */  
export interface GetEmpStatusCodeDescList_input{
   TableName:string,
   FieldName:string,
   FoundPayroll:boolean,
}

export interface GetEmpStatusCodeDescList_output{
   returnObj:string,
}

export interface GetIfCurrentSiteHasExternalMES_output{
   returnObj:boolean,
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListExpEmployees_input{
      /**  Whereclause for EmpBasic table.  */  
   whereClause:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetListExpEmployees_output{
   returnObj:Erp_Tablesets_EmpBasicListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListForExpense_input{
      /**  Whereclause for EmpBasic table.  */  
   whereClause:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetListForExpense_output{
   returnObj:Erp_Tablesets_EmpBasicListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListForTE_input{
      /**  Whereclause for EmpBasic table.  */  
   whereClause:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetListForTE_output{
   returnObj:Erp_Tablesets_EmpBasicListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListForTime_input{
      /**  Whereclause for EmpBasic table.  */  
   whereClause:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetListForTime_output{
   returnObj:Erp_Tablesets_EmpBasicListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
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
   returnObj:Erp_Tablesets_EmpBasicListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param empID
   */  
export interface GetNewEmpBasicAttch_input{
   ds:Erp_Tablesets_EmpBasicTableset[],
   empID:string,
}

export interface GetNewEmpBasicAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewEmpBasic_input{
   ds:Erp_Tablesets_EmpBasicTableset[],
}

export interface GetNewEmpBasic_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param ds
      @param empID
      @param calendarID
   */  
export interface GetNewEmpCal_input{
   ds:Erp_Tablesets_EmpBasicTableset[],
   empID:string,
   calendarID:string,
}

export interface GetNewEmpCal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param ds
      @param empID
   */  
export interface GetNewEmpLabExpRate_input{
   ds:Erp_Tablesets_EmpBasicTableset[],
   empID:string,
}

export interface GetNewEmpLabExpRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param ds
      @param empID
      @param roleCd
   */  
export interface GetNewEmpRoleRt_input{
   ds:Erp_Tablesets_EmpBasicTableset[],
   empID:string,
   roleCd:string,
}

export interface GetNewEmpRoleRt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param ds
      @param empID
   */  
export interface GetNewEmpRole_input{
   ds:Erp_Tablesets_EmpBasicTableset[],
   empID:string,
}

export interface GetNewEmpRole_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param ds
      @param relatedToFile
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param key6
   */  
export interface GetNewEntityGLC_input{
   ds:Erp_Tablesets_EmpBasicTableset[],
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   key6:string,
}

export interface GetNewEntityGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param ds
      @param partnerNum
      @param partnerType
      @param partnerID
   */  
export interface GetNewPartner_input{
   ds:Erp_Tablesets_EmpBasicTableset[],
   partnerNum:number,
   partnerType:number,
   partnerID:string,
}

export interface GetNewPartner_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param ds
      @param resourceGrpID
      @param resourceID
   */  
export interface GetNewResourceCal_input{
   ds:Erp_Tablesets_EmpBasicTableset[],
   resourceGrpID:string,
   resourceID:string,
}

export interface GetNewResourceCal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param PerConID
      @param ds
   */  
export interface GetPerConData_input{
   PerConID:number,
   ds:Erp_Tablesets_EmpBasicTableset[],
}

export interface GetPerConData_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetRowsFromList_input{
   ds:Erp_Tablesets_EmpBasicListTableset[],
}

export interface GetRowsFromList_output{
   returnObj:Erp_Tablesets_EmpBasicTableset[],
}

   /** Required : 
      @param whereClauseEmpBasic
      @param whereClauseEmpBasicAttch
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsWhoIsNotHere_input{
      /**  Whereclause for EmpBasic table.  */  
   whereClauseEmpBasic:string,
      /**  Whereclause for EmpBasicAttch table.  */  
   whereClauseEmpBasicAttch:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsWhoIsNotHere_output{
   returnObj:Erp_Tablesets_EmpBasicTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseEmpBasic
      @param whereClauseEmpBasicAttch
      @param whereClauseEmpLabExpRate
      @param whereClauseEmpCal
      @param whereClausePartner
      @param whereClauseResourceCal
      @param whereClauseEmpRole
      @param whereClauseEntityGLC
      @param whereClauseEmpRoleRt
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseEmpBasic:string,
   whereClauseEmpBasicAttch:string,
   whereClauseEmpLabExpRate:string,
   whereClauseEmpCal:string,
   whereClausePartner:string,
   whereClauseResourceCal:string,
   whereClauseEmpRole:string,
   whereClauseEntityGLC:string,
   whereClauseEmpRoleRt:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_EmpBasicTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param vTime
   */  
export interface Hours2Int_input{
   vTime:string,
}

export interface Hours2Int_output{
   returnObj:number,
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
      @param vTime
   */  
export interface Mins2Int_input{
   vTime:string,
}

export interface Mins2Int_output{
   returnObj:number,
}

   /** Required : 
      @param ds
   */  
export interface ModifySearchIDs_input{
   ds:Erp_Tablesets_EmpBasicTableset[],
}

export interface ModifySearchIDs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param ipCalendarID
      @param ds
   */  
export interface OnChangeCalendarID_input{
   ipCalendarID:string,
   ds:Erp_Tablesets_EmpBasicTableset[],
}

export interface OnChangeCalendarID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param ipCurrencyCode
      @param ds
   */  
export interface OnChangeCurrencyCode_input{
   ipCurrencyCode:string,
   ds:Erp_Tablesets_EmpBasicTableset[],
}

export interface OnChangeCurrencyCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param allowExpenses
      @param ds
   */  
export interface OnChangeExpenseAllowed_input{
   allowExpenses:boolean,
   ds:Erp_Tablesets_EmpBasicTableset[],
}

export interface OnChangeExpenseAllowed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param proposedExpenseAutoApprove
      @param ds
   */  
export interface OnChangeExpenseAutoApprove_input{
   proposedExpenseAutoApprove:boolean,
   ds:Erp_Tablesets_EmpBasicTableset[],
}

export interface OnChangeExpenseAutoApprove_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param ipVendorID
      @param ds
   */  
export interface OnChangeExpenseVendor_input{
   ipVendorID:string,
   ds:Erp_Tablesets_EmpBasicTableset[],
}

export interface OnChangeExpenseVendor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param ipEffRate
      @param ds
   */  
export interface OnChangeRateEffectiveDate_input{
   ipEffRate:string,
   ds:Erp_Tablesets_EmpBasicTableset[],
}

export interface OnChangeRateEffectiveDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param ipEndRate
      @param ds
   */  
export interface OnChangeRateEndDate_input{
   ipEndRate:string,
   ds:Erp_Tablesets_EmpBasicTableset[],
}

export interface OnChangeRateEndDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param ipResourceGrp
      @param ds
   */  
export interface OnChangeResourceGrp_input{
   ipResourceGrp:string,
   ds:Erp_Tablesets_EmpBasicTableset[],
}

export interface OnChangeResourceGrp_output{
parameters : {
      /**  output parameters  */  
   resourceMsg:string,
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param ipResource
      @param ds
   */  
export interface OnChangeResource_input{
   ipResource:string,
   ds:Erp_Tablesets_EmpBasicTableset[],
}

export interface OnChangeResource_output{
parameters : {
      /**  output parameters  */  
   resourceMsg:string,
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param ipRoleCd
      @param ds
   */  
export interface OnChangeRoleCd_input{
   ipRoleCd:string,
   ds:Erp_Tablesets_EmpBasicTableset[],
}

export interface OnChangeRoleCd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param proposedTimeAutoApprove
      @param ds
   */  
export interface OnChangeTimeAutoApprove_input{
   proposedTimeAutoApprove:boolean,
   ds:Erp_Tablesets_EmpBasicTableset[],
}

export interface OnChangeTimeAutoApprove_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param ipTimeTypeCd
      @param ds
   */  
export interface OnChangeTimeTypeCode_input{
   ipTimeTypeCd:string,
   ds:Erp_Tablesets_EmpBasicTableset[],
}

export interface OnChangeTimeTypeCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param ipColChanging
      @param ipWFGrpID
      @param ds
   */  
export interface OnChangeWFGroup_input{
      /**  The column name changing  */  
   ipColChanging:string,
      /**  The value changing  */  
   ipWFGrpID:string,
   ds:Erp_Tablesets_EmpBasicTableset[],
}

export interface OnChangeWFGroup_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtEmpBasicTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtEmpBasicTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateResourceCal_input{
   ds:Erp_Tablesets_EmpBasicTableset[],
}

export interface UpdateResourceCal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_EmpBasicTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpBasicTableset[],
}
}

   /** Required : 
      @param proposedCompany
   */  
export interface getValidCompanyName_input{
   proposedCompany:string,
}

export interface getValidCompanyName_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   errorMessage:string,
}
}

