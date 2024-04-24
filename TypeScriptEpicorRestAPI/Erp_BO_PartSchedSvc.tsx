import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PartSchedSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/$metadata", {
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
   Description: Get PartScheds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartScheds
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartSchedRow
   */  
export function get_PartScheds(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSchedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartScheds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSchedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartScheds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartSchedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartSchedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartScheds(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartScheds", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PartSched item
   Description: Calls GetByID to retrieve the PartSched item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartSched
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartSchedRow
   */  
export function get_PartScheds_Company_PartNum_Plant(Company:string, PartNum:string, Plant:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartSchedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartScheds(" + Company + "," + PartNum + "," + Plant + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PartSchedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PartSched for the service
   Description: Calls UpdateExt to update PartSched. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartSched
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartSchedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PartScheds_Company_PartNum_Plant(Company:string, PartNum:string, Plant:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartScheds(" + Company + "," + PartNum + "," + Plant + ")", {
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
   Summary: Call UpdateExt to delete PartSched item
   Description: Call UpdateExt to delete PartSched item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartSched
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PartScheds_Company_PartNum_Plant(Company:string, PartNum:string, Plant:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartScheds(" + Company + "," + PartNum + "," + Plant + ")", {
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
   Description: Get PartSchedVends items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PartSchedVends1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartSchedVendRow
   */  
export function get_PartScheds_Company_PartNum_Plant_PartSchedVends(Company:string, PartNum:string, Plant:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSchedVendRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartScheds(" + Company + "," + PartNum + "," + Plant + ")/PartSchedVends", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSchedVendRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PartSchedVend item
   Description: Calls GetByID to retrieve the PartSchedVend item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartSchedVend1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartSchedVendRow
   */  
export function get_PartScheds_Company_PartNum_Plant_PartSchedVends_Company_PartNum_Plant_VendorNum_PurPoint(Company:string, PartNum:string, Plant:string, VendorNum:string, PurPoint:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartSchedVendRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartScheds(" + Company + "," + PartNum + "," + Plant + ")/PartSchedVends(" + Company + "," + PartNum + "," + Plant + "," + VendorNum + "," + PurPoint + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PartSchedVendRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PartSchedVendPOes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PartSchedVendPOes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartSchedVendPORow
   */  
export function get_PartScheds_Company_PartNum_Plant_PartSchedVendPOes(Company:string, PartNum:string, Plant:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSchedVendPORow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartScheds(" + Company + "," + PartNum + "," + Plant + ")/PartSchedVendPOes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSchedVendPORow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PartSchedVendPO item
   Description: Calls GetByID to retrieve the PartSchedVendPO item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartSchedVendPO1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param ContractPONum Desc: ContractPONum   Required: True
      @param ContractPOLine Desc: ContractPOLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartSchedVendPORow
   */  
export function get_PartScheds_Company_PartNum_Plant_PartSchedVendPOes_Company_PartNum_Plant_VendorNum_PurPoint_ContractPONum_ContractPOLine(Company:string, PartNum:string, Plant:string, VendorNum:string, PurPoint:string, ContractPONum:string, ContractPOLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartSchedVendPORow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartScheds(" + Company + "," + PartNum + "," + Plant + ")/PartSchedVendPOes(" + Company + "," + PartNum + "," + Plant + "," + VendorNum + "," + PurPoint + "," + ContractPONum + "," + ContractPOLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PartSchedVendPORow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PartSchedVends items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartSchedVends
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartSchedVendRow
   */  
export function get_PartSchedVends(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSchedVendRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartSchedVends", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSchedVendRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartSchedVends
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartSchedVendRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartSchedVendRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartSchedVends(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartSchedVends", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PartSchedVend item
   Description: Calls GetByID to retrieve the PartSchedVend item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartSchedVend
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartSchedVendRow
   */  
export function get_PartSchedVends_Company_PartNum_Plant_VendorNum_PurPoint(Company:string, PartNum:string, Plant:string, VendorNum:string, PurPoint:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartSchedVendRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartSchedVends(" + Company + "," + PartNum + "," + Plant + "," + VendorNum + "," + PurPoint + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PartSchedVendRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PartSchedVend for the service
   Description: Calls UpdateExt to update PartSchedVend. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartSchedVend
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartSchedVendRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PartSchedVends_Company_PartNum_Plant_VendorNum_PurPoint(Company:string, PartNum:string, Plant:string, VendorNum:string, PurPoint:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartSchedVends(" + Company + "," + PartNum + "," + Plant + "," + VendorNum + "," + PurPoint + ")", {
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
   Summary: Call UpdateExt to delete PartSchedVend item
   Description: Call UpdateExt to delete PartSchedVend item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartSchedVend
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PartSchedVends_Company_PartNum_Plant_VendorNum_PurPoint(Company:string, PartNum:string, Plant:string, VendorNum:string, PurPoint:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartSchedVends(" + Company + "," + PartNum + "," + Plant + "," + VendorNum + "," + PurPoint + ")", {
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
   Description: Get PartSchedVendPOes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartSchedVendPOes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartSchedVendPORow
   */  
export function get_PartSchedVendPOes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSchedVendPORow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartSchedVendPOes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSchedVendPORow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartSchedVendPOes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartSchedVendPORow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartSchedVendPORow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartSchedVendPOes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartSchedVendPOes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PartSchedVendPO item
   Description: Calls GetByID to retrieve the PartSchedVendPO item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartSchedVendPO
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param ContractPONum Desc: ContractPONum   Required: True
      @param ContractPOLine Desc: ContractPOLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartSchedVendPORow
   */  
export function get_PartSchedVendPOes_Company_PartNum_Plant_VendorNum_PurPoint_ContractPONum_ContractPOLine(Company:string, PartNum:string, Plant:string, VendorNum:string, PurPoint:string, ContractPONum:string, ContractPOLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartSchedVendPORow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartSchedVendPOes(" + Company + "," + PartNum + "," + Plant + "," + VendorNum + "," + PurPoint + "," + ContractPONum + "," + ContractPOLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PartSchedVendPORow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PartSchedVendPO for the service
   Description: Calls UpdateExt to update PartSchedVendPO. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartSchedVendPO
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param ContractPONum Desc: ContractPONum   Required: True
      @param ContractPOLine Desc: ContractPOLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartSchedVendPORow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PartSchedVendPOes_Company_PartNum_Plant_VendorNum_PurPoint_ContractPONum_ContractPOLine(Company:string, PartNum:string, Plant:string, VendorNum:string, PurPoint:string, ContractPONum:string, ContractPOLine:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartSchedVendPOes(" + Company + "," + PartNum + "," + Plant + "," + VendorNum + "," + PurPoint + "," + ContractPONum + "," + ContractPOLine + ")", {
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
   Summary: Call UpdateExt to delete PartSchedVendPO item
   Description: Call UpdateExt to delete PartSchedVendPO item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartSchedVendPO
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param ContractPONum Desc: ContractPONum   Required: True
      @param ContractPOLine Desc: ContractPOLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PartSchedVendPOes_Company_PartNum_Plant_VendorNum_PurPoint_ContractPONum_ContractPOLine(Company:string, PartNum:string, Plant:string, VendorNum:string, PurPoint:string, ContractPONum:string, ContractPOLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartSchedVendPOes(" + Company + "," + PartNum + "," + Plant + "," + VendorNum + "," + PurPoint + "," + ContractPONum + "," + ContractPOLine + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartSchedListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSchedListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSchedListRow)
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
export function get_GetRows(whereClausePartSched:string, whereClausePartSchedVend:string, whereClausePartSchedVendPO:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePartSched!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartSched=" + whereClausePartSched
   }
   if(typeof whereClausePartSchedVend!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartSchedVend=" + whereClausePartSchedVend
   }
   if(typeof whereClausePartSchedVendPO!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartSchedVendPO=" + whereClausePartSchedVendPO
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(partNum:string, plant:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof partNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "partNum=" + partNum
   }
   if(typeof plant!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "plant=" + plant
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/GetList" + params, {
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
   Summary: Invoke method GetPartXRefInfo
   Description: This method defaults PartAdvisor fields when the PartNum field changes
   OperationID: GetPartXRefInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartXRefInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/GetPartXRefInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Validate CalendarId value
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/OnChangeCalendarID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeInspNextDelivery
   Description: Validate InspNextDelivery value
   OperationID: OnChangeInspNextDelivery
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeInspNextDelivery_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInspNextDelivery_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeInspNextDelivery(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/OnChangeInspNextDelivery", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMinDeliveryQty1
   Description: Validate MinDeliveryQty1 value
   OperationID: OnChangeMinDeliveryQty1
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMinDeliveryQty1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMinDeliveryQty1_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMinDeliveryQty1(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/OnChangeMinDeliveryQty1", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMinDeliveryQty2
   Description: Validate MinDeliveryQty2 value
   OperationID: OnChangeMinDeliveryQty2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMinDeliveryQty2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMinDeliveryQty2_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMinDeliveryQty2(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/OnChangeMinDeliveryQty2", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMinForwardSpan
   Description: Validate MinForwardSpan value
   OperationID: OnChangeMinForwardSpan
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMinForwardSpan_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMinForwardSpan_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMinForwardSpan(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/OnChangeMinForwardSpan", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOrderCover
   Description: Validate OrderCover value
   OperationID: OnChangeOrderCover
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOrderCover_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOrderCover_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOrderCover(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/OnChangeOrderCover", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePartNum
   Description: Validate PartNum value
   OperationID: OnChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/OnChangePartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePercentShare
   Description: Validate PercentShare value
   OperationID: OnChangePercentShare
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePercentShare_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePercentShare_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePercentShare(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/OnChangePercentShare", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePeriodicityCode1
   Description: Validate PeriodicityCode1 value
   OperationID: OnChangePeriodicityCode1
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePeriodicityCode1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePeriodicityCode1_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePeriodicityCode1(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/OnChangePeriodicityCode1", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePeriodicityCode2
   Description: Validate PeriodicityCode2 value
   OperationID: OnChangePeriodicityCode2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePeriodicityCode2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePeriodicityCode2_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePeriodicityCode2(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/OnChangePeriodicityCode2", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePeriodShift
   Description: Validate PeriodShift value
   OperationID: OnChangePeriodShift
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePeriodShift_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePeriodShift_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePeriodShift(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/OnChangePeriodShift", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePrintLength
   Description: Validate PrintLength value
   OperationID: OnChangePrintLength
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePrintLength_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePrintLength_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePrintLength(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/OnChangePrintLength", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePurPoint
   Description: Validate PurPoint value
   OperationID: OnChangePurPoint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePurPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePurPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePurPoint(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/OnChangePurPoint", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeScheduleFirm
   Description: Validate ScheduleFirm value
   OperationID: OnChangeScheduleFirm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeScheduleFirm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeScheduleFirm_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeScheduleFirm(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/OnChangeScheduleFirm", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeScheduleLength
   Description: Validate ScheduleLength value
   OperationID: OnChangeScheduleLength
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeScheduleLength_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeScheduleLength_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeScheduleLength(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/OnChangeScheduleLength", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeVendorID
   Description: Validate VendorId value
   OperationID: OnChangeVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeVendorID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/OnChangeVendorID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeVendorNum
   Description: Validate VendorNum value
   OperationID: OnChangeVendorNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeVendorNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendorNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeVendorNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/OnChangeVendorNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PartPlantIsLinkedToContract
   Description: Read the Link To Contract flag from PartPlant.
   OperationID: PartPlantIsLinkedToContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartPlantIsLinkedToContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartPlantIsLinkedToContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartPlantIsLinkedToContract(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/PartPlantIsLinkedToContract", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FindPart
   OperationID: FindPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FindPart(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/FindPart", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPartFromRowID
   OperationID: GetPartFromRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartFromRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFromRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartFromRowID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/GetPartFromRowID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetValidAndProjectedWorkingDate
   Description: Projects forwards the Days to add from the base date only counting working days, and then using existing function to ensure that projected date is valid
   OperationID: GetValidAndProjectedWorkingDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetValidAndProjectedWorkingDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetValidAndProjectedWorkingDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetValidAndProjectedWorkingDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/GetValidAndProjectedWorkingDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPartSched
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartSched
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartSched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartSched_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartSched(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/GetNewPartSched", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPartSchedVend
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartSchedVend
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartSchedVend_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartSchedVend_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartSchedVend(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/GetNewPartSchedVend", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPartSchedVendPO
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartSchedVendPO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartSchedVendPO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartSchedVendPO_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartSchedVendPO(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/GetNewPartSchedVendPO", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartSchedSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSchedListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartSchedListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSchedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartSchedRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSchedVendPORow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartSchedVendPORow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSchedVendRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartSchedVendRow[],
}

export interface Erp_Tablesets_PartSchedListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique part number that identifies this part.  */  
   "PartNum":string,
      /**  Unique identifier of this Site assigned by the user.  */  
   "Plant":string,
      /**  Is this Part active within a Purchase Contract Schedule within this Site?  */  
   "IsActive":boolean,
      /**   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  */  
   "CalendarID":string,
      /**  Periodicity Code.  Possible values are 1 = Semi-Weekly, 2 = Daily, 3 = Monthly Forward, 4 = Weekly Forward, 5 = Weekly Not Last Week of the Month, 6 = Nth Day of the Month  */  
   "PeriodicityCode1":number,
      /**  Periodicity Code.  Possible values are 1 = Semi-Weekly, 2 = Daily, 3 = Monthly Forward, 4 = Weekly Forward, 5 = Weekly Not Last Week of the Month, 6 = Nth Day of the Month  */  
   "PeriodicityCode2":number,
      /**  Defines when the scheduling system will shift the schedule from Periodicity Code 1 to Periodicity Code 2.  */  
   "PeriodShift":number,
      /**  Minimum quantity for any given Purchase Contract Delivery relating to Periodicity Code 1.  */  
   "MinDeliveryQty1":number,
      /**  Minimum quantity for any given Purchase Contract Delivery relating to Periodicity Code 2.  */  
   "MinDeliveryQty2":number,
      /**  How far into the future the Minimum Delivery Quantity should be applied.  */  
   "MinForwardSpan":number,
      /**  Used only when Periodicity Code 2 (Daily) is used - and defines how many days from the current date that no increases in quantity are allowed.  */  
   "FirmIncrease":number,
      /**  Used only when Periodicity Code 2 (Daily) is used - and defines how many days from the current date that no decreases in quantity are allowed.  */  
   "FirmDecrease":number,
      /**  How many days into the future Purchase Order Releases should be created for the Purchase Contract.  */  
   "OrderCover":number,
      /**  How many days of Material Costs will be honored on the Purchase Contract.  */  
   "MaterialCover":number,
      /**  The Number of Days for which the Part Schedule will be printed.  */  
   "PrintLength":number,
      /**  The maximum period for which schedules will be created.  */  
   "ScheduleLength":number,
      /**  The number of days for which the current schedule is considered firm and will not be overwritten by a new proposed schedule.  If this value is zero, then all dates can be overwritten.  */  
   "ScheduleFirm":number,
      /**  For development use only.  */  
   "DevChar01":string,
      /**  For development use only.  */  
   "DevChar02":string,
      /**  For development use only.  */  
   "DevChar03":string,
      /**  For development use only.  */  
   "DevChar04":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PartDesctiption  */  
   "PartDescription":string,
      /**  Check if both MinDeliveryQty's are 0  */  
   "AreMinQuantitiesZero":boolean,
      /**  Base UOM  */  
   "IUM":string,
      /**  The Plant name. Used on shipping reports.  */  
   "PlantName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartSchedRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique part number that identifies this part.  */  
   "PartNum":string,
      /**  Unique identifier of this Site assigned by the user.  */  
   "Plant":string,
      /**  Is this Part active within a Purchase Contract Schedule within this Site?  */  
   "IsActive":boolean,
      /**   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  */  
   "CalendarID":string,
      /**  Periodicity Code.  Possible values are 1 = Semi-Weekly, 2 = Daily, 3 = Monthly Forward, 4 = Weekly Forward, 5 = Weekly Not Last Week of the Month, 6 = Nth Day of the Month  */  
   "PeriodicityCode1":number,
      /**  Periodicity Code.  Possible values are 1 = Semi-Weekly, 2 = Daily, 3 = Monthly Forward, 4 = Weekly Forward, 5 = Weekly Not Last Week of the Month, 6 = Nth Day of the Month  */  
   "PeriodicityCode2":number,
      /**  Defines when the scheduling system will shift the schedule from Periodicity Code 1 to Periodicity Code 2.  */  
   "PeriodShift":number,
      /**  Minimum quantity for any given Purchase Contract Delivery relating to Periodicity Code 1.  */  
   "MinDeliveryQty1":number,
      /**  Minimum quantity for any given Purchase Contract Delivery relating to Periodicity Code 2.  */  
   "MinDeliveryQty2":number,
      /**  How far into the future the Minimum Delivery Quantity should be applied.  */  
   "MinForwardSpan":number,
      /**  Used only when Periodicity Code 2 (Daily) is used - and defines how many days from the current date that no increases in quantity are allowed.  */  
   "FirmIncrease":number,
      /**  Used only when Periodicity Code 2 (Daily) is used - and defines how many days from the current date that no decreases in quantity are allowed.  */  
   "FirmDecrease":number,
      /**  How many days into the future Purchase Order Releases should be created for the Purchase Contract.  */  
   "OrderCover":number,
      /**  How many days of Material Costs will be honored on the Purchase Contract.  */  
   "MaterialCover":number,
      /**  The Number of Days for which the Part Schedule will be printed.  */  
   "PrintLength":number,
      /**  The maximum period for which schedules will be created.  */  
   "ScheduleLength":number,
      /**  The number of days for which the current schedule is considered firm and will not be overwritten by a new proposed schedule.  If this value is zero, then all dates can be overwritten.  */  
   "ScheduleFirm":number,
      /**  For development use only.  */  
   "DevChar01":string,
      /**  For development use only.  */  
   "DevChar02":string,
      /**  For development use only.  */  
   "DevChar03":string,
      /**  For development use only.  */  
   "DevChar04":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PartDesctiption  */  
   "PartDescription":string,
      /**  Check if both MinDeliveryQty's are 0  */  
   "AreMinQuantitiesZero":boolean,
      /**  Base UOM  */  
   "IUM":string,
   "LastRunDate":string,
   "BitFlag":number,
   "PlantName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartSchedVendPORow{
      /**  Company  */  
   "Company":string,
      /**  PartNum  */  
   "PartNum":string,
      /**  Plant  */  
   "Plant":string,
      /**  VendorNum  */  
   "VendorNum":number,
      /**  PurPoint  */  
   "PurPoint":string,
      /**  ContractPONum  */  
   "ContractPONum":number,
      /**  ContractPOLine  */  
   "ContractPOLine":number,
      /**  ContractStartDate  */  
   "ContractStartDate":string,
      /**  ContractEndDate  */  
   "ContractEndDate":string,
      /**  IsActive  */  
   "IsActive":boolean,
      /**  IsExpired  */  
   "IsExpired":boolean,
      /**  IsApproved  */  
   "IsApproved":boolean,
      /**  PercentShare  */  
   "PercentShare":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "ScheduleFirmDate":string,
   "MinPeriod1ShiftDate":string,
   "MinForwardSpanDate":string,
   "LastRunDate":string,
   "BitFlag":number,
   "PlantName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartSchedVendRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique part number that identifies this part.  */  
   "PartNum":string,
      /**  Unique identifier of this Site assigned by the user.  */  
   "Plant":string,
      /**  A unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   "VendorNum":number,
      /**  Purchase Point  */  
   "PurPoint":string,
      /**  Percentage Share of the Purchase Schedule for this Supplier.  Total of all Suppliers for this Part must equal 100 percent.  */  
   "PercentShare":number,
      /**  Should the Inspection flag be set when the Purchase Schedule is approved.  */  
   "InspNextDelivery":number,
      /**  Purchase order number that uniquely identifies the Contract Purchase Order.  */  
   "ContractPONum":number,
      /**  The line number of the detail record on the Contract Purchase Order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   "ContractPOLine":number,
      /**  Does the Supplier make deliveries on Monday?  */  
   "DeliverMonday":boolean,
      /**  Does the Supplier make deliveries on Tuesday?  */  
   "DeliverTuesday":boolean,
      /**  Does the Supplier make deliveries on Wednesday?  */  
   "DeliverWednesday":boolean,
      /**  Does the Supplier make deliveries on Thursday?  */  
   "DeliverThursday":boolean,
      /**  Does the Supplier make deliveries on Friday?  */  
   "DeliverFriday":boolean,
      /**  Does the Supplier make deliveries on Saturday?  */  
   "DeliverSaturday":boolean,
      /**  Does the Supplier make deliveries on Sunday?  */  
   "DeliverSunday":boolean,
      /**  For development use only.  */  
   "DevChar01":string,
      /**  For development use only.  */  
   "DevChar02":string,
      /**  For development use only.  */  
   "DevChar03":string,
      /**  For development use only.  */  
   "DevChar04":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  VendorName  */  
   "VendorName":string,
      /**  VendorID  */  
   "VendorID":string,
      /**  Indicates if the Supplier is active.  Supplier is inactive if PercentShare is 0.  */  
   "IsActive":boolean,
   "BitFlag":number,
   "PlantName":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param partNum
      @param plant
   */  
export interface DeleteByID_input{
   partNum:string,
   plant:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PartSchedListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  Unique identifier of this Site assigned by the user.  */  
   Plant:string,
      /**  Is this Part active within a Purchase Contract Schedule within this Site?  */  
   IsActive:boolean,
      /**   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  */  
   CalendarID:string,
      /**  Periodicity Code.  Possible values are 1 = Semi-Weekly, 2 = Daily, 3 = Monthly Forward, 4 = Weekly Forward, 5 = Weekly Not Last Week of the Month, 6 = Nth Day of the Month  */  
   PeriodicityCode1:number,
      /**  Periodicity Code.  Possible values are 1 = Semi-Weekly, 2 = Daily, 3 = Monthly Forward, 4 = Weekly Forward, 5 = Weekly Not Last Week of the Month, 6 = Nth Day of the Month  */  
   PeriodicityCode2:number,
      /**  Defines when the scheduling system will shift the schedule from Periodicity Code 1 to Periodicity Code 2.  */  
   PeriodShift:number,
      /**  Minimum quantity for any given Purchase Contract Delivery relating to Periodicity Code 1.  */  
   MinDeliveryQty1:number,
      /**  Minimum quantity for any given Purchase Contract Delivery relating to Periodicity Code 2.  */  
   MinDeliveryQty2:number,
      /**  How far into the future the Minimum Delivery Quantity should be applied.  */  
   MinForwardSpan:number,
      /**  Used only when Periodicity Code 2 (Daily) is used - and defines how many days from the current date that no increases in quantity are allowed.  */  
   FirmIncrease:number,
      /**  Used only when Periodicity Code 2 (Daily) is used - and defines how many days from the current date that no decreases in quantity are allowed.  */  
   FirmDecrease:number,
      /**  How many days into the future Purchase Order Releases should be created for the Purchase Contract.  */  
   OrderCover:number,
      /**  How many days of Material Costs will be honored on the Purchase Contract.  */  
   MaterialCover:number,
      /**  The Number of Days for which the Part Schedule will be printed.  */  
   PrintLength:number,
      /**  The maximum period for which schedules will be created.  */  
   ScheduleLength:number,
      /**  The number of days for which the current schedule is considered firm and will not be overwritten by a new proposed schedule.  If this value is zero, then all dates can be overwritten.  */  
   ScheduleFirm:number,
      /**  For development use only.  */  
   DevChar01:string,
      /**  For development use only.  */  
   DevChar02:string,
      /**  For development use only.  */  
   DevChar03:string,
      /**  For development use only.  */  
   DevChar04:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PartDesctiption  */  
   PartDescription:string,
      /**  Check if both MinDeliveryQty's are 0  */  
   AreMinQuantitiesZero:boolean,
      /**  Base UOM  */  
   IUM:string,
      /**  The Plant name. Used on shipping reports.  */  
   PlantName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartSchedListTableset{
   PartSchedList:Erp_Tablesets_PartSchedListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartSchedRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  Unique identifier of this Site assigned by the user.  */  
   Plant:string,
      /**  Is this Part active within a Purchase Contract Schedule within this Site?  */  
   IsActive:boolean,
      /**   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  */  
   CalendarID:string,
      /**  Periodicity Code.  Possible values are 1 = Semi-Weekly, 2 = Daily, 3 = Monthly Forward, 4 = Weekly Forward, 5 = Weekly Not Last Week of the Month, 6 = Nth Day of the Month  */  
   PeriodicityCode1:number,
      /**  Periodicity Code.  Possible values are 1 = Semi-Weekly, 2 = Daily, 3 = Monthly Forward, 4 = Weekly Forward, 5 = Weekly Not Last Week of the Month, 6 = Nth Day of the Month  */  
   PeriodicityCode2:number,
      /**  Defines when the scheduling system will shift the schedule from Periodicity Code 1 to Periodicity Code 2.  */  
   PeriodShift:number,
      /**  Minimum quantity for any given Purchase Contract Delivery relating to Periodicity Code 1.  */  
   MinDeliveryQty1:number,
      /**  Minimum quantity for any given Purchase Contract Delivery relating to Periodicity Code 2.  */  
   MinDeliveryQty2:number,
      /**  How far into the future the Minimum Delivery Quantity should be applied.  */  
   MinForwardSpan:number,
      /**  Used only when Periodicity Code 2 (Daily) is used - and defines how many days from the current date that no increases in quantity are allowed.  */  
   FirmIncrease:number,
      /**  Used only when Periodicity Code 2 (Daily) is used - and defines how many days from the current date that no decreases in quantity are allowed.  */  
   FirmDecrease:number,
      /**  How many days into the future Purchase Order Releases should be created for the Purchase Contract.  */  
   OrderCover:number,
      /**  How many days of Material Costs will be honored on the Purchase Contract.  */  
   MaterialCover:number,
      /**  The Number of Days for which the Part Schedule will be printed.  */  
   PrintLength:number,
      /**  The maximum period for which schedules will be created.  */  
   ScheduleLength:number,
      /**  The number of days for which the current schedule is considered firm and will not be overwritten by a new proposed schedule.  If this value is zero, then all dates can be overwritten.  */  
   ScheduleFirm:number,
      /**  For development use only.  */  
   DevChar01:string,
      /**  For development use only.  */  
   DevChar02:string,
      /**  For development use only.  */  
   DevChar03:string,
      /**  For development use only.  */  
   DevChar04:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PartDesctiption  */  
   PartDescription:string,
      /**  Check if both MinDeliveryQty's are 0  */  
   AreMinQuantitiesZero:boolean,
      /**  Base UOM  */  
   IUM:string,
   LastRunDate:string,
   BitFlag:number,
   PlantName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartSchedTableset{
   PartSched:Erp_Tablesets_PartSchedRow[],
   PartSchedVend:Erp_Tablesets_PartSchedVendRow[],
   PartSchedVendPO:Erp_Tablesets_PartSchedVendPORow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartSchedVendPORow{
      /**  Company  */  
   Company:string,
      /**  PartNum  */  
   PartNum:string,
      /**  Plant  */  
   Plant:string,
      /**  VendorNum  */  
   VendorNum:number,
      /**  PurPoint  */  
   PurPoint:string,
      /**  ContractPONum  */  
   ContractPONum:number,
      /**  ContractPOLine  */  
   ContractPOLine:number,
      /**  ContractStartDate  */  
   ContractStartDate:string,
      /**  ContractEndDate  */  
   ContractEndDate:string,
      /**  IsActive  */  
   IsActive:boolean,
      /**  IsExpired  */  
   IsExpired:boolean,
      /**  IsApproved  */  
   IsApproved:boolean,
      /**  PercentShare  */  
   PercentShare:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   ScheduleFirmDate:string,
   MinPeriod1ShiftDate:string,
   MinForwardSpanDate:string,
   LastRunDate:string,
   BitFlag:number,
   PlantName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartSchedVendRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  Unique identifier of this Site assigned by the user.  */  
   Plant:string,
      /**  A unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   VendorNum:number,
      /**  Purchase Point  */  
   PurPoint:string,
      /**  Percentage Share of the Purchase Schedule for this Supplier.  Total of all Suppliers for this Part must equal 100 percent.  */  
   PercentShare:number,
      /**  Should the Inspection flag be set when the Purchase Schedule is approved.  */  
   InspNextDelivery:number,
      /**  Purchase order number that uniquely identifies the Contract Purchase Order.  */  
   ContractPONum:number,
      /**  The line number of the detail record on the Contract Purchase Order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   ContractPOLine:number,
      /**  Does the Supplier make deliveries on Monday?  */  
   DeliverMonday:boolean,
      /**  Does the Supplier make deliveries on Tuesday?  */  
   DeliverTuesday:boolean,
      /**  Does the Supplier make deliveries on Wednesday?  */  
   DeliverWednesday:boolean,
      /**  Does the Supplier make deliveries on Thursday?  */  
   DeliverThursday:boolean,
      /**  Does the Supplier make deliveries on Friday?  */  
   DeliverFriday:boolean,
      /**  Does the Supplier make deliveries on Saturday?  */  
   DeliverSaturday:boolean,
      /**  Does the Supplier make deliveries on Sunday?  */  
   DeliverSunday:boolean,
      /**  For development use only.  */  
   DevChar01:string,
      /**  For development use only.  */  
   DevChar02:string,
      /**  For development use only.  */  
   DevChar03:string,
      /**  For development use only.  */  
   DevChar04:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  VendorName  */  
   VendorName:string,
      /**  VendorID  */  
   VendorID:string,
      /**  Indicates if the Supplier is active.  Supplier is inactive if PercentShare is 0.  */  
   IsActive:boolean,
   BitFlag:number,
   PlantName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtPartSchedTableset{
   PartSched:Erp_Tablesets_PartSchedRow[],
   PartSchedVend:Erp_Tablesets_PartSchedVendRow[],
   PartSchedVendPO:Erp_Tablesets_PartSchedVendPORow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ipPartNum
   */  
export interface FindPart_input{
   ipPartNum:string,
}

export interface FindPart_output{
parameters : {
      /**  output parameters  */  
   opPartNum:string,
   opUOM:string,
   opMatchType:string,
}
}

   /** Required : 
      @param partNum
      @param plant
   */  
export interface GetByID_input{
   partNum:string,
   plant:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PartSchedTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PartSchedTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PartSchedTableset[],
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
   returnObj:Erp_Tablesets_PartSchedListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param partNum
      @param plant
      @param vendorNum
      @param purPoint
      @param contractPONum
   */  
export interface GetNewPartSchedVendPO_input{
   ds:Erp_Tablesets_PartSchedTableset[],
   partNum:string,
   plant:string,
   vendorNum:number,
   purPoint:string,
   contractPONum:number,
}

export interface GetNewPartSchedVendPO_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartSchedTableset[],
}
}

   /** Required : 
      @param ds
      @param partNum
      @param plant
      @param vendorNum
   */  
export interface GetNewPartSchedVend_input{
   ds:Erp_Tablesets_PartSchedTableset[],
   partNum:string,
   plant:string,
   vendorNum:number,
}

export interface GetNewPartSchedVend_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartSchedTableset[],
}
}

   /** Required : 
      @param ds
      @param partNum
   */  
export interface GetNewPartSched_input{
   ds:Erp_Tablesets_PartSchedTableset[],
   partNum:string,
}

export interface GetNewPartSched_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartSchedTableset[],
}
}

   /** Required : 
      @param ipRowType
      @param ipRowID
   */  
export interface GetPartFromRowID_input{
   ipRowType:string,
   ipRowID:string,
}

export interface GetPartFromRowID_output{
parameters : {
      /**  output parameters  */  
   opPartNum:string,
   opUOM:string,
}
}

   /** Required : 
      @param partNum
      @param SysRowID
      @param rowType
      @param uomCode
   */  
export interface GetPartXRefInfo_input{
      /**  Proposed PartNumber change  */  
   partNum:string,
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   SysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
      /**  UOM Code (only used for Product Codes)  */  
   uomCode:string,
}

export interface GetPartXRefInfo_output{
parameters : {
      /**  output parameters  */  
   partNum:string,
   uomCode:string,
   serialWarning:string,
   questionString:string,
   multipleMatch:boolean,
}
}

   /** Required : 
      @param whereClausePartSched
      @param whereClausePartSchedVend
      @param whereClausePartSchedVendPO
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePartSched:string,
   whereClausePartSchedVend:string,
   whereClausePartSchedVendPO:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PartSchedTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param BaseDate
      @param DaysToAdd
      @param ProdCalID
   */  
export interface GetValidAndProjectedWorkingDate_input{
   BaseDate:string,
   DaysToAdd:number,
   ProdCalID:string,
}

export interface GetValidAndProjectedWorkingDate_output{
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
      @param ProposedCalendarId
      @param ds
   */  
export interface OnChangeCalendarID_input{
      /**  The proposed CalendarId value  */  
   ProposedCalendarId:string,
   ds:Erp_Tablesets_PartSchedTableset[],
}

export interface OnChangeCalendarID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartSchedTableset[],
}
}

   /** Required : 
      @param proposedInspNextDelivery
      @param ds
   */  
export interface OnChangeInspNextDelivery_input{
      /**  The proposed InspNextDelivery value  */  
   proposedInspNextDelivery:number,
   ds:Erp_Tablesets_PartSchedTableset[],
}

export interface OnChangeInspNextDelivery_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartSchedTableset[],
}
}

   /** Required : 
      @param ipMinDeliveryQty1
      @param ds
   */  
export interface OnChangeMinDeliveryQty1_input{
      /**  The proposed MinDeliveryQty1 value  */  
   ipMinDeliveryQty1:number,
   ds:Erp_Tablesets_PartSchedTableset[],
}

export interface OnChangeMinDeliveryQty1_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartSchedTableset[],
}
}

   /** Required : 
      @param ipMinDeliveryQty2
      @param ds
   */  
export interface OnChangeMinDeliveryQty2_input{
      /**  The proposed MinDeliveryQty2 value  */  
   ipMinDeliveryQty2:number,
   ds:Erp_Tablesets_PartSchedTableset[],
}

export interface OnChangeMinDeliveryQty2_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartSchedTableset[],
}
}

   /** Required : 
      @param ProposedMinForwardSpan
      @param ds
   */  
export interface OnChangeMinForwardSpan_input{
      /**  The proposed MinForwardSpan value  */  
   ProposedMinForwardSpan:number,
   ds:Erp_Tablesets_PartSchedTableset[],
}

export interface OnChangeMinForwardSpan_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartSchedTableset[],
}
}

   /** Required : 
      @param ProposedOrderCover
      @param ds
   */  
export interface OnChangeOrderCover_input{
      /**  The proposed OrderCover value  */  
   ProposedOrderCover:number,
   ds:Erp_Tablesets_PartSchedTableset[],
}

export interface OnChangeOrderCover_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartSchedTableset[],
}
}

   /** Required : 
      @param ProposedPartNum
      @param uomCode
      @param ds
   */  
export interface OnChangePartNum_input{
      /**  The proposed PartNum value  */  
   ProposedPartNum:string,
      /**  UOM Code (only used for Product Codes)  */  
   uomCode:string,
   ds:Erp_Tablesets_PartSchedTableset[],
}

export interface OnChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartSchedTableset[],
}
}

   /** Required : 
      @param ProposedPercentShare
      @param ds
   */  
export interface OnChangePercentShare_input{
      /**  The proposed PercentShare value  */  
   ProposedPercentShare:number,
   ds:Erp_Tablesets_PartSchedTableset[],
}

export interface OnChangePercentShare_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartSchedTableset[],
}
}

   /** Required : 
      @param ProposedPeriodShift
      @param ds
   */  
export interface OnChangePeriodShift_input{
      /**  The proposed PeriodShift value  */  
   ProposedPeriodShift:number,
   ds:Erp_Tablesets_PartSchedTableset[],
}

export interface OnChangePeriodShift_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartSchedTableset[],
}
}

   /** Required : 
      @param ProposedPeriodicityCode1
      @param ds
   */  
export interface OnChangePeriodicityCode1_input{
      /**  The proposed PeriodicityCode1 value  */  
   ProposedPeriodicityCode1:number,
   ds:Erp_Tablesets_PartSchedTableset[],
}

export interface OnChangePeriodicityCode1_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartSchedTableset[],
}
}

   /** Required : 
      @param proposedPeriodicityCode2
      @param ds
   */  
export interface OnChangePeriodicityCode2_input{
      /**  The proposed PeriodicityCode2 value  */  
   proposedPeriodicityCode2:number,
   ds:Erp_Tablesets_PartSchedTableset[],
}

export interface OnChangePeriodicityCode2_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartSchedTableset[],
}
}

   /** Required : 
      @param ProposedPrintLength
      @param ds
   */  
export interface OnChangePrintLength_input{
      /**  The proposed PrintLength value  */  
   ProposedPrintLength:number,
   ds:Erp_Tablesets_PartSchedTableset[],
}

export interface OnChangePrintLength_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartSchedTableset[],
}
}

   /** Required : 
      @param ProposedPurPoint
      @param ds
   */  
export interface OnChangePurPoint_input{
      /**  The proposed Purchase Point value  */  
   ProposedPurPoint:string,
   ds:Erp_Tablesets_PartSchedTableset[],
}

export interface OnChangePurPoint_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartSchedTableset[],
}
}

   /** Required : 
      @param proposedScheduleFirm
      @param ds
   */  
export interface OnChangeScheduleFirm_input{
      /**  The proposed ScheduleFirm value  */  
   proposedScheduleFirm:number,
   ds:Erp_Tablesets_PartSchedTableset[],
}

export interface OnChangeScheduleFirm_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartSchedTableset[],
}
}

   /** Required : 
      @param ProposedScheduleLength
      @param ds
   */  
export interface OnChangeScheduleLength_input{
      /**  The proposed ScheduleLength value  */  
   ProposedScheduleLength:number,
   ds:Erp_Tablesets_PartSchedTableset[],
}

export interface OnChangeScheduleLength_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartSchedTableset[],
}
}

   /** Required : 
      @param ProposedVendorID
      @param ds
   */  
export interface OnChangeVendorID_input{
      /**  The proposed VendorId value  */  
   ProposedVendorID:string,
   ds:Erp_Tablesets_PartSchedTableset[],
}

export interface OnChangeVendorID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartSchedTableset[],
}
}

   /** Required : 
      @param ProposedVendorNum
      @param ds
   */  
export interface OnChangeVendorNum_input{
      /**  The proposed VendorNum value  */  
   ProposedVendorNum:number,
   ds:Erp_Tablesets_PartSchedTableset[],
}

export interface OnChangeVendorNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartSchedTableset[],
}
}

   /** Required : 
      @param company
      @param plant
      @param partNum
   */  
export interface PartPlantIsLinkedToContract_input{
   company:string,
   plant:string,
   partNum:string,
}

export interface PartPlantIsLinkedToContract_output{
   returnObj:boolean,
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPartSchedTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPartSchedTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PartSchedTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartSchedTableset[],
}
}

