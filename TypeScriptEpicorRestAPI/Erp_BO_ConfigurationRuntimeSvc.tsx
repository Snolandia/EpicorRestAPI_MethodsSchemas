import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ConfigurationRuntimeSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/$metadata", {
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
   Description: Get ConfigurationRuntimes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConfigurationRuntimes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcValueGrpRow
   */  
export function get_ConfigurationRuntimes(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcValueGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ConfigurationRuntimes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcValueGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConfigurationRuntimes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcValueGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcValueGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConfigurationRuntimes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ConfigurationRuntimes", {
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
   Summary: Calls GetByID to retrieve the ConfigurationRuntime item
   Description: Calls GetByID to retrieve the ConfigurationRuntime item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConfigurationRuntime
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupSeq Desc: GroupSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcValueGrpRow
   */  
export function get_ConfigurationRuntimes_Company_GroupSeq(Company:string, GroupSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcValueGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ConfigurationRuntimes(" + Company + "," + GroupSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcValueGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ConfigurationRuntime for the service
   Description: Calls UpdateExt to update ConfigurationRuntime. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConfigurationRuntime
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupSeq Desc: GroupSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcValueGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ConfigurationRuntimes_Company_GroupSeq(Company:string, GroupSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ConfigurationRuntimes(" + Company + "," + GroupSeq + ")", {
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
   Summary: Call UpdateExt to delete ConfigurationRuntime item
   Description: Call UpdateExt to delete ConfigurationRuntime item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConfigurationRuntime
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupSeq Desc: GroupSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ConfigurationRuntimes_Company_GroupSeq(Company:string, GroupSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ConfigurationRuntimes(" + Company + "," + GroupSeq + ")", {
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
   Description: Get PcValueHeads items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcValueHeads1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupSeq Desc: GroupSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcValueHeadRow
   */  
export function get_ConfigurationRuntimes_Company_GroupSeq_PcValueHeads(Company:string, GroupSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcValueHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ConfigurationRuntimes(" + Company + "," + GroupSeq + ")/PcValueHeads", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcValueHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcValueHead item
   Description: Calls GetByID to retrieve the PcValueHead item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcValueHead1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupSeq Desc: GroupSeq   Required: True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcValueHeadRow
   */  
export function get_ConfigurationRuntimes_Company_GroupSeq_PcValueHeads_Company_GroupSeq_HeadNum(Company:string, GroupSeq:string, HeadNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcValueHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ConfigurationRuntimes(" + Company + "," + GroupSeq + ")/PcValueHeads(" + Company + "," + GroupSeq + "," + HeadNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcValueHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PcValueHeads items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcValueHeads
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcValueHeadRow
   */  
export function get_PcValueHeads(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcValueHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueHeads", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcValueHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcValueHeads
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcValueHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcValueHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcValueHeads(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueHeads", {
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
   Summary: Calls GetByID to retrieve the PcValueHead item
   Description: Calls GetByID to retrieve the PcValueHead item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcValueHead
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupSeq Desc: GroupSeq   Required: True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcValueHeadRow
   */  
export function get_PcValueHeads_Company_GroupSeq_HeadNum(Company:string, GroupSeq:string, HeadNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcValueHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueHeads(" + Company + "," + GroupSeq + "," + HeadNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcValueHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcValueHead for the service
   Description: Calls UpdateExt to update PcValueHead. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcValueHead
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupSeq Desc: GroupSeq   Required: True
      @param HeadNum Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcValueHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcValueHeads_Company_GroupSeq_HeadNum(Company:string, GroupSeq:string, HeadNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueHeads(" + Company + "," + GroupSeq + "," + HeadNum + ")", {
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
   Summary: Call UpdateExt to delete PcValueHead item
   Description: Call UpdateExt to delete PcValueHead item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcValueHead
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupSeq Desc: GroupSeq   Required: True
      @param HeadNum Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcValueHeads_Company_GroupSeq_HeadNum(Company:string, GroupSeq:string, HeadNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueHeads(" + Company + "," + GroupSeq + "," + HeadNum + ")", {
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
   Description: Get PcConfigurationParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcConfigurationParams
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcConfigurationParamsRow
   */  
export function get_PcConfigurationParams(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcConfigurationParamsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcConfigurationParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcConfigurationParamsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcConfigurationParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcConfigurationParamsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcConfigurationParamsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcConfigurationParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcConfigurationParams", {
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
   Summary: Calls GetByID to retrieve the PcConfigurationParam item
   Description: Calls GetByID to retrieve the PcConfigurationParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcConfigurationParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param UniqueID Desc: UniqueID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcConfigurationParamsRow
   */  
export function get_PcConfigurationParams_Company_UniqueID(Company:string, UniqueID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcConfigurationParamsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcConfigurationParams(" + Company + "," + UniqueID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcConfigurationParamsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcConfigurationParam for the service
   Description: Calls UpdateExt to update PcConfigurationParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcConfigurationParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param UniqueID Desc: UniqueID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcConfigurationParamsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcConfigurationParams_Company_UniqueID(Company:string, UniqueID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcConfigurationParams(" + Company + "," + UniqueID + ")", {
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
   Summary: Call UpdateExt to delete PcConfigurationParam item
   Description: Call UpdateExt to delete PcConfigurationParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcConfigurationParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param UniqueID Desc: UniqueID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcConfigurationParams_Company_UniqueID(Company:string, UniqueID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcConfigurationParams(" + Company + "," + UniqueID + ")", {
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
   Description: Get PcConfiguredDrawings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcConfiguredDrawings
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcConfiguredDrawingsRow
   */  
export function get_PcConfiguredDrawings(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcConfiguredDrawingsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcConfiguredDrawings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcConfiguredDrawingsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcConfiguredDrawings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcConfiguredDrawingsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcConfiguredDrawingsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcConfiguredDrawings(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcConfiguredDrawings", {
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
   Summary: Calls GetByID to retrieve the PcConfiguredDrawing item
   Description: Calls GetByID to retrieve the PcConfiguredDrawing item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcConfiguredDrawing
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupSeq Desc: GroupSeq   Required: True
      @param HeadNum Desc: HeadNum   Required: True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcConfiguredDrawingsRow
   */  
export function get_PcConfiguredDrawings_Company_GroupSeq_HeadNum_InputName(Company:string, GroupSeq:string, HeadNum:string, InputName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcConfiguredDrawingsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcConfiguredDrawings(" + Company + "," + GroupSeq + "," + HeadNum + "," + InputName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcConfiguredDrawingsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcConfiguredDrawing for the service
   Description: Calls UpdateExt to update PcConfiguredDrawing. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcConfiguredDrawing
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupSeq Desc: GroupSeq   Required: True
      @param HeadNum Desc: HeadNum   Required: True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcConfiguredDrawingsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcConfiguredDrawings_Company_GroupSeq_HeadNum_InputName(Company:string, GroupSeq:string, HeadNum:string, InputName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcConfiguredDrawings(" + Company + "," + GroupSeq + "," + HeadNum + "," + InputName + ")", {
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
   Summary: Call UpdateExt to delete PcConfiguredDrawing item
   Description: Call UpdateExt to delete PcConfiguredDrawing item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcConfiguredDrawing
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupSeq Desc: GroupSeq   Required: True
      @param HeadNum Desc: HeadNum   Required: True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcConfiguredDrawings_Company_GroupSeq_HeadNum_InputName(Company:string, GroupSeq:string, HeadNum:string, InputName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcConfiguredDrawings(" + Company + "," + GroupSeq + "," + HeadNum + "," + InputName + ")", {
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
   Description: Get PcContextProperties items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcContextProperties
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcContextPropertiesRow
   */  
export function get_PcContextProperties(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcContextPropertiesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcContextProperties", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcContextPropertiesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcContextProperties
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcContextPropertiesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcContextPropertiesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcContextProperties(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcContextProperties", {
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
   Summary: Calls GetByID to retrieve the PcContextProperty item
   Description: Calls GetByID to retrieve the PcContextProperty item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcContextProperty
      @param ConfigurationID Desc: ConfigurationID   Required: True   Allow empty value : True
      @param CompanyID Desc: CompanyID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcContextPropertiesRow
   */  
export function get_PcContextProperties_ConfigurationID_CompanyID(ConfigurationID:string, CompanyID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcContextPropertiesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcContextProperties(" + ConfigurationID + "," + CompanyID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcContextPropertiesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcContextProperty for the service
   Description: Calls UpdateExt to update PcContextProperty. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcContextProperty
      @param ConfigurationID Desc: ConfigurationID   Required: True   Allow empty value : True
      @param CompanyID Desc: CompanyID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcContextPropertiesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcContextProperties_ConfigurationID_CompanyID(ConfigurationID:string, CompanyID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcContextProperties(" + ConfigurationID + "," + CompanyID + ")", {
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
   Summary: Call UpdateExt to delete PcContextProperty item
   Description: Call UpdateExt to delete PcContextProperty item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcContextProperty
      @param ConfigurationID Desc: ConfigurationID   Required: True   Allow empty value : True
      @param CompanyID Desc: CompanyID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcContextProperties_ConfigurationID_CompanyID(ConfigurationID:string, CompanyID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcContextProperties(" + ConfigurationID + "," + CompanyID + ")", {
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
   Description: Get PcInputsLayerDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcInputsLayerDetails
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsLayerDetailRow
   */  
export function get_PcInputsLayerDetails(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsLayerDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsLayerDetails", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsLayerDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcInputsLayerDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcInputsLayerDetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcInputsLayerDetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcInputsLayerDetails(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsLayerDetails", {
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
   Summary: Calls GetByID to retrieve the PcInputsLayerDetail item
   Description: Calls GetByID to retrieve the PcInputsLayerDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsLayerDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ImageLayerID Desc: ImageLayerID   Required: True   Allow empty value : True
      @param LayerSeq Desc: LayerSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsLayerDetailRow
   */  
export function get_PcInputsLayerDetails_Company_ConfigID_InputName_ImageLayerID_LayerSeq(Company:string, ConfigID:string, InputName:string, ImageLayerID:string, LayerSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcInputsLayerDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsLayerDetails(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + "," + LayerSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcInputsLayerDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcInputsLayerDetail for the service
   Description: Calls UpdateExt to update PcInputsLayerDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcInputsLayerDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ImageLayerID Desc: ImageLayerID   Required: True   Allow empty value : True
      @param LayerSeq Desc: LayerSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcInputsLayerDetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcInputsLayerDetails_Company_ConfigID_InputName_ImageLayerID_LayerSeq(Company:string, ConfigID:string, InputName:string, ImageLayerID:string, LayerSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsLayerDetails(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + "," + LayerSeq + ")", {
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
   Summary: Call UpdateExt to delete PcInputsLayerDetail item
   Description: Call UpdateExt to delete PcInputsLayerDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcInputsLayerDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ImageLayerID Desc: ImageLayerID   Required: True   Allow empty value : True
      @param LayerSeq Desc: LayerSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcInputsLayerDetails_Company_ConfigID_InputName_ImageLayerID_LayerSeq(Company:string, ConfigID:string, InputName:string, ImageLayerID:string, LayerSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsLayerDetails(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + "," + LayerSeq + ")", {
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
   Description: Get PcInputsLayerHeaders items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcInputsLayerHeaders
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsLayerHeaderRow
   */  
export function get_PcInputsLayerHeaders(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsLayerHeaderRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsLayerHeaders", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsLayerHeaderRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcInputsLayerHeaders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcInputsLayerHeaderRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcInputsLayerHeaderRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcInputsLayerHeaders(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsLayerHeaders", {
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
   Summary: Calls GetByID to retrieve the PcInputsLayerHeader item
   Description: Calls GetByID to retrieve the PcInputsLayerHeader item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsLayerHeader
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ImageLayerID Desc: ImageLayerID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsLayerHeaderRow
   */  
export function get_PcInputsLayerHeaders_Company_ConfigID_InputName_ImageLayerID(Company:string, ConfigID:string, InputName:string, ImageLayerID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcInputsLayerHeaderRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsLayerHeaders(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcInputsLayerHeaderRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcInputsLayerHeader for the service
   Description: Calls UpdateExt to update PcInputsLayerHeader. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcInputsLayerHeader
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ImageLayerID Desc: ImageLayerID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcInputsLayerHeaderRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcInputsLayerHeaders_Company_ConfigID_InputName_ImageLayerID(Company:string, ConfigID:string, InputName:string, ImageLayerID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsLayerHeaders(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + ")", {
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
   Summary: Call UpdateExt to delete PcInputsLayerHeader item
   Description: Call UpdateExt to delete PcInputsLayerHeader item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcInputsLayerHeader
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ImageLayerID Desc: ImageLayerID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcInputsLayerHeaders_Company_ConfigID_InputName_ImageLayerID(Company:string, ConfigID:string, InputName:string, ImageLayerID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsLayerHeaders(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + ")", {
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
   Description: Get PcInputsPublishToDocParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcInputsPublishToDocParams
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsPublishToDocParamsRow
   */  
export function get_PcInputsPublishToDocParams(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsPublishToDocParamsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsPublishToDocParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsPublishToDocParamsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcInputsPublishToDocParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcInputsPublishToDocParamsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcInputsPublishToDocParamsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcInputsPublishToDocParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsPublishToDocParams", {
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
   Summary: Calls GetByID to retrieve the PcInputsPublishToDocParam item
   Description: Calls GetByID to retrieve the PcInputsPublishToDocParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsPublishToDocParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Key Desc: Key   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsPublishToDocParamsRow
   */  
export function get_PcInputsPublishToDocParams_Company_Key(Company:string, Key:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcInputsPublishToDocParamsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsPublishToDocParams(" + Company + "," + Key + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcInputsPublishToDocParamsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcInputsPublishToDocParam for the service
   Description: Calls UpdateExt to update PcInputsPublishToDocParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcInputsPublishToDocParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Key Desc: Key   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcInputsPublishToDocParamsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcInputsPublishToDocParams_Company_Key(Company:string, Key:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsPublishToDocParams(" + Company + "," + Key + ")", {
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
   Summary: Call UpdateExt to delete PcInputsPublishToDocParam item
   Description: Call UpdateExt to delete PcInputsPublishToDocParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcInputsPublishToDocParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Key Desc: Key   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcInputsPublishToDocParams_Company_Key(Company:string, Key:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsPublishToDocParams(" + Company + "," + Key + ")", {
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
   Description: Get PcInputVars items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcInputVars
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputVarRow
   */  
export function get_PcInputVars(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputVarRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputVars", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputVarRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcInputVars
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcInputVarRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcInputVarRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcInputVars(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputVars", {
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
   Summary: Calls GetByID to retrieve the PcInputVar item
   Description: Calls GetByID to retrieve the PcInputVar item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputVar
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VarName Desc: VarName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputVarRow
   */  
export function get_PcInputVars_Company_VarName(Company:string, VarName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcInputVarRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputVars(" + Company + "," + VarName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcInputVarRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcInputVar for the service
   Description: Calls UpdateExt to update PcInputVar. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcInputVar
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VarName Desc: VarName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcInputVarRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcInputVars_Company_VarName(Company:string, VarName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputVars(" + Company + "," + VarName + ")", {
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
   Summary: Call UpdateExt to delete PcInputVar item
   Description: Call UpdateExt to delete PcInputVar item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcInputVar
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VarName Desc: VarName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcInputVars_Company_VarName(Company:string, VarName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputVars(" + Company + "," + VarName + ")", {
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
   Description: Get PcValueInputLayerDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcValueInputLayerDetails
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcValueInputLayerDetailRow
   */  
export function get_PcValueInputLayerDetails(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcValueInputLayerDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueInputLayerDetails", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcValueInputLayerDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcValueInputLayerDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcValueInputLayerDetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcValueInputLayerDetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcValueInputLayerDetails(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueInputLayerDetails", {
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
   Summary: Calls GetByID to retrieve the PcValueInputLayerDetail item
   Description: Calls GetByID to retrieve the PcValueInputLayerDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcValueInputLayerDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupSeq Desc: GroupSeq   Required: True
      @param HeadNum Desc: HeadNum   Required: True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ImageLayerID Desc: ImageLayerID   Required: True   Allow empty value : True
      @param LayerSeq Desc: LayerSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcValueInputLayerDetailRow
   */  
export function get_PcValueInputLayerDetails_Company_GroupSeq_HeadNum_ConfigID_InputName_ImageLayerID_LayerSeq(Company:string, GroupSeq:string, HeadNum:string, ConfigID:string, InputName:string, ImageLayerID:string, LayerSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcValueInputLayerDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueInputLayerDetails(" + Company + "," + GroupSeq + "," + HeadNum + "," + ConfigID + "," + InputName + "," + ImageLayerID + "," + LayerSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcValueInputLayerDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcValueInputLayerDetail for the service
   Description: Calls UpdateExt to update PcValueInputLayerDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcValueInputLayerDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupSeq Desc: GroupSeq   Required: True
      @param HeadNum Desc: HeadNum   Required: True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ImageLayerID Desc: ImageLayerID   Required: True   Allow empty value : True
      @param LayerSeq Desc: LayerSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcValueInputLayerDetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcValueInputLayerDetails_Company_GroupSeq_HeadNum_ConfigID_InputName_ImageLayerID_LayerSeq(Company:string, GroupSeq:string, HeadNum:string, ConfigID:string, InputName:string, ImageLayerID:string, LayerSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueInputLayerDetails(" + Company + "," + GroupSeq + "," + HeadNum + "," + ConfigID + "," + InputName + "," + ImageLayerID + "," + LayerSeq + ")", {
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
   Summary: Call UpdateExt to delete PcValueInputLayerDetail item
   Description: Call UpdateExt to delete PcValueInputLayerDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcValueInputLayerDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupSeq Desc: GroupSeq   Required: True
      @param HeadNum Desc: HeadNum   Required: True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ImageLayerID Desc: ImageLayerID   Required: True   Allow empty value : True
      @param LayerSeq Desc: LayerSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcValueInputLayerDetails_Company_GroupSeq_HeadNum_ConfigID_InputName_ImageLayerID_LayerSeq(Company:string, GroupSeq:string, HeadNum:string, ConfigID:string, InputName:string, ImageLayerID:string, LayerSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueInputLayerDetails(" + Company + "," + GroupSeq + "," + HeadNum + "," + ConfigID + "," + InputName + "," + ImageLayerID + "," + LayerSeq + ")", {
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
   Description: Get PcValueInputLayerHeaders items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcValueInputLayerHeaders
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcValueInputLayerHeaderRow
   */  
export function get_PcValueInputLayerHeaders(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcValueInputLayerHeaderRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueInputLayerHeaders", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcValueInputLayerHeaderRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcValueInputLayerHeaders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcValueInputLayerHeaderRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcValueInputLayerHeaderRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcValueInputLayerHeaders(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueInputLayerHeaders", {
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
   Summary: Calls GetByID to retrieve the PcValueInputLayerHeader item
   Description: Calls GetByID to retrieve the PcValueInputLayerHeader item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcValueInputLayerHeader
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupSeq Desc: GroupSeq   Required: True
      @param HeadNum Desc: HeadNum   Required: True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ImageLayerID Desc: ImageLayerID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcValueInputLayerHeaderRow
   */  
export function get_PcValueInputLayerHeaders_Company_GroupSeq_HeadNum_ConfigID_InputName_ImageLayerID(Company:string, GroupSeq:string, HeadNum:string, ConfigID:string, InputName:string, ImageLayerID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcValueInputLayerHeaderRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueInputLayerHeaders(" + Company + "," + GroupSeq + "," + HeadNum + "," + ConfigID + "," + InputName + "," + ImageLayerID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcValueInputLayerHeaderRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcValueInputLayerHeader for the service
   Description: Calls UpdateExt to update PcValueInputLayerHeader. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcValueInputLayerHeader
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupSeq Desc: GroupSeq   Required: True
      @param HeadNum Desc: HeadNum   Required: True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ImageLayerID Desc: ImageLayerID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcValueInputLayerHeaderRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcValueInputLayerHeaders_Company_GroupSeq_HeadNum_ConfigID_InputName_ImageLayerID(Company:string, GroupSeq:string, HeadNum:string, ConfigID:string, InputName:string, ImageLayerID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueInputLayerHeaders(" + Company + "," + GroupSeq + "," + HeadNum + "," + ConfigID + "," + InputName + "," + ImageLayerID + ")", {
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
   Summary: Call UpdateExt to delete PcValueInputLayerHeader item
   Description: Call UpdateExt to delete PcValueInputLayerHeader item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcValueInputLayerHeader
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupSeq Desc: GroupSeq   Required: True
      @param HeadNum Desc: HeadNum   Required: True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ImageLayerID Desc: ImageLayerID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcValueInputLayerHeaders_Company_GroupSeq_HeadNum_ConfigID_InputName_ImageLayerID(Company:string, GroupSeq:string, HeadNum:string, ConfigID:string, InputName:string, ImageLayerID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueInputLayerHeaders(" + Company + "," + GroupSeq + "," + HeadNum + "," + ConfigID + "," + InputName + "," + ImageLayerID + ")", {
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
   Description: Get QBuildMappings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QBuildMappings
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QBuildMappingRow
   */  
export function get_QBuildMappings(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QBuildMappingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/QBuildMappings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QBuildMappingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QBuildMappings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QBuildMappingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QBuildMappingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QBuildMappings(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/QBuildMappings", {
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
   Summary: Calls GetByID to retrieve the QBuildMapping item
   Description: Calls GetByID to retrieve the QBuildMapping item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QBuildMapping
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ObjName Desc: ObjName   Required: True   Allow empty value : True
      @param ObjParameter Desc: ObjParameter   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QBuildMappingRow
   */  
export function get_QBuildMappings_Company_ConfigID_InputName_ObjName_ObjParameter(Company:string, ConfigID:string, InputName:string, ObjName:string, ObjParameter:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QBuildMappingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/QBuildMappings(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + "," + ObjParameter + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QBuildMappingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QBuildMapping for the service
   Description: Calls UpdateExt to update QBuildMapping. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QBuildMapping
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ObjName Desc: ObjName   Required: True   Allow empty value : True
      @param ObjParameter Desc: ObjParameter   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QBuildMappingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QBuildMappings_Company_ConfigID_InputName_ObjName_ObjParameter(Company:string, ConfigID:string, InputName:string, ObjName:string, ObjParameter:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/QBuildMappings(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + "," + ObjParameter + ")", {
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
   Summary: Call UpdateExt to delete QBuildMapping item
   Description: Call UpdateExt to delete QBuildMapping item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QBuildMapping
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ObjName Desc: ObjName   Required: True   Allow empty value : True
      @param ObjParameter Desc: ObjParameter   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QBuildMappings_Company_ConfigID_InputName_ObjName_ObjParameter(Company:string, ConfigID:string, InputName:string, ObjName:string, ObjParameter:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/QBuildMappings(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + "," + ObjParameter + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcValueGrpListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcValueGrpListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcValueGrpListRow)
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
export function get_GetRows(whereClausePcValueGrp:string, whereClausePcValueHead:string, whereClausePcConfigurationParams:string, whereClausePcConfiguredDrawings:string, whereClausePcContextProperties:string, whereClausePcInputsLayerDetail:string, whereClausePcInputsLayerHeader:string, whereClausePcInputsPublishToDocParams:string, whereClausePcInputVar:string, whereClausePcValueInputLayerDetail:string, whereClausePcValueInputLayerHeader:string, whereClauseQBuildMapping:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePcValueGrp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcValueGrp=" + whereClausePcValueGrp
   }
   if(typeof whereClausePcValueHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcValueHead=" + whereClausePcValueHead
   }
   if(typeof whereClausePcConfigurationParams!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcConfigurationParams=" + whereClausePcConfigurationParams
   }
   if(typeof whereClausePcConfiguredDrawings!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcConfiguredDrawings=" + whereClausePcConfiguredDrawings
   }
   if(typeof whereClausePcContextProperties!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcContextProperties=" + whereClausePcContextProperties
   }
   if(typeof whereClausePcInputsLayerDetail!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcInputsLayerDetail=" + whereClausePcInputsLayerDetail
   }
   if(typeof whereClausePcInputsLayerHeader!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcInputsLayerHeader=" + whereClausePcInputsLayerHeader
   }
   if(typeof whereClausePcInputsPublishToDocParams!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcInputsPublishToDocParams=" + whereClausePcInputsPublishToDocParams
   }
   if(typeof whereClausePcInputVar!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcInputVar=" + whereClausePcInputVar
   }
   if(typeof whereClausePcValueInputLayerDetail!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcValueInputLayerDetail=" + whereClausePcValueInputLayerDetail
   }
   if(typeof whereClausePcValueInputLayerHeader!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcValueInputLayerHeader=" + whereClausePcValueInputLayerHeader
   }
   if(typeof whereClauseQBuildMapping!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQBuildMapping=" + whereClauseQBuildMapping
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/GetRows" + params, {
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
export function get_GetByID(groupSeq:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof groupSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "groupSeq=" + groupSeq
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/GetList" + params, {
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
   Summary: Invoke method GetGeneratedClient
   Description: Returns the generated source code to compile the client code of a configuration
   OperationID: GetGeneratedClient
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGeneratedClient_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGeneratedClient_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGeneratedClient(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/GetGeneratedClient", {
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
   Summary: Invoke method PreStartConfiguration
   Description: Perform any logic that needs to be executed before starting a configuration
   OperationID: PreStartConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreStartConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreStartConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreStartConfiguration(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PreStartConfiguration", {
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
   Summary: Invoke method StartPcValueConfiguration
   Description: Starts a configuration given a configuration sequence (PcStruct) record and the source and target information.
For Keep When process:
* If PcValueHead does not exists State will be Added
   OperationID: StartPcValueConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartPcValueConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartPcValueConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_StartPcValueConfiguration(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/StartPcValueConfiguration", {
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
   Summary: Invoke method StartConfiguration
   Description: Starts a configuration given a configuration sequence (PcStruct) record and the source and target information.
For Keep When process:
* If PcValueHead does not exists State will be Added
   OperationID: StartConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_StartConfiguration(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/StartConfiguration", {
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
   Summary: Invoke method SavePcValueConfiguration
   Description: Saves a single level configuration.
   OperationID: SavePcValueConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SavePcValueConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SavePcValueConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SavePcValueConfiguration(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/SavePcValueConfiguration", {
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
   Summary: Invoke method SavePcValueConfigurationMulti
   Description: Saves a multi level configuration from kinetic.
   OperationID: SavePcValueConfigurationMulti
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SavePcValueConfigurationMulti_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SavePcValueConfigurationMulti_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SavePcValueConfigurationMulti(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/SavePcValueConfigurationMulti", {
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
   Summary: Invoke method SaveConfiguration
   Description: Saves a single level configuration.
   OperationID: SaveConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SaveConfiguration(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/SaveConfiguration", {
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
   Summary: Invoke method SaveMultiConfiguration
   Description: Saves a multi-level configuration.
For Keep When process:
* For all configurators that KeepIt are false will not be saved
* Identify all configurators KeepIt are false to delete PcValueHead and PcValueSet
   OperationID: SaveMultiConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveMultiConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveMultiConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SaveMultiConfiguration(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/SaveMultiConfiguration", {
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
   Summary: Invoke method DeleteAssembliesInTestMode
   Description: Method is executed when the customer X-es out of the configurator instead of pressing save and they are in test mode
   OperationID: DeleteAssembliesInTestMode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteAssembliesInTestMode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteAssembliesInTestMode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteAssembliesInTestMode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/DeleteAssembliesInTestMode", {
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
   Summary: Invoke method ProcessNoInputsConfigurator
   Description: Process the no inputs configurator for Kinetic screens.
The method uses the parameters to build the Tablesets needed to invoke the ProcessNICDocumentRules.
   OperationID: ProcessNoInputsConfigurator
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessNoInputsConfigurator_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessNoInputsConfigurator_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessNoInputsConfigurator(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ProcessNoInputsConfigurator", {
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
   Summary: Invoke method ProcessNICDocumentRules
   Description: Process NIC  document rules
   OperationID: ProcessNICDocumentRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessNICDocumentRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessNICDocumentRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessNICDocumentRules(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ProcessNICDocumentRules", {
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
   Summary: Invoke method ProcessDocumentRules
   Description: Process document rules
   OperationID: ProcessDocumentRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessDocumentRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessDocumentRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessDocumentRules(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ProcessDocumentRules", {
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
   Summary: Invoke method ProcessKeepWhen
   Description: Objective: Run methods rules to determine if assemblies should be keep it or not to hide or show the corresponding configuration.
This process will be executed when:
* When is clicked next page and changes to next configurator
* Is multiconfigurator
* If current part revision has rules set(OPR or ASM)
   OperationID: ProcessKeepWhen
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessKeepWhen_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessKeepWhen_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessKeepWhen(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ProcessKeepWhen", {
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
   Summary: Invoke method DeleteSubConfiguration
   Description: DeleteSubConfiguration
   OperationID: DeleteSubConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteSubConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteSubConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteSubConfiguration(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/DeleteSubConfiguration", {
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
   Summary: Invoke method CheckServerSyntax
   Description: Provides ability to check server side syntax
   OperationID: CheckServerSyntax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckServerSyntax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckServerSyntax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckServerSyntax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/CheckServerSyntax", {
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
   Summary: Invoke method TestNICRules
   Description: Call this method when you want to test the rules of a No Inputs Configurator
   OperationID: TestNICRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestNICRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestNICRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TestNICRules(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/TestNICRules", {
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
   Summary: Invoke method EWCTestRules
   Description: Call this method to retrieve the Test Rules results dataset that is temporarily stored in the FileStore for EWC configurators.
   OperationID: EWCTestRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EWCTestRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EWCTestRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EWCTestRules(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/EWCTestRules", {
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
   Summary: Invoke method EDIDemandConfiguration
   Description: Receives configuration values on a smart string and processes it completely.
   OperationID: EDIDemandConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EDIDemandConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EDIDemandConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EDIDemandConfiguration(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/EDIDemandConfiguration", {
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
   Summary: Invoke method EDIValidateSmartString
   Description: Validate the smart string against inputs
   OperationID: EDIValidateSmartString
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EDIValidateSmartString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EDIValidateSmartString_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EDIValidateSmartString(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/EDIValidateSmartString", {
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
   Summary: Invoke method PartExists
   Description: Part exists.
   OperationID: PartExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PartExists", {
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
   Summary: Invoke method PartRevExists
   Description: Determines if the part rev exists
   OperationID: PartRevExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartRevExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartRevExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartRevExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PartRevExists", {
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
   Summary: Invoke method GetTargetEntityValues
   Description: Get AllowRecordCreation and IncomingSmartString columns to process before the configuration is saved for the first time.
These values were obtained but only after the configuration was saved for the first time.
   OperationID: GetTargetEntityValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTargetEntityValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTargetEntityValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTargetEntityValues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/GetTargetEntityValues", {
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
   Summary: Invoke method SuggestSmartString
   Description: Original logic to suggest a smart string.  This is called from Win client and EWA.  It cannot be called from EWC.
   OperationID: SuggestSmartString
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SuggestSmartString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SuggestSmartString_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SuggestSmartString(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/SuggestSmartString", {
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
   Summary: Invoke method EWCSuggestSmartString
   Description: Call this method when you need to suggest a smart string value and you are not calling from EWA or your ConfigType is EWC.
   OperationID: EWCSuggestSmartString
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EWCSuggestSmartString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EWCSuggestSmartString_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EWCSuggestSmartString(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/EWCSuggestSmartString", {
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
   Summary: Invoke method AddUserDenfinedParameterString
   Description: Purpose: Adds a row and populates the string value in the User Defined Table used to pass parameters
from the client to the server for Server Side UDMethods.
<param name="methodName">The name of the server side UDmethod the parameter is being added for.</param><param name="parameterName">The name of the Parameter being added.</param><param name="configID">The ID of the configurator the UDmethod is tied to.</param><param name="paramSeq">The position the parameter is in the signature of the UDMethod.</param><param name="newValue">This holds the string value being passed for string parameters.</param><param name="pcValueDS">The name of the server side UDmethod parameter is being added for.</param>
   OperationID: AddUserDenfinedParameterString
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddUserDenfinedParameterString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddUserDenfinedParameterString_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddUserDenfinedParameterString(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/AddUserDenfinedParameterString", {
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
   Summary: Invoke method AddUserDenfinedParameterInt
   Description: Purpose: Adds a row and populates the int value in the User Defined Table used to pass parameters
from the client to the server for Server Side UDMethods.
<param name="methodName">The name of the server side UDmethod the parameter is being added for.</param><param name="parameterName">The name of the Parameter being added.</param><param name="configID">The ID of the configurator the UDmethod is tied to.</param><param name="paramSeq">The position the parameter is in the signature of the UDMethod.</param><param name="newValue">This holds the int value being passed for string parameters.</param><param name="pcValueDS">The name of the server side UDmethod parameter is being added for.</param>
   OperationID: AddUserDenfinedParameterInt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddUserDenfinedParameterInt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddUserDenfinedParameterInt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddUserDenfinedParameterInt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/AddUserDenfinedParameterInt", {
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
   Summary: Invoke method AddUserDenfinedParameterDecimal
   Description: Purpose: Adds a row and populates the decimal value in the User Defined Table used to pass parameters
from the client to the server for Server Side UDMethods.
<param name="methodName">The name of the server side UDmethod the parameter is being added for.</param><param name="parameterName">The name of the Parameter being added.</param><param name="configID">The ID of the configurator the UDmethod is tied to.</param><param name="paramSeq">The position the parameter is in the signature of the UDMethod.</param><param name="newValue">This holds the decimal value being passed for string parameters.</param><param name="pcValueDS">The name of the server side UDmethod parameter is being added for.</param>
   OperationID: AddUserDenfinedParameterDecimal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddUserDenfinedParameterDecimal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddUserDenfinedParameterDecimal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddUserDenfinedParameterDecimal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/AddUserDenfinedParameterDecimal", {
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
   Summary: Invoke method AddUserDenfinedParameterDateTime
   Description: Purpose: Adds a row and populates the DateTime value in the User Defined Table used to pass parameters
from the client to the server for Server Side UDMethods.
<param name="methodName">The name of the server side UDmethod the parameter is being added for.</param><param name="parameterName">The name of the Parameter being added.</param><param name="configID">The ID of the configurator the UDmethod is tied to.</param><param name="paramSeq">The position the parameter is in the signature of the UDMethod.</param><param name="newValue">This holds the DateTime value being passed for string parameters.</param><param name="pcValueDS">The name of the server side UDmethod parameter is being added for.</param>
   OperationID: AddUserDenfinedParameterDateTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddUserDenfinedParameterDateTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddUserDenfinedParameterDateTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddUserDenfinedParameterDateTime(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/AddUserDenfinedParameterDateTime", {
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
   Summary: Invoke method AddUserDenfinedParameterBool
   Description: Purpose: Adds a row and populates the bool value in the User Defined Table used to pass parameters
from the client to the server for Server Side UDMethods.
<param name="methodName">The name of the server side UDmethod the parameter is being added for.</param><param name="parameterName">The name of the Parameter being added.</param><param name="configID">The ID of the configurator the UDmethod is tied to.</param><param name="paramSeq">The position the parameter is in the signature of the UDMethod.</param><param name="newValue">This holds the bool value being passed for string parameters.</param><param name="pcValueDS">The name of the server side UDmethod parameter is being added for.</param>
   OperationID: AddUserDenfinedParameterBool
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddUserDenfinedParameterBool_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddUserDenfinedParameterBool_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddUserDenfinedParameterBool(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/AddUserDenfinedParameterBool", {
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
   Summary: Invoke method ClearUDMethodParams
   Description: Purpose: Clears the Rows in PcUserDefinedMethodParameters.  Rows should be cleared before and after calling
a server side UDMethod.
   OperationID: ClearUDMethodParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearUDMethodParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearUDMethodParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClearUDMethodParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ClearUDMethodParams", {
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
   Summary: Invoke method ExecuteGenerateImageLayerScriptCode
   Description: Used to generate Image Layer script code for the given Image Layer ID
   OperationID: ExecuteGenerateImageLayerScriptCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExecuteGenerateImageLayerScriptCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExecuteGenerateImageLayerScriptCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExecuteGenerateImageLayerScriptCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ExecuteGenerateImageLayerScriptCode", {
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
   Summary: Invoke method ExecuteGenerateSingleImageLayerScriptCode
   Description: Used to generate Image Layer script code for the given Image Layer ID
   OperationID: ExecuteGenerateSingleImageLayerScriptCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExecuteGenerateSingleImageLayerScriptCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExecuteGenerateSingleImageLayerScriptCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExecuteGenerateSingleImageLayerScriptCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ExecuteGenerateSingleImageLayerScriptCode", {
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
   Summary: Invoke method ExecuteGenerateFullImageLayerScriptCode
   OperationID: ExecuteGenerateFullImageLayerScriptCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExecuteGenerateFullImageLayerScriptCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExecuteGenerateFullImageLayerScriptCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExecuteGenerateFullImageLayerScriptCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ExecuteGenerateFullImageLayerScriptCode", {
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
   Summary: Invoke method ExecuteUserDefinedWithArrayReturn
   Description: Need to execute this method to execute server-side UDmethods that will return an array of objects.
   OperationID: ExecuteUserDefinedWithArrayReturn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExecuteUserDefinedWithArrayReturn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExecuteUserDefinedWithArrayReturn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExecuteUserDefinedWithArrayReturn(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ExecuteUserDefinedWithArrayReturn", {
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
   Summary: Invoke method ExecuteUserDefined
   Description: Need to execute this method to execute server side UDmethods from the client out other API.
<param name="methodName">The name of the server-side UDmethod to execute.</param><param name="configID">The ID of the configurator the UDmethod is tied to.</param><param name="testID">When executing under a test (Test Inputs/Rules) this parameter should contain a valid System.Guid, otherwise it can be System.Guid.Empty</param><param name="pcValueDS">Values from  current configurator.</param>
   OperationID: ExecuteUserDefined
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExecuteUserDefined_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExecuteUserDefined_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExecuteUserDefined(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ExecuteUserDefined", {
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
   Summary: Invoke method ExecuteDataLookup
   Description: Purpose: Executes DataLookup functiosn from the client side.
   OperationID: ExecuteDataLookup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExecuteDataLookup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExecuteDataLookup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExecuteDataLookup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ExecuteDataLookup", {
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
   Summary: Invoke method ExecutePageOnLoadEvents
   Description: Purpose: Call from the client to execute Page OnLoad events.
<param name="pageLoadEvent">The name of the page load event wanting to execute.</param><param name="configID">The ID of the configurator the UDmethod is tied to.</param><param name="testID"></param><param name="pcValueDS"></param>
   OperationID: ExecutePageOnLoadEvents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExecutePageOnLoadEvents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExecutePageOnLoadEvents_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExecutePageOnLoadEvents(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ExecutePageOnLoadEvents", {
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
   Summary: Invoke method GetPictureBoxImage
   Description: GetPictureBoxImage
   OperationID: GetPictureBoxImage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPictureBoxImage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPictureBoxImage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPictureBoxImage(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/GetPictureBoxImage", {
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
   Summary: Invoke method GetAllImages
   Description: Retrieve all picture box images and 2D Viewer drawings in one trip to the server and send the data back in a tableset
   OperationID: GetAllImages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllImages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllImages_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAllImages(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/GetAllImages", {
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
   Summary: Invoke method GetAllPictureBoxImages
   Description: Retrieves the images for a page in a configurator
   OperationID: GetAllPictureBoxImages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllPictureBoxImages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllPictureBoxImages_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAllPictureBoxImages(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/GetAllPictureBoxImages", {
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
   Summary: Invoke method GetNewPcConfigParams
   Description: GetNewPcConfigParams
   OperationID: GetNewPcConfigParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcConfigParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcConfigParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcConfigParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/GetNewPcConfigParams", {
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
   Summary: Invoke method GetNewPcInputsPublishToDoc
   Description: GetNewPcInputsPublishToDoc
   OperationID: GetNewPcInputsPublishToDoc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcInputsPublishToDoc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcInputsPublishToDoc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcInputsPublishToDoc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/GetNewPcInputsPublishToDoc", {
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
   Summary: Invoke method DataColumnLookupList
   Description: DataColumnLookupList
   OperationID: DataColumnLookupList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DataColumnLookupList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DataColumnLookupList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataColumnLookupList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/DataColumnLookupList", {
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
   Summary: Invoke method DataColumnList
   Description: DataColumnList
   OperationID: DataColumnList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DataColumnList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DataColumnList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataColumnList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/DataColumnList", {
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
   Summary: Invoke method DataColumnListNum
   Description: DataColumnListNum
   OperationID: DataColumnListNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DataColumnListNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DataColumnListNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataColumnListNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/DataColumnListNum", {
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
   Summary: Invoke method DataColumnRange
   Description: DataColumnRange
   OperationID: DataColumnRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DataColumnRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DataColumnRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataColumnRange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/DataColumnRange", {
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
   Summary: Invoke method DataRowList
   Description: DataRowList
   OperationID: DataRowList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DataRowList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DataRowList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataRowList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/DataRowList", {
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
   Summary: Invoke method DataRowListNum
   Description: DataRowListNum
   OperationID: DataRowListNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DataRowListNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DataRowListNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataRowListNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/DataRowListNum", {
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
   Summary: Invoke method DataRowRange
   Description: DataRowRange
   OperationID: DataRowRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DataRowRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DataRowRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataRowRange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/DataRowRange", {
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
   Summary: Invoke method DataRowLookup
   Description: DataRowLookup
   OperationID: DataRowLookup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DataRowLookup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DataRowLookup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataRowLookup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/DataRowLookup", {
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
   Summary: Invoke method DataLookup
   Description: DataLookup
   OperationID: DataLookup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DataLookup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DataLookup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataLookup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/DataLookup", {
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
   Summary: Invoke method EWCInitializeRuntime
   Description: Method to initialize the EWC runtime site files for the specific config ID.
   OperationID: EWCInitializeRuntime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EWCInitializeRuntime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EWCInitializeRuntime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EWCInitializeRuntime(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/EWCInitializeRuntime", {
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
   Summary: Invoke method EWCReadAllBytesIfNewer
   Description: Return the EWC Runtime files from the FileStore ConfigID.zip for the current Tenant and Company.
   OperationID: EWCReadAllBytesIfNewer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EWCReadAllBytesIfNewer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EWCReadAllBytesIfNewer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EWCReadAllBytesIfNewer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/EWCReadAllBytesIfNewer", {
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
   Summary: Invoke method GetTenantID
   Description: Return the Tenant ID from the current Company.
   OperationID: GetTenantID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTenantID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTenantID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTenantID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/GetTenantID", {
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
   Summary: Invoke method EWCWriteOrCreateAllBytes
   Description: Write or create the byte array to the FileStore for the current company, tenant.
   OperationID: EWCWriteOrCreateAllBytes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EWCWriteOrCreateAllBytes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EWCWriteOrCreateAllBytes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EWCWriteOrCreateAllBytes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/EWCWriteOrCreateAllBytes", {
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
   Summary: Invoke method GetPCTransportTableset
   Description: Returns the configuration specific data in the transport table for use in Question and Answer sessions not controlled by the
E10 client side run time engine.  This must be called once for every configurator involved in a configuration session.
   OperationID: GetPCTransportTableset
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPCTransportTableset_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPCTransportTableset_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPCTransportTableset(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/GetPCTransportTableset", {
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
   Summary: Invoke method SavePCTransportConfiguration
   Description: Method to save a configuration session to be used by Epicor Web
   OperationID: SavePCTransportConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SavePCTransportConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SavePCTransportConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SavePCTransportConfiguration(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/SavePCTransportConfiguration", {
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
   Summary: Invoke method DeleteTestInputsFileStoreEntry
   Description: Remove the temporary file storeS entry for Test Inputs
   OperationID: DeleteTestInputsFileStoreEntry
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteTestInputsFileStoreEntry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteTestInputsFileStoreEntry_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteTestInputsFileStoreEntry(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/DeleteTestInputsFileStoreEntry", {
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
   Summary: Invoke method PrepareEWCRequirements
   Description: This method retrieves the token and for enterprise configurators when in the sales company verifies the configurator has been deployed to EWC in that company and if not
executes the deploy logic so the end user is able to configure.
   OperationID: PrepareEWCRequirements
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrepareEWCRequirements_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrepareEWCRequirements_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrepareEWCRequirements(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PrepareEWCRequirements", {
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
   Summary: Invoke method GetECCConfigurator
   Description: Get ECC Part configurator initial data and process to return configuration setup to display Kinetic Configurator
   OperationID: GetECCConfigurator
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetECCConfigurator_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetECCConfigurator_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetECCConfigurator(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/GetECCConfigurator", {
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
   Summary: Invoke method GetNewPcValueGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcValueGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcValueGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcValueGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcValueGrp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/GetNewPcValueGrp", {
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
   Summary: Invoke method GetNewPcValueHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcValueHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcValueHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcValueHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcValueHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/GetNewPcValueHead", {
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
   Summary: Invoke method GetNewPcInputsLayerDetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcInputsLayerDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcInputsLayerDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcInputsLayerDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcInputsLayerDetail(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/GetNewPcInputsLayerDetail", {
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
   Summary: Invoke method GetNewPcInputsLayerHeader
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcInputsLayerHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcInputsLayerHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcInputsLayerHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcInputsLayerHeader(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/GetNewPcInputsLayerHeader", {
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
   Summary: Invoke method GetNewPcInputVar
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcInputVar
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcInputVar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcInputVar_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcInputVar(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/GetNewPcInputVar", {
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
   Summary: Invoke method GetNewPcValueInputLayerDetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcValueInputLayerDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcValueInputLayerDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcValueInputLayerDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcValueInputLayerDetail(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/GetNewPcValueInputLayerDetail", {
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
   Summary: Invoke method GetNewPcValueInputLayerHeader
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcValueInputLayerHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcValueInputLayerHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcValueInputLayerHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcValueInputLayerHeader(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/GetNewPcValueInputLayerHeader", {
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
   Summary: Invoke method GetNewQBuildMapping
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQBuildMapping
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQBuildMapping_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQBuildMapping_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQBuildMapping(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/GetNewQBuildMapping", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcConfigurationParamsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcConfigurationParamsRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcConfiguredDrawingsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcConfiguredDrawingsRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcContextPropertiesRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcContextPropertiesRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputVarRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcInputVarRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsLayerDetailRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcInputsLayerDetailRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsLayerHeaderRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcInputsLayerHeaderRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsPublishToDocParamsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcInputsPublishToDocParamsRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcValueGrpListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcValueGrpListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcValueGrpRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcValueGrpRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcValueHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcValueHeadRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcValueInputLayerDetailRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcValueInputLayerDetailRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcValueInputLayerHeaderRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcValueInputLayerHeaderRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QBuildMappingRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QBuildMappingRow[],
}

export interface Erp_Tablesets_PcConfigurationParamsRow{
   "ForeignTableName":string,
   "ForeignSysRowID":string,
   "TgtStructTag":string,
   "StructID":number,
   "InSmartString":string,
   "IsTestPlan":boolean,
   "SpecID":string,
   "SpecRevNum":string,
   "InspType":string,
   "RunningStateOverride":string,
   "EqmPassed":string,
   "EqmFailDesc":string,
   "EqmOverride":boolean,
   "RelatedToTable":string,
   "RelatedToSysRowID":string,
   "SourceTable":string,
   "TestID":string,
   "TestMode":string,
   "AppServerID":string,
   "PcStatusSysRowID":string,
   "ConfigVersion":number,
   "UniqueID":string,
   "ConfigID":string,
   "Company":string,
   "InputPricingSet":boolean,
   "OrderPrice":number,
   "QuotePrice":number,
   "DemandPrice":number,
   "PurchasePrice":number,
   "WebOrderBasketPrice":number,
   "PartNum":string,
   "RevisionNum":string,
   "AltMethod":string,
   "InitialStructTag":string,
   "InitialRuleTag":string,
      /**  Determines if a configuration was opened from a tracker.  */  
   "TrackerMode":boolean,
   "ConfigType":string,
      /**  This is the web address to call when launching an Epicor Web configurtor.  */  
   "EWCConfiguratorURL":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcConfiguredDrawingsRow{
   "Company":string,
   "ConfigID":string,
   "GroupSeq":number,
   "HeadNum":number,
   "InputName":string,
   "ImageID":string,
   "Content":string,
   "PageSeq":number,
   "QBuildObjExist":boolean,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcContextPropertiesRow{
   "AttributeID":string,
   "CompanyID":string,
   "ConfigurationID":string,
   "Currency":string,
   "CustomerID":string,
   "DemandHeadNumber":number,
   "DemandLineNumber":number,
   "Entity":string,
   "JobNumber":string,
   "OrderDetailNumber":number,
   "OrderNumber":number,
   "PackSlip":string,
   "PartNumber":string,
   "PartRevisionNumber":string,
   "PODetailNumber":number,
   "PONumber":number,
   "QuoteLineNumber":number,
   "QuoteNumber":number,
   "SpecificationID":string,
   "SpecificationRevision":string,
   "SupplierID":string,
   "UserID":string,
   "NonConfID":string,
   "AssemblySeq":number,
   "OprSeq":number,
   "RMALine":number,
   "PackLine":number,
   "SiteID":string,
   "ECCQuoteNum":string,
   "CustomerNumber":number,
   "SupplierNumber":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcInputVarRow{
      /**  Company  */  
   "Company":string,
      /**  VarName  */  
   "VarName":string,
      /**  DataType  */  
   "DataType":string,
      /**  InitValue  */  
   "InitValue":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "InitString":string,
   "InitDecimal":number,
   "InitLogical":boolean,
   "InitDate":string,
      /**  Determines if the variable is being used by an input.  */  
   "InUse":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcInputsLayerDetailRow{
      /**  Company  */  
   "Company":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  InputName  */  
   "InputName":string,
      /**  ImageLayerID  */  
   "ImageLayerID":string,
      /**  LayerSeq  */  
   "LayerSeq":number,
      /**  LayerName  */  
   "LayerName":string,
      /**  LayerDesc  */  
   "LayerDesc":string,
      /**  Order in which layers are placed on the base image.  */  
   "ZIndex":number,
      /**  ImageID  */  
   "ImageID":string,
      /**  Png type is supported.  */  
   "FileType":string,
      /**  Free form text enabling users to categorize layers  */  
   "Category":string,
      /**  Width of image  */  
   "Width":number,
      /**  Height of image  */  
   "Height":number,
      /**  Reserved for Future Development  */  
   "xPos":number,
      /**  Reserved for Future Development  */  
   "yPos":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcInputsLayerHeaderRow{
      /**  Company  */  
   "Company":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  Input name this header is assigned.  */  
   "InputName":string,
      /**  Image Layer ID.  */  
   "ImageLayerID":string,
      /**  File name of the image to be retrieved from the Image URL.  */  
   "ImageID":string,
      /**  Description  */  
   "Description":string,
      /**  The URL location of the image.  */  
   "ImageURL":string,
      /**  File types png and jpg are supported.  */  
   "FileType":string,
      /**  Image Width  */  
   "Width":number,
      /**  Image height  */  
   "Height":number,
      /**  Internal next number indicating the current version. Thi is is used by Verfiy Configuration to identify when a warning message is to be written to the log.  */  
   "Version":number,
      /**  Reserved for future development  */  
   "xPos":number,
      /**  Reserved for future development  */  
   "yPos":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcInputsPublishToDocParamsRow{
   "Key":string,
   "Value":string,
   "Company":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcValueGrpListRow{
      /**  Company  */  
   "Company":string,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  RelatedToTableName  */  
   "RelatedToTableName":string,
      /**  RelatedToSysRowID  */  
   "RelatedToSysRowID":string,
      /**  CreateDate  */  
   "CreateDate":string,
      /**  CreateUserID  */  
   "CreateUserID":string,
      /**  LastUpdated  */  
   "LastUpdated":string,
      /**  LastUpdatedBy  */  
   "LastUpdatedBy":string,
      /**  ConfigStatus  */  
   "ConfigStatus":string,
      /**  SIValues  */  
   "SIValues":boolean,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcValueGrpRow{
      /**  Company  */  
   "Company":string,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  RelatedToTableName  */  
   "RelatedToTableName":string,
      /**  RelatedToSysRowID  */  
   "RelatedToSysRowID":string,
      /**  CreateDate  */  
   "CreateDate":string,
      /**  CreateUserID  */  
   "CreateUserID":string,
      /**  LastUpdated  */  
   "LastUpdated":string,
      /**  LastUpdatedBy  */  
   "LastUpdatedBy":string,
      /**  ConfigStatus  */  
   "ConfigStatus":string,
      /**  SIValues  */  
   "SIValues":boolean,
      /**  HeadNum  */  
   "HeadNum":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "DisplaySummary":boolean,
   "IncomingSmartString":boolean,
      /**  Indicates if this value group was created because of a test (test inputs or test rules).  */  
   "TestID":string,
      /**  Indicates the test mode of this value group, note that TestID should be populated with a non empty Guid to make sure that all programs are generated as a test. Then this column will indicate if rules or anything else should be tested too.  */  
   "TestMode":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcValueHeadRow{
      /**  Company  */  
   "Company":string,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  HeadNum  */  
   "HeadNum":number,
      /**  StructTag  */  
   "StructTag":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  RevolvingSeq  */  
   "RevolvingSeq":number,
      /**  ForeignTableName  */  
   "ForeignTableName":string,
      /**  ForeignSysRowID  */  
   "ForeignSysRowID":string,
      /**  SourceTableName  */  
   "SourceTableName":string,
      /**  SourceSysRowID  */  
   "SourceSysRowID":string,
      /**  ConfigType  */  
   "ConfigType":string,
      /**  ConfigVersion  */  
   "ConfigVersion":number,
      /**  DisplayTag  */  
   "DisplayTag":string,
      /**  RuleTag  */  
   "RuleTag":string,
      /**  ExtConfig  */  
   "ExtConfig":boolean,
      /**  ExtCompany  */  
   "ExtCompany":string,
      /**  AllowRecordCreation  */  
   "AllowRecordCreation":boolean,
      /**  AllowPricing  */  
   "AllowPricing":boolean,
      /**  PromptForConfig  */  
   "PromptForConfig":boolean,
      /**  InSmartString  */  
   "InSmartString":boolean,
      /**  DisplaySummary  */  
   "DisplaySummary":boolean,
      /**  AllowReconfig  */  
   "AllowReconfig":boolean,
      /**  IsMainForeign  */  
   "IsMainForeign":boolean,
      /**  NewPartNum  */  
   "NewPartNum":string,
      /**  NewSmartString  */  
   "NewSmartString":string,
      /**  SIValues  */  
   "SIValues":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "SIValuesGroupSeq":number,
   "TestID":string,
      /**  Copied from the parent PcValueGrp record  */  
   "RelatedToSysRowID":string,
      /**  Value is brought from the parent PcValueGroup record.  */  
   "RelatedToTableName":string,
   "SIValuesHeadNum":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcValueInputLayerDetailRow{
      /**  Company  */  
   "Company":string,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  HeadNum  */  
   "HeadNum":number,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  Input Name  */  
   "InputName":string,
      /**  Image Layer ID  */  
   "ImageLayerID":string,
      /**  Programmatically calculated value used to keep the rows unique.  */  
   "LayerSeq":number,
      /**  LayerName  */  
   "LayerName":string,
      /**  LayerDesc  */  
   "LayerDesc":string,
      /**  ZIndex  */  
   "ZIndex":number,
      /**  Image ID  */  
   "ImageID":string,
      /**  Png file types are supported  */  
   "FileType":string,
      /**  Width  */  
   "Width":number,
      /**  Height  */  
   "Height":number,
      /**  Free form text  */  
   "Category":string,
      /**  Reserved for future development  */  
   "xPos":number,
      /**  Reserved for future development  */  
   "yPos":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcValueInputLayerHeaderRow{
      /**  Company  */  
   "Company":string,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  HeadNum  */  
   "HeadNum":number,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  Input Name  */  
   "InputName":string,
      /**  Image Layer ID  */  
   "ImageLayerID":string,
      /**  Image ID  */  
   "ImageID":string,
      /**  Description  */  
   "Description":string,
      /**  Location of Image  */  
   "ImageURL":string,
      /**  FileType  */  
   "FileType":string,
      /**  Width  */  
   "Width":number,
      /**  Height  */  
   "Height":number,
      /**  Used by Verify Configuration to identify changes in the layer definition.  */  
   "Version":number,
      /**  Reserved for future development  */  
   "xPos":number,
      /**  Reserved for future development  */  
   "yPos":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QBuildMappingRow{
      /**  Company  */  
   "Company":string,
      /**  Configuration ID  */  
   "ConfigID":string,
      /**  Input Name  */  
   "InputName":string,
      /**  This is the object name.  */  
   "ObjName":string,
      /**  This is the name of the object parameter.  */  
   "ObjParameter":string,
      /**  Name of the input mapped to this object parameter.  */  
   "MappedInputName":string,
      /**  This is the data type of the object parameter.  */  
   "ObjParameterDataType":string,
      /**  This is the initial value of the object parameter as it was defined in the designer.  This is reserved for future development.  */  
   "ObjParameterInitValue":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "DataType":string,
   "PageSeq":number,
   "BitFlag":number,
   "QBuildObjObjType":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param methodName
      @param parameterName
      @param configID
      @param paramSeq
      @param newValue
      @param pcValueDS
   */  
export interface AddUserDenfinedParameterBool_input{
   methodName:string,
   parameterName:string,
   configID:string,
   paramSeq:number,
   newValue:boolean,
   pcValueDS:Erp_Tablesets_PcValueTableset[],
}

export interface AddUserDenfinedParameterBool_output{
parameters : {
      /**  output parameters  */  
   pcValueDS:Erp_Tablesets_PcValueTableset[],
}
}

   /** Required : 
      @param methodName
      @param parameterName
      @param configID
      @param paramSeq
      @param newValue
      @param pcValueDS
   */  
export interface AddUserDenfinedParameterDateTime_input{
   methodName:string,
   parameterName:string,
   configID:string,
   paramSeq:number,
   newValue:string,
   pcValueDS:Erp_Tablesets_PcValueTableset[],
}

export interface AddUserDenfinedParameterDateTime_output{
parameters : {
      /**  output parameters  */  
   pcValueDS:Erp_Tablesets_PcValueTableset[],
}
}

   /** Required : 
      @param methodName
      @param parameterName
      @param configID
      @param paramSeq
      @param newValue
      @param pcValueDS
   */  
export interface AddUserDenfinedParameterDecimal_input{
   methodName:string,
   parameterName:string,
   configID:string,
   paramSeq:number,
   newValue:number,
   pcValueDS:Erp_Tablesets_PcValueTableset[],
}

export interface AddUserDenfinedParameterDecimal_output{
parameters : {
      /**  output parameters  */  
   pcValueDS:Erp_Tablesets_PcValueTableset[],
}
}

   /** Required : 
      @param methodName
      @param parameterName
      @param configID
      @param paramSeq
      @param newValue
      @param pcValueDS
   */  
export interface AddUserDenfinedParameterInt_input{
   methodName:string,
   parameterName:string,
   configID:string,
   paramSeq:number,
   newValue:number,
   pcValueDS:Erp_Tablesets_PcValueTableset[],
}

export interface AddUserDenfinedParameterInt_output{
parameters : {
      /**  output parameters  */  
   pcValueDS:Erp_Tablesets_PcValueTableset[],
}
}

   /** Required : 
      @param methodName
      @param parameterName
      @param configID
      @param paramSeq
      @param newValue
      @param pcValueDS
   */  
export interface AddUserDenfinedParameterString_input{
   methodName:string,
   parameterName:string,
   configID:string,
   paramSeq:number,
   newValue:string,
   pcValueDS:Erp_Tablesets_PcValueTableset[],
}

export interface AddUserDenfinedParameterString_output{
parameters : {
      /**  output parameters  */  
   pcValueDS:Erp_Tablesets_PcValueTableset[],
}
}

   /** Required : 
      @param configID
      @param docRuleCheckSyntaxArgs
      @param serverEventCheckSyntaxArgs
      @param methodRuleCheckSyntaxArgs
   */  
export interface CheckServerSyntax_input{
   configID:string,
   docRuleCheckSyntaxArgs:Erp_Shared_Lib_Configurator_DocRuleCheckSyntaxArgs[],
   serverEventCheckSyntaxArgs:Erp_Shared_Lib_Configurator_ServerEventCheckSyntaxArgs[],
   methodRuleCheckSyntaxArgs:Erp_Shared_Lib_Configurator_MethodRuleCheckSyntaxArgs[],
}

export interface CheckServerSyntax_output{
parameters : {
      /**  output parameters  */  
   syntaxErrors:string,
}
}

   /** Required : 
      @param pcValueDS
   */  
export interface ClearUDMethodParams_input{
   pcValueDS:Erp_Tablesets_PcValueTableset[],
}

export interface ClearUDMethodParams_output{
parameters : {
      /**  output parameters  */  
   pcValueDS:Erp_Tablesets_PcValueTableset[],
}
}

   /** Required : 
      @param configId
      @param testId
      @param lookupTableID
      @param colName
   */  
export interface DataColumnListNum_input{
      /**  The configuration ID  */  
   configId:string,
      /**  The test ID  */  
   testId:string,
      /**  The lookup table name  */  
   lookupTableID:string,
      /**  The column name  */  
   colName:string,
}

export interface DataColumnListNum_output{
   returnObj:string,
}

   /** Required : 
      @param configId
      @param testId
      @param lookupTableID
      @param colName
   */  
export interface DataColumnList_input{
      /**  The configuration ID  */  
   configId:string,
      /**  The test ID  */  
   testId:string,
      /**  The lookup table name  */  
   lookupTableID:string,
      /**  The column name  */  
   colName:string,
}

export interface DataColumnList_output{
   returnObj:string,
}

   /** Required : 
      @param configId
      @param testId
      @param lookupTblID
      @param colName
      @param searchValue
   */  
export interface DataColumnLookupList_input{
      /**  The configuration ID  */  
   configId:string,
      /**  The test ID  */  
   testId:string,
      /**  The lookup table name  */  
   lookupTblID:string,
      /**  The column name  */  
   colName:string,
   searchValue:string,
}

export interface DataColumnLookupList_output{
   returnObj:string,
}

   /** Required : 
      @param configId
      @param testId
      @param lookupTableID
      @param colName
      @param startRow
      @param endRow
   */  
export interface DataColumnRange_input{
      /**  The configuration ID  */  
   configId:string,
      /**  The test ID  */  
   testId:string,
      /**  The lookup table name  */  
   lookupTableID:string,
      /**  The column name  */  
   colName:string,
      /**  The Start row  */  
   startRow:string,
      /**  The end row  */  
   endRow:string,
}

export interface DataColumnRange_output{
   returnObj:string,
}

   /** Required : 
      @param configId
      @param testId
      @param lookupTblID
      @param rowName
      @param colName
   */  
export interface DataLookup_input{
      /**  The configuration ID  */  
   configId:string,
      /**  The test ID  */  
   testId:string,
      /**  The lookup table name  */  
   lookupTblID:string,
      /**  The row name  */  
   rowName:string,
      /**  The column name  */  
   colName:string,
}

export interface DataLookup_output{
   returnObj:string,
}

   /** Required : 
      @param configId
      @param testId
      @param lookupTableID
      @param rowName
   */  
export interface DataRowListNum_input{
      /**  The configuration ID  */  
   configId:string,
      /**  The test ID  */  
   testId:string,
      /**  The lookup table name  */  
   lookupTableID:string,
      /**  The row name  */  
   rowName:string,
}

export interface DataRowListNum_output{
   returnObj:string,
}

   /** Required : 
      @param configId
      @param testId
      @param lookupTableID
      @param rowName
   */  
export interface DataRowList_input{
      /**  The configuration ID  */  
   configId:string,
      /**  The test ID  */  
   testId:string,
      /**  The lookup table name  */  
   lookupTableID:string,
      /**  The row name  */  
   rowName:string,
}

export interface DataRowList_output{
   returnObj:string,
}

   /** Required : 
      @param configId
      @param testId
      @param lookupTblID
      @param rowName
      @param searchValue
   */  
export interface DataRowLookup_input{
      /**  The configuration ID  */  
   configId:string,
      /**  The test ID  */  
   testId:string,
      /**  The lookup table name  */  
   lookupTblID:string,
      /**  The row name  */  
   rowName:string,
      /**  The value to search  */  
   searchValue:string,
}

export interface DataRowLookup_output{
   returnObj:string,
}

   /** Required : 
      @param configId
      @param testId
      @param lookupTableID
      @param rowName
      @param startCol
      @param endCol
   */  
export interface DataRowRange_input{
      /**  The configuration ID  */  
   configId:string,
      /**  The test ID  */  
   testId:string,
      /**  The lookup table name  */  
   lookupTableID:string,
      /**  The row name  */  
   rowName:string,
      /**  The start column  */  
   startCol:string,
      /**  The end column.  */  
   endCol:string,
}

export interface DataRowRange_output{
   returnObj:string,
}

   /** Required : 
      @param configSequenceDS
      @param testID
   */  
export interface DeleteAssembliesInTestMode_input{
   configSequenceDS:Erp_Tablesets_ConfigurationSequenceTableset[],
      /**  Test Guid  */  
   testID:string,
}

export interface DeleteAssembliesInTestMode_output{
parameters : {
      /**  output parameters  */  
   configSequenceDS:Erp_Tablesets_ConfigurationSequenceTableset[],
}
}

   /** Required : 
      @param groupSeq
   */  
export interface DeleteByID_input{
   groupSeq:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param ttPcValueGrpRow
      @param ttPcStructRow
   */  
export interface DeleteSubConfiguration_input{
   ttPcValueGrpRow:Erp_Tablesets_PcValueGrpRow[],
   ttPcStructRow:Erp_Tablesets_PcStructRow[],
}

export interface DeleteSubConfiguration_output{
}

   /** Required : 
      @param testInputsFileName
   */  
export interface DeleteTestInputsFileStoreEntry_input{
      /**  file to delete  */  
   testInputsFileName:string,
}

export interface DeleteTestInputsFileStoreEntry_output{
}

   /** Required : 
      @param parentMfgCompID
      @param iDemandContractNum
      @param iDemandHeadSeq
      @param iDemandDtlSeq
      @param iSmartString
   */  
export interface EDIDemandConfiguration_input{
      /**  Parent Manufacturing Company ID  */  
   parentMfgCompID:string,
      /**  Demand Contract Number  */  
   iDemandContractNum:number,
      /**  Demand Head Sequence that contains the configurable line  */  
   iDemandHeadSeq:number,
      /**  Demand Detail Sequence that contains the configurable part  */  
   iDemandDtlSeq:number,
      /**  Smart String value  */  
   iSmartString:string,
}

export interface EDIDemandConfiguration_output{
}

   /** Required : 
      @param partNum
      @param revisionNum
      @param ipSmartString
   */  
export interface EDIValidateSmartString_input{
      /**  The part num being used.  */  
   partNum:string,
      /**  The revision num being used.  */  
   revisionNum:string,
      /**  Smart String value  */  
   ipSmartString:string,
}

export interface EDIValidateSmartString_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   ssLogText:string,
}
}

   /** Required : 
      @param ConfigId
      @param RelatedToTable
      @param RelatedToRowID
      @param PartNum
      @param PartRev
      @param ECCUser
      @param ECCPwd
      @param ReturnURL
      @param TestInputMode
   */  
export interface EWCInitializeRuntime_input{
      /**  The ConfigID to run  */  
   ConfigId:string,
      /**  The related to table name  */  
   RelatedToTable:string,
      /**  The related to SysRowID  */  
   RelatedToRowID:string,
      /**  The part number to configure  */  
   PartNum:string,
      /**  The revision to configure  */  
   PartRev:string,
      /**  The encrypted ECC user  */  
   ECCUser:string,
      /**  The encrypted ECC password  */  
   ECCPwd:string,
      /**  The return URL  */  
   ReturnURL:string,
      /**  True of running test inputs, else false for runtime  */  
   TestInputMode:boolean,
}

export interface EWCInitializeRuntime_output{
      /**  Path to index.html  */  
   returnObj:string,
parameters : {
      /**  output parameters  */  
   AccessToken:string,
   ExpiresIn:number,
}
}

   /** Required : 
      @param FileName
      @param LastModifiedUTCDateTime
   */  
export interface EWCReadAllBytesIfNewer_input{
      /**  The EWC runtime file name  */  
   FileName:string,
      /**  Only return the file if the UTC DateTime is greater than this parameter  */  
   LastModifiedUTCDateTime:string,
}

export interface EWCReadAllBytesIfNewer_output{
      /**  The file as a byte array  */  
   returnObj:string,
}

   /** Required : 
      @param configID
      @param testMode
      @param ipRelatedToTable
      @param ipRelatedToSysRowID
      @param smartStringValues
      @param subPartNum
      @param basePartNum
      @param partNum
      @param subBasePartNum
   */  
export interface EWCSuggestSmartString_input{
      /**  Configuration ID  */  
   configID:string,
      /**  Test Inputs true/false  */  
   testMode:boolean,
      /**  Target entity this call is related to  */  
   ipRelatedToTable:string,
      /**  The SysRowID of the target Entity  */  
   ipRelatedToSysRowID:string,
      /**  Collection of current input values gathered so far during the configuration session.  */  
   smartStringValues:System_Collections_Generic_KeyValuePair_System_String_System_String[],
   subPartNum:string,
   basePartNum:string,
   partNum:string,
   subBasePartNum:string,
}

export interface EWCSuggestSmartString_output{
parameters : {
      /**  output parameters  */  
   outSmartString:string,
}
}

   /** Required : 
      @param partNum
      @param revisionNum
      @param configID
      @param testRulesResultsDS
   */  
export interface EWCTestRules_input{
      /**  part number Test Rules was executed for  */  
   partNum:string,
      /**  revision number Test Rules was executed for  */  
   revisionNum:string,
      /**  Configuration ID Test Rules was executed for  */  
   configID:string,
   testRulesResultsDS:Erp_Tablesets_PcTestResultsTableset[],
}

export interface EWCTestRules_output{
parameters : {
      /**  output parameters  */  
   testRulesResultsDS:Erp_Tablesets_PcTestResultsTableset[],
}
}

   /** Required : 
      @param FileName
      @param Bytes
   */  
export interface EWCWriteOrCreateAllBytes_input{
      /**  The name of the file.  */  
   FileName:string,
      /**  The file contents  */  
   Bytes:string,
}

export interface EWCWriteOrCreateAllBytes_output{
}

export interface Erp_Shared_Lib_Configurator_ClientCheckSyntaxArgs{
   checkContext:number,
   tableName:string,
   inputName:string,
   pageNumber:number,
   syntaxCode:string,
   eventName:string,
   generateCSharpForEWC:boolean,
}

export interface Erp_Shared_Lib_Configurator_DocRuleCheckSyntaxArgs{
   docRuleContext:number,
   ruleNum:number,
   actionNum:number,
   docRuleType:number,
   commandType:string,
   lValue:string,
   rValue:string,
   rValueType:string,
   syntaxCode:string,
   DocVarNum:number,
}

export interface Erp_Shared_Lib_Configurator_MethodRuleCheckSyntaxArgs{
   ruleSetID:number,
   ruleNum:number,
   ruleTag:string,
   ruleType:number,
   expressionType:string,
   syntaxCode:string,
   KeepWhenType:string,
   PartNum:string,
   RevisionNum:string,
   AltMethod:string,
   SeqNum:number,
   VarNum:number,
}

export interface Erp_Shared_Lib_Configurator_PCKeyValuePair_System_String_System_String{
   Key:string,
   Value:string,
}

export interface Erp_Shared_Lib_Configurator_ServerEventCheckSyntaxArgs{
   serverEventTable:number,
   serverMethodName:string,
   expressionType:string,
   syntaxCode:string,
}

export interface Erp_Tablesets_ConfigurationRuntimeListTableset{
   PcValueGrpList:Erp_Tablesets_PcValueGrpListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ConfigurationRuntimeTableset{
   PcValueGrp:Erp_Tablesets_PcValueGrpRow[],
   PcValueHead:Erp_Tablesets_PcValueHeadRow[],
   PcConfigurationParams:Erp_Tablesets_PcConfigurationParamsRow[],
   PcConfiguredDrawings:Erp_Tablesets_PcConfiguredDrawingsRow[],
   PcContextProperties:Erp_Tablesets_PcContextPropertiesRow[],
   PcInputsLayerDetail:Erp_Tablesets_PcInputsLayerDetailRow[],
   PcInputsLayerHeader:Erp_Tablesets_PcInputsLayerHeaderRow[],
   PcInputsPublishToDocParams:Erp_Tablesets_PcInputsPublishToDocParamsRow[],
   PcInputVar:Erp_Tablesets_PcInputVarRow[],
   PcValueInputLayerDetail:Erp_Tablesets_PcValueInputLayerDetailRow[],
   PcValueInputLayerHeader:Erp_Tablesets_PcValueInputLayerHeaderRow[],
   QBuildMapping:Erp_Tablesets_QBuildMappingRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ConfigurationSequenceTableset{
   PcStruct:Erp_Tablesets_PcStructRow[],
   PcConfigSmartString:Erp_Tablesets_PcConfigSmartStringRow[],
   PcStrComp:Erp_Tablesets_PcStrCompRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ConfigurationSummaryRow{
   Company:string,
   QuoteNum:number,
   QuoteLine:number,
   OrderNum:number,
   OrderLine:number,
   JobNum:string,
   ConfigUnitPrice:number,
   ConfigBaseUnitPrice:number,
   DocConfigUnitPrice:number,
   DocConfigBaseUnitPrice:number,
   CurrSymbol:string,
   BaseCurrSymbol:string,
   CurrencySwitch:boolean,
   LastConfigDate:string,
   LastConfigTime:number,
   LastConfigUserID:string,
   Rpt1ConfigBaseUnitPrice:number,
   Rpt2ConfigBaseUnitPrice:number,
   Rpt3ConfigBaseUnitPrice:number,
   Rpt1ConfigUnitPrice:number,
   Rpt2ConfigUnitPrice:number,
   Rpt3ConfigUnitPrice:number,
   Rpt1DocConfigBaseUnitPrice:number,
   Rpt2DocConfigBaseUnitPrice:number,
   Rpt3DocConfigBaseUnitPrice:number,
   Rpt1DocConfigUnitPrice:number,
   Rpt2DocConfigUnitPrice:number,
   Rpt3DocConfigUnitPrice:number,
   BaseCurrencyID:string,
   CurrencyID:string,
   DemandContractNum:number,
   DemandHeadSeq:number,
   DemandDtlSeq:number,
   ConfigID:string,
   SmartString:string,
   BasePartNum:string,
   BaseRevisionNum:string,
   GroupSeq:number,
   HeadNum:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ConfigurationSummaryTableset{
   ConfigurationSummary:Erp_Tablesets_ConfigurationSummaryRow[],
   PcInputValue:Erp_Tablesets_PcInputValueRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MethodsListRow{
      /**  Original AssemblySeq  */  
   SeqNum:number,
   PartNum:string,
   RevisionNum:string,
   AltMethod:string,
   BomLevel:number,
   GeneratedRuleTag:string,
   IsConfig:boolean,
   TestType:string,
   Processed:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcActionResultRow{
   Company:string,
   RuleSetID:number,
   RuleSeq:number,
   SeqNum:number,
   ExprType:string,
   RuleTag:string,
   ExpressionText:string,
   ExprResult:string,
   TestType:string,
   ActionResult:string,
   ExprToolTip:string,
   BOMElementSysRowID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcAsmResultRow{
   Company:string,
   TestType:string,
   AssemblySeq:number,
   PartNum:string,
   RevisionNum:string,
   AltMethod:string,
   Description:string,
   RuleTag:string,
   ParentAsmSeq:number,
   ParentRuleTag:string,
   RelatedOperation:number,
   HasRuleSet:boolean,
   IsKept:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcConfigSmartStringRow{
   Company:string,
   ConfigID:string,
   StringStyle:string,
   PrefacePart:boolean,
      /**  Reserved for future development  */  
   CrtCustPart:boolean,
   Separator:string,
      /**  Reserved for future development  */  
   NumberFormat:string,
   StartNumber:number,
      /**  Reserved for future development  */  
   TargetEntityForSmartString:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcConfigurationParamsRow{
   ForeignTableName:string,
   ForeignSysRowID:string,
   TgtStructTag:string,
   StructID:number,
   InSmartString:string,
   IsTestPlan:boolean,
   SpecID:string,
   SpecRevNum:string,
   InspType:string,
   RunningStateOverride:string,
   EqmPassed:string,
   EqmFailDesc:string,
   EqmOverride:boolean,
   RelatedToTable:string,
   RelatedToSysRowID:string,
   SourceTable:string,
   TestID:string,
   TestMode:string,
   AppServerID:string,
   PcStatusSysRowID:string,
   ConfigVersion:number,
   UniqueID:string,
   ConfigID:string,
   Company:string,
   InputPricingSet:boolean,
   OrderPrice:number,
   QuotePrice:number,
   DemandPrice:number,
   PurchasePrice:number,
   WebOrderBasketPrice:number,
   PartNum:string,
   RevisionNum:string,
   AltMethod:string,
   InitialStructTag:string,
   InitialRuleTag:string,
      /**  Determines if a configuration was opened from a tracker.  */  
   TrackerMode:boolean,
   ConfigType:string,
      /**  This is the web address to call when launching an Epicor Web configurtor.  */  
   EWCConfiguratorURL:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcConfiguredDrawingsRow{
   Company:string,
   ConfigID:string,
   GroupSeq:number,
   HeadNum:number,
   InputName:string,
   ImageID:string,
   Content:string,
   PageSeq:number,
   QBuildObjExist:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcContextPropertiesRow{
   AttributeID:string,
   CompanyID:string,
   ConfigurationID:string,
   Currency:string,
   CustomerID:string,
   DemandHeadNumber:number,
   DemandLineNumber:number,
   Entity:string,
   JobNumber:string,
   OrderDetailNumber:number,
   OrderNumber:number,
   PackSlip:string,
   PartNumber:string,
   PartRevisionNumber:string,
   PODetailNumber:number,
   PONumber:number,
   QuoteLineNumber:number,
   QuoteNumber:number,
   SpecificationID:string,
   SpecificationRevision:string,
   SupplierID:string,
   UserID:string,
   NonConfID:string,
   AssemblySeq:number,
   OprSeq:number,
   RMALine:number,
   PackLine:number,
   SiteID:string,
   ECCQuoteNum:string,
   CustomerNumber:number,
   SupplierNumber:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcFieldPropertiesTransportRow{
   AttributeID:string,
   GroupSeq:number,
   HeadNum:number,
   Height:number,
   Increment:number,
   InitialValue:string,
   InputName:string,
   Invisible:boolean,
   Label:string,
   MaximumDate:string,
   MaximumDecimal:number,
   MinimumDate:string,
   MinimumDecimal:number,
   PageSeq:number,
   ReadOnly:boolean,
   Required:boolean,
   ToolTip:string,
   ValidList:string,
   ValueSetSeq:number,
   Width:number,
   XPosition:number,
   YPosition:number,
   ControlType:string,
   DataType:string,
   AutoSizeList:boolean,
   ListWidth:number,
   Description:string,
   ImageSource:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcImagesRow{
   Company:string,
   ConfigID:string,
   ImageID:string,
   Content:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcImagesTableset{
   PcImages:Erp_Tablesets_PcImagesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PcInputValueRow{
   Company:string,
   GroupSeq:number,
   PageSeq:number,
   SubTableName:string,
   InputName:string,
   InputValue:string,
   HeadNum:number,
   ReadOnly:boolean,
   NoDispSummary:boolean,
   SideLabel:string,
   SummaryLabel:string,
   ConfigID:string,
   TabOrder:number,
   PageTitle:string,
   DspPageSeq:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcInputVarRow{
      /**  Company  */  
   Company:string,
      /**  VarName  */  
   VarName:string,
      /**  DataType  */  
   DataType:string,
      /**  InitValue  */  
   InitValue:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   InitString:string,
   InitDecimal:number,
   InitLogical:boolean,
   InitDate:string,
      /**  Determines if the variable is being used by an input.  */  
   InUse:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcInputsLayerDetailRow{
      /**  Company  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  InputName  */  
   InputName:string,
      /**  ImageLayerID  */  
   ImageLayerID:string,
      /**  LayerSeq  */  
   LayerSeq:number,
      /**  LayerName  */  
   LayerName:string,
      /**  LayerDesc  */  
   LayerDesc:string,
      /**  Order in which layers are placed on the base image.  */  
   ZIndex:number,
      /**  ImageID  */  
   ImageID:string,
      /**  Png type is supported.  */  
   FileType:string,
      /**  Free form text enabling users to categorize layers  */  
   Category:string,
      /**  Width of image  */  
   Width:number,
      /**  Height of image  */  
   Height:number,
      /**  Reserved for Future Development  */  
   xPos:number,
      /**  Reserved for Future Development  */  
   yPos:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcInputsLayerHeaderRow{
      /**  Company  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  Input name this header is assigned.  */  
   InputName:string,
      /**  Image Layer ID.  */  
   ImageLayerID:string,
      /**  File name of the image to be retrieved from the Image URL.  */  
   ImageID:string,
      /**  Description  */  
   Description:string,
      /**  The URL location of the image.  */  
   ImageURL:string,
      /**  File types png and jpg are supported.  */  
   FileType:string,
      /**  Image Width  */  
   Width:number,
      /**  Image height  */  
   Height:number,
      /**  Internal next number indicating the current version. Thi is is used by Verfiy Configuration to identify when a warning message is to be written to the log.  */  
   Version:number,
      /**  Reserved for future development  */  
   xPos:number,
      /**  Reserved for future development  */  
   yPos:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcInputsPublishToDocParamsRow{
   Key:string,
   Value:string,
   Company:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcJobAsmblRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if the Job is complete.  This is a mirror image of JobHead.JobComplete.  Not directly maintainable.  When Job is complete, then all assembly records are also marked complete.  This is used to make database access to open assembly records more efficient.  */  
   JobComplete:boolean,
      /**  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  */  
   JobNum:string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  */  
   AssemblySeq:number,
      /**  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  */  
   PartNum:string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   Description:string,
      /**  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  The production quantity required for this assembly per one of it's parent part.  */  
   QtyPer:number,
      /**  The internal unit of measure for this assembly.  Use the Part.IUM as a default.  */  
   IUM:string,
      /**   This is how many of the assemblies are required to produce the END ITEM.  This is a calculated field.  Calculated as the (( Parents RequiredQty - Parents PullQty) X QtyPer) + OverRunQty.
This field needs to be refreshed whenever a change is made to the production quantity in any of its parents or when its QtyPer, or Overrun fields are changed. The refresh may also occur if the structure of the assemblies is changed.
The production quantity for the assembly which will drive raw material requirements and estimated production times can be determined by ( RequiredQty - PullQty).  */  
   RequiredQty:number,
      /**  This indicates a quantity that will be pulled from inventory for this assembly instead of being manufactured. This is a fixed quantity and is not affected by  QtyPer type changes. If this a valid Part, then it must update the PartWhse.AllocQty.  */  
   PullQty:number,
      /**  This is the warehouse that the material is allocated against.  */  
   WarehouseCode:string,
      /**  The material burden rate for this Job Assembly.  */  
   MtlBurRate:number,
      /**  The estimated unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  */  
   EstUnitCost:number,
      /**  The estimated Mtl burden unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  */  
   EstMtlBurUnitCost:number,
      /**  This value indicates a quantity that is planned to be overrun and put into inventory. This is kept as a separate field so that is does not distort the BOM requirement relationships. This increases the total production quantity for the assembly.  This is a FIXED quantity and is not affected by structure or qty/per type changes.  */  
   OverRunQty:number,
      /**  Scheduled start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process.  */  
   StartDate:string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  */  
   StartHour:number,
      /**  The scheduled due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  */  
   DueDate:string,
      /**  This field is established by scheduling.  It represents the  "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  */  
   DueHour:number,
      /**  Sequence number of the Parent Assembly.  */  
   Parent:number,
      /**   The  sequence number of the prior assembly that is on the same level as this assembly.  This  is known as a PriorPeer assembly.  This is automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the NextPeer is -1.  Then NextPeer of that assembly gets updated with this assemblies sequence number and this assembly gets its PriorPeer field updated with the sequence number from the assembly which was found.  */  
   PriorPeer:number,
      /**   The sequence number of the Next Assembly on the same level as this assembly.  This is known as a NextPeer assembly.  Automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the PriorPeer is -1.  Then the PriorPeer of that assembly is updated with this assemblies sequence number and then this assemblies NextPeer gets updated with the sequence number from the assembly that was found.  */  
   NextPeer:number,
      /**  Sequence number of this assemblies very first subassembly.  This is known as the Child assembly.  Automatically maintained by the maintenance programs.  The logic is to find the Parent assembly record and if its child is -1, update it with this assemblies sequence number.  */  
   Child:number,
      /**  Total cost to date, of this component that was issued from stock.  */  
   TotalCost:number,
      /**  Total material burden cost to date, of this component that was issued from stock.  */  
   MtlBurCost:number,
      /**  This quantity is a summary of all Issue Transactions that were issued to meet this assemblies PullQty requirements.  This is not directly maintainable.  */  
   IssuedQty:number,
      /**  Optional field for Engineering Drawing Number.  Defaulted from BomHead.DrawNum during methods pull functions.  */  
   DrawNum:string,
      /**  Indicates if the pull quantity has been issued complete.  If "yes" then this record is NOT part of the PartWhse.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  */  
   IssuedComplete:boolean,
      /**  Editor widget for Job Assembly comments.  */  
   CommentText:string,
      /**  Indicates if this assembly is to be included in the browse of assemblies in the  "get details" function.  The user can use this option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly, it just keeps it out of the browse.  */  
   InCopyList:boolean,
      /**  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  */  
   BomSequence:number,
      /**  An internally system assigned integer which represents the "Level of Indention" of the assembly in reference to the Bill of Material structure.  */  
   BomLevel:number,
      /**  Scheduled "What If" start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process  */  
   WIStartDate:string,
      /**  This field is established by scheduling.  It represents the What-If  "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  */  
   WIStartHour:number,
      /**  The scheduled "What-If" due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  */  
   WIDueDate:string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  */  
   WIDueHour:number,
      /**  This Level Actual Labor Cost.  */  
   TLALaborCost:number,
      /**  This Level Actual Burden Cost.  */  
   TLABurdenCost:number,
      /**  This Level Actual Material Cost.  */  
   TLAMaterialCost:number,
      /**  This Level Actual Subcontract Cost.  */  
   TLASubcontractCost:number,
      /**  This Level Actual Material Burden Cost.  */  
   TLAMtlBurCost:number,
      /**  This Level Actual Setup Hours.  */  
   TLASetupHours:number,
      /**  This Level Actual Production Hours.  */  
   TLAProdHours:number,
      /**  This Level Estimated Labor Cost.  */  
   TLELaborCost:number,
      /**  This Level Estimated Burden Cost.  */  
   TLEBurdenCost:number,
      /**  This Level Estimated Material Cost.  */  
   TLEMaterialCost:number,
      /**  This Level Estimated Subcontract Cost.  */  
   TLESubcontractCost:number,
      /**  This Level Estimated Material Burden Cost.  */  
   TLEMtlBurCost:number,
      /**  This Level Estimated Setup Hours.  */  
   TLESetupHours:number,
      /**  This Level Estimated Production Hours.  */  
   TLEProdHours:number,
      /**  Lower Level Actual Labor Cost.  */  
   LLALaborCost:number,
      /**  Lower Level Burden Labor Cost.  */  
   LLABurdenCost:number,
      /**  Lower Level Actual Material Cost.  */  
   LLAMaterialCost:number,
      /**  Lower Level Actual Subcontractor Cost.  */  
   LLASubcontractCost:number,
      /**  Lower Level Actual Material Burden Cost.  */  
   LLAMtlBurCost:number,
      /**  Lower Level Actual Setup Hours.  */  
   LLASetupHours:number,
      /**  Lower Level Actual Production Hours.  */  
   LLAProdHours:number,
      /**  Lower Level Estimated Labor Cost.  */  
   LLELaborCost:number,
      /**  Lower Level Estimated Burden Cost.  */  
   LLEBurdenCost:number,
      /**  Lower Level Estimated Material Cost.  */  
   LLEMaterialCost:number,
      /**  Lower Level Estimated Subcontract Cost.  */  
   LLESubcontractCost:number,
      /**  Lower Level Estimated Material Burden Cost.  */  
   LLEMtlBurCost:number,
      /**  Lower Level Estimated Setup Hours.  */  
   LLESetupHours:number,
      /**  Lower Level Estimated Production Hours.  */  
   LLEProdHours:number,
      /**   The operation number (JobOper.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable.  Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   AutoRecOpr:number,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   FinalOpr:number,
      /**  FUTURE IMPLEMENTATION - Characters used on the parent assembly drawing to show where assembly  is used.  */  
   FindNum:string,
      /**  Total received to stock.  This pertains receiving an OverRun quantity.  Used to update the PartDtl file for expected production quantity.  PartDtl is OverRun - ReceivedToStock.  */  
   ReceivedToStock:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Indicates if this assembly material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified..  */  
   Direct:boolean,
      /**   An assembly record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this assembly is required at the very beginning of the production job.  The related operation is also used to calculate scheduled start date.  */  
   RelatedOperation:number,
      /**  This Level Actual Material Labor Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialLabCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   TLAMaterialLabCost:number,
      /**  This Level Actual Issued Material Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialMtlCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   TLAMaterialMtlCost:number,
      /**  This Level Actual Material Subcontract Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialSubCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   TLAMaterialSubCost:number,
      /**  This Level Actual Material Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialBurCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   TLAMaterialBurCost:number,
      /**  Lower Level Actual Material Labor Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialLabCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   LLAMaterialLabCost:number,
      /**  Lower Level Actual Material Material Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialMtlCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   LLAMaterialMtlCost:number,
      /**  Lower Level Actual Material Subcontract Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialSubCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   LLAMaterialSubCost:number,
      /**  Lower Level Actual Material Burden Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialBurCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   LLAMaterialBurCost:number,
      /**  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  */  
   TotalMtlMtlCost:number,
      /**  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   TotalMtlLabCost:number,
      /**  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   TotalMtlSubCost:number,
      /**  Total Burden cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   TotalMtlBurCost:number,
      /**  The service call that this assembly belongs to.  */  
   CallNum:number,
      /**  The Service Call Line that this assembly relates to.  */  
   CallLine:number,
      /**  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  */  
   RestoreFlag:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  The date when the configuration was completed for the assembly.  */  
   LastConfigDate:string,
      /**  The system time when the configuration was completed for the assembly.  */  
   LastConfigTime:number,
      /**  The User ID of the last user to complete the configuration of the assembly.  */  
   LastConfigUserID:string,
      /**  This field will be set to the value of the JobAsmbl.RequiredQty at the time the JobHead.Engineered flag is set to true.  */  
   OrigRequiredQty:number,
      /**  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   UserMapData:string,
      /**  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  */  
   WhseAllocFlag:boolean,
      /**  This Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for this level.  Otherwise, TLAMaterialMtlBurCost may be populated but is not included in the calculation of TLAMaterialCost.  */  
   TLAMaterialMtlBurCost:number,
      /**  Lower Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for the lower level.  Otherwise, LLAMaterialMtlBurCost may be populated but is not included in the calculation of LLAMaterialCost.  */  
   LLAMaterialMtlBurCost:number,
      /**  This Level Actual Component Labor Cost.  This is the Total Labor costs of all manufactured parts issued as material for this level. Unlike TLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   TLAMfgCompLabCost:number,
      /**  This Level Actual Component Material Cost.  This is the Total Material costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   TLAMfgCompMtlCost:number,
      /**  This Level Actual Component Subcontract Cost.  This is the Total Subcontract costs of all manufactured parts issued as material for this level. Unlike TLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   TLAMfgCompSubCost:number,
      /**  This Level Actual Component Burden Cost.  This is the Total Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   TLAMfgCompBurCost:number,
      /**  This Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   TLAMfgCompMtlBurCost:number,
      /**  Lower Level Actual Component Labor Cost. This is the Total Labor costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   LLAMfgCompLabCost:number,
      /**  Lower Level Actual Component Material Cost. This is the Total Material costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   LLAMfgCompMtlCost:number,
      /**  Lower Level Actual Component Subcontract Cost. This is the Total Subcontract costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   LLAMfgCompSubCost:number,
      /**  Lower Level Actual Component Burden Cost. This is the Total Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   LLAMfgCompBurCost:number,
      /**  Lower Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   LLAMfgCompMtlBurCost:number,
      /**  Assembly Weight defaulted from Part Master.  */  
   Weight:number,
      /**  Assembly Weight UOM defaulted from Part Master.  */  
   WeightUOM:string,
      /**  Original Material Sequence. Used in the configurator.  */  
   OrigMtlSeq:number,
      /**  Original Rule Tag. Used in the Configurator.  */  
   OrigRuleTag:string,
      /**  Validate Reference Designators.  */  
   ValRefDes:boolean,
      /**  Base Part Number. Used in the configurator to identify the configurator part Number.  */  
   BasePartNum:string,
      /**  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  */  
   BaseRevisionNum:string,
      /**   The estimated material unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   EstMtlUnitCost:number,
      /**   The estimated labor unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   EstLbrUnitCost:number,
      /**   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   EstBurUnitCost:number,
      /**   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   EstSubUnitCost:number,
      /**  Indicates if the sub-assemby can be spawned off to a different job.  This can occur during the firming up of a job.  */  
   PlanAsAsm:boolean,
      /**  Plan as assembly reference.  Used to link related subassemblies together when multiple assemblies are created for the same part due to PartSite lot size values.  */  
   PAARef:string,
      /**  Used only on Plan As Assembly records.  Indicates the sub assembly will be split of from the the current job and a separate job for the assembly will be created.  */  
   PAAFirm:boolean,
      /**  EstScrap =  a number representing either a scrap qty or a scrap percent depending on the value of EstScrapType field.  */  
   EstScrap:number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   EstScrapType:string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   SmartStringProcessed:boolean,
      /**  Original smart string passed in for configuration  */  
   SmartString:string,
      /**  Required number of designators  */  
   ReqRefDes:number,
      /**  Reassign Serial Numbers Assembly  */  
   ReassignSNAsm:boolean,
      /**  This Level Actual Other Direct Cost.  */  
   TLAODCCost:number,
      /**  AssemblyMatch  */  
   AssemblyMatch:string,
      /**  JdfStatus  */  
   JdfStatus:string,
      /**  PressDevice  */  
   PressDevice:string,
      /**  DigitalFileName  */  
   DigitalFileName:string,
      /**  PrepressJobName  */  
   PrepressJobName:string,
      /**  JdfPrepressAction  */  
   JdfPrepressAction:string,
      /**  SendToPress  */  
   SendToPress:boolean,
      /**  RemovedFromPlan  */  
   RemovedFromPlan:boolean,
      /**  SendToPressInitiator  */  
   SendToPressInitiator:number,
      /**  OperationType  */  
   OperationType:number,
      /**  SendToPrePress  */  
   SendToPrePress:boolean,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PartPlanInfo  */  
   PartPlanInfo:string,
      /**  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   OrigStructTag:string,
      /**  ContractID  */  
   ContractID:string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the Planning Contract.  */  
   LinkToContract:boolean,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   KBConfigProdID:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcJobHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  */  
   JobClosed:boolean,
      /**  Date the Job was closed.  Defaults as the system but can be overridden.  */  
   ClosedDate:string,
      /**  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  */  
   JobComplete:boolean,
      /**  The date that production was completed for this Job.  Maintained via Job Completion Processing.  */  
   JobCompletionDate:string,
      /**  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  */  
   JobEngineered:boolean,
      /**   Optional Job check off number 1.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff1:boolean,
      /**   Optional Job check off number 2.  The label for this field is found in JCSyst. If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff2:boolean,
      /**   Optional Job check off number 3.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff3:boolean,
      /**  Optional Job check off number 4.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff4:boolean,
      /**  Optional Job check off number 5.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff5:boolean,
      /**  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  */  
   JobReleased:boolean,
      /**  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  */  
   JobHeld:boolean,
      /**  Scheduling Status Control (R-Required, P-Pending, A-Active, C-Complete).  NOT CURRENTLY IMPLEMENTED.  */  
   SchedStatus:string,
      /**  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  */  
   JobNum:string,
      /**   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  */  
   PartNum:string,
      /**  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  */  
   DrawNum:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   PartDescription:string,
      /**  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  */  
   ProdQty:number,
      /**  The unit of measure for the job.  Defaulted from Part.IUM.  */  
   IUM:string,
      /**  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   StartDate:string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   StartHour:number,
      /**  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  */  
   DueDate:string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  */  
   DueHour:number,
      /**  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  */  
   ReqDueDate:string,
      /**  An optional user defined code.  This will be used for report selections and views of job headers.  */  
   JobCode:string,
      /**  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  */  
   QuoteNum:number,
      /**  Contains the quote line number reference. (see QuoteNum )  */  
   QuoteLine:number,
      /**  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  UserChar1  */  
   UserChar1:string,
      /**  UserChar2  */  
   UserChar2:string,
      /**  UserChar3  */  
   UserChar3:string,
      /**  UserChar4  */  
   UserChar4:string,
      /**  UserDate1  */  
   UserDate1:string,
      /**  UserDate2  */  
   UserDate2:string,
      /**  UserDate3  */  
   UserDate3:string,
      /**  UserDate4  */  
   UserDate4:string,
      /**  UserDecimal1  */  
   UserDecimal1:number,
      /**  UserDecimal2  */  
   UserDecimal2:number,
      /**  UserInteger1  */  
   UserInteger1:number,
      /**  UserInteger2  */  
   UserInteger2:number,
      /**  Editor widget for Job header comments.  */  
   CommentText:string,
      /**  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  */  
   ExpenseCode:string,
      /**  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  */  
   InCopyList:boolean,
      /**   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  */  
   WIName:string,
      /**  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   WIStartDate:string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   WIStartHour:number,
      /**  Scheduled "What If" finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  */  
   WIDueDate:string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  */  
   WIDueHour:number,
      /**   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  */  
   Candidate:boolean,
      /**  Scheduling Code.  SchedCode references a record in the SchedPri table.  */  
   SchedCode:string,
      /**  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  */  
   SchedLocked:boolean,
      /**  Associates the JobHead with a project in the Project table.  This can be blank.  */  
   ProjectID:string,
      /**  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  */  
   WIPCleared:boolean,
      /**  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  */  
   JobFirm:boolean,
      /**  A LIST-DELIM delimited list of people.  */  
   PersonList:string,
      /**   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  */  
   PersonID:string,
      /**  Production Team for the Job.  Associates the JobHead with a ProdTeam.  */  
   ProdTeamID:string,
      /**   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  */  
   QtyCompleted:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  */  
   DatePurged:string,
      /**  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  */  
   TravelerReadyToPrint:boolean,
      /**  The last date the job traveler was mass printed.  */  
   TravelerLastPrinted:string,
      /**  Indicates if the Status can be printed. Print functions are not available if this is = No.  */  
   StatusReadyToPrint:boolean,
      /**  The last date the job status was mass printed.  */  
   StatusLastPrinted:string,
      /**  The Service Call number that this Job is linked to.  */  
   CallNum:number,
      /**  The Service Call Line that this Job is linked to.  */  
   CallLine:number,
      /**  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  */  
   JobType:string,
      /**  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  */  
   RestoreFlag:string,
      /**  Project Phase ID  */  
   PhaseID:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  Indicates that the quantity on this job is locked  */  
   LockQty:boolean,
      /**  The help desk case that created this job.  */  
   HDCaseNum:number,
      /**   Values: S(Sequential) or C(Concurrent).
Defaults as S. Must have Advanced Production License to change. Controls how the operations and material requirements are developed. Concurrent jobs are used where the production time is based on the number of machine operations performed and not on the number of parts created. For example, a stamping operation where each cycle of the machine stamps out x number of parts. A further extension of this is that the operation can yield multiple different parts from each cycle of the machine.  Identification of these parts and there associated PPO (parts per operation) is define in the JobPart table.  */  
   ProcessMode:string,
      /**  The planned date when the job needs to be actioned by the production department to make sure that the job is ready on the planned completion date.  */  
   PlannedActionDate:string,
      /**  The date that the job needs to be ready for the warehouse to kit to make sure that it is ready for the job start date.  */  
   PlannedKitDate:string,
      /**  The task ID that is returned from Microsoft Project.  */  
   MSPTaskID:string,
      /**  This is the Microsoft Project predecessor. This needs to be a text field as Microsoft Project may pass back an alpha numeric string.  */  
   MSPPredecessor:string,
      /**  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   UserMapData:string,
      /**  Flag to indicate whether operations for this job will use the production yield features set up in OpMaster for the operation code. Defaulted from Site.ProductionYield  */  
   ProductionYield:boolean,
      /**  This field will be set to the value of the JobHead.ProdQty at the time the JobHead.Engineered flag is set to true.  */  
   OrigProdQty:number,
      /**  This field is used to indicate whether the original quantities should be reset in the job header and its assemblies at JobHead update if JobHead.JobEngineered has been changed from false to true. Generally the orig qtys will be reset, unless this flag is set to true because the user was asked if they wanted to reset the orig qtys and they answered yes.  */  
   PreserveOrigQtys:boolean,
      /**  If set to yes then exclude this job from the Job Auto-Completion process. Not directly maintainable.  */  
   NoAutoCompletion:boolean,
      /**  No Auto Closing. If set to yes then exclude this job from the Job Auto-Closing process.  */  
   NoAutoClosing:boolean,
      /**  The user that created this Job.  */  
   CreatedBy:string,
      /**  The date that this Job was created.  */  
   CreateDate:string,
      /**  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  */  
   WhseAllocFlag:boolean,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   OwnershipStatus:string,
      /**  Holds the internal object id of PDM parts.  */  
   PDMObjID:string,
      /**  This field is used to store a code that represents the external system that the Job is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  */  
   ExportRequested:string,
      /**  Flag to indicate how to split the manufacturing cost elements when a manufactured material is issued to the job.  If flag is set to true, the cost of the issued material will be split into individual manufacturing cost elements. If set to false, the cost of the issued material is added to the manufacturing material cost element only.  This is defaulted from the JCSyst.SplitMfgCostElements and is not user maintainable.  */  
   SplitMfgCostElements:boolean,
      /**  Cross Reference Part Num. Used for alternate serial mask support.  */  
   XRefPartNum:string,
      /**   Cross Reference Part Type. Used for alternate serial mask support.

I=Internal Cross Reference / C = Customer Part  */  
   XRefPartType:string,
      /**  Customer Number XRefPartNum is related to if it is a customer part. Used for alternate serial number mask support.  */  
   XRefCustNum:number,
      /**  Base Part Number. Used in the configurator to identify the configurator part Number.  */  
   BasePartNum:string,
      /**  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  */  
   BaseRevisionNum:string,
      /**  Indicates if the job was rough cut scheduled.  */  
   RoughCutScheduled:boolean,
      /**   The ID of the Equipment that this "Maintenance Job" is for.
Foreign key component to Equip table.  */  
   EquipID:string,
      /**   Preventive Maintenance Plan Number that this "Maintenance Job" is for. Foreign key component to EquipPlan table.
Note: A Maintenance Job does not have to be for a Preventive Maintenance plan, in which case this is zero.
If time based plan, then the closing process will update the EquipPlan.NextDate. Therefore, the Job must know the EquipID and PlanNum in order to do this.  */  
   PlanNum:number,
      /**  Maintenance Job Priority. Valid values: H - High, M - Medium, L - Low.  M is default or if created from a Maint Request then MaintReq.Priority is used as default.  */  
   MaintPriority:string,
      /**  Internal field indicating this job was created by a job split.  Assigned true when a job has been split due to start minimum lot size quantity processing.  */  
   SplitJob:boolean,
      /**  Indicates the type of prefix which is used for create jobs in MRP  */  
   NumberSource:boolean,
      /**  The Meter Reading value entered at time of Job Closing.  */  
   CloseMeterReading:number,
      /**  Maintenance Issue Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  */  
   IssueTopicID1:string,
      /**  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  */  
   IssueTopicID2:string,
      /**  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  */  
   IssueTopicID3:string,
      /**  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  */  
   IssueTopicID4:string,
      /**  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  */  
   IssueTopicID5:string,
      /**  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  */  
   IssueTopicID6:string,
      /**  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  */  
   IssueTopicID7:string,
      /**  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  */  
   IssueTopicID8:string,
      /**  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  */  
   IssueTopicID9:string,
      /**  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  */  
   IssueTopicID10:string,
      /**  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  */  
   IssueTopics:string,
      /**  Maintenance Resolution Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintRes = Yes  */  
   ResTopicID1:string,
      /**  Maintenance Resolution Topic 2. A sub-topic of ResTopicID1.  */  
   ResTopicID2:string,
      /**  Maintenace  Resolution Topic 3. A sub-topic of ResTopicID2.  */  
   ResTopicID3:string,
      /**  Maintenance Resolution Topic 4. A sub-topic of ResTopicID3.  */  
   ResTopicID4:string,
      /**  Maintenance Resolution Topic 5. A sub-topic of ResTopicID4.  */  
   ResTopicID5:string,
      /**  Maintenance Resolution Topic 6. A sub-topic of ResTopicID5.  */  
   ResTopicID6:string,
      /**  Maintenance Resolution Topic 7. A sub-topic of ResTopicID6.  */  
   ResTopicID7:string,
      /**  Maintenance Resolution Topic 8. A sub-topic of ResTopicID7.  */  
   ResTopicID8:string,
      /**  Maintenance Resolution Topic 9. A sub-topic of ResTopicID8.  */  
   ResTopicID9:string,
      /**  Maintenance Resolution Topic 10. A sub-topic of ResTopicID9.  */  
   ResTopicID10:string,
      /**  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  */  
   ResTopics:string,
      /**  It is updated by Calculate Global Scheduling Order process, it indicates if a job has to be scheduled Backwards or Forwards by Global Scheduling Process and it can be modified by Adjust Scheduling Global Order  */  
   Forward:boolean,
      /**  This is the sequence number used to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  */  
   SchedSeq:number,
      /**  Indicates if at least one subassembly contains a part that is plan as assembly.  It does not indicate if the assembly is marked as PAA - only that the part is PAA in the BOM.  Used in MRP when determining if a job can be reused.  */  
   PAAExists:boolean,
      /**  Indicates if the job structure (BOM) was created inside or outside of the mfg lead time for the job part.  Used in MRP when determining if a job can be reused.  */  
   DtlsWithinLeadTime:boolean,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  It indicates that the shop load for that job was not generated (shopload table). The load in shopload can be recreated by Save Resource Load process  */  
   RoughCut:boolean,
      /**  PlanGUID  */  
   PlanGUID:string,
      /**  PlanUserID  */  
   PlanUserID:string,
      /**  LastChangedBy  */  
   LastChangedBy:string,
      /**  LastChangedOn  */  
   LastChangedOn:string,
      /**  EPMExportLevel  */  
   EPMExportLevel:number,
      /**  JobWorkflowState  */  
   JobWorkflowState:string,
      /**  JobCSR  */  
   JobCSR:string,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  LastExternalMESDate  */  
   LastExternalMESDate:string,
      /**  LastScheduleDate  */  
   LastScheduleDate:string,
      /**  LastScheduleProc  */  
   LastScheduleProc:string,
      /**  Sequence priority used internally by Calculate Global Scheduling Order process to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  */  
   SchedPriority:number,
      /**  It indicates the days a job is going to be late in relation to its required due date  */  
   DaysLate:number,
      /**  ContractID  */  
   ContractID:string,
      /**  Logical field to indicate if this record has been read by project analysis process  */  
   ProjProcessed:boolean,
      /**  SyncReqBy  */  
   SyncReqBy:boolean,
      /**  CustName  */  
   CustName:string,
      /**  CustID  */  
   CustID:string,
      /**  IsCSRSet  */  
   IsCSRSet:boolean,
      /**  UnReadyCostProcess  */  
   UnReadyCostProcess:boolean,
      /**  ProcSuspendedUpdates  */  
   ProcSuspendedUpdates:string,
      /**  DateTime field to indicate when this record has been read by project analysis process  */  
   ProjProcessedDate:string,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
      /**  Related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   KBConfigProdID:number,
      /**  Indicates if this revision is to use Advanced Staging.  */  
   UseAdvancedStaging:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  PersonIDName  */  
   PersonIDName:string,
      /**  This flag indicates if the job is ready to be fulfilled.  */  
   ReadyToFulfill:boolean,
      /**  FSMSendTo  */  
   FSMSendTo:boolean,
      /**  FSMServiceReportID  */  
   FSMServiceReportID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcJobMtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if  "Job"  is complete.  This is a mirror image of JobHead.Complete.  Not directly maintainable.  When the Job is completed, then all JobMtl records are also marked.  This is used to make database access to open material records more efficient.  */  
   JobComplete:boolean,
      /**  Indicates if this material requirement has been issued complete.  If "yes" then this record is NOT part of the Part.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  */  
   IssuedComplete:boolean,
      /**  Job Number.  */  
   JobNum:string,
      /**  Assembly sequence number that this material is associated with.  */  
   AssemblySeq:number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   MtlSeq:number,
      /**  Part number.  If the material is being purchased (JobMtl.BuyIt = yes) this does need to be a valid part in the Part file.  */  
   PartNum:string,
      /**  A description of the material.  */  
   Description:string,
      /**  Quantity per parent.  Field Service was EstQty in FSCallMt.  */  
   QtyPer:number,
      /**  Required Quantity per END ITEM.  This is a calculated field.  Calculated as (Parent Required Qty X QtyPer) + calculated Scrap.  The parent quantity is either the JobHead.ProdQty if  JobMtl.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobMtl.AssemblySeq > 0.  */  
   RequiredQty:number,
      /**  Internal unit of measure.  The unit used to measure the material.  */  
   IUM:string,
      /**   Expected purchasing lead time (in days).  This field is only valid if JobMtl.BuyIt = yes.  This can be used to calculate a suggested "Order By Date" based off the Required Date field.
When scheduling the job, purchased material can push a schedule out if the material lead time prevents the material from being available when the operation could start.  */  
   LeadTime:number,
      /**   A material record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job.  The related operation is also used to calculate the JobMtl.ReqDate based on the operations scheduled start date and materials lead time.  */  
   RelatedOperation:number,
      /**  The material burden rate for this Job Material.  */  
   MtlBurRate:number,
      /**  Estimated Material Burden Unit Cost of the material.  Defaults from the Part table if valid PartNum.  */  
   EstMtlBurUnitCost:number,
      /**  Estimated Unit Cost of the material.  Defaults from the Part table if valid PartNum.  */  
   EstUnitCost:number,
      /**  This quantity is a summary of all Issue Transactions.  For FS this was FSCallMt.ActQty  */  
   IssuedQty:number,
      /**  Total cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  FS - was UnitCost in FSCallMt  */  
   TotalCost:number,
      /**  Total Material Burden cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  */  
   MtlBurCost:number,
      /**  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  */  
   ReqDate:string,
      /**  The warehouse that the material is allocated against.  */  
   WarehouseCode:string,
      /**  Part number for salvageable scrap from this material record.  An optional field.  This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via salvage receipt process.  */  
   SalvagePartNum:string,
      /**  Description of Salvageable material.  Use Part.Description for a default.  */  
   SalvageDescription:string,
      /**  A factor that multiplied by the JobMtl.RequiredQty results in the expected total salvage quantity.  */  
   SalvageQtyPer:number,
      /**  Default unit of measure for the Salvaged Part.  Default from the Part.IUM.  */  
   SalvageUM:string,
      /**  The salvage material burden rate for this Job Material.  */  
   SalvageMtlBurRate:number,
      /**  Estimated Salvage Unit Credit.  Use the appropriate cost from the Part master as a default.  */  
   SalvageUnitCredit:number,
      /**  Estimated Salvage Mtl burden Unit Credit.  Use the appropriate cost from the Part master as a default.  */  
   SalvageEstMtlBurUnitCredit:number,
      /**  This quantity is a summary of all transactions for receipt of salvage to inventory.  This is not directly maintainable.  */  
   SalvageQtyToDate:number,
      /**  Total salvage credit to date.  A summary of salvage receipt transactions.  */  
   SalvageCredit:number,
      /**  Total salvage Mtl Burden credit to date.  A summary of salvage receipt transactions.  */  
   SalvageMtlBurCredit:number,
      /**   Comments for manufacturing about this material record.  These comments are printed on manufacturing reports, such as the router.  For valid Parts use the Part.MfgComment as a default.
View as editor widget.  */  
   MfgComment:string,
      /**  Used to identify a default vendor.  Use the Part.VendorNum as a default.  This will be used as a default for purchasing and miscellaneous receipts.  This field is not directly maintainable, instead its assigned by having the user either entering the "VendorID" and then finding the VendorNum in the Vendor file or by selection list processing.  An optional field, but if entered must be valid.  */  
   VendorNum:number,
      /**  The Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default purchase point defined in the Vendor file.  */  
   PurPoint:string,
      /**  Indicates if this material is to be purchased for the Job.  If this is a non inventory part then this is "Yes" and cannot be changed.  If this is a valid Part then set it to "NO" but the user can override it. Material that is marked to be purchased (BuyIt = Yes) are NOT included in the PartWhse.AllocatedQty.  */  
   BuyIt:boolean,
      /**  FUTURE IMPLEMENTATION.  This logical relates to material that is flagged to be purchased (BuyIt = Yes).  When purchase orders are created for this job material requirement this flag is set to Yes indicating that a purchase order has been placed.  The idea would be to use this within purchasing to quickly see the "direct job requirements" where no purchase orders have been placed.  */  
   Ordered:boolean,
      /**   Comments for purchasing about this material record on this job. These comments will be used as defaults to the PODetail.Comment field when the purchase order references this JobMtl record.
View as editor widget.  */  
   PurComment:string,
      /**   Indicates if this material will be backflushed.
Note: this field is defaulted from Part.BackFlush
Backflushing occurs via the write trigger on LaborDtl.  The basic idea is to issue material based on the labor quantities reported. The formula for the issue quantity is: (JobMtl.RequiredQty/JobOper.RunQty) * (LaborDtl.LaborQty + LaborDtl.SrapQty).  */  
   BackFlush:boolean,
      /**  Estimated Scrap.  */  
   EstScrap:number,
      /**  Qualifies the EstScrapQty entry as being a fixed quantity or a percentage of required quantity.  */  
   EstScrapType:string,
      /**  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  */  
   FixedQty:boolean,
      /**  Characters used on the drawing to show where material is used.  */  
   FindNum:string,
      /**  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  Controls if an alert is to be sent when this JobMtl is completed.  */  
   SndAlrtCmpl:boolean,
      /**  Indicates if inspection is required when items are received to this JobMtl.  Inspection may also be enforced if the related PartClass, Vendor, PODetail have their "RcvInspectionReq" fields set to Yes.  */  
   RcvInspectionReq:boolean,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Indicates if this material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified.  */  
   Direct:boolean,
      /**  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  */  
   MaterialMtlCost:number,
      /**  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   MaterialLabCost:number,
      /**  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   MaterialSubCost:number,
      /**  Total Bur cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   MaterialBurCost:number,
      /**  Total salvage Mtl credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   SalvageMtlCredit:number,
      /**  Total salvage Lbr credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   SalvageLbrCredit:number,
      /**  Total salvage Burden credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   SalvageBurCredit:number,
      /**  Total salvage Subcontract credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   SalvageSubCredit:number,
      /**   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  */  
   APSAddResType:string,
      /**  The service call that this Material belongs to.  */  
   CallNum:number,
      /**  The Service Call Line that this material relates to.  */  
   CallLine:number,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  FS - Unit Price for the Material in base currency.  */  
   UnitPrice:number,
      /**  FS - Billable Unit Price for the Material in base currency.  */  
   BillableUnitPrice:number,
      /**  FS - Billable Price per unit for the material in customers currency.  */  
   DocBillableUnitPrice:number,
      /**  Problem reason code from the reason master table. type Service call.  */  
   ResReasonCode:string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each,"C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E".  */  
   PricePerCode:string,
      /**  Is this a billable material item.  */  
   Billable:boolean,
      /**  Holds the quantity of the item that has been shipped through misc.  shipments  */  
   ShippedQty:number,
      /**  FS - Unit Price for the Material in Customer currency.  */  
   DocUnitPrice:number,
      /**  The todate quantity that has been moved to the work centers input Warehouse/Bin.  This is NOT A balance.  It is a todate value. It is not reduced as it is consumed. Used in calculation of "Outstanding" material in the Request Material program (ame30-dg.w). Only updated if the Advanced Material Mgmt module is installed and only by transactions which "move" the material in/out of the staging area(Issues,Returns).  */  
   QtyStagedToDate:number,
      /**  This material was added after initial setup of the job  */  
   AddedMtl:boolean,
      /**  This indicates that this JobMtl record is for a Misc charge related to this job/assembly.  */  
   MiscCharge:boolean,
      /**  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.   It must be a AP Misc. charge.  */  
   MiscCode:string,
      /**  The Miscellaneous Charge Code for Service Call billing. This must be valid in the MiscChrg master file.   It must be a AR Misc. charge.  */  
   SCMiscCode:string,
      /**  A flag to indicate that this job material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  */  
   RFQNeeded:boolean,
      /**  The number of vendor quotes that are required for this job material.  Can be zero if RFQ(s) are not required.  */  
   RFQVendQuotes:number,
      /**  RFQ number that the item is linked to.  */  
   RFQNum:number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   RFQLine:number,
      /**   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  */  
   RFQStat:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  Global RFQ flag.  Used in Consolidated Purchasing.  */  
   GlbRFQ:boolean,
      /**  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  */  
   WhseAllocFlag:boolean,
      /**  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  */  
   WIReqDate:string,
      /**  Reporting currency value of this field  */  
   Rpt1BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
      /**   Required Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the JobMtl.RequiredQty which is in the UOM of the requirement to the JobMtl.BaseUOM which is the UOM of the Part and it's unit costs.
This quantity multiplied by the JobMtl.EstMtlUnitCost is used to update the total estimated costs found in JobAsmbl.TLEMaterialCost  */  
   BaseRequiredQty:number,
      /**   Unit of Measure of the JobMtl.BaseRequiredQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as JobMtl.IUM  */  
   BaseUOM:string,
      /**  Material Weight defaulted from Part Master.  */  
   Weight:number,
      /**  Material Weight UOM defaulted from Part Master.  */  
   WeightUOM:string,
      /**  Required number of designators  */  
   ReqRefDes:number,
      /**  Base Part Number. Used in the configurator to identify the configurator part Number.  */  
   BasePartNum:string,
      /**  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  */  
   BaseRevisionNum:string,
      /**  Indicates if the job material is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   SelectForPicking:boolean,
      /**  The job pick "Staging" warehouse for the job material.  Defaults from the system default warehouse (PlantConfCtrl.DefJobPickWhse).  */  
   StagingWarehouseCode:string,
      /**  The job pick "Staging" bin for the job material.  Defaults from the system default bin (PlantConfCtrl.DefJobPickBin).  */  
   StagingBinNum:string,
      /**   A non blank character indicates that the release could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  */  
   PickError:string,
      /**   Estimated Material Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   EstMtlUnitCost:number,
      /**   Estimated Labor Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   EstLbrUnitCost:number,
      /**   Estimated Burden Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   EstBurUnitCost:number,
      /**   Estimated Subcontract Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   EstSubUnitCost:number,
      /**   Estimated Salvage Material Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   SalvageEstMtlUnitCredit:number,
      /**   Estimated Salvage Labor Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   SalvageEstLbrUnitCredit:number,
      /**   Estimated Salvage Burden Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   SalvageEstBurUnitCredit:number,
      /**   Estimated Salvage Subcontract Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   SalvageEstSubUnitCredit:number,
      /**  The material quantity that has been loaned out to another job.  */  
   LoanedQty:number,
      /**  The material quantity that has been borrowed from another job.  */  
   BorrowedQty:number,
      /**  flag used to designate if the serial numbers from the job material/subassembly can be reassigned as the serial number of the parent assembly (top assembly or n deep subassembly) being reworked using a job.  */  
   ReassignSNAsm:boolean,
      /**  GeneralPlanInfo  */  
   GeneralPlanInfo:string,
      /**  EstStdDescription  */  
   EstStdDescription:string,
      /**  PricingUOM  */  
   PricingUOM:string,
      /**  RemovedFromPlan  */  
   RemovedFromPlan:boolean,
      /**  IsPOCostingMaintained  */  
   IsPOCostingMaintained:boolean,
      /**  EstStdType  */  
   EstStdType:number,
      /**  POCostingFactor  */  
   POCostingFactor:number,
      /**  PlannedQtyPerUnit  */  
   PlannedQtyPerUnit:number,
      /**  POCostingDirection  */  
   POCostingDirection:number,
      /**  POCostingUnitVal  */  
   POCostingUnitVal:number,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   OrigStructTag:string,
      /**  By storing the original Group Sequence of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   OrigGroupSeq:number,
      /**  ShowStatusIcon  */  
   ShowStatusIcon:string,
      /**  ContractID  */  
   ContractID:string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the Planning Contract.  */  
   LinkToContract:boolean,
      /**  Stores the lot number of the material in the Staging Warehouse/Bin.  */  
   StagingLotNum:string,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
      /**  Controls if this material record is viewable in Location Management or the web.  */  
   LocationView:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   SalvageAttributeSetID:number,
      /**  Salvage planning number of pieces for this attribute set.  */  
   SalvagePlanningNumberOfPieces:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   SalvagePlanningAttributeSetID:number,
      /**  The identification of related StageNo.  */  
   RelatedStage:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   SalvageRevisionNum:string,
      /**  Indicates if the job material should be added or removed from the fulfillment queue.  */  
   PartAllocQueueAction:string,
      /**  This flag indicates if the job material is ready to be fulfilled.  */  
   ReadyToFulfill:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcJobOpDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Job Number.  Associates the record back to the JobHead.  */  
   JobNum:string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  Assigned by the system.  */  
   AssemblySeq:number,
      /**  A sequence number which uniquely identifies the JobOper record within the JobAsmbl.   System assigned.  */  
   OprSeq:number,
      /**  Uniquely identifies an OpDtl.  System assigned.  */  
   OpDtlSeq:number,
      /**  Identifies which part of the production, setup or production, the resource is required for.   Valid values are "S", indicating the resource is RequiredFor the Setup phase of this operation, "P" for Production phase, or "B" meaning Both setup and production phase.  */  
   SetupOrProd:string,
      /**  The user can select the capability the operation is to perform.  The system will select the resource.  */  
   CapabilityID:string,
      /**  The user can select a Resource Group for the operation to be performed on.  The system will select the actual resource.  */  
   ResourceGrpID:string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource for this operation to be performed on.  If a resource was not explicitly assigned this field is blank.  */  
   ResourceID:string,
      /**  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  */  
   ConcurrentCapacity:number,
      /**  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  */  
   DailyProdRate:number,
      /**  This is the number of resources the operation can run on.  If multiple resources can perform the required Capability, then up to this many will be employed.  This determines the number of setups the system will allow for the operation.  However, the number of setups cannot exceed the number of operations.  The idea being that once a part is on a machine you will complete the operation on that resource.  */  
   NumResources:number,
      /**  Total estimated set up hours.  Calculated as EstSetHoursPerMch * Machines.  It is set to zero if operation qty is zero.  This is maintained via the JobOper write trigger.  */  
   EstSetHours:number,
      /**   The estimated Production run hours for internal operations (JobOper.Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to  recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (JobOper.RunQty / Std).
If StdFormat = "PM" then (JobOper.RunQty / Std ) / 60.
If StdFormat = "OH" then (JobOper.RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((JobOper.RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (JobOPer.RunQty/Basis) X Std.
If StdFormat = "MP" then ((JobOper.RunQty/Basis) X Std) / 60.  */  
   EstProdHours:number,
      /**   The production standard for the operation.  It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours.  A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  */  
   ProdStandard:number,
      /**   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  */  
   StdFormat:string,
      /**   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   StdBasis:string,
      /**  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  */  
   OpsPerPart:number,
      /**  Labor rate used for estimated production labor costs. Default from the OpMasDtl.ProdLabRate.  */  
   ProdLabRate:number,
      /**  Labor rate for estimated setup labor costs. Default from the OpMaster.SetupLabRate.  */  
   SetupLabRate:number,
      /**  The burden rate to be used for the production time on this operation. (EstProdHrs X ProdBurRate). Default from the WrkCenter.ProdBurRate.  */  
   ProdBurRate:number,
      /**  The burden rate to be used for the Setup time on this operation. (EstSetHours X ProdBurRate). Default from the WrkCenter.SetupBurRate.  */  
   SetupBurRate:number,
      /**  A flag indicating if the production is complete for this operation. It is updated via Labor Entry.  */  
   ProdComplete:boolean,
      /**  Flag that indicates if Setup is complete on this operation. This flag is only used when the operation has EstSetupHours > 0.00.  */  
   SetupComplete:boolean,
      /**  Total Actual Production Hours. A summary of non-setup LaborDtl.BurdenHrs. This includes REWORK hours.  This is maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActReworkHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H").  */  
   ActProdHours:number,
      /**  Total Actual Production Rework  Hours. A summary of rework labor transactions (LaborDtl.BurdenHrs) where LaborDtl.LaborType = "P" and Rework = Yes. This number is also included as part of the JobOPer.ActProdHours.  Maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActProdHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H"). (See the lib/inopload.i code for load remaining logic)  */  
   ActProdRwkHours:number,
      /**  Actual setup hours.  A summary of setup (LaborDtl.LaborType = S) labor transactions hours (LaborDtl.Burden). Actual Setup hours reduce the shop load if the system is configured to remove load based on hours (JCSyst.RemoveLoad = "H").  */  
   ActSetupHours:number,
      /**  Total Actual Setup Rework  Hours. A summary of rework labor transactions (LaborDtl.BurdenHrs) where LaborDtl.LaborType = "S" and Rework = Yes. This number is also included as part of the JobOPer.ActSetupHours.  Maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActSetHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H"). (See the lib/inopload.i code for load remaining logic)  */  
   ActSetupRwkHours:number,
      /**  Setup function percent complete.  Maintained via labor entry.  */  
   SetupPctComplete:number,
      /**  Total Burden cost to date. This is update via the LaborDtl\Write.p trigger procedure. It includes ALL burden costs (Setup, Production and Rework)  */  
   ActBurCost:number,
      /**   Total of ALL labor costs to date. This includes Setup, Production and Rework. Updated via the LaborDtl.Write.p trigger.
The Total Cost, updated via the receipt process.  */  
   ActLabCost:number,
      /**  Total Rework Burden cost todate. This value is also included in the ActBurCost total. It includes both setup & production rework. Updated via LaborDtl\Write.P trigger.  */  
   ReworkBurCost:number,
      /**  Total Rework Labor cost to date. This value is also included in the ActLabCost field. This includes both Setup and Production. Updated via the LaborDtl\Write.p trigger.  */  
   ReworkLabCost:number,
      /**  Resource Lock.  If the user explicitly selected a Resource for the JobOpDtl, when they accept the scheduling changes, the WISchedResource will be stored as the explicit Resource.  Else the WISchedResource will become the SchedResource and the WISchedResourceGrp will become the ResourceGroup.  */  
   ResourceLock:boolean,
      /**  System maintained.  Date the JobOpDtl record was added to the database.  */  
   SysCreateDate:string,
      /**  Time in seconds since midnight that the system created the record.  */  
   SysCreateTime:number,
      /**  Description is initially created when the JobOpDtl is created.   If the JobOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   OpDtlDesc:string,
      /**   The estimated set up hours per machine.
Default from OpStd.SetupHours.  Used to calculate JobOper.EstSetupHours.  */  
   EstSetHoursPerMch:number,
      /**  If yes then the user has overridden the rates that were on the  record when it was inititally created.  The initial rates came from the master files.  */  
   OverrideRates:boolean,
      /**  Duplicated from JobOper.SetupCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  */  
   ProdCrewSize:number,
      /**  Duplicated from JobOper.SetupCrewSize. Its the number of people it physically takes to setup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   SetUpCrewSize:number,
      /**  RemovedFromPlan  */  
   RemovedFromPlan:boolean,
      /**  IsPrimaryProd  */  
   IsPrimaryProd:boolean,
      /**  IsPrimarySetup  */  
   IsPrimarySetup:boolean,
      /**  AutoSystemAdded  */  
   AutoSystemAdded:boolean,
      /**  MobileAllocatedResource  */  
   MobileAllocatedResource:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   QtyPerCycle:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcJobOperRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if  "Job"  is complete.  This is a mirror image of JobHead.Complete.  Not directly maintainable.  When the Job is completed, then all JobOper records are also marked.  This is used to make database access to open operation records more efficient.  */  
   JobComplete:boolean,
      /**   Indicates if this operation is completed. This is normally set to complete via labor entry transactions.   Not maintainable by Job Entry. It can't be reset to "No" if the JobHead.Complete = Yes.
Labor entry setting logic is: If SetUpComplete = Yes and  EstProdHours = 0 or ProdComplete = Yes and EstSetHours = 0 or both ProdComplete = Yes and SetupComplete = Yes  then OpComplete = Yes.
This field is also set by PO receipt entry "issue complete" for subcontract operations.  */  
   OpComplete:boolean,
      /**  Job Number  */  
   JobNum:string,
      /**  Assembly Sequence # that this Operation is associated with.  */  
   AssemblySeq:number,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   OprSeq:number,
      /**  Operation Master Code - Links the JobOper  record with a OpMaster record.  Default is given from WrkCenter.OpCode.  Must be valid in the OpMaster file.  */  
   OpCode:string,
      /**   The Operation standard ID.  This links the JobOper to the OpStd master file.  This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.
Valid for "inside operations" only.  */  
   OpStdID:string,
      /**  Total estimated set up hours.  Calculated as EstSetHoursPerMch * Machines.  It is set to zero if operation qty is zero.  This is maintained via the JobOper write trigger.  */  
   EstSetHours:number,
      /**   The estimated Production run hours for internal operations (JobOper.Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to  recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (JobOper.RunQty / Std).
If StdFormat = "PM" then (JobOper.RunQty / Std ) / 60.
If StdFormat = "OH" then (JobOper.RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((JobOper.RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (JobOPer.RunQty/Basis) X Std.
If StdFormat = "MP" then ((JobOper.RunQty/Basis) X Std) / 60.  */  
   EstProdHours:number,
      /**   The production standard for the operation.  It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours.  A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  */  
   ProdStandard:number,
      /**   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  */  
   StdFormat:string,
      /**   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   StdBasis:string,
      /**  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  */  
   OpsPerPart:number,
      /**  Production Quantity per one of the Parent Item.  */  
   QtyPer:number,
      /**  Scheduled queue start date. Not directly maintainable, updated via the scheduling process.  */  
   QueStartDate:string,
      /**  Scheduled queue start hour offset from the beginning of the work day.  This field is established by scheduling.  */  
   QueStartHour:number,
      /**  Scheduled production start date. Not directly maintainable, updated via the scheduling process.  */  
   StartDate:string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  */  
   StartHour:number,
      /**  Scheduled production due date. Not directly maintainable, updated via the scheduling process.  */  
   DueDate:string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  */  
   DueHour:number,
      /**  Scheduled move due date. Not directly maintainable, updated via the scheduling process.  */  
   MoveDueDate:string,
      /**  Scheduled move due hour offset from the beginning of the work day.  This field is established by scheduling.  */  
   MoveDueHour:number,
      /**  Labor rate used for estimated production labor costs. Default from the OpMaster.ProdLabRate.  */  
   ProdLabRate:number,
      /**  Labor rate for estimated setup labor costs. Default from the OpMaster.SetupLabRate.  */  
   SetupLabRate:number,
      /**  The burden rate to be used for the production time on this operation. (EstProdHrs X ProdBurRate). Default from the WrkCenter.ProdBurRate.  */  
   ProdBurRate:number,
      /**  The burden rate to be used for the Setup time on this operation. (EstSetHours X ProdBurRate). Default from the WrkCenter.SetupBurRate.  */  
   SetupBurRate:number,
      /**  This indicates if this is an "added operation". An added operation is one that was not planned on.  */  
   AddedOper:boolean,
      /**  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  */  
   Machines:number,
      /**  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to setup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   SetUpCrewSize:number,
      /**  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  */  
   ProdCrewSize:number,
      /**  A flag indicating if the production is complete for this operation. It is updated via Labor Entry.  */  
   ProdComplete:boolean,
      /**  Flag that indicates if Setup is complete on this operation. This flag is only used when the operation has EstSetupHours > 0.00.  */  
   SetupComplete:boolean,
      /**  Total Actual Production Hours. A summary of non-setup LaborDtl.BurdenHrs. This includes REWORK hours.  This is maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActReworkHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H").  */  
   ActProdHours:number,
      /**  Total Actual Production Rework  Hours. A summary of rework labor transactions (LaborDtl.BurdenHrs) where LaborDtl.LaborType = "P" and Rework = Yes. This number is also included as part of the JobOPer.ActProdHours.  Maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActProdHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H"). (See the lib/inopload.i code for load remaining logic)  */  
   ActProdRwkHours:number,
      /**  Actual setup hours.  A summary of setup (LaborDtl.LaborType = S) labor transactions hours (LaborDtl.Burden). Actual Setup hours reduce the shop load if the system is configured to remove load based on hours (JCSyst.RemoveLoad = "H").  */  
   ActSetupHours:number,
      /**  Total Actual Setup Rework  Hours. A summary of rework labor transactions (LaborDtl.BurdenHrs) where LaborDtl.LaborType = "S" and Rework = Yes. This number is also included as part of the JobOPer.ActSetupHours.  Maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActSetHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H"). (See the lib/inopload.i code for load remaining logic)  */  
   ActSetupRwkHours:number,
      /**   For Non Subcontract operations: A summary of labor transaction detail. (LaborDtl.LaborQty). Labor entry/collection maintains this field.  Only the LaborQty for transactions that are Production labor ( LaborType = P ) and Not rework (LaborDtl.Rework = No) are included in this summary.
This quantity is used to reduce shop load when the system is configured to reduce load based on quantity completed. (JCSyst.RemoveLoad = Q)
For Subcontract Operations this field is updated by the Purchased Receipt process. The detail records are in the PartTran file.  */  
   QtyCompleted:number,
      /**  Setup function percent complete.  Maintained via labor entry.  */  
   SetupPctComplete:number,
      /**  EstScrap =  a number representing either a scrap qty or a scrap percent depending on the value of EstScrapType field.  */  
   EstScrap:number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   EstScrapType:string,
      /**  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  */  
   SubContract:boolean,
      /**  Inventory UOM  */  
   IUM:string,
      /**  Estimated Unit Cost for the SubContract operation.  Defaults from the Part table if valid PartNum.  */  
   EstUnitCost:number,
      /**  Hours required is calculated as days * 8.  */  
   DaysOut:number,
      /**  The PartNum to be shipped to the subcontract. Default the JobHead.PartNum or JobAsmbl.PartNum depending on the JobMtl.AssemblySeq.  */  
   PartNum:string,
      /**  Description used only for subcontract operations  */  
   Description:string,
      /**  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  */  
   PurPoint:string,
      /**  Editor widget for Job operation comments.  */  
   CommentText:string,
      /**   Indicates the scheduling relationship between this and the preceding  operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  */  
   SchedRelation:string,
      /**   The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0.
This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  */  
   RunQty:number,
      /**   This field is blank or contains the UserID. When not blank it indicates that the operations schedule has been changed and is considered as being in a "What If" mode.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  */  
   WIName:string,
      /**  This is the What-If number of machines that this operation will run on at the same time.  Setup by and for scheduling from the Machines field.  */  
   WIMachines:number,
      /**  What-if Scheduled queue start date. Not directly maintainable, updated via the scheduling process.  */  
   WIQueStartDate:string,
      /**  What-if Scheduled queue start hour offset from the beginning of the work day.  This field is established by scheduling.  */  
   WIQueStartHour:number,
      /**  What if Scheduled production start date. Not directly maintainable, updated via the scheduling process.  */  
   WIStartDate:string,
      /**  This field is established by scheduling. It represents the What If "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  */  
   WIStartHour:number,
      /**  What If Scheduled production due date. Not directly maintainable, updated via the scheduling process.  */  
   WIDueDate:string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  */  
   WIDueHour:number,
      /**  What-If Scheduled move due date. Not directly maintainable, updated via the scheduling process.  */  
   WIMoveDueDate:string,
      /**  What-if Scheduled move due hour offset from the beginning of the work day.  This field is established by scheduling.  */  
   WIMoveDueHour:number,
      /**  The Number of Hours per machine per day that this operations "What If" schedule is based on.  This is for "Inbetween" days, not first or last days.  It is a copy of WrkCenter.HoursPerMachine field at the time of scheduling.  Used in logic of maintaining ShopLoad records.  */  
   WIHoursPerMachine:number,
      /**  Date at which the operations current outstanding "What-If" load starts at.  Updated by the JobOper write trigger. (See LoadDate)  */  
   WILoadDate:string,
      /**  "Hour offset from the beginning of the work day" for the operations outstanding "What-If"  load. Related to WILoadDate.  */  
   WILoadHour:number,
      /**  Total Burden cost to date. This is update via the LaborDtl\Write.p trigger procedure. It includes ALL burden costs (Setup, Production and Rework)  */  
   ActBurCost:number,
      /**   FOR NON-SUBCONTRACT OPERATIONS: Total of "ALL" labor costs to date. This includes Setup, Production and Rework. Updated via the LaborDtl.Write.p trigger.
FOR SUBCONTRACT OPERATIONS: The Total Cost, updated via the receipt process.  */  
   ActLabCost:number,
      /**  Total Rework Burden cost todate. This value is also included in the ActBurCost total. It includes both setup & production rework. Updated via LaborDtl\Write.P trigger.  */  
   ReworkBurCost:number,
      /**  Total Rework Labor cost to date. This value is also included in the ActLabCost field. This includes both Setup & Production. Updated via the LaborDtl\Write.p trigger.  */  
   ReworkLabCost:number,
      /**   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...).
Defaulted from VendPart.MiscAmt. This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  */  
   MiscAmt:number,
      /**  The Number of Hours per machine per day that this operations "actual" schedule is based on.  This is for "Inbetween" days, not first or last days.  It is a copy of WrkCenter.HoursPerMachine field at the time of scheduling.  Used in logic of maintaining the ShopLoad records.  */  
   HoursPerMachine:number,
      /**   Date at which the operations current outstanding load starts at.
Ex: Op schedule is 2/1/97 - 2/10/97, initially LoadDate = 2/1/97. As load is relieved through labor processing the LoadDate moves forward accordingly. When 1/2 completed the LoadDate would be 2/5/97. This field is primarily used by the Scheduling Board to calculate the graphical image of outstanding load.  Updated by the JobOper write trigger.  */  
   LoadDate:string,
      /**  "Hour offset from the beginning of the work day" for the operations outstanding load. Related to LoadDate.  */  
   LoadHour:number,
      /**  Internally used field to prevent redundant read of JobOper during execution of "Reloader" program. (See WrkCenter.ReloadNum)  */  
   ReloadNum:number,
      /**  Controls if an alert is to be sent when this JobOper is completed.  */  
   SndAlrtCmpl:boolean,
      /**  Indicates if  Inspection is required when items are received to this JobOper (subcontract only). Inspection may also be enforced if the related PartClass, Vendor, PODetail have their "RcvInspectionReq" fields set to Yes.  */  
   RcvInspectionReq:boolean,
      /**  Identical to JobHead.JobEngineered.  ShopLoad capacity is only allocated to Jobs where JobEngineered = YES.  */  
   JobEngineered:boolean,
      /**   The estimated set up hours per machine.
Default from OpStd.SetupHours.  Used to calculate JobOper.EstSetupHours.  */  
   EstSetHoursPerMch:number,
      /**   Part Revision number.
Pertains to subcontracting operations only.   An optional field.   Related JobAsmbl.RevisionNum is used as the default.  */  
   RevisionNum:string,
      /**  Currently not used. Prep for future development.  */  
   AutoReceiptDate:string,
      /**  The labor date of the last labor transaction that was posted to this operation.  Used by the JobOper write trigger Auto Receieve logic.  */  
   LastLaborDate:string,
      /**  The service call that this operation belongs to.  */  
   CallNum:number,
      /**  The Service Call Line that this operation relates to.  */  
   CallLine:number,
      /**  Labor rate used for  time on an operation.  Time per hour per technician. in base currency.  */  
   LaborRate:number,
      /**  Billable Labor rate used for  time on a service.  Time per hour per technician. in base currency. This field considers the percentage coverage of a warranty or contract.  */  
   BillableLaborRate:number,
      /**  Labor rate used for  time on a service.  Time per hour per technician. In Customer currency. Does not consider warranty or contract  */  
   DocLaborRate:number,
      /**  Billable Labor rate used for  time on a service.  Time per hour per technician. In Customer currency. considers warranty or contract  */  
   DocBillableLaborRate:number,
      /**  FS - Is this a billable operation.  */  
   Billable:boolean,
      /**  FS - Unit Price for the subcontract in base currency.  */  
   UnitPrice:number,
      /**  FS - Billable Unit Price for the subcontract in base currency.  */  
   BillableUnitPrice:number,
      /**  FS - Billable Price per unit for the subcontract in customers currency.  */  
   DocBillableUnitPrice:number,
      /**  FS - Unit Price for the for the Subcontract in Customer currency.  */  
   DocUnitPrice:number,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  */  
   LaborEntryMethod:string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each,"C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E".  */  
   PricePerCode:string,
      /**  The quantity requested for first article inspection.  */  
   FAQty:number,
      /**  The "to date" quantity that has been moved to the input Warehouse/Bin of the subsequent operations ResourceGroup/Resource input Warehouse/Bin.  This is NOT A balance.  It is a "to date" value.  It is not reduced as it is consumed.  Used in calculation of "Outstanding" WIP in the Request Material/WIP program (ame30-dg.w).  Only updated if the Advanced Material Mgmt module is installed and only by transactions which "move" the WIP material in/out of the staging area (Issues, Returns).  */  
   QtyStagedToDate:number,
      /**  A flag to indicate that this job operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  */  
   RFQNeeded:boolean,
      /**  The number of vendor quotes that are required for this job subcontract operation.  Can be zero if RFQ(s) are not required.  */  
   RFQVendQuotes:number,
      /**  RFQ number that the item is linked to.  */  
   RFQNum:number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   RFQLine:number,
      /**   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  */  
   RFQStat:string,
      /**  Used to group operation to save on setups.  */  
   SetupGroup:string,
      /**  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  */  
   RestoreFlag:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**   Identifies the primary JobOpDtl to be used for setup.  The setup time for the operation is determined on the JobOpDtl.
If <> 0, must identify a valid JobOpDtl.  The JobOpDtl needs to have a RequiredFor = S or B.  */  
   PrimarySetupOpDtl:number,
      /**   Identifies the primary JobOpDtl to be used for production.  The production run time for the operation is determined on the JobOpDtl.
If <> 0, must identify a valid JobOpDtl.  The JobOpDtl needs to have a RequiredFor = P or B.  */  
   PrimaryProdOpDtl:number,
      /**  Operation Description.  */  
   OpDesc:string,
      /**  Kit Date. Not directly maintanable. Updated via the scheduling process.  */  
   KitDate:string,
      /**  Global RFQ flag.  Used in Consolidated Purchasing.  */  
   GlbRFQ:boolean,
      /**  Booked Unit Cost  */  
   BookedUnitCost:number,
      /**   Initially defaulted to false. This flag is set to true at the time JobOper.ProdComplete is set to true if JobHead.ProductionYield = true and OpMaster. PrdYldRecalcExpected = true and the actual completed qty for the operation vs. the expected completion qty is out of variance based on the under percentage set in OpMaster. This flag is used by the production yield recalculation logic to determine if recalculation is required for a job.
This field is maintained by the system only.  */  
   RecalcExpProdYld:boolean,
      /**  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   UserMapData:string,
      /**  When true this would signify that this operation was rough cut scheduled - meaning the operation would have start and end dates but no supporting resourcetimeused or shopload records.  */  
   RoughCutSched:boolean,
      /**  Scheduling Comments  */  
   SchedComment:string,
      /**  Reporting currency value of this field  */  
   Rpt1BillableLaborRate:number,
      /**  Reporting currency value of this field  */  
   Rpt2BillableLaborRate:number,
      /**  Reporting currency value of this field  */  
   Rpt3BillableLaborRate:number,
      /**  Reporting currency value of this field  */  
   Rpt1BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1LaborRate:number,
      /**  Reporting currency value of this field  */  
   Rpt2LaborRate:number,
      /**  Reporting currency value of this field  */  
   Rpt3LaborRate:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
      /**  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  */  
   SNRequiredOpr:boolean,
      /**  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  */  
   SNRequiredSubConShip:boolean,
      /**  Operation Weight defaulted from Part Master.  */  
   Weight:number,
      /**  Operation Weight UOM defaulted from Part Master.  */  
   WeightUOM:string,
      /**   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  */  
   SendAheadType:string,
      /**   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  */  
   SendAheadOffset:number,
      /**  Delimited list of PrjRoleCd codes that are allowed for this operation.  */  
   PrjRoleList:string,
      /**  Scheduled tear down start date. The start date would be the production end date.  */  
   TearDwnEndDate:string,
      /**  Scheduled tear down due hour offset from the end of the prodution time.  This field is established by scheduling.  */  
   TearDwnEndHour:number,
      /**  Scheduled tear down start date. The start date would be the production end date.  */  
   WITearDwnEndDate:string,
      /**  Scheduled tear down due hour offset from the end of the prodution time.  This field is established by scheduling.  */  
   WITearDwnEndHour:number,
   UseAllRoles:boolean,
      /**  The PartNum for the asset. This should be disabled for a service call job, in which case the asset information would be transferred from the service call line when an operation is created for the job.  */  
   AssetPartNum:string,
      /**  Serial number of the asset.  */  
   SerialNumber:string,
      /**  ActualStartDate  */  
   ActualStartDate:string,
      /**  ActualStartHour  */  
   ActualStartHour:number,
      /**  ActualEndDate  */  
   ActualEndDate:string,
      /**  ActualEndHour  */  
   ActualEndHour:number,
      /**  FSJobStatus  */  
   FSJobStatus:number,
      /**  Instructions  */  
   Instructions:string,
      /**  ProdUOM  */  
   ProdUOM:string,
      /**  GeneralPlanInfo  */  
   GeneralPlanInfo:string,
      /**  EstStdDescription  */  
   EstStdDescription:string,
      /**  JDFOpCompleted  */  
   JDFOpCompleted:boolean,
      /**  RemovedfromPlan  */  
   RemovedfromPlan:boolean,
      /**  EstStdType  */  
   EstStdType:number,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  PctReg  */  
   PctReg:number,
      /**  SetupMaterial  */  
   SetupMaterial:number,
      /**  MaterialColorRating  */  
   MaterialColorRating:number,
      /**  MiscInfo1  */  
   MiscInfo1:string,
      /**  MiscInfo2  */  
   MiscInfo2:string,
      /**  SetupURL  */  
   SetupURL:string,
      /**  ExpPctUp  */  
   ExpPctUp:number,
      /**  ExpCycTm  */  
   ExpCycTm:number,
      /**  ExpGood  */  
   ExpGood:number,
      /**  NonProdLimit  */  
   NonProdLimit:number,
      /**  AutoSpcEnable  */  
   AutoSpcEnable:boolean,
      /**  AutoSpcPeriod  */  
   AutoSpcPeriod:number,
      /**  PartQualEnable  */  
   PartQualEnable:boolean,
      /**  AutoSpcSubgroup  */  
   AutoSpcSubgroup:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MobileOperation  */  
   MobileOperation:boolean,
      /**  ReWork  */  
   ReWork:boolean,
      /**  RequestMove  */  
   RequestMove:boolean,
      /**  ContractID  */  
   ContractID:string,
      /**  PrinterID  */  
   PrinterID:string,
      /**  LastPrintedDate  */  
   LastPrintedDate:string,
      /**  LastPCIDPrinted  */  
   LastPCIDPrinted:string,
      /**  CurrentPkgCode  */  
   CurrentPkgCode:string,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   QtyPerCycle:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  The identification of related StageNo.  */  
   StageNumber:string,
      /**  TemplateID  */  
   TemplateID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcKitCompResultRow{
      /**  Company  */  
   Company:string,
   HasRuleSet:boolean,
   IsKept:boolean,
   ParentRuleTag:string,
      /**  Part Number  */  
   PartNum:string,
      /**  Quote Line  */  
   QuoteLine:number,
      /**  Quote Number  */  
   QuoteNum:number,
      /**  Revision Number  */  
   RevisionNum:string,
   RuleTag:string,
      /**  Test Type  */  
   TestType:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcMtlResultRow{
   Company:string,
   TestType:string,
   AssemblySeq:number,
   ParentAsmSeq:number,
   OprSeq:number,
   MtlSeq:number,
   MtlType:string,
   PartNum:string,
   RuleTag:string,
   Description:string,
   ParentRuleTag:string,
   AsmPartNum:string,
   HasRuleSet:boolean,
   IsKept:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcOpDtlResultRow{
   Company:string,
   TestType:string,
   AssemblySeq:number,
   OprSeq:number,
   OpDtlSeq:number,
   CapabilityID:string,
   Description:string,
   ResourceGrpID:string,
   ResourceID:string,
   RuleTag:string,
   ParentRuleTag:string,
   AsmPartNum:string,
   HasRuleSet:boolean,
   IsKept:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcOprResultRow{
   Company:string,
   TestType:string,
   AssemblySeq:number,
   OprSeq:number,
   OpCode:string,
   OpDesc:string,
   RuleTag:string,
   ParentRuleTag:string,
   AsmPartNum:string,
   HasRuleSet:boolean,
   IsKept:boolean,
   SubContract:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcQuoteAsmRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the last QuoteDtl record for the Quote and the adding 1 to it.  */  
   QuoteLine:number,
      /**  An integer that uniquely identifies the Assembly record within the Quote/Line.  Assigned by the system one greater than the last QuoteAsm record on file for the given quote/line.  */  
   AssemblySeq:number,
      /**  Part number for this assembly.  Cannot be blank.  It does not have to be valid in the Part master file.  */  
   PartNum:string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description if valid Part record.  */  
   Description:string,
      /**  The revision number for the assembly. An optional field. Use the Part.RevisionNum as a default.  */  
   RevisionNum:string,
      /**  The production Quantity required for this assembly per one of it's Parent Part.  */  
   QtyPer:number,
      /**  The unit of measure for this assembly. Use the Part.IUM as a default.  */  
   IUM:string,
      /**  Indicates if this assembly material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse  */  
   Direct:boolean,
      /**  Sequence number of the Parent Assembly.  0 means no parent assembly (i.e. this is the final assembly).  Cannot be negative like the other pointers because this one shows up in a browser.  */  
   Parent:number,
      /**   The  sequence number of the prior assembly that is on the same level as this assembly.  This  is known as a PriorPeer assembly.  This is automatically maintained by the maintenance programs.
The logic is to find the last assembly (i.e. where the Parent is the same and the NextPeer is -1). Then NextPeer of that assembly gets updated with this assembly's sequence number and this assembly gets its PriorPeer field updated with the sequence number from that assembly which was found.  -1 means that there is no prior assembly (i.e. it is the first assembly of its peers).  */  
   PriorPeer:number,
      /**   The sequence number of the Next Assembly on the same level as this assembly.  This is known as a NextPeer assembly.  Automatically maintained by the maintenance programs.
The logic is to find the first assembly (i.e. where the Parent is the same and the PriorPeer is -1).  Then the PriorPeer of that assembly is updated with this assembly's sequence number and then this assembly's NextPeer gets updated with the sequence number from the assembly that was found.   -1 means that the assembly is the last assembly of its peers.  */  
   NextPeer:number,
      /**  Seq # of this assembly's very first subassembly. This is known as the Child assembly. Automatically maintained by the maintenance programs. The logic is to find the Parent assembly record and if its child is -1, update it with this assembly's seq #.  */  
   Child:number,
      /**  Optional field for Engineering Drawing Number. Defaulted from BomHead.DrawNum during methods pull functions.  */  
   DrawNum:string,
      /**  Editor widget for Job Assembly comments.  */  
   CommentText:string,
      /**  An internally system assigned integer which is used as part of an index to organize the QuoteAsm records into a Bill of Material fashion sequence.  */  
   BomSequence:number,
      /**  An internally system assigned integer which represents the "Level of Indention" of the QuoteAsm in reference to the Bill of Material structure.  */  
   BomLevel:number,
      /**   A system maintained field. This is how many of the assemblies are required to produce ONE of the END ITEM.  This is a calculated field.  Calculated as the
 ( Parents RequiredQty  X QtyPer).
This field needs to be refreshed whenever a change is made to the production quantity in any of its parents or when its QtyPer. The refresh may also occur if the structure of the assemblies is changed.  */  
   RequiredQty:number,
      /**  Indicates if this quote assembly is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  */  
   Template:boolean,
      /**   The operation number (Quote.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   AutoRecOpr:number,
      /**  FUTURE IMPLEMENTATION - Characters used on the parent assembly drawing to show where assembly  is used.  */  
   FindNum:string,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   FinalOpr:number,
      /**  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  */  
   WIStartDate:string,
      /**  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  */  
   WIStartHour:number,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIDueDate:string,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIDueHour:number,
      /**   An assembly record can be related to a specific operation.  This field contains the QuoteOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this assembly is required at the very beginning of the production job.  The related operation is also used to calculate scheduled start date.  */  
   RelatedOperation:number,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  Estimated Scrap (fallout) that is expected to occur for this material. The scrap increase the Required quantity. Example; need 1000 pieces scrap of 10 % will show a required quantity of 1100.  */  
   EstScrap:number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   EstScrapType:string,
   OrigMtlSeq:number,
   OrigRuleTag:string,
      /**  Validate Reference Designators.  */  
   ValRefDes:boolean,
      /**  The part number used to identify the configured part number initially entered on the assembly.  */  
   BasePartNum:string,
      /**  The revision number used to identify the configured part/revision number initially entered on the material.  */  
   BaseRevisionNum:string,
      /**  Required number of designators  */  
   ReqRefDes:number,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   OrigStructTag:string,
      /**  LinkToContract  */  
   LinkToContract:boolean,
      /**  ContractID  */  
   ContractID:string,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   KBConfigProdID:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcQuoteDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   QuoteLine:number,
      /**  Indicates if this Quote item has been ordered. This is not directly set by the user. It is updated via Order Entry when the QuoteDtl is referenced.  */  
   Ordered:boolean,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the QuoteDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  */  
   PartNum:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   RevisionNum:string,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the CustXPrt table.. The XPartNum can be blank, does not have to exist in the CustXPrt table.  THIS FIELD WILL BE USED TO PASS THE VALUE ALONG TO ORDER ENTRY.  */  
   XPartNum:string,
      /**  Contains comments about the detail line item. These will be printed on the Quote form.  */  
   QuoteComment:string,
      /**  A field to describe lead time. For example "Allow 4-5 weeks". This is printed on the Quote form.  */  
   LeadTime:string,
      /**  Indicates if this quote detail is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  */  
   Template:boolean,
      /**  Engineering Drawing Number. An optional field.  */  
   DrawNum:string,
      /**  Production Job comments. These will be copied to the JobHead.CommentText when the quote is pulled into a job during a get detail function.  It is also copied to the OrderDtl.PickListComment which may then be copied to JobHead.CommentText when linked.  */  
   JobComment:string,
      /**  An internally used flag field which indicates if Manufacturing Details exist for this quote line item. It is set to "Yes" if any QuoteOpr or QuoteMtl records exist for the quote line. This is controlled via write/delete triggers on the QuoteOpr and QuoteMtl files. Used by the "Get Detail" function in job entry so that only QuoteDtl record that MfgDetail = Yes are shown in the browser.  */  
   MfgDetail:boolean,
      /**  Indicates the Tax Category for this record. Defaults from the Part Master.  */  
   TaxCatID:string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   XRevisionNum:string,
      /**  Number that relates to the Customer master. Duplicated from QuoteHed.CustNum.  Used to allow efficient browsing of the QuoteDtl records for a specific customer.  */  
   CustNum:number,
      /**  Mirror image of QuoteHed.Quoted.  Duplicated to provide efficient browsing of QuoteDtl records.  */  
   Quoted:boolean,
      /**  Mirror image of QuoteHed.Expired.  Duplicated to provide efficient browsing of QuoteDtl records.  */  
   Expired:boolean,
      /**  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  */  
   WIStartDate:string,
      /**  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  */  
   WIStartHour:number,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIDueDate:string,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIDueHour:number,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   BasePartNum:string,
      /**  The quantity expected to be ordered. (In selling unit of measure)  */  
   SellingExpectedQty:number,
      /**  Unit of measure (how it is sold/issued) for the SellingExpectedQty.  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   SellingExpectedUM:string,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential for the quote line  */  
   ConfidencePct:number,
      /**  The date this line was last updated  */  
   LastUpdate:string,
      /**  The last User Is that updated this Quote  */  
   LastDcdUserID:string,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the QuoteHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  */  
   DiscountPercent:number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Discount:number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or QuoteQty fields are changed.  */  
   DocDiscount:number,
      /**  Expected revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  */  
   ExpectedRevenue:number,
      /**  Expected revenue for this line  in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  */  
   DocExpectedRevenue:number,
      /**  The requested ship date for the sales order  */  
   ReqShipDate:string,
      /**  The quantity to be used when a Sales order is created. (In selling unit of measure)  */  
   OrderQty:number,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingExpFactor:number,
      /**  Indicates that the order line made from this quote line should have multiple releases.  Informational only.  */  
   MultiRel:boolean,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   POLine:string,
      /**  A Code which uniquely identifies a SalesCat record.  */  
   SalesCatID:string,
      /**  Replicated from QuoteHed to easier sorting  */  
   TerritoryID:string,
      /**   Duplicated from QuoteHed for Query's.  Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  */  
   CurrentStage:string,
      /**  Indicates if the Quote line was created from opportunity entry "QUOTE" or from Order Entry "ORDER".  Used to determine if the Quote can be deleted when the Order gets deleted.  */  
   CreatedFrom:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  Holds the internal object id of pdm parts.  */  
   PDMObjID:string,
      /**  The date when the configuration was completed for the assembly.  */  
   LastConfigDate:string,
      /**  The system time when the configuration was completed for the assembly.  */  
   LastConfigTime:number,
      /**  The User ID of the last user to complete the configuration of the assembly.  */  
   LastConfigUserID:string,
      /**   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  */  
   ConfigUnitPrice:number,
      /**  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  */  
   ConfigBaseUnitPrice:number,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   BaseRevisionNum:string,
      /**  This is the Price List used to determine the starting base price.  */  
   PriceListCode:string,
      /**  This is the Price List used to determine the break % or amount.  */  
   BreakListCode:string,
      /**  The Expected Quantity (total qty of related quote lines) used to find price when quantity based discounting is applied.  */  
   PricingQty:number,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied.  */  
   ListPrice:number,
      /**   Same as List price except that this field contains the list price in
QuoteHed).  */  
   DocListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  */  
   OrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on QuoteHed).  */  
   DocOrdBasedPrice:number,
      /**  This is the Price Group ID used to price the quote line with.  */  
   PriceGroupCode:string,
      /**  Indicates if the user selected a price list different from the default.  */  
   OverridePriceList:boolean,
      /**  The Expected Order Value (total extended price of related quote lines) used to find order value break when value based discounting is applied.  */  
   PricingValue:number,
      /**  This is the unit price based on the expected quantity.  */  
   ExpUnitPrice:number,
      /**  This is the unit price (in customer currency) based on the expected quantity.  */  
   DocExpUnitPrice:number,
      /**   Indicates the pricing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the QuoteDtl.SellingExpectedQty by the appropriate "per" value and then multiply by expected unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E"  */  
   ExpPricePerCode:string,
      /**  An internally used integer assigned by the system to provide a unique key to the QuoteQty file.  This indicate what QuoteQty break should be used to get the related miscellaneous charges.  */  
   MiscQtyNum:number,
      /**  The Quote Line has been Engineered.  */  
   Engineer:boolean,
      /**  Indicates if Engineering details are complete/valid if the EngineerReq field is marked as Yes.  */  
   ReadyToQuote:boolean,
      /**  Indicates if component lines can be added, deleted and modified during quote entry.  This field is only relevant for quote lines which are kit parents.  */  
   KitAllowUpdate:boolean,
      /**  Indicates if the parent kitted part must be shipped complete or if kit components can be shipped in varying degrees of completeness.  This field is only relevant for quote lines which are kit parents.  If this field is set to "No", then KitPricing must be set to "C".  */  
   KitShipComplete:boolean,
      /**  Indicates if all components are to be backflushd when a kit parent item is shipped.  This field is only relevant for quote lines which are kit parents.  */  
   KitBackFlush:boolean,
      /**  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes",then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  */  
   KitPrintCompsPS:boolean,
      /**  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  */  
   KitPrintCompsInv:boolean,
      /**  Indicates how kits will be priced.  Values are: P = Parent Pricing (The price is otained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for quote lines which are kit parents.  */  
   KitPricing:string,
      /**  The quote line number of the parent kit item.  This is only relevent for quote lines which are kit parent or component lines.  If the KitParentLine equals the QuoteLine then this is a kit parent line.  */  
   KitParentLine:number,
      /**  Component quantity required to fulfill one kit parent.  This field is only relevant on a quote line which is a kit component.  */  
   KitQtyPer:number,
      /**  This field controls the order in which quote lines are displayed.  DisplaySeq is a decimal number where the whole number portion is used to sequence normal quote lines and the decimal portion is ued to sequence kit components under their associated kit parent.  */  
   DisplaySeq:number,
      /**  Project ID of linked project.  Must exist on the Project table. Can be blank.  */  
   ProjectID:string,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   SellingFactorDirection:string,
      /**  To indicate whether or not the line is make direct  */  
   MakeDirect:boolean,
      /**  Must exist on ProjPhase table if entered  */  
   PhaseID:string,
      /**   A character flag field used to differentiate between regular quote line, Sales Kit parent quote line and Sales Kit component quote line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  */  
   KitFlag:string,
      /**  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new quote line.  */  
   KitsLoaded:boolean,
      /**  Non-blank value prevents taxes from being calculated for this line item  */  
   TaxExempt:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   OwnershipStatus:string,
      /**  Reporting currency value of this field  */  
   Rpt1Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt2Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt3Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExpectedRevenue:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExpectedRevenue:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExpectedRevenue:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExpUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExpUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExpUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1ListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2ListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3ListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1OrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2OrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3OrdBasedPrice:number,
      /**  Extended Price for the quote line, rounded according to the Base currency Round rule  */  
   ExtPriceDtl:number,
      /**  Extended Price for the quote line in Customer currency, rounded according to the Doc currency Round rule  */  
   DocExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExtPriceDtl:number,
      /**  Reserved for future use  */  
   InDiscount:number,
      /**  Reserved for future use  */  
   DocInDiscount:number,
      /**  Reserved for future use  */  
   InExpectedRevenue:number,
      /**  Reserved for future use  */  
   DocInExpectedRevenue:number,
      /**  Reserved for future use  */  
   InListPrice:number,
      /**  Reserved for future use  */  
   DocInListPrice:number,
      /**  Reserved for future use  */  
   InOrdBasedPrice:number,
      /**  Reserved for future use  */  
   DocInOrdBasedPrice:number,
      /**  Reserved for future use  */  
   InExpUnitPrice:number,
      /**  Reserved for future use  */  
   DocInExpUnitPrice:number,
      /**  Reserved for future use  */  
   Rpt1InDiscount:number,
      /**  Reserved for future use  */  
   Rpt2InDiscount:number,
      /**  Reserved for future use  */  
   Rpt3InDiscount:number,
      /**  Reserved for future use  */  
   Rpt1InExpectedRevenue:number,
      /**  Reserved for future use  */  
   Rpt2InExpectedRevenue:number,
      /**  Reserved for future use  */  
   Rpt3InExpectedRevenue:number,
      /**  Reserved for future use  */  
   Rpt1InExpUnitPrice:number,
      /**  Reserved for future use  */  
   Rpt2InExpUnitPrice:number,
      /**  Reserved for future use  */  
   Rpt3InExpUnitPrice:number,
      /**  Reserved for future use  */  
   Rpt1InListPrice:number,
      /**  Reserved for future use  */  
   Rpt2InListPrice:number,
      /**  Reserved for future use  */  
   Rpt3InListPrice:number,
      /**  Reserved for future use  */  
   Rpt1InOrdBasedPrice:number,
      /**  Reserved for future use  */  
   Rpt2InOrdBasedPrice:number,
      /**  Reserved for future use  */  
   Rpt3InOrdBasedPrice:number,
      /**  Reserved for future use  */  
   InExtPriceDtl:number,
      /**  Reserved for future use  */  
   DocInExtPriceDtl:number,
      /**  Reserved for future use  */  
   Rpt1InExtPriceDtl:number,
      /**  Reserved for future use  */  
   Rpt2InExtPriceDtl:number,
      /**  Reserved for future use  */  
   Rpt3InExtPriceDtl:number,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (worst case) for the quote line.  */  
   WorstCsPct:number,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (best case) for the quote line.  */  
   BestCsPct:number,
      /**  Worst case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  */  
   WorstCsRevenue:number,
      /**  Worst case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  */  
   DocWorstCsRevenue:number,
   Rpt1WorstCsRevenue:number,
   Rpt2WorstCsRevenue:number,
   Rpt3WorstCsRevenue:number,
      /**  Best case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  */  
   BestCsRevenue:number,
      /**  Best case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  */  
   DocBestCsRevenue:number,
   Rpt1BestCsRevenue:number,
   Rpt2BestCsRevenue:number,
   Rpt3BestCsRevenue:number,
      /**  The original material sequence of this kit component under the kit parent part.  */  
   KitCompOrigSeq:number,
      /**  The original kit component part number prior to processing any configurator rule programs  */  
   KitCompOrigPart:string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   SmartStringProcessed:boolean,
      /**  Original smart string passed in for configuration  */  
   SmartString:string,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   LineType:string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   ContractNum:number,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   ContractCode:string,
   DiscBreakListCode:string,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
   DiscListPrice:number,
      /**  The demand contract this demand is for.  */  
   DemandContractNum:number,
   OverrideDiscPriceList:boolean,
      /**  Demand Contract Line  */  
   DemandContractLine:number,
      /**  Demand Header sequence number to which this record is related.  */  
   DemandHedSeq:number,
      /**  Demand Detail Sequence number to which this record is related.  */  
   DemandDtlSeq:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   ICPOLine:number,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   ICPONum:number,
      /**  Indicates if this quote line is linked to an inter-company PO line.  */  
   Linked:boolean,
      /**  Indicates if the price of the quote line can be changed.  */  
   LockPrice:boolean,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the quote quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   LockQty:boolean,
      /**  Indicates that the line item was closed before any shipments were made against it.  */  
   VoidLine:boolean,
      /**  Indicate that the item or the product group has a warranty.  */  
   Warranty:boolean,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   WarrantyCode:string,
      /**  Editor widget for Warranty comments.  */  
   WarrantyComment:string,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  EstimateGUID  */  
   EstimateGUID:string,
      /**  RFQCurrBaseEst  */  
   RFQCurrBaseEst:string,
      /**  RFQTemplate  */  
   RFQTemplate:string,
      /**  CreateEstimate  */  
   CreateEstimate:boolean,
      /**  Rating  */  
   Rating:string,
      /**  EstimateUserID  */  
   EstimateUserID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  NeedByDate  */  
   NeedByDate:string,
      /**  Indicates the way in which parts are made for Co-Part jobs.  There are two value “S” – Sequential and “C” – Concurrent.  Sequential is the default. This field is similar to the JobHead.ProcessMode field.  */  
   ProcessMode:string,
      /**  ECC Quote Number  */  
   ECCQuoteNum:string,
      /**  ECC Quote Line  */  
   ECCQuoteLine:number,
      /**  ECC Comment Ref  */  
   ECCCmmtRef:string,
      /**  ECCComment  */  
   ECCComment:string,
      /**  ContractID  */  
   ContractID:string,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**  Total tax in base currency. Tax detail for the line.  */  
   Tax:number,
      /**  Total tax in base currency. Tax detail for the line.  */  
   DocTax:number,
      /**  Total tax in base currency. Tax detail for the line.  */  
   Rpt1Tax:number,
      /**  Total tax in base currency. Tax detail for the line.  */  
   Rpt2Tax:number,
      /**  Total tax in base currency. Tax detail for the line.  */  
   Rpt3Tax:number,
      /**  If true, the QuoteDtlTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   TaxConnectCalc:boolean,
      /**  Indicates if no tax recalculation by the system is supposed to be done.  */  
   NoTaxRecalc:boolean,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   TotalSATax:number,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   DocTotalSATax:number,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   Rpt1TotalSATax:number,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   Rpt2TotalSATax:number,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   Rpt3TotalSATax:number,
      /**  EntityUseCode  */  
   EntityUseCode:string,
      /**  This field holds the id of this quote line in the External CRM  */  
   ExternalCRMQuoteLineID:string,
      /**  Type for returns: Blank, (C)redit or (S)tandard  */  
   ReturnLineType:string,
      /**  Base price before any price breaks and discounts  */  
   MSRP:number,
      /**  Same as MSRP except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  */  
   DocMSRP:number,
      /**  Same as MSRP except that this field contains the price in a report currency converted..  */  
   Rpt1MSRP:number,
      /**  Same as MSRP except that this field contains the price in a report currency converted..  */  
   Rpt2MSRP:number,
      /**  Same as MSRP except that this field contains the price in a report currency converted..  */  
   Rpt3MSRP:number,
      /**  Distributor end customer price.  */  
   EndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  */  
   DocEndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in a report currency converted.  */  
   Rpt1EndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in a report currency converted.  */  
   Rpt2EndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in a report currency converted.  */  
   Rpt3EndCustomerPrice:number,
      /**  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  */  
   MFCustNum:number,
      /**  Mark For ShipToNum  */  
   MFShipToNum:string,
      /**  Indicates that the One Time Mark For information defined for this record should be used.  */  
   UseOTMF:boolean,
      /**  One Time Mark For Contact Name  */  
   OTMFName:string,
      /**  One Time Mark For first line of the ShipTo address.  */  
   OTMFAddress1:string,
      /**  One Time Mark For second line of the ShipTo address.  */  
   OTMFAddress2:string,
      /**  One Time Mark For third line of the ShipTo address.  */  
   OTMFAddress3:string,
      /**  City portion of the One Time Mark For address.  */  
   OTMFCity:string,
      /**  The state or province portion of the One Time Mark For address.  */  
   OTMFState:string,
      /**  The zip or postal code portion of the One Time Mark For address.  */  
   OTMFZIP:string,
      /**  One Time Mark For Contact Name  */  
   OTMFContact:string,
      /**  Fax number for the One Time Mark For.  */  
   OTMFFaxNum:string,
      /**  Phone number for the One Time Mark For  */  
   OTMFPhoneNum:string,
      /**  Country number for the One Time Mark For  */  
   OTMFCountryNum:number,
      /**  Promotional Price offered to Dealer and Distributors  */  
   PromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  */  
   DocPromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  */  
   Rpt1PromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  */  
   Rpt2PromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  */  
   Rpt3PromotionalPrice:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  Used specifically for Deal Portal and Location Inventory, not for Inventory Tracked Attributes.  */  
   AttributeSetID:number,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   KBConfigProdID:number,
      /**  The unique identifier of the related original CPQ Configured Quote Product.  */  
   KBOriginalConfigProdID:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcQuoteHedRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number is an integer which is used to uniquely identify a quote within the system.  This is automatically assigned by the system when the user requests to create a new quote. To create a new quote the user either takes an "add" option or leaves the Quote Number fill-in zero. The system generates a number by finding the quote number of the last record on file and then a 1 to it. It then uses the greater of Last quote number + 1 or the EQSyst.StartQuoteNum.  */  
   QuoteNum:number,
      /**  Contains the internal Customer number that the links the quote to the customer master. This is not directly entered by the user. Instead the CustID is entered which provides the CustNum from the customer master. The quote must reference a valid Customer master.  */  
   CustNum:number,
      /**  Date that quote was created in the system. Not user maintainable. Set equal to the system date when record was created.  */  
   EntryDate:string,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   PrcConNum:number,
      /**  Contains comments about the overall Quote. These will be printed on the Quote form.  */  
   QuoteComment:string,
      /**  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  */  
   DueDate:string,
      /**  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  */  
   Quoted:boolean,
      /**  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  */  
   DateQuoted:string,
      /**   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.

This date is also used as part of the quote purging criteria testing.  */  
   ExpirationDate:string,
      /**  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  */  
   FollowUpDate:string,
      /**  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  */  
   Reference:string,
      /**   Optional Quote check off # 1. The label for this field is found in EQSyst. If the label field is blank then field should be invisible.
These "check offs" could be used for selecting quotes. An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff1:boolean,
      /**  Optional check off # 2.  */  
   CheckOff2:boolean,
      /**  Optional check off # 3.  */  
   CheckOff3:boolean,
      /**  Optional check off # 4.  */  
   CheckOff4:boolean,
      /**  Optional check off # 5.  */  
   CheckOff5:boolean,
      /**  Indicates if the Quote has expired.  A quote is expired when QuoteHed.ExpirationDate < Today.  Each time a user logs on the system does a quick check for any unexpired quotes that have an expiration date < Today and sets them as expired. This field is also set during the QuoteHed write trigger.  */  
   Expired:boolean,
      /**  System maintained flag - set to yes when the quote follow up alert has been sent.  */  
   FlwAlrtSnt:boolean,
      /**  System maintained flag - set to yes when the quote due date alert has been sent.  */  
   DueAlrtSnt:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  A = High, Z = Low  */  
   LeadRating:string,
      /**  Link to the territory Id for this LOQ  */  
   TerritoryID:string,
      /**  Link to Task set  */  
   TaskSetID:string,
      /**   Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  */  
   CurrentStage:string,
      /**  Link to the parent Quote.  This Quote is a for the same job as the parent but for a different customer.  This quotes revenues estimates won't be included in the sales managers figures.  */  
   ParentQuoteNum:number,
      /**  The Currently active Stage changing task  */  
   ActiveTaskID:string,
      /**  The Last Complete Milestone task  */  
   LastTaskID:string,
      /**  The date this quote is expected to close.  */  
   ExpectedClose:string,
      /**  Indicates the Type of reason for closing this quote.   "W" Win CRM "L" - Loss CRM, "T" Task CRM.  */  
   ReasonType:string,
      /**  Select from list of Win or loss reason codes depending on the setting if the conclusion field  */  
   ReasonCode:string,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential  */  
   ConfidencePct:number,
      /**  Used to establish a discount percent value which will be used as a default during Quote line entry. It can be left as zero.  Use the CUSTOMER.DISCOUNTPERCENT field as a default. Refreshed whenever QUOTEHED.CUSTOMER field changes.  */  
   DiscountPercent:number,
      /**  Indicates which customer ship to is to be used as the default for the Order release record created from this Quote. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new Quotes or when the QuoteHED.CUSTNUM is changed.  */  
   ShipToNum:string,
      /**  Establishes the Shipping Contact to be used as default on the Order release record created from this Quote. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   ShpConNum:number,
      /**  This quote is no longer updatable.  */  
   QuoteClosed:boolean,
      /**  The date that the Quote was closed.  */  
   ClosedDate:string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table. Use the CUSTOMER.SHIPVIA as the default when the CUSTNUM field is changed and the SHIPTO is blank. Use SHIPTO.SHIPVIA when CUSTNUM or SHIPTO fields are changed and the SHIPTO is not blank.  */  
   ShipViaCode:string,
      /**  Link to the Marketing Campaign related to this Quote.  */  
   MktgCampaignID:string,
      /**  Link to the marketing event associated with this record.  */  
   MktgEvntSeq:number,
      /**  CallType code from the CallType table.  Identifies what type of communication this is. For example email, phone, visit, etc.  */  
   CallTypeCode:string,
      /**  This is an optional field used to enter the customers Purchase Order Number.  */  
   PONum:string,
      /**   Contains the key value of the record in the TERMS table which indicates the sales terms established for this Opportunity/Quote. On change of QutoeHED.CUSTNUM use the CUSTOMER.TERMS
field as the default.  */  
   TermsCode:string,
      /**  Indicates that the one or more detail line items have been ordered on this quote. Note: This can be set via 3 methods. 1 - When the task is marked as a win and order is created, 2 - Via the Order Entry Get function, 2 - Via the Order Entry Add from Quote Line function.  */  
   Ordered:boolean,
      /**  Indicates if order based discounting needs to be applied to the quote.  */  
   ApplyOrderBasedDisc:boolean,
      /**  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  */  
   AutoOrderBasedDisc:boolean,
      /**  The help desk case that created this quote.  */  
   HDCaseNum:number,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**  When checked the exchange rate defaults the currency's exchanged reate, but the user can change it. When not checked the exchange rate defaults the currecy's exchange rate, and the field is disabled  */  
   LockRate:boolean,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  This flag will be used to indicate if the Quote is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the quote which could affect taxes (QuoteDtl, QuoteHed, QuoteMsc, etc). It defaults from EQSyst.QuoReadyToCalcDflt field when an order is created.  */  
   ReadyToCalc:boolean,
      /**  This field is used to store a code that represents the external system that the Quote is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  */  
   ExportRequested:string,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   Rounding:number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   DocRounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt2Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt3Rounding:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Total quote Amount. This field is an accumulation of the extended net amounts of the detail line items.  */  
   QuoteAmt:number,
      /**  Total quote Amount in customer currency. This field is an accumulation of the extended net amounts of the detail line items and rounded according to the Doc currency Round rule  */  
   DocQuoteAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1QuoteAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2QuoteAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3QuoteAmt:number,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   UseOTS:boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portion of the One Time Shipto  address.  */  
   OTSCity:string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   OTSZIP:string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   OTSResaleID:string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   OTSTaxRegionCode:string,
      /**  One Time Ship To Contact Name  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipping Country Number  */  
   OTSCountryNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Indicates that the tax is included in the unit price  */  
   InPrice:boolean,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (worst case) for the quote line.  */  
   WorstCsPct:number,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (best case) for the quote line.  */  
   BestCsPct:number,
      /**  The demand contract this demand is for.  */  
   DemandContractNum:number,
      /**  Demand Header sequence number to which this record is related.  */  
   DemandHeadSeq:number,
      /**  Defines if this document is marked as EDI Ready.  */  
   EDIReady:boolean,
      /**  Quote created from EDI interfaced module.  */  
   EDIQuote:boolean,
      /**  Updated from EDI module this type of document is created.  */  
   EDIAck:boolean,
      /**  Incremented whenever an outbound quote document is generated from the quote i.e. Response to Request For Quotes, etc.  */  
   OutboundQuoteDocCtr:number,
      /**  Date in which the related demand was last processed.  */  
   DemandProcessDate:string,
      /**  System Time when demand was last processed.  */  
   DemandProcessTime:number,
      /**  EDI Transaction Control Number  */  
   LastTCtrlNum:string,
      /**  EDI Batch Control Number  */  
   LastBatchNum:string,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   DocTotalSATax:number,
      /**   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   DocTotalTax:number,
      /**   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   DocTotalWHTax:number,
      /**   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt1TotalSATax:number,
      /**   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt1TotalTax:number,
      /**   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt1TotalWHTax:number,
      /**   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt2TotalSATax:number,
      /**   Total Quote Invoice TaxesQuote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt2TotalTax:number,
      /**   Total Order Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt2TotalWHTax:number,
      /**   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt3TotalSATax:number,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt3TotalTax:number,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   Rpt3TotalWHTax:number,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   DeliveryConf:number,
      /**  Tax Point  */  
   TaxPoint:string,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Date Used to calculate Tax Rates  */  
   TaxRateDate:string,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**  Freight charges will not be returned if 'yes'  */  
   DropShip:boolean,
      /**   Quote Total Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   TotalSATax:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**   Quote Total Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   TotalTax:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**   Quote Total Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  */  
   TotalWHTax:number,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Inter-Company Purchase order number that uniquely identifies the purchase order.  */  
   ICPONum:number,
      /**  Indicates if this quote header is linked to an inter-company PO header.  */  
   Linked:boolean,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the quote quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   LockQty:boolean,
      /**  Date customer needs the items on the order to arrive. This is used only as the default value for the NeedByDate when creating quote detail line items. This can be left blank.  */  
   NeedByDate:string,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  True if Customer or ShipTo record was created using the  OTS info.  */  
   OTSCustSaved:boolean,
      /**  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  */  
   OTSSaveAs:string,
      /**  CustID to be used if the OTS is used to create a customer record.  */  
   OTSSaveCustID:string,
      /**  Override Carrier Defaults.  If not checked then the Site values will be used  */  
   OverrideCarrier:boolean,
      /**  Override Service Options.  If not checked then the Site values will be used  */  
   OverrideService:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for QuoteDtl.RequestDate.  */  
   RequestDate:string,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Indicates that the Quote item was closed before any shipments were made against it.  */  
   VoidQuote:boolean,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Total discount percent.  */  
   TotalDiscPct:number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   TotalExpected:number,
   TotalGrossValue:number,
   TotalMiscAmt:number,
   TotalPotential:number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   TotalWorstCs:number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   DocTotalBestCs:number,
   DocTotalDiscount:number,
      /**  Total discount percent.  */  
   DocTotalDiscPct:number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   DocTotalExpected:number,
   DocTotalGrossValue:number,
   DocTotalMiscAmt:number,
   DocTotalPotential:number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   DocTotalWorstCs:number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   Rpt1TotalBestCs:number,
   Rpt1TotalDiscount:number,
      /**  Total discount percent.  */  
   Rpt1TotalDiscPct:number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   Rpt1TotalExpected:number,
   Rpt1TotalGrossValue:number,
   Rpt1TotalMiscAmt:number,
   Rpt1TotalPotential:number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   Rpt1TotalWorstCs:number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   Rpt2TotalBestCs:number,
   Rpt2TotalDiscount:number,
      /**  Total discount percent.  */  
   Rpt2TotalDiscPct:number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   Rpt2TotalExpected:number,
   Rpt2TotalGrossValue:number,
   Rpt2TotalMiscAmt:number,
   Rpt2TotalPotential:number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   Rpt2TotalWorstCs:number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   Rpt3TotalBestCs:number,
   Rpt3TotalDiscount:number,
      /**  Total discount percent.  */  
   Rpt3TotalDiscPct:number,
      /**  The expected revenue, calculated with the confidence factor.  */  
   Rpt3TotalExpected:number,
   Rpt3TotalGrossValue:number,
   Rpt3TotalMiscAmt:number,
   Rpt3TotalPotential:number,
      /**  Worst case revenue, calculated with the worst case confidence factor.  */  
   Rpt3TotalWorstCs:number,
      /**  Total best case revenue, calculated with the best case confidence factor.  */  
   TotalBestCs:number,
   TotalDiscount:number,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  LOQPrepressText  */  
   LOQPrepressText:string,
      /**  LOQNewPageOnQuoteLine  */  
   LOQNewPageOnQuoteLine:boolean,
      /**  LOQBookPCFinishing  */  
   LOQBookPCFinishing:boolean,
      /**  LOQBookPCPaper  */  
   LOQBookPCPaper:boolean,
      /**  LOQBookPCPress  */  
   LOQBookPCPress:boolean,
      /**  LOQBookPCPlates  */  
   LOQBookPCPlates:boolean,
      /**  LOQVariations  */  
   LOQVariations:boolean,
      /**  AEPLOQType  */  
   AEPLOQType:string,
      /**  LOQPrepressStyle  */  
   LOQPrepressStyle:string,
      /**  QuoteCSR  */  
   QuoteCSR:string,
      /**  DueHour  */  
   DueHour:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Quote was confirmed/rejected by ECC Web  */  
   ECCConfirmed:boolean,
      /**  Quote was confirmed/rejected by this ECC user  */  
   ECCConfirmedBy:string,
      /**  ECC quote message: RFQ or GQR  */  
   ECCMsgType:string,
      /**  Quote is ready to be approved by user via ECC web site.  */  
   ECCWebReady:boolean,
      /**  ECC Quote Number  */  
   ECCQuoteNum:string,
      /**  ECC Comment Reference Number  */  
   ECCCmmtRef:string,
      /**  ECCComment  */  
   ECCComment:string,
      /**  ECC Quote Status  */  
   ECCStatus:string,
      /**  ECC Expiration Date  */  
   ECCExpirationDate:string,
      /**  ECCCmmtRefSK  */  
   ECCCmmtRefSK:string,
      /**  This field defines if the Quote  is synchronized to an External CRM.  */  
   ExternalCRMQuote:boolean,
      /**  This field holds the  id of this quote in the External CRM  */  
   ExternalCRMQuoteID:string,
      /**  This field holds the sales order created in the External CRM. This id might not match an Epicor ERP Order id.  */  
   ExternalCRMOrderID:string,
      /**  Web Sales Rep ID  */  
   ECCSalesRepID:string,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   Tax:number,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   DocTax:number,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   Rpt1Tax:number,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   Rpt2Tax:number,
      /**  Total tax in base currency. The sum of all the tax details for the quote.  */  
   Rpt3Tax:number,
      /**  HdrTaxNoUpdt  */  
   HdrTaxNoUpdt:boolean,
      /**  This field defines the last time that the Quote has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  */  
   ExternalCRMLastSync:string,
      /**  This fields determines if the quotes needs to be synchronized to the External CRM. If there are changes in the quote or quote detail file, Epicor ERP automatically turns on this field.  */  
   ExternalCRMSyncRequired:boolean,
      /**  Total of claims credit lines  */  
   TotalClaimsCredit:number,
      /**  Total of claims credit lines in customer currency  */  
   DocTotalClaimsCredit:number,
      /**  Total of claims credit lines in report currency  */  
   Rpt1TotalClaimsCredit:number,
      /**  Total of claims credit lines in report currency  */  
   Rpt2TotalClaimsCredit:number,
      /**  Total of claims credit lines in report currency  */  
   Rpt3TotalClaimsCredit:number,
      /**  Total Quote claims credit Invoice Taxes.  */  
   TotalClaimsTax:number,
      /**  Total Quote claims credit Invoice Taxes in customer currency.  */  
   DocTotalClaimsTax:number,
      /**  Total Quote claims credit Invoice Taxes in report currency.  */  
   Rpt1TotalClaimsTax:number,
      /**  Total Quote claims credit Invoice Taxes in report currency.  */  
   Rpt2TotalClaimsTax:number,
      /**  Total Quote claims credit Invoice Taxes in report currency.  */  
   Rpt3TotalClaimsTax:number,
      /**  Total Quote claims credit Self Assessed Taxes.  */  
   TotalClaimsSATax:number,
      /**  Total Quote claims credit Self Assessed Taxes in customer currency.  */  
   DocTotalClaimsSATax:number,
      /**  Total Quote claims credit Self Assessed Taxes in customer currency.  */  
   Rpt1TotalClaimsSATax:number,
      /**  Total Quote claims credit Self Assessed Taxes in customer currency.  */  
   Rpt2TotalClaimsSATax:number,
      /**  Total Quote claims credit Self Assessed Taxes in customer currency.  */  
   Rpt3TotalClaimsSATax:number,
      /**  Total Quote claims credit Withholding Taxes.  */  
   TotalClaimsWHTax:number,
      /**  Total Quote claims credit Withholding Taxes in customer currency.  */  
   DocTotalClaimsWHTax:number,
      /**  Total Quote claims credit Withholding Taxes in report currency.  */  
   Rpt1TotalClaimsWHTax:number,
      /**  Total Quote claims credit Withholding Taxes in report currency.  */  
   Rpt2TotalClaimsWHTax:number,
      /**  Total Quote claims credit Withholding Taxes in report currency.  */  
   Rpt3TotalClaimsWHTax:number,
      /**  OTSTaxValidationStatus  */  
   OTSTaxValidationStatus:number,
      /**  OTSTaxValidationDate  */  
   OTSTaxValidationDate:string,
      /**  FSMSendTo  */  
   FSMSendTo:boolean,
      /**  Incoterm Code  */  
   IncotermCode:string,
      /**  Incoterm Location  */  
   IncotermLocation:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcQuoteMtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  The QuoteLine that record is related to.  */  
   QuoteLine:number,
      /**  The AssemblySeq number of the related QuoteAsm record.  */  
   AssemblySeq:number,
      /**  A sequence number that uniquely defines the Material record within a specific Quote/Line/Assembly.  System assigned using the next available number, determined by reading last QuoteMtl record on the Quote/Line/Assembly and then adding one to it.  */  
   MtlSeq:number,
      /**  Part number of required material. Does not have to be valid in Part master file, but must not be blank.  */  
   PartNum:string,
      /**  Description of the material. Cannot be blank  */  
   Description:string,
      /**  Quantity required per one of the Parent item. This is a factor used in calculating the total material requirement.  */  
   QtyPer:number,
      /**  The issue/usage unit of measure for this material.  */  
   IUM:string,
      /**  Indicates if this material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  */  
   Direct:boolean,
      /**  Expected Purchasing lead time (in days) for the material. This is passed along to the job if the item gets manufactured.  */  
   LeadTime:number,
      /**   A material record can be related to a specific operation. This field contains the QuoteOpr.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job.  */  
   RelatedOperation:number,
      /**  Part number for Salvaged scrap from this material record.  An optional field. This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via Salvage receipt process.  */  
   SalvagePartNum:string,
      /**  Description of Salvaged material. Use Part.Description for a default.  */  
   SalvageDescription:string,
      /**  A factor that multiplied by the RequiredQty for the material results in the expected total salvage quantity.  */  
   SalvageQtyPer:number,
      /**  Default Unit of measure for the Salvaged Part. Default from the Part.IUM.  */  
   SalvageUM:string,
      /**  Estimated Salvage Unit Credit. Use the appropriate cost from the Part master as a default.  */  
   SalvageUnitCredit:number,
      /**  The salvage material burden rate for this Quote Material.  */  
   SalvageMtlBurRate:number,
      /**  Estimated salvage Mtl Burden Unit Credit. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  */  
   SalvageEstMtlBurUnitCredit:number,
      /**   Comments for manufacturing about this material record. These comments are printed on manufacturing reports,  such as the router. For valid Parts use the Part.MfgComment as a default.
View as Editor widget.  */  
   MfgComment:string,
      /**  Used to identify a default vendor. Use the Part.VendorNum as a default. This will be used as a default for purchasing and miscellaneous receipts. This field is not directly maintainable; instead it's assigned by having the user either entering the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  An optional field, but if entered must be valid.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  */  
   PurPoint:string,
      /**  Indicates if this material is to be Purchased for the Job. If this is a non inventory part then this is "Yes" and can't be changed. If this is a valid Part then set it to "NO" but the user can override it.  */  
   BuyIt:boolean,
      /**   Comments for purchasing about this material record on this job. These comments will be used as defaults to the PODetail.Comment field when the purchase order references this JobMtl record.

View as Editor widget.  */  
   PurComment:string,
      /**  Minimum Cost that will be used for this material. That is if the system will take the greater of (required quantity * unit cost) or (MinimumCost) when calculating the material cost for the quote.  */  
   MinimumCost:number,
      /**  Estimated Unit Cost. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  */  
   EstUnitCost:number,
      /**  The material burden rate for this Quote Material.  */  
   MtlBurRate:number,
      /**  Estimated Mtl Burden Unit Cost. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  */  
   EstMtlBurUnitCost:number,
      /**  Required Qty per ONE of the  END ITEM.  This is a system calculated field.  Calculated as (Parent Required Qty X QtyPer). The parent qty is one if assemblySeq zero else  (QuoteAsmbl.RequireQty) if AssemblySeq > 0.  */  
   RequiredQty:number,
      /**  Estimated Scrap (fallout) that is expected to occur for this material. The scrap increase the Required quantity. Example; need 1000 pieces scrap of 10 % will show a required quantity of 1100.  */  
   EstScrap:number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   EstScrapType:string,
      /**  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  */  
   FixedQty:boolean,
      /**  Characters used on the drawing to show where material is used.  */  
   FindNum:string,
      /**   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
CLasses could be set up for different type of raw materials. It will primarily be used as a report selection parameter.  */  
   Class:string,
      /**   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  */  
   APSAddResType:string,
      /**  A flag to indicate that this quote material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  */  
   RFQNeeded:boolean,
      /**  The number of vendor quotes that are required for this quote material.  Can be zero if RFQ(s) are not required.  */  
   RFQVendQuotes:number,
      /**  RFQ number that the item is linked to.  */  
   RFQNum:number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   RFQLine:number,
      /**   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  */  
   RFQStat:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  Global RFQ flag.  Used in Consolidated Purchasing.  */  
   GlbRFQ:boolean,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost02:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost03:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost04:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost05:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost06:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost07:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost08:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost09:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost10:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty01:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty02:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty03:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty04:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty05:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty06:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty07:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty08:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty09:number,
      /**  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  */  
   PBrkQty10:number,
      /**  Unit cost for the corresponding price break quantity. (PBrkQty)  */  
   PBrkCost01:number,
      /**  Required number of designators  */  
   ReqRefDes:number,
      /**  The part number used to identify the configured part number initially entered on the assembly.  */  
   BasePartNum:string,
      /**  The revision number used to identify the configured part/revision number initially entered on the material.  */  
   BaseRevisionNum:string,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   OrigStructTag:string,
      /**  By storing the original Group Sequence of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   OrigGroupSeq:number,
      /**  Estimated Material Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:  */  
   EstMtlUnitCost:number,
      /**  LinkToContract  */  
   LinkToContract:boolean,
      /**  ContractID  */  
   ContractID:string,
      /**  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.   It must be a AP Misc. charge.  */  
   MiscCode:string,
      /**  This indicates that this JobMtl record is for a Misc charge related to this job/assembly.  */  
   MiscCharge:boolean,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  Unique identifier per Quote Line that allows PLM Integration to find QuoteMtl record.  */  
   PLMMtlSeq:number,
      /**  Controls if this material record is viewable in Location Management or the web.  */  
   LocationView:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   SalvageAttributeSetID:number,
      /**  Salvage planning number of pieces for this attribute set.  */  
   SalvagePlanningNumberOfPieces:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   SalvagePlanningAttributeSetID:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   SalvageRevisionNum:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcQuoteOpDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this line item detail record is associated with.   System assigned.  */  
   QuoteNum:number,
      /**  Used to link back to the QuoteLine.   System assigned.  */  
   QuoteLine:number,
      /**  Used to link back to the QuoteAsmbl record.  System assigned.  */  
   AssemblySeq:number,
      /**  Used to link back to the QuoteOpr record.  System assigned.  */  
   OprSeq:number,
      /**  Uniquely identifies the QuoteOpDtl.  System assigned.  */  
   OpDtlSeq:number,
      /**  The user can select the capability the operation is to perform.  The system will select the resource.  */  
   CapabilityID:string,
      /**  The user can select a Resource Group for the operation to be performed on.  The system will select the actual resource.  */  
   ResourceGrpID:string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource for this operation to be performed on.  */  
   ResourceID:string,
      /**  The standard setup hours for the operation.   This is the setup time required for each machine.  */  
   SetupHours:number,
      /**  Production hours for this operation.  It is the total hours, as though the operation were running on a single machine.  */  
   ProdHours:number,
      /**  This is the number of resources the operation can run on.  If multiple resources can perform the required Capability, then up to this many will be employed.  This determines the number of setups the system will allow for the operation.  However, the number of setups cannot exceed the number of operations.  The idea being that once a part is on a machine you will complete the operation on that resource.  */  
   NumResources:number,
      /**  The burden rate used for setup time.  Used as a default in Job and Quote entry.  */  
   SetupBurRate:number,
      /**  Burden rate used for production time on an operation. Job and Quoting use it as a default when entering operation details.  */  
   ProdBurRate:number,
      /**  The labor rate used for setup time.  Used as a default in Job and Quote entry.  */  
   SetupLabRate:number,
      /**  Labor rate used for production time on an operation. Job and Quoting use it as a default when entering operation details.  */  
   ProdLabRate:number,
      /**  Identifies which part of the production, setup or production, the resource is required for.   Valid values are "S", indicating the resource is RequiredFor the Setup phase of this operation, "P" for Production phase, or "B" meaning Both setup and production phase.  */  
   SetupOrProd:string,
      /**  Description is initially created when the QuoteOpDtl is created.   If the QuoteOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   OpDtlDesc:string,
      /**   The production standard for the operation.  It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours.  A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  */  
   ProdStandard:number,
      /**   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  */  
   StdFormat:string,
      /**   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   StdBasis:string,
      /**  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  */  
   OpsPerPart:number,
      /**  If yes then the user has overridden the rates that were on the  record when it was inititally created.  The initial rates came from the master files.  */  
   OverrideRates:boolean,
      /**  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  */  
   ConcurrentCapacity:number,
      /**  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  */  
   DailyProdRate:number,
      /**  Duplicated from QuoteOper.SetupCrewSize.   It's the number of people it physically takes to set up this operation.  It is used as a multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation.  This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   SetUpCrewSize:number,
      /**  Duplicated from QuoteOper.ProdCrewSize.  The number of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee.  See also SetUpCrewSize.  */  
   ProdCrewSize:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   QtyPerCycle:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcQuoteOprRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  The QuoteLine that record is related to.  */  
   QuoteLine:number,
      /**  The AssemblySeq number of the related QuoteAsm record.  */  
   AssemblySeq:number,
      /**  A sequence number which uniquely identifies the operation record within the Quote/Line/Assembly. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last QuoteOpr for the QuoteLine/Asm and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   OprSeq:number,
      /**   Operation Master Code - Links the QuoteOpr  record with a OpMaster record.  Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  */  
   OpCode:string,
      /**   The Operation standard ID. This links the JobOPer to the OpStd master file. This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.

Valid for "inside operations" only.  */  
   OpStdID:string,
      /**  The TOTAL estimated set up hours FOR ALL MACHINES. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours * Machines.  */  
   EstSetHours:number,
      /**   The production standard for the operation. It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours. A value can be defaulted from the OpStd master.

NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  */  
   ProdStandard:number,
      /**   Qualifier for the Production Standard field.  The valid qualifiers are:

"HP" - Hours/Piece, "MP" - Minutes/Piece, "PH" - Pieces/Hour,

"PM" - Pieces/Minute, "OH" - Operations/Hour,

"OM"  - Operations/Minute, HR - Fixed Hours.  */  
   StdFormat:string,
      /**   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor to the number of pieces. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.

This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   StdBasis:string,
      /**  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  */  
   OpsPerPart:number,
      /**  Production Quantity per one of the Parent Item.  */  
   QtyPer:number,
      /**  Labor rate used for estimated production labor costs. Default from the OpMaster.QProdLRate if not zero, else OpMaster.ProdLRate.  */  
   ProdLabRate:number,
      /**  Labor rate for estimated setup labor costs. Default from the OpMaster.QSetupLRate if not zero, else OpMaster.SetupLabRate.  */  
   SetupLabRate:number,
      /**  The burden rate to be used for the production time on this operation. (EstProdHrs X ProdBurRate). Default from the WrkCenter.QProdBurRate if not zero, else WrkCenter.ProdBurRate.  */  
   ProdBurRate:number,
      /**  The burden rate to be used for the Setup time on this operation. (EstSetHours X ProdBurRate). Default from the WrkCenter.QSetUpBurRate if not zero, else WrkCenter.SetupBurRate.  */  
   SetupBurRate:number,
      /**  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is, the more machines the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, NOT SETUP.  The stored setup hours is a total for all machines.  This stored number is divided by the number of machines when it is displayed on the screen during operation maintenance.  */  
   Machines:number,
      /**  Defaulted from the WrkCenter.SetUpCrewSize field.  It's the number of people it physically takes to set up this operation.  It is used as a multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation.  This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   SetUpCrewSize:number,
      /**  Defaults from the WrkCenter.ProdCrewSize. The number of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee.  See also SetUpCrewSize.  */  
   ProdCrewSize:number,
      /**  Estimated Scrap (fallout) that is expected to occur on this operation. The scrap increase the Run quantity. Example; need 1000 pieces scrap of 10 % will show a operation run quantity of 1100.  */  
   EstScrap:number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   EstScrapType:string,
      /**  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  */  
   SubContract:boolean,
      /**  Issue Unit of Measure. Applicable only when SubContract = Yes  */  
   IUM:string,
      /**  Hours required is calculated as days * 8. Only Applicable when SubContract = Yes.  */  
   DaysOut:number,
      /**  The PartNum to be shipped to the subcontract. Applicable only when SubContract = Yes.  Default the QuoteDtl.PartNum or QuoteAsm.PartNum depending on the QuoteOpr.AssemblySeq.  */  
   PartNum:string,
      /**  Description of item to be sent to subcontractor.  */  
   Description:string,
      /**  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  */  
   PurPoint:string,
      /**  Editor widget for quote operation comments.  */  
   CommentText:string,
      /**   Indicates the scheduling relationship between this and the preceding  operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  */  
   SchedRelation:string,
      /**  Minimum Cost that will be used for subcontract costs. That is if the system will take the greater of (required quantity * unit cost) or (MinimumCost) when calculating the subcontract cost for the quote.  */  
   MinimumCost:number,
      /**  Estimated Unit Cost. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  */  
   EstUnitCost:number,
      /**  Additional Setup Hours that will be required after a certain quantity has been run for this operation. The quantity at which this occurs is established in AddSetupQty field. The system determines the setup hours as SetupHrs + (Max((RunQty - AddlSetupQty,0))/AddlSetUpQty) * AddlSetupHours. Any fractional results of the AddlSetUpQty calcs are rounded up to the next whole number before multiplying by the AddlSetUpHours..  */  
   AddlSetupHours:number,
      /**  Additional Setup quantity indicates the quantity at which additional setup time will be incurred.  */  
   AddlSetUpQty:number,
      /**  Specifies the total production quantity for this operation. This is an application calculated field used for display purposes only. If no quantity is calculated, the default quantity displays the value of one. The value that displays in this field calculates as follows: Run Quantity = Scrap Quantity + Production Quantity. Note: The Run Qty value refreshes when maintenance is performed on the operation record or the assemblies production quantity is changed.  */  
   RunQty:number,
      /**   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...).
Defaulted from VendPart.MiscAmt. This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  */  
   MiscAmt:number,
      /**  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  */  
   WIQueStartDate:string,
      /**  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  */  
   WIQueStartHour:number,
      /**  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  */  
   WIStartDate:string,
      /**  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  */  
   WIStartHour:number,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIDueDate:string,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIDueHour:number,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIMoveDueDate:string,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIMoveDueHour:number,
      /**  The Number of Hours per machine per day that this operations "actual" schedule is based on.  Used in logic of quote scheduling.  */  
   WIHoursPerMachine:number,
      /**  A flag to indicate that this quote operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  */  
   RFQNeeded:boolean,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  */  
   LaborEntryMethod:string,
      /**  The number of vendor quotes that are required for this quote subcontract operation.  Can be zero if RFQ(s) are not required.  */  
   RFQVendQuotes:number,
      /**  The quantity requested for first article inspection.  */  
   FAQty:number,
      /**  RFQ number that the item is linked to.  */  
   RFQNum:number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   RFQLine:number,
      /**   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  */  
   RFQStat:string,
      /**  Used to group operation to save on setups.  */  
   SetupGroup:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**   Identifies the primary QuoteOpDtl to be used for setup.  The setup time for the operation is determined on the QuoteOpDtl.
If <> 0, must identify a valid QuoteOpDtl.  The QuoteOpDtl needs to have a RequiredFor = S or B.  */  
   PrimarySetupOpDtl:number,
      /**   Identifies the primary QuoteOpDtl to be used for production.  The production run time for the operation is determined on the QuoteOpDtl.
If <> 0, must identify a valid QuoteOpDtl.  The QuoteOpDtl needs to have a RequiredFor = P or B.  */  
   PrimaryProdOpDtl:number,
      /**  Operation Description.  */  
   OpDesc:string,
      /**  Global RFQ flag.  Used in Consolidated Purchasing.  */  
   GlbRFQ:boolean,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty07:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty08:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty09:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty10:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost01:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost02:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost03:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost04:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost05:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost06:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost07:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost08:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost09:number,
      /**  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  */  
   PBrkCost10:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate01:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate02:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate03:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate04:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate05:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate06:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate07:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate08:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate09:number,
      /**  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  */  
   PBrkStdRate10:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty01:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty02:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty03:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty04:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty05:number,
      /**  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  */  
   BrkQty06:number,
      /**  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  */  
   SNRequiredOpr:boolean,
      /**  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  */  
   SNRequiredSubConShip:boolean,
      /**   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  */  
   SendAheadType:string,
      /**   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  */  
   SendAheadOffset:number,
      /**  Delimited list of PrjRoleCd codes that are allowed for this operation.  */  
   PrjRoleList:string,
      /**  Allow use all Roles  */  
   UseAllRoles:boolean,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  PctReg  */  
   PctReg:number,
      /**  SetupMaterial  */  
   SetupMaterial:number,
      /**  MaterialColorRating  */  
   MaterialColorRating:number,
      /**  MiscInfo1  */  
   MiscInfo1:string,
      /**  MiscInfo2  */  
   MiscInfo2:string,
      /**  SetupURL  */  
   SetupURL:string,
      /**  ExpPctUp  */  
   ExpPctUp:number,
      /**  ExpCycTm  */  
   ExpCycTm:number,
      /**  ExpGood  */  
   ExpGood:number,
      /**  NonProdLimit  */  
   NonProdLimit:number,
      /**  AutoSpcEnable  */  
   AutoSpcEnable:boolean,
      /**  AutoSpcPeriod  */  
   AutoSpcPeriod:number,
      /**  PartQualEnable  */  
   PartQualEnable:boolean,
      /**  AutoSpcSubgroup  */  
   AutoSpcSubgroup:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   QtyPerCycle:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  TemplateID  */  
   TemplateID:string,
      /**  StageNumber  */  
   StageNumber:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcRuleSetResultRow{
   Company:string,
   RuleSetID:number,
   RuleTag:string,
   BOMElementTableName:string,
   BOMElementSysRowID:string,
   TestType:string,
   AssemblySeq:number,
   OprSeq:number,
   OpDtlSeq:number,
   KeepIt:boolean,
   KWExpression:string,
   AsmPartNum:string,
   MtlSeq:number,
   ExprToolTip:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcRulesResultRow{
   Company:string,
   RuleSetID:number,
   RuleSeq:number,
   ProcessSeq:number,
   RuleType:string,
   RuleTag:string,
   ExpressionText:string,
   ExprResult:string,
   TestType:string,
   ExprToolTip:string,
   BOMElementSysRowID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcStrCompRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  Part Number of the associated configurator  */  
   PartNum:string,
      /**  Revision Number of the associated configurator  */  
   RevisionNum:string,
      /**  Position order  */  
   PosOrder:number,
      /**  Name  */  
   CompName:string,
      /**  Type  */  
   CompType:string,
      /**  Data Type  */  
   CompDataType:string,
      /**  Display Format  */  
   DisplayFormat:string,
      /**  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  */  
   SourceDBRecid:string,
      /**  Defines a starting position for the value of this input in a smart string  */  
   SmartStringStart:number,
      /**  Defines an ending position for the value of this input in a smart string  */  
   SmartStringEnd:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  If true then fields on the record may be updated  */  
   CanUpdate:boolean,
      /**  The coded format to use for a Date component  */  
   DateFormat:string,
      /**  The separator to use for a date component  */  
   DateSeparator:string,
      /**  If True a 4 digit year will be used for the date  */  
   DateFourDigitYear:boolean,
      /**  Use a 3 character month instead of a numeric month  */  
   DateThreeCharMonth:boolean,
      /**  A coded value indicating the format to use for a logical component  */  
   LogicalFormat:string,
      /**  The value to use for a True logical value  */  
   LogicalTrueValue:string,
      /**  The value to use for a False logical value  */  
   LogicalFalseValue:string,
      /**  The possible values for a Radio-Set, Combo-Box, or validated Character Fill-In  */  
   PossibleValues:string,
      /**  True if formatting can be applied to the component  */  
   CanFormat:boolean,
   SmartStringSeparator:string,
      /**  Number of decimals  */  
   NumberDecimals:number,
      /**  Number of digits.  */  
   NumberDigits:number,
      /**  Type of negatives.  */  
   NumberNegatives:string,
      /**  Thousands' separator.  */  
   NumberThousands:boolean,
   BitFlag:number,
   PartNumIUM:string,
   PartNumTrackDimension:boolean,
   PartNumPartDescription:string,
   PartNumTrackSerialNum:boolean,
   PartNumTrackLots:boolean,
   PartNumPricePerCode:string,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcStructRow{
      /**  Company ID  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  Part Number of the parent configured part number  */  
   PartNum:string,
      /**  Revision Number of the parent configured part number  */  
   RevisionNum:string,
      /**  An optional label to identify the purpose of the sub configurator rule.  */  
   ConfLabel:string,
      /**  Sub assembly configured part number that can be run from this configurator based on the condition of this rule  */  
   SubPartNum:string,
      /**  The revision number of the configurator that can be run from this configurator based on the condition of this rule  */  
   SubRevisionNum:string,
      /**  Optional field.  The sales companies do not have the manufacturing information available but the manufacturing company must put the result of the sub configurator somewhere in the method.  The field has 3 options, E (Equal), G (Greater Than), L (Less Than).  The result of this rule will be inserted in the BOM in the location specified in this field.  If no value is entered, the result will be appended at the end of the BOM structure.  */  
   MtlSeq:number,
      /**  Comments describing the structure rule  */  
   Comments:string,
      /**  Default operation sequence  */  
   OprSeq:number,
      /**  Rule Tag  */  
   RuleTag:string,
      /**  Stores the assembly part number within the multi-level BOM for which the rule is related.  */  
   AsmPartNum:string,
      /**  Ex: Customization, Personalization  */  
   TypeCode:string,
      /**  StructID  */  
   StructID:number,
      /**  RelatedTo  */  
   RelatedTo:string,
      /**  RelatedToID  */  
   RelatedToID:string,
      /**  DisplaySeq  */  
   DisplaySeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  E9PcInValueRuleTag  */  
   E9PcInValueRuleTag:string,
   BasePartNum:string,
   BaseRevisionNum:string,
   CanUpdate:boolean,
   ConfigSysRowID:string,
   ConfigType:string,
   ConfigVersion:number,
   CreatePart:boolean,
   DefaultECO:string,
   DisplayTag:string,
   KeepIt:boolean,
   NewPartNum:string,
   OverwriteSIValues:boolean,
   ParentNewAsm:string,
   PromptForAutoCreate:boolean,
   PromptForCheckout:boolean,
   PromptForPart:boolean,
   PromptForSIValues:boolean,
   ResponseAutoCreatePart:boolean,
   RevExists:boolean,
      /**  Revolving Sequence  */  
   RevolvingSeq:number,
   SavedGroupSeq:number,
   SaveHeadNum:number,
   SIGroupSeq:number,
   SIHeadNum:number,
   SmartString:string,
      /**  Calculated source table name, if the RelatedTo is "Part" then this column will contain "PartRe the PartRev.SysRowID and SourceTableName will have "PartRev", otherwise both columns will be blank. For non PC configurators the source row is the same across parent and child configurators.  */  
   SourceSysRowID:string,
      /**  Calculated source table name, if the RelatedTo is "Part" then this column will contain "PartRev" and SourceSysRowID will contain the PartRev.SysRowID, otherwise both columns will be blank. For non PC configurators the source row is the same across parent and child configurators.  */  
   SourceTableName:string,
   StructTag:string,
   SubBasePartNum:string,
   SubBaseRevisionNum:string,
   SubConfigID:string,
   UseKeepWhen:boolean,
   ParentStructID:number,
   GenerateMethod:boolean,
   BitFlag:number,
   PartSellingFactor:number,
   PartTrackSerialNum:boolean,
   PartTrackDimension:boolean,
   PartPricePerCode:string,
   PartPartDescription:string,
   PartSalesUM:string,
   PartTrackLots:boolean,
   PartIUM:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcTestResultRow{
   Company:string,
   TestType:string,
   TestDesc:string,
   ConfigID:string,
   SourceEntity:string,
   TargetEntity:string,
      /**  This flag is used on the client side to filter the current test that should be displayed on the tree. Only one record should have this value set to TRUE.  */  
   ShowOnTree:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcTestResultsTableset{
   PcTestResult:Erp_Tablesets_PcTestResultRow[],
   PcAsmResult:Erp_Tablesets_PcAsmResultRow[],
   PcMtlResult:Erp_Tablesets_PcMtlResultRow[],
   PcOprResult:Erp_Tablesets_PcOprResultRow[],
   PcOpDtlResult:Erp_Tablesets_PcOpDtlResultRow[],
   PcRuleSetResult:Erp_Tablesets_PcRuleSetResultRow[],
   PcRulesResult:Erp_Tablesets_PcRulesResultRow[],
   PcActionResult:Erp_Tablesets_PcActionResultRow[],
   MethodsList:Erp_Tablesets_MethodsListRow[],
   PcJobAsmbl:Erp_Tablesets_PcJobAsmblRow[],
   PcJobHead:Erp_Tablesets_PcJobHeadRow[],
   PcJobMtl:Erp_Tablesets_PcJobMtlRow[],
   PcJobOpDtl:Erp_Tablesets_PcJobOpDtlRow[],
   PcJobOper:Erp_Tablesets_PcJobOperRow[],
   PcKitCompResult:Erp_Tablesets_PcKitCompResultRow[],
   PcQuoteAsm:Erp_Tablesets_PcQuoteAsmRow[],
   PcQuoteDtl:Erp_Tablesets_PcQuoteDtlRow[],
   PcQuoteHed:Erp_Tablesets_PcQuoteHedRow[],
   PcQuoteMtl:Erp_Tablesets_PcQuoteMtlRow[],
   PcQuoteOpDtl:Erp_Tablesets_PcQuoteOpDtlRow[],
   PcQuoteOpr:Erp_Tablesets_PcQuoteOprRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PcUserDefinedMethodParametersRow{
   BoolValue:boolean,
   Company:string,
   ConfigID:string,
   DateTimeValue:string,
   DecimalValue:number,
   FunctionName:string,
   IntValue:number,
   Modifier:string,
   ParameterName:string,
   ParamSeq:number,
   ParamType:string,
   StringValue:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcValueGrpListRow{
      /**  Company  */  
   Company:string,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  RelatedToTableName  */  
   RelatedToTableName:string,
      /**  RelatedToSysRowID  */  
   RelatedToSysRowID:string,
      /**  CreateDate  */  
   CreateDate:string,
      /**  CreateUserID  */  
   CreateUserID:string,
      /**  LastUpdated  */  
   LastUpdated:string,
      /**  LastUpdatedBy  */  
   LastUpdatedBy:string,
      /**  ConfigStatus  */  
   ConfigStatus:string,
      /**  SIValues  */  
   SIValues:boolean,
      /**  SysRowID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcValueGrpRow{
      /**  Company  */  
   Company:string,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  RelatedToTableName  */  
   RelatedToTableName:string,
      /**  RelatedToSysRowID  */  
   RelatedToSysRowID:string,
      /**  CreateDate  */  
   CreateDate:string,
      /**  CreateUserID  */  
   CreateUserID:string,
      /**  LastUpdated  */  
   LastUpdated:string,
      /**  LastUpdatedBy  */  
   LastUpdatedBy:string,
      /**  ConfigStatus  */  
   ConfigStatus:string,
      /**  SIValues  */  
   SIValues:boolean,
      /**  HeadNum  */  
   HeadNum:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   DisplaySummary:boolean,
   IncomingSmartString:boolean,
      /**  Indicates if this value group was created because of a test (test inputs or test rules).  */  
   TestID:string,
      /**  Indicates the test mode of this value group, note that TestID should be populated with a non empty Guid to make sure that all programs are generated as a test. Then this column will indicate if rules or anything else should be tested too.  */  
   TestMode:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcValueHeadRow{
      /**  Company  */  
   Company:string,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  HeadNum  */  
   HeadNum:number,
      /**  StructTag  */  
   StructTag:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  RevolvingSeq  */  
   RevolvingSeq:number,
      /**  ForeignTableName  */  
   ForeignTableName:string,
      /**  ForeignSysRowID  */  
   ForeignSysRowID:string,
      /**  SourceTableName  */  
   SourceTableName:string,
      /**  SourceSysRowID  */  
   SourceSysRowID:string,
      /**  ConfigType  */  
   ConfigType:string,
      /**  ConfigVersion  */  
   ConfigVersion:number,
      /**  DisplayTag  */  
   DisplayTag:string,
      /**  RuleTag  */  
   RuleTag:string,
      /**  ExtConfig  */  
   ExtConfig:boolean,
      /**  ExtCompany  */  
   ExtCompany:string,
      /**  AllowRecordCreation  */  
   AllowRecordCreation:boolean,
      /**  AllowPricing  */  
   AllowPricing:boolean,
      /**  PromptForConfig  */  
   PromptForConfig:boolean,
      /**  InSmartString  */  
   InSmartString:boolean,
      /**  DisplaySummary  */  
   DisplaySummary:boolean,
      /**  AllowReconfig  */  
   AllowReconfig:boolean,
      /**  IsMainForeign  */  
   IsMainForeign:boolean,
      /**  NewPartNum  */  
   NewPartNum:string,
      /**  NewSmartString  */  
   NewSmartString:string,
      /**  SIValues  */  
   SIValues:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   SIValuesGroupSeq:number,
   TestID:string,
      /**  Copied from the parent PcValueGrp record  */  
   RelatedToSysRowID:string,
      /**  Value is brought from the parent PcValueGroup record.  */  
   RelatedToTableName:string,
   SIValuesHeadNum:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcValueInputLayerDetailRow{
      /**  Company  */  
   Company:string,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  HeadNum  */  
   HeadNum:number,
      /**  ConfigID  */  
   ConfigID:string,
      /**  Input Name  */  
   InputName:string,
      /**  Image Layer ID  */  
   ImageLayerID:string,
      /**  Programmatically calculated value used to keep the rows unique.  */  
   LayerSeq:number,
      /**  LayerName  */  
   LayerName:string,
      /**  LayerDesc  */  
   LayerDesc:string,
      /**  ZIndex  */  
   ZIndex:number,
      /**  Image ID  */  
   ImageID:string,
      /**  Png file types are supported  */  
   FileType:string,
      /**  Width  */  
   Width:number,
      /**  Height  */  
   Height:number,
      /**  Free form text  */  
   Category:string,
      /**  Reserved for future development  */  
   xPos:number,
      /**  Reserved for future development  */  
   yPos:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcValueInputLayerHeaderRow{
      /**  Company  */  
   Company:string,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  HeadNum  */  
   HeadNum:number,
      /**  ConfigID  */  
   ConfigID:string,
      /**  Input Name  */  
   InputName:string,
      /**  Image Layer ID  */  
   ImageLayerID:string,
      /**  Image ID  */  
   ImageID:string,
      /**  Description  */  
   Description:string,
      /**  Location of Image  */  
   ImageURL:string,
      /**  FileType  */  
   FileType:string,
      /**  Width  */  
   Width:number,
      /**  Height  */  
   Height:number,
      /**  Used by Verify Configuration to identify changes in the layer definition.  */  
   Version:number,
      /**  Reserved for future development  */  
   xPos:number,
      /**  Reserved for future development  */  
   yPos:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcValueTableset{
   PcValueHead:Erp_Tablesets_PcValueHeadRow[],
   PcConfiguredDrawings:Erp_Tablesets_PcConfiguredDrawingsRow[],
   PcContextProperties:Erp_Tablesets_PcContextPropertiesRow[],
   PcFieldPropertiesTransport:Erp_Tablesets_PcFieldPropertiesTransportRow[],
   PcUserDefinedMethodParameters:Erp_Tablesets_PcUserDefinedMethodParametersRow[],
   PcValueInputLayerDetail:Erp_Tablesets_PcValueInputLayerDetailRow[],
   PcValueInputLayerHeader:Erp_Tablesets_PcValueInputLayerHeaderRow[],
   PcValueTransport:Erp_Tablesets_PcValueTransportRow[],
   PcVariableTransport:Erp_Tablesets_PcVariableTransportRow[],
   QBuildMapping:Erp_Tablesets_QBuildMappingRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PcValueTransportRow{
   GroupSeq:number,
   HeadNum:number,
   InputName:string,
   InputType:string,
   InputValue:string,
   PageSeq:number,
   ValueSetSeq:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcVariableTransportRow{
      /**  PcVariable group sequence.  */  
   GroupSeq:number,
      /**  PcVariable Value set sequence  */  
   ValueSetSeq:number,
      /**  PcVariable data type.  */  
   VarDataType:string,
      /**  PcVariable var name.  */  
   VarName:string,
      /**  PcVariable value.  */  
   VarValue:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QBuildMappingRow{
      /**  Company  */  
   Company:string,
      /**  Configuration ID  */  
   ConfigID:string,
      /**  Input Name  */  
   InputName:string,
      /**  This is the object name.  */  
   ObjName:string,
      /**  This is the name of the object parameter.  */  
   ObjParameter:string,
      /**  Name of the input mapped to this object parameter.  */  
   MappedInputName:string,
      /**  This is the data type of the object parameter.  */  
   ObjParameterDataType:string,
      /**  This is the initial value of the object parameter as it was defined in the designer.  This is reserved for future development.  */  
   ObjParameterInitValue:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   DataType:string,
   PageSeq:number,
   BitFlag:number,
   QBuildObjObjType:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtConfigurationRuntimeTableset{
   PcValueGrp:Erp_Tablesets_PcValueGrpRow[],
   PcValueHead:Erp_Tablesets_PcValueHeadRow[],
   PcConfigurationParams:Erp_Tablesets_PcConfigurationParamsRow[],
   PcConfiguredDrawings:Erp_Tablesets_PcConfiguredDrawingsRow[],
   PcContextProperties:Erp_Tablesets_PcContextPropertiesRow[],
   PcInputsLayerDetail:Erp_Tablesets_PcInputsLayerDetailRow[],
   PcInputsLayerHeader:Erp_Tablesets_PcInputsLayerHeaderRow[],
   PcInputsPublishToDocParams:Erp_Tablesets_PcInputsPublishToDocParamsRow[],
   PcInputVar:Erp_Tablesets_PcInputVarRow[],
   PcValueInputLayerDetail:Erp_Tablesets_PcValueInputLayerDetailRow[],
   PcValueInputLayerHeader:Erp_Tablesets_PcValueInputLayerHeaderRow[],
   QBuildMapping:Erp_Tablesets_QBuildMappingRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param methodName
      @param configId
      @param testId
      @param inParams
   */  
export interface ExecuteDataLookup_input{
   methodName:string,
   configId:string,
   testId:string,
   inParams:string,
}

export interface ExecuteDataLookup_output{
   returnObj:string,
}

   /** Required : 
      @param imageLayersInfo
   */  
export interface ExecuteGenerateFullImageLayerScriptCode_input{
   imageLayersInfo:System_Collections_Generic_KeyValuePair_System_String_System_String[],
}

export interface ExecuteGenerateFullImageLayerScriptCode_output{
   returnObj:string,
}

   /** Required : 
      @param imageLayerID
   */  
export interface ExecuteGenerateImageLayerScriptCode_input{
      /**  The Image Layer ID to be used for script generation  */  
   imageLayerID:string,
}

export interface ExecuteGenerateImageLayerScriptCode_output{
      /**  Returns the generated script code to be used by an EpiEOWebBrowser control.  */  
   returnObj:string,
}

   /** Required : 
      @param imageLayerID
      @param zIndex
      @param imageValue
      @param layerSeq
   */  
export interface ExecuteGenerateSingleImageLayerScriptCode_input{
      /**  The Image Layer ID to be used for script generation  */  
   imageLayerID:string,
      /**  The Zindex value to be used for script generation. ZIndex determines the order in which the layers are displayed.  */  
   zIndex:number,
      /**  The image to be used on script generation.  */  
   imageValue:string,
      /**  The layer index that belongs to the modified layer.  */  
   layerSeq:number,
}

export interface ExecuteGenerateSingleImageLayerScriptCode_output{
      /**  Returns the generated script code to be used by an EpiEOWebBrowser control.  */  
   returnObj:string,
}

   /** Required : 
      @param pageLoadEvent
      @param configID
      @param testID
      @param pcValueDS
   */  
export interface ExecutePageOnLoadEvents_input{
   pageLoadEvent:string,
   configID:string,
   testID:string,
   pcValueDS:Erp_Tablesets_PcValueTableset[],
}

export interface ExecutePageOnLoadEvents_output{
parameters : {
      /**  output parameters  */  
   pcValueDS:Erp_Tablesets_PcValueTableset[],
}
}

   /** Required : 
      @param methodName
      @param configID
      @param testID
      @param pcValueDS
   */  
export interface ExecuteUserDefinedWithArrayReturn_input{
      /**  The name of the server-side UDmethod to execute.  */  
   methodName:string,
      /**  The ID of the configurator the UDmethod is tied to.  */  
   configID:string,
      /**  When executing under a test (Test Inputs/Rules) this parameter should contain a valid System.Guid, otherwise it can be System.Guid.Empty  */  
   testID:string,
   pcValueDS:Erp_Tablesets_PcValueTableset[],
}

export interface ExecuteUserDefinedWithArrayReturn_output{
   returnObj:object
parameters : {
      /**  output parameters  */  
   pcValueDS:Erp_Tablesets_PcValueTableset[],
}
}

   /** Required : 
      @param methodName
      @param configID
      @param testID
      @param pcValueDS
   */  
export interface ExecuteUserDefined_input{
   methodName:string,
   configID:string,
   testID:string,
   pcValueDS:Erp_Tablesets_PcValueTableset[],
}

export interface ExecuteUserDefined_output{
   returnObj:any,      //schema had no properties on an object.
parameters : {
      /**  output parameters  */  
   pcValueDS:Erp_Tablesets_PcValueTableset[],
}
}

   /** Required : 
      @param inputImageList
      @param ConfigID
      @param GroupSeq
      @param HeadNum
   */  
export interface GetAllImages_input{
      /**  List of images used in the configurator  */  
   inputImageList:System_Collections_Generic_KeyValuePair_System_String_System_String[],
      /**  Configurator ID to retrieve the drawings and images  */  
   ConfigID:string,
      /**  Group Sequence for the reconfigure scenarios  */  
   GroupSeq:number,
      /**  Head Number that represents the configuration in the structure of a multi level configurator  */  
   HeadNum:number,
}

export interface GetAllImages_output{
   returnObj:Erp_Tablesets_PcImagesTableset[],
}

   /** Required : 
      @param inputImageList
   */  
export interface GetAllPictureBoxImages_input{
      /**  list of images for the current panel in the configuration.  The key is the input name.  The value is the image name.  */  
   inputImageList:System_Collections_Generic_KeyValuePair_System_String_System_String[],
}

export interface GetAllPictureBoxImages_output{
   returnObj:System_Collections_Generic_KeyValuePair_System_String_System_ByteArray[],
}

   /** Required : 
      @param groupSeq
   */  
export interface GetByID_input{
   groupSeq:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ConfigurationRuntimeTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ConfigurationRuntimeTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ConfigurationRuntimeTableset[],
}

   /** Required : 
      @param eccConfigSetup
   */  
export interface GetECCConfigurator_input{
      /**  eccConfigSetup: json object returned from ECC  */  
   eccConfigSetup:any,      //schema had no properties on an object.
}

export interface GetECCConfigurator_output{
      /**  configuratorContext string  */  
   returnObj:string,
}

   /** Required : 
      @param configID
      @param TestID
      @param IsTestPlan
      @param SpecID
      @param SpecRevNum
      @param clientCheckSyntaxArgs
   */  
export interface GetGeneratedClient_input{
      /**  Target configuration to generate, note that company is taken from session.  */  
   configID:string,
      /**  When executing under a test (Test Inputs/Rules) this parameter should contain a valid System.Guid, otherwise it can be System.Guid.Empty  */  
   TestID:string,
      /**  True when configuring inspection plan configuration  */  
   IsTestPlan:boolean,
      /**  Specification ID of inspection plan configuration  */  
   SpecID:string,
      /**  Specification Revision of inspection plan configuration  */  
   SpecRevNum:string,
   clientCheckSyntaxArgs:Erp_Shared_Lib_Configurator_ClientCheckSyntaxArgs[],
}

export interface GetGeneratedClient_output{
      /**  An array of compressed source code strings.  */  
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
   returnObj:Erp_Tablesets_ConfigurationRuntimeListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param RuntimeDS
      @param configID
      @param uniqueID
   */  
export interface GetNewPcConfigParams_input{
   RuntimeDS:Erp_Tablesets_ConfigurationRuntimeTableset[],
   configID:string,
   uniqueID:string,
}

export interface GetNewPcConfigParams_output{
parameters : {
      /**  output parameters  */  
   RuntimeDS:Erp_Tablesets_ConfigurationRuntimeTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPcInputVar_input{
   ds:Erp_Tablesets_ConfigurationRuntimeTableset[],
}

export interface GetNewPcInputVar_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationRuntimeTableset[],
}
}

   /** Required : 
      @param ds
      @param configID
      @param inputName
      @param imageLayerID
   */  
export interface GetNewPcInputsLayerDetail_input{
   ds:Erp_Tablesets_ConfigurationRuntimeTableset[],
   configID:string,
   inputName:string,
   imageLayerID:string,
}

export interface GetNewPcInputsLayerDetail_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationRuntimeTableset[],
}
}

   /** Required : 
      @param ds
      @param configID
      @param inputName
   */  
export interface GetNewPcInputsLayerHeader_input{
   ds:Erp_Tablesets_ConfigurationRuntimeTableset[],
   configID:string,
   inputName:string,
}

export interface GetNewPcInputsLayerHeader_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationRuntimeTableset[],
}
}

   /** Required : 
      @param RuntimeDS
      @param key
   */  
export interface GetNewPcInputsPublishToDoc_input{
   RuntimeDS:Erp_Tablesets_ConfigurationRuntimeTableset[],
   key:string,
}

export interface GetNewPcInputsPublishToDoc_output{
parameters : {
      /**  output parameters  */  
   RuntimeDS:Erp_Tablesets_ConfigurationRuntimeTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPcValueGrp_input{
   ds:Erp_Tablesets_ConfigurationRuntimeTableset[],
}

export interface GetNewPcValueGrp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationRuntimeTableset[],
}
}

   /** Required : 
      @param ds
      @param groupSeq
   */  
export interface GetNewPcValueHead_input{
   ds:Erp_Tablesets_ConfigurationRuntimeTableset[],
   groupSeq:number,
}

export interface GetNewPcValueHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationRuntimeTableset[],
}
}

   /** Required : 
      @param ds
      @param groupSeq
      @param headNum
      @param configID
      @param inputName
      @param imageLayerID
   */  
export interface GetNewPcValueInputLayerDetail_input{
   ds:Erp_Tablesets_ConfigurationRuntimeTableset[],
   groupSeq:number,
   headNum:number,
   configID:string,
   inputName:string,
   imageLayerID:string,
}

export interface GetNewPcValueInputLayerDetail_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationRuntimeTableset[],
}
}

   /** Required : 
      @param ds
      @param groupSeq
      @param headNum
      @param configID
      @param inputName
   */  
export interface GetNewPcValueInputLayerHeader_input{
   ds:Erp_Tablesets_ConfigurationRuntimeTableset[],
   groupSeq:number,
   headNum:number,
   configID:string,
   inputName:string,
}

export interface GetNewPcValueInputLayerHeader_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationRuntimeTableset[],
}
}

   /** Required : 
      @param ds
      @param configID
      @param inputName
      @param objName
   */  
export interface GetNewQBuildMapping_input{
   ds:Erp_Tablesets_ConfigurationRuntimeTableset[],
   configID:string,
   inputName:string,
   objName:string,
}

export interface GetNewQBuildMapping_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationRuntimeTableset[],
}
}

   /** Required : 
      @param configurationRuntime
      @param configurationSequenceTableSet
   */  
export interface GetPCTransportTableset_input{
   configurationRuntime:Erp_Tablesets_ConfigurationRuntimeTableset[],
   configurationSequenceTableSet:Erp_Tablesets_ConfigurationSequenceTableset[],
}

export interface GetPCTransportTableset_output{
   returnObj:Erp_Tablesets_PcValueTableset[],
parameters : {
      /**  output parameters  */  
   configurationRuntime:Erp_Tablesets_ConfigurationRuntimeTableset[],
   configurationSequenceTableSet:Erp_Tablesets_ConfigurationSequenceTableset[],
}
}

   /** Required : 
      @param fileName
      @param inputName
   */  
export interface GetPictureBoxImage_input{
   fileName:string,
   inputName:string,
}

export interface GetPictureBoxImage_output{
   returnObj:string,
}

   /** Required : 
      @param whereClausePcValueGrp
      @param whereClausePcValueHead
      @param whereClausePcConfigurationParams
      @param whereClausePcConfiguredDrawings
      @param whereClausePcContextProperties
      @param whereClausePcInputsLayerDetail
      @param whereClausePcInputsLayerHeader
      @param whereClausePcInputsPublishToDocParams
      @param whereClausePcInputVar
      @param whereClausePcValueInputLayerDetail
      @param whereClausePcValueInputLayerHeader
      @param whereClauseQBuildMapping
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePcValueGrp:string,
   whereClausePcValueHead:string,
   whereClausePcConfigurationParams:string,
   whereClausePcConfiguredDrawings:string,
   whereClausePcContextProperties:string,
   whereClausePcInputsLayerDetail:string,
   whereClausePcInputsLayerHeader:string,
   whereClausePcInputsPublishToDocParams:string,
   whereClausePcInputVar:string,
   whereClausePcValueInputLayerDetail:string,
   whereClausePcValueInputLayerHeader:string,
   whereClauseQBuildMapping:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ConfigurationRuntimeTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param configID
      @param relatedToTableName
   */  
export interface GetTargetEntityValues_input{
   configID:string,
   relatedToTableName:string,
}

export interface GetTargetEntityValues_output{
parameters : {
      /**  output parameters  */  
   allowRecordCreation:boolean,
   useInSmartString:boolean,
}
}

   /** Required : 
      @param company
   */  
export interface GetTenantID_input{
      /**  company  */  
   company:string,
}

export interface GetTenantID_output{
      /**  Tenant ID  */  
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
      @param configID
      @param targetEntity
      @param groupSeq
      @param basePartNum
      @param baseRevisionNum
      @param newPartNum
      @param mtlSeq
      @param ruleTag
   */  
export interface PartExists_input{
      /**  Configuration ID  */  
   configID:string,
      /**  Target Entity - table name being processed by the configurator  */  
   targetEntity:string,
      /**  Configuaration PcValueGrp.GroupSeq  */  
   groupSeq:number,
      /**  Base Part Number  */  
   basePartNum:string,
      /**  Base Revision Number  */  
   baseRevisionNum:string,
      /**  The part being configured  */  
   newPartNum:string,
      /**  Material Sequence of the revision being configured  */  
   mtlSeq:number,
      /**  Generated Rule Tag of the part being configured  */  
   ruleTag:string,
}

export interface PartExists_output{
parameters : {
      /**  output parameters  */  
   partExists:boolean,
   notUnique:boolean,
   sIValues:boolean,
}
}

   /** Required : 
      @param ipPartNum
      @param ipRevisionNum
   */  
export interface PartRevExists_input{
   ipPartNum:string,
   ipRevisionNum:string,
}

export interface PartRevExists_output{
   returnObj:boolean,
}

   /** Required : 
      @param configurationRuntimeDS
      @param configurationSummaryTS
   */  
export interface PreStartConfiguration_input{
   configurationRuntimeDS:Erp_Tablesets_ConfigurationRuntimeTableset[],
   configurationSummaryTS:Erp_Tablesets_ConfigurationSummaryTableset[],
}

export interface PreStartConfiguration_output{
   returnObj:Erp_Tablesets_ConfigurationSequenceTableset[],
parameters : {
      /**  output parameters  */  
   configurationRuntimeDS:Erp_Tablesets_ConfigurationRuntimeTableset[],
   configurationSummaryTS:Erp_Tablesets_ConfigurationSummaryTableset[],
}
}

   /** Required : 
      @param configID
   */  
export interface PrepareEWCRequirements_input{
      /**  Configuration ID  */  
   configID:string,
}

export interface PrepareEWCRequirements_output{
parameters : {
      /**  output parameters  */  
   accessToken:string,
   expiresIn:number,
}
}

   /** Required : 
      @param configSequenceDS
      @param configRuntimeDS
      @param pcValueDS
   */  
export interface ProcessDocumentRules_input{
   configSequenceDS:Erp_Tablesets_ConfigurationSequenceTableset[],
   configRuntimeDS:Erp_Tablesets_ConfigurationRuntimeTableset[],
   pcValueDS:Erp_Tablesets_PcValueTableset[],
}

export interface ProcessDocumentRules_output{
parameters : {
      /**  output parameters  */  
   configSequenceDS:Erp_Tablesets_ConfigurationSequenceTableset[],
   configRuntimeDS:Erp_Tablesets_ConfigurationRuntimeTableset[],
}
}

   /** Required : 
      @param configurationSequenceDS
      @param configRuntimeDS
      @param pcValueDS
      @param parAltMethod
      @param checkNextCfg
      @param enableNextPage
   */  
export interface ProcessKeepWhen_input{
   configurationSequenceDS:Erp_Tablesets_ConfigurationSequenceTableset[],
   configRuntimeDS:Erp_Tablesets_ConfigurationRuntimeTableset[],
   pcValueDS:Erp_Tablesets_PcValueTableset[],
      /**  Parent AltMethod  */  
   parAltMethod:string,
      /**  Process Keep When Run before the configuration is display to identify if configuration sequence will be changed by changing partnum rule  */  
   checkNextCfg:boolean,
   enableNextPage:boolean,
}

export interface ProcessKeepWhen_output{
parameters : {
      /**  output parameters  */  
   configurationSequenceDS:Erp_Tablesets_ConfigurationSequenceTableset[],
   configRuntimeDS:Erp_Tablesets_ConfigurationRuntimeTableset[],
   enableNextPage:boolean,
}
}

   /** Required : 
      @param configSequenceDS
      @param configRuntimeDS
   */  
export interface ProcessNICDocumentRules_input{
   configSequenceDS:Erp_Tablesets_ConfigurationSequenceTableset[],
   configRuntimeDS:Erp_Tablesets_ConfigurationRuntimeTableset[],
}

export interface ProcessNICDocumentRules_output{
parameters : {
      /**  output parameters  */  
   configSequenceDS:Erp_Tablesets_ConfigurationSequenceTableset[],
   configRuntimeDS:Erp_Tablesets_ConfigurationRuntimeTableset[],
}
}

   /** Required : 
      @param relatedToTable
      @param relatedToSysRowID
      @param partNum
      @param revisionNum
      @param altMethod
      @param configID
      @param foreignTableName
      @param foreignSysRowID
   */  
export interface ProcessNoInputsConfigurator_input{
      /**  Target entity this call is related to  */  
   relatedToTable:string,
      /**  SysRowID of the target entity  */  
   relatedToSysRowID:string,
      /**  Part Number to run NIC  */  
   partNum:string,
      /**  Revision Number to run NIC  */  
   revisionNum:string,
      /**  Alternate Method to run NIC  */  
   altMethod:string,
      /**  Configuration ID  */  
   configID:string,
      /**  Foreign entity this call is related to  */  
   foreignTableName:string,
      /**  SysRowID of the foreign entity  */  
   foreignSysRowID:string,
}

export interface ProcessNoInputsConfigurator_output{
}

   /** Required : 
      @param configurationSequenceDS
      @param configurationRuntimeDS
      @param pcValueDS
      @param testResultsDS
   */  
export interface SaveConfiguration_input{
   configurationSequenceDS:Erp_Tablesets_ConfigurationSequenceTableset[],
   configurationRuntimeDS:Erp_Tablesets_ConfigurationRuntimeTableset[],
   pcValueDS:string,
   testResultsDS:Erp_Tablesets_PcTestResultsTableset[],
}

export interface SaveConfiguration_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   configurationRuntimeDS:Erp_Tablesets_ConfigurationRuntimeTableset[],
   testPassed:boolean,
   failText:string,
   testResultsDS:Erp_Tablesets_PcTestResultsTableset[],
}
}

   /** Required : 
      @param configSequenceDS
      @param configRuntimeDS
      @param serializedData
      @param testResultsDS
   */  
export interface SaveMultiConfiguration_input{
   configSequenceDS:Erp_Tablesets_ConfigurationSequenceTableset[],
   configRuntimeDS:Erp_Tablesets_ConfigurationRuntimeTableset[],
      /**  All configuration values stored in sets of System.String and byte[] in Bas64 format serialized.  */  
   serializedData:string,
   testResultsDS:Erp_Tablesets_PcTestResultsTableset[],
}

export interface SaveMultiConfiguration_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   configSequenceDS:Erp_Tablesets_ConfigurationSequenceTableset[],
   configRuntimeDS:Erp_Tablesets_ConfigurationRuntimeTableset[],
   testResultsDS:Erp_Tablesets_PcTestResultsTableset[],
   testPassed:boolean,
   failText:string,
}
}

   /** Required : 
      @param configurationSequenceDS
      @param configurationRuntimeDS
      @param pcValueDS
      @param testResultsDS
   */  
export interface SavePCTransportConfiguration_input{
   configurationSequenceDS:Erp_Tablesets_ConfigurationSequenceTableset[],
   configurationRuntimeDS:Erp_Tablesets_ConfigurationRuntimeTableset[],
   pcValueDS:Erp_Tablesets_PcValueTableset[],
   testResultsDS:Erp_Tablesets_PcTestResultsTableset[],
}

export interface SavePCTransportConfiguration_output{
parameters : {
      /**  output parameters  */  
   configurationRuntimeDS:Erp_Tablesets_ConfigurationRuntimeTableset[],
   testResultsDS:Erp_Tablesets_PcTestResultsTableset[],
}
}

   /** Required : 
      @param configSequenceDS
      @param configRuntimeDS
      @param pcValueDsArray
      @param testResultsDS
   */  
export interface SavePcValueConfigurationMulti_input{
   configSequenceDS:Erp_Tablesets_ConfigurationSequenceTableset[],
   configRuntimeDS:Erp_Tablesets_ConfigurationRuntimeTableset[],
   pcValueDsArray:any,      //schema had no properties on an object.
   testResultsDS:Erp_Tablesets_PcTestResultsTableset[],
}

export interface SavePcValueConfigurationMulti_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   configRuntimeDS:Erp_Tablesets_ConfigurationRuntimeTableset[],
   testPassed:boolean,
   failText:string,
   testResultsDS:Erp_Tablesets_PcTestResultsTableset[],
}
}

   /** Required : 
      @param configurationSequenceDS
      @param configurationRuntimeDS
      @param pcValueDS
      @param testResultsDS
   */  
export interface SavePcValueConfiguration_input{
   configurationSequenceDS:Erp_Tablesets_ConfigurationSequenceTableset[],
   configurationRuntimeDS:Erp_Tablesets_ConfigurationRuntimeTableset[],
   pcValueDS:Erp_Tablesets_PcValueTableset[],
   testResultsDS:Erp_Tablesets_PcTestResultsTableset[],
}

export interface SavePcValueConfiguration_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   configurationRuntimeDS:Erp_Tablesets_ConfigurationRuntimeTableset[],
   testPassed:boolean,
   failText:string,
   testResultsDS:Erp_Tablesets_PcTestResultsTableset[],
}
}

   /** Required : 
      @param ds
      @param ds2
   */  
export interface StartConfiguration_input{
   ds:Erp_Tablesets_ConfigurationRuntimeTableset[],
   ds2:Erp_Tablesets_ConfigurationSequenceTableset[],
}

export interface StartConfiguration_output{
      /**  Serialized input values.  */  
   returnObj:string,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationRuntimeTableset[],
}
}

   /** Required : 
      @param ds
      @param ds2
   */  
export interface StartPcValueConfiguration_input{
   ds:Erp_Tablesets_ConfigurationRuntimeTableset[],
   ds2:Erp_Tablesets_ConfigurationSequenceTableset[],
}

export interface StartPcValueConfiguration_output{
   returnObj:Erp_Tablesets_PcValueTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationRuntimeTableset[],
}
}

   /** Required : 
      @param configID
      @param testMode
      @param ts
      @param ipRelatedToTable
      @param ipRelatedToSysRowID
      @param smartStringValues
      @param structTag
      @param structID
   */  
export interface SuggestSmartString_input{
      /**  Configuration ID  */  
   configID:string,
      /**  Test Inputs true/false  */  
   testMode:boolean,
   ts:Erp_Tablesets_ConfigurationSequenceTableset[],
      /**  Target entity this call is related to  */  
   ipRelatedToTable:string,
      /**  SysRowID of the target entity  */  
   ipRelatedToSysRowID:string,
      /**  Collection of current input answers from the configuration session.  */  
   smartStringValues:Erp_Shared_Lib_Configurator_PCKeyValuePair_System_String_System_String[],
      /**  Identifies the row in the ConfigurationSequenceTableset being processed  */  
   structTag:string,
      /**  Identifies the row in the ConfigurationSequenceTableset being processed  */  
   structID:number,
}

export interface SuggestSmartString_output{
parameters : {
      /**  output parameters  */  
   ts:Erp_Tablesets_ConfigurationSequenceTableset[],
   outSmartString:string,
}
}

export interface System_Collections_Generic_KeyValuePair_System_String_System_ByteArray{
   Key:string,
   Value:string,
}

export interface System_Collections_Generic_KeyValuePair_System_String_System_String{
   Key:string,
   Value:string,
}

   /** Required : 
      @param configID
      @param partNum
      @param revisionNum
      @param ts
   */  
export interface TestNICRules_input{
      /**  Configuration ID to run test rules  */  
   configID:string,
      /**  Part Number to run test rules  */  
   partNum:string,
      /**  Revision Number to run test rules  */  
   revisionNum:string,
   ts:Erp_Tablesets_PcTestResultsTableset[],
}

export interface TestNICRules_output{
parameters : {
      /**  output parameters  */  
   ts:Erp_Tablesets_PcTestResultsTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtConfigurationRuntimeTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtConfigurationRuntimeTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ConfigurationRuntimeTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationRuntimeTableset[],
}
}

