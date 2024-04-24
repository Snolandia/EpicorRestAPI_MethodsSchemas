import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ServiceContractSvc
// Description: Service Contract Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/$metadata", {
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
   Description: Get ServiceContracts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ServiceContracts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSContHdRow
   */  
export function get_ServiceContracts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContHdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ServiceContracts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContHdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ServiceContracts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSContHdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSContHdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ServiceContracts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ServiceContracts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ServiceContract item
   Description: Calls GetByID to retrieve the ServiceContract item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ServiceContract
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSContHdRow
   */  
export function get_ServiceContracts_Company_ContractNum(Company:string, ContractNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FSContHdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ServiceContracts(" + Company + "," + ContractNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FSContHdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ServiceContract for the service
   Description: Calls UpdateExt to update ServiceContract. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ServiceContract
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSContHdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ServiceContracts_Company_ContractNum(Company:string, ContractNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ServiceContracts(" + Company + "," + ContractNum + ")", {
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
   Summary: Call UpdateExt to delete ServiceContract item
   Description: Call UpdateExt to delete ServiceContract item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ServiceContract
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ServiceContracts_Company_ContractNum(Company:string, ContractNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ServiceContracts(" + Company + "," + ContractNum + ")", {
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
   Description: Get FSContDts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FSContDts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSContDtRow
   */  
export function get_ServiceContracts_Company_ContractNum_FSContDts(Company:string, ContractNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContDtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ServiceContracts(" + Company + "," + ContractNum + ")/FSContDts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContDtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FSContDt item
   Description: Calls GetByID to retrieve the FSContDt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSContDt1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param ContractLine Desc: ContractLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSContDtRow
   */  
export function get_ServiceContracts_Company_ContractNum_FSContDts_Company_ContractNum_ContractLine(Company:string, ContractNum:string, ContractLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FSContDtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ServiceContracts(" + Company + "," + ContractNum + ")/FSContDts(" + Company + "," + ContractNum + "," + ContractLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FSContDtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get FSRenewals items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FSRenewals1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSRenewalRow
   */  
export function get_ServiceContracts_Company_ContractNum_FSRenewals(Company:string, ContractNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSRenewalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ServiceContracts(" + Company + "," + ContractNum + ")/FSRenewals", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSRenewalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FSRenewal item
   Description: Calls GetByID to retrieve the FSRenewal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSRenewal1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param RenewalNbr Desc: RenewalNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSRenewalRow
   */  
export function get_ServiceContracts_Company_ContractNum_FSRenewals_Company_ContractNum_RenewalNbr(Company:string, ContractNum:string, RenewalNbr:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FSRenewalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ServiceContracts(" + Company + "," + ContractNum + ")/FSRenewals(" + Company + "," + ContractNum + "," + RenewalNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FSRenewalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get FSContLabExpRates items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FSContLabExpRates1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSContLabExpRateRow
   */  
export function get_ServiceContracts_Company_ContractNum_FSContLabExpRates(Company:string, ContractNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContLabExpRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ServiceContracts(" + Company + "," + ContractNum + ")/FSContLabExpRates", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContLabExpRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FSContLabExpRate item
   Description: Calls GetByID to retrieve the FSContLabExpRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSContLabExpRate1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param ExpenseCode Desc: ExpenseCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSContLabExpRateRow
   */  
export function get_ServiceContracts_Company_ContractNum_FSContLabExpRates_Company_ContractNum_ExpenseCode(Company:string, ContractNum:string, ExpenseCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FSContLabExpRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ServiceContracts(" + Company + "," + ContractNum + ")/FSContLabExpRates(" + Company + "," + ContractNum + "," + ExpenseCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FSContLabExpRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get FSContDts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FSContDts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSContDtRow
   */  
export function get_FSContDts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContDtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContDts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContDtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FSContDts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSContDtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSContDtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FSContDts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContDts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FSContDt item
   Description: Calls GetByID to retrieve the FSContDt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSContDt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param ContractLine Desc: ContractLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSContDtRow
   */  
export function get_FSContDts_Company_ContractNum_ContractLine(Company:string, ContractNum:string, ContractLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FSContDtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContDts(" + Company + "," + ContractNum + "," + ContractLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FSContDtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FSContDt for the service
   Description: Calls UpdateExt to update FSContDt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FSContDt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param ContractLine Desc: ContractLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSContDtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FSContDts_Company_ContractNum_ContractLine(Company:string, ContractNum:string, ContractLine:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContDts(" + Company + "," + ContractNum + "," + ContractLine + ")", {
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
   Summary: Call UpdateExt to delete FSContDt item
   Description: Call UpdateExt to delete FSContDt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FSContDt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param ContractLine Desc: ContractLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FSContDts_Company_ContractNum_ContractLine(Company:string, ContractNum:string, ContractLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContDts(" + Company + "," + ContractNum + "," + ContractLine + ")", {
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
   Description: Get FSContSNs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FSContSNs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param ContractLine Desc: ContractLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSContSNRow
   */  
export function get_FSContDts_Company_ContractNum_ContractLine_FSContSNs(Company:string, ContractNum:string, ContractLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContSNRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContDts(" + Company + "," + ContractNum + "," + ContractLine + ")/FSContSNs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContSNRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FSContSN item
   Description: Calls GetByID to retrieve the FSContSN item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSContSN1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param ContractLine Desc: ContractLine   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSContSNRow
   */  
export function get_FSContDts_Company_ContractNum_ContractLine_FSContSNs_Company_ContractNum_ContractLine_PartNum_SerialNumber(Company:string, ContractNum:string, ContractLine:string, PartNum:string, SerialNumber:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FSContSNRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContDts(" + Company + "," + ContractNum + "," + ContractLine + ")/FSContSNs(" + Company + "," + ContractNum + "," + ContractLine + "," + PartNum + "," + SerialNumber + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FSContSNRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get FSContSNs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FSContSNs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSContSNRow
   */  
export function get_FSContSNs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContSNRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContSNs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContSNRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FSContSNs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSContSNRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSContSNRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FSContSNs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContSNs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FSContSN item
   Description: Calls GetByID to retrieve the FSContSN item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSContSN
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param ContractLine Desc: ContractLine   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSContSNRow
   */  
export function get_FSContSNs_Company_ContractNum_ContractLine_PartNum_SerialNumber(Company:string, ContractNum:string, ContractLine:string, PartNum:string, SerialNumber:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FSContSNRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContSNs(" + Company + "," + ContractNum + "," + ContractLine + "," + PartNum + "," + SerialNumber + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FSContSNRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FSContSN for the service
   Description: Calls UpdateExt to update FSContSN. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FSContSN
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param ContractLine Desc: ContractLine   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSContSNRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FSContSNs_Company_ContractNum_ContractLine_PartNum_SerialNumber(Company:string, ContractNum:string, ContractLine:string, PartNum:string, SerialNumber:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContSNs(" + Company + "," + ContractNum + "," + ContractLine + "," + PartNum + "," + SerialNumber + ")", {
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
   Summary: Call UpdateExt to delete FSContSN item
   Description: Call UpdateExt to delete FSContSN item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FSContSN
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param ContractLine Desc: ContractLine   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FSContSNs_Company_ContractNum_ContractLine_PartNum_SerialNumber(Company:string, ContractNum:string, ContractLine:string, PartNum:string, SerialNumber:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContSNs(" + Company + "," + ContractNum + "," + ContractLine + "," + PartNum + "," + SerialNumber + ")", {
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
   Description: Get FSRenewals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FSRenewals
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSRenewalRow
   */  
export function get_FSRenewals(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSRenewalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewals", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSRenewalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FSRenewals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSRenewalRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSRenewalRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FSRenewals(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewals", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FSRenewal item
   Description: Calls GetByID to retrieve the FSRenewal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSRenewal
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param RenewalNbr Desc: RenewalNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSRenewalRow
   */  
export function get_FSRenewals_Company_ContractNum_RenewalNbr(Company:string, ContractNum:string, RenewalNbr:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FSRenewalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewals(" + Company + "," + ContractNum + "," + RenewalNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FSRenewalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FSRenewal for the service
   Description: Calls UpdateExt to update FSRenewal. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FSRenewal
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param RenewalNbr Desc: RenewalNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSRenewalRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FSRenewals_Company_ContractNum_RenewalNbr(Company:string, ContractNum:string, RenewalNbr:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewals(" + Company + "," + ContractNum + "," + RenewalNbr + ")", {
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
   Summary: Call UpdateExt to delete FSRenewal item
   Description: Call UpdateExt to delete FSRenewal item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FSRenewal
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param RenewalNbr Desc: RenewalNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FSRenewals_Company_ContractNum_RenewalNbr(Company:string, ContractNum:string, RenewalNbr:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewals(" + Company + "," + ContractNum + "," + RenewalNbr + ")", {
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
   Description: Get FSRenewalDts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FSRenewalDts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param RenewalNbr Desc: RenewalNbr   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSRenewalDtRow
   */  
export function get_FSRenewals_Company_ContractNum_RenewalNbr_FSRenewalDts(Company:string, ContractNum:string, RenewalNbr:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSRenewalDtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewals(" + Company + "," + ContractNum + "," + RenewalNbr + ")/FSRenewalDts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSRenewalDtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FSRenewalDt item
   Description: Calls GetByID to retrieve the FSRenewalDt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSRenewalDt1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param RenewalNbr Desc: RenewalNbr   Required: True
      @param RenewalLine Desc: RenewalLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSRenewalDtRow
   */  
export function get_FSRenewals_Company_ContractNum_RenewalNbr_FSRenewalDts_Company_ContractNum_RenewalNbr_RenewalLine(Company:string, ContractNum:string, RenewalNbr:string, RenewalLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FSRenewalDtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewals(" + Company + "," + ContractNum + "," + RenewalNbr + ")/FSRenewalDts(" + Company + "," + ContractNum + "," + RenewalNbr + "," + RenewalLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FSRenewalDtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get FSRenewalDts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FSRenewalDts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSRenewalDtRow
   */  
export function get_FSRenewalDts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSRenewalDtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewalDts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSRenewalDtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FSRenewalDts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSRenewalDtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSRenewalDtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FSRenewalDts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewalDts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FSRenewalDt item
   Description: Calls GetByID to retrieve the FSRenewalDt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSRenewalDt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param RenewalNbr Desc: RenewalNbr   Required: True
      @param RenewalLine Desc: RenewalLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSRenewalDtRow
   */  
export function get_FSRenewalDts_Company_ContractNum_RenewalNbr_RenewalLine(Company:string, ContractNum:string, RenewalNbr:string, RenewalLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FSRenewalDtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewalDts(" + Company + "," + ContractNum + "," + RenewalNbr + "," + RenewalLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FSRenewalDtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FSRenewalDt for the service
   Description: Calls UpdateExt to update FSRenewalDt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FSRenewalDt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param RenewalNbr Desc: RenewalNbr   Required: True
      @param RenewalLine Desc: RenewalLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSRenewalDtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FSRenewalDts_Company_ContractNum_RenewalNbr_RenewalLine(Company:string, ContractNum:string, RenewalNbr:string, RenewalLine:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewalDts(" + Company + "," + ContractNum + "," + RenewalNbr + "," + RenewalLine + ")", {
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
   Summary: Call UpdateExt to delete FSRenewalDt item
   Description: Call UpdateExt to delete FSRenewalDt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FSRenewalDt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param RenewalNbr Desc: RenewalNbr   Required: True
      @param RenewalLine Desc: RenewalLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FSRenewalDts_Company_ContractNum_RenewalNbr_RenewalLine(Company:string, ContractNum:string, RenewalNbr:string, RenewalLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewalDts(" + Company + "," + ContractNum + "," + RenewalNbr + "," + RenewalLine + ")", {
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
   Description: Get FSRenewalSNs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FSRenewalSNs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param RenewalNbr Desc: RenewalNbr   Required: True
      @param RenewalLine Desc: RenewalLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSRenewalSNRow
   */  
export function get_FSRenewalDts_Company_ContractNum_RenewalNbr_RenewalLine_FSRenewalSNs(Company:string, ContractNum:string, RenewalNbr:string, RenewalLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSRenewalSNRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewalDts(" + Company + "," + ContractNum + "," + RenewalNbr + "," + RenewalLine + ")/FSRenewalSNs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSRenewalSNRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FSRenewalSN item
   Description: Calls GetByID to retrieve the FSRenewalSN item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSRenewalSN1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param RenewalNbr Desc: RenewalNbr   Required: True
      @param RenewalLine Desc: RenewalLine   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSRenewalSNRow
   */  
export function get_FSRenewalDts_Company_ContractNum_RenewalNbr_RenewalLine_FSRenewalSNs_Company_ContractNum_RenewalNbr_RenewalLine_PartNum_SerialNumber(Company:string, ContractNum:string, RenewalNbr:string, RenewalLine:string, PartNum:string, SerialNumber:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FSRenewalSNRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewalDts(" + Company + "," + ContractNum + "," + RenewalNbr + "," + RenewalLine + ")/FSRenewalSNs(" + Company + "," + ContractNum + "," + RenewalNbr + "," + RenewalLine + "," + PartNum + "," + SerialNumber + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FSRenewalSNRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get FSRenewalSNs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FSRenewalSNs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSRenewalSNRow
   */  
export function get_FSRenewalSNs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSRenewalSNRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewalSNs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSRenewalSNRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FSRenewalSNs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSRenewalSNRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSRenewalSNRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FSRenewalSNs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewalSNs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FSRenewalSN item
   Description: Calls GetByID to retrieve the FSRenewalSN item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSRenewalSN
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param RenewalNbr Desc: RenewalNbr   Required: True
      @param RenewalLine Desc: RenewalLine   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSRenewalSNRow
   */  
export function get_FSRenewalSNs_Company_ContractNum_RenewalNbr_RenewalLine_PartNum_SerialNumber(Company:string, ContractNum:string, RenewalNbr:string, RenewalLine:string, PartNum:string, SerialNumber:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FSRenewalSNRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewalSNs(" + Company + "," + ContractNum + "," + RenewalNbr + "," + RenewalLine + "," + PartNum + "," + SerialNumber + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FSRenewalSNRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FSRenewalSN for the service
   Description: Calls UpdateExt to update FSRenewalSN. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FSRenewalSN
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param RenewalNbr Desc: RenewalNbr   Required: True
      @param RenewalLine Desc: RenewalLine   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSRenewalSNRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FSRenewalSNs_Company_ContractNum_RenewalNbr_RenewalLine_PartNum_SerialNumber(Company:string, ContractNum:string, RenewalNbr:string, RenewalLine:string, PartNum:string, SerialNumber:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewalSNs(" + Company + "," + ContractNum + "," + RenewalNbr + "," + RenewalLine + "," + PartNum + "," + SerialNumber + ")", {
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
   Summary: Call UpdateExt to delete FSRenewalSN item
   Description: Call UpdateExt to delete FSRenewalSN item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FSRenewalSN
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param RenewalNbr Desc: RenewalNbr   Required: True
      @param RenewalLine Desc: RenewalLine   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FSRenewalSNs_Company_ContractNum_RenewalNbr_RenewalLine_PartNum_SerialNumber(Company:string, ContractNum:string, RenewalNbr:string, RenewalLine:string, PartNum:string, SerialNumber:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSRenewalSNs(" + Company + "," + ContractNum + "," + RenewalNbr + "," + RenewalLine + "," + PartNum + "," + SerialNumber + ")", {
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
   Description: Get FSContLabExpRates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FSContLabExpRates
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSContLabExpRateRow
   */  
export function get_FSContLabExpRates(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContLabExpRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContLabExpRates", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContLabExpRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FSContLabExpRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSContLabExpRateRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSContLabExpRateRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FSContLabExpRates(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContLabExpRates", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FSContLabExpRate item
   Description: Calls GetByID to retrieve the FSContLabExpRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSContLabExpRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param ExpenseCode Desc: ExpenseCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSContLabExpRateRow
   */  
export function get_FSContLabExpRates_Company_ContractNum_ExpenseCode(Company:string, ContractNum:string, ExpenseCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FSContLabExpRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContLabExpRates(" + Company + "," + ContractNum + "," + ExpenseCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FSContLabExpRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FSContLabExpRate for the service
   Description: Calls UpdateExt to update FSContLabExpRate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FSContLabExpRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param ExpenseCode Desc: ExpenseCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSContLabExpRateRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FSContLabExpRates_Company_ContractNum_ExpenseCode(Company:string, ContractNum:string, ExpenseCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContLabExpRates(" + Company + "," + ContractNum + "," + ExpenseCode + ")", {
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
   Summary: Call UpdateExt to delete FSContLabExpRate item
   Description: Call UpdateExt to delete FSContLabExpRate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FSContLabExpRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractNum Desc: ContractNum   Required: True
      @param ExpenseCode Desc: ExpenseCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FSContLabExpRates_Company_ContractNum_ExpenseCode(Company:string, ContractNum:string, ExpenseCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContLabExpRates(" + Company + "," + ContractNum + "," + ExpenseCode + ")", {
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
   Description: Get FSContOrderDtlLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FSContOrderDtlLists
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSContOrderDtlListRow
   */  
export function get_FSContOrderDtlLists(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContOrderDtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContOrderDtlLists", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContOrderDtlListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FSContOrderDtlLists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSContOrderDtlListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSContOrderDtlListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FSContOrderDtlLists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContOrderDtlLists", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FSContOrderDtlList item
   Description: Calls GetByID to retrieve the FSContOrderDtlList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSContOrderDtlList
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSContOrderDtlListRow
   */  
export function get_FSContOrderDtlLists_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FSContOrderDtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContOrderDtlLists(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FSContOrderDtlListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FSContOrderDtlList for the service
   Description: Calls UpdateExt to update FSContOrderDtlList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FSContOrderDtlList
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSContOrderDtlListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FSContOrderDtlLists_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContOrderDtlLists(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete FSContOrderDtlList item
   Description: Call UpdateExt to delete FSContOrderDtlList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FSContOrderDtlList
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FSContOrderDtlLists_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FSContOrderDtlLists(" + SysRowID + ")", {
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
   Description: Get SelectedSerialNumbers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SelectedSerialNumbers
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SelectedSerialNumbersRow
   */  
export function get_SelectedSerialNumbers(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/SelectedSerialNumbers", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectedSerialNumbers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/SelectedSerialNumbers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the SelectedSerialNumber item
   Description: Calls GetByID to retrieve the SelectedSerialNumber item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SelectedSerialNumber
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   */  
export function get_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company:string, PartNum:string, SerialNumber:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SelectedSerialNumbersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SelectedSerialNumbersRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SelectedSerialNumber for the service
   Description: Calls UpdateExt to update SelectedSerialNumber. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SelectedSerialNumber
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company:string, PartNum:string, SerialNumber:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
   Summary: Call UpdateExt to delete SelectedSerialNumber item
   Description: Call UpdateExt to delete SelectedSerialNumber item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SelectedSerialNumber
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company:string, PartNum:string, SerialNumber:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
   Description: Get SNFormats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SNFormats
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SNFormatRow
   */  
export function get_SNFormats(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/SNFormats", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SNFormats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SNFormats(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/SNFormats", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the SNFormat item
   Description: Calls GetByID to retrieve the SNFormat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SNFormat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   */  
export function get_SNFormats_Company_PartNum_Plant(Company:string, PartNum:string, Plant:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SNFormatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SNFormatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SNFormat for the service
   Description: Calls UpdateExt to update SNFormat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SNFormat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SNFormats_Company_PartNum_Plant(Company:string, PartNum:string, Plant:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
   Summary: Call UpdateExt to delete SNFormat item
   Description: Call UpdateExt to delete SNFormat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SNFormat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SNFormats_Company_PartNum_Plant(Company:string, PartNum:string, Plant:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSContHdListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContHdListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContHdListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseFSContHd:string, whereClauseFSContDt:string, whereClauseFSContSN:string, whereClauseFSRenewal:string, whereClauseFSRenewalDt:string, whereClauseFSRenewalSN:string, whereClauseFSContLabExpRate:string, whereClauseFSContOrderDtlList:string, whereClauseSelectedSerialNumbers:string, whereClauseSNFormat:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseFSContHd!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFSContHd=" + whereClauseFSContHd
   }
   if(typeof whereClauseFSContDt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFSContDt=" + whereClauseFSContDt
   }
   if(typeof whereClauseFSContSN!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFSContSN=" + whereClauseFSContSN
   }
   if(typeof whereClauseFSRenewal!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFSRenewal=" + whereClauseFSRenewal
   }
   if(typeof whereClauseFSRenewalDt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFSRenewalDt=" + whereClauseFSRenewalDt
   }
   if(typeof whereClauseFSRenewalSN!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFSRenewalSN=" + whereClauseFSRenewalSN
   }
   if(typeof whereClauseFSContLabExpRate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFSContLabExpRate=" + whereClauseFSContLabExpRate
   }
   if(typeof whereClauseFSContOrderDtlList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFSContOrderDtlList=" + whereClauseFSContOrderDtlList
   }
   if(typeof whereClauseSelectedSerialNumbers!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSelectedSerialNumbers=" + whereClauseSelectedSerialNumbers
   }
   if(typeof whereClauseSNFormat!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSNFormat=" + whereClauseSNFormat
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GetRows" + params, {
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
export function get_GetByID(contractNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof contractNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "contractNum=" + contractNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GetList" + params, {
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
   Summary: Invoke method ActivateContract
   Description: Method to call when activating the contract.
   OperationID: ActivateContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ActivateContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ActivateContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ActivateContract(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ActivateContract", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContDtBillEndDate
   Description: Method to call when changing the billing end date on the contract detail record.
Updates FSContDt with values based on the new billing start date.
   OperationID: ChangeFSContDtBillEndDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContDtBillEndDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContDtBillEndDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContDtBillEndDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContDtBillEndDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContDtBillStartDate
   Description: Method to call when changing the billing start date on the contract detail record.
Updates FSContDt with values based on the new billing start date.
   OperationID: ChangeFSContDtBillStartDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContDtBillStartDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContDtBillStartDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContDtBillStartDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContDtBillStartDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContDtContractQty
   Description: Method to call when changing the contract quantity on the contract detail record.
Recalculates Ext Prices on FSContDt with values from the new quantity.
   OperationID: ChangeFSContDtContractQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContDtContractQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContDtContractQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContDtContractQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContDtContractQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContDtOrderLine
   Description: Method to call when changing the order line on the contract detail record.
Validates the line and updates FSContDt with values from the order line.
   OperationID: ChangeFSContDtOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContDtOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContDtOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContDtOrderLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContDtOrderLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContDtOrderNum
   Description: Method to call when changing the order number on the contract detail record.
Validates the number and updates FSContDt with values from the order.
   OperationID: ChangeFSContDtOrderNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContDtOrderNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContDtOrderNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContDtOrderNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContDtOrderNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContDtPartNumWithSubs
   Description: Method to call when changing the part number on the contract detail record.
Updates FSContDt with values from the part number. If substitute PartNum is provided,
it will use the substitute part instead of the proposed part.
Prior to calling this method, the CheckPartNumChange method should be run
to validate the part.
   OperationID: ChangeFSContDtPartNumWithSubs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContDtPartNumWithSubs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContDtPartNumWithSubs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContDtPartNumWithSubs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContDtPartNumWithSubs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContDtPartNum
   Description: Method to call when changing the part number on the contract detail record.
Updates FSContDt with values from the part number.
Prior to calling this method, the CheckPartNumChange method should be run
to validate the part.
   OperationID: ChangeFSContDtPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContDtPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContDtPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContDtPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContDtPartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContDtPricePerUnit
   Description: Method to call when changing the price per unit on the contract detail record.
Recalculates Ext Prices on FSContDt with values from the new price per unit.
   OperationID: ChangeFSContDtPricePerUnit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContDtPricePerUnit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContDtPricePerUnit_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContDtPricePerUnit(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContDtPricePerUnit", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContDtProdCode
   Description: Method to call when changing the product code on the contract detail record.
Validates the code and updates FSContDt with values from the product code.
   OperationID: ChangeFSContDtProdCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContDtProdCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContDtProdCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContDtProdCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContDtProdCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContDtProjectID
   Description: Method to call when changing the project id on the contract detail record.
Validates the id and updates FSContDt with values from the project.
   OperationID: ChangeFSContDtProjectID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContDtProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContDtProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContDtProjectID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContDtProjectID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContDtXPartNum
   Description: Method to call when changing the customer part number (XPartNum) on the
contract detail record.
Updates FSContDt with values from the customer part.
   OperationID: ChangeFSContDtXPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContDtXPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContDtXPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContDtXPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContDtXPartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContHdActiveDate
   Description: Method to call when changing the effective date on the contract header record.
Updates FSContHd with values based on the new effective date.
   OperationID: ChangeFSContHdActiveDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdActiveDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdActiveDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContHdActiveDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContHdActiveDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContHdBTCusNum
   Description: Method to call when changing the customer id on the contract header record.
Validates the customer id and updates FSContHd with values from the customer.
   OperationID: ChangeFSContHdBTCusNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdBTCusNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdBTCusNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContHdBTCusNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContHdBTCusNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContHdContractCode
   Description: Method to call when changing the contract code on the contract header record.
Validates the code and updates FSContHd with values from the contract.
   OperationID: ChangeFSContHdContractCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdContractCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdContractCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContHdContractCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContHdContractCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContHdCurrencyCode
   Description: Method to call when changing the currency code on the contract header record.
Validates the code and updates FSContHd with values from the currency.
   OperationID: ChangeFSContHdCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContHdCurrencyCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContHdCurrencyCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContHdCustID
   Description: Method to call when changing the customer id on the contract header record.
Validates the customer id and updates FSContHd with values from the customer.
   OperationID: ChangeFSContHdCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContHdCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContHdCustID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContHdDeferredRev
   Description: Method to call when changing the Deferred Revenue flag on the contract header record.
   OperationID: ChangeFSContHdDeferredRev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdDeferredRev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdDeferredRev_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContHdDeferredRev(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContHdDeferredRev", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContHdDuration
   Description: Method to call when changing the duration on the contract header record.
Updates FSContHd with values based on the new duration.
   OperationID: ChangeFSContHdDuration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdDuration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdDuration_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContHdDuration(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContHdDuration", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContHdFiscalCalendarID
   Description: Method to call when changing the Fiscal Calendar on the contract header record.
   OperationID: ChangeFSContHdFiscalCalendarID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdFiscalCalendarID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdFiscalCalendarID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContHdFiscalCalendarID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContHdFiscalCalendarID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContHdModifier
   Description: Method to call when changing the Modifier on the contract header record.
Updates FSContHd with values based on the new Modifier.
   OperationID: ChangeFSContHdModifier
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdModifier_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdModifier_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContHdModifier(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContHdModifier", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContHdPrcConNum
   Description: Method to call when changing the customer contact number on the contract header record.
Validates the number and updates FSContHd with values from the contact.
   OperationID: ChangeFSContHdPrcConNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdPrcConNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdPrcConNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContHdPrcConNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContHdPrcConNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContHdPricePer
   Description: Method to call when changing the PricePer on the contract header record.
Updates FSContHd with values based on the new PricePer.
   OperationID: ChangeFSContHdPricePer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdPricePer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdPricePer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContHdPricePer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContHdPricePer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContHdQuotedContract
   Description: Method to call when changing the Quoted Contract flag on the contract header record.
   OperationID: ChangeFSContHdQuotedContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdQuotedContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdQuotedContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContHdQuotedContract(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContHdQuotedContract", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContHdRACode
   Description: Method to call when changing the RACode on the contract header record.
   OperationID: ChangeFSContHdRACode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdRACode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdRACode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContHdRACode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContHdRACode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContHdRecurringFreq
   Description: Method to call when changing the RecurringFreq on the contract header record.
Updates FSContHd with values based on the new RecurringFreq.
   OperationID: ChangeFSContHdRecurringFreq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdRecurringFreq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdRecurringFreq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContHdRecurringFreq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContHdRecurringFreq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContHdShipToCustID
   Description: Method to call when changing the ShipTo Customer ID on the contract header record.
Validates the ShipTo Customer ID and updates FSContHd with values from the customer.
   OperationID: ChangeFSContHdShipToCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdShipToCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdShipToCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContHdShipToCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContHdShipToCustID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContHdShipToNum
   Description: Method to call when changing the ship to on the contract header record.
Validates the number and updates FSContHd with values from the ship to.
   OperationID: ChangeFSContHdShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContHdShipToNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContHdShipToNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContHdShpConNum
   Description: Method to call when changing the ship to contact on the contract header record.
Validates the contact and updates FSContHd with values from the ship to contact.
   OperationID: ChangeFSContHdShpConNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdShpConNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdShpConNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContHdShpConNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContHdShpConNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContHdSuspended
   Description: Method to call when changing the Suspended flag on the contract header record.
This method determines if the contract has outstanding invoice revenue amortization
schedules that need to be updated to be put on hold or not. If InvcDtlRASch records
exist then a message will be returned to the user to let the user decide whether to
continue the update of invoice revenue schedules or not. The FSContHd.Suspended is
updated right away if no related invoice schedule exists.
   OperationID: ChangeFSContHdSuspended
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdSuspended_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdSuspended_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContHdSuspended(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContHdSuspended", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContHdTaskSetID
   Description: Method to call when changing the Task Set ID on the contract header record.
   OperationID: ChangeFSContHdTaskSetID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdTaskSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdTaskSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContHdTaskSetID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContHdTaskSetID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContHdTaxCatID
   Description: Method to call when changing the tax category id on the contract header record.
Validates the id and updates FSContHd with values from the tax category.
   OperationID: ChangeFSContHdTaxCatID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdTaxCatID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdTaxCatID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContHdTaxCatID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContHdTaxCatID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContHdRecurringInv
   Description: Method to call when changing the recurring invoice flag on the contract header record.
   OperationID: ChangeFSContHdRecurringInv
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHdRecurringInv_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHdRecurringInv_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContHdRecurringInv(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContHdRecurringInv", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSContHDUseOTS
   Description: Method to call when changing the UseOTS field the contract header record.
Refreshes the address list and contact info
   OperationID: ChangeFSContHDUseOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSContHDUseOTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSContHDUseOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSContHDUseOTS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSContHDUseOTS", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalContractCode
   Description: Method to call when changing the contract code on the contract renewal header record.
Validates the code and updates FSRenewal with values from the contract code defaults.
   OperationID: ChangeFSRenewalContractCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalContractCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalContractCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalContractCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalContractCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalDeferredRev
   Description: Method to call when changing the Deferred Revenue flag on the contract renewal header record.
   OperationID: ChangeFSRenewalDeferredRev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDeferredRev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDeferredRev_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalDeferredRev(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalDeferredRev", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalDtBillEndDate
   Description: Method to call when changing the billing end date on the contract renewal detail record.
Updates FSRenewalDt with values based on the new billing start date.
   OperationID: ChangeFSRenewalDtBillEndDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDtBillEndDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDtBillEndDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalDtBillEndDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalDtBillEndDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalDtBillStartDate
   Description: Method to call when changing the billing start date on the contract renewal detail record.
Updates FSRenewalDt with values based on the new billing start date.
   OperationID: ChangeFSRenewalDtBillStartDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDtBillStartDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDtBillStartDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalDtBillStartDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalDtBillStartDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalDtContractQty
   Description: Method to call when changing the contract quantity on the contract renewal detail record.
Recalculates Ext Prices on FSRenewalDt with values from the new quantity.
   OperationID: ChangeFSRenewalDtContractQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDtContractQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDtContractQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalDtContractQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalDtContractQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalDtIncreasePct
   Description: Method to call when changing the increase percent on the contract renewal detail record.
Recalculates Prices on FSRenewalDt with values from the new increase percent.
   OperationID: ChangeFSRenewalDtIncreasePct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDtIncreasePct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDtIncreasePct_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalDtIncreasePct(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalDtIncreasePct", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalDtOrderLine
   Description: Method to call when changing the order line on the contract renewal detail record.
Validates the line and updates FSRenewalDt with values from the order line.
   OperationID: ChangeFSRenewalDtOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDtOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDtOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalDtOrderLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalDtOrderLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalDtOrderNum
   Description: Method to call when changing the order number on the contract renewal detail record.
Validates the number and updates FSRenewalDt with values from the order.
   OperationID: ChangeFSRenewalDtOrderNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDtOrderNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDtOrderNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalDtOrderNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalDtOrderNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalDtPartNum
   Description: Method to call when changing the part number on the contract renewal detail record.
Updates FSRenewalDt with values from the part number.
Prior to calling this method, the CheckPartNumChange method should be run
to validate the part.
   OperationID: ChangeFSRenewalDtPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDtPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDtPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalDtPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalDtPartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalDtPartNumWithSubs
   Description: Method to call when changing the part number on the contract renewal detail record.
Updates FSRenewalDt with values from the part number.
Prior to calling this method, the CheckPartNumChange method should be run
to validate the part.
   OperationID: ChangeFSRenewalDtPartNumWithSubs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDtPartNumWithSubs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDtPartNumWithSubs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalDtPartNumWithSubs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalDtPartNumWithSubs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalDtPricePerUnit
   Description: Method to call when changing the price per unit on the contract renewal detail record.
Recalculates Ext Prices on FSRenewalDt with values from the new price per unit.
   OperationID: ChangeFSRenewalDtPricePerUnit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDtPricePerUnit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDtPricePerUnit_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalDtPricePerUnit(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalDtPricePerUnit", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalDtProdCode
   Description: Method to call when changing the product code on the contract renewal detail record.
Validates the code and updates FSRenewalDt with values from the product code.
   OperationID: ChangeFSRenewalDtProdCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDtProdCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDtProdCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalDtProdCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalDtProdCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalDtProjectID
   Description: Method to call when changing the project id on the contract renewal detail record.
Validates the id and updates FSRenewalDt with values from the project.
   OperationID: ChangeFSRenewalDtProjectID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDtProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDtProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalDtProjectID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalDtProjectID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalDtXPartNum
   Description: Method to call when changing the customer part number (XPartNum) on the
contract renewal detail record.
Updates FSRenewalDt with values from the customer part.
   OperationID: ChangeFSRenewalDtXPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDtXPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDtXPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalDtXPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalDtXPartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalDuration
   Description: Method to call when changing the duration on the contract renewal header record.
Updates FSRenewal with values based on the new duration.
   OperationID: ChangeFSRenewalDuration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalDuration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalDuration_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalDuration(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalDuration", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalFiscalCalendarID
   Description: Method to call when changing the Fiscal Calendar on the contract renewal header record.
   OperationID: ChangeFSRenewalFiscalCalendarID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalFiscalCalendarID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalFiscalCalendarID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalFiscalCalendarID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalFiscalCalendarID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalModifier
   Description: Method to call when changing the Modifier on the contract renewal header record.
Updates FSRenewal with values based on the new Modifier.
   OperationID: ChangeFSRenewalModifier
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalModifier_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalModifier_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalModifier(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalModifier", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalPricePer
   Description: Method to call when changing the PricePer on the contract renewal header record.
Updates FSRenewal with values based on the new PricePer.
   OperationID: ChangeFSRenewalPricePer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalPricePer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalPricePer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalPricePer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalPricePer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalQuotedRenewal
   Description: Method to call when changing the Quoted Renewal flag on the contract renewal header record.
   OperationID: ChangeFSRenewalQuotedRenewal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalQuotedRenewal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalQuotedRenewal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalQuotedRenewal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalQuotedRenewal", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalRACode
   Description: Method to call when changing the RACode on the contract renewal header record.
   OperationID: ChangeFSRenewalRACode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalRACode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalRACode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalRACode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalRACode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalRecurringFreq
   Description: Method to call when changing the RecurringFreq on the contract renewal header record.
Updates FSRenewal with values based on the new RecurringFreq.
   OperationID: ChangeFSRenewalRecurringFreq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalRecurringFreq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalRecurringFreq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalRecurringFreq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalRecurringFreq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalRenewEffDate
   Description: Method to call when changing the renewal effective date on the contract renewal header record.
Updates FSRenewal with values based on the new effective date.
   OperationID: ChangeFSRenewalRenewEffDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalRenewEffDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalRenewEffDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalRenewEffDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalRenewEffDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalTaskSetID
   Description: Method to call when changing the Task Set ID on the contract renewal header record.
   OperationID: ChangeFSRenewalTaskSetID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalTaskSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalTaskSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalTaskSetID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalTaskSetID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalTaxCatID
   Description: Method to call when changing the tax category id on the contract renewal header record.
Validates the id and updates FSRenewal with values from the tax category.
   OperationID: ChangeFSRenewalTaxCatID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalTaxCatID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalTaxCatID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalTaxCatID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalTaxCatID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSRenewalRecurringInv
   Description: Method to call when changing the recurring invoice flag on the contract renewal header record.
   OperationID: ChangeFSRenewalRecurringInv
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSRenewalRecurringInv_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSRenewalRecurringInv_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSRenewalRecurringInv(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ChangeFSRenewalRecurringInv", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPartNumChange
   Description: The method is to be run on leave of the PartNum field before the
ChangeFSContDtPartNum or Update methods are run.
This returns all the questions that need to be asked before a part can be changed.
   OperationID: CheckPartNumChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPartNumChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPartNumChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPartNumChange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/CheckPartNumChange", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckSerialNumbers
   Description: This method returns text of a message to be asked if the number of serial numbers
selected does not match the quantity entered for the FSContDt record.
The user has the option of continuing with the mismatch quantities or canceling.
This method should be called before the update method and should be called only when
part is serial number tracked and the quantity is greater than zero.
If the user answers yes, the change can occur; otherwise the change shouldn't occur.
   OperationID: CheckSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckSerialNumbers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/CheckSerialNumbers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateContractRMA
   Description: Call this method to create RMA for a given service contract.
   OperationID: CreateContractRMA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateContractRMA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateContractRMA_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateContractRMA(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/CreateContractRMA", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExpireContract
   Description: Call this method to expire a service contract.  Allow the user to confirm the
intention to expire the contract before calling this method.  Warn the user
that expiring the contract cannot be undone.
   OperationID: ExpireContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExpireContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExpireContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExpireContract(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ExpireContract", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FrequencyList
   Description: Method to call to get the list for the Frequency options.  The list is
returned in code1`code desc1~code2`code desc2 format.
   OperationID: FrequencyList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/FrequencyList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FrequencyList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/FrequencyList", {
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
   Summary: Invoke method GenerateRenewal
   Description: Call this method to generate Contract Renewal (FSRenewal and FsRenewalDt)
from a given Contract or Renewal.
   OperationID: GenerateRenewal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateRenewal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateRenewal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateRenewal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GenerateRenewal", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateRenewalLines
   Description: Call this method to generate Contract Renewal Lines (FsRenewalDt)
for a given Contract Renewal Header.
   OperationID: GenerateRenewalLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateRenewalLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateRenewalLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateRenewalLines(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GenerateRenewalLines", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListCustom
   Description: Custom GetList method. Retrieves records based on a delimited list
of Contract Numbers.
   OperationID: GetListCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListCustom(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GetListCustom", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewFSContHdFromOrder
   Description: Method to call when adding a contract from an order.
   OperationID: GetNewFSContHdFromOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSContHdFromOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSContHdFromOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFSContHdFromOrder(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GetNewFSContHdFromOrder", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsContactTracker
   Description: Calls the normal GetRows method and then constructs a custom data set combining Hd/Dt fields for the contact tracker.
   OperationID: GetRowsContactTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsContactTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsContactTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsContactTracker(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GetRowsContactTracker", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsCustom
   Description: Custom GetList method. Retrieves records based on a delimited list
of Contract Numbers.
   OperationID: GetRowsCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCustom(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GetRowsCustom", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsCustomerTracker
   Description: Calls the normal GetRows method and then constructs a custom data set combining Hd/Dt fields for the customer tracker.
   OperationID: GetRowsCustomerTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCustomerTracker(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GetRowsCustomerTracker", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsCustomerTrackerActive
   Description: Returns active/not voided contracts for the customer
   OperationID: GetRowsCustomerTrackerActive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTrackerActive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTrackerActive_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCustomerTrackerActive(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GetRowsCustomerTrackerActive", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsCustomerTrackerExpired
   Description: Returns expired/not voided contracts for the customer
   OperationID: GetRowsCustomerTrackerExpired
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTrackerExpired_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTrackerExpired_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCustomerTrackerExpired(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GetRowsCustomerTrackerExpired", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSelectedSerialNumbers
   Description: This method will retrieve the serial numbers for a service contract line and
update the SelectedSerialNumbers table with these records.
   OperationID: GetSelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectedSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectedSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectedSerialNumbers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GetSelectedSerialNumbers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Gets parameters required for launching Select Serial Numbers
   OperationID: GetSelectSerialNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectSerialNumbersParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GetSelectSerialNumbersParams", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRenewalSelectedSerialNumbers
   Description: This method will retrieve the serial numbers for a service contract Renewal line and
update the SelectedSerialNumbers table with these records.
   OperationID: GetRenewalSelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRenewalSelectedSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRenewalSelectedSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRenewalSelectedSerialNumbers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GetRenewalSelectedSerialNumbers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRenewalSelectSerialNumbersParams
   Description: Gets parameters required for launching Select Serial Numbers
   OperationID: GetRenewalSelectSerialNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRenewalSelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRenewalSelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRenewalSelectSerialNumbersParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GetRenewalSelectSerialNumbersParams", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CountContractsOnQuote
   Description: Verifies if the Contract/Renewal has any Quote. Then check if the Quote is related with other Contracts/Renewals.
   OperationID: CountContractsOnQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CountContractsOnQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CountContractsOnQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CountContractsOnQuote(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/CountContractsOnQuote", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsPlantSerialTracking
   Description: Verifies if the current login plant is set for Serial Tracking
   OperationID: IsPlantSerialTracking
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsPlantSerialTracking_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsPlantSerialTracking(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/IsPlantSerialTracking", {
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
   Summary: Invoke method PricePerList
   Description: Method to call to get the list for the Price Per options.  The list is
returned in code1`code desc1~code2`code desc2 format.
   OperationID: PricePerList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/PricePerList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PricePerList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/PricePerList", {
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
   Summary: Invoke method SuspendContract
   Description: Call this method after the user answered yes to the warning message returned by
SuspendContract method.  This logic updates all related InvcDtlRASch
records for this service contract. Based on the input contract status, the related
invoice revenue schedules will be put on hold/unhold.
   OperationID: SuspendContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SuspendContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SuspendContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SuspendContract(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/SuspendContract", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateSN
   Description: Validates that a single serial number is valid for this transaction
   OperationID: ValidateSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSN(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ValidateSN", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VoidContract
   Description: Method to call when voiding the contract.
   OperationID: VoidContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VoidContract(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/VoidContract", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DisableContractLines
   OperationID: DisableContractLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DisableContractLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DisableContractLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DisableContractLines(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/DisableContractLines", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method isContractExpired
   Description: Validates contract Expired date against the current time zone Date for the current company.
   OperationID: isContractExpired
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/isContractExpired_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/isContractExpired_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_isContractExpired(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/isContractExpired", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateOTSTaxID
   Description: One Time Ship To Tax Id validation
   OperationID: ValidateOTSTaxID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateOTSTaxID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOTSTaxID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateOTSTaxID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/ValidateOTSTaxID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewFSContHd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSContHd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSContHd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSContHd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFSContHd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GetNewFSContHd", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewFSContDt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSContDt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSContDt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSContDt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFSContDt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GetNewFSContDt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewFSContSN
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSContSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSContSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSContSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFSContSN(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GetNewFSContSN", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewFSRenewal
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSRenewal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSRenewal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSRenewal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFSRenewal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GetNewFSRenewal", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewFSRenewalDt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSRenewalDt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSRenewalDt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSRenewalDt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFSRenewalDt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GetNewFSRenewalDt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewFSRenewalSN
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSRenewalSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSRenewalSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSRenewalSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFSRenewalSN(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GetNewFSRenewalSN", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewFSContLabExpRate
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSContLabExpRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSContLabExpRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSContLabExpRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFSContLabExpRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GetNewFSContLabExpRate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContDtRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FSContDtRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContHdListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FSContHdListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContHdRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FSContHdRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContLabExpRateRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FSContLabExpRateRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContOrderDtlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FSContOrderDtlListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContSNRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FSContSNRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSRenewalDtRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FSRenewalDtRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSRenewalRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FSRenewalRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSRenewalSNRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FSRenewalSNRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SNFormatRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SelectedSerialNumbersRow[],
}

export interface Erp_Tablesets_FSContDtRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Contract Number of the Contract  */  
   "ContractNum":number,
      /**  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  */  
   "ContractLine":number,
      /**  A unique code that identifies the Contract  */  
   "ContractCode":string,
      /**  The PartNum field identifies the Part  */  
   "PartNum":string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   "RevisionNum":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "LineDesc":string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if its a valid Part.  */  
   "IUM":string,
      /**  Price per unit for the Contract in base currency.  Defaults from the FScontCd table  */  
   "PricePerUnit":number,
      /**  Price per unit for the Contract in customers currency.  Defaults from the FScontCd table  */  
   "DocPricePerUnit":number,
      /**  Total Contract Quantity for the line item.  */  
   "ContractQty":number,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   "ProdCode":string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   "XPartNum":string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   "XRevisionNum":string,
      /**  Used to establish invoice comments about the Contract line item. These will copied into the Invoice detail  file as defaults.  */  
   "InvoiceComment":string,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the FSContDt records for a specific customer.  */  
   "CustNum":number,
      /**  Contains the Order Number that ties this detail record back to an OrderHed record.  */  
   "OrderNum":number,
      /**  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   "OrderLine":number,
      /**  Project ID of the Project table record that this FSContDt record. Can be blank.  */  
   "ProjectID":string,
      /**  Editor widget for Contract comments.  */  
   "CommentText":string,
      /**   A value of "ORD-ENT" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.
(Duplicated from FSContHd for Browse)  */  
   "ContractType":string,
      /**  Contains comments about the detail contract line item. These will be printed on the Sales Acknowledgements and service contracts  */  
   "ContractComment":string,
      /**  Sold to Order Number  */  
   "SoldOrderNum":number,
      /**  Sold To Order line  */  
   "SoldOrderLine":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Reporting currency value of this field  */  
   "Rpt1PricePerUnit":number,
      /**  Reporting currency value of this field  */  
   "Rpt2PricePerUnit":number,
      /**  Reporting currency value of this field  */  
   "Rpt3PricePerUnit":number,
      /**  A value of Yes indicates the line is not part of the service contract agreement and it will not be included in the contract amounts.  */  
   "Inactive":boolean,
      /**  This is the date the contract line was set to inactive.  */  
   "DateInactivated":string,
      /**  This is the first date the contract line is considered for billing purposes.  */  
   "BillStartDate":string,
      /**  This is the last date the contract line is considered for billing.  */  
   "BillEndDate":string,
      /**  Indicates this line has been invoiced.  */  
   "Invoiced":boolean,
      /**  Date this line was invoiced.  */  
   "DateInvoiced":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "AllowUpdate":boolean,
   "CurrencySwitch":boolean,
   "BaseCurrSymbol":string,
   "ExtPrice":number,
   "DocExtPrice":number,
   "DisplayContractType":string,
      /**  Return Quantity used in the create RMA process.  */  
   "ReturnQty":number,
      /**  Indicates if the contract line is selected to create RMA for.  */  
   "SelectedforRMA":boolean,
   "HdCurrencyCode":string,
   "HdCurrencyCodeDesc":string,
      /**  Document currency symbol.  */  
   "DocCurrSymbol":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
      /**  Unit of Measure Description  */  
   "IUMDesc":string,
   "TrackSerialNumbers":boolean,
   "Rpt1ExtPrice":number,
   "Rpt2ExtPrice":number,
   "Rpt3ExtPrice":number,
      /**  The calculated PriceMulti is based on the parent FSContHd record.  */  
   "PriceMulti":number,
      /**  Unique identifier of related integration record.  */  
   "IntExternalKey":string,
   "BitFlag":number,
   "ContractCodeContractDescription":string,
   "CustNumBTName":string,
   "CustNumCustID":string,
   "CustNumName":string,
   "OrderLineLineDesc":string,
   "OrderNumCurrencyCode":string,
   "OrderNumCardMemberName":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumPricePerCode":string,
   "PartNumSalesUM":string,
   "PartNumIUM":string,
   "PartNumSellingFactor":number,
   "PartNumTrackDimension":boolean,
   "PartNumPartDescription":string,
   "PartNumTrackLots":boolean,
   "ProdCodeDescription":string,
   "ProjectIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FSContHdListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   "ContractNum":number,
      /**  A value of "Ord-Ent" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.  */  
   "ContractType":string,
      /**  Contains the Customer number that the Service Contract is for.  This must be valid in the Customer table.  */  
   "CustNum":number,
      /**  The Sales order that this contract is linked to.  */  
   "OrderNum":number,
      /**  The line number of the sales order that this contract is linked to  */  
   "OrderLine":number,
      /**  Same as OrderDate when SLSORD.  TODAY when CNTENT  */  
   "EntryDate":string,
      /**  A unique code that identifies the Contract  */  
   "ContractCode":string,
      /**  Contains comments about the overall Contract. These will be printed on the Service Contract.  */  
   "ContractComment":string,
      /**  Used to establish invoice comments about the overall Contract. These will copied into the Invoice detail file as defaults.  */  
   "InvoiceComment":string,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   "PrcConNum":number,
      /**  Indicates which customer ship to is to be used  for the Service Contract. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   "ShipToNum":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this Contract.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   "LockRate":boolean,
      /**   This is used as one of the selection parameters on the Service Contract entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   "EntryPerson":string,
      /**  This Service Contract has been deactivated when TRUE  */  
   "ContVoid":boolean,
      /**  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service contract is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   "ShpConNum":number,
      /**   The date of the earliest FscontSp.activateDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed. This will always be the earliest activate date on this contract.  */  
   "ActiveDate":string,
      /**   The date of the Latest FscontSp.ExpirationDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed.  this will always be the Latest activate date on this contract.  */  
   "ExpireDate":string,
      /**  Duration of Contract  */  
   "Duration":number,
      /**  Whether the duration is for Days, Months, years.  */  
   "Modifier":string,
      /**  Coverage  for material  */  
   "Material":boolean,
      /**  Coverage for Labor  */  
   "Labor":boolean,
      /**  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  */  
   "Misc":boolean,
      /**  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  */  
   "Invoiced":boolean,
      /**  Packing slip number that this detail record is linked with.  */  
   "PackNum":number,
      /**  An integer that Ties the Contract record to a packing slip detail line  */  
   "PackLine":number,
      /**  This contract covers on site visits  */  
   "OnSite":boolean,
      /**  Indicates that Service Contract with this Code will generate recurring invoices.  */  
   "RecurringInv":boolean,
      /**  The frequency that recurring invoices are generated only 'monthly' for now.  */  
   "RecurringFreq":string,
      /**  Price modifier for unit price field Daily, monthly, Contract(Full length of the contract)  */  
   "PricePer":string,
      /**  This flag is set to TRUE after the last recurring invoice is generated for the contract.  */  
   "LastInvGen":boolean,
      /**  The invoice number of the last recurring invoice.  */  
   "InvoiceNum":number,
      /**  Indicates the Tax Category for this record.  */  
   "TaxCatID":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Bill To Customer Number  */  
   "BTCustNum":number,
      /**   Indicates if the One Time ShipTo information should be used instead of the standard ShipTo.  One Time ShipTo info is stored in this record in the fields prefixed with "OTS"
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   "UseOTS":boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   "OTSName":string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   "OTSAddress1":string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   "OTSAddress2":string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   "OTSAddress3":string,
      /**  City portion of the One Time Shipto  address.  */  
   "OTSCity":string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   "OTSState":string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   "OTSZIP":string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   "OTSResaleID":string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   "OTSTaxRegionCode":string,
      /**  Full name of the contact.  */  
   "OTSContact":string,
      /**  Fax number for the One Time ShipTo.  */  
   "OTSFaxNum":string,
      /**  Phone number for the One Time ShipTo  */  
   "OTSPhoneNum":string,
      /**  One Time Shipping country Number.  */  
   "OTSCountryNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   "DeferredRev":boolean,
      /**  Revenue Amortization Code.  */  
   "RACode":string,
      /**  Starting date the revenue is deferred.  */  
   "DefRevStart":string,
      /**  Indicates if the contract has been suspended.  A suspended contract cannot have any calls linked to it.  */  
   "Suspended":boolean,
      /**  Indicates if the contrct will automatically generate a quote  */  
   "QuotedContract":boolean,
      /**  Defaulted from the service contract code.  Determines whether or not the contract can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  */  
   "ShipContract":boolean,
      /**  Unique identifier of the task set assigned by the user.  */  
   "TaskSetID":string,
      /**  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  */  
   "ReadyToInvoice":boolean,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   "QuoteNum":number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   "QuoteLine":number,
      /**  Indicates the Quote has been accepted  */  
   "QuoteAccepted":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "OTSCountry":string,
   "ContractStartup":boolean,
   "SoldToPhoneNum":string,
   "SoldToFaxNum":string,
   "SoldToContactName":string,
   "ShipToPhoneNum":string,
   "ShipToFaxNum":string,
   "ShipToContactName":string,
   "ContractExpired":boolean,
   "ContractTotal":number,
   "DocContractTotal":number,
   "CurrencySwitch":boolean,
   "BaseCurrSymbol":string,
   "EnableBillTo":boolean,
   "EnableShipTo":boolean,
   "EnableCurrency":boolean,
   "AllowUpdate":boolean,
   "DisplayContractType":string,
   "ShipToAddressList":string,
   "SoldToAddressList":string,
   "PartOrderDtlList":string,
   "opMessage":string,
   "Rpt1ContractTotal":number,
   "Rpt2ContractTotal":number,
   "Rpt3ContractTotal":number,
      /**  Customer.AllowOTS value. Allow One Time Shipto.  */  
   "CustAllowOTS":boolean,
      /**  Name of the Bill To Customer  */  
   "BTCustName":string,
      /**  Delimited list of available bill to customers.  */  
   "AvailBTCustList":string,
   "BaseCurrencyID":string,
      /**  The expire date of the last effective renewed contract  */  
   "RenewedUntil":string,
   "RenewalTotal":number,
   "DocRenewalTotal":number,
   "Rpt1RenewalTotal":number,
   "Rpt2RenewalTotal":number,
   "Rpt3RenewalTotal":number,
   "ContractRenewed":boolean,
      /**  Flag to indicate if the service contract can be renewed.  */  
   "EnableRenewal":boolean,
      /**  Description of the service contract.  */  
   "ContractCodeContractDescription":string,
      /**  Description of the currency  */  
   "CurrencyCodeCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCodeCurrSymbol":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCodeCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyCodeDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCodeCurrName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustNumBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustNumCustID":string,
      /**  The full name of the customer.  */  
   "CustNumName":string,
      /**  When yes, a ShipTo CustID on certain forms will be enabled. This allows a shipto of a different customer to be referenced as a 3rd party for a document.  */  
   "CustNumAllowShipTo3":boolean,
      /**  The member's name on the credit card.  */  
   "InvoiceNumCardMemberName":string,
      /**  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   "InvoiceNumTermsCode":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "OrderLineLineDesc":string,
      /**  A unique code that identifies the currency.  */  
   "OrderNumCurrencyCode":string,
      /**  The member's name on the credit card.  */  
   "OrderNumCardMemberName":string,
      /**  Full description for the Tax Region.  */  
   "OTSTaxRegionCodeDescription":string,
      /**  Line description.  */  
   "PackLineLineDesc":string,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  */  
   "PackNumName":string,
      /**  Free form text describing the revenue amortization code.  */  
   "RACodeRADesc":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "ShipToBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "ShipToCustID":string,
      /**  The full name of the customer.  */  
   "ShipToName":string,
      /**  Full description for the Sales Tax category.  */  
   "TaxCatIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FSContHdRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   "ContractNum":number,
      /**  A value of "Ord-Ent" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.  */  
   "ContractType":string,
      /**  Contains the Customer number that the Service Contract is for.  This must be valid in the Customer table.  */  
   "CustNum":number,
      /**  The Sales order that this contract is linked to.  */  
   "OrderNum":number,
      /**  The line number of the sales order that this contract is linked to  */  
   "OrderLine":number,
      /**  Same as OrderDate when SLSORD.  TODAY when CNTENT  */  
   "EntryDate":string,
      /**  A unique code that identifies the Contract  */  
   "ContractCode":string,
      /**  Contains comments about the overall Contract. These will be printed on the Service Contract.  */  
   "ContractComment":string,
      /**  Used to establish invoice comments about the overall Contract. These will copied into the Invoice detail file as defaults.  */  
   "InvoiceComment":string,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   "PrcConNum":number,
      /**  Indicates which customer ship to is to be used  for the Service Contract. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   "ShipToNum":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this Contract.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   "LockRate":boolean,
      /**   This is used as one of the selection parameters on the Service Contract entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   "EntryPerson":string,
      /**  This Service Contract has been deactivated when TRUE  */  
   "ContVoid":boolean,
      /**  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service contract is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   "ShpConNum":number,
      /**   The date of the earliest FscontSp.activateDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed. This will always be the earliest activate date on this contract.  */  
   "ActiveDate":string,
      /**   The date of the Latest FscontSp.ExpirationDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed.  this will always be the Latest activate date on this contract.  */  
   "ExpireDate":string,
      /**  Duration of Contract  */  
   "Duration":number,
      /**  Whether the duration is for Days, Months, years.  */  
   "Modifier":string,
      /**  Coverage  for material  */  
   "Material":boolean,
      /**  Coverage for Labor  */  
   "Labor":boolean,
      /**  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  */  
   "Misc":boolean,
      /**  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  */  
   "Invoiced":boolean,
      /**  Packing slip number that this detail record is linked with.  */  
   "PackNum":number,
      /**  An integer that Ties the Contract record to a packing slip detail line  */  
   "PackLine":number,
      /**  This contract covers on site visits  */  
   "OnSite":boolean,
      /**  Indicates that Service Contract with this Code will generate recurring invoices.  */  
   "RecurringInv":boolean,
      /**  The frequency that recurring invoices are generated only 'monthly' for now.  */  
   "RecurringFreq":string,
      /**  Price modifier for unit price field Daily, monthly, Contract(Full length of the contract)  */  
   "PricePer":string,
      /**  This flag is set to TRUE after the last recurring invoice is generated for the contract.  */  
   "LastInvGen":boolean,
      /**  The invoice number of the last recurring invoice.  */  
   "InvoiceNum":number,
      /**  Indicates the Tax Category for this record.  */  
   "TaxCatID":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Bill To Customer Number  */  
   "BTCustNum":number,
      /**   Indicates if the One Time ShipTo information should be used instead of the standard ShipTo.  One Time ShipTo info is stored in this record in the fields prefixed with "OTS"
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   "UseOTS":boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   "OTSName":string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   "OTSAddress1":string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   "OTSAddress2":string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   "OTSAddress3":string,
      /**  City portion of the One Time Shipto  address.  */  
   "OTSCity":string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   "OTSState":string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   "OTSZIP":string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   "OTSResaleID":string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   "OTSTaxRegionCode":string,
      /**  Full name of the contact.  */  
   "OTSContact":string,
      /**  Fax number for the One Time ShipTo.  */  
   "OTSFaxNum":string,
      /**  Phone number for the One Time ShipTo  */  
   "OTSPhoneNum":string,
      /**  One Time Shipping country Number.  */  
   "OTSCountryNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   "DeferredRev":boolean,
      /**  Revenue Amortization Code.  */  
   "RACode":string,
      /**  Starting date the revenue is deferred.  */  
   "DefRevStart":string,
      /**  Indicates if the contract has been suspended.  A suspended contract cannot have any calls linked to it.  */  
   "Suspended":boolean,
      /**  Indicates if the contrct will automatically generate a quote  */  
   "QuotedContract":boolean,
      /**  Defaulted from the service contract code.  Determines whether or not the contract can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  */  
   "ShipContract":boolean,
      /**  Unique identifier of the task set assigned by the user.  */  
   "TaskSetID":string,
      /**  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  */  
   "ReadyToInvoice":boolean,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   "QuoteNum":number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   "QuoteLine":number,
      /**  Indicates the Quote has been accepted  */  
   "QuoteAccepted":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  InvcTiming  */  
   "InvcTiming":string,
      /**  Indicates how often an invoice is generated for the contract.  */  
   "FiscalCalendarID":string,
      /**  Indicates if the service contract using is valid for renewal.  */  
   "Renewable":boolean,
      /**  Intrastat: Activates HS Commodity code retrieving in contract invoicing  */  
   "IncIntrastat":boolean,
      /**  Determines if the service contract has to be synchronized with Epicor FSA application.  */  
   "SendToFSA":boolean,
      /**  OTSTaxValidationStatus  */  
   "OTSTaxValidationStatus":number,
      /**  OTSTaxValidationDate  */  
   "OTSTaxValidationDate":string,
   "AllowUpdate":boolean,
      /**  Delimited list of available bill to customers.  */  
   "AvailBTCustList":string,
   "BaseCurrencyID":string,
   "BaseCurrSymbol":string,
      /**  Name of the Bill To Customer  */  
   "BTCustName":string,
   "ContractExpired":boolean,
   "ContractRenewed":boolean,
   "ContractStartup":boolean,
   "ContractTotal":number,
   "CurrencySwitch":boolean,
      /**  Customer.AllowOTS value. Allow One Time Shipto.  */  
   "CustAllowOTS":boolean,
   "DisplayContractType":string,
   "DocContractTotal":number,
   "DocRenewalTotal":number,
   "EnableBillTo":boolean,
   "EnableCurrency":boolean,
   "EnableQuote":boolean,
      /**  Flag to indicate when to enable the Renewable check box.  The flag is set to no if the current contract has been renewed already (FSRenewal exists).  */  
   "EnableRenewable":boolean,
      /**  Flag to indicate if the service contract can be renewed.  (This flag should not be confused with EnableRenewable.)  This EnableRenewal is used to check if the current original contract (FSContHd) or the latest contract renewal (FSRenewal) (whichever is currently actve) meets the expiration date check against the expire horizon and contract renewal period set at FSSyst table.  */  
   "EnableRenewal":boolean,
   "EnableShipTo":boolean,
   "FiscalCalDescription":string,
   "opMessage":string,
   "OTSCountry":string,
   "PartOrderDtlList":string,
      /**  Flag to indicate if the Contract is ready to be quoted.  */  
   "ReadyToQuote":boolean,
   "RenewalTotal":number,
      /**  The expire date of the last effective renewed contract  */  
   "RenewedUntil":string,
   "Rpt1ContractTotal":number,
   "Rpt1RenewalTotal":number,
   "Rpt2ContractTotal":number,
   "Rpt2RenewalTotal":number,
   "Rpt3ContractTotal":number,
   "Rpt3RenewalTotal":number,
   "ShipToAddressList":string,
   "ShipToContactName":string,
   "ShipToFaxNum":string,
   "ShipToPhoneNum":string,
   "SoldToAddressList":string,
   "SoldToContactName":string,
   "SoldToFaxNum":string,
   "SoldToPhoneNum":string,
      /**  Flag to indicate if additional uninvoiced contract line has been added after the contract has been invoiced.  */  
   "UninvoicedLine":boolean,
   "UpdateLineDates":boolean,
      /**  Used to indicate which FSA Service Agreement a Contract Renewal is related to.  */  
   "FSAServiceAgreementNum":number,
   "BitFlag":number,
   "CompanySendToFSA":boolean,
   "ContractCodeContractDescription":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeCurrSymbol":string,
   "CustNumCustID":string,
   "CustNumAllowShipTo3":boolean,
   "CustNumName":string,
   "CustNumBTName":string,
   "CustNumSendToFSA":boolean,
   "InvoiceNumCardMemberName":string,
   "InvoiceNumTermsCode":string,
   "OrderLineLineDesc":string,
   "OrderNumCurrencyCode":string,
   "OrderNumCardMemberName":string,
   "OTSCountryEUMember":boolean,
   "OTSCountryISOCode":string,
   "OTSTaxRegionCodeDescription":string,
   "PackLineLineDesc":string,
   "PackNumName":string,
   "RACodeRADesc":string,
   "ShipToBTName":string,
   "ShipToName":string,
   "ShipToCustID":string,
   "ShipToNumInactive":boolean,
   "ShipToNumName":string,
   "TaskSetWorkflowType":string,
   "TaskSetTaskSetDescription":string,
   "TaxCatIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FSContLabExpRateRow{
      /**  Company  */  
   "Company":string,
      /**  ContractNum  */  
   "ContractNum":number,
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
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FSContOrderDtlListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Contains the Order Number that ties this detail record back to an OrderHed record.  */  
   "OrderNum":number,
      /**  This field along with Company and OrderNum make up the unique key to the OrderHed table.  */  
   "OrderLine":number,
      /**  The user's Internal Part number used to identify Order line item part.  */  
   "PartNum":string,
      /**  Order Line Item description. The Part.Description can be used as a default.  */  
   "LineDesc":string,
      /**  Status of Order Line  */  
   "LineStatus":string,
      /**  boolean flag to indicate user has selected this row  */  
   "Selected":boolean,
      /**  Unique identifier for OrderDtl  row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FSContSNRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Contract Number of the Contract  */  
   "ContractNum":number,
      /**  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  */  
   "ContractLine":number,
      /**  The PartNum field identifies the Part. Not directly maintainable. Mirror image of FSContDt.PartNum. Having this field, allows a SerialNo record to find the contracts that it is related to.  */  
   "PartNum":string,
      /**  Serial number of the Part that is assigned to this Field Service contract line.  */  
   "SerialNumber":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  True indicates that the FSContSN record was auto added by CustShip or DropShip processing  */  
   "AutoAdd":boolean,
      /**  Expire Date of the contract, for display in Serial Number tracker  */  
   "ExpireDate":string,
      /**  Description of the contract header contract type, for display in SerialNo tracker  */  
   "FSContCdDesc":string,
      /**  Unique identifier of related integration record.  */  
   "IntExternalKey":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FSRenewalDtRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   "ContractNum":number,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   "RenewalNbr":number,
      /**  This field along with Company and ContractNum make up the unique key to the table.  */  
   "RenewalLine":number,
      /**  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  */  
   "ContractLine":number,
      /**  The PartNum field identifies the Part  */  
   "PartNum":string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   "RevisionNum":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "LineDesc":string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if its a valid Part.  */  
   "IUM":string,
      /**  The percentage increase of the renewal price.  */  
   "IncreasePct":number,
      /**  Price per unit for the Contract in base currency.  Defaults from the FScontCd table  */  
   "PricePerUnit":number,
      /**  Price per unit for the Contract in customers currency.  Defaults from the FScontCd table  */  
   "DocPricePerUnit":number,
      /**  Reporting currency value of this field  */  
   "Rpt1PricePerUnit":number,
      /**  Reporting currency value of this field  */  
   "Rpt2PricePerUnit":number,
      /**  Reporting currency value of this field  */  
   "Rpt3PricePerUnit":number,
      /**  Total Contract Quantity for the line item.  */  
   "ContractQty":number,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   "XPartNum":string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   "XRevisionNum":string,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the FSContDt records for a specific customer.  */  
   "CustNum":number,
      /**  Contains the Order Number that ties this detail record back to an OrderHed record.  */  
   "OrderNum":number,
      /**  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   "OrderLine":number,
      /**  Project ID of the Project table record that this FSContDt record. Can be blank.  */  
   "ProjectID":string,
      /**  A value of Yes indicates the line is not part of the service contract agreement and it will not be included in the contract amounts.  */  
   "Inactive":boolean,
      /**  This is the date the contract line was set to inactive.  */  
   "DateInactivated":string,
      /**  This is the first date the contract line is considered for billing purposes.  */  
   "BillStartDate":string,
      /**  This is the last date the contract line is considered for billing.  */  
   "BillEndDate":string,
      /**  Indicates this line has been invoiced.  */  
   "Invoiced":boolean,
      /**  Date this line was invoiced.  */  
   "DateInvoiced":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The RefRenewalNbr stores the reference renewal number of the renewal record was copied.  */  
   "RefRenewalNbr":number,
      /**  It is a unique code used to identify a specific product group.  */  
   "ProdCode":string,
      /**  Sales Order Num related to this FSContDt record.  */  
   "SoldOrderNum":number,
      /**  Sales Order Line related to this FSContDt record.  */  
   "SoldOrderLine":number,
   "AllowUpdate":boolean,
   "BaseCurrSymbol":string,
   "CurrencyCode":string,
   "DocCurrSymbol":string,
   "DocExtendedPrice":number,
   "DocOrigPricePerUnit":number,
      /**  Extended Price of the Contract Renewal Line  */  
   "ExtendedPrice":number,
   "IUMDesc":string,
      /**  Original Contract Qty of the Contract Line  */  
   "OrigContractQty":number,
      /**  Original IUM of the Contract Line  */  
   "OrigIUM":string,
   "OrigIUMDesc":string,
      /**  Original Price Per Unit of the Contract Line  */  
   "OrigPricePerUnit":number,
      /**  The calculated PriceMulti is based on the parent FSRenewal record.  */  
   "PriceMulti":number,
   "ProdCodeDescription":string,
   "Rpt1ExtendedPrice":number,
   "Rpt1OrigPricePerUnit":number,
   "Rpt2ExtendedPrice":number,
   "Rpt2OrigPricePerUnit":number,
   "Rpt3ExtendedPrice":number,
   "Rpt3OrigPricePerUnit":number,
   "TrackSerialNumbers":boolean,
      /**  Unique identifier of related integration record.  */  
   "IntExternalKey":string,
   "BitFlag":number,
   "CustNumCustID":string,
   "CustNumName":string,
   "CustNumBTName":string,
   "OrderLineLineDesc":string,
   "OrderNumCardMemberName":string,
   "OrderNumCurrencyCode":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumSellingFactor":number,
   "PartNumTrackDimension":boolean,
   "PartNumIUM":string,
   "PartNumPartDescription":string,
   "PartNumSalesUM":string,
   "PartNumTrackLots":boolean,
   "PartNumPricePerCode":string,
   "ProjectIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FSRenewalRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   "ContractNum":number,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   "RenewalNbr":number,
      /**  Indicates if the renwal will automatically generate a quote.  */  
   "QuotedRenewal":boolean,
      /**  Unique identifier of the task set assigned by the user.  */  
   "TaskSetID":string,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   "QuoteNum":number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   "QuoteLine":number,
      /**  Indicates the Quote has been accepted.  */  
   "QuoteAccepted":boolean,
      /**  This is the contract code assigned to the renewal.  */  
   "RenewalCode":string,
      /**  Defaulted from the service contract code.  Determines whether or not the renewal can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  */  
   "ShipRenewal":boolean,
      /**  Revenue Amortization Code.  */  
   "RACode":string,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   "DeferredRev":boolean,
      /**  Starting date the revenue is deferred.  */  
   "DefRevStart":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this Contract.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   "LockRate":boolean,
      /**   This is used as one of the selection parameters on the Service Contract entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   "EntryPerson":string,
      /**  Date the renewal was created.  */  
   "EntryDate":string,
      /**  Coverage  for material  */  
   "Material":boolean,
      /**  Coverage for Labor  */  
   "Labor":boolean,
      /**  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  */  
   "Misc":boolean,
      /**  This contract covers on site visits  */  
   "OnSite":boolean,
      /**  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  */  
   "Invoiced":boolean,
      /**  The invoice number of the last recurring invoice.  */  
   "InvoiceNum":number,
      /**  Packing slip number that this detail record is linked with.  */  
   "PackNum":number,
      /**  An integer that Ties the Contract record to a packing slip detail line  */  
   "PackLine":number,
      /**  Indicates that Service Contract with this Code will generate recurring invoices.  */  
   "RecurringInv":boolean,
      /**  The frequency that recurring invoices are generated only 'monthly' for now.  */  
   "RecurringFreq":string,
      /**  Price modifier for unit price field Daily, monthly, Contract(Full length of the contract)  */  
   "PricePer":string,
      /**  This flag is set to TRUE after the last recurring invoice is generated for the contract.  */  
   "LastInvGen":boolean,
      /**  Indicates the Tax Category for this record.  */  
   "TaxCatID":string,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  */  
   "ReadyToInvoice":boolean,
      /**  The Sales order that this contract is linked to.  */  
   "OrderNum":number,
      /**  The line number of the sales order that this contract is linked to  */  
   "OrderLine":number,
      /**  Duration of Contract  */  
   "Duration":number,
      /**  Used to establish invoice comments about the overall Renewal.  */  
   "RenewalComment":string,
      /**  Date when the renewal begins.  */  
   "RenewEffDate":string,
      /**  Date the renewal ends.  */  
   "RenewedUntil":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  InvcTiming  */  
   "InvcTiming":string,
      /**  It is the same as the contract type but applied to renewals  */  
   "ContractCode":string,
      /**  The unit of measure of time that the renewal contract lasts.  */  
   "Modifier":string,
      /**  Indicates how often an invoice is generated for the contract  */  
   "FiscalCalendarID":string,
      /**  Indicates if the service contract is valid for renewal  */  
   "Renewable":boolean,
      /**  Total Renewal Amount  */  
   "RenewalTotal":number,
   "DocRenewalTotal":number,
   "Rpt1RenewalTotal":number,
   "Rpt2RenewalTotal":number,
   "Rpt3RenewalTotal":number,
      /**  Indicates if the Contract Renewal has expired.  */  
   "RenewalExpired":boolean,
      /**  Indicates if the Contract Renewal has been renewed.  */  
   "RenewalRenewed":boolean,
      /**  Indicates if the related Contract Header has been voided.  */  
   "RenewalVoid":boolean,
   "AllowUpdate":boolean,
      /**  Flag to indicate if additional uninvoiced renewal line has been added after the renewal header has been invoiced.  */  
   "UninvoicedLine":boolean,
   "FiscalCalDescription":string,
      /**  Flag to indicate if the Contract Renewal is ready to be quoted.  */  
   "ReadyToQuote":boolean,
   "EnableQuote":boolean,
      /**  Flag to indicate when to enable the Renewable check box.  The flag is set to no if the current contract renewal has been renewed already (another FSRenewal exists).  */  
   "EnableRenewable":boolean,
   "UpdateLineDates":boolean,
   "ContractCodeDescription":string,
   "BitFlag":number,
   "CodeContractDescription":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeCurrName":string,
   "RACodeRADesc":string,
   "TaskSetWorkflowType":string,
   "TaskSetTaskSetDescription":string,
   "TaxCatIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FSRenewalSNRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Contract Number of the Contract  */  
   "ContractNum":number,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   "RenewalNbr":number,
      /**  This field along with Company and ContractNum make up the unique key to the table.  */  
   "RenewalLine":number,
      /**  The PartNum field identifies the Part. Not directly maintainable. Mirror image of FSContDt.PartNum. Having this field, allows a SerialNo record to find the contracts that it is related to.  */  
   "PartNum":string,
      /**  Serial number of the Part that is assigned to this Field Service contract line.  */  
   "SerialNumber":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Description of the contract header contract type, for display in SerialNo tracker  */  
   "FSContCdDesc":string,
      /**  Unique identifier of related integration record.  */  
   "IntExternalKey":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SNFormatRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site Identifier. This field cannot be blank.  */  
   "Plant":string,
      /**  The PartNum field identifies the Part and is used in the primary key.  */  
   "PartNum":string,
      /**  Number of digits in the serial number  */  
   "NumberOfDigits":number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   "SNMask":string,
      /**   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  */  
   "SNBaseDataType":string,
   "SNFormat1":string,
      /**  Whether or not to have leading zeroes  */  
   "LeadingZeroes":boolean,
      /**   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  */  
   "SNPrefix":string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   "SNMaskSuffix":string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   "SNMaskPrefix":string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   "SNLastUsedSeq":string,
   "HasSerialNumbers":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "PartPricePerCode":string,
   "PartTrackLots":boolean,
   "PartTrackSerialNum":boolean,
   "PartTrackDimension":boolean,
   "PartSalesUM":string,
   "PartIUM":string,
   "PartSellingFactor":number,
   "PartPartDescription":string,
   "SerialMaskMaskType":number,
   "SerialMaskMask":string,
   "SerialMaskExample":string,
   "SerialMaskDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SelectedSerialNumbersRow{
      /**  Company  */  
   "Company":string,
      /**  SerialNumber  */  
   "SerialNumber":string,
      /**  Scrapped flag  */  
   "Scrapped":boolean,
      /**  Scrapped reason code  */  
   "ScrappedReasonCode":string,
      /**  Voided flag  */  
   "Voided":boolean,
      /**  Reference field  */  
   "Reference":string,
      /**  Reason code type = s  */  
   "ReasonCodeType":string,
      /**  Reason code description  */  
   "ReasonCodeDesc":string,
      /**  PartNumber  */  
   "PartNum":string,
      /**  Serial number prefix  */  
   "SNPrefix":string,
      /**  Base number used to create the serial number  */  
   "SNBaseNumber":string,
      /**  RowID of the source record for this serial number  */  
   "SourceRowID":string,
      /**  TransType of the record that created this serial number  */  
   "TransType":string,
      /**  True if this serial numbered part passed inspection  */  
   "PassedInspection":boolean,
      /**  Used to flag previously selected serial numbers as deselected  */  
   "Deselected":boolean,
   "KitWhseList":string,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  */  
   "RawSerialNum":string,
      /**  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  */  
   "KBLbrAction":number,
      /**  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  */  
   "KBLbrActionDesc":string,
      /**  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  */  
   "PreventDeselect":boolean,
      /**  Used only by SN Assignment  */  
   "XRefPartNum":string,
      /**  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  */  
   "XRefPartType":string,
   "PreDeselected":boolean,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   "poLinkValues":string,
      /**  The mask the was used to generate the serial number  */  
   "SNMask":string,
      /**  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  */  
   "NotSavedToDB":boolean,
   "RowSelected":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ActivateContractNum
      @param ds
   */  
export interface ActivateContract_input{
      /**  The contract number to activate  */  
   ActivateContractNum:number,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ActivateContract_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipBillEndDate
      @param ds
   */  
export interface ChangeFSContDtBillEndDate_input{
      /**  The proposed bill end date  */  
   ipBillEndDate:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContDtBillEndDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipBillStartDate
      @param ds
   */  
export interface ChangeFSContDtBillStartDate_input{
      /**  The proposed bill start date  */  
   ipBillStartDate:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContDtBillStartDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ProposedContractQty
      @param ds
   */  
export interface ChangeFSContDtContractQty_input{
      /**  The proposed contract quantity  */  
   ProposedContractQty:number,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContDtContractQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ProposedOrderLine
      @param ds
   */  
export interface ChangeFSContDtOrderLine_input{
      /**  The proposed order line number  */  
   ProposedOrderLine:number,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContDtOrderLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ProposedOrderNum
      @param ds
   */  
export interface ChangeFSContDtOrderNum_input{
      /**  The proposed order number  */  
   ProposedOrderNum:number,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContDtOrderNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ProposedPartNum
      @param substitutePartNum
      @param ds
   */  
export interface ChangeFSContDtPartNumWithSubs_input{
   ProposedPartNum:string,
   substitutePartNum:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContDtPartNumWithSubs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ProposedPartNum
      @param ds
   */  
export interface ChangeFSContDtPartNum_input{
      /**  The proposed part number  */  
   ProposedPartNum:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContDtPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ProposedPricePerUnit
      @param ds
   */  
export interface ChangeFSContDtPricePerUnit_input{
      /**  The proposed price per unit  */  
   ProposedPricePerUnit:number,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContDtPricePerUnit_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ProposedProdCode
      @param ds
   */  
export interface ChangeFSContDtProdCode_input{
      /**  The proposed product code  */  
   ProposedProdCode:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContDtProdCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ProposedProjectID
      @param ds
   */  
export interface ChangeFSContDtProjectID_input{
      /**  The proposed project id  */  
   ProposedProjectID:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContDtProjectID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ProposedXPartNum
      @param ds
   */  
export interface ChangeFSContDtXPartNum_input{
      /**  The proposed xref part number  */  
   ProposedXPartNum:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContDtXPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeFSContHDUseOTS_input{
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContHDUseOTS_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ProposedActiveDate
      @param ds
   */  
export interface ChangeFSContHdActiveDate_input{
      /**  The proposed active date  */  
   ProposedActiveDate:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContHdActiveDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ProposedCustNum
      @param ds
   */  
export interface ChangeFSContHdBTCusNum_input{
      /**  The proposed Bill To customer Num  */  
   ProposedCustNum:number,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContHdBTCusNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ProposedContractCode
      @param ds
   */  
export interface ChangeFSContHdContractCode_input{
      /**  The proposed contract code  */  
   ProposedContractCode:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContHdContractCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ProposedCurrencyCode
      @param ds
   */  
export interface ChangeFSContHdCurrencyCode_input{
      /**  The proposed currency code  */  
   ProposedCurrencyCode:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContHdCurrencyCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ProposedCustID
      @param ds
   */  
export interface ChangeFSContHdCustID_input{
      /**  The proposed customer id  */  
   ProposedCustID:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContHdCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipDeferredRev
      @param ds
   */  
export interface ChangeFSContHdDeferredRev_input{
      /**  The proposed Deferred Revenue value  */  
   ipDeferredRev:boolean,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContHdDeferredRev_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ProposedDuration
      @param ds
   */  
export interface ChangeFSContHdDuration_input{
      /**  The proposed duration  */  
   ProposedDuration:number,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContHdDuration_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipFiscalCalendarID
      @param ds
   */  
export interface ChangeFSContHdFiscalCalendarID_input{
      /**  The proposed Fiscal Calendar ID value  */  
   ipFiscalCalendarID:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContHdFiscalCalendarID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param proposedModifier
      @param ds
   */  
export interface ChangeFSContHdModifier_input{
      /**  The proposed Modifier  */  
   proposedModifier:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContHdModifier_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ProposedConNum
      @param ds
   */  
export interface ChangeFSContHdPrcConNum_input{
      /**  The proposed contact number  */  
   ProposedConNum:number,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContHdPrcConNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipPricePer
      @param ds
   */  
export interface ChangeFSContHdPricePer_input{
      /**  The proposed PricePer  */  
   ipPricePer:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContHdPricePer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipQuotedContract
      @param ds
   */  
export interface ChangeFSContHdQuotedContract_input{
      /**  The proposed Quoted Contract value  */  
   ipQuotedContract:boolean,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContHdQuotedContract_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipRACode
      @param ds
   */  
export interface ChangeFSContHdRACode_input{
      /**  The proposed Revenue Amortization Code value  */  
   ipRACode:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContHdRACode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipRecurringFreq
      @param ds
   */  
export interface ChangeFSContHdRecurringFreq_input{
      /**  The proposed RecurringFreq  */  
   ipRecurringFreq:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContHdRecurringFreq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipRecurringInv
      @param ds
   */  
export interface ChangeFSContHdRecurringInv_input{
      /**  The proposed recurring invoice value  */  
   ipRecurringInv:boolean,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContHdRecurringInv_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipShipToCustID
      @param ds
   */  
export interface ChangeFSContHdShipToCustID_input{
      /**  The proposed ShipTo Customer ID  */  
   ipShipToCustID:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContHdShipToCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ProposedShipToNum
      @param ds
   */  
export interface ChangeFSContHdShipToNum_input{
      /**  The proposed ship to number  */  
   ProposedShipToNum:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContHdShipToNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ProposedShpConNum
      @param ds
   */  
export interface ChangeFSContHdShpConNum_input{
      /**  The proposed ship to number  */  
   ProposedShpConNum:number,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContHdShpConNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipSuspended
      @param ds
   */  
export interface ChangeFSContHdSuspended_input{
      /**  The proposed Suspended value  */  
   ipSuspended:boolean,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContHdSuspended_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipTaskSetID
      @param ds
   */  
export interface ChangeFSContHdTaskSetID_input{
      /**  The proposed Task Set ID value  */  
   ipTaskSetID:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContHdTaskSetID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ProposedTaxCatID
      @param ds
   */  
export interface ChangeFSContHdTaxCatID_input{
      /**  The proposed tax category id  */  
   ProposedTaxCatID:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSContHdTaxCatID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipContractCode
      @param ds
   */  
export interface ChangeFSRenewalContractCode_input{
      /**  The proposed contract code  */  
   ipContractCode:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalContractCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipDeferredRev
      @param ds
   */  
export interface ChangeFSRenewalDeferredRev_input{
      /**  The proposed Deferred Revenue value  */  
   ipDeferredRev:boolean,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalDeferredRev_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipBillEndDate
      @param ds
   */  
export interface ChangeFSRenewalDtBillEndDate_input{
      /**  The proposed bill end date  */  
   ipBillEndDate:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalDtBillEndDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipBillStartDate
      @param ds
   */  
export interface ChangeFSRenewalDtBillStartDate_input{
      /**  The proposed bill start date  */  
   ipBillStartDate:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalDtBillStartDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipContractQty
      @param ds
   */  
export interface ChangeFSRenewalDtContractQty_input{
      /**  The proposed contract quantity  */  
   ipContractQty:number,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalDtContractQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipIncreasePct
      @param ds
   */  
export interface ChangeFSRenewalDtIncreasePct_input{
      /**  The proposed increase percent  */  
   ipIncreasePct:number,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalDtIncreasePct_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipOrderLine
      @param ds
   */  
export interface ChangeFSRenewalDtOrderLine_input{
      /**  The proposed order line number  */  
   ipOrderLine:number,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalDtOrderLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipOrderNum
      @param ds
   */  
export interface ChangeFSRenewalDtOrderNum_input{
      /**  The proposed order number  */  
   ipOrderNum:number,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalDtOrderNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ProposedPartNum
      @param substitutePartNum
      @param ds
   */  
export interface ChangeFSRenewalDtPartNumWithSubs_input{
      /**  The proposed part number  */  
   ProposedPartNum:string,
      /**  The substitute part if any  */  
   substitutePartNum:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalDtPartNumWithSubs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipPartNum
      @param ds
   */  
export interface ChangeFSRenewalDtPartNum_input{
      /**  The proposed part number  */  
   ipPartNum:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalDtPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipPricePerUnit
      @param ipBaseOrDoc
      @param ds
   */  
export interface ChangeFSRenewalDtPricePerUnit_input{
      /**  The proposed price per unit  */  
   ipPricePerUnit:number,
      /**  Indicates if calculating for Base ('B') or Doc ('D')  */  
   ipBaseOrDoc:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalDtPricePerUnit_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipProdCode
      @param ds
   */  
export interface ChangeFSRenewalDtProdCode_input{
      /**  The proposed product code  */  
   ipProdCode:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalDtProdCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipProjectID
      @param ds
   */  
export interface ChangeFSRenewalDtProjectID_input{
      /**  The proposed project id  */  
   ipProjectID:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalDtProjectID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipXPartNum
      @param ds
   */  
export interface ChangeFSRenewalDtXPartNum_input{
      /**  The proposed xref part number  */  
   ipXPartNum:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalDtXPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipDuration
      @param ds
   */  
export interface ChangeFSRenewalDuration_input{
      /**  The proposed duration  */  
   ipDuration:number,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalDuration_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipFiscalCalendarID
      @param ds
   */  
export interface ChangeFSRenewalFiscalCalendarID_input{
      /**  The proposed Fiscal Calendar ID value  */  
   ipFiscalCalendarID:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalFiscalCalendarID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipModifier
      @param ds
   */  
export interface ChangeFSRenewalModifier_input{
      /**  The proposed Modifier  */  
   ipModifier:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalModifier_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipPricePer
      @param ds
   */  
export interface ChangeFSRenewalPricePer_input{
      /**  The proposed PricePer  */  
   ipPricePer:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalPricePer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipQuotedRenewal
      @param ds
   */  
export interface ChangeFSRenewalQuotedRenewal_input{
      /**  The proposed Quoted Renewal value  */  
   ipQuotedRenewal:boolean,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalQuotedRenewal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipRACode
      @param ds
   */  
export interface ChangeFSRenewalRACode_input{
      /**  The proposed Revenue Amortization Code value  */  
   ipRACode:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalRACode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipRecurringFreq
      @param ds
   */  
export interface ChangeFSRenewalRecurringFreq_input{
      /**  The proposed RecurringFreq  */  
   ipRecurringFreq:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalRecurringFreq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipRecurringInv
      @param ds
   */  
export interface ChangeFSRenewalRecurringInv_input{
      /**  The proposed recurring invoice value  */  
   ipRecurringInv:boolean,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalRecurringInv_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipRenewEffDate
      @param ds
   */  
export interface ChangeFSRenewalRenewEffDate_input{
      /**  The proposed renewal effective date  */  
   ipRenewEffDate:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalRenewEffDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipTaskSetID
      @param ds
   */  
export interface ChangeFSRenewalTaskSetID_input{
      /**  The proposed Task Set ID value  */  
   ipTaskSetID:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalTaskSetID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipTaxCatID
      @param ds
   */  
export interface ChangeFSRenewalTaxCatID_input{
      /**  The proposed tax category id  */  
   ipTaxCatID:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ChangeFSRenewalTaxCatID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param cPartNum
   */  
export interface CheckPartNumChange_input{
      /**  The new PartNum if a substitute part is found, partNum will be the substitute part
            No means the part cannot be changed  */  
   cPartNum:string,
}

export interface CheckPartNumChange_output{
parameters : {
      /**  output parameters  */  
   cPartNum:string,
   cSubPartMessage:string,
   lSubAvail:boolean,
   cMsgType:string,
}
}

   /** Required : 
      @param ds
      @param contractQty
   */  
export interface CheckSerialNumbers_input{
   ds:Erp_Tablesets_ServiceContractTableset[],
      /**  Quantity of Serial Numbers required for the Contract Line  */  
   contractQty:number,
}

export interface CheckSerialNumbers_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
   cMessageText:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CountContractsOnQuote_input{
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface CountContractsOnQuote_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipContractNum
      @param ipReasonCode
      @param ds
   */  
export interface CreateContractRMA_input{
      /**  The contract number to create the RMA for.  */  
   ipContractNum:number,
      /**  The Reason Code for the RMA.  */  
   ipReasonCode:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface CreateContractRMA_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param contractNum
   */  
export interface DeleteByID_input{
   contractNum:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param expiredDate
   */  
export interface DisableContractLines_input{
   expiredDate:string,
}

export interface DisableContractLines_output{
   returnObj:boolean,
}

export interface Erp_Tablesets_FSContCustTrkRow{
      /**  from FSContHd.Comany  */  
   Company:string,
      /**  from FSContHd.CustNum  */  
   CustNum:number,
      /**  from FSContHd.ContractNum  */  
   ContractNum:number,
      /**  from FSContHd.ShpConNum  */  
   ShpConNum:number,
      /**  from FSContHd.ContractCodeDescription  */  
   ContractCodeDescription:string,
      /**  from FSContHd.Duration and FSContHd.Modifier  */  
   Duration:number,
      /**  from FSContHd.OnSite  */  
   OnSite:boolean,
      /**  from FSContHd.Material  */  
   Material:boolean,
      /**  from FSContHd.Labor  */  
   Labor:boolean,
      /**  from FSContHd.Misc  */  
   Misc:boolean,
      /**  from FSContHd.ActiveDate  */  
   ActiveDate:string,
      /**  from FSContHd.ExpireDate  */  
   ExpireDate:string,
      /**  from FSContHd.Invoiced  */  
   Invoiced:boolean,
      /**  from FSContCd.InvoiceNum  */  
   InvoiceNum:number,
      /**  from FSContHd.ContractCode  */  
   ContractCode:string,
      /**  from FSContHd.PackLine  */  
   PackLine:number,
      /**  from FSContHd.PackNum  */  
   PackNum:number,
      /**  from FSContDt.ContractLine  */  
   ContractLine:number,
      /**  from FSContDt.PartNum  */  
   PartNum:string,
      /**  from FSContDt.LineDesc  */  
   LineDesc:string,
      /**  from FSContDt.ContractQty  */  
   ContractQty:number,
      /**  from FSContDt.OrderNum  */  
   OrderNum:number,
      /**  from FSContDt.OrderLine  */  
   OrderLine:number,
      /**  from FSContHd.ContractExpired  */  
   ContractExpired:boolean,
      /**  from FSContDt.RevisionNum  */  
   RevisionNum:string,
      /**  from FSContDt.XPartNum  */  
   XPartNum:string,
      /**  from FSContDt.XRevisionNum  */  
   XRevisionNum:string,
   Modifier:string,
      /**  Duration + Modifier  */  
   DispDuration:string,
      /**  The full name for customer.  */  
   CustomerName:string,
      /**  The name for the ship to location.  */  
   ShipToName:string,
   ShipToNum:string,
   PrcConNum:number,
      /**  The customer ID.  */  
   CustID:string,
      /**  from FSContDt.IUM  */  
   IUM:string,
   OTSTaxRegionDesc:string,
   ShipToCustNum:number,
      /**  from FSContHd.ContVoid  */  
   ContVoid:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FSContCustTrkTableset{
   FSContCustTrk:Erp_Tablesets_FSContCustTrkRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FSContDtRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Contract Number of the Contract  */  
   ContractNum:number,
      /**  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  */  
   ContractLine:number,
      /**  A unique code that identifies the Contract  */  
   ContractCode:string,
      /**  The PartNum field identifies the Part  */  
   PartNum:string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   RevisionNum:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if its a valid Part.  */  
   IUM:string,
      /**  Price per unit for the Contract in base currency.  Defaults from the FScontCd table  */  
   PricePerUnit:number,
      /**  Price per unit for the Contract in customers currency.  Defaults from the FScontCd table  */  
   DocPricePerUnit:number,
      /**  Total Contract Quantity for the line item.  */  
   ContractQty:number,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   XPartNum:string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   XRevisionNum:string,
      /**  Used to establish invoice comments about the Contract line item. These will copied into the Invoice detail  file as defaults.  */  
   InvoiceComment:string,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the FSContDt records for a specific customer.  */  
   CustNum:number,
      /**  Contains the Order Number that ties this detail record back to an OrderHed record.  */  
   OrderNum:number,
      /**  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   OrderLine:number,
      /**  Project ID of the Project table record that this FSContDt record. Can be blank.  */  
   ProjectID:string,
      /**  Editor widget for Contract comments.  */  
   CommentText:string,
      /**   A value of "ORD-ENT" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.
(Duplicated from FSContHd for Browse)  */  
   ContractType:string,
      /**  Contains comments about the detail contract line item. These will be printed on the Sales Acknowledgements and service contracts  */  
   ContractComment:string,
      /**  Sold to Order Number  */  
   SoldOrderNum:number,
      /**  Sold To Order line  */  
   SoldOrderLine:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Reporting currency value of this field  */  
   Rpt1PricePerUnit:number,
      /**  Reporting currency value of this field  */  
   Rpt2PricePerUnit:number,
      /**  Reporting currency value of this field  */  
   Rpt3PricePerUnit:number,
      /**  A value of Yes indicates the line is not part of the service contract agreement and it will not be included in the contract amounts.  */  
   Inactive:boolean,
      /**  This is the date the contract line was set to inactive.  */  
   DateInactivated:string,
      /**  This is the first date the contract line is considered for billing purposes.  */  
   BillStartDate:string,
      /**  This is the last date the contract line is considered for billing.  */  
   BillEndDate:string,
      /**  Indicates this line has been invoiced.  */  
   Invoiced:boolean,
      /**  Date this line was invoiced.  */  
   DateInvoiced:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   AllowUpdate:boolean,
   CurrencySwitch:boolean,
   BaseCurrSymbol:string,
   ExtPrice:number,
   DocExtPrice:number,
   DisplayContractType:string,
      /**  Return Quantity used in the create RMA process.  */  
   ReturnQty:number,
      /**  Indicates if the contract line is selected to create RMA for.  */  
   SelectedforRMA:boolean,
   HdCurrencyCode:string,
   HdCurrencyCodeDesc:string,
      /**  Document currency symbol.  */  
   DocCurrSymbol:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  Unit of Measure Description  */  
   IUMDesc:string,
   TrackSerialNumbers:boolean,
   Rpt1ExtPrice:number,
   Rpt2ExtPrice:number,
   Rpt3ExtPrice:number,
      /**  The calculated PriceMulti is based on the parent FSContHd record.  */  
   PriceMulti:number,
      /**  Unique identifier of related integration record.  */  
   IntExternalKey:string,
   BitFlag:number,
   ContractCodeContractDescription:string,
   CustNumBTName:string,
   CustNumCustID:string,
   CustNumName:string,
   OrderLineLineDesc:string,
   OrderNumCurrencyCode:string,
   OrderNumCardMemberName:string,
   PartNumTrackSerialNum:boolean,
   PartNumPricePerCode:string,
   PartNumSalesUM:string,
   PartNumIUM:string,
   PartNumSellingFactor:number,
   PartNumTrackDimension:boolean,
   PartNumPartDescription:string,
   PartNumTrackLots:boolean,
   ProdCodeDescription:string,
   ProjectIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FSContHdListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   ContractNum:number,
      /**  A value of "Ord-Ent" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.  */  
   ContractType:string,
      /**  Contains the Customer number that the Service Contract is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  The Sales order that this contract is linked to.  */  
   OrderNum:number,
      /**  The line number of the sales order that this contract is linked to  */  
   OrderLine:number,
      /**  Same as OrderDate when SLSORD.  TODAY when CNTENT  */  
   EntryDate:string,
      /**  A unique code that identifies the Contract  */  
   ContractCode:string,
      /**  Contains comments about the overall Contract. These will be printed on the Service Contract.  */  
   ContractComment:string,
      /**  Used to establish invoice comments about the overall Contract. These will copied into the Invoice detail file as defaults.  */  
   InvoiceComment:string,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   PrcConNum:number,
      /**  Indicates which customer ship to is to be used  for the Service Contract. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   ShipToNum:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this Contract.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**   This is used as one of the selection parameters on the Service Contract entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   EntryPerson:string,
      /**  This Service Contract has been deactivated when TRUE  */  
   ContVoid:boolean,
      /**  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service contract is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   ShpConNum:number,
      /**   The date of the earliest FscontSp.activateDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed. This will always be the earliest activate date on this contract.  */  
   ActiveDate:string,
      /**   The date of the Latest FscontSp.ExpirationDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed.  this will always be the Latest activate date on this contract.  */  
   ExpireDate:string,
      /**  Duration of Contract  */  
   Duration:number,
      /**  Whether the duration is for Days, Months, years.  */  
   Modifier:string,
      /**  Coverage  for material  */  
   Material:boolean,
      /**  Coverage for Labor  */  
   Labor:boolean,
      /**  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  */  
   Misc:boolean,
      /**  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  */  
   Invoiced:boolean,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  An integer that Ties the Contract record to a packing slip detail line  */  
   PackLine:number,
      /**  This contract covers on site visits  */  
   OnSite:boolean,
      /**  Indicates that Service Contract with this Code will generate recurring invoices.  */  
   RecurringInv:boolean,
      /**  The frequency that recurring invoices are generated only 'monthly' for now.  */  
   RecurringFreq:string,
      /**  Price modifier for unit price field Daily, monthly, Contract(Full length of the contract)  */  
   PricePer:string,
      /**  This flag is set to TRUE after the last recurring invoice is generated for the contract.  */  
   LastInvGen:boolean,
      /**  The invoice number of the last recurring invoice.  */  
   InvoiceNum:number,
      /**  Indicates the Tax Category for this record.  */  
   TaxCatID:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**   Indicates if the One Time ShipTo information should be used instead of the standard ShipTo.  One Time ShipTo info is stored in this record in the fields prefixed with "OTS"
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
      /**  Full name of the contact.  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipping country Number.  */  
   OTSCountryNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   DeferredRev:boolean,
      /**  Revenue Amortization Code.  */  
   RACode:string,
      /**  Starting date the revenue is deferred.  */  
   DefRevStart:string,
      /**  Indicates if the contract has been suspended.  A suspended contract cannot have any calls linked to it.  */  
   Suspended:boolean,
      /**  Indicates if the contrct will automatically generate a quote  */  
   QuotedContract:boolean,
      /**  Defaulted from the service contract code.  Determines whether or not the contract can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  */  
   ShipContract:boolean,
      /**  Unique identifier of the task set assigned by the user.  */  
   TaskSetID:string,
      /**  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  */  
   ReadyToInvoice:boolean,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   QuoteLine:number,
      /**  Indicates the Quote has been accepted  */  
   QuoteAccepted:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   OTSCountry:string,
   ContractStartup:boolean,
   SoldToPhoneNum:string,
   SoldToFaxNum:string,
   SoldToContactName:string,
   ShipToPhoneNum:string,
   ShipToFaxNum:string,
   ShipToContactName:string,
   ContractExpired:boolean,
   ContractTotal:number,
   DocContractTotal:number,
   CurrencySwitch:boolean,
   BaseCurrSymbol:string,
   EnableBillTo:boolean,
   EnableShipTo:boolean,
   EnableCurrency:boolean,
   AllowUpdate:boolean,
   DisplayContractType:string,
   ShipToAddressList:string,
   SoldToAddressList:string,
   PartOrderDtlList:string,
   opMessage:string,
   Rpt1ContractTotal:number,
   Rpt2ContractTotal:number,
   Rpt3ContractTotal:number,
      /**  Customer.AllowOTS value. Allow One Time Shipto.  */  
   CustAllowOTS:boolean,
      /**  Name of the Bill To Customer  */  
   BTCustName:string,
      /**  Delimited list of available bill to customers.  */  
   AvailBTCustList:string,
   BaseCurrencyID:string,
      /**  The expire date of the last effective renewed contract  */  
   RenewedUntil:string,
   RenewalTotal:number,
   DocRenewalTotal:number,
   Rpt1RenewalTotal:number,
   Rpt2RenewalTotal:number,
   Rpt3RenewalTotal:number,
   ContractRenewed:boolean,
      /**  Flag to indicate if the service contract can be renewed.  */  
   EnableRenewal:boolean,
      /**  Description of the service contract.  */  
   ContractCodeContractDescription:string,
      /**  Description of the currency  */  
   CurrencyCodeCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCodeCurrSymbol:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCodeCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyCodeDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCodeCurrName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustNumBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustNumCustID:string,
      /**  The full name of the customer.  */  
   CustNumName:string,
      /**  When yes, a ShipTo CustID on certain forms will be enabled. This allows a shipto of a different customer to be referenced as a 3rd party for a document.  */  
   CustNumAllowShipTo3:boolean,
      /**  The member's name on the credit card.  */  
   InvoiceNumCardMemberName:string,
      /**  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   InvoiceNumTermsCode:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   OrderLineLineDesc:string,
      /**  A unique code that identifies the currency.  */  
   OrderNumCurrencyCode:string,
      /**  The member's name on the credit card.  */  
   OrderNumCardMemberName:string,
      /**  Full description for the Tax Region.  */  
   OTSTaxRegionCodeDescription:string,
      /**  Line description.  */  
   PackLineLineDesc:string,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  */  
   PackNumName:string,
      /**  Free form text describing the revenue amortization code.  */  
   RACodeRADesc:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   ShipToBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   ShipToCustID:string,
      /**  The full name of the customer.  */  
   ShipToName:string,
      /**  Full description for the Sales Tax category.  */  
   TaxCatIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FSContHdListTableset{
   FSContHdList:Erp_Tablesets_FSContHdListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FSContHdRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   ContractNum:number,
      /**  A value of "Ord-Ent" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.  */  
   ContractType:string,
      /**  Contains the Customer number that the Service Contract is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  The Sales order that this contract is linked to.  */  
   OrderNum:number,
      /**  The line number of the sales order that this contract is linked to  */  
   OrderLine:number,
      /**  Same as OrderDate when SLSORD.  TODAY when CNTENT  */  
   EntryDate:string,
      /**  A unique code that identifies the Contract  */  
   ContractCode:string,
      /**  Contains comments about the overall Contract. These will be printed on the Service Contract.  */  
   ContractComment:string,
      /**  Used to establish invoice comments about the overall Contract. These will copied into the Invoice detail file as defaults.  */  
   InvoiceComment:string,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   PrcConNum:number,
      /**  Indicates which customer ship to is to be used  for the Service Contract. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   ShipToNum:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this Contract.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**   This is used as one of the selection parameters on the Service Contract entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   EntryPerson:string,
      /**  This Service Contract has been deactivated when TRUE  */  
   ContVoid:boolean,
      /**  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service contract is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   ShpConNum:number,
      /**   The date of the earliest FscontSp.activateDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed. This will always be the earliest activate date on this contract.  */  
   ActiveDate:string,
      /**   The date of the Latest FscontSp.ExpirationDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed.  this will always be the Latest activate date on this contract.  */  
   ExpireDate:string,
      /**  Duration of Contract  */  
   Duration:number,
      /**  Whether the duration is for Days, Months, years.  */  
   Modifier:string,
      /**  Coverage  for material  */  
   Material:boolean,
      /**  Coverage for Labor  */  
   Labor:boolean,
      /**  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  */  
   Misc:boolean,
      /**  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  */  
   Invoiced:boolean,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  An integer that Ties the Contract record to a packing slip detail line  */  
   PackLine:number,
      /**  This contract covers on site visits  */  
   OnSite:boolean,
      /**  Indicates that Service Contract with this Code will generate recurring invoices.  */  
   RecurringInv:boolean,
      /**  The frequency that recurring invoices are generated only 'monthly' for now.  */  
   RecurringFreq:string,
      /**  Price modifier for unit price field Daily, monthly, Contract(Full length of the contract)  */  
   PricePer:string,
      /**  This flag is set to TRUE after the last recurring invoice is generated for the contract.  */  
   LastInvGen:boolean,
      /**  The invoice number of the last recurring invoice.  */  
   InvoiceNum:number,
      /**  Indicates the Tax Category for this record.  */  
   TaxCatID:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**   Indicates if the One Time ShipTo information should be used instead of the standard ShipTo.  One Time ShipTo info is stored in this record in the fields prefixed with "OTS"
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
      /**  Full name of the contact.  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipping country Number.  */  
   OTSCountryNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   DeferredRev:boolean,
      /**  Revenue Amortization Code.  */  
   RACode:string,
      /**  Starting date the revenue is deferred.  */  
   DefRevStart:string,
      /**  Indicates if the contract has been suspended.  A suspended contract cannot have any calls linked to it.  */  
   Suspended:boolean,
      /**  Indicates if the contrct will automatically generate a quote  */  
   QuotedContract:boolean,
      /**  Defaulted from the service contract code.  Determines whether or not the contract can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  */  
   ShipContract:boolean,
      /**  Unique identifier of the task set assigned by the user.  */  
   TaskSetID:string,
      /**  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  */  
   ReadyToInvoice:boolean,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   QuoteLine:number,
      /**  Indicates the Quote has been accepted  */  
   QuoteAccepted:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  InvcTiming  */  
   InvcTiming:string,
      /**  Indicates how often an invoice is generated for the contract.  */  
   FiscalCalendarID:string,
      /**  Indicates if the service contract using is valid for renewal.  */  
   Renewable:boolean,
      /**  Intrastat: Activates HS Commodity code retrieving in contract invoicing  */  
   IncIntrastat:boolean,
      /**  Determines if the service contract has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  OTSTaxValidationStatus  */  
   OTSTaxValidationStatus:number,
      /**  OTSTaxValidationDate  */  
   OTSTaxValidationDate:string,
   AllowUpdate:boolean,
      /**  Delimited list of available bill to customers.  */  
   AvailBTCustList:string,
   BaseCurrencyID:string,
   BaseCurrSymbol:string,
      /**  Name of the Bill To Customer  */  
   BTCustName:string,
   ContractExpired:boolean,
   ContractRenewed:boolean,
   ContractStartup:boolean,
   ContractTotal:number,
   CurrencySwitch:boolean,
      /**  Customer.AllowOTS value. Allow One Time Shipto.  */  
   CustAllowOTS:boolean,
   DisplayContractType:string,
   DocContractTotal:number,
   DocRenewalTotal:number,
   EnableBillTo:boolean,
   EnableCurrency:boolean,
   EnableQuote:boolean,
      /**  Flag to indicate when to enable the Renewable check box.  The flag is set to no if the current contract has been renewed already (FSRenewal exists).  */  
   EnableRenewable:boolean,
      /**  Flag to indicate if the service contract can be renewed.  (This flag should not be confused with EnableRenewable.)  This EnableRenewal is used to check if the current original contract (FSContHd) or the latest contract renewal (FSRenewal) (whichever is currently actve) meets the expiration date check against the expire horizon and contract renewal period set at FSSyst table.  */  
   EnableRenewal:boolean,
   EnableShipTo:boolean,
   FiscalCalDescription:string,
   opMessage:string,
   OTSCountry:string,
   PartOrderDtlList:string,
      /**  Flag to indicate if the Contract is ready to be quoted.  */  
   ReadyToQuote:boolean,
   RenewalTotal:number,
      /**  The expire date of the last effective renewed contract  */  
   RenewedUntil:string,
   Rpt1ContractTotal:number,
   Rpt1RenewalTotal:number,
   Rpt2ContractTotal:number,
   Rpt2RenewalTotal:number,
   Rpt3ContractTotal:number,
   Rpt3RenewalTotal:number,
   ShipToAddressList:string,
   ShipToContactName:string,
   ShipToFaxNum:string,
   ShipToPhoneNum:string,
   SoldToAddressList:string,
   SoldToContactName:string,
   SoldToFaxNum:string,
   SoldToPhoneNum:string,
      /**  Flag to indicate if additional uninvoiced contract line has been added after the contract has been invoiced.  */  
   UninvoicedLine:boolean,
   UpdateLineDates:boolean,
      /**  Used to indicate which FSA Service Agreement a Contract Renewal is related to.  */  
   FSAServiceAgreementNum:number,
   BitFlag:number,
   CompanySendToFSA:boolean,
   ContractCodeContractDescription:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrSymbol:string,
   CustNumCustID:string,
   CustNumAllowShipTo3:boolean,
   CustNumName:string,
   CustNumBTName:string,
   CustNumSendToFSA:boolean,
   InvoiceNumCardMemberName:string,
   InvoiceNumTermsCode:string,
   OrderLineLineDesc:string,
   OrderNumCurrencyCode:string,
   OrderNumCardMemberName:string,
   OTSCountryEUMember:boolean,
   OTSCountryISOCode:string,
   OTSTaxRegionCodeDescription:string,
   PackLineLineDesc:string,
   PackNumName:string,
   RACodeRADesc:string,
   ShipToBTName:string,
   ShipToName:string,
   ShipToCustID:string,
   ShipToNumInactive:boolean,
   ShipToNumName:string,
   TaskSetWorkflowType:string,
   TaskSetTaskSetDescription:string,
   TaxCatIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FSContLabExpRateRow{
      /**  Company  */  
   Company:string,
      /**  ContractNum  */  
   ContractNum:number,
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
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FSContOrderDtlListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Contains the Order Number that ties this detail record back to an OrderHed record.  */  
   OrderNum:number,
      /**  This field along with Company and OrderNum make up the unique key to the OrderHed table.  */  
   OrderLine:number,
      /**  The user's Internal Part number used to identify Order line item part.  */  
   PartNum:string,
      /**  Order Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  Status of Order Line  */  
   LineStatus:string,
      /**  boolean flag to indicate user has selected this row  */  
   Selected:boolean,
      /**  Unique identifier for OrderDtl  row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FSContSNRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Contract Number of the Contract  */  
   ContractNum:number,
      /**  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  */  
   ContractLine:number,
      /**  The PartNum field identifies the Part. Not directly maintainable. Mirror image of FSContDt.PartNum. Having this field, allows a SerialNo record to find the contracts that it is related to.  */  
   PartNum:string,
      /**  Serial number of the Part that is assigned to this Field Service contract line.  */  
   SerialNumber:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  True indicates that the FSContSN record was auto added by CustShip or DropShip processing  */  
   AutoAdd:boolean,
      /**  Expire Date of the contract, for display in Serial Number tracker  */  
   ExpireDate:string,
      /**  Description of the contract header contract type, for display in SerialNo tracker  */  
   FSContCdDesc:string,
      /**  Unique identifier of related integration record.  */  
   IntExternalKey:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FSRenewalDtRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   ContractNum:number,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
      /**  This field along with Company and ContractNum make up the unique key to the table.  */  
   RenewalLine:number,
      /**  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  */  
   ContractLine:number,
      /**  The PartNum field identifies the Part  */  
   PartNum:string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   RevisionNum:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if its a valid Part.  */  
   IUM:string,
      /**  The percentage increase of the renewal price.  */  
   IncreasePct:number,
      /**  Price per unit for the Contract in base currency.  Defaults from the FScontCd table  */  
   PricePerUnit:number,
      /**  Price per unit for the Contract in customers currency.  Defaults from the FScontCd table  */  
   DocPricePerUnit:number,
      /**  Reporting currency value of this field  */  
   Rpt1PricePerUnit:number,
      /**  Reporting currency value of this field  */  
   Rpt2PricePerUnit:number,
      /**  Reporting currency value of this field  */  
   Rpt3PricePerUnit:number,
      /**  Total Contract Quantity for the line item.  */  
   ContractQty:number,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   XPartNum:string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   XRevisionNum:string,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the FSContDt records for a specific customer.  */  
   CustNum:number,
      /**  Contains the Order Number that ties this detail record back to an OrderHed record.  */  
   OrderNum:number,
      /**  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   OrderLine:number,
      /**  Project ID of the Project table record that this FSContDt record. Can be blank.  */  
   ProjectID:string,
      /**  A value of Yes indicates the line is not part of the service contract agreement and it will not be included in the contract amounts.  */  
   Inactive:boolean,
      /**  This is the date the contract line was set to inactive.  */  
   DateInactivated:string,
      /**  This is the first date the contract line is considered for billing purposes.  */  
   BillStartDate:string,
      /**  This is the last date the contract line is considered for billing.  */  
   BillEndDate:string,
      /**  Indicates this line has been invoiced.  */  
   Invoiced:boolean,
      /**  Date this line was invoiced.  */  
   DateInvoiced:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The RefRenewalNbr stores the reference renewal number of the renewal record was copied.  */  
   RefRenewalNbr:number,
      /**  It is a unique code used to identify a specific product group.  */  
   ProdCode:string,
      /**  Sales Order Num related to this FSContDt record.  */  
   SoldOrderNum:number,
      /**  Sales Order Line related to this FSContDt record.  */  
   SoldOrderLine:number,
   AllowUpdate:boolean,
   BaseCurrSymbol:string,
   CurrencyCode:string,
   DocCurrSymbol:string,
   DocExtendedPrice:number,
   DocOrigPricePerUnit:number,
      /**  Extended Price of the Contract Renewal Line  */  
   ExtendedPrice:number,
   IUMDesc:string,
      /**  Original Contract Qty of the Contract Line  */  
   OrigContractQty:number,
      /**  Original IUM of the Contract Line  */  
   OrigIUM:string,
   OrigIUMDesc:string,
      /**  Original Price Per Unit of the Contract Line  */  
   OrigPricePerUnit:number,
      /**  The calculated PriceMulti is based on the parent FSRenewal record.  */  
   PriceMulti:number,
   ProdCodeDescription:string,
   Rpt1ExtendedPrice:number,
   Rpt1OrigPricePerUnit:number,
   Rpt2ExtendedPrice:number,
   Rpt2OrigPricePerUnit:number,
   Rpt3ExtendedPrice:number,
   Rpt3OrigPricePerUnit:number,
   TrackSerialNumbers:boolean,
      /**  Unique identifier of related integration record.  */  
   IntExternalKey:string,
   BitFlag:number,
   CustNumCustID:string,
   CustNumName:string,
   CustNumBTName:string,
   OrderLineLineDesc:string,
   OrderNumCardMemberName:string,
   OrderNumCurrencyCode:string,
   PartNumTrackSerialNum:boolean,
   PartNumSellingFactor:number,
   PartNumTrackDimension:boolean,
   PartNumIUM:string,
   PartNumPartDescription:string,
   PartNumSalesUM:string,
   PartNumTrackLots:boolean,
   PartNumPricePerCode:string,
   ProjectIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FSRenewalRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   ContractNum:number,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
      /**  Indicates if the renwal will automatically generate a quote.  */  
   QuotedRenewal:boolean,
      /**  Unique identifier of the task set assigned by the user.  */  
   TaskSetID:string,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   QuoteLine:number,
      /**  Indicates the Quote has been accepted.  */  
   QuoteAccepted:boolean,
      /**  This is the contract code assigned to the renewal.  */  
   RenewalCode:string,
      /**  Defaulted from the service contract code.  Determines whether or not the renewal can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  */  
   ShipRenewal:boolean,
      /**  Revenue Amortization Code.  */  
   RACode:string,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   DeferredRev:boolean,
      /**  Starting date the revenue is deferred.  */  
   DefRevStart:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this Contract.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**   This is used as one of the selection parameters on the Service Contract entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   EntryPerson:string,
      /**  Date the renewal was created.  */  
   EntryDate:string,
      /**  Coverage  for material  */  
   Material:boolean,
      /**  Coverage for Labor  */  
   Labor:boolean,
      /**  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  */  
   Misc:boolean,
      /**  This contract covers on site visits  */  
   OnSite:boolean,
      /**  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  */  
   Invoiced:boolean,
      /**  The invoice number of the last recurring invoice.  */  
   InvoiceNum:number,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  An integer that Ties the Contract record to a packing slip detail line  */  
   PackLine:number,
      /**  Indicates that Service Contract with this Code will generate recurring invoices.  */  
   RecurringInv:boolean,
      /**  The frequency that recurring invoices are generated only 'monthly' for now.  */  
   RecurringFreq:string,
      /**  Price modifier for unit price field Daily, monthly, Contract(Full length of the contract)  */  
   PricePer:string,
      /**  This flag is set to TRUE after the last recurring invoice is generated for the contract.  */  
   LastInvGen:boolean,
      /**  Indicates the Tax Category for this record.  */  
   TaxCatID:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  */  
   ReadyToInvoice:boolean,
      /**  The Sales order that this contract is linked to.  */  
   OrderNum:number,
      /**  The line number of the sales order that this contract is linked to  */  
   OrderLine:number,
      /**  Duration of Contract  */  
   Duration:number,
      /**  Used to establish invoice comments about the overall Renewal.  */  
   RenewalComment:string,
      /**  Date when the renewal begins.  */  
   RenewEffDate:string,
      /**  Date the renewal ends.  */  
   RenewedUntil:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  InvcTiming  */  
   InvcTiming:string,
      /**  It is the same as the contract type but applied to renewals  */  
   ContractCode:string,
      /**  The unit of measure of time that the renewal contract lasts.  */  
   Modifier:string,
      /**  Indicates how often an invoice is generated for the contract  */  
   FiscalCalendarID:string,
      /**  Indicates if the service contract is valid for renewal  */  
   Renewable:boolean,
      /**  Total Renewal Amount  */  
   RenewalTotal:number,
   DocRenewalTotal:number,
   Rpt1RenewalTotal:number,
   Rpt2RenewalTotal:number,
   Rpt3RenewalTotal:number,
      /**  Indicates if the Contract Renewal has expired.  */  
   RenewalExpired:boolean,
      /**  Indicates if the Contract Renewal has been renewed.  */  
   RenewalRenewed:boolean,
      /**  Indicates if the related Contract Header has been voided.  */  
   RenewalVoid:boolean,
   AllowUpdate:boolean,
      /**  Flag to indicate if additional uninvoiced renewal line has been added after the renewal header has been invoiced.  */  
   UninvoicedLine:boolean,
   FiscalCalDescription:string,
      /**  Flag to indicate if the Contract Renewal is ready to be quoted.  */  
   ReadyToQuote:boolean,
   EnableQuote:boolean,
      /**  Flag to indicate when to enable the Renewable check box.  The flag is set to no if the current contract renewal has been renewed already (another FSRenewal exists).  */  
   EnableRenewable:boolean,
   UpdateLineDates:boolean,
   ContractCodeDescription:string,
   BitFlag:number,
   CodeContractDescription:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeCurrName:string,
   RACodeRADesc:string,
   TaskSetWorkflowType:string,
   TaskSetTaskSetDescription:string,
   TaxCatIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FSRenewalSNRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Contract Number of the Contract  */  
   ContractNum:number,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
      /**  This field along with Company and ContractNum make up the unique key to the table.  */  
   RenewalLine:number,
      /**  The PartNum field identifies the Part. Not directly maintainable. Mirror image of FSContDt.PartNum. Having this field, allows a SerialNo record to find the contracts that it is related to.  */  
   PartNum:string,
      /**  Serial number of the Part that is assigned to this Field Service contract line.  */  
   SerialNumber:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Description of the contract header contract type, for display in SerialNo tracker  */  
   FSContCdDesc:string,
      /**  Unique identifier of related integration record.  */  
   IntExternalKey:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SNFormatRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  The PartNum field identifies the Part and is used in the primary key.  */  
   PartNum:string,
      /**  Number of digits in the serial number  */  
   NumberOfDigits:number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   SNMask:string,
      /**   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  */  
   SNBaseDataType:string,
      /**   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  */  
   SNFormat:string,
      /**  Whether or not to have leading zeroes  */  
   LeadingZeroes:boolean,
      /**   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  */  
   SNPrefix:string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   SNMaskSuffix:string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   SNMaskPrefix:string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   SNLastUsedSeq:string,
   HasSerialNumbers:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   PartPricePerCode:string,
   PartTrackLots:boolean,
   PartTrackSerialNum:boolean,
   PartTrackDimension:boolean,
   PartSalesUM:string,
   PartIUM:string,
   PartSellingFactor:number,
   PartPartDescription:string,
   SerialMaskMaskType:number,
   SerialMaskMask:string,
   SerialMaskExample:string,
   SerialMaskDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SelectSerialNumbersParamsRow{
      /**  The part number to which the serial numbers have been assigned.  */  
   partNum:string,
      /**  The quantity of serial numbers that need to be selected.  */  
   quantity:number,
      /**  whereClause for filtering available serial numbers  */  
   whereClause:string,
      /**  transType of this transaction  */  
   transType:string,
      /**  Include when filtering a set of SN's for BL processing is necessary.  It may be null if not needed.  */  
   sourceRowID:string,
      /**  Determines if serial numbers can be created.  */  
   enableCreate:boolean,
      /**  Determines if serial numbers can be selected.  */  
   enableSelect:boolean,
      /**  Determines if serial numbers can be retrieved.  */  
   enableRetrieve:boolean,
      /**  Specifies whether Voided serial numbers can be manually selected.  */  
   allowVoided:boolean,
      /**  The Plant associated with this transaction  */  
   plant:string,
   xrefPartNum:string,
   xrefPartType:string,
   xrefCustNum:number,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   poLinkValues:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   attributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   attributeSetShortDescription:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   revisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SelectSerialNumbersParamsTableset{
   SelectSerialNumbersParams:Erp_Tablesets_SelectSerialNumbersParamsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SelectedSerialNumbersRow{
      /**  Company  */  
   Company:string,
      /**  SerialNumber  */  
   SerialNumber:string,
      /**  Scrapped flag  */  
   Scrapped:boolean,
      /**  Scrapped reason code  */  
   ScrappedReasonCode:string,
      /**  Voided flag  */  
   Voided:boolean,
      /**  Reference field  */  
   Reference:string,
      /**  Reason code type = s  */  
   ReasonCodeType:string,
      /**  Reason code description  */  
   ReasonCodeDesc:string,
      /**  PartNumber  */  
   PartNum:string,
      /**  Serial number prefix  */  
   SNPrefix:string,
      /**  Base number used to create the serial number  */  
   SNBaseNumber:string,
      /**  RowID of the source record for this serial number  */  
   SourceRowID:string,
      /**  TransType of the record that created this serial number  */  
   TransType:string,
      /**  True if this serial numbered part passed inspection  */  
   PassedInspection:boolean,
      /**  Used to flag previously selected serial numbers as deselected  */  
   Deselected:boolean,
   KitWhseList:string,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  */  
   RawSerialNum:string,
      /**  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  */  
   KBLbrAction:number,
      /**  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  */  
   KBLbrActionDesc:string,
      /**  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  */  
   PreventDeselect:boolean,
      /**  Used only by SN Assignment  */  
   XRefPartNum:string,
      /**  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  */  
   XRefPartType:string,
   PreDeselected:boolean,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   poLinkValues:string,
      /**  The mask the was used to generate the serial number  */  
   SNMask:string,
      /**  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  */  
   NotSavedToDB:boolean,
   RowSelected:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ServiceContractTableset{
   FSContHd:Erp_Tablesets_FSContHdRow[],
   FSContDt:Erp_Tablesets_FSContDtRow[],
   FSContSN:Erp_Tablesets_FSContSNRow[],
   FSRenewal:Erp_Tablesets_FSRenewalRow[],
   FSRenewalDt:Erp_Tablesets_FSRenewalDtRow[],
   FSRenewalSN:Erp_Tablesets_FSRenewalSNRow[],
   FSContLabExpRate:Erp_Tablesets_FSContLabExpRateRow[],
   FSContOrderDtlList:Erp_Tablesets_FSContOrderDtlListRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtServiceContractTableset{
   FSContHd:Erp_Tablesets_FSContHdRow[],
   FSContDt:Erp_Tablesets_FSContDtRow[],
   FSContSN:Erp_Tablesets_FSContSNRow[],
   FSRenewal:Erp_Tablesets_FSRenewalRow[],
   FSRenewalDt:Erp_Tablesets_FSRenewalDtRow[],
   FSRenewalSN:Erp_Tablesets_FSRenewalSNRow[],
   FSContLabExpRate:Erp_Tablesets_FSContLabExpRateRow[],
   FSContOrderDtlList:Erp_Tablesets_FSContOrderDtlListRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ipContractNum
      @param ds
   */  
export interface ExpireContract_input{
      /**  The contract number to expire  */  
   ipContractNum:number,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface ExpireContract_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

export interface FrequencyList_output{
parameters : {
      /**  output parameters  */  
   FrequencyList:string,
}
}

   /** Required : 
      @param ipContractNum
      @param ipRenewalNbr
      @param ds
   */  
export interface GenerateRenewalLines_input{
      /**  The target contract number.  */  
   ipContractNum:number,
      /**  The target renewal number.  */  
   ipRenewalNbr:number,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface GenerateRenewalLines_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ipContractNum
      @param ds
   */  
export interface GenerateRenewal_input{
      /**  The source contract number.  */  
   ipContractNum:number,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface GenerateRenewal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param contractNum
   */  
export interface GetByID_input{
   contractNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ServiceContractTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ServiceContractTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ServiceContractTableset[],
}

   /** Required : 
      @param ContractNumList
      @param pageSize
      @param absolutePage
   */  
export interface GetListCustom_input{
      /**  The contract number list  */  
   ContractNumList:string,
      /**  The pageSize number list  */  
   pageSize:number,
      /**  The absolutePage number list  */  
   absolutePage:number,
}

export interface GetListCustom_output{
   returnObj:Erp_Tablesets_FSContHdListTableset[],
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
   returnObj:Erp_Tablesets_FSContHdListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param contractNum
   */  
export interface GetNewFSContDt_input{
   ds:Erp_Tablesets_ServiceContractTableset[],
   contractNum:number,
}

export interface GetNewFSContDt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param OrderNum
      @param ds
   */  
export interface GetNewFSContHdFromOrder_input{
      /**  The order number  */  
   OrderNum:number,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface GetNewFSContHdFromOrder_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewFSContHd_input{
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface GetNewFSContHd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ds
      @param contractNum
   */  
export interface GetNewFSContLabExpRate_input{
   ds:Erp_Tablesets_ServiceContractTableset[],
   contractNum:number,
}

export interface GetNewFSContLabExpRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ds
      @param contractNum
      @param contractLine
      @param partNum
   */  
export interface GetNewFSContSN_input{
   ds:Erp_Tablesets_ServiceContractTableset[],
   contractNum:number,
   contractLine:number,
   partNum:string,
}

export interface GetNewFSContSN_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ds
      @param contractNum
      @param renewalNbr
   */  
export interface GetNewFSRenewalDt_input{
   ds:Erp_Tablesets_ServiceContractTableset[],
   contractNum:number,
   renewalNbr:number,
}

export interface GetNewFSRenewalDt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ds
      @param contractNum
      @param renewalNbr
      @param renewalLine
      @param partNum
   */  
export interface GetNewFSRenewalSN_input{
   ds:Erp_Tablesets_ServiceContractTableset[],
   contractNum:number,
   renewalNbr:number,
   renewalLine:number,
   partNum:string,
}

export interface GetNewFSRenewalSN_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ds
      @param contractNum
   */  
export interface GetNewFSRenewal_input{
   ds:Erp_Tablesets_ServiceContractTableset[],
   contractNum:number,
}

export interface GetNewFSRenewal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetRenewalSelectSerialNumbersParams_input{
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface GetRenewalSelectSerialNumbersParams_output{
   returnObj:Erp_Tablesets_SelectSerialNumbersParamsTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param iContractNum
      @param iRenewalNbr
      @param iRenewalLine
      @param iPartNum
      @param ds
   */  
export interface GetRenewalSelectedSerialNumbers_input{
      /**  The Contract Number  */  
   iContractNum:number,
      /**  The Contract Renewal number  */  
   iRenewalNbr:number,
      /**  The Contract Renewal Line number  */  
   iRenewalLine:number,
      /**  The Part Num  */  
   iPartNum:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface GetRenewalSelectedSerialNumbers_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param whereClauseFSContHd
      @param whereClauseFSContDt
      @param whereClauseFSContSN
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSerialNumberSearch
      @param whereClauseSNFormat
      @param contactName
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsContactTracker_input{
      /**  Whereclause for FSContHd table.  */  
   whereClauseFSContHd:string,
      /**  Whereclause for FSContDt table.  */  
   whereClauseFSContDt:string,
      /**  Whereclause for FSContSN table.  */  
   whereClauseFSContSN:string,
      /**  Whereclause for SelectedSerialNumbers.  */  
   whereClauseSelectedSerialNumbers:string,
      /**  Whereclause for SerialNumberSearch  */  
   whereClauseSerialNumberSearch:string,
      /**  Whereclause for SNFormat table.  */  
   whereClauseSNFormat:string,
      /**  Contact to return data for.  */  
   contactName:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsContactTracker_output{
   returnObj:Erp_Tablesets_FSContCustTrkTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ContractNumList
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustom_input{
      /**  The contract number list  */  
   ContractNumList:string,
      /**  The pageSize number list  */  
   pageSize:number,
      /**  The absolutePage number list  */  
   absolutePage:number,
}

export interface GetRowsCustom_output{
   returnObj:Erp_Tablesets_ServiceContractTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseFSContHd
      @param whereClauseFSContDt
      @param whereClauseFSContSN
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSerialNumberSearch
      @param whereClauseSNFormat
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustomerTrackerActive_input{
      /**  Whereclause for FSContHd table.  */  
   whereClauseFSContHd:string,
      /**  Whereclause for FSContDt table.  */  
   whereClauseFSContDt:string,
      /**  Whereclause for FSContSN table.  */  
   whereClauseFSContSN:string,
      /**  Whereclause for SelectedSerialNumbers.  */  
   whereClauseSelectedSerialNumbers:string,
      /**  Whereclause for SerialNumberSearch  */  
   whereClauseSerialNumberSearch:string,
      /**  Whereclause for SNFormat table.  */  
   whereClauseSNFormat:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsCustomerTrackerActive_output{
   returnObj:Erp_Tablesets_FSContCustTrkTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseFSContHd
      @param whereClauseFSContDt
      @param whereClauseFSContSN
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSerialNumberSearch
      @param whereClauseSNFormat
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustomerTrackerExpired_input{
      /**  Whereclause for FSContHd table.  */  
   whereClauseFSContHd:string,
      /**  Whereclause for FSContDt table.  */  
   whereClauseFSContDt:string,
      /**  Whereclause for FSContSN table.  */  
   whereClauseFSContSN:string,
      /**  Whereclause for SelectedSerialNumbers.  */  
   whereClauseSelectedSerialNumbers:string,
      /**  Whereclause for SerialNumberSearch  */  
   whereClauseSerialNumberSearch:string,
      /**  Whereclause for SNFormat table.  */  
   whereClauseSNFormat:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsCustomerTrackerExpired_output{
   returnObj:Erp_Tablesets_FSContCustTrkTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseFSContHd
      @param whereClauseFSContDt
      @param whereClauseFSContSN
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSerialNumberSearch
      @param whereClauseSNFormat
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustomerTracker_input{
      /**  Whereclause for FSContHd table.  */  
   whereClauseFSContHd:string,
      /**  Whereclause for FSContDt table.  */  
   whereClauseFSContDt:string,
      /**  Whereclause for FSContSN table.  */  
   whereClauseFSContSN:string,
      /**  Whereclause for SelectedSerialNumbers.  */  
   whereClauseSelectedSerialNumbers:string,
      /**  Whereclause for SerialNumberSearch  */  
   whereClauseSerialNumberSearch:string,
      /**  Whereclause for SNFormat table.  */  
   whereClauseSNFormat:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsCustomerTracker_output{
   returnObj:Erp_Tablesets_FSContCustTrkTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseFSContHd
      @param whereClauseFSContDt
      @param whereClauseFSContSN
      @param whereClauseFSRenewal
      @param whereClauseFSRenewalDt
      @param whereClauseFSRenewalSN
      @param whereClauseFSContLabExpRate
      @param whereClauseFSContOrderDtlList
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSNFormat
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseFSContHd:string,
   whereClauseFSContDt:string,
   whereClauseFSContSN:string,
   whereClauseFSRenewal:string,
   whereClauseFSRenewalDt:string,
   whereClauseFSRenewalSN:string,
   whereClauseFSContLabExpRate:string,
   whereClauseFSContOrderDtlList:string,
   whereClauseSelectedSerialNumbers:string,
   whereClauseSNFormat:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ServiceContractTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetSelectSerialNumbersParams_input{
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface GetSelectSerialNumbersParams_output{
   returnObj:Erp_Tablesets_SelectSerialNumbersParamsTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param iContractNum
      @param iContractLine
      @param iPartNum
      @param ds
   */  
export interface GetSelectedSerialNumbers_input{
      /**  The Contract Number  */  
   iContractNum:number,
      /**  The Contract Detail line number  */  
   iContractLine:number,
      /**  The Part Num  */  
   iPartNum:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface GetSelectedSerialNumbers_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
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

export interface IsPlantSerialTracking_output{
parameters : {
      /**  output parameters  */  
   isSerialTracking:boolean,
}
}

export interface PricePerList_output{
parameters : {
      /**  output parameters  */  
   PricePerList:string,
}
}

   /** Required : 
      @param ipSuspend
      @param ipReasonCode
      @param ds
   */  
export interface SuspendContract_input{
      /**  The requested Suspend or Unsuspend status change.  */  
   ipSuspend:boolean,
      /**  The Reason Code for the hold request.  */  
   ipReasonCode:string,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface SuspendContract_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtServiceContractTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtServiceContractTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ds
      @param manualValidation
      @param hmrcFraudPrevHeader
   */  
export interface ValidateOTSTaxID_input{
   ds:Erp_Tablesets_ServiceContractTableset[],
   manualValidation:boolean,
   hmrcFraudPrevHeader:string,
}

export interface ValidateOTSTaxID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
   opMessage:string,
}
}

   /** Required : 
      @param ds
      @param serialNumber
   */  
export interface ValidateSN_input{
   ds:Erp_Tablesets_ServiceContractTableset[],
      /**  Serial number to validate.  */  
   serialNumber:string,
}

export interface ValidateSN_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
   isVoided:boolean,
}
}

   /** Required : 
      @param VoidContractNum
      @param ds
   */  
export interface VoidContract_input{
      /**  The contract number to void  */  
   VoidContractNum:number,
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface VoidContract_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface isContractExpired_input{
   ds:Erp_Tablesets_ServiceContractTableset[],
}

export interface isContractExpired_output{
      /**  Returns true if expired, false if not expired.  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ServiceContractTableset[],
}
}

