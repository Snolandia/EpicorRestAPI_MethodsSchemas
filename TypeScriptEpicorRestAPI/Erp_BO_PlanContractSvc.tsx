import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PlanContractSvc
// Description: Plan Contract Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/$metadata", {
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
   Description: Get PlanContracts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlanContracts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlanContractHdrRow
   */  
export function get_PlanContracts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractHdrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContracts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractHdrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlanContracts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlanContractHdrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlanContractHdrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlanContracts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContracts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlanContract item
   Description: Calls GetByID to retrieve the PlanContract item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlanContract
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractID Desc: ContractID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlanContractHdrRow
   */  
export function get_PlanContracts_Company_ContractID(Company:string, ContractID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlanContractHdrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContracts(" + Company + "," + ContractID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PlanContractHdrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PlanContract for the service
   Description: Calls UpdateExt to update PlanContract. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlanContract
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractID Desc: ContractID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlanContractHdrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PlanContracts_Company_ContractID(Company:string, ContractID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContracts(" + Company + "," + ContractID + ")", {
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
   Summary: Call UpdateExt to delete PlanContract item
   Description: Call UpdateExt to delete PlanContract item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlanContract
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractID Desc: ContractID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PlanContracts_Company_ContractID(Company:string, ContractID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContracts(" + Company + "," + ContractID + ")", {
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
   Description: Get PlanContractDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlanContractDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractID Desc: ContractID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlanContractDtlRow
   */  
export function get_PlanContracts_Company_ContractID_PlanContractDtls(Company:string, ContractID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContracts(" + Company + "," + ContractID + ")/PlanContractDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlanContractDtl item
   Description: Calls GetByID to retrieve the PlanContractDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlanContractDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractID Desc: ContractID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlanContractDtlRow
   */  
export function get_PlanContracts_Company_ContractID_PlanContractDtls_Company_ContractID_LineNum(Company:string, ContractID:string, LineNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlanContractDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContracts(" + Company + "," + ContractID + ")/PlanContractDtls(" + Company + "," + ContractID + "," + LineNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PlanContractDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PlanContractWhseBins items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlanContractWhseBins1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractID Desc: ContractID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlanContractWhseBinRow
   */  
export function get_PlanContracts_Company_ContractID_PlanContractWhseBins(Company:string, ContractID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractWhseBinRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContracts(" + Company + "," + ContractID + ")/PlanContractWhseBins", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractWhseBinRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlanContractWhseBin item
   Description: Calls GetByID to retrieve the PlanContractWhseBin item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlanContractWhseBin1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractID Desc: ContractID   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlanContractWhseBinRow
   */  
export function get_PlanContracts_Company_ContractID_PlanContractWhseBins_Company_ContractID_WarehouseCode_BinNum(Company:string, ContractID:string, WarehouseCode:string, BinNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlanContractWhseBinRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContracts(" + Company + "," + ContractID + ")/PlanContractWhseBins(" + Company + "," + ContractID + "," + WarehouseCode + "," + BinNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PlanContractWhseBinRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PlanContractDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlanContractDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlanContractDtlRow
   */  
export function get_PlanContractDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlanContractDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlanContractDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlanContractDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlanContractDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlanContractDtl item
   Description: Calls GetByID to retrieve the PlanContractDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlanContractDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractID Desc: ContractID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlanContractDtlRow
   */  
export function get_PlanContractDtls_Company_ContractID_LineNum(Company:string, ContractID:string, LineNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlanContractDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDtls(" + Company + "," + ContractID + "," + LineNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PlanContractDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PlanContractDtl for the service
   Description: Calls UpdateExt to update PlanContractDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlanContractDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractID Desc: ContractID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlanContractDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PlanContractDtls_Company_ContractID_LineNum(Company:string, ContractID:string, LineNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDtls(" + Company + "," + ContractID + "," + LineNum + ")", {
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
   Summary: Call UpdateExt to delete PlanContractDtl item
   Description: Call UpdateExt to delete PlanContractDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlanContractDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractID Desc: ContractID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PlanContractDtls_Company_ContractID_LineNum(Company:string, ContractID:string, LineNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDtls(" + Company + "," + ContractID + "," + LineNum + ")", {
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
   Description: Get PlanContractWhseBins items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlanContractWhseBins
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlanContractWhseBinRow
   */  
export function get_PlanContractWhseBins(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractWhseBinRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractWhseBins", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractWhseBinRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlanContractWhseBins
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlanContractWhseBinRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlanContractWhseBinRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlanContractWhseBins(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractWhseBins", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlanContractWhseBin item
   Description: Calls GetByID to retrieve the PlanContractWhseBin item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlanContractWhseBin
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractID Desc: ContractID   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlanContractWhseBinRow
   */  
export function get_PlanContractWhseBins_Company_ContractID_WarehouseCode_BinNum(Company:string, ContractID:string, WarehouseCode:string, BinNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlanContractWhseBinRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractWhseBins(" + Company + "," + ContractID + "," + WarehouseCode + "," + BinNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PlanContractWhseBinRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PlanContractWhseBin for the service
   Description: Calls UpdateExt to update PlanContractWhseBin. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlanContractWhseBin
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractID Desc: ContractID   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlanContractWhseBinRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PlanContractWhseBins_Company_ContractID_WarehouseCode_BinNum(Company:string, ContractID:string, WarehouseCode:string, BinNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractWhseBins(" + Company + "," + ContractID + "," + WarehouseCode + "," + BinNum + ")", {
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
   Summary: Call UpdateExt to delete PlanContractWhseBin item
   Description: Call UpdateExt to delete PlanContractWhseBin item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlanContractWhseBin
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ContractID Desc: ContractID   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PlanContractWhseBins_Company_ContractID_WarehouseCode_BinNum(Company:string, ContractID:string, WarehouseCode:string, BinNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractWhseBins(" + Company + "," + ContractID + "," + WarehouseCode + "," + BinNum + ")", {
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
   Description: Get PlanContractDmdDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlanContractDmdDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlanContractDmdDtlRow
   */  
export function get_PlanContractDmdDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractDmdDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDmdDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractDmdDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlanContractDmdDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlanContractDmdDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlanContractDmdDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlanContractDmdDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDmdDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlanContractDmdDtl item
   Description: Calls GetByID to retrieve the PlanContractDmdDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlanContractDmdDtl
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlanContractDmdDtlRow
   */  
export function get_PlanContractDmdDtls_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlanContractDmdDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDmdDtls(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PlanContractDmdDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PlanContractDmdDtl for the service
   Description: Calls UpdateExt to update PlanContractDmdDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlanContractDmdDtl
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlanContractDmdDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PlanContractDmdDtls_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDmdDtls(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete PlanContractDmdDtl item
   Description: Call UpdateExt to delete PlanContractDmdDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlanContractDmdDtl
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PlanContractDmdDtls_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDmdDtls(" + SysRowID + ")", {
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
   Description: Get PlanContractDmdHdrs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlanContractDmdHdrs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlanContractDmdHdrRow
   */  
export function get_PlanContractDmdHdrs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractDmdHdrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDmdHdrs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractDmdHdrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlanContractDmdHdrs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlanContractDmdHdrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlanContractDmdHdrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlanContractDmdHdrs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDmdHdrs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlanContractDmdHdr item
   Description: Calls GetByID to retrieve the PlanContractDmdHdr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlanContractDmdHdr
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlanContractDmdHdrRow
   */  
export function get_PlanContractDmdHdrs_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlanContractDmdHdrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDmdHdrs(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PlanContractDmdHdrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PlanContractDmdHdr for the service
   Description: Calls UpdateExt to update PlanContractDmdHdr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlanContractDmdHdr
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlanContractDmdHdrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PlanContractDmdHdrs_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDmdHdrs(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete PlanContractDmdHdr item
   Description: Call UpdateExt to delete PlanContractDmdHdr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlanContractDmdHdr
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PlanContractDmdHdrs_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractDmdHdrs(" + SysRowID + ")", {
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
   Description: Get PlanContractSplyDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlanContractSplyDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlanContractSplyDtlRow
   */  
export function get_PlanContractSplyDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractSplyDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractSplyDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractSplyDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlanContractSplyDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlanContractSplyDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlanContractSplyDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlanContractSplyDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractSplyDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlanContractSplyDtl item
   Description: Calls GetByID to retrieve the PlanContractSplyDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlanContractSplyDtl
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlanContractSplyDtlRow
   */  
export function get_PlanContractSplyDtls_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlanContractSplyDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractSplyDtls(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PlanContractSplyDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PlanContractSplyDtl for the service
   Description: Calls UpdateExt to update PlanContractSplyDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlanContractSplyDtl
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlanContractSplyDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PlanContractSplyDtls_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractSplyDtls(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete PlanContractSplyDtl item
   Description: Call UpdateExt to delete PlanContractSplyDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlanContractSplyDtl
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PlanContractSplyDtls_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractSplyDtls(" + SysRowID + ")", {
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
   Description: Get PlanContractSplyHdrs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlanContractSplyHdrs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlanContractSplyHdrRow
   */  
export function get_PlanContractSplyHdrs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractSplyHdrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractSplyHdrs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractSplyHdrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlanContractSplyHdrs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlanContractSplyHdrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlanContractSplyHdrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlanContractSplyHdrs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractSplyHdrs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlanContractSplyHdr item
   Description: Calls GetByID to retrieve the PlanContractSplyHdr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlanContractSplyHdr
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlanContractSplyHdrRow
   */  
export function get_PlanContractSplyHdrs_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlanContractSplyHdrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractSplyHdrs(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PlanContractSplyHdrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PlanContractSplyHdr for the service
   Description: Calls UpdateExt to update PlanContractSplyHdr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlanContractSplyHdr
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlanContractSplyHdrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PlanContractSplyHdrs_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractSplyHdrs(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete PlanContractSplyHdr item
   Description: Call UpdateExt to delete PlanContractSplyHdr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlanContractSplyHdr
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PlanContractSplyHdrs_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractSplyHdrs(" + SysRowID + ")", {
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
   Description: Get PlanContractTranDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlanContractTranDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlanContractTranDtlRow
   */  
export function get_PlanContractTranDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractTranDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractTranDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractTranDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlanContractTranDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlanContractTranDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlanContractTranDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlanContractTranDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractTranDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlanContractTranDtl item
   Description: Calls GetByID to retrieve the PlanContractTranDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlanContractTranDtl
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlanContractTranDtlRow
   */  
export function get_PlanContractTranDtls_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlanContractTranDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractTranDtls(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PlanContractTranDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PlanContractTranDtl for the service
   Description: Calls UpdateExt to update PlanContractTranDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlanContractTranDtl
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlanContractTranDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PlanContractTranDtls_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractTranDtls(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete PlanContractTranDtl item
   Description: Call UpdateExt to delete PlanContractTranDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlanContractTranDtl
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PlanContractTranDtls_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractTranDtls(" + SysRowID + ")", {
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
   Description: Get PlanContractTranHdrs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlanContractTranHdrs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlanContractTranHdrRow
   */  
export function get_PlanContractTranHdrs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractTranHdrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractTranHdrs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractTranHdrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlanContractTranHdrs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlanContractTranHdrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlanContractTranHdrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlanContractTranHdrs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractTranHdrs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlanContractTranHdr item
   Description: Calls GetByID to retrieve the PlanContractTranHdr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlanContractTranHdr
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlanContractTranHdrRow
   */  
export function get_PlanContractTranHdrs_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlanContractTranHdrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractTranHdrs(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PlanContractTranHdrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PlanContractTranHdr for the service
   Description: Calls UpdateExt to update PlanContractTranHdr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlanContractTranHdr
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlanContractTranHdrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PlanContractTranHdrs_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractTranHdrs(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete PlanContractTranHdr item
   Description: Call UpdateExt to delete PlanContractTranHdr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlanContractTranHdr
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PlanContractTranHdrs_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PlanContractTranHdrs(" + SysRowID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlanContractHdrListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractHdrListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractHdrListRow)
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
export function get_GetRows(whereClausePlanContractHdr:string, whereClausePlanContractDtl:string, whereClausePlanContractWhseBin:string, whereClausePlanContractDmdDtl:string, whereClausePlanContractDmdHdr:string, whereClausePlanContractSplyDtl:string, whereClausePlanContractSplyHdr:string, whereClausePlanContractTranDtl:string, whereClausePlanContractTranHdr:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePlanContractHdr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePlanContractHdr=" + whereClausePlanContractHdr
   }
   if(typeof whereClausePlanContractDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePlanContractDtl=" + whereClausePlanContractDtl
   }
   if(typeof whereClausePlanContractWhseBin!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePlanContractWhseBin=" + whereClausePlanContractWhseBin
   }
   if(typeof whereClausePlanContractDmdDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePlanContractDmdDtl=" + whereClausePlanContractDmdDtl
   }
   if(typeof whereClausePlanContractDmdHdr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePlanContractDmdHdr=" + whereClausePlanContractDmdHdr
   }
   if(typeof whereClausePlanContractSplyDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePlanContractSplyDtl=" + whereClausePlanContractSplyDtl
   }
   if(typeof whereClausePlanContractSplyHdr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePlanContractSplyHdr=" + whereClausePlanContractSplyHdr
   }
   if(typeof whereClausePlanContractTranDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePlanContractTranDtl=" + whereClausePlanContractTranDtl
   }
   if(typeof whereClausePlanContractTranHdr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePlanContractTranHdr=" + whereClausePlanContractTranHdr
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/GetRows" + params, {
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
export function get_GetByID(contractID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof contractID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "contractID=" + contractID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/GetList" + params, {
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
   Summary: Invoke method ExistsInventoryOrReceivingBin
   Description: Validates PlanContractHdr.Active column changing:
1.-If a contract is flagged as inactive and there is stock in the warehouse / bin location defined at the contract, then a warning message should be shown.
   OperationID: ExistsInventoryOrReceivingBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsInventoryOrReceivingBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsInventoryOrReceivingBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExistsInventoryOrReceivingBin(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/ExistsInventoryOrReceivingBin", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeActive
   Description: Validates PlanContractHdr.Active column changing:
1.-If a contract is flagged as inactive and there is stock in the warehouse / bin location defined at the contract, then a warning message should be shown.
   OperationID: OnChangeActive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeActive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeActive_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeActive(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/OnChangeActive", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeWhseBinDefaultInvWhseBin
   Description: Validates PlanContractWhseBin.DefaultInvWhseBin column changing:
   OperationID: OnChangeWhseBinDefaultInvWhseBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWhseBinDefaultInvWhseBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWhseBinDefaultInvWhseBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeWhseBinDefaultInvWhseBin(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/OnChangeWhseBinDefaultInvWhseBin", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeWhseBinDefaultRcvWhseBin
   Description: Validates PlanContractWhseBin.DefaultRcvWhseBin column changing:
   OperationID: OnChangeWhseBinDefaultRcvWhseBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWhseBinDefaultRcvWhseBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWhseBinDefaultRcvWhseBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeWhseBinDefaultRcvWhseBin(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/OnChangeWhseBinDefaultRcvWhseBin", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeWhseBinBackflushBin
   Description: Validates PlanContractWhseBin.BackflushBin column changing:
   OperationID: OnChangeWhseBinBackflushBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWhseBinBackflushBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWhseBinBackflushBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeWhseBinBackflushBin(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/OnChangeWhseBinBackflushBin", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeWhseBinWarehouseCode
   Description: Validates PlanContractWhseBin.WarehouseCode column changing:
1.- The WarehouseCode field should only allow warehouses with at least one bin location flagged as contract bin.
2.-The same combination of warehouse/bin is only allowed once for all the active contracts.
   OperationID: OnChangeWhseBinWarehouseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWhseBinWarehouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWhseBinWarehouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeWhseBinWarehouseCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/OnChangeWhseBinWarehouseCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePlanContractDtlWarehouseCode
   Description: Validates PlanContractDtl.WarehouseCode column changing:
1.- The WarehouseCode field should only allow warehouses with at least one bin location flagged as contract bin.
2.-The same combination of warehouse/bin must exist in PlanContractWhseBin
   OperationID: OnChangePlanContractDtlWarehouseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePlanContractDtlWarehouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePlanContractDtlWarehouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePlanContractDtlWarehouseCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/OnChangePlanContractDtlWarehouseCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDtlBinNum
   Description: Validates PlanContractDtl.BinNum column changing:
1.-The BinNum field should only allow bins that have a “Contract” Type.
2.-The same combination of warehouse/bin is only allowed once for all the active contracts.
   OperationID: OnChangeDtlBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDtlBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDtlBinNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/OnChangeDtlBinNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeWhseBinNum
   Description: Validates PlanContractWhseBin.BinNum column changing:
1.-The BinNum field should only allow bins that have a “Contract” Type.
2.-The same combination of warehouse/bin is only allowed once for all the active contracts.
   OperationID: OnChangeWhseBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWhseBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWhseBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeWhseBinNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/OnChangeWhseBinNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Validates PlanContractDtl.PartNum column changing:
1.-	Sales Kits parts are not allowed in contract lines.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/OnChangePartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangingAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingAttributeSet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/OnChangingAttributeSet", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingRevisionNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/OnChangingRevisionNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetContractHdrDmdRows
   Description: Get the dataset of Contract Demand Header.
   OperationID: GetContractHdrDmdRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContractHdrDmdRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContractHdrDmdRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContractHdrDmdRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/GetContractHdrDmdRows", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetContractDtlDmdRows
   Description: Get the dataset of Contract Demand Lines.
   OperationID: GetContractDtlDmdRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContractDtlDmdRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContractDtlDmdRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContractDtlDmdRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/GetContractDtlDmdRows", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetContractHdrTranRows
   Description: Get the dataset of Contract Transaction Header.
   OperationID: GetContractHdrTranRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContractHdrTranRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContractHdrTranRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContractHdrTranRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/GetContractHdrTranRows", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetContractDtlTranRows
   Description: Get the dataset of Contract Transaction Header.
   OperationID: GetContractDtlTranRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContractDtlTranRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContractDtlTranRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContractDtlTranRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/GetContractDtlTranRows", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetContractSplyRows
   Description: Get the dataset for Plan Contract Supply (Hdr or Dtl).
If param sPart has value you get PlanContractSplyDtl table otherwhise PlanContractSplyHdr table(all parts).
   OperationID: GetContractSplyRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContractSplyRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContractSplyRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContractSplyRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/GetContractSplyRows", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/PartPlantIsLinkedToContract", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePlanContractHdrinDiffPlant
   Description: Validate whether the ContractID belongs to another plant.
   OperationID: ValidatePlanContractHdrinDiffPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePlanContractHdrinDiffPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePlanContractHdrinDiffPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePlanContractHdrinDiffPlant(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/ValidatePlanContractHdrinDiffPlant", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeContractDemandQuantities
   Description: Update Plan Contract Detail information when the Contract UOM or Contrcat Qty changes
   OperationID: ChangeContractDemandQuantities
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeContractDemandQuantities_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeContractDemandQuantities_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeContractDemandQuantities(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/ChangeContractDemandQuantities", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPlanContractHdr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlanContractHdr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPlanContractHdr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlanContractHdr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPlanContractHdr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/GetNewPlanContractHdr", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPlanContractDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlanContractDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPlanContractDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlanContractDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPlanContractDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/GetNewPlanContractDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPlanContractWhseBin
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlanContractWhseBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPlanContractWhseBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlanContractWhseBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPlanContractWhseBin(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/GetNewPlanContractWhseBin", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlanContractSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractDmdDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlanContractDmdDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractDmdHdrRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlanContractDmdHdrRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlanContractDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractHdrListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlanContractHdrListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractHdrRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlanContractHdrRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractSplyDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlanContractSplyDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractSplyHdrRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlanContractSplyHdrRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractTranDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlanContractTranDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractTranHdrRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlanContractTranHdrRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlanContractWhseBinRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlanContractWhseBinRow[],
}

export interface Erp_Tablesets_PlanContractDmdDtlRow{
   "AssemblySeq":number,
   "Company":string,
   "ContractID":string,
   "DueDate":string,
   "IUM":string,
   "JobNum":string,
   "LineNum":number,
   "MtlSeq":number,
   "OrderLine":number,
   "OrderNum":number,
   "OrderRelNum":number,
   "RequiredQty":number,
   "SourceName":string,
   "TFOrdLine":number,
   "TFOrdNum":string,
   "TFLineNum":string,
   "PartNum":string,
   "PartDescription":string,
      /**  ID of related Attribute Class  */  
   "AttrClassID":string,
      /**  Description of values in set  */  
   "AttributeSetDesc":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   "AttributeSetShortDesc":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PlanContractDmdHdrRow{
   "AssemblySeq":number,
   "Company":string,
   "ContractID":string,
   "DueDate":string,
   "IUM":string,
   "JobNum":string,
   "MtlSeq":number,
   "OrderLine":number,
   "OrderNum":number,
   "OrderRelNum":number,
   "RequiredQty":number,
   "SourceName":string,
   "TFOrdLine":number,
   "TFOrdNum":string,
   "TFLineNum":string,
   "PartNum":string,
   "PartDescription":string,
      /**  ID of related Attribute Class  */  
   "AttrClassID":string,
      /**  Description of values in set  */  
   "AttributeSetDesc":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   "AttributeSetShortDesc":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PlanContractDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The unique identifier of the planning contract.  */  
   "ContractID":string,
      /**  The unique identifier of the planning contract line.  */  
   "LineNum":number,
      /**  A unique part number that identifies this part. Sales Kits not allowed. Same part number can only be entered once in the same contract.  */  
   "PartNum":string,
      /**  Describes the Part.  */  
   "PartDescription":string,
      /**  The quantity that the user defined that the planning contract needs to plan ahead.  */  
   "ContractQty":number,
      /**  ContractUOM  */  
   "ContractUOM":string,
      /**  Due date of the planning contract line.  */  
   "DueDate":string,
      /**  The planning contract line comments.  */  
   "Comments":string,
      /**  OurContractQty  */  
   "OurContractQty":number,
      /**  The portion of the contract quantity that has been consumed for the demands linked to this planning contract. This is calculated when MRP is executed.  */  
   "ConsumedQty":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  The portion of the demand linked to the contract that has been already satisfied.  */  
   "CompletedQty":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Indicates the Job Material warehouse location. Optional. Warehouse must exist in PlanContractWhseBin.  */  
   "WarehouseCode":string,
      /**  Indicates the Job Material bin location. Optional. Bin must exist in PlanContractWhseBin.  */  
   "BinNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  The portion of the contract quantity that has not been consumed yet. Calculated as Contract Qty – Consumed Qty.  */  
   "UnconsumedQty":number,
      /**  Inventory UOM that the Plan ContractDetail Part is allocated against.  */  
   "InvtyUOM":string,
      /**  The Contract Quantity expressed in the Inventory Unit of Measure  */  
   "ThisContractInvtyQty":number,
      /**  The portion of the contract quantity that has been Consumed but it is not yet been Completed. Calculated as Completed Qty - Consumed Qty.  */  
   "ThisOpenQty":number,
   "OnHandQty":number,
      /**  ID of related Attribute Class  */  
   "AttrClassID":string,
      /**  Description of values in set  */  
   "AttributeSetDesc":string,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   "AttributeSetShortDesc":string,
   "EnableAttributeSetSearch":boolean,
      /**  Site identifier.  */  
   "Plant":string,
   "BitFlag":number,
   "BinNumDescription":string,
   "DynAttrValueSetDescription":string,
   "DynAttrValueSetShortDescription":string,
   "PartNumTrackDimension":boolean,
   "PartNumIUM":string,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumAttrClassID":string,
   "PartNumPartDescription":string,
   "PartNumSellingFactor":number,
   "PartNumTrackLots":boolean,
   "PartNumPricePerCode":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumSalesUM":string,
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PlanContractHdrListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The unique identifier of the planning contract.  */  
   "ContractID":string,
      /**  Planning Contract Description.  */  
   "Description":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  The planning contract header comments.  */  
   "Comments":string,
      /**  The ID of the Planner.  */  
   "PlannerID":string,
      /**  The user ID that created this planning contract.  */  
   "CreatedBy":string,
      /**  Indicates if the planning contract have been approved.  */  
   "Approved":boolean,
      /**  Indicates the inventory warehouse location. This location is defaulted from the setting at the site level but it can be changed at the contract level. Only warehouses with at least one bin location flagged as contract bin are allowed.  */  
   "WarehouseCode":string,
      /**  Indicates the inventory bin location. Only bins of “Contract” Type are allowed.  */  
   "BinNum":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PlanContractHdrRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The unique identifier of the planning contract.  */  
   "ContractID":string,
      /**  Planning Contract Description.  */  
   "Description":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  The planning contract header comments.  */  
   "Comments":string,
      /**  The ID of the Planner.  */  
   "PlannerID":string,
      /**  The user ID that created this planning contract.  */  
   "CreatedBy":string,
      /**  Indicates if the planning contract have been approved.  */  
   "Approved":boolean,
      /**  Indicates the inventory warehouse location. This location is defaulted from the setting at the site level but it can be changed at the contract level. Only warehouses with at least one bin location flagged as contract bin are allowed.  */  
   "WarehouseCode":string,
      /**  Indicates the inventory bin location. Only bins of “Contract” Type are allowed.  */  
   "BinNum":string,
      /**  Indicates if the planning contract is active.  */  
   "Active":boolean,
      /**  Controls the action that is to be taken when an inventory move (receipt, issue, return) is going to be done to a bin other than the contract bin selected for the contract.  */  
   "NonPCBinAction":string,
      /**  The ID of the Buyer.  */  
   "BuyerID":string,
      /**  Default Warehouse that received the item.  Only warehouses with at least one bin location flagged as contract bin are allowed.  */  
   "RcvWhse":string,
      /**  Default Bin location of the warehouse which received the item. Only bins of “Contract” Type are allowed.  */  
   "RcvBin":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Controls the action that is to be taken when an inventory move (issue, shipment) is going to be done from a contract bin to other location outside the contract.  */  
   "NonPCOutsideAction":string,
   "BuyerIDName":string,
   "BitFlag":number,
   "BinNumDescription":string,
   "PersonName":string,
   "PlantName":string,
   "RcvBinDescription":string,
   "RcvWhseDescription":string,
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PlanContractSplyDtlRow{
   "BinDescription":string,
   "BinNum":string,
   "Company":string,
   "ContractID":string,
   "LineNum":number,
   "LotNum":string,
   "PartDescription":string,
   "PartNum":string,
   "Plant":string,
   "WarehouseCode":string,
   "WarehouseDesc":string,
   "PlantName":string,
   "DueDate":string,
   "JobNum":string,
   "POLine":number,
   "PONum":number,
   "IUM":string,
   "PORelNum":number,
   "ReceiptQty":number,
   "SourceName":string,
   "SugNum":number,
   "TFLineNum":string,
   "TFOrdLine":number,
   "TFOrdNum":string,
      /**  ID of related Attribute Class  */  
   "AttrClassID":string,
      /**  Description of values in set  */  
   "AttributeSetDesc":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   "AttributeSetShortDesc":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PlanContractSplyHdrRow{
   "BinDescription":string,
   "BinNum":string,
   "Company":string,
   "ContractID":string,
   "LotNum":string,
   "PartDescription":string,
   "PartNum":string,
   "Plant":string,
   "WarehouseCode":string,
   "WarehouseDesc":string,
   "PlantName":string,
   "DueDate":string,
   "IUM":string,
   "JobNum":string,
   "POLine":number,
   "PONum":number,
   "PORelNum":number,
   "ReceiptQty":number,
   "SourceName":string,
   "SugNum":number,
   "TFLineNum":string,
   "TFOrdLine":number,
   "TFOrdNum":string,
      /**  ID of related Attribute Class  */  
   "AttrClassID":string,
      /**  Description of values in set  */  
   "AttributeSetDesc":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   "AttributeSetShortDesc":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PlanContractTranDtlRow{
      /**  Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM. Related to PartTran. TranQty which is the ActTranQty converted into the Parts Primary Inventory UO  */  
   "ActTranQty":number,
      /**  Actual Unit of Measure of the ActTransQty.  */  
   "ActTransUOM":string,
      /**  Bin Description  */  
   "BinDescription":string,
      /**  Identifies the Bin location that this transaction affected.  */  
   "BinNum":string,
      /**  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  */  
   "BinType":string,
      /**  Burden Unit Cost  */  
   "BurUnitCost":number,
      /**  Reference to the service call that the material is being issued for.  */  
   "CallNum":number,
      /**  Company Identifier.  */  
   "Company":string,
      /**  The unique identifier of the planning contract.  */  
   "ContractID":string,
      /**  Unique dimension code for the part.  */  
   "DimCode":string,
      /**  Dim Code Description  */  
   "DimCodeDesc":string,
      /**  Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure. Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   "DimConvFactor":number,
      /**  Dimension Quantity  */  
   "DimQty":number,
      /**  Drop shipment Packing Slip.  */  
   "DropShipPackSlip":string,
      /**  Dimension unit of measure.  */  
   "DUM":string,
      /**  This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit. This field is set equal to the Login ID variable. It can not be overridden.  */  
   "EntryPerson":string,
      /**  Extended Cost is calculated as (TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  */  
   "ExtCost":number,
      /**  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  */  
   "InventoryTrans":boolean,
      /**  Job Number that transaction is associated with.  */  
   "JobNum":string,
      /**  Labor Unit Cost  */  
   "LbrUnitCost":number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
   "LotNum":string,
      /**  Miscelaneous Shipment Entry Packing ID  */  
   "MiscShipPackID":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   "MtlBurdenUnitCost":number,
      /**  Material Burden Unit Cost  */  
   "MtlBurUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlLabUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlMtlUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlSubUnitCost":number,
      /**  Material Unit Cost  */  
   "MtlUnitCost":number,
      /**  The sales order number that this detail shipment line is linked to. This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  */  
   "OrderNum":number,
   "Packer":string,
      /**  Packing slip number.  */  
   "PackNum":number,
      /**  Vendors Packing Slip #.  */  
   "PackSlip":string,
      /**  Part description that this transaction is for.  */  
   "PartDescription":string,
      /**  Part Number that this transaction is for.  */  
   "PartNum":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Plant Name.  */  
   "PlantName":string,
      /**  Created by Purchase Order Receipt Process.  */  
   "PONum":number,
      /**  Full description of Reason... used on displays/reports.  */  
   "ReasonDesc":string,
      /**  RMA Number  */  
   "RMANum":number,
      /**  Calculated Running Total  */  
   "RunningTotal":number,
      /**  RunningTotal UOM  */  
   "RunningTotalUOM":string,
      /**  Subcontractor Shipment Packing ID  */  
   "SubConShipPackID":number,
      /**  Subcontract Unit Cost  */  
   "SubUnitCost":number,
      /**  System date at time that record was created.  */  
   "SysDate":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   "SysTime":number,
      /**  PackID from Transfer Order Packing type  */  
   "TOPackID":number,
      /**  Date of transaction.  */  
   "TranDate":string,
      /**  A number which is used to allow create a unique key for the file.  */  
   "TranNum":number,
      /**  Transaction Quantity. Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran. UM This is the UOM that the unit costs are based on. The actual Transaction quatity is found in ActTranQty  */  
   "TranQty":number,
      /**  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  */  
   "TranReference":string,
      /**  Field that indicates the type of transaction: ADJ-CST -  Adjustment to Stock Cost. ADJ-DEM - Adjustment to Demand Quantity. ADJ-MTL - Adjustment to Job Cost Material. ADJ-PUR - Purchase Price variance (created by A/P invoice) ADJ-QTY - Adjustment to  */  
   "TranType":string,
      /**  Unit of Measure.  (part primary inventory uom)  */  
   "UM":string,
      /**  Warehouse that transaction is applied to  */  
   "WarehouseCode":string,
      /**  Warehouse description.  */  
   "WarehouseDesc":string,
      /**  ID of related Attribute Class  */  
   "AttrClassID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   "AttributeSetShortDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PlanContractTranHdrRow{
      /**  Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM. Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UO  */  
   "ActTranQty":number,
      /**  Actual Unit of Measure of the ActTransQty.  */  
   "ActTransUOM":string,
   "BinDescription":string,
      /**  Identifies the Bin location that this transaction affected.  */  
   "BinNum":string,
      /**  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  */  
   "BinType":string,
      /**  Burden Unit Cost  */  
   "BurUnitCost":number,
      /**  Reference to the service call that the material is being issued for.  */  
   "CallNum":number,
      /**  Company Identifier.  */  
   "Company":string,
      /**  The unique identifier of the planning contract.  */  
   "ContractID":string,
      /**  Unique dimension code for the part.  */  
   "DimCode":string,
      /**  Dim Code Description  */  
   "DimCodeDesc":string,
      /**  Dimension conversion factor. This conversion factor is used to convert the qty to the base part unit of measure. Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   "DimConvFactor":number,
      /**  Dimension Quantity  */  
   "DimQty":number,
      /**  Drop shipment Packing Slip.  */  
   "DropShipPackSlip":string,
      /**  Dimension unit of measure.  */  
   "DUM":string,
      /**  This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit. This field is set equal to the Login ID variable. It can not be overridden.  */  
   "EntryPerson":string,
      /**  Extended Cost is calculated as (TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  */  
   "ExtCost":number,
      /**  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  */  
   "InventoryTrans":boolean,
      /**  Job Number that transaction is associated with.  */  
   "JobNum":string,
      /**  Labor Unit Cost  */  
   "LbrUnitCost":number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  Lot Number  */  
   "LotNum":string,
      /**  Miscelaneous Shipment Entry Packing ID  */  
   "MiscShipPackID":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   "MtlBurdenUnitCost":number,
      /**  Material Burden Unit Cost  */  
   "MtlBurUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlLabUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlMtlUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlSubUnitCost":number,
      /**  Material Unit Cost  */  
   "MtlUnitCost":number,
      /**  The sales order number that this detail shipment line is linked to. This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  */  
   "OrderNum":number,
   "Packer":string,
      /**  Packing slip number.  */  
   "PackNum":number,
      /**  Vendors Packing Slip #.  */  
   "PackSlip":string,
      /**  Part description that this transaction is for.  */  
   "PartDescription":string,
      /**  Part Number that this transaction is for.  */  
   "PartNum":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Plant Name.  */  
   "PlantName":string,
      /**  Created by Purchase Order Receipt Process.  */  
   "PONum":number,
      /**  Full description of Reason... used on displays/reports.  */  
   "ReasonDesc":string,
      /**  RMA Number  */  
   "RMANum":number,
      /**  Calculated Running Total  */  
   "RunningTotal":number,
      /**  RunningTotal UOM  */  
   "RunningTotalUOM":string,
      /**  Subcontractor Shipment Packing ID  */  
   "SubConShipPackID":number,
      /**  Subcontract Unit Cost  */  
   "SubUnitCost":number,
      /**  System date at time that record was created.  */  
   "SysDate":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   "SysTime":number,
      /**  PackID from Transfer Order Packing type  */  
   "TOPackID":number,
      /**  Date of transaction.  */  
   "TranDate":string,
      /**  A number which is used to allow create a unique key for the file.  */  
   "TranNum":number,
      /**  Transaction Quantity. Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran. UM This is the UOM that the unit costs are based on. The actual Transaction quatity is found in ActTranQty  */  
   "TranQty":number,
      /**  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  */  
   "TranReference":string,
      /**  Field that indicates the type of transaction: ADJ-CST -  Adjustment to Stock Cost. ADJ-DEM - Adjustment to Demand Quantity. ADJ-MTL - Adjustment to Job Cost Material. ADJ-PUR - Purchase Price variance (created by A/P invoice) ADJ-QTY - Adjustment to  */  
   "TranType":string,
      /**  Unit of Measure.  (part primary inventory uom)  */  
   "UM":string,
      /**  Warehouse that transaction is applied to  */  
   "WarehouseCode":string,
      /**  Warehouse description.  */  
   "WarehouseDesc":string,
      /**  ID of related Attribute Class  */  
   "AttrClassID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   "AttributeSetShortDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PlanContractWhseBinRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The unique identifier of the planning contract.  */  
   "ContractID":string,
      /**  Indicates the warehouse location. Only warehouses with at least one bin location flagged as contract bin are allowed.  */  
   "WarehouseCode":string,
      /**  Indicates the bin location. Only bins of “Contract” Type are allowed.  */  
   "BinNum":string,
      /**  Indicates if the warehouse/bin combination is the default Inventory warehouse/bin.  */  
   "DefaultInvWhseBin":boolean,
      /**  Indicates if the warehouse/bin combination is the default Receiving warehouse/bin.  */  
   "DefaultRcvWhseBin":boolean,
      /**  Indicates if the warehouse/bin combination is the Backflush warehouse/bin.  */  
   "BackflushBin":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Site identifier.  */  
   "Plant":string,
   "BitFlag":number,
   "BinNumDescription":string,
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param partNum
      @param contractQty
      @param contractUOM
      @param consumedQty
      @param completedQty
   */  
export interface ChangeContractDemandQuantities_input{
      /**  partNum  */  
   partNum:string,
      /**  contractQty  */  
   contractQty:number,
      /**  contractUOM  */  
   contractUOM:string,
      /**  consumedQty  */  
   consumedQty:number,
      /**  completedQty  */  
   completedQty:number,
}

export interface ChangeContractDemandQuantities_output{
parameters : {
      /**  output parameters  */  
   outThisContractInvtyQty:number,
   outThisOpenQty:number,
   outUnconsumedQty:number,
   outCompletedQty:number,
}
}

   /** Required : 
      @param contractID
   */  
export interface DeleteByID_input{
   contractID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PlanContractDmdDtlRow{
   AssemblySeq:number,
   Company:string,
   ContractID:string,
   DueDate:string,
   IUM:string,
   JobNum:string,
   LineNum:number,
   MtlSeq:number,
   OrderLine:number,
   OrderNum:number,
   OrderRelNum:number,
   RequiredQty:number,
   SourceName:string,
   TFOrdLine:number,
   TFOrdNum:string,
   TFLineNum:string,
   PartNum:string,
   PartDescription:string,
      /**  ID of related Attribute Class  */  
   AttrClassID:string,
      /**  Description of values in set  */  
   AttributeSetDesc:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   AttributeSetShortDesc:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlanContractDmdHdrRow{
   AssemblySeq:number,
   Company:string,
   ContractID:string,
   DueDate:string,
   IUM:string,
   JobNum:string,
   MtlSeq:number,
   OrderLine:number,
   OrderNum:number,
   OrderRelNum:number,
   RequiredQty:number,
   SourceName:string,
   TFOrdLine:number,
   TFOrdNum:string,
   TFLineNum:string,
   PartNum:string,
   PartDescription:string,
      /**  ID of related Attribute Class  */  
   AttrClassID:string,
      /**  Description of values in set  */  
   AttributeSetDesc:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   AttributeSetShortDesc:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlanContractDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The unique identifier of the planning contract.  */  
   ContractID:string,
      /**  The unique identifier of the planning contract line.  */  
   LineNum:number,
      /**  A unique part number that identifies this part. Sales Kits not allowed. Same part number can only be entered once in the same contract.  */  
   PartNum:string,
      /**  Describes the Part.  */  
   PartDescription:string,
      /**  The quantity that the user defined that the planning contract needs to plan ahead.  */  
   ContractQty:number,
      /**  ContractUOM  */  
   ContractUOM:string,
      /**  Due date of the planning contract line.  */  
   DueDate:string,
      /**  The planning contract line comments.  */  
   Comments:string,
      /**  OurContractQty  */  
   OurContractQty:number,
      /**  The portion of the contract quantity that has been consumed for the demands linked to this planning contract. This is calculated when MRP is executed.  */  
   ConsumedQty:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  The portion of the demand linked to the contract that has been already satisfied.  */  
   CompletedQty:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Indicates the Job Material warehouse location. Optional. Warehouse must exist in PlanContractWhseBin.  */  
   WarehouseCode:string,
      /**  Indicates the Job Material bin location. Optional. Bin must exist in PlanContractWhseBin.  */  
   BinNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  The portion of the contract quantity that has not been consumed yet. Calculated as Contract Qty – Consumed Qty.  */  
   UnconsumedQty:number,
      /**  Inventory UOM that the Plan ContractDetail Part is allocated against.  */  
   InvtyUOM:string,
      /**  The Contract Quantity expressed in the Inventory Unit of Measure  */  
   ThisContractInvtyQty:number,
      /**  The portion of the contract quantity that has been Consumed but it is not yet been Completed. Calculated as Completed Qty - Consumed Qty.  */  
   ThisOpenQty:number,
   OnHandQty:number,
      /**  ID of related Attribute Class  */  
   AttrClassID:string,
      /**  Description of values in set  */  
   AttributeSetDesc:string,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   AttributeSetShortDesc:string,
   EnableAttributeSetSearch:boolean,
      /**  Site identifier.  */  
   Plant:string,
   BitFlag:number,
   BinNumDescription:string,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
   PartNumTrackDimension:boolean,
   PartNumIUM:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumTrackInventoryByRevision:boolean,
   PartNumAttrClassID:string,
   PartNumPartDescription:string,
   PartNumSellingFactor:number,
   PartNumTrackLots:boolean,
   PartNumPricePerCode:string,
   PartNumTrackSerialNum:boolean,
   PartNumSalesUM:string,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlanContractHdrListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The unique identifier of the planning contract.  */  
   ContractID:string,
      /**  Planning Contract Description.  */  
   Description:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  The planning contract header comments.  */  
   Comments:string,
      /**  The ID of the Planner.  */  
   PlannerID:string,
      /**  The user ID that created this planning contract.  */  
   CreatedBy:string,
      /**  Indicates if the planning contract have been approved.  */  
   Approved:boolean,
      /**  Indicates the inventory warehouse location. This location is defaulted from the setting at the site level but it can be changed at the contract level. Only warehouses with at least one bin location flagged as contract bin are allowed.  */  
   WarehouseCode:string,
      /**  Indicates the inventory bin location. Only bins of “Contract” Type are allowed.  */  
   BinNum:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlanContractHdrListTableset{
   PlanContractHdrList:Erp_Tablesets_PlanContractHdrListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PlanContractHdrRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The unique identifier of the planning contract.  */  
   ContractID:string,
      /**  Planning Contract Description.  */  
   Description:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  The planning contract header comments.  */  
   Comments:string,
      /**  The ID of the Planner.  */  
   PlannerID:string,
      /**  The user ID that created this planning contract.  */  
   CreatedBy:string,
      /**  Indicates if the planning contract have been approved.  */  
   Approved:boolean,
      /**  Indicates the inventory warehouse location. This location is defaulted from the setting at the site level but it can be changed at the contract level. Only warehouses with at least one bin location flagged as contract bin are allowed.  */  
   WarehouseCode:string,
      /**  Indicates the inventory bin location. Only bins of “Contract” Type are allowed.  */  
   BinNum:string,
      /**  Indicates if the planning contract is active.  */  
   Active:boolean,
      /**  Controls the action that is to be taken when an inventory move (receipt, issue, return) is going to be done to a bin other than the contract bin selected for the contract.  */  
   NonPCBinAction:string,
      /**  The ID of the Buyer.  */  
   BuyerID:string,
      /**  Default Warehouse that received the item.  Only warehouses with at least one bin location flagged as contract bin are allowed.  */  
   RcvWhse:string,
      /**  Default Bin location of the warehouse which received the item. Only bins of “Contract” Type are allowed.  */  
   RcvBin:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Controls the action that is to be taken when an inventory move (issue, shipment) is going to be done from a contract bin to other location outside the contract.  */  
   NonPCOutsideAction:string,
   BuyerIDName:string,
   BitFlag:number,
   BinNumDescription:string,
   PersonName:string,
   PlantName:string,
   RcvBinDescription:string,
   RcvWhseDescription:string,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlanContractSplyDtlRow{
   BinDescription:string,
   BinNum:string,
   Company:string,
   ContractID:string,
   LineNum:number,
   LotNum:string,
   PartDescription:string,
   PartNum:string,
   Plant:string,
   WarehouseCode:string,
   WarehouseDesc:string,
   PlantName:string,
   DueDate:string,
   JobNum:string,
   POLine:number,
   PONum:number,
   IUM:string,
   PORelNum:number,
   ReceiptQty:number,
   SourceName:string,
   SugNum:number,
   TFLineNum:string,
   TFOrdLine:number,
   TFOrdNum:string,
      /**  ID of related Attribute Class  */  
   AttrClassID:string,
      /**  Description of values in set  */  
   AttributeSetDesc:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   AttributeSetShortDesc:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlanContractSplyHdrRow{
   BinDescription:string,
   BinNum:string,
   Company:string,
   ContractID:string,
   LotNum:string,
   PartDescription:string,
   PartNum:string,
   Plant:string,
   WarehouseCode:string,
   WarehouseDesc:string,
   PlantName:string,
   DueDate:string,
   IUM:string,
   JobNum:string,
   POLine:number,
   PONum:number,
   PORelNum:number,
   ReceiptQty:number,
   SourceName:string,
   SugNum:number,
   TFLineNum:string,
   TFOrdLine:number,
   TFOrdNum:string,
      /**  ID of related Attribute Class  */  
   AttrClassID:string,
      /**  Description of values in set  */  
   AttributeSetDesc:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   AttributeSetShortDesc:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlanContractTableset{
   PlanContractHdr:Erp_Tablesets_PlanContractHdrRow[],
   PlanContractDtl:Erp_Tablesets_PlanContractDtlRow[],
   PlanContractWhseBin:Erp_Tablesets_PlanContractWhseBinRow[],
   PlanContractDmdDtl:Erp_Tablesets_PlanContractDmdDtlRow[],
   PlanContractDmdHdr:Erp_Tablesets_PlanContractDmdHdrRow[],
   PlanContractSplyDtl:Erp_Tablesets_PlanContractSplyDtlRow[],
   PlanContractSplyHdr:Erp_Tablesets_PlanContractSplyHdrRow[],
   PlanContractTranDtl:Erp_Tablesets_PlanContractTranDtlRow[],
   PlanContractTranHdr:Erp_Tablesets_PlanContractTranHdrRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PlanContractTranDtlRow{
      /**  Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM. Related to PartTran. TranQty which is the ActTranQty converted into the Parts Primary Inventory UO  */  
   ActTranQty:number,
      /**  Actual Unit of Measure of the ActTransQty.  */  
   ActTransUOM:string,
      /**  Bin Description  */  
   BinDescription:string,
      /**  Identifies the Bin location that this transaction affected.  */  
   BinNum:string,
      /**  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  */  
   BinType:string,
      /**  Burden Unit Cost  */  
   BurUnitCost:number,
      /**  Reference to the service call that the material is being issued for.  */  
   CallNum:number,
      /**  Company Identifier.  */  
   Company:string,
      /**  The unique identifier of the planning contract.  */  
   ContractID:string,
      /**  Unique dimension code for the part.  */  
   DimCode:string,
      /**  Dim Code Description  */  
   DimCodeDesc:string,
      /**  Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure. Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   DimConvFactor:number,
      /**  Dimension Quantity  */  
   DimQty:number,
      /**  Drop shipment Packing Slip.  */  
   DropShipPackSlip:string,
      /**  Dimension unit of measure.  */  
   DUM:string,
      /**  This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit. This field is set equal to the Login ID variable. It can not be overridden.  */  
   EntryPerson:string,
      /**  Extended Cost is calculated as (TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  */  
   ExtCost:number,
      /**  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  */  
   InventoryTrans:boolean,
      /**  Job Number that transaction is associated with.  */  
   JobNum:string,
      /**  Labor Unit Cost  */  
   LbrUnitCost:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
   LotNum:string,
      /**  Miscelaneous Shipment Entry Packing ID  */  
   MiscShipPackID:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   MtlBurdenUnitCost:number,
      /**  Material Burden Unit Cost  */  
   MtlBurUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlLabUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlMtlUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlSubUnitCost:number,
      /**  Material Unit Cost  */  
   MtlUnitCost:number,
      /**  The sales order number that this detail shipment line is linked to. This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  */  
   OrderNum:number,
   Packer:string,
      /**  Packing slip number.  */  
   PackNum:number,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  Part description that this transaction is for.  */  
   PartDescription:string,
      /**  Part Number that this transaction is for.  */  
   PartNum:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Plant Name.  */  
   PlantName:string,
      /**  Created by Purchase Order Receipt Process.  */  
   PONum:number,
      /**  Full description of Reason... used on displays/reports.  */  
   ReasonDesc:string,
      /**  RMA Number  */  
   RMANum:number,
      /**  Calculated Running Total  */  
   RunningTotal:number,
      /**  RunningTotal UOM  */  
   RunningTotalUOM:string,
      /**  Subcontractor Shipment Packing ID  */  
   SubConShipPackID:number,
      /**  Subcontract Unit Cost  */  
   SubUnitCost:number,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   SysTime:number,
      /**  PackID from Transfer Order Packing type  */  
   TOPackID:number,
      /**  Date of transaction.  */  
   TranDate:string,
      /**  A number which is used to allow create a unique key for the file.  */  
   TranNum:number,
      /**  Transaction Quantity. Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran. UM This is the UOM that the unit costs are based on. The actual Transaction quatity is found in ActTranQty  */  
   TranQty:number,
      /**  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  */  
   TranReference:string,
      /**  Field that indicates the type of transaction: ADJ-CST -  Adjustment to Stock Cost. ADJ-DEM - Adjustment to Demand Quantity. ADJ-MTL - Adjustment to Job Cost Material. ADJ-PUR - Purchase Price variance (created by A/P invoice) ADJ-QTY - Adjustment to  */  
   TranType:string,
      /**  Unit of Measure.  (part primary inventory uom)  */  
   UM:string,
      /**  Warehouse that transaction is applied to  */  
   WarehouseCode:string,
      /**  Warehouse description.  */  
   WarehouseDesc:string,
      /**  ID of related Attribute Class  */  
   AttrClassID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   AttributeSetShortDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlanContractTranHdrRow{
      /**  Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM. Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UO  */  
   ActTranQty:number,
      /**  Actual Unit of Measure of the ActTransQty.  */  
   ActTransUOM:string,
   BinDescription:string,
      /**  Identifies the Bin location that this transaction affected.  */  
   BinNum:string,
      /**  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  */  
   BinType:string,
      /**  Burden Unit Cost  */  
   BurUnitCost:number,
      /**  Reference to the service call that the material is being issued for.  */  
   CallNum:number,
      /**  Company Identifier.  */  
   Company:string,
      /**  The unique identifier of the planning contract.  */  
   ContractID:string,
      /**  Unique dimension code for the part.  */  
   DimCode:string,
      /**  Dim Code Description  */  
   DimCodeDesc:string,
      /**  Dimension conversion factor. This conversion factor is used to convert the qty to the base part unit of measure. Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   DimConvFactor:number,
      /**  Dimension Quantity  */  
   DimQty:number,
      /**  Drop shipment Packing Slip.  */  
   DropShipPackSlip:string,
      /**  Dimension unit of measure.  */  
   DUM:string,
      /**  This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit. This field is set equal to the Login ID variable. It can not be overridden.  */  
   EntryPerson:string,
      /**  Extended Cost is calculated as (TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  */  
   ExtCost:number,
      /**  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  */  
   InventoryTrans:boolean,
      /**  Job Number that transaction is associated with.  */  
   JobNum:string,
      /**  Labor Unit Cost  */  
   LbrUnitCost:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  Lot Number  */  
   LotNum:string,
      /**  Miscelaneous Shipment Entry Packing ID  */  
   MiscShipPackID:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   MtlBurdenUnitCost:number,
      /**  Material Burden Unit Cost  */  
   MtlBurUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlLabUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlMtlUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlSubUnitCost:number,
      /**  Material Unit Cost  */  
   MtlUnitCost:number,
      /**  The sales order number that this detail shipment line is linked to. This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  */  
   OrderNum:number,
   Packer:string,
      /**  Packing slip number.  */  
   PackNum:number,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  Part description that this transaction is for.  */  
   PartDescription:string,
      /**  Part Number that this transaction is for.  */  
   PartNum:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Plant Name.  */  
   PlantName:string,
      /**  Created by Purchase Order Receipt Process.  */  
   PONum:number,
      /**  Full description of Reason... used on displays/reports.  */  
   ReasonDesc:string,
      /**  RMA Number  */  
   RMANum:number,
      /**  Calculated Running Total  */  
   RunningTotal:number,
      /**  RunningTotal UOM  */  
   RunningTotalUOM:string,
      /**  Subcontractor Shipment Packing ID  */  
   SubConShipPackID:number,
      /**  Subcontract Unit Cost  */  
   SubUnitCost:number,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   SysTime:number,
      /**  PackID from Transfer Order Packing type  */  
   TOPackID:number,
      /**  Date of transaction.  */  
   TranDate:string,
      /**  A number which is used to allow create a unique key for the file.  */  
   TranNum:number,
      /**  Transaction Quantity. Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran. UM This is the UOM that the unit costs are based on. The actual Transaction quatity is found in ActTranQty  */  
   TranQty:number,
      /**  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  */  
   TranReference:string,
      /**  Field that indicates the type of transaction: ADJ-CST -  Adjustment to Stock Cost. ADJ-DEM - Adjustment to Demand Quantity. ADJ-MTL - Adjustment to Job Cost Material. ADJ-PUR - Purchase Price variance (created by A/P invoice) ADJ-QTY - Adjustment to  */  
   TranType:string,
      /**  Unit of Measure.  (part primary inventory uom)  */  
   UM:string,
      /**  Warehouse that transaction is applied to  */  
   WarehouseCode:string,
      /**  Warehouse description.  */  
   WarehouseDesc:string,
      /**  ID of related Attribute Class  */  
   AttrClassID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   AttributeSetShortDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlanContractWhseBinRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The unique identifier of the planning contract.  */  
   ContractID:string,
      /**  Indicates the warehouse location. Only warehouses with at least one bin location flagged as contract bin are allowed.  */  
   WarehouseCode:string,
      /**  Indicates the bin location. Only bins of “Contract” Type are allowed.  */  
   BinNum:string,
      /**  Indicates if the warehouse/bin combination is the default Inventory warehouse/bin.  */  
   DefaultInvWhseBin:boolean,
      /**  Indicates if the warehouse/bin combination is the default Receiving warehouse/bin.  */  
   DefaultRcvWhseBin:boolean,
      /**  Indicates if the warehouse/bin combination is the Backflush warehouse/bin.  */  
   BackflushBin:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Site identifier.  */  
   Plant:string,
   BitFlag:number,
   BinNumDescription:string,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtPlanContractTableset{
   PlanContractHdr:Erp_Tablesets_PlanContractHdrRow[],
   PlanContractDtl:Erp_Tablesets_PlanContractDtlRow[],
   PlanContractWhseBin:Erp_Tablesets_PlanContractWhseBinRow[],
   PlanContractDmdDtl:Erp_Tablesets_PlanContractDmdDtlRow[],
   PlanContractDmdHdr:Erp_Tablesets_PlanContractDmdHdrRow[],
   PlanContractSplyDtl:Erp_Tablesets_PlanContractSplyDtlRow[],
   PlanContractSplyHdr:Erp_Tablesets_PlanContractSplyHdrRow[],
   PlanContractTranDtl:Erp_Tablesets_PlanContractTranDtlRow[],
   PlanContractTranHdr:Erp_Tablesets_PlanContractTranHdrRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
   */  
export interface ExistsInventoryOrReceivingBin_input{
   ds:Erp_Tablesets_PlanContractTableset[],
}

export interface ExistsInventoryOrReceivingBin_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlanContractTableset[],
   invOrRec:string,
}
}

   /** Required : 
      @param contractID
   */  
export interface GetByID_input{
   contractID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PlanContractTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PlanContractTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PlanContractTableset[],
}

   /** Required : 
      @param sCompany
      @param sContractID
      @param sPart
      @param sAttributeSetID
   */  
export interface GetContractDtlDmdRows_input{
   sCompany:string,
   sContractID:string,
   sPart:string,
   sAttributeSetID:number,
}

export interface GetContractDtlDmdRows_output{
   returnObj:Erp_Tablesets_PlanContractTableset[],
}

   /** Required : 
      @param sCompany
      @param sContractID
      @param sPart
      @param sAttributeSetID
   */  
export interface GetContractDtlTranRows_input{
   sCompany:string,
   sContractID:string,
   sPart:string,
   sAttributeSetID:number,
}

export interface GetContractDtlTranRows_output{
   returnObj:Erp_Tablesets_PlanContractTableset[],
}

   /** Required : 
      @param sCompany
      @param sContractID
   */  
export interface GetContractHdrDmdRows_input{
   sCompany:string,
   sContractID:string,
}

export interface GetContractHdrDmdRows_output{
   returnObj:Erp_Tablesets_PlanContractTableset[],
}

   /** Required : 
      @param sCompany
      @param sContractID
   */  
export interface GetContractHdrTranRows_input{
   sCompany:string,
   sContractID:string,
}

export interface GetContractHdrTranRows_output{
   returnObj:Erp_Tablesets_PlanContractTableset[],
}

   /** Required : 
      @param sCompany
      @param sContractID
      @param sPart
      @param sAttributeSetID
   */  
export interface GetContractSplyRows_input{
   sCompany:string,
   sContractID:string,
   sPart:string,
   sAttributeSetID:number,
}

export interface GetContractSplyRows_output{
   returnObj:Erp_Tablesets_PlanContractTableset[],
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
   returnObj:Erp_Tablesets_PlanContractHdrListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param contractID
   */  
export interface GetNewPlanContractDtl_input{
   ds:Erp_Tablesets_PlanContractTableset[],
   contractID:string,
}

export interface GetNewPlanContractDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlanContractTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPlanContractHdr_input{
   ds:Erp_Tablesets_PlanContractTableset[],
}

export interface GetNewPlanContractHdr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlanContractTableset[],
}
}

   /** Required : 
      @param ds
      @param contractID
      @param warehouseCode
   */  
export interface GetNewPlanContractWhseBin_input{
   ds:Erp_Tablesets_PlanContractTableset[],
   contractID:string,
   warehouseCode:string,
}

export interface GetNewPlanContractWhseBin_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlanContractTableset[],
}
}

   /** Required : 
      @param whereClausePlanContractHdr
      @param whereClausePlanContractDtl
      @param whereClausePlanContractWhseBin
      @param whereClausePlanContractDmdDtl
      @param whereClausePlanContractDmdHdr
      @param whereClausePlanContractSplyDtl
      @param whereClausePlanContractSplyHdr
      @param whereClausePlanContractTranDtl
      @param whereClausePlanContractTranHdr
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePlanContractHdr:string,
   whereClausePlanContractDtl:string,
   whereClausePlanContractWhseBin:string,
   whereClausePlanContractDmdDtl:string,
   whereClausePlanContractDmdHdr:string,
   whereClausePlanContractSplyDtl:string,
   whereClausePlanContractSplyHdr:string,
   whereClausePlanContractTranDtl:string,
   whereClausePlanContractTranHdr:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PlanContractTableset[],
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
      @param Active
   */  
export interface OnChangeActive_input{
   ds:Erp_Tablesets_PlanContractTableset[],
   Active:boolean,
}

export interface OnChangeActive_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlanContractTableset[],
}
}

   /** Required : 
      @param ds
      @param sBinNum
   */  
export interface OnChangeDtlBinNum_input{
   ds:Erp_Tablesets_PlanContractTableset[],
   sBinNum:string,
}

export interface OnChangeDtlBinNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlanContractTableset[],
   sBinNum:string,
}
}

   /** Required : 
      @param ds
      @param sPartNum
   */  
export interface OnChangePartNum_input{
   ds:Erp_Tablesets_PlanContractTableset[],
   sPartNum:string,
}

export interface OnChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlanContractTableset[],
   sPartNum:string,
}
}

   /** Required : 
      @param ds
      @param WarehouseCode
   */  
export interface OnChangePlanContractDtlWarehouseCode_input{
   ds:Erp_Tablesets_PlanContractTableset[],
   WarehouseCode:string,
}

export interface OnChangePlanContractDtlWarehouseCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlanContractTableset[],
}
}

   /** Required : 
      @param ds
      @param ipBackflushBin
   */  
export interface OnChangeWhseBinBackflushBin_input{
   ds:Erp_Tablesets_PlanContractTableset[],
   ipBackflushBin:boolean,
}

export interface OnChangeWhseBinBackflushBin_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlanContractTableset[],
}
}

   /** Required : 
      @param ds
      @param ipDefaultInvWhseBin
   */  
export interface OnChangeWhseBinDefaultInvWhseBin_input{
   ds:Erp_Tablesets_PlanContractTableset[],
   ipDefaultInvWhseBin:boolean,
}

export interface OnChangeWhseBinDefaultInvWhseBin_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlanContractTableset[],
}
}

   /** Required : 
      @param ds
      @param ipDefaultRcvWhseBin
   */  
export interface OnChangeWhseBinDefaultRcvWhseBin_input{
   ds:Erp_Tablesets_PlanContractTableset[],
   ipDefaultRcvWhseBin:boolean,
}

export interface OnChangeWhseBinDefaultRcvWhseBin_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlanContractTableset[],
}
}

   /** Required : 
      @param ds
      @param sBinNum
   */  
export interface OnChangeWhseBinNum_input{
   ds:Erp_Tablesets_PlanContractTableset[],
   sBinNum:string,
}

export interface OnChangeWhseBinNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlanContractTableset[],
   sBinNum:string,
}
}

   /** Required : 
      @param ds
      @param WarehouseCode
   */  
export interface OnChangeWhseBinWarehouseCode_input{
   ds:Erp_Tablesets_PlanContractTableset[],
   WarehouseCode:string,
}

export interface OnChangeWhseBinWarehouseCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlanContractTableset[],
}
}

   /** Required : 
      @param attributeSetID
      @param ds
   */  
export interface OnChangingAttributeSet_input{
   attributeSetID:number,
   ds:Erp_Tablesets_PlanContractTableset[],
}

export interface OnChangingAttributeSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlanContractTableset[],
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_PlanContractTableset[],
}

export interface OnChangingRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlanContractTableset[],
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
   ds:Erp_Tablesets_UpdExtPlanContractTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPlanContractTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PlanContractTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlanContractTableset[],
}
}

   /** Required : 
      @param sCompany
      @param sPlant
      @param sContractID
   */  
export interface ValidatePlanContractHdrinDiffPlant_input{
   sCompany:string,
   sPlant:string,
   sContractID:string,
}

export interface ValidatePlanContractHdrinDiffPlant_output{
}

