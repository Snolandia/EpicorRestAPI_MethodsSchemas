import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.FiscalCalSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/$metadata", {
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
   Description: Get FiscalCals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FiscalCals
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FiscalCalRow
   */  
export function get_FiscalCals(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalCalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalCals", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalCalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FiscalCals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FiscalCalRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FiscalCalRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FiscalCals(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalCals", {
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
   Summary: Calls GetByID to retrieve the FiscalCal item
   Description: Calls GetByID to retrieve the FiscalCal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FiscalCal
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FiscalCalRow
   */  
export function get_FiscalCals_Company_FiscalCalendarID(Company:string, FiscalCalendarID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FiscalCalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalCals(" + Company + "," + FiscalCalendarID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FiscalCalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FiscalCal for the service
   Description: Calls UpdateExt to update FiscalCal. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FiscalCal
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FiscalCalRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FiscalCals_Company_FiscalCalendarID(Company:string, FiscalCalendarID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalCals(" + Company + "," + FiscalCalendarID + ")", {
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
   Summary: Call UpdateExt to delete FiscalCal item
   Description: Call UpdateExt to delete FiscalCal item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FiscalCal
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FiscalCals_Company_FiscalCalendarID(Company:string, FiscalCalendarID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalCals(" + Company + "," + FiscalCalendarID + ")", {
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
   Description: Get FiscalYrs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FiscalYrs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FiscalYrRow
   */  
export function get_FiscalCals_Company_FiscalCalendarID_FiscalYrs(Company:string, FiscalCalendarID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalYrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalCals(" + Company + "," + FiscalCalendarID + ")/FiscalYrs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalYrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FiscalYr item
   Description: Calls GetByID to retrieve the FiscalYr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FiscalYr1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FiscalYrRow
   */  
export function get_FiscalCals_Company_FiscalCalendarID_FiscalYrs_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix(Company:string, FiscalCalendarID:string, FiscalYear:string, FiscalYearSuffix:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FiscalYrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalCals(" + Company + "," + FiscalCalendarID + ")/FiscalYrs(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FiscalYrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get FiscalYrs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FiscalYrs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FiscalYrRow
   */  
export function get_FiscalYrs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalYrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalYrs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalYrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FiscalYrs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FiscalYrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FiscalYrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FiscalYrs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalYrs", {
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
   Summary: Calls GetByID to retrieve the FiscalYr item
   Description: Calls GetByID to retrieve the FiscalYr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FiscalYr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FiscalYrRow
   */  
export function get_FiscalYrs_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix(Company:string, FiscalCalendarID:string, FiscalYear:string, FiscalYearSuffix:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FiscalYrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalYrs(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FiscalYrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FiscalYr for the service
   Description: Calls UpdateExt to update FiscalYr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FiscalYr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FiscalYrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FiscalYrs_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix(Company:string, FiscalCalendarID:string, FiscalYear:string, FiscalYearSuffix:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalYrs(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + ")", {
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
   Summary: Call UpdateExt to delete FiscalYr item
   Description: Call UpdateExt to delete FiscalYr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FiscalYr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FiscalYrs_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix(Company:string, FiscalCalendarID:string, FiscalYear:string, FiscalYearSuffix:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalYrs(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + ")", {
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
   Description: Get FiscalPers items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FiscalPers1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FiscalPerRow
   */  
export function get_FiscalYrs_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPers(Company:string, FiscalCalendarID:string, FiscalYear:string, FiscalYearSuffix:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalPerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalYrs(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + ")/FiscalPers", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalPerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FiscalPer item
   Description: Calls GetByID to retrieve the FiscalPer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FiscalPer1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FiscalPerRow
   */  
export function get_FiscalYrs_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPers_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company:string, FiscalCalendarID:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FiscalPerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalYrs(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + ")/FiscalPers(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FiscalPerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get FiscalPers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FiscalPers
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FiscalPerRow
   */  
export function get_FiscalPers(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalPerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalPers", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   OperationID: NewUpdateExt_FiscalPers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FiscalPerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FiscalPerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FiscalPers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalPers", {
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
   Summary: Calls GetByID to retrieve the FiscalPer item
   Description: Calls GetByID to retrieve the FiscalPer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FiscalPer
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FiscalPerRow
   */  
export function get_FiscalPers_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company:string, FiscalCalendarID:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FiscalPerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalPers(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FiscalPerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FiscalPer for the service
   Description: Calls UpdateExt to update FiscalPer. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FiscalPer
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FiscalPerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FiscalPers_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company:string, FiscalCalendarID:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalPers(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")", {
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
   Summary: Call UpdateExt to delete FiscalPer item
   Description: Call UpdateExt to delete FiscalPer item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FiscalPer
      @param Company Desc: Company   Required: True   Allow empty value : True
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
export function delete_FiscalPers_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company:string, FiscalCalendarID:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalPers(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FiscalCalListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalCalListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalCalListRow)
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
export function get_GetRows(whereClauseFiscalCal:string, whereClauseFiscalYr:string, whereClauseFiscalPer:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseFiscalCal!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFiscalCal=" + whereClauseFiscalCal
   }
   if(typeof whereClauseFiscalYr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFiscalYr=" + whereClauseFiscalYr
   }
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/GetRows" + params, {
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
export function get_GetByID(fiscalCalendarID:string, epicorHeaders?:Headers){
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

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/GetList" + params, {
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
   Summary: Invoke method GetLinkedBooks
   Description: Get list of GL Books which are referenced by this calendar.
   OperationID: GetLinkedBooks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLinkedBooks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLinkedBooks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLinkedBooks(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/GetLinkedBooks", {
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
   Summary: Invoke method UpdateLinkedBooksWithBalFmtChg
   Description: Update each referenced GL book with COABalFmtChg = true
   OperationID: UpdateLinkedBooksWithBalFmtChg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateLinkedBooksWithBalFmtChg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateLinkedBooksWithBalFmtChg_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateLinkedBooksWithBalFmtChg(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/UpdateLinkedBooksWithBalFmtChg", {
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
   Summary: Invoke method CalculateITPeriodDflts
   Description: Uses Income Tax Fiscal Year values to populate all its related fiscal Periods. Method only used for MX Localization.
   OperationID: CalculateITPeriodDflts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateITPeriodDflts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateITPeriodDflts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalculateITPeriodDflts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/CalculateITPeriodDflts", {
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
   Summary: Invoke method deletebulk
   OperationID: deletebulk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/deletebulk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/deletebulk_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_deletebulk(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/deletebulk", {
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
   Summary: Invoke method GeneratePeriods
   Description: Get dataset record for Generate Fiscal Periods functionality.
   OperationID: GeneratePeriods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GeneratePeriods_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GeneratePeriods_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GeneratePeriods(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/GeneratePeriods", {
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
   Summary: Invoke method GetFiscalPerGenerate
   Description: Get dataset record for Generate Fiscal Periods functionality.
   OperationID: GetFiscalPerGenerate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFiscalPerGenerate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFiscalPerGenerate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFiscalPerGenerate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/GetFiscalPerGenerate", {
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
   Summary: Invoke method GetGLJrnDtlInYear
   OperationID: GetGLJrnDtlInYear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGLJrnDtlInYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLJrnDtlInYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGLJrnDtlInYear(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/GetGLJrnDtlInYear", {
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
   Summary: Invoke method GetGLJrnDtlByPeriods
   OperationID: GetGLJrnDtlByPeriods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGLJrnDtlByPeriods_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLJrnDtlByPeriods_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGLJrnDtlByPeriods(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/GetGLJrnDtlByPeriods", {
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
   Summary: Invoke method GetFiscalCal
   Description: Returns Calendar defined in company
   OperationID: GetFiscalCal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFiscalCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFiscalCal(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/GetFiscalCal", {
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
   Summary: Invoke method CheckDataInGLJrnDtl
   OperationID: CheckDataInGLJrnDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDataInGLJrnDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDataInGLJrnDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDataInGLJrnDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/CheckDataInGLJrnDtl", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/GetCodeDescList", {
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
   Summary: Invoke method SetFiscalYrDefaults
   Description: Sets default references on Previous and Next Fiscal Years, Start and End Dates depending on Fiscal Year and Fiscal Year Suffix entered
   OperationID: SetFiscalYrDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetFiscalYrDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetFiscalYrDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetFiscalYrDefaults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/SetFiscalYrDefaults", {
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
   Summary: Invoke method CheckIncompleteFiscalYear
   Description: Throws exception if EndDate of at least one Fiscal Year in the Calendar is not covered by corresponding Fiscal Period
   OperationID: CheckIncompleteFiscalYear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckIncompleteFiscalYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIncompleteFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckIncompleteFiscalYear(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/CheckIncompleteFiscalYear", {
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
   Summary: Invoke method GetNewFiscalCal
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFiscalCal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFiscalCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFiscalCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFiscalCal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/GetNewFiscalCal", {
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
   Summary: Invoke method GetNewFiscalYr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFiscalYr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFiscalYr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFiscalYr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFiscalYr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/GetNewFiscalYr", {
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
   Summary: Invoke method GetNewFiscalPer
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFiscalPer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFiscalPer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFiscalPer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFiscalPer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/GetNewFiscalPer", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalCalListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FiscalCalListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalCalRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FiscalCalRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalPerRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FiscalPerRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalYrRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FiscalYrRow[],
}

export interface Erp_Tablesets_FiscalCalListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The unique identifier of the fiscal calendar.  */  
   "FiscalCalendarID":string,
      /**  Calendar description.  */  
   "Description":string,
      /**  The start date of the fiscal calendar.  */  
   "StartDate":string,
      /**  The end date of the fiscal calendar.  */  
   "EndDate":string,
      /**  Determines whether or not this calendar is shared between more than one company.  */  
   "GlobalCal":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FiscalCalRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The unique identifier of the fiscal calendar.  */  
   "FiscalCalendarID":string,
      /**  Calendar description.  */  
   "Description":string,
      /**  The start date of the fiscal calendar.  */  
   "StartDate":string,
      /**  The end date of the fiscal calendar.  */  
   "EndDate":string,
      /**  Determines whether or not this calendar is shared between more than one company.  */  
   "GlobalCal":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
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

export interface Erp_Tablesets_FiscalYrRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The id of the fiscal calendar this record is related to.  */  
   "FiscalCalendarID":string,
      /**  The fiscal year.  */  
   "FiscalYear":number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal year start date.  */  
   "StartDate":string,
      /**  The fiscal year end date.  */  
   "EndDate":string,
      /**  The number of ordinary fiscal periods in the year.  */  
   "NumPeriods":number,
      /**  The number of closing periods for the fiscal year.  Can be zero.  */  
   "NumClosingPeriods":number,
      /**  The next fiscal year (next FiscalYr record).  */  
   "NextFiscalYear":number,
      /**  The next fiscal year suffix.  */  
   "NextFiscalYearSuffix":string,
      /**  The previous fiscal year (previous FiscalYr record).  */  
   "PrevFiscalYear":number,
      /**  The previous fiscal year suffix.  */  
   "PrevFiscalYearSuffix":string,
      /**  Fiscal year description.  */  
   "Description":string,
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
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Concatenation of Year and Suffix for tree view.  */  
   "YearSuffix":string,
      /**  Indicates if StartDate is available for input.  */  
   "EnableStartDate":boolean,
      /**  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  */  
   "ITUpdateRate":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ipFiscalCalendarID
      @param ipFiscalYear
      @param ipFiscalYearSuffix
      @param ds
   */  
export interface CalculateITPeriodDflts_input{
      /**  current Fiscal Calendar ID  */  
   ipFiscalCalendarID:string,
      /**  current Fiscal Year  */  
   ipFiscalYear:number,
      /**  current Fiscal Year Suffix.  */  
   ipFiscalYearSuffix:string,
   ds:Erp_Tablesets_FiscalCalTableset[],
}

export interface CalculateITPeriodDflts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FiscalCalTableset[],
}
}

   /** Required : 
      @param cFiscalCalendarID
      @param iFiscalYear
      @param cFiscalYearSuffix
      @param iFiscalPeriod
      @param dStartDate
      @param dEndDate
      @param iWorkMode
   */  
export interface CheckDataInGLJrnDtl_input{
   cFiscalCalendarID:string,
   iFiscalYear:number,
   cFiscalYearSuffix:string,
   iFiscalPeriod:number,
   dStartDate:string,
   dEndDate:string,
   iWorkMode:number,
}

export interface CheckDataInGLJrnDtl_output{
   returnObj:number,
parameters : {
      /**  output parameters  */  
   cBookID:string,
   cJournalCode:string,
   iJournalNum:number,
   iJournalLine:number,
}
}

   /** Required : 
      @param fiscalCalendarID
   */  
export interface CheckIncompleteFiscalYear_input{
      /**  Fiscal Calendar ID  */  
   fiscalCalendarID:string,
}

export interface CheckIncompleteFiscalYear_output{
}

   /** Required : 
      @param fiscalCalendarID
   */  
export interface DeleteByID_input{
   fiscalCalendarID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_FiscalCalListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The unique identifier of the fiscal calendar.  */  
   FiscalCalendarID:string,
      /**  Calendar description.  */  
   Description:string,
      /**  The start date of the fiscal calendar.  */  
   StartDate:string,
      /**  The end date of the fiscal calendar.  */  
   EndDate:string,
      /**  Determines whether or not this calendar is shared between more than one company.  */  
   GlobalCal:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FiscalCalListTableset{
   FiscalCalList:Erp_Tablesets_FiscalCalListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FiscalCalRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The unique identifier of the fiscal calendar.  */  
   FiscalCalendarID:string,
      /**  Calendar description.  */  
   Description:string,
      /**  The start date of the fiscal calendar.  */  
   StartDate:string,
      /**  The end date of the fiscal calendar.  */  
   EndDate:string,
      /**  Determines whether or not this calendar is shared between more than one company.  */  
   GlobalCal:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FiscalCalTableset{
   FiscalCal:Erp_Tablesets_FiscalCalRow[],
   FiscalYr:Erp_Tablesets_FiscalYrRow[],
   FiscalPer:Erp_Tablesets_FiscalPerRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FiscalPerGenerateRow{
   Company:string,
   FiscalCalendarID:string,
   FiscalYear:number,
   FiscalYearSuffix:string,
   StartDate:string,
   EndDate:string,
   PeriodDuration:number,
   DurationType:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FiscalPerGenerateTableset{
   FiscalPerGenerate:Erp_Tablesets_FiscalPerGenerateRow[],
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

export interface Erp_Tablesets_FiscalYrRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The id of the fiscal calendar this record is related to.  */  
   FiscalCalendarID:string,
      /**  The fiscal year.  */  
   FiscalYear:number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   FiscalYearSuffix:string,
      /**  The fiscal year start date.  */  
   StartDate:string,
      /**  The fiscal year end date.  */  
   EndDate:string,
      /**  The number of ordinary fiscal periods in the year.  */  
   NumPeriods:number,
      /**  The number of closing periods for the fiscal year.  Can be zero.  */  
   NumClosingPeriods:number,
      /**  The next fiscal year (next FiscalYr record).  */  
   NextFiscalYear:number,
      /**  The next fiscal year suffix.  */  
   NextFiscalYearSuffix:string,
      /**  The previous fiscal year (previous FiscalYr record).  */  
   PrevFiscalYear:number,
      /**  The previous fiscal year suffix.  */  
   PrevFiscalYearSuffix:string,
      /**  Fiscal year description.  */  
   Description:string,
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
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Concatenation of Year and Suffix for tree view.  */  
   YearSuffix:string,
      /**  Indicates if StartDate is available for input.  */  
   EnableStartDate:boolean,
      /**  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  */  
   ITUpdateRate:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtFiscalCalTableset{
   FiscalCal:Erp_Tablesets_FiscalCalRow[],
   FiscalYr:Erp_Tablesets_FiscalYrRow[],
   FiscalPer:Erp_Tablesets_FiscalPerRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
   */  
export interface GeneratePeriods_input{
   ds:Erp_Tablesets_FiscalPerGenerateTableset[],
}

export interface GeneratePeriods_output{
   returnObj:Erp_Tablesets_FiscalCalTableset[],
parameters : {
      /**  output parameters  */  
   cOutMessage:string,
}
}

   /** Required : 
      @param fiscalCalendarID
   */  
export interface GetByID_input{
   fiscalCalendarID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_FiscalCalTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_FiscalCalTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_FiscalCalTableset[],
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

export interface GetFiscalCal_output{
   returnObj:string,
}

   /** Required : 
      @param cFiscalCalendarID
      @param iFiscalYear
      @param cFiscalYearSuffix
   */  
export interface GetFiscalPerGenerate_input{
      /**  The Fiscal Calendar ID  */  
   cFiscalCalendarID:string,
      /**  The Fiscal Year  */  
   iFiscalYear:number,
      /**  The Fiscal Year Suffix  */  
   cFiscalYearSuffix:string,
}

export interface GetFiscalPerGenerate_output{
   returnObj:Erp_Tablesets_FiscalPerGenerateTableset[],
}

   /** Required : 
      @param cFiscalCalendarID
      @param iFiscalYear
      @param cFiscalYearSuffix
      @param iFiscalPeriodFrom
      @param iWorkMode
   */  
export interface GetGLJrnDtlByPeriods_input{
   cFiscalCalendarID:string,
   iFiscalYear:number,
   cFiscalYearSuffix:string,
   iFiscalPeriodFrom:number,
   iWorkMode:number,
}

export interface GetGLJrnDtlByPeriods_output{
parameters : {
      /**  output parameters  */  
   lIsGetIt:number,
   cBookID:string,
   cJournalCode:string,
   iJournalNum:number,
   iJournalLine:number,
   iFiscalYearOut:number,
   cFiscalYearSuffixOut:string,
   iFiscalPeriodOut:number,
}
}

   /** Required : 
      @param cFiscalCalendarID
      @param iFiscalYear
      @param cFiscalYearSuffix
      @param iFiscalPeriodFrom
      @param iWorkMode
   */  
export interface GetGLJrnDtlInYear_input{
   cFiscalCalendarID:string,
   iFiscalYear:number,
   cFiscalYearSuffix:string,
   iFiscalPeriodFrom:number,
   iWorkMode:number,
}

export interface GetGLJrnDtlInYear_output{
parameters : {
      /**  output parameters  */  
   lIsGetIt:number,
   cBookID:string,
   cJournalCode:string,
   iJournalNum:number,
   iJournalLine:number,
   iFiscalYearOut:number,
   cFiscalYearSuffixOut:string,
   iFiscalPeriodOut:number,
}
}

   /** Required : 
      @param fiscalCalendarID
   */  
export interface GetLinkedBooks_input{
      /**  Fiscal Calendar ID  */  
   fiscalCalendarID:string,
}

export interface GetLinkedBooks_output{
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
   returnObj:Erp_Tablesets_FiscalCalListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewFiscalCal_input{
   ds:Erp_Tablesets_FiscalCalTableset[],
}

export interface GetNewFiscalCal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FiscalCalTableset[],
}
}

   /** Required : 
      @param ds
      @param fiscalCalendarID
      @param fiscalYear
      @param fiscalYearSuffix
   */  
export interface GetNewFiscalPer_input{
   ds:Erp_Tablesets_FiscalCalTableset[],
   fiscalCalendarID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
}

export interface GetNewFiscalPer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FiscalCalTableset[],
}
}

   /** Required : 
      @param ds
      @param fiscalCalendarID
      @param fiscalYear
   */  
export interface GetNewFiscalYr_input{
   ds:Erp_Tablesets_FiscalCalTableset[],
   fiscalCalendarID:string,
   fiscalYear:number,
}

export interface GetNewFiscalYr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FiscalCalTableset[],
}
}

   /** Required : 
      @param whereClauseFiscalCal
      @param whereClauseFiscalYr
      @param whereClauseFiscalPer
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseFiscalCal:string,
   whereClauseFiscalYr:string,
   whereClauseFiscalPer:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_FiscalCalTableset[],
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
   */  
export interface SetFiscalYrDefaults_input{
   ds:Erp_Tablesets_FiscalCalTableset[],
}

export interface SetFiscalYrDefaults_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FiscalCalTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtFiscalCalTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtFiscalCalTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param fiscalCalendarID
   */  
export interface UpdateLinkedBooksWithBalFmtChg_input{
   fiscalCalendarID:string,
}

export interface UpdateLinkedBooksWithBalFmtChg_output{
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_FiscalCalTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FiscalCalTableset[],
}
}

   /** Required : 
      @param ipFiscalCalendarID
      @param ipFiscalYear
      @param ipFiscalYearSuffix
      @param ds
   */  
export interface deletebulk_input{
   ipFiscalCalendarID:string,
   ipFiscalYear:number,
   ipFiscalYearSuffix:string,
   ds:Erp_Tablesets_FiscalCalTableset[],
}

export interface deletebulk_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FiscalCalTableset[],
}
}

