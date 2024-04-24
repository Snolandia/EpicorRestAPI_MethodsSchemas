import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ConsMonitorSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/$metadata", {
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
   Description: Get ConsMonitors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConsMonitors
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CompanyRow
   */  
export function get_ConsMonitors(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CompanyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsMonitors", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CompanyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConsMonitors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CompanyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CompanyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConsMonitors(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsMonitors", {
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
   Summary: Calls GetByID to retrieve the ConsMonitor item
   Description: Calls GetByID to retrieve the ConsMonitor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsMonitor
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CompanyRow
   */  
export function get_ConsMonitors_Company(Company:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CompanyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsMonitors(" + Company + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CompanyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ConsMonitor for the service
   Description: Calls UpdateExt to update ConsMonitor. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConsMonitor
      @param Company Desc: Company   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CompanyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ConsMonitors_Company(Company:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsMonitors(" + Company + ")", {
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
   Summary: Call UpdateExt to delete ConsMonitor item
   Description: Call UpdateExt to delete ConsMonitor item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConsMonitor
      @param Company Desc: Company   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ConsMonitors_Company(Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsMonitors(" + Company + ")", {
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
   Description: Get ConsTgtDefs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ConsTgtDefs1
      @param Company Desc: Company   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtDefRow
   */  
export function get_ConsMonitors_Company_ConsTgtDefs(Company:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsMonitors(" + Company + ")/ConsTgtDefs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ConsTgtDef item
   Description: Calls GetByID to retrieve the ConsTgtDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsTgtDef1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConsDefID Desc: ConsDefID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsTgtDefRow
   */  
export function get_ConsMonitors_Company_ConsTgtDefs_Company_ConsDefID(Company:string, ConsDefID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ConsTgtDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsMonitors(" + Company + ")/ConsTgtDefs(" + Company + "," + ConsDefID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ConsTgtDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ConsTgtDefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConsTgtDefs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtDefRow
   */  
export function get_ConsTgtDefs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtDefs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConsTgtDefs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ConsTgtDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ConsTgtDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConsTgtDefs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtDefs", {
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
   Summary: Calls GetByID to retrieve the ConsTgtDef item
   Description: Calls GetByID to retrieve the ConsTgtDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsTgtDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConsDefID Desc: ConsDefID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsTgtDefRow
   */  
export function get_ConsTgtDefs_Company_ConsDefID(Company:string, ConsDefID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ConsTgtDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtDefs(" + Company + "," + ConsDefID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ConsTgtDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ConsTgtDef for the service
   Description: Calls UpdateExt to update ConsTgtDef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConsTgtDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConsDefID Desc: ConsDefID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ConsTgtDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ConsTgtDefs_Company_ConsDefID(Company:string, ConsDefID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtDefs(" + Company + "," + ConsDefID + ")", {
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
   Summary: Call UpdateExt to delete ConsTgtDef item
   Description: Call UpdateExt to delete ConsTgtDef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConsTgtDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConsDefID Desc: ConsDefID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ConsTgtDefs_Company_ConsDefID(Company:string, ConsDefID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtDefs(" + Company + "," + ConsDefID + ")", {
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
   Description: Get ConsTgtGens items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ConsTgtGens1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConsDefID Desc: ConsDefID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtGenRow
   */  
export function get_ConsTgtDefs_Company_ConsDefID_ConsTgtGens(Company:string, ConsDefID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtGenRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtDefs(" + Company + "," + ConsDefID + ")/ConsTgtGens", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtGenRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ConsTgtGen item
   Description: Calls GetByID to retrieve the ConsTgtGen item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsTgtGen1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConsDefID Desc: ConsDefID   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsTgtGenRow
   */  
export function get_ConsTgtDefs_Company_ConsDefID_ConsTgtGens_Company_GenID(Company:string, ConsDefID:string, GenID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ConsTgtGenRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtDefs(" + Company + "," + ConsDefID + ")/ConsTgtGens(" + Company + "," + GenID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ConsTgtGenRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ConsTgtSrcs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ConsTgtSrcs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConsDefID Desc: ConsDefID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtSrcRow
   */  
export function get_ConsTgtDefs_Company_ConsDefID_ConsTgtSrcs(Company:string, ConsDefID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtSrcRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtDefs(" + Company + "," + ConsDefID + ")/ConsTgtSrcs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtSrcRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ConsTgtSrc item
   Description: Calls GetByID to retrieve the ConsTgtSrc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsTgtSrc1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConsDefID Desc: ConsDefID   Required: True   Allow empty value : True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsTgtSrcRow
   */  
export function get_ConsTgtDefs_Company_ConsDefID_ConsTgtSrcs_Company_ConsDefID_SourceBook(Company:string, ConsDefID:string, SourceBook:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ConsTgtSrcRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtDefs(" + Company + "," + ConsDefID + ")/ConsTgtSrcs(" + Company + "," + ConsDefID + "," + SourceBook + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ConsTgtSrcRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ConsTgtGens items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConsTgtGens
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtGenRow
   */  
export function get_ConsTgtGens(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtGenRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtGens", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtGenRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConsTgtGens
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ConsTgtGenRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ConsTgtGenRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConsTgtGens(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtGens", {
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
   Summary: Calls GetByID to retrieve the ConsTgtGen item
   Description: Calls GetByID to retrieve the ConsTgtGen item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsTgtGen
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsTgtGenRow
   */  
export function get_ConsTgtGens_Company_GenID(Company:string, GenID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ConsTgtGenRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtGens(" + Company + "," + GenID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ConsTgtGenRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ConsTgtGen for the service
   Description: Calls UpdateExt to update ConsTgtGen. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConsTgtGen
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ConsTgtGenRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ConsTgtGens_Company_GenID(Company:string, GenID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtGens(" + Company + "," + GenID + ")", {
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
   Summary: Call UpdateExt to delete ConsTgtGen item
   Description: Call UpdateExt to delete ConsTgtGen item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConsTgtGen
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ConsTgtGens_Company_GenID(Company:string, GenID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtGens(" + Company + "," + GenID + ")", {
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
   Description: Get ConsSrcCtrls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ConsSrcCtrls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsSrcCtrlRow
   */  
export function get_ConsTgtGens_Company_GenID_ConsSrcCtrls(Company:string, GenID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsSrcCtrlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtGens(" + Company + "," + GenID + ")/ConsSrcCtrls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsSrcCtrlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ConsSrcCtrl item
   Description: Calls GetByID to retrieve the ConsSrcCtrl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsSrcCtrl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsSrcCtrlRow
   */  
export function get_ConsTgtGens_Company_GenID_ConsSrcCtrls_Company_GenID_SourceBook(Company:string, GenID:string, SourceBook:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ConsSrcCtrlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtGens(" + Company + "," + GenID + ")/ConsSrcCtrls(" + Company + "," + GenID + "," + SourceBook + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ConsSrcCtrlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ConsSrcCtrls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConsSrcCtrls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsSrcCtrlRow
   */  
export function get_ConsSrcCtrls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsSrcCtrlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsSrcCtrls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsSrcCtrlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConsSrcCtrls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ConsSrcCtrlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ConsSrcCtrlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConsSrcCtrls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsSrcCtrls", {
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
   Summary: Calls GetByID to retrieve the ConsSrcCtrl item
   Description: Calls GetByID to retrieve the ConsSrcCtrl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsSrcCtrl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsSrcCtrlRow
   */  
export function get_ConsSrcCtrls_Company_GenID_SourceBook(Company:string, GenID:string, SourceBook:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ConsSrcCtrlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsSrcCtrls(" + Company + "," + GenID + "," + SourceBook + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ConsSrcCtrlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ConsSrcCtrl for the service
   Description: Calls UpdateExt to update ConsSrcCtrl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConsSrcCtrl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ConsSrcCtrlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ConsSrcCtrls_Company_GenID_SourceBook(Company:string, GenID:string, SourceBook:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsSrcCtrls(" + Company + "," + GenID + "," + SourceBook + ")", {
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
   Summary: Call UpdateExt to delete ConsSrcCtrl item
   Description: Call UpdateExt to delete ConsSrcCtrl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConsSrcCtrl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ConsSrcCtrls_Company_GenID_SourceBook(Company:string, GenID:string, SourceBook:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsSrcCtrls(" + Company + "," + GenID + "," + SourceBook + ")", {
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
   Description: Get ConsSrcRates items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ConsSrcRates1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsSrcRatesRow
   */  
export function get_ConsSrcCtrls_Company_GenID_SourceBook_ConsSrcRates(Company:string, GenID:string, SourceBook:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsSrcRatesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsSrcCtrls(" + Company + "," + GenID + "," + SourceBook + ")/ConsSrcRates", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsSrcRatesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ConsSrcRate item
   Description: Calls GetByID to retrieve the ConsSrcRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsSrcRate1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param RateTypeID Desc: RateTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsSrcRatesRow
   */  
export function get_ConsSrcCtrls_Company_GenID_SourceBook_ConsSrcRates_Company_GenID_SourceBook_FiscalYear_FiscalYearSuffix_FiscalPeriod_RateTypeID(Company:string, GenID:string, SourceBook:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, RateTypeID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ConsSrcRatesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsSrcCtrls(" + Company + "," + GenID + "," + SourceBook + ")/ConsSrcRates(" + Company + "," + GenID + "," + SourceBook + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + RateTypeID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ConsSrcRatesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ConsSrcRates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConsSrcRates
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsSrcRatesRow
   */  
export function get_ConsSrcRates(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsSrcRatesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsSrcRates", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsSrcRatesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConsSrcRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ConsSrcRatesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ConsSrcRatesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConsSrcRates(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsSrcRates", {
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
   Summary: Calls GetByID to retrieve the ConsSrcRate item
   Description: Calls GetByID to retrieve the ConsSrcRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsSrcRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param RateTypeID Desc: RateTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsSrcRatesRow
   */  
export function get_ConsSrcRates_Company_GenID_SourceBook_FiscalYear_FiscalYearSuffix_FiscalPeriod_RateTypeID(Company:string, GenID:string, SourceBook:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, RateTypeID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ConsSrcRatesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsSrcRates(" + Company + "," + GenID + "," + SourceBook + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + RateTypeID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ConsSrcRatesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ConsSrcRate for the service
   Description: Calls UpdateExt to update ConsSrcRate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConsSrcRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param RateTypeID Desc: RateTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ConsSrcRatesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ConsSrcRates_Company_GenID_SourceBook_FiscalYear_FiscalYearSuffix_FiscalPeriod_RateTypeID(Company:string, GenID:string, SourceBook:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, RateTypeID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsSrcRates(" + Company + "," + GenID + "," + SourceBook + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + RateTypeID + ")", {
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
   Summary: Call UpdateExt to delete ConsSrcRate item
   Description: Call UpdateExt to delete ConsSrcRate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConsSrcRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param FiscalPeriod Desc: FiscalPeriod   Required: True
      @param RateTypeID Desc: RateTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ConsSrcRates_Company_GenID_SourceBook_FiscalYear_FiscalYearSuffix_FiscalPeriod_RateTypeID(Company:string, GenID:string, SourceBook:string, FiscalYear:string, FiscalYearSuffix:string, FiscalPeriod:string, RateTypeID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsSrcRates(" + Company + "," + GenID + "," + SourceBook + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + RateTypeID + ")", {
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
   Description: Get ConsTgtSrcs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConsTgtSrcs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtSrcRow
   */  
export function get_ConsTgtSrcs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtSrcRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtSrcs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtSrcRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConsTgtSrcs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ConsTgtSrcRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ConsTgtSrcRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConsTgtSrcs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtSrcs", {
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
   Summary: Calls GetByID to retrieve the ConsTgtSrc item
   Description: Calls GetByID to retrieve the ConsTgtSrc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsTgtSrc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConsDefID Desc: ConsDefID   Required: True   Allow empty value : True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsTgtSrcRow
   */  
export function get_ConsTgtSrcs_Company_ConsDefID_SourceBook(Company:string, ConsDefID:string, SourceBook:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ConsTgtSrcRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtSrcs(" + Company + "," + ConsDefID + "," + SourceBook + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ConsTgtSrcRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ConsTgtSrc for the service
   Description: Calls UpdateExt to update ConsTgtSrc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConsTgtSrc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConsDefID Desc: ConsDefID   Required: True   Allow empty value : True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ConsTgtSrcRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ConsTgtSrcs_Company_ConsDefID_SourceBook(Company:string, ConsDefID:string, SourceBook:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtSrcs(" + Company + "," + ConsDefID + "," + SourceBook + ")", {
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
   Summary: Call UpdateExt to delete ConsTgtSrc item
   Description: Call UpdateExt to delete ConsTgtSrc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConsTgtSrc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConsDefID Desc: ConsDefID   Required: True   Allow empty value : True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ConsTgtSrcs_Company_ConsDefID_SourceBook(Company:string, ConsDefID:string, SourceBook:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtSrcs(" + Company + "," + ConsDefID + "," + SourceBook + ")", {
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
   Description: Get ConsTgtGenTemps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ConsTgtGenTemps1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConsDefID Desc: ConsDefID   Required: True   Allow empty value : True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtGenTempRow
   */  
export function get_ConsTgtSrcs_Company_ConsDefID_SourceBook_ConsTgtGenTemps(Company:string, ConsDefID:string, SourceBook:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtGenTempRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtSrcs(" + Company + "," + ConsDefID + "," + SourceBook + ")/ConsTgtGenTemps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtGenTempRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ConsTgtGenTemp item
   Description: Calls GetByID to retrieve the ConsTgtGenTemp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsTgtGenTemp1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConsDefID Desc: ConsDefID   Required: True   Allow empty value : True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsTgtGenTempRow
   */  
export function get_ConsTgtSrcs_Company_ConsDefID_SourceBook_ConsTgtGenTemps_Company_ConsDefID_GenID_SourceBook(Company:string, ConsDefID:string, SourceBook:string, GenID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ConsTgtGenTempRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtSrcs(" + Company + "," + ConsDefID + "," + SourceBook + ")/ConsTgtGenTemps(" + Company + "," + ConsDefID + "," + GenID + "," + SourceBook + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ConsTgtGenTempRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ConsTgtGenTemps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConsTgtGenTemps
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtGenTempRow
   */  
export function get_ConsTgtGenTemps(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtGenTempRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtGenTemps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtGenTempRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConsTgtGenTemps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ConsTgtGenTempRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ConsTgtGenTempRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConsTgtGenTemps(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtGenTemps", {
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
   Summary: Calls GetByID to retrieve the ConsTgtGenTemp item
   Description: Calls GetByID to retrieve the ConsTgtGenTemp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsTgtGenTemp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConsDefID Desc: ConsDefID   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsTgtGenTempRow
   */  
export function get_ConsTgtGenTemps_Company_ConsDefID_GenID_SourceBook(Company:string, ConsDefID:string, GenID:string, SourceBook:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ConsTgtGenTempRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtGenTemps(" + Company + "," + ConsDefID + "," + GenID + "," + SourceBook + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ConsTgtGenTempRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ConsTgtGenTemp for the service
   Description: Calls UpdateExt to update ConsTgtGenTemp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConsTgtGenTemp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConsDefID Desc: ConsDefID   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ConsTgtGenTempRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ConsTgtGenTemps_Company_ConsDefID_GenID_SourceBook(Company:string, ConsDefID:string, GenID:string, SourceBook:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtGenTemps(" + Company + "," + ConsDefID + "," + GenID + "," + SourceBook + ")", {
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
   Summary: Call UpdateExt to delete ConsTgtGenTemp item
   Description: Call UpdateExt to delete ConsTgtGenTemp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConsTgtGenTemp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConsDefID Desc: ConsDefID   Required: True   Allow empty value : True
      @param GenID Desc: GenID   Required: True
      @param SourceBook Desc: SourceBook   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ConsTgtGenTemps_Company_ConsDefID_GenID_SourceBook(Company:string, ConsDefID:string, GenID:string, SourceBook:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtGenTemps(" + Company + "," + ConsDefID + "," + GenID + "," + SourceBook + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CompanyListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CompanyListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CompanyListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseCompany:string, whereClauseConsTgtDef:string, whereClauseConsTgtGen:string, whereClauseConsSrcCtrl:string, whereClauseConsSrcRates:string, whereClauseConsTgtSrc:string, whereClauseConsTgtGenTemp:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCompany!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCompany=" + whereClauseCompany
   }
   if(typeof whereClauseConsTgtDef!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseConsTgtDef=" + whereClauseConsTgtDef
   }
   if(typeof whereClauseConsTgtGen!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseConsTgtGen=" + whereClauseConsTgtGen
   }
   if(typeof whereClauseConsSrcCtrl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseConsSrcCtrl=" + whereClauseConsSrcCtrl
   }
   if(typeof whereClauseConsSrcRates!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseConsSrcRates=" + whereClauseConsSrcRates
   }
   if(typeof whereClauseConsTgtSrc!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseConsTgtSrc=" + whereClauseConsTgtSrc
   }
   if(typeof whereClauseConsTgtGenTemp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseConsTgtGenTemp=" + whereClauseConsTgtGenTemp
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/GetByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/GetList" + params, {
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
   Summary: Invoke method GetSelectDefaults
   Description: Get the select default values
   OperationID: GetSelectDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectDefaults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/GetSelectDefaults", {
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
   Summary: Invoke method GetSelectDefaultsWithCalendarID
   Description: Get the select default values for Book
   OperationID: GetSelectDefaultsWithCalendarID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectDefaultsWithCalendarID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectDefaultsWithCalendarID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectDefaultsWithCalendarID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/GetSelectDefaultsWithCalendarID", {
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
   Summary: Invoke method GetSelectYearDefaultsWithCalendarID
   Description: Get the select default values for Book and Year
   OperationID: GetSelectYearDefaultsWithCalendarID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectYearDefaultsWithCalendarID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectYearDefaultsWithCalendarID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectYearDefaultsWithCalendarID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/GetSelectYearDefaultsWithCalendarID", {
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
   Summary: Invoke method GetSelectYearSuffixDefaultsWithCalendarID
   Description: Get the select default values for Book, Year and YearSuffix
   OperationID: GetSelectYearSuffixDefaultsWithCalendarID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectYearSuffixDefaultsWithCalendarID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectYearSuffixDefaultsWithCalendarID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectYearSuffixDefaultsWithCalendarID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/GetSelectYearSuffixDefaultsWithCalendarID", {
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
   Summary: Invoke method OnChangeSelectFiscalInfo
   Description: On change fiscal information from selection section.
   OperationID: OnChangeSelectFiscalInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSelectFiscalInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSelectFiscalInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSelectFiscalInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/OnChangeSelectFiscalInfo", {
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
   Summary: Invoke method ValidateTargetBook
   Description: Validate book when is selected.
   OperationID: ValidateTargetBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateTargetBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateTargetBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateTargetBook(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ValidateTargetBook", {
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
   Summary: Invoke method ValidateSelectFiscalInfo
   Description: Validate when fiscal info changed.
   OperationID: ValidateSelectFiscalInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSelectFiscalInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSelectFiscalInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSelectFiscalInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ValidateSelectFiscalInfo", {
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
   Summary: Invoke method ValidateSelectFiscalYearSuffixInfo
   Description: Validate when fiscal info changed.
   OperationID: ValidateSelectFiscalYearSuffixInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSelectFiscalYearSuffixInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSelectFiscalYearSuffixInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSelectFiscalYearSuffixInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ValidateSelectFiscalYearSuffixInfo", {
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
   Summary: Invoke method ValidateSelectFiscalYearInfo
   Description: Validate when fiscal info changed.
   OperationID: ValidateSelectFiscalYearInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSelectFiscalYearInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSelectFiscalYearInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSelectFiscalYearInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ValidateSelectFiscalYearInfo", {
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
   Summary: Invoke method GetRowsMonitor
   Description: Retrieve all records for Monitor
   OperationID: GetRowsMonitor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsMonitor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsMonitor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsMonitor(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/GetRowsMonitor", {
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
   Summary: Invoke method GetDefinitionMonitor
   OperationID: GetDefinitionMonitor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefinitionMonitor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefinitionMonitor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefinitionMonitor(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/GetDefinitionMonitor", {
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
   Summary: Invoke method GetNewCompany
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCompany(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/GetNewCompany", {
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
   Summary: Invoke method GetNewConsTgtDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewConsTgtDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewConsTgtDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConsTgtDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewConsTgtDef(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/GetNewConsTgtDef", {
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
   Summary: Invoke method GetNewConsTgtGen
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewConsTgtGen
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewConsTgtGen_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConsTgtGen_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewConsTgtGen(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/GetNewConsTgtGen", {
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
   Summary: Invoke method GetNewConsSrcCtrl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewConsSrcCtrl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewConsSrcCtrl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConsSrcCtrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewConsSrcCtrl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/GetNewConsSrcCtrl", {
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
   Summary: Invoke method GetNewConsSrcRates
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewConsSrcRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewConsSrcRates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConsSrcRates_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewConsSrcRates(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/GetNewConsSrcRates", {
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
   Summary: Invoke method GetNewConsTgtSrc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewConsTgtSrc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewConsTgtSrc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConsTgtSrc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewConsTgtSrc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/GetNewConsTgtSrc", {
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
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CompanyListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CompanyListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CompanyRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CompanyRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsSrcCtrlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ConsSrcCtrlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsSrcRatesRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ConsSrcRatesRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtDefRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ConsTgtDefRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtGenRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ConsTgtGenRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtGenTempRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ConsTgtGenTempRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtSrcRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ConsTgtSrcRow[],
}

export interface Erp_Tablesets_CompanyListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Company Name  */  
   "Name":string,
      /**  First company address line.  */  
   "Address1":string,
      /**  City portion of company address.  */  
   "City":string,
      /**  State portion of company address.  */  
   "State":string,
      /**  Postal code or zip code portion of company address.  */  
   "Zip":string,
      /**  Company phone number  */  
   "PhoneNum":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CompanyRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Company Name  */  
   "Name":string,
      /**  First company address line.  */  
   "Address1":string,
      /**  Second company address line.  */  
   "Address2":string,
      /**  Third company address line.  */  
   "Address3":string,
      /**  City portion of company address.  */  
   "City":string,
      /**  State portion of company address.  */  
   "State":string,
      /**  Postal code or zip code portion of company address.  */  
   "Zip":string,
      /**  Country portion of company address.  */  
   "Country":string,
      /**  Company phone number  */  
   "PhoneNum":string,
      /**  Company fax number  */  
   "FaxNum":string,
      /**  Federal Income Tax Number  */  
   "FEIN":string,
      /**  State Tax ID  */  
   "StateTaxID":string,
      /**  Current fiscal year  */  
   "CurrentFiscalYear":number,
      /**  This is the Trading Partner ID that is used for incoming and outgoing EDI.  */  
   "EDICode":string,
      /**  The Tax Region Code for this company. This tax region is used to define the 'interior'. It is used as a default tax region in Vendor Maintenance.  */  
   "TaxRegionCode":string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  Added for FRx Integration which requires that the company is identified by a unique positive integer, as opposed to a character string.  FRx calls this the entity number.  It is maintained on the General Ledger configuration screen.  */  
   "Number":number,
      /**  Data Source Name for the FRx database for this company.  Must be linked to a SQL Server 7.0 database to allow exporting of data for financial reporting using FRx.  This field is maintained on the General Ledger configuration screen for each company.  */  
   "FRxDSN":string,
      /**  The file set where the eScheduling XML messages will be sent.  It must be a valid DOS file name.  If eScheduling is being used with the Manufacturing System this field is required.  */  
   "EschedFileSet":string,
      /**  Unique identifier from and external G/L interface  */  
   "ExternalID":string,
      /**  Name of file that contains the company's logo image.  This can be blank (no logo available).  This is used for Customer/Sales/Supplier Connect.  */  
   "LogoFile":string,
      /**  Path the Employee Photos are stored in.  */  
   "EmpPhotoPath":string,
      /**   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  */  
   "CalendarID":string,
      /**  The User ID for FRx.  */  
   "FrxUserid":string,
      /**  FRxUserID password  */  
   "FRxPassWord":string,
      /**  The fiscal calendar id for the company.  */  
   "FiscalCalendarID":string,
      /**  Company legal name  */  
   "LegalName":string,
      /**  Tax Payer Registration Reason Code  */  
   "TaxRegReason":string,
      /**  Economic Activity Type  */  
   "ActTypeCode":string,
      /**  Organization Registration Code  */  
   "OrgRegCode":string,
      /**  Chief Executive Officerr name  */  
   "ManagerName":string,
      /**  Chief Financial Officer Name  */  
   "ChiefAcctName":string,
      /**  Type of report  */  
   "ReportTypePref":string,
      /**  WIApplication  */  
   "WIApplication":string,
      /**  WIAutoCreateJob  */  
   "WIAutoCreateJob":boolean,
      /**  WIGetDetails  */  
   "WIGetDetails":boolean,
      /**  WISchedule  */  
   "WISchedule":boolean,
      /**  WIRelease  */  
   "WIRelease":boolean,
      /**  WIShippingCosts  */  
   "WIShippingCosts":boolean,
      /**  DeepCopy  */  
   "DeepCopy":boolean,
      /**  DeepCopyDupOrRevEst  */  
   "DeepCopyDupOrRevEst":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MapURL  */  
   "MapURL":string,
      /**  MXMunicipio  */  
   "MXMunicipio":string,
      /**  APBOE Check  */  
   "APBOECheck":number,
      /**  COSequenceCert  */  
   "COSequenceCert":number,
      /**  Determines if the Company has to be synchronized with Epicor FSA application.  */  
   "SendToFSA":boolean,
      /**  Epicor client number for CRE  */  
   "EpicorAccountNum":number,
      /**  StartDate  */  
   "StartDate":string,
      /**  Kind of Employer F - Federal Government, S - State and Local Governmental Employer, T - Tax Exempt Employer, Y - State and Local Tax Exempt Employer, N - None Apply  */  
   "KindOfEmp":string,
      /**  Use the Employment Code field to select either the 941 (Option R) tax form or the 944 (Option F) tax form, depending upon the tax form the employer files. This selection is used in the W2 Processing program during W2 form export.  */  
   "EmploymentCode":string,
      /**  Purchase Schedule Mode specifies how the related demand requirements should be handled for this company.  */  
   "PurchaseScheduleMode":string,
      /**  Currency.BaseCurrCode field  */  
   "BaseCurrCode":string,
   "ExtPRConfig":boolean,
      /**  Has Currency Transactions  */  
   "HasCurrTrans":boolean,
   "Intrastat":boolean,
      /**  Name of product (MFGSYS Name)  */  
   "ProductName":string,
   "AllowSchedulingBeforeToday":boolean,
   "BitFlag":number,
   "CalendarDescription":string,
   "FiscalCalDescription":string,
   "TaxRegionDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ConsSrcCtrlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Internal system calcualted sequence number not inteneded for external use.  */  
   "GenID":number,
      /**  Unique Book Identifier  This is the book that is being consolidated into a target book.  */  
   "SourceBook":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  The fiscal year.  */  
   "FiscalYear":number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal period number in the fiscal year.  */  
   "FiscalPeriod":number,
      /**  Unique identifer for the consolidation definition  */  
   "ConsDefID":string,
      /**  Posted Date  */  
   "PostedDate":string,
      /**  (secounds since midnight)  */  
   "PostedTime":number,
      /**  User ID of person that posted this period.  */  
   "PostedBy":string,
      /**  Account Number where rounding differences will be posted  */  
   "DiffOnExchangeAcct":string,
      /**  Indicates the current status of the generation.  G =  Generated.  PI = Posted to the Intermediate book.  P = consolidated and Posted to the target.  */  
   "GenStatus":string,
      /**  Indicates if consolidation was bypassed  */  
   "Bypassed":boolean,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   "DiffExSegValue1":string,
      /**  SegmentValue 2.  See COASegment segment number 1 for a description of this field.  */  
   "DiffExSegValue2":string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   "DiffExSegValue3":string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   "DiffExSegValue4":string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   "DiffExSegValue5":string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   "DiffExSegValue6":string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   "DiffExSegValue7":string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   "DiffExSegValue8":string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   "DiffExSegValue9":string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   "DiffExSegValue10":string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   "DiffExSegValue11":string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   "DiffExSegValue12":string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   "DiffExSegValue13":string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   "DiffExSegValue14":string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   "DiffExSegValue15":string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   "DiffExSegValue16":string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   "DiffExSegValue17":string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   "DiffExSegValue18":string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   "DiffExSegValue19":string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   "DiffExSegValue20":string,
      /**  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  */  
   "RemoteAcct":string,
      /**  The related ConsType ID  */  
   "BalanceSheetDefType":string,
      /**  The related ConsType ID  */  
   "IncomeStmtDefType":string,
      /**  The number of closing periods to be processed during consolidation.  The default value is zero which indicates that closing periods are not consolidated.  */  
   "ClosingPeriods":number,
      /**  Applies to Periodic Consolidation only.  Logical indicating if open periods are excluded from consolidation.  If yes, any balance records written against a source book in a period that is still open is not sent to the target company.  If no, all balance records are sent.  Note: The fiscal calendar is defined on the GLBook table for the source company and book.  */  
   "ExcludeOpenPrds":boolean,
      /**  The journal code to use when posting the consolidation records in the target company book.  */  
   "TgtJrnlCode":string,
      /**  This option is only avaialble when 'Use Intermediate Book' equals yes.  Indicates if debit and credit amounts are swapped before the data is transferred.  */  
   "ReverseDBCR":boolean,
      /**  Accounting segments mapping ID to use when calling the mapping engine.  Must be a valid entry in the COAMap table.  This is NOT available when remote parent is set to true.  The source COA on the mapping record must be the same as the COA assigned to the source book.  If the source company equals the target company then the target COA on this mapping record must be the COA assigned to the target book.  */  
   "COAMapUID":number,
      /**  Only available when 'Use Intermediate Book' equals yes.  This is the the journal code to use when posting consolidated entries to the intermediate book.  */  
   "IntermediateJrnlCode":string,
      /**  Retransfer  */  
   "Retransfer":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The fiscal period to start adjusting from  */  
   "AdjustFromFiscalPeriod":number,
      /**  PeriodEndDate  */  
   "PeriodEndDate":string,
      /**  AdjPeriodEndDate  */  
   "AdjPeriodEndDate":string,
      /**  When posting, the last fiscal period that was processed without error, particulary for consolidations that span multiple periods.  */  
   "ProcessedFiscalPeriod":number,
      /**   Indicates the status of the consolidation for display purposes.  Is set programatically.

F - First consolidation
R - Retrospective
L - Last Period Delta
O - Overriding Period  */  
   "ConsolidationStatus":string,
      /**  Indicates if previous periods have not been consolidated  */  
   "PeriodsMissed":boolean,
      /**  Source COA code  */  
   "SourceCOA":string,
      /**  TargetCOA for DiffExtAccount  */  
   "TargetCOA":string,
      /**  Flag indicating that next period consolidation has been performed  */  
   "NextPeriodConsolidation":boolean,
   "BitFlag":number,
   "FiscalCalDescription":string,
   "SourceBookDescription":string,
   "SourceBookCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ConsSrcRatesRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Internal system calcualted sequence number not inteneded for external use.  */  
   "GenID":number,
      /**  Unique Book Identifier  This is the book that is being consolidated into a target book.  */  
   "SourceBook":string,
      /**  The fiscal year.  */  
   "FiscalYear":number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal period number in the fiscal year.  */  
   "FiscalPeriod":number,
      /**  Rate Type id of related RateType.  */  
   "RateTypeID":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Exchange Rate that will be used for this Rate Type.  */  
   "ExchangeRate":number,
      /**  Internal field used to indicate whether or not the user modified the rates.  */  
   "UserModified":boolean,
      /**  Internal field used to indicate if the system was unable to calcuate the rates.  If yes, the rates are in error.  If no, the rates are okay.  */  
   "RateError":boolean,
      /**  Calculation Date  */  
   "CalcDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Daily Average, Period End or None  */  
   "DefaultMethod":string,
      /**  Indicates if the record is selected for retrieval of default values  */  
   "Selected":boolean,
   "Description":string,
   "BitFlag":number,
   "RateTypeIDDescription":string,
   "SourceBookCurrencyCode":string,
   "SourceBookDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ConsTgtDefRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifer for the consolidation definition  */  
   "ConsDefID":string,
      /**  Free form text that describes the target that sources are consolidated into.  */  
   "Description":string,
      /**  Used to notify the consolidation routine whether or not the Parent company is in the same database as the subsidiary's data.  */  
   "RemoteParent":boolean,
      /**  Used to notify the consolidation routine whether or not the Parent company is running an Epicor database.  */  
   "VantageDB":boolean,
      /**  Target Company Identifier.  */  
   "TgtCompany":string,
      /**  Unique Book Identifier  This is the book the source book is consolidated to.  */  
   "TgtBook":string,
      /**  Target Chart of Accounts.  Can only be entered when remote parent is set to true or when the source and target companies are not the same and the target book is null.  This must be a vlaid entry in the GLBCOA table.  */  
   "TargetCOA":string,
      /**   Identifies how data is consolidated.  P = Periodic.  C = Continuous.

Under Periodic Consolidation the GLPeriodBal records are consolidated and transmitted to the target company and book.  Under Continuous Consolidation the GLJrnDtl records are transmitted.  */  
   "ConsolidationType":string,
      /**  Import/Export file name.  */  
   "OutputFile":string,
      /**  Only available when 'Use Intermediate Book' equals true.  Must be a valid GLBook in the source company whose BookType = 2 (Consolidation).  The intermediate book must have the same COA and currency as the target book.  */  
   "IntermediateBookID":string,
      /**  Logical indicating if the data written to the intermediate book is automatically transferred to the target company.  If yes, the data is automatically transferred.  If not, the user has the opportunity to review the intermediate books and is responsible for submitting the process that transfers the data.  This option is only available when 'Use Intermediate Book' equals yes.  */  
   "ImmediateTrans":boolean,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  */  
   "RemoteAcct":string,
      /**  D = Delta Generation.  The difference between the existing ConsBookTrack amount and the newly calcualted amount is consolidated into the parent company.

O = Override.  The existing GLJrnDtl records are deleted and new ones are created for the current balance.  */  
   "AdjustMode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Target Book Fiscal Calendar  */  
   "TgtBookCal":string,
      /**  Intermediate book fiscal calendar  */  
   "IterBookFiscalCal":string,
      /**  Target Book fiscal Calendar  */  
   "TgtBookFiscalCal":string,
      /**  Target Book Description  */  
   "TgtBookDesc":string,
      /**  Intermediate COA Code  */  
   "IntermediateCOA":string,
      /**  Field used for UI.  The option is stored in db filed AdjustMode, which is a string.  On the UI, the field should appear as a checkbox.  */  
   "AdjustModeInput":boolean,
      /**  Source Company  */  
   "SrcCompany":string,
      /**  Source Company Name  */  
   "SrcCompanyName":string,
      /**  This column is used to accomplish the following UI behavior, in order to enable and disable some UI controls according to if a consolidation was already created using the definition.  */  
   "HasConsolitation":boolean,
      /**  The field is used in the Consolidation Monitor Entry for tracking the state of the last consolidation  */  
   "LastGenStatus":string,
      /**  Intermediate book fiscal calendar ID.  */  
   "IterBookFiscalCalID":string,
      /**  Target Book fiscal Calendar ID.  */  
   "TgtBookFiscalCalID":string,
   "BitFlag":number,
   "InterBookCurrencyCode":string,
   "InterBookDescription":string,
   "TargetCOName":string,
   "TgtCOADescription":string,
   "TgtCurrencyCurrName":string,
   "TgtCurrencyCurrSymbol":string,
   "TgtCurrencyCurrencyID":string,
   "TgtCurrencyDocumentDesc":string,
   "TgtCurrencyCurrDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ConsTgtGenRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Internal system calculated sequence number not inteneded for external use.  */  
   "GenID":number,
      /**  Unique identifer for the consolidation definition  */  
   "ConsDefID":string,
      /**  Generation Description  */  
   "Description":string,
      /**  Indicates the current status of the generation.  O = Open generation and consolidation have not occurred.  G =  Generated.  PI = Posted to the Intermediate book.  P = consolidated and Posted to the target.  */  
   "GenStatus":string,
      /**  Target Company Identifier.  */  
   "TgtCompany":string,
      /**  Unique Book Identifier  This is the book the source book is consolidated to.  */  
   "TgtBook":string,
      /**  Target Chart of Accounts.  Can only be entered when remote parent is set to true or when the source and target companies are not the same and the target book is null.  This must be a vlaid entry in the GLBCOA table.  */  
   "TargetCOA":string,
      /**  Only available when 'Use Intermediate Book' equals true.  Must be a valid GLBook in the source company whose BookType = 2 (Consolidation).  The intermediate book must have the same COA and currency as the target book.  */  
   "IntermediateBookID":string,
      /**  Logical indicating if the data written to the intermediate book is automatically transferred to the target company.  If yes, the data is automatically transferred.  If not, the user has the opportunity to review the intermediate books and is responsible for submitting the process that transfers the data.  This option is only available when 'Use Intermediate Book' equals yes.  */  
   "ImmediateTrans":boolean,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Used to notify the consolidation routine whether or not the Parent company is in the same database as the subsidiary's data.  */  
   "RemoteParent":boolean,
      /**  Used to notify the consolidation routine whether or not the Parent company is running an Epicor database.  */  
   "VantageDB":boolean,
      /**  Import/Export file name.  */  
   "OutputFile":string,
      /**  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  */  
   "RemoteAcct":string,
      /**   Identifies how data is consolidated.  P = Periodic.  C = Continuous.

Under Periodic Consolidation the GLPeriodBal records are consolidated and transmitted to the target company and book.  Under Continuous Consolidation the GLJrnDtl records are transmitted.  */  
   "ConsolidationType":string,
      /**   THIS IS RESERVED FOR FUTURE USE.

D = Delta Generation.  The difference between the existing ConsBookTrack amount and the newly calcualted amount is consolidated into the parent company.

F = Full Replacement.  The existing GLJrnDtl records are deleted and new ones are created for the current balance.  */  
   "AdjustMode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Identifies the mode the record was added in.  C = Consolidation, R = Retrospective Adjustment  */  
   "EntryMode":string,
      /**  Logical indicating if this COA is the Master COA.  */  
   "MasterCOA":boolean,
      /**  LatestConsolidation  */  
   "LatestConsolidation":boolean,
      /**  Closing periods parameter defined in Consolidation definition.  */  
   "ClosingPeriods":number,
   "BitFlag":number,
   "ConsDefIDDescription":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeCurrName":string,
   "IntermediateBookIDDescription":string,
   "IntermediateBookIDCurrencyCode":string,
   "TargetCOADescription":string,
   "TgtBookCurrencyCode":string,
   "TgtBookDescription":string,
   "TgtCompanyName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ConsTgtGenTempRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Internal system calculated sequence number not inteneded for external use.  */  
   "GenID":number,
      /**  Unique identifer for the consolidation definition  */  
   "ConsDefID":string,
      /**  Generation Description  */  
   "Description":string,
      /**  Indicates the current status of the generation.  O = Open generation and consolidation have not occurred.  G =  Generated.  PI = Posted to the Intermediate book.  P = consolidated and Posted to the target.  */  
   "GenStatus":string,
      /**  Target Company Identifier.  */  
   "TgtCompany":string,
      /**  Unique Book Identifier  This is the book the source book is consolidated to.  */  
   "TgtBook":string,
      /**  Target Chart of Accounts.  Can only be entered when remote parent is set to true or when the source and target companies are not the same and the target book is null.  This must be a vlaid entry in the GLBCOA table.  */  
   "TargetCOA":string,
      /**  Only available when 'Use Intermediate Book' equals true.  Must be a valid GLBook in the source company whose BookType = 2 (Consolidation).  The intermediate book must have the same COA and currency as the target book.  */  
   "IntermediateBookID":string,
      /**  Logical indicating if the data written to the intermediate book is automatically transferred to the target company.  If yes, the data is automatically transferred.  If not, the user has the opportunity to review the intermediate books and is responsible for submitting the process that transfers the data.  This option is only available when 'Use Intermediate Book' equals yes.  */  
   "ImmediateTrans":boolean,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Used to notify the consolidation routine whether or not the Parent company is in the same database as the subsidiary's data.  */  
   "RemoteParent":boolean,
      /**  Used to notify the consolidation routine whether or not the Parent company is running a Vantage database.  */  
   "VantageDB":boolean,
      /**  Import/Export file name.  */  
   "OutputFile":string,
      /**  The free form Diff on Exchange Acct for a Remote Parent that is not a Vantage Database  */  
   "RemoteAcct":string,
      /**   Identifies how data is consolidated.  P = Periodic.  C = Continuous.

Under Periodic Consolidation the GLPeriodBal records are consolidated and transmitted to the target company and book.  Under Continuous Consolidation the GLJrnDtl records are transmitted.  */  
   "ConsolidationType":string,
      /**   THIS IS RESERVED FOR FUTURE USE.

D = Delta Generation.  The difference between the existing ConsBookTrack amount and the newly calcualted amount is consolidated into the parent company.

F = Full Replacement.  The existing GLJrnDtl records are deleted and new ones are created for the current balance.  */  
   "AdjustMode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Identifies the mode the record was added in.  C = Consolidation, R = Retrospective Adjustment  */  
   "EntryMode":string,
      /**  Logical indicating if this COA is the Master COA.  */  
   "MasterCOA":boolean,
   "SourceBook":string,
   "ScrBookDesc":string,
   "ConsNodeCaption":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ConsTgtSrcRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifer for the consolidation definition  */  
   "ConsDefID":string,
      /**  Unique Book Identifier  This is the book that is being consolidated into a target book.  */  
   "SourceBook":string,
      /**  The related ConsType ID  */  
   "BalanceSheetDefType":string,
      /**  The related ConsType ID  */  
   "IncomeStmtDefType":string,
      /**  The number of closing periods to be processed during consolidation.  The default value is zero which indicates that closing periods are not consolidated.  */  
   "ClosingPeriods":number,
      /**  Applies to Periodic Consolidation only.  Logical indicating if open periods are excluded from consolidation.  If yes, any balance records written against a source book in a period that is still open is not sent to the target company.  If no, all balance records are sent.  Note: The fiscal calendar is defined on the GLBook table for the source company and book.  */  
   "ExcludeOpenPrds":boolean,
      /**  The journal code to use when posting the consolidation records in the target company book.  */  
   "TgtJrnlCode":string,
      /**  This option is only avaialble when 'Use Intermediate Book' equals yes.  Indicates if debit and credit amounts are swapped before the data is transferred.  */  
   "ReverseDBCR":boolean,
      /**  Accounting segments mapping ID to use when calling the mapping engine.  Must be a valid entry in the COAMap table.  This is NOT available when remote parent is set to true.  The source COA on the mapping record must be the same as the COA assigned to the source book.  If the source company equals the target company then the target COA on this mapping record must be the COA assigned to the target book.  */  
   "COAMapUID":number,
      /**  Only available when 'Use Intermediate Book' equals yes.  This is the the journal code to use when posting consolidated entries to the intermediate book.  */  
   "IntermediateJrnlCode":string,
      /**  Account Number where rounding differences will be posted  */  
   "DiffOnExchangeAcct":string,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   "DiffExSegValue1":string,
      /**  SegmentValue 2.  See COASegment segment number 1 for a description of this field.  */  
   "DiffExSegValue2":string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   "DiffExSegValue3":string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   "DiffExSegValue4":string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   "DiffExSegValue5":string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   "DiffExSegValue6":string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   "DiffExSegValue7":string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   "DiffExSegValue8":string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   "DiffExSegValue9":string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   "DiffExSegValue10":string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   "DiffExSegValue11":string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   "DiffExSegValue12":string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   "DiffExSegValue13":string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   "DiffExSegValue14":string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   "DiffExSegValue15":string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   "DiffExSegValue16":string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   "DiffExSegValue17":string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   "DiffExSegValue18":string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   "DiffExSegValue19":string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   "DiffExSegValue20":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Target COA - this field is intended for internal use  */  
   "TargetCOA":string,
      /**  Target Company ID - intended for internal use  */  
   "TargetCompany":string,
      /**  Source COA code  */  
   "SourceCOA":string,
      /**  Intermediate Journal Code description.  This is either from the JrnlCode or GLBJrnCode table.  */  
   "InterJrnlDesc":string,
      /**  Target Journal Code description.  This is either from the JrnlCode or GLBJrnCode table.  */  
   "TgtJrnlCodeDesc":string,
      /**  Currency code description from either the Currency or GLBCurrency table.  */  
   "CurrencyDesc":string,
      /**  Source book fiscal calendar.  */  
   "SrcFiscalCalendar":string,
      /**  Holds GLAccount description temporarily to provide extra information to the user.  */  
   "DiffOnExchangeDesc":string,
      /**  Intermediate COA Code  */  
   "IntermediateCOA":string,
   "BitFlag":number,
   "BalanceConsTypeDescription":string,
   "BalanceRateDescription":string,
   "COAMapDisplayName":string,
   "IncomeConsTypeDescription":string,
   "IncomeRateDescription":string,
   "SrcBookDescription":string,
   "SrcBookCurrencyCode":string,
   "SrcCompanyName":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface DeleteByID_output{
}

export interface Erp_Tablesets_CompanyListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Company Name  */  
   Name:string,
      /**  First company address line.  */  
   Address1:string,
      /**  City portion of company address.  */  
   City:string,
      /**  State portion of company address.  */  
   State:string,
      /**  Postal code or zip code portion of company address.  */  
   Zip:string,
      /**  Company phone number  */  
   PhoneNum:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CompanyRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Company Name  */  
   Name:string,
      /**  First company address line.  */  
   Address1:string,
      /**  Second company address line.  */  
   Address2:string,
      /**  Third company address line.  */  
   Address3:string,
      /**  City portion of company address.  */  
   City:string,
      /**  State portion of company address.  */  
   State:string,
      /**  Postal code or zip code portion of company address.  */  
   Zip:string,
      /**  Country portion of company address.  */  
   Country:string,
      /**  Company phone number  */  
   PhoneNum:string,
      /**  Company fax number  */  
   FaxNum:string,
      /**  Federal Income Tax Number  */  
   FEIN:string,
      /**  State Tax ID  */  
   StateTaxID:string,
      /**  Current fiscal year  */  
   CurrentFiscalYear:number,
      /**  This is the Trading Partner ID that is used for incoming and outgoing EDI.  */  
   EDICode:string,
      /**  The Tax Region Code for this company. This tax region is used to define the 'interior'. It is used as a default tax region in Vendor Maintenance.  */  
   TaxRegionCode:string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  Added for FRx Integration which requires that the company is identified by a unique positive integer, as opposed to a character string.  FRx calls this the entity number.  It is maintained on the General Ledger configuration screen.  */  
   Number:number,
      /**  Data Source Name for the FRx database for this company.  Must be linked to a SQL Server 7.0 database to allow exporting of data for financial reporting using FRx.  This field is maintained on the General Ledger configuration screen for each company.  */  
   FRxDSN:string,
      /**  The file set where the eScheduling XML messages will be sent.  It must be a valid DOS file name.  If eScheduling is being used with the Manufacturing System this field is required.  */  
   EschedFileSet:string,
      /**  Unique identifier from and external G/L interface  */  
   ExternalID:string,
      /**  Name of file that contains the company's logo image.  This can be blank (no logo available).  This is used for Customer/Sales/Supplier Connect.  */  
   LogoFile:string,
      /**  Path the Employee Photos are stored in.  */  
   EmpPhotoPath:string,
      /**   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  */  
   CalendarID:string,
      /**  The User ID for FRx.  */  
   FrxUserid:string,
      /**  FRxUserID password  */  
   FRxPassWord:string,
      /**  The fiscal calendar id for the company.  */  
   FiscalCalendarID:string,
      /**  Company legal name  */  
   LegalName:string,
      /**  Tax Payer Registration Reason Code  */  
   TaxRegReason:string,
      /**  Economic Activity Type  */  
   ActTypeCode:string,
      /**  Organization Registration Code  */  
   OrgRegCode:string,
      /**  Chief Executive Officerr name  */  
   ManagerName:string,
      /**  Chief Financial Officer Name  */  
   ChiefAcctName:string,
      /**  Type of report  */  
   ReportTypePref:string,
      /**  WIApplication  */  
   WIApplication:string,
      /**  WIAutoCreateJob  */  
   WIAutoCreateJob:boolean,
      /**  WIGetDetails  */  
   WIGetDetails:boolean,
      /**  WISchedule  */  
   WISchedule:boolean,
      /**  WIRelease  */  
   WIRelease:boolean,
      /**  WIShippingCosts  */  
   WIShippingCosts:boolean,
      /**  DeepCopy  */  
   DeepCopy:boolean,
      /**  DeepCopyDupOrRevEst  */  
   DeepCopyDupOrRevEst:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MapURL  */  
   MapURL:string,
      /**  MXMunicipio  */  
   MXMunicipio:string,
      /**  APBOE Check  */  
   APBOECheck:number,
      /**  COSequenceCert  */  
   COSequenceCert:number,
      /**  Determines if the Company has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  Epicor client number for CRE  */  
   EpicorAccountNum:number,
      /**  StartDate  */  
   StartDate:string,
      /**  Kind of Employer F - Federal Government, S - State and Local Governmental Employer, T - Tax Exempt Employer, Y - State and Local Tax Exempt Employer, N - None Apply  */  
   KindOfEmp:string,
      /**  Use the Employment Code field to select either the 941 (Option R) tax form or the 944 (Option F) tax form, depending upon the tax form the employer files. This selection is used in the W2 Processing program during W2 form export.  */  
   EmploymentCode:string,
      /**  Purchase Schedule Mode specifies how the related demand requirements should be handled for this company.  */  
   PurchaseScheduleMode:string,
      /**  Currency.BaseCurrCode field  */  
   BaseCurrCode:string,
   ExtPRConfig:boolean,
      /**  Has Currency Transactions  */  
   HasCurrTrans:boolean,
   Intrastat:boolean,
      /**  Name of product (MFGSYS Name)  */  
   ProductName:string,
   AllowSchedulingBeforeToday:boolean,
   BitFlag:number,
   CalendarDescription:string,
   FiscalCalDescription:string,
   TaxRegionDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ConsMonitorListTableset{
   CompanyList:Erp_Tablesets_CompanyListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ConsMonitorTableset{
   Company:Erp_Tablesets_CompanyRow[],
   ConsTgtDef:Erp_Tablesets_ConsTgtDefRow[],
   ConsTgtGen:Erp_Tablesets_ConsTgtGenRow[],
   ConsSrcCtrl:Erp_Tablesets_ConsSrcCtrlRow[],
   ConsSrcRates:Erp_Tablesets_ConsSrcRatesRow[],
   ConsTgtSrc:Erp_Tablesets_ConsTgtSrcRow[],
   ConsTgtGenTemp:Erp_Tablesets_ConsTgtGenTempRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ConsSrcCtrlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Internal system calcualted sequence number not inteneded for external use.  */  
   GenID:number,
      /**  Unique Book Identifier  This is the book that is being consolidated into a target book.  */  
   SourceBook:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  The fiscal year.  */  
   FiscalYear:number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   FiscalYearSuffix:string,
      /**  The fiscal period number in the fiscal year.  */  
   FiscalPeriod:number,
      /**  Unique identifer for the consolidation definition  */  
   ConsDefID:string,
      /**  Posted Date  */  
   PostedDate:string,
      /**  (secounds since midnight)  */  
   PostedTime:number,
      /**  User ID of person that posted this period.  */  
   PostedBy:string,
      /**  Account Number where rounding differences will be posted  */  
   DiffOnExchangeAcct:string,
      /**  Indicates the current status of the generation.  G =  Generated.  PI = Posted to the Intermediate book.  P = consolidated and Posted to the target.  */  
   GenStatus:string,
      /**  Indicates if consolidation was bypassed  */  
   Bypassed:boolean,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   DiffExSegValue1:string,
      /**  SegmentValue 2.  See COASegment segment number 1 for a description of this field.  */  
   DiffExSegValue2:string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   DiffExSegValue3:string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   DiffExSegValue4:string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   DiffExSegValue5:string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   DiffExSegValue6:string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   DiffExSegValue7:string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   DiffExSegValue8:string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   DiffExSegValue9:string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   DiffExSegValue10:string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   DiffExSegValue11:string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   DiffExSegValue12:string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   DiffExSegValue13:string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   DiffExSegValue14:string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   DiffExSegValue15:string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   DiffExSegValue16:string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   DiffExSegValue17:string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   DiffExSegValue18:string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   DiffExSegValue19:string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   DiffExSegValue20:string,
      /**  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  */  
   RemoteAcct:string,
      /**  The related ConsType ID  */  
   BalanceSheetDefType:string,
      /**  The related ConsType ID  */  
   IncomeStmtDefType:string,
      /**  The number of closing periods to be processed during consolidation.  The default value is zero which indicates that closing periods are not consolidated.  */  
   ClosingPeriods:number,
      /**  Applies to Periodic Consolidation only.  Logical indicating if open periods are excluded from consolidation.  If yes, any balance records written against a source book in a period that is still open is not sent to the target company.  If no, all balance records are sent.  Note: The fiscal calendar is defined on the GLBook table for the source company and book.  */  
   ExcludeOpenPrds:boolean,
      /**  The journal code to use when posting the consolidation records in the target company book.  */  
   TgtJrnlCode:string,
      /**  This option is only avaialble when 'Use Intermediate Book' equals yes.  Indicates if debit and credit amounts are swapped before the data is transferred.  */  
   ReverseDBCR:boolean,
      /**  Accounting segments mapping ID to use when calling the mapping engine.  Must be a valid entry in the COAMap table.  This is NOT available when remote parent is set to true.  The source COA on the mapping record must be the same as the COA assigned to the source book.  If the source company equals the target company then the target COA on this mapping record must be the COA assigned to the target book.  */  
   COAMapUID:number,
      /**  Only available when 'Use Intermediate Book' equals yes.  This is the the journal code to use when posting consolidated entries to the intermediate book.  */  
   IntermediateJrnlCode:string,
      /**  Retransfer  */  
   Retransfer:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The fiscal period to start adjusting from  */  
   AdjustFromFiscalPeriod:number,
      /**  PeriodEndDate  */  
   PeriodEndDate:string,
      /**  AdjPeriodEndDate  */  
   AdjPeriodEndDate:string,
      /**  When posting, the last fiscal period that was processed without error, particulary for consolidations that span multiple periods.  */  
   ProcessedFiscalPeriod:number,
      /**   Indicates the status of the consolidation for display purposes.  Is set programatically.

F - First consolidation
R - Retrospective
L - Last Period Delta
O - Overriding Period  */  
   ConsolidationStatus:string,
      /**  Indicates if previous periods have not been consolidated  */  
   PeriodsMissed:boolean,
      /**  Source COA code  */  
   SourceCOA:string,
      /**  TargetCOA for DiffExtAccount  */  
   TargetCOA:string,
      /**  Flag indicating that next period consolidation has been performed  */  
   NextPeriodConsolidation:boolean,
   BitFlag:number,
   FiscalCalDescription:string,
   SourceBookDescription:string,
   SourceBookCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ConsSrcRatesRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Internal system calcualted sequence number not inteneded for external use.  */  
   GenID:number,
      /**  Unique Book Identifier  This is the book that is being consolidated into a target book.  */  
   SourceBook:string,
      /**  The fiscal year.  */  
   FiscalYear:number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   FiscalYearSuffix:string,
      /**  The fiscal period number in the fiscal year.  */  
   FiscalPeriod:number,
      /**  Rate Type id of related RateType.  */  
   RateTypeID:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Exchange Rate that will be used for this Rate Type.  */  
   ExchangeRate:number,
      /**  Internal field used to indicate whether or not the user modified the rates.  */  
   UserModified:boolean,
      /**  Internal field used to indicate if the system was unable to calcuate the rates.  If yes, the rates are in error.  If no, the rates are okay.  */  
   RateError:boolean,
      /**  Calculation Date  */  
   CalcDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Daily Average, Period End or None  */  
   DefaultMethod:string,
      /**  Indicates if the record is selected for retrieval of default values  */  
   Selected:boolean,
   Description:string,
   BitFlag:number,
   RateTypeIDDescription:string,
   SourceBookCurrencyCode:string,
   SourceBookDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ConsTgtDefRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifer for the consolidation definition  */  
   ConsDefID:string,
      /**  Free form text that describes the target that sources are consolidated into.  */  
   Description:string,
      /**  Used to notify the consolidation routine whether or not the Parent company is in the same database as the subsidiary's data.  */  
   RemoteParent:boolean,
      /**  Used to notify the consolidation routine whether or not the Parent company is running an Epicor database.  */  
   VantageDB:boolean,
      /**  Target Company Identifier.  */  
   TgtCompany:string,
      /**  Unique Book Identifier  This is the book the source book is consolidated to.  */  
   TgtBook:string,
      /**  Target Chart of Accounts.  Can only be entered when remote parent is set to true or when the source and target companies are not the same and the target book is null.  This must be a vlaid entry in the GLBCOA table.  */  
   TargetCOA:string,
      /**   Identifies how data is consolidated.  P = Periodic.  C = Continuous.

Under Periodic Consolidation the GLPeriodBal records are consolidated and transmitted to the target company and book.  Under Continuous Consolidation the GLJrnDtl records are transmitted.  */  
   ConsolidationType:string,
      /**  Import/Export file name.  */  
   OutputFile:string,
      /**  Only available when 'Use Intermediate Book' equals true.  Must be a valid GLBook in the source company whose BookType = 2 (Consolidation).  The intermediate book must have the same COA and currency as the target book.  */  
   IntermediateBookID:string,
      /**  Logical indicating if the data written to the intermediate book is automatically transferred to the target company.  If yes, the data is automatically transferred.  If not, the user has the opportunity to review the intermediate books and is responsible for submitting the process that transfers the data.  This option is only available when 'Use Intermediate Book' equals yes.  */  
   ImmediateTrans:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  */  
   RemoteAcct:string,
      /**  D = Delta Generation.  The difference between the existing ConsBookTrack amount and the newly calcualted amount is consolidated into the parent company.

O = Override.  The existing GLJrnDtl records are deleted and new ones are created for the current balance.  */  
   AdjustMode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Target Book Fiscal Calendar  */  
   TgtBookCal:string,
      /**  Intermediate book fiscal calendar  */  
   IterBookFiscalCal:string,
      /**  Target Book fiscal Calendar  */  
   TgtBookFiscalCal:string,
      /**  Target Book Description  */  
   TgtBookDesc:string,
      /**  Intermediate COA Code  */  
   IntermediateCOA:string,
      /**  Field used for UI.  The option is stored in db filed AdjustMode, which is a string.  On the UI, the field should appear as a checkbox.  */  
   AdjustModeInput:boolean,
      /**  Source Company  */  
   SrcCompany:string,
      /**  Source Company Name  */  
   SrcCompanyName:string,
      /**  This column is used to accomplish the following UI behavior, in order to enable and disable some UI controls according to if a consolidation was already created using the definition.  */  
   HasConsolitation:boolean,
      /**  The field is used in the Consolidation Monitor Entry for tracking the state of the last consolidation  */  
   LastGenStatus:string,
      /**  Intermediate book fiscal calendar ID.  */  
   IterBookFiscalCalID:string,
      /**  Target Book fiscal Calendar ID.  */  
   TgtBookFiscalCalID:string,
   BitFlag:number,
   InterBookCurrencyCode:string,
   InterBookDescription:string,
   TargetCOName:string,
   TgtCOADescription:string,
   TgtCurrencyCurrName:string,
   TgtCurrencyCurrSymbol:string,
   TgtCurrencyCurrencyID:string,
   TgtCurrencyDocumentDesc:string,
   TgtCurrencyCurrDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ConsTgtGenRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Internal system calculated sequence number not inteneded for external use.  */  
   GenID:number,
      /**  Unique identifer for the consolidation definition  */  
   ConsDefID:string,
      /**  Generation Description  */  
   Description:string,
      /**  Indicates the current status of the generation.  O = Open generation and consolidation have not occurred.  G =  Generated.  PI = Posted to the Intermediate book.  P = consolidated and Posted to the target.  */  
   GenStatus:string,
      /**  Target Company Identifier.  */  
   TgtCompany:string,
      /**  Unique Book Identifier  This is the book the source book is consolidated to.  */  
   TgtBook:string,
      /**  Target Chart of Accounts.  Can only be entered when remote parent is set to true or when the source and target companies are not the same and the target book is null.  This must be a vlaid entry in the GLBCOA table.  */  
   TargetCOA:string,
      /**  Only available when 'Use Intermediate Book' equals true.  Must be a valid GLBook in the source company whose BookType = 2 (Consolidation).  The intermediate book must have the same COA and currency as the target book.  */  
   IntermediateBookID:string,
      /**  Logical indicating if the data written to the intermediate book is automatically transferred to the target company.  If yes, the data is automatically transferred.  If not, the user has the opportunity to review the intermediate books and is responsible for submitting the process that transfers the data.  This option is only available when 'Use Intermediate Book' equals yes.  */  
   ImmediateTrans:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Used to notify the consolidation routine whether or not the Parent company is in the same database as the subsidiary's data.  */  
   RemoteParent:boolean,
      /**  Used to notify the consolidation routine whether or not the Parent company is running an Epicor database.  */  
   VantageDB:boolean,
      /**  Import/Export file name.  */  
   OutputFile:string,
      /**  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  */  
   RemoteAcct:string,
      /**   Identifies how data is consolidated.  P = Periodic.  C = Continuous.

Under Periodic Consolidation the GLPeriodBal records are consolidated and transmitted to the target company and book.  Under Continuous Consolidation the GLJrnDtl records are transmitted.  */  
   ConsolidationType:string,
      /**   THIS IS RESERVED FOR FUTURE USE.

D = Delta Generation.  The difference between the existing ConsBookTrack amount and the newly calcualted amount is consolidated into the parent company.

F = Full Replacement.  The existing GLJrnDtl records are deleted and new ones are created for the current balance.  */  
   AdjustMode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Identifies the mode the record was added in.  C = Consolidation, R = Retrospective Adjustment  */  
   EntryMode:string,
      /**  Logical indicating if this COA is the Master COA.  */  
   MasterCOA:boolean,
      /**  LatestConsolidation  */  
   LatestConsolidation:boolean,
      /**  Closing periods parameter defined in Consolidation definition.  */  
   ClosingPeriods:number,
   BitFlag:number,
   ConsDefIDDescription:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeCurrName:string,
   IntermediateBookIDDescription:string,
   IntermediateBookIDCurrencyCode:string,
   TargetCOADescription:string,
   TgtBookCurrencyCode:string,
   TgtBookDescription:string,
   TgtCompanyName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ConsTgtGenTempRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Internal system calculated sequence number not inteneded for external use.  */  
   GenID:number,
      /**  Unique identifer for the consolidation definition  */  
   ConsDefID:string,
      /**  Generation Description  */  
   Description:string,
      /**  Indicates the current status of the generation.  O = Open generation and consolidation have not occurred.  G =  Generated.  PI = Posted to the Intermediate book.  P = consolidated and Posted to the target.  */  
   GenStatus:string,
      /**  Target Company Identifier.  */  
   TgtCompany:string,
      /**  Unique Book Identifier  This is the book the source book is consolidated to.  */  
   TgtBook:string,
      /**  Target Chart of Accounts.  Can only be entered when remote parent is set to true or when the source and target companies are not the same and the target book is null.  This must be a vlaid entry in the GLBCOA table.  */  
   TargetCOA:string,
      /**  Only available when 'Use Intermediate Book' equals true.  Must be a valid GLBook in the source company whose BookType = 2 (Consolidation).  The intermediate book must have the same COA and currency as the target book.  */  
   IntermediateBookID:string,
      /**  Logical indicating if the data written to the intermediate book is automatically transferred to the target company.  If yes, the data is automatically transferred.  If not, the user has the opportunity to review the intermediate books and is responsible for submitting the process that transfers the data.  This option is only available when 'Use Intermediate Book' equals yes.  */  
   ImmediateTrans:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Used to notify the consolidation routine whether or not the Parent company is in the same database as the subsidiary's data.  */  
   RemoteParent:boolean,
      /**  Used to notify the consolidation routine whether or not the Parent company is running a Vantage database.  */  
   VantageDB:boolean,
      /**  Import/Export file name.  */  
   OutputFile:string,
      /**  The free form Diff on Exchange Acct for a Remote Parent that is not a Vantage Database  */  
   RemoteAcct:string,
      /**   Identifies how data is consolidated.  P = Periodic.  C = Continuous.

Under Periodic Consolidation the GLPeriodBal records are consolidated and transmitted to the target company and book.  Under Continuous Consolidation the GLJrnDtl records are transmitted.  */  
   ConsolidationType:string,
      /**   THIS IS RESERVED FOR FUTURE USE.

D = Delta Generation.  The difference between the existing ConsBookTrack amount and the newly calcualted amount is consolidated into the parent company.

F = Full Replacement.  The existing GLJrnDtl records are deleted and new ones are created for the current balance.  */  
   AdjustMode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Identifies the mode the record was added in.  C = Consolidation, R = Retrospective Adjustment  */  
   EntryMode:string,
      /**  Logical indicating if this COA is the Master COA.  */  
   MasterCOA:boolean,
   SourceBook:string,
   ScrBookDesc:string,
   ConsNodeCaption:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ConsTgtSrcRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifer for the consolidation definition  */  
   ConsDefID:string,
      /**  Unique Book Identifier  This is the book that is being consolidated into a target book.  */  
   SourceBook:string,
      /**  The related ConsType ID  */  
   BalanceSheetDefType:string,
      /**  The related ConsType ID  */  
   IncomeStmtDefType:string,
      /**  The number of closing periods to be processed during consolidation.  The default value is zero which indicates that closing periods are not consolidated.  */  
   ClosingPeriods:number,
      /**  Applies to Periodic Consolidation only.  Logical indicating if open periods are excluded from consolidation.  If yes, any balance records written against a source book in a period that is still open is not sent to the target company.  If no, all balance records are sent.  Note: The fiscal calendar is defined on the GLBook table for the source company and book.  */  
   ExcludeOpenPrds:boolean,
      /**  The journal code to use when posting the consolidation records in the target company book.  */  
   TgtJrnlCode:string,
      /**  This option is only avaialble when 'Use Intermediate Book' equals yes.  Indicates if debit and credit amounts are swapped before the data is transferred.  */  
   ReverseDBCR:boolean,
      /**  Accounting segments mapping ID to use when calling the mapping engine.  Must be a valid entry in the COAMap table.  This is NOT available when remote parent is set to true.  The source COA on the mapping record must be the same as the COA assigned to the source book.  If the source company equals the target company then the target COA on this mapping record must be the COA assigned to the target book.  */  
   COAMapUID:number,
      /**  Only available when 'Use Intermediate Book' equals yes.  This is the the journal code to use when posting consolidated entries to the intermediate book.  */  
   IntermediateJrnlCode:string,
      /**  Account Number where rounding differences will be posted  */  
   DiffOnExchangeAcct:string,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   DiffExSegValue1:string,
      /**  SegmentValue 2.  See COASegment segment number 1 for a description of this field.  */  
   DiffExSegValue2:string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   DiffExSegValue3:string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   DiffExSegValue4:string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   DiffExSegValue5:string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   DiffExSegValue6:string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   DiffExSegValue7:string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   DiffExSegValue8:string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   DiffExSegValue9:string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   DiffExSegValue10:string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   DiffExSegValue11:string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   DiffExSegValue12:string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   DiffExSegValue13:string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   DiffExSegValue14:string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   DiffExSegValue15:string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   DiffExSegValue16:string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   DiffExSegValue17:string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   DiffExSegValue18:string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   DiffExSegValue19:string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   DiffExSegValue20:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Target COA - this field is intended for internal use  */  
   TargetCOA:string,
      /**  Target Company ID - intended for internal use  */  
   TargetCompany:string,
      /**  Source COA code  */  
   SourceCOA:string,
      /**  Intermediate Journal Code description.  This is either from the JrnlCode or GLBJrnCode table.  */  
   InterJrnlDesc:string,
      /**  Target Journal Code description.  This is either from the JrnlCode or GLBJrnCode table.  */  
   TgtJrnlCodeDesc:string,
      /**  Currency code description from either the Currency or GLBCurrency table.  */  
   CurrencyDesc:string,
      /**  Source book fiscal calendar.  */  
   SrcFiscalCalendar:string,
      /**  Holds GLAccount description temporarily to provide extra information to the user.  */  
   DiffOnExchangeDesc:string,
      /**  Intermediate COA Code  */  
   IntermediateCOA:string,
   BitFlag:number,
   BalanceConsTypeDescription:string,
   BalanceRateDescription:string,
   COAMapDisplayName:string,
   IncomeConsTypeDescription:string,
   IncomeRateDescription:string,
   SrcBookDescription:string,
   SrcBookCurrencyCode:string,
   SrcCompanyName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtConsMonitorTableset{
   Company:Erp_Tablesets_CompanyRow[],
   ConsTgtDef:Erp_Tablesets_ConsTgtDefRow[],
   ConsTgtGen:Erp_Tablesets_ConsTgtGenRow[],
   ConsSrcCtrl:Erp_Tablesets_ConsSrcCtrlRow[],
   ConsSrcRates:Erp_Tablesets_ConsSrcRatesRow[],
   ConsTgtSrc:Erp_Tablesets_ConsTgtSrcRow[],
   ConsTgtGenTemp:Erp_Tablesets_ConsTgtGenTempRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ConsMonitorTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ConsMonitorTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ConsMonitorTableset[],
}

   /** Required : 
      @param ipConsDefID
      @param ipTgtBook
      @param ipTgtBookStartDate
      @param ipTgtBookEndDate
   */  
export interface GetDefinitionMonitor_input{
   ipConsDefID:string,
   ipTgtBook:string,
   ipTgtBookStartDate:string,
   ipTgtBookEndDate:string,
}

export interface GetDefinitionMonitor_output{
   returnObj:Erp_Tablesets_ConsMonitorTableset[],
parameters : {
      /**  output parameters  */  
   opMessage:string,
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
   returnObj:Erp_Tablesets_ConsMonitorListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCompany_input{
   ds:Erp_Tablesets_ConsMonitorTableset[],
}

export interface GetNewCompany_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsMonitorTableset[],
}
}

   /** Required : 
      @param ds
      @param genID
   */  
export interface GetNewConsSrcCtrl_input{
   ds:Erp_Tablesets_ConsMonitorTableset[],
   genID:number,
}

export interface GetNewConsSrcCtrl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsMonitorTableset[],
}
}

   /** Required : 
      @param ds
      @param genID
      @param sourceBook
      @param fiscalYear
      @param fiscalYearSuffix
      @param fiscalPeriod
   */  
export interface GetNewConsSrcRates_input{
   ds:Erp_Tablesets_ConsMonitorTableset[],
   genID:number,
   sourceBook:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   fiscalPeriod:number,
}

export interface GetNewConsSrcRates_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsMonitorTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewConsTgtDef_input{
   ds:Erp_Tablesets_ConsMonitorTableset[],
}

export interface GetNewConsTgtDef_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsMonitorTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewConsTgtGen_input{
   ds:Erp_Tablesets_ConsMonitorTableset[],
}

export interface GetNewConsTgtGen_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsMonitorTableset[],
}
}

   /** Required : 
      @param ds
      @param consDefID
   */  
export interface GetNewConsTgtSrc_input{
   ds:Erp_Tablesets_ConsMonitorTableset[],
   consDefID:string,
}

export interface GetNewConsTgtSrc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsMonitorTableset[],
}
}

   /** Required : 
      @param ipTgtBook
      @param ipTgtBookStartDate
      @param ipTgtBookEndDate
   */  
export interface GetRowsMonitor_input{
   ipTgtBook:string,
   ipTgtBookStartDate:string,
   ipTgtBookEndDate:string,
}

export interface GetRowsMonitor_output{
   returnObj:Erp_Tablesets_ConsMonitorTableset[],
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param whereClauseCompany
      @param whereClauseConsTgtDef
      @param whereClauseConsTgtGen
      @param whereClauseConsSrcCtrl
      @param whereClauseConsSrcRates
      @param whereClauseConsTgtSrc
      @param whereClauseConsTgtGenTemp
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCompany:string,
   whereClauseConsTgtDef:string,
   whereClauseConsTgtGen:string,
   whereClauseConsSrcCtrl:string,
   whereClauseConsSrcRates:string,
   whereClauseConsTgtSrc:string,
   whereClauseConsTgtGenTemp:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ConsMonitorTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param opBookID
   */  
export interface GetSelectDefaultsWithCalendarID_input{
   opBookID:string,
}

export interface GetSelectDefaultsWithCalendarID_output{
parameters : {
      /**  output parameters  */  
   ouFiscalYear:number,
   ouFiscalPeriod:number,
   ouFiscalYearSuffix:string,
   ouPeriodStart:string,
   ouPeriodEnd:string,
   fiscalCalendarID:string,
}
}

   /** Required : 
      @param opBookID
   */  
export interface GetSelectDefaults_input{
   opBookID:string,
}

export interface GetSelectDefaults_output{
parameters : {
      /**  output parameters  */  
   ouFiscalYear:number,
   ouFiscalPeriod:number,
   ouFiscalYearSuffix:string,
   ouPeriodStart:string,
   ouPeriodEnd:string,
}
}

   /** Required : 
      @param opBookID
      @param ouFiscalYear
   */  
export interface GetSelectYearDefaultsWithCalendarID_input{
   opBookID:string,
   ouFiscalYear:number,
}

export interface GetSelectYearDefaultsWithCalendarID_output{
parameters : {
      /**  output parameters  */  
   ouFiscalPeriod:number,
   ouFiscalYearSuffix:string,
   ouPeriodStart:string,
   ouPeriodEnd:string,
   fiscalCalendarID:string,
}
}

   /** Required : 
      @param opBookID
      @param ouFiscalYear
      @param ouFiscalYearSuffix
   */  
export interface GetSelectYearSuffixDefaultsWithCalendarID_input{
   opBookID:string,
   ouFiscalYear:number,
   ouFiscalYearSuffix:string,
}

export interface GetSelectYearSuffixDefaultsWithCalendarID_output{
parameters : {
      /**  output parameters  */  
   ouFiscalPeriod:number,
   ouPeriodStart:string,
   ouPeriodEnd:string,
   fiscalCalendarID:string,
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
      @param ipBookID
      @param ipFiscalYear
      @param ipFiscalYearSuffix
      @param ipFiscalPeriod
   */  
export interface OnChangeSelectFiscalInfo_input{
   ipBookID:string,
   ipFiscalYear:number,
   ipFiscalYearSuffix:string,
   ipFiscalPeriod:number,
}

export interface OnChangeSelectFiscalInfo_output{
parameters : {
      /**  output parameters  */  
   opPeriodStartDate:string,
   opPeriodEndDate:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtConsMonitorTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtConsMonitorTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ConsMonitorTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConsMonitorTableset[],
}
}

   /** Required : 
      @param ipBookID
      @param ipFiscalYear
      @param ipFiscalYearSuffix
      @param ipFiscalPeriod
   */  
export interface ValidateSelectFiscalInfo_input{
   ipBookID:string,
   ipFiscalYear:number,
   ipFiscalYearSuffix:string,
   ipFiscalPeriod:number,
}

export interface ValidateSelectFiscalInfo_output{
}

   /** Required : 
      @param ipBookID
      @param ipFiscalYear
   */  
export interface ValidateSelectFiscalYearInfo_input{
   ipBookID:string,
   ipFiscalYear:number,
}

export interface ValidateSelectFiscalYearInfo_output{
}

   /** Required : 
      @param ipBookID
      @param ipFiscalYear
      @param ipFiscalYearSuffix
   */  
export interface ValidateSelectFiscalYearSuffixInfo_input{
   ipBookID:string,
   ipFiscalYear:number,
   ipFiscalYearSuffix:string,
}

export interface ValidateSelectFiscalYearSuffixInfo_output{
}

   /** Required : 
      @param ipBookID
   */  
export interface ValidateTargetBook_input{
   ipBookID:string,
}

export interface ValidateTargetBook_output{
}

