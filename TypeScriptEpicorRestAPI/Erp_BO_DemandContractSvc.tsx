import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.DemandContractSvc
// Description: Add your summary for this object here
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/$metadata", {
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
   Description: Get DemandContracts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandContracts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DmdCntHdrRow
   */  
export function get_DemandContracts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntHdrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DemandContracts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntHdrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandContracts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DmdCntHdrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DmdCntHdrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DemandContracts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DemandContracts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DemandContract item
   Description: Calls GetByID to retrieve the DemandContract item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandContract
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DmdCntHdrRow
   */  
export function get_DemandContracts_Company_DemandContractNum(Company:string, DemandContractNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DmdCntHdrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DemandContracts(" + Company + "," + DemandContractNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DmdCntHdrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DemandContract for the service
   Description: Calls UpdateExt to update DemandContract. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandContract
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DmdCntHdrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DemandContracts_Company_DemandContractNum(Company:string, DemandContractNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DemandContracts(" + Company + "," + DemandContractNum + ")", {
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
   Summary: Call UpdateExt to delete DemandContract item
   Description: Call UpdateExt to delete DemandContract item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandContract
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DemandContracts_Company_DemandContractNum(Company:string, DemandContractNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DemandContracts(" + Company + "," + DemandContractNum + ")", {
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
   Description: Get DmdCntDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DmdCntDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DmdCntDtlRow
   */  
export function get_DemandContracts_Company_DemandContractNum_DmdCntDtls(Company:string, DemandContractNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DemandContracts(" + Company + "," + DemandContractNum + ")/DmdCntDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DmdCntDtl item
   Description: Calls GetByID to retrieve the DmdCntDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DmdCntDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandContractLine Desc: DemandContractLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DmdCntDtlRow
   */  
export function get_DemandContracts_Company_DemandContractNum_DmdCntDtls_Company_DemandContractNum_DemandContractLine(Company:string, DemandContractNum:string, DemandContractLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DmdCntDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DemandContracts(" + Company + "," + DemandContractNum + ")/DmdCntDtls(" + Company + "," + DemandContractNum + "," + DemandContractLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DmdCntDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get DmdCntHdrAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DmdCntHdrAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DmdCntHdrAttchRow
   */  
export function get_DemandContracts_Company_DemandContractNum_DmdCntHdrAttches(Company:string, DemandContractNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntHdrAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DemandContracts(" + Company + "," + DemandContractNum + ")/DmdCntHdrAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntHdrAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DmdCntHdrAttch item
   Description: Calls GetByID to retrieve the DmdCntHdrAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DmdCntHdrAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DmdCntHdrAttchRow
   */  
export function get_DemandContracts_Company_DemandContractNum_DmdCntHdrAttches_Company_DemandContractNum_DrawingSeq(Company:string, DemandContractNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DmdCntHdrAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DemandContracts(" + Company + "," + DemandContractNum + ")/DmdCntHdrAttches(" + Company + "," + DemandContractNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DmdCntHdrAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get DmdCntDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DmdCntDtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DmdCntDtlRow
   */  
export function get_DmdCntDtls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DmdCntDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DmdCntDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DmdCntDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DmdCntDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DmdCntDtl item
   Description: Calls GetByID to retrieve the DmdCntDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DmdCntDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandContractLine Desc: DemandContractLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DmdCntDtlRow
   */  
export function get_DmdCntDtls_Company_DemandContractNum_DemandContractLine(Company:string, DemandContractNum:string, DemandContractLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DmdCntDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntDtls(" + Company + "," + DemandContractNum + "," + DemandContractLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DmdCntDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DmdCntDtl for the service
   Description: Calls UpdateExt to update DmdCntDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DmdCntDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandContractLine Desc: DemandContractLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DmdCntDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DmdCntDtls_Company_DemandContractNum_DemandContractLine(Company:string, DemandContractNum:string, DemandContractLine:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntDtls(" + Company + "," + DemandContractNum + "," + DemandContractLine + ")", {
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
   Summary: Call UpdateExt to delete DmdCntDtl item
   Description: Call UpdateExt to delete DmdCntDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DmdCntDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandContractLine Desc: DemandContractLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DmdCntDtls_Company_DemandContractNum_DemandContractLine(Company:string, DemandContractNum:string, DemandContractLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntDtls(" + Company + "," + DemandContractNum + "," + DemandContractLine + ")", {
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
   Description: Get DmdCntDtlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DmdCntDtlAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandContractLine Desc: DemandContractLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DmdCntDtlAttchRow
   */  
export function get_DmdCntDtls_Company_DemandContractNum_DemandContractLine_DmdCntDtlAttches(Company:string, DemandContractNum:string, DemandContractLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntDtls(" + Company + "," + DemandContractNum + "," + DemandContractLine + ")/DmdCntDtlAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DmdCntDtlAttch item
   Description: Calls GetByID to retrieve the DmdCntDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DmdCntDtlAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandContractLine Desc: DemandContractLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DmdCntDtlAttchRow
   */  
export function get_DmdCntDtls_Company_DemandContractNum_DemandContractLine_DmdCntDtlAttches_Company_DemandContractNum_DemandContractLine_DrawingSeq(Company:string, DemandContractNum:string, DemandContractLine:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DmdCntDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntDtls(" + Company + "," + DemandContractNum + "," + DemandContractLine + ")/DmdCntDtlAttches(" + Company + "," + DemandContractNum + "," + DemandContractLine + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DmdCntDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get DmdCntDtlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DmdCntDtlAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DmdCntDtlAttchRow
   */  
export function get_DmdCntDtlAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntDtlAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DmdCntDtlAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DmdCntDtlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DmdCntDtlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DmdCntDtlAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntDtlAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DmdCntDtlAttch item
   Description: Calls GetByID to retrieve the DmdCntDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DmdCntDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandContractLine Desc: DemandContractLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DmdCntDtlAttchRow
   */  
export function get_DmdCntDtlAttches_Company_DemandContractNum_DemandContractLine_DrawingSeq(Company:string, DemandContractNum:string, DemandContractLine:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DmdCntDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntDtlAttches(" + Company + "," + DemandContractNum + "," + DemandContractLine + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DmdCntDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DmdCntDtlAttch for the service
   Description: Calls UpdateExt to update DmdCntDtlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DmdCntDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandContractLine Desc: DemandContractLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DmdCntDtlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DmdCntDtlAttches_Company_DemandContractNum_DemandContractLine_DrawingSeq(Company:string, DemandContractNum:string, DemandContractLine:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntDtlAttches(" + Company + "," + DemandContractNum + "," + DemandContractLine + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete DmdCntDtlAttch item
   Description: Call UpdateExt to delete DmdCntDtlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DmdCntDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandContractLine Desc: DemandContractLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DmdCntDtlAttches_Company_DemandContractNum_DemandContractLine_DrawingSeq(Company:string, DemandContractNum:string, DemandContractLine:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntDtlAttches(" + Company + "," + DemandContractNum + "," + DemandContractLine + "," + DrawingSeq + ")", {
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
   Description: Get DmdCntHdrAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DmdCntHdrAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DmdCntHdrAttchRow
   */  
export function get_DmdCntHdrAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntHdrAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntHdrAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntHdrAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DmdCntHdrAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DmdCntHdrAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DmdCntHdrAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DmdCntHdrAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntHdrAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DmdCntHdrAttch item
   Description: Calls GetByID to retrieve the DmdCntHdrAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DmdCntHdrAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DmdCntHdrAttchRow
   */  
export function get_DmdCntHdrAttches_Company_DemandContractNum_DrawingSeq(Company:string, DemandContractNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DmdCntHdrAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntHdrAttches(" + Company + "," + DemandContractNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DmdCntHdrAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DmdCntHdrAttch for the service
   Description: Calls UpdateExt to update DmdCntHdrAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DmdCntHdrAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DmdCntHdrAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DmdCntHdrAttches_Company_DemandContractNum_DrawingSeq(Company:string, DemandContractNum:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntHdrAttches(" + Company + "," + DemandContractNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete DmdCntHdrAttch item
   Description: Call UpdateExt to delete DmdCntHdrAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DmdCntHdrAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DmdCntHdrAttches_Company_DemandContractNum_DrawingSeq(Company:string, DemandContractNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntHdrAttches(" + Company + "," + DemandContractNum + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DmdCntHdrListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntHdrListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntHdrListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseDmdCntHdr:string, whereClauseDmdCntHdrAttch:string, whereClauseDmdCntDtl:string, whereClauseDmdCntDtlAttch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseDmdCntHdr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDmdCntHdr=" + whereClauseDmdCntHdr
   }
   if(typeof whereClauseDmdCntHdrAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDmdCntHdrAttch=" + whereClauseDmdCntHdrAttch
   }
   if(typeof whereClauseDmdCntDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDmdCntDtl=" + whereClauseDmdCntDtl
   }
   if(typeof whereClauseDmdCntDtlAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDmdCntDtlAttch=" + whereClauseDmdCntDtlAttch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/GetRows" + params, {
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
export function get_GetByID(demandContractNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof demandContractNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "demandContractNum=" + demandContractNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/GetList" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/FindPart", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/GetPartFromRowID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCurrValue
   Description: To change the currency value
   OperationID: ChangeCurrValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCurrValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCurrValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCurrValue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/ChangeCurrValue", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeLineUnitPrice
   Description: Called when the contract line unit price is changing
   OperationID: ChangeLineUnitPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLineUnitPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLineUnitPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeLineUnitPrice(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/ChangeLineUnitPrice", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDCDtlSellingTotalContractQty
   Description: Update DmdCntDtl information when Customer Part Number is changed.
   OperationID: ChangeDCDtlSellingTotalContractQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDCDtlSellingTotalContractQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDCDtlSellingTotalContractQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDCDtlSellingTotalContractQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/ChangeDCDtlSellingTotalContractQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDCDtlTotalContractQtyUOM
   Description: Update DmdCntDtl Totals UOM when TotalContract Quantity UOM is changed.
   OperationID: ChangeDCDtlTotalContractQtyUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDCDtlTotalContractQtyUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDCDtlTotalContractQtyUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDCDtlTotalContractQtyUOM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/ChangeDCDtlTotalContractQtyUOM", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDmdCntDtlMktgCamp
   Description: Update MktgCampaign on the DmdCntDtl.
   OperationID: ChangeDmdCntDtlMktgCamp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDmdCntDtlMktgCamp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDmdCntDtlMktgCamp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDmdCntDtlMktgCamp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/ChangeDmdCntDtlMktgCamp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDmdCntDtlMktgEvnt
   Description: Update MktgEvnt on the DmdCntDtl.
   OperationID: ChangeDmdCntDtlMktgEvnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDmdCntDtlMktgEvnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDmdCntDtlMktgEvnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDmdCntDtlMktgEvnt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/ChangeDmdCntDtlMktgEvnt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDmdCntDtlPartNum
   Description: Update DmdCntDtl information when Part Number is changed.
   OperationID: ChangeDmdCntDtlPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDmdCntDtlPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDmdCntDtlPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDmdCntDtlPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/ChangeDmdCntDtlPartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDmdCntDtlProject
   Description: Update ProjectID on the DmdCntDtl.
   OperationID: ChangeDmdCntDtlProject
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDmdCntDtlProject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDmdCntDtlProject_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDmdCntDtlProject(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/ChangeDmdCntDtlProject", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDmdCntDtlPriceTolerance
   OperationID: ChangeDmdCntDtlPriceTolerance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDmdCntDtlPriceTolerance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDmdCntDtlPriceTolerance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDmdCntDtlPriceTolerance(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/ChangeDmdCntDtlPriceTolerance", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDmdCntDtlXPartNum
   Description: Update DmdCntDtl infomation when Customer Part Number is changed.
   OperationID: ChangeDmdCntDtlXPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDmdCntDtlXPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDmdCntDtlXPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDmdCntDtlXPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/ChangeDmdCntDtlXPartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDmdCntHdrBTCustNum
   Description: Update DmdCntHdr information when Bill To Customer is changed.
   OperationID: ChangeDmdCntHdrBTCustNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDmdCntHdrBTCustNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDmdCntHdrBTCustNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDmdCntHdrBTCustNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/ChangeDmdCntHdrBTCustNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDmdCntHdrCustID
   Description: Update Order Header information with values from the Sold To when the Sold To is changed.
   OperationID: ChangeDmdCntHdrCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDmdCntHdrCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDmdCntHdrCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDmdCntHdrCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/ChangeDmdCntHdrCustID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDmdCntHdrProject
   Description: Update ProjectID on the DmdCntHdr.
   OperationID: ChangeDmdCntHdrProject
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDmdCntHdrProject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDmdCntHdrProject_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDmdCntHdrProject(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/ChangeDmdCntHdrProject", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CloseDmdCntHdr
   Description: Closes the Demand Contract Header.
   OperationID: CloseDmdCntHdr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseDmdCntHdr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseDmdCntHdr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CloseDmdCntHdr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/CloseDmdCntHdr", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByDemandContractCustID
   Description: Gets row by DemandContract.
   OperationID: GetByDemandContractCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByDemandContractCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByDemandContractCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByDemandContractCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/GetByDemandContractCustID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByDmdCntTradingPartner
   Description: Gets row by DemandContract.
   OperationID: GetByDmdCntTradingPartner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByDmdCntTradingPartner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByDmdCntTradingPartner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByDmdCntTradingPartner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/GetByDmdCntTradingPartner", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetContractNumByID
   Description: Gets contract number by contract id.
   OperationID: GetContractNumByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContractNumByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContractNumByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContractNumByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/GetContractNumByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshPlant
   Description: Update Plant on DemandDetail related records.
   OperationID: RefreshPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshPlant(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/RefreshPlant", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByCustNumDemandContract
   Description: Returns Demand Contract records for a customer and demand contract
   OperationID: GetByCustNumDemandContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByCustNumDemandContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByCustNumDemandContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByCustNumDemandContract(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/GetByCustNumDemandContract", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDmdCntHdr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDmdCntHdr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDmdCntHdr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDmdCntHdr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDmdCntHdr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/GetNewDmdCntHdr", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDmdCntHdrAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDmdCntHdrAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDmdCntHdrAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDmdCntHdrAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDmdCntHdrAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/GetNewDmdCntHdrAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDmdCntDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDmdCntDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDmdCntDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDmdCntDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDmdCntDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/GetNewDmdCntDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDmdCntDtlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDmdCntDtlAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDmdCntDtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDmdCntDtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDmdCntDtlAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/GetNewDmdCntDtlAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntDtlAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DmdCntDtlAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DmdCntDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntHdrAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DmdCntHdrAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntHdrListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DmdCntHdrListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntHdrRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DmdCntHdrRow[],
}

export interface Erp_Tablesets_DmdCntDtlAttchRow{
   "Company":string,
   "DemandContractNum":number,
   "DemandContractLine":number,
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

export interface Erp_Tablesets_DmdCntDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  System assigned internal number to uniquely identify the demand contract record.  Is the link to the DemandContractHdr table.  */  
   "DemandContractNum":number,
      /**  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandContractDtl record for the contract and the adding 1 to it.  */  
   "DemandContractLine":number,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.
A default should be made when the DemandContractDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table.  */  
   "PartNum":string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   "XPartNum":string,
      /**  Determines whether or not this contract line is being run in a test mode. When contracts are first set up for EDI it is useful to send all documents in test mode so trading partners can verify the data before going into production mode.  */  
   "TestRecord":boolean,
      /**  The total selling quantity expected to be ordered for this line over the life of the contract.  */  
   "SellingTotalContractQty":number,
      /**  The total quantity expected to be ordered for this line over the life of the contract.  */  
   "TotalContractQty":number,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "LineDesc":string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   "IUM":string,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the Customer.DiscountPercent.  */  
   "DiscountPercent":number,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "UnitPrice":number,
      /**  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   "PricePerCode":string,
      /**  Project ID of the Project table record for this DemandContractDtl record. Can be blank.  */  
   "ProjectID":string,
      /**  This is the Price Group ID used to price the order line with.  */  
   "PriceGroupCode":string,
      /**  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   "SalesUM":string,
      /**  Comments about the demand detail line.  */  
   "DetailComments":string,
      /**  Use standard Epicor Price matrix/logic  */  
   "UsePriceList":boolean,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Total invoice amount of orders lines invoiced for this contract line in base currency. This field has a true sign. (credit memos are negative).  */  
   "TotalInvoiceAmt":number,
      /**  Total  amount of orders for this contract line in base currency. This field has a true sign. (credit memos are negative).  */  
   "TotalOrderAmt":number,
      /**  The total actual quantity ordered for this contract line. (credit memos may change it to negative).  */  
   "TotalOrderedQty":number,
      /**  The total actual quantity shipped for this contract line. (credit memos may change it to negative).  */  
   "TotalShippedQty":number,
      /**  The total actual quantity invoiced for this contract line. (credit memos may change it to negative).  */  
   "TotalInvoicedQty":number,
      /**  Indicates if current open Order Releases that have not been shipped and do not have a job should be deleted when processing the demand.  Provides the default value for DemandDetail.  */  
   "DeleteCurrentReleases":boolean,
      /**  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via Demand Contract entry if the CRM module is installed.  */  
   "MktgCampaignID":string,
      /**   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via demand contract entry if the CRM module is installed.  */  
   "MktgEvntSeq":number,
      /**  The mininum quantity that should be for each individual demand schedule record. If the schedule quantity is less than the minimum call off quantity, a warning will be issued but processing can continue.  */  
   "MinCallOffQty":number,
      /**  Optional field that contains the  part revision.  */  
   "RevisionNum":string,
      /**  Optional field that contains the customers revision.  */  
   "XRevisionNum":string,
      /**  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  */  
   "DemandPricing":string,
      /**   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "DocUnitPrice":number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   "Rpt1UnitPrice":number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   "Rpt2UnitPrice":number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   "Rpt3UnitPrice":number,
      /**  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  */  
   "OTSmartString":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Total invoice amount of orders invoiced for this contract in document currency. This field has a true sign. (credit memos are negative).  */  
   "DocTotalInvoiceAmt":number,
      /**  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   "Rpt1TotalInvoiceAmt":number,
      /**  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   "Rpt2TotalInvoiceAmt":number,
      /**  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   "Rpt3TotalInvoiceAmt":number,
      /**  Total amount of orders for this contract in document currency. This field has a true sign. (credit memos are negative).  */  
   "DocTotalOrderAmt":number,
      /**  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   "Rpt1TotalOrderAmt":number,
      /**  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   "Rpt2TotalOrderAmt":number,
      /**  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   "Rpt3TotalOrderAmt":number,
      /**  Defines the tolerance for price difference validations.  */  
   "PriceTolerance":number,
      /**  Defines the tolerance for price difference validations in document currency.  */  
   "DocPriceTolerance":number,
      /**  Defines the tolerance for price difference validations in a report currency.  */  
   "Rpt1PriceTolerance":number,
      /**  Defines the tolerance for price difference validations in a report currency.  */  
   "Rpt2PriceTolerance":number,
      /**  Defines the tolerance for price difference validations in a report currency.  */  
   "Rpt3PriceTolerance":number,
   "CurrencyCode":string,
      /**  Indicates if this record has been selected to create a demand detail record.  Used for automatically creating DemandDetail records from contract lines.  */  
   "SelectedForDemand":boolean,
      /**  Ordered Qty, Shipped Qty, Invoiced Qty, Minimum Call Off UOM  */  
   "TotOrdShpInvCallOffQtyUOM":string,
   "CurrencySwitch":boolean,
   "BitFlag":number,
   "DemandCntHdrDemandContract":string,
   "MktgCampaignIDCampDescription":string,
   "MktgEvntEvntDescription":string,
   "PlantName":string,
   "ProjectIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DmdCntHdrAttchRow{
   "Company":string,
   "DemandContractNum":number,
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

export interface Erp_Tablesets_DmdCntHdrListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  System assigned internal number to uniquely identify the demand contract record.  The number comes from Sequence DemandContractNum.  */  
   "DemandContractNum":number,
      /**  Contains the Customer number that the demand contract is for.  This must be valid in the Customer table.  */  
   "CustNum":number,
      /**  The unique identifier of the demand contract.  This must be unique for a customer.  */  
   "DemandContract":string,
      /**  The start date of the demand contract.  */  
   "StartDate":string,
      /**  The end date of the contract.  */  
   "EndDate":string,
      /**  The number of days from today for which a scheduled quantity is considered firm.  */  
   "FirmDays":number,
      /**  The trading partner name.  */  
   "TradingPartnerName":string,
      /**  The setting for reconciling cumulative shipping quantities.  Values are:  PART - By Part  PO - By Part/PO  */  
   "CUMMSetting":string,
      /**  An optional field that describes the FOB policy.  */  
   "FOB":string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   "ShipViaCode":string,
      /**   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of DemandContractHdr.CUSTNUM use the CUSTOMER.TERMS
field as the default.  */  
   "TermsCode":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  */  
   "LockRate":boolean,
      /**  Code used to relate a AllocPri record to the order.  Defaulted from Customer.AllocPriorityCode.  */  
   "AllocPriorityCode":string,
      /**  Code used to relate a ReservePri record to the order.  Defaulted from Customer.ReservePriorityCode.  */  
   "ReservePriorityCode":string,
      /**  Indicates if the order must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases with a ship date <= the given cutoff date alos have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "O" (Ship Order 100% complete)  */  
   "ShipOrderComplete":boolean,
      /**  Comments about the demand contract.  */  
   "ContractComments":string,
      /**  Mandatory entry and must be valid. Default as the system date.  */  
   "ContractDate":string,
      /**  Project ID of the Project table record for this DemandContractHdr record. Can be blank.  */  
   "ProjectID":string,
      /**  Indicates if this contract is in an "open" status.  When a contract is closed, all DemandHead records that are associated with the contract will also be set to closed.  */  
   "OpenContract":boolean,
      /**  The user that entered the contract.  On new demand contracts use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   "EntryPerson":string,
      /**  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  */  
   "AutoOrderBasedDisc":boolean,
      /**  Bill To Customer Number  */  
   "BTCustNum":number,
      /**  Total invoice amount of orders invoiced for this contract in base currency. This field has a true sign. (credit memos are negative).  */  
   "TotalInvoiceAmt":number,
      /**  Total  amount of orders for this contract in base currency. This field has a true sign. (credit memos are negative).  */  
   "TotalOrderAmt":number,
      /**  When matching, match demands to order releases by reference number.  */  
   "MatchByRef":boolean,
      /**  When matching, match demands to order releases by ship by (reqdate) date.  */  
   "MatchByReqDate":boolean,
      /**  When matching, match demands to order releases by quantity.  */  
   "MatchByQty":boolean,
      /**  When matching, match demands to order releases by matching the first open demand and the first open release.  All subsequent open demands and releases not already matched will be matched.  Subsequent demands and releases are determined by querying the tables by reqdate.  */  
   "MatchByOpen":boolean,
      /**  Indicates where reference matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByRef is false.  */  
   "MatchSeqRef":number,
      /**  Indicates where date matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByReqDate is false.  */  
   "MatchSeqReqDate":number,
      /**  Indicates where quantity matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByQty is false.  */  
   "MatchSeqQty":number,
      /**  Indicates where open matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByOpen is false.  */  
   "MatchSeqOpen":number,
      /**  Hold for Review  */  
   "OrderHoldForReview":boolean,
      /**  Flag to decide if the non matched schedules needs to be closed.  */  
   "DemandCloseNoMatch":boolean,
      /**  Flag that state if the work flow error will be checked in every line.  */  
   "WFLockByLine":boolean,
      /**  rate group code  */  
   "RateGrpCode":string,
      /**  When true this field will indicate that Demand Schedules and Releases will only be matched if they meet all priorities listed in the Matching Priority List.  */  
   "PerfectMatch":boolean,
      /**  A list of priorities in which the matching will be executed, first items are of higher priority than items at the last of the list.  */  
   "MatchPriorityList":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  A LIST-DELIM delimited list of part options  */  
   "MatchOptionAvailList":string,
      /**  A LIST-DELIM delimited list of part options  */  
   "MatchOptSelectedList":string,
      /**  Address Name  */  
   "Name":string,
      /**  Customer Address displays on Demand Contract Summary and Header Detail Screen  */  
   "ContractAddressList":string,
      /**  FAX Number  */  
   "FAXNum":string,
      /**  Phone Number  */  
   "PhoneNum":string,
      /**  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  */  
   "AvailBTCustList":string,
   "BillToCustomerName":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "BaseCurrCurrName":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "BaseCurrCurrSymbol":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "BaseCurrCurrencyID":string,
      /**  Description of the currency  */  
   "BaseCurrCurrDesc":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "BaseCurrDocumentDesc":string,
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
   "CustomerBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustomerCustID":string,
      /**  The full name of the customer.  */  
   "CustomerName":string,
      /**  Full description of the FOB Code.  */  
   "FOBDescription":string,
      /**  Full description of Project Management Code.  */  
   "ProjectIDDescription":string,
      /**  Description of the reservation priority. Example "High".  */  
   "ReservePriDescription":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "ShipViaCodeWebDesc":string,
      /**  Full description for the shipping company (carrier).  */  
   "ShipViaCodeDescription":string,
      /**  Full description of the terms which prints on sales orders and invoices.  */  
   "TermsCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DmdCntHdrRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  System assigned internal number to uniquely identify the demand contract record.  The number comes from Sequence DemandContractNum.  */  
   "DemandContractNum":number,
      /**  Contains the Customer number that the demand contract is for.  This must be valid in the Customer table.  */  
   "CustNum":number,
   "DemandContract1":string,
      /**  The start date of the demand contract.  */  
   "StartDate":string,
      /**  The end date of the contract.  */  
   "EndDate":string,
      /**  The number of days from today for which a scheduled quantity is considered firm.  */  
   "FirmDays":number,
      /**  The trading partner name.  */  
   "TradingPartnerName":string,
      /**  The setting for reconciling cumulative shipping quantities.  Values are:  PART - By Part  PO - By Part/PO  */  
   "CUMMSetting":string,
      /**  An optional field that describes the FOB policy.  */  
   "FOB":string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   "ShipViaCode":string,
      /**   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of DemandContractHdr.CUSTNUM use the CUSTOMER.TERMS
field as the default.  */  
   "TermsCode":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  */  
   "LockRate":boolean,
      /**  Code used to relate a AllocPri record to the order.  Defaulted from Customer.AllocPriorityCode.  */  
   "AllocPriorityCode":string,
      /**  Code used to relate a ReservePri record to the order.  Defaulted from Customer.ReservePriorityCode.  */  
   "ReservePriorityCode":string,
      /**  Indicates if the order must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases with a ship date <= the given cutoff date alos have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "O" (Ship Order 100% complete)  */  
   "ShipOrderComplete":boolean,
      /**  Comments about the demand contract.  */  
   "ContractComments":string,
      /**  Mandatory entry and must be valid. Default as the system date.  */  
   "ContractDate":string,
      /**  Project ID of the Project table record for this DemandContractHdr record. Can be blank.  */  
   "ProjectID":string,
      /**  Indicates if this contract is in an "open" status.  When a contract is closed, all DemandHead records that are associated with the contract will also be set to closed.  */  
   "OpenContract":boolean,
      /**  The user that entered the contract.  On new demand contracts use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   "EntryPerson":string,
      /**  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  */  
   "AutoOrderBasedDisc":boolean,
      /**  Bill To Customer Number  */  
   "BTCustNum":number,
      /**  Total invoice amount of orders invoiced for this contract in base currency. This field has a true sign. (credit memos are negative).  */  
   "TotalInvoiceAmt":number,
      /**  Total  amount of orders for this contract in base currency. This field has a true sign. (credit memos are negative).  */  
   "TotalOrderAmt":number,
      /**  When matching, match demands to order releases by reference number.  */  
   "MatchByRef":boolean,
      /**  When matching, match demands to order releases by ship by (reqdate) date.  */  
   "MatchByReqDate":boolean,
      /**  When matching, match demands to order releases by quantity.  */  
   "MatchByQty":boolean,
      /**  When matching, match demands to order releases by matching the first open demand and the first open release.  All subsequent open demands and releases not already matched will be matched.  Subsequent demands and releases are determined by querying the tables by reqdate.  */  
   "MatchByOpen":boolean,
      /**  Indicates where reference matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByRef is false.  */  
   "MatchSeqRef":number,
      /**  Indicates where date matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByReqDate is false.  */  
   "MatchSeqReqDate":number,
      /**  Indicates where quantity matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByQty is false.  */  
   "MatchSeqQty":number,
      /**  Indicates where open matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByOpen is false.  */  
   "MatchSeqOpen":number,
      /**  Hold for Review  */  
   "OrderHoldForReview":boolean,
      /**  Flag to decide if the non matched schedules needs to be closed.  */  
   "DemandCloseNoMatch":boolean,
      /**  Flag that state if the work flow error will be checked in every line.  */  
   "WFLockByLine":boolean,
      /**  rate group code  */  
   "RateGrpCode":string,
      /**  When true this field will indicate that Demand Schedules and Releases will only be matched if they meet all priorities listed in the Matching Priority List.  */  
   "PerfectMatch":boolean,
      /**  A list of priorities in which the matching will be executed, first items are of higher priority than items at the last of the list.  */  
   "MatchPriorityList":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  This option should be defaulted to false. If the user manually turns on this flag then the system will match the schedules as it is working today. If that flag is turned off then the system will match the schedules  only and only if all the criterias selected in the matching options matches between the schedules and the releases.  */  
   "AllowNonPerfectMatch":boolean,
      /**  A LIST-DELIM delimited list of part options  */  
   "MatchOptionAvailList":string,
      /**  A LIST-DELIM delimited list of part options  */  
   "MatchOptSelectedList":string,
      /**  When TRUE, the Cancel Non Matched logic will skip any schedule whose NeedByDate is from Today until the resulting date of adding UntilDays to TODAY  */  
   "ExcludeUntil":boolean,
      /**  When TRUE, the Cancel Non Matched logic will skip any schedule whose NeedByDate is FROM the resulting date of substracting BeforeDays from TODAY and until TODAY  */  
   "ExcludeBefore":boolean,
      /**  Number of days that will be added to TODAY when ExcludeUntil is TRUE. The Cancel Non Match logic will then skip any schedule whose NeedByDate is between TODAY and the resulting date (TODAY + UntilDays).  */  
   "UntilDays":number,
      /**  Number of days that will be substracting TODAY, the resulting date will tell the Cancel Non Match to skip any schedule with a NeedByDate within this date and the current date.  */  
   "BeforeDays":number,
      /**  Total invoice amount of orders invoiced for this contract in document currency. This field has a true sign. (credit memos are negative).  */  
   "DocTotalInvoiceAmt":number,
      /**  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   "Rpt1TotalInvoiceAmt":number,
      /**  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   "Rpt2TotalInvoiceAmt":number,
      /**  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   "Rpt3TotalInvoiceAmt":number,
      /**  Total amount of orders for this contract in document currency. This field has a true sign. (credit memos are negative).  */  
   "DocTotalOrderAmt":number,
      /**  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   "Rpt1TotalOrderAmt":number,
      /**  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   "Rpt2TotalOrderAmt":number,
      /**  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   "Rpt3TotalOrderAmt":number,
      /**  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  */  
   "AvailBTCustList":string,
   "BillToCustomerName":string,
      /**  Customer Address displays on Demand Contract Summary and Header Detail Screen  */  
   "ContractAddressList":string,
      /**  FAX Number  */  
   "FAXNum":string,
      /**  Address Name  */  
   "Name":string,
      /**  Phone Number  */  
   "PhoneNum":string,
   "BaseCurrencyCode":string,
   "CurrencySwitch":boolean,
      /**  The formatted Contract Address  */  
   "ContractAddressFormatted":string,
      /**  List of available match options  */  
   "MatchOptionsList":string,
   "BitFlag":number,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeDocumentDesc":string,
   "CustomerCustID":string,
   "CustomerBTName":string,
   "CustomerName":string,
   "FOBDescription":string,
   "ProjectIDDescription":string,
   "ReservePriDescription":string,
   "ShipViaCodeDescription":string,
   "ShipViaCodeWebDesc":string,
   "TermsCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ipReplaceValue
      @param ipbaseordoc
      @param ds
   */  
export interface ChangeCurrValue_input{
      /**  ReplaceValue that was entered.  */  
   ipReplaceValue:number,
      /**  The field type - base or doc  */  
   ipbaseordoc:string,
   ds:Erp_Tablesets_DemandContractTableset[],
}

export interface ChangeCurrValue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandContractTableset[],
}
}

   /** Required : 
      @param iSellingTotalContractQty
      @param ds
   */  
export interface ChangeDCDtlSellingTotalContractQty_input{
      /**  The Selling Total Contract Quantity  */  
   iSellingTotalContractQty:number,
   ds:Erp_Tablesets_DemandContractTableset[],
}

export interface ChangeDCDtlSellingTotalContractQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandContractTableset[],
}
}

   /** Required : 
      @param iTotalContractQtyUOM
      @param ds
   */  
export interface ChangeDCDtlTotalContractQtyUOM_input{
      /**  The Total Contract Quantity  */  
   iTotalContractQtyUOM:string,
   ds:Erp_Tablesets_DemandContractTableset[],
}

export interface ChangeDCDtlTotalContractQtyUOM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandContractTableset[],
}
}

   /** Required : 
      @param iMktgCampaignID
      @param ds
   */  
export interface ChangeDmdCntDtlMktgCamp_input{
      /**  The Marketing Campaign ID  */  
   iMktgCampaignID:string,
   ds:Erp_Tablesets_DemandContractTableset[],
}

export interface ChangeDmdCntDtlMktgCamp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandContractTableset[],
}
}

   /** Required : 
      @param iMktgEvntSeq
      @param ds
   */  
export interface ChangeDmdCntDtlMktgEvnt_input{
      /**  The Marketing Event  */  
   iMktgEvntSeq:number,
   ds:Erp_Tablesets_DemandContractTableset[],
}

export interface ChangeDmdCntDtlMktgEvnt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandContractTableset[],
}
}

   /** Required : 
      @param ds
      @param iPartNum
      @param SysRowID
      @param rowType
   */  
export interface ChangeDmdCntDtlPartNum_input{
   ds:Erp_Tablesets_DemandContractTableset[],
      /**  The Part Number  */  
   iPartNum:string,
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   SysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
}

export interface ChangeDmdCntDtlPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandContractTableset[],
   iPartNum:string,
   serialWarning:string,
   questionString:string,
   multipleMatch:boolean,
}
}

   /** Required : 
      @param iPriceTolerance
      @param ds
   */  
export interface ChangeDmdCntDtlPriceTolerance_input{
   iPriceTolerance:number,
   ds:Erp_Tablesets_DemandContractTableset[],
}

export interface ChangeDmdCntDtlPriceTolerance_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandContractTableset[],
}
}

   /** Required : 
      @param iProjectID
      @param ds
   */  
export interface ChangeDmdCntDtlProject_input{
      /**  The ProjectID  */  
   iProjectID:string,
   ds:Erp_Tablesets_DemandContractTableset[],
}

export interface ChangeDmdCntDtlProject_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandContractTableset[],
}
}

   /** Required : 
      @param iPartNum
      @param iXPartNum
      @param ds
   */  
export interface ChangeDmdCntDtlXPartNum_input{
      /**  The Customer Part Number  */  
   iPartNum:string,
      /**  The Customer Part Number  */  
   iXPartNum:string,
   ds:Erp_Tablesets_DemandContractTableset[],
}

export interface ChangeDmdCntDtlXPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandContractTableset[],
}
}

   /** Required : 
      @param iBTCustNum
      @param ds
   */  
export interface ChangeDmdCntHdrBTCustNum_input{
      /**  The Bill To Customer Number  */  
   iBTCustNum:number,
   ds:Erp_Tablesets_DemandContractTableset[],
}

export interface ChangeDmdCntHdrBTCustNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandContractTableset[],
}
}

   /** Required : 
      @param iCustID
      @param ds
   */  
export interface ChangeDmdCntHdrCustID_input{
      /**  The Customer Number  */  
   iCustID:string,
   ds:Erp_Tablesets_DemandContractTableset[],
}

export interface ChangeDmdCntHdrCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandContractTableset[],
}
}

   /** Required : 
      @param iProjectID
      @param ds
   */  
export interface ChangeDmdCntHdrProject_input{
      /**  The ProjectID  */  
   iProjectID:string,
   ds:Erp_Tablesets_DemandContractTableset[],
}

export interface ChangeDmdCntHdrProject_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandContractTableset[],
}
}

   /** Required : 
      @param unitPrice
      @param baseOrDoc
      @param unitPriceOverride
      @param ds
   */  
export interface ChangeLineUnitPrice_input{
      /**  The proposed unit price value  */  
   unitPrice:number,
      /**  (B)ase or (D) unit price  */  
   baseOrDoc:string,
      /**  Indicates the user chooses to override the unit price  */  
   unitPriceOverride:boolean,
   ds:Erp_Tablesets_DemandContractTableset[],
}

export interface ChangeLineUnitPrice_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandContractTableset[],
}
}

   /** Required : 
      @param iDemandContractNum
      @param iOpenContract
   */  
export interface CloseDmdCntHdr_input{
      /**  The Demand Contract Number  */  
   iDemandContractNum:number,
      /**  The Demand Contract Number  */  
   iOpenContract:boolean,
}

export interface CloseDmdCntHdr_output{
   returnObj:Erp_Tablesets_DemandContractTableset[],
}

   /** Required : 
      @param demandContractNum
   */  
export interface DeleteByID_input{
   demandContractNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_DemandContractTableset{
   DmdCntHdr:Erp_Tablesets_DmdCntHdrRow[],
   DmdCntHdrAttch:Erp_Tablesets_DmdCntHdrAttchRow[],
   DmdCntDtl:Erp_Tablesets_DmdCntDtlRow[],
   DmdCntDtlAttch:Erp_Tablesets_DmdCntDtlAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DmdCntDtlAttchRow{
   Company:string,
   DemandContractNum:number,
   DemandContractLine:number,
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

export interface Erp_Tablesets_DmdCntDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  System assigned internal number to uniquely identify the demand contract record.  Is the link to the DemandContractHdr table.  */  
   DemandContractNum:number,
      /**  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandContractDtl record for the contract and the adding 1 to it.  */  
   DemandContractLine:number,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.
A default should be made when the DemandContractDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table.  */  
   PartNum:string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   XPartNum:string,
      /**  Determines whether or not this contract line is being run in a test mode. When contracts are first set up for EDI it is useful to send all documents in test mode so trading partners can verify the data before going into production mode.  */  
   TestRecord:boolean,
      /**  The total selling quantity expected to be ordered for this line over the life of the contract.  */  
   SellingTotalContractQty:number,
      /**  The total quantity expected to be ordered for this line over the life of the contract.  */  
   TotalContractQty:number,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   IUM:string,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the Customer.DiscountPercent.  */  
   DiscountPercent:number,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   UnitPrice:number,
      /**  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   PricePerCode:string,
      /**  Project ID of the Project table record for this DemandContractDtl record. Can be blank.  */  
   ProjectID:string,
      /**  This is the Price Group ID used to price the order line with.  */  
   PriceGroupCode:string,
      /**  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   SalesUM:string,
      /**  Comments about the demand detail line.  */  
   DetailComments:string,
      /**  Use standard Epicor Price matrix/logic  */  
   UsePriceList:boolean,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Total invoice amount of orders lines invoiced for this contract line in base currency. This field has a true sign. (credit memos are negative).  */  
   TotalInvoiceAmt:number,
      /**  Total  amount of orders for this contract line in base currency. This field has a true sign. (credit memos are negative).  */  
   TotalOrderAmt:number,
      /**  The total actual quantity ordered for this contract line. (credit memos may change it to negative).  */  
   TotalOrderedQty:number,
      /**  The total actual quantity shipped for this contract line. (credit memos may change it to negative).  */  
   TotalShippedQty:number,
      /**  The total actual quantity invoiced for this contract line. (credit memos may change it to negative).  */  
   TotalInvoicedQty:number,
      /**  Indicates if current open Order Releases that have not been shipped and do not have a job should be deleted when processing the demand.  Provides the default value for DemandDetail.  */  
   DeleteCurrentReleases:boolean,
      /**  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via Demand Contract entry if the CRM module is installed.  */  
   MktgCampaignID:string,
      /**   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via demand contract entry if the CRM module is installed.  */  
   MktgEvntSeq:number,
      /**  The mininum quantity that should be for each individual demand schedule record. If the schedule quantity is less than the minimum call off quantity, a warning will be issued but processing can continue.  */  
   MinCallOffQty:number,
      /**  Optional field that contains the  part revision.  */  
   RevisionNum:string,
      /**  Optional field that contains the customers revision.  */  
   XRevisionNum:string,
      /**  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  */  
   DemandPricing:string,
      /**   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   DocUnitPrice:number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   Rpt1UnitPrice:number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   Rpt2UnitPrice:number,
      /**  Same as Unit price except that this field contains the unit price in a report currency  */  
   Rpt3UnitPrice:number,
      /**  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  */  
   OTSmartString:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Total invoice amount of orders invoiced for this contract in document currency. This field has a true sign. (credit memos are negative).  */  
   DocTotalInvoiceAmt:number,
      /**  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   Rpt1TotalInvoiceAmt:number,
      /**  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   Rpt2TotalInvoiceAmt:number,
      /**  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   Rpt3TotalInvoiceAmt:number,
      /**  Total amount of orders for this contract in document currency. This field has a true sign. (credit memos are negative).  */  
   DocTotalOrderAmt:number,
      /**  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   Rpt1TotalOrderAmt:number,
      /**  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   Rpt2TotalOrderAmt:number,
      /**  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   Rpt3TotalOrderAmt:number,
      /**  Defines the tolerance for price difference validations.  */  
   PriceTolerance:number,
      /**  Defines the tolerance for price difference validations in document currency.  */  
   DocPriceTolerance:number,
      /**  Defines the tolerance for price difference validations in a report currency.  */  
   Rpt1PriceTolerance:number,
      /**  Defines the tolerance for price difference validations in a report currency.  */  
   Rpt2PriceTolerance:number,
      /**  Defines the tolerance for price difference validations in a report currency.  */  
   Rpt3PriceTolerance:number,
   CurrencyCode:string,
      /**  Indicates if this record has been selected to create a demand detail record.  Used for automatically creating DemandDetail records from contract lines.  */  
   SelectedForDemand:boolean,
      /**  Ordered Qty, Shipped Qty, Invoiced Qty, Minimum Call Off UOM  */  
   TotOrdShpInvCallOffQtyUOM:string,
   CurrencySwitch:boolean,
   BitFlag:number,
   DemandCntHdrDemandContract:string,
   MktgCampaignIDCampDescription:string,
   MktgEvntEvntDescription:string,
   PlantName:string,
   ProjectIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DmdCntHdrAttchRow{
   Company:string,
   DemandContractNum:number,
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

export interface Erp_Tablesets_DmdCntHdrListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  System assigned internal number to uniquely identify the demand contract record.  The number comes from Sequence DemandContractNum.  */  
   DemandContractNum:number,
      /**  Contains the Customer number that the demand contract is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  The unique identifier of the demand contract.  This must be unique for a customer.  */  
   DemandContract:string,
      /**  The start date of the demand contract.  */  
   StartDate:string,
      /**  The end date of the contract.  */  
   EndDate:string,
      /**  The number of days from today for which a scheduled quantity is considered firm.  */  
   FirmDays:number,
      /**  The trading partner name.  */  
   TradingPartnerName:string,
      /**  The setting for reconciling cumulative shipping quantities.  Values are:  PART - By Part  PO - By Part/PO  */  
   CUMMSetting:string,
      /**  An optional field that describes the FOB policy.  */  
   FOB:string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   ShipViaCode:string,
      /**   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of DemandContractHdr.CUSTNUM use the CUSTOMER.TERMS
field as the default.  */  
   TermsCode:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  */  
   LockRate:boolean,
      /**  Code used to relate a AllocPri record to the order.  Defaulted from Customer.AllocPriorityCode.  */  
   AllocPriorityCode:string,
      /**  Code used to relate a ReservePri record to the order.  Defaulted from Customer.ReservePriorityCode.  */  
   ReservePriorityCode:string,
      /**  Indicates if the order must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases with a ship date <= the given cutoff date alos have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "O" (Ship Order 100% complete)  */  
   ShipOrderComplete:boolean,
      /**  Comments about the demand contract.  */  
   ContractComments:string,
      /**  Mandatory entry and must be valid. Default as the system date.  */  
   ContractDate:string,
      /**  Project ID of the Project table record for this DemandContractHdr record. Can be blank.  */  
   ProjectID:string,
      /**  Indicates if this contract is in an "open" status.  When a contract is closed, all DemandHead records that are associated with the contract will also be set to closed.  */  
   OpenContract:boolean,
      /**  The user that entered the contract.  On new demand contracts use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   EntryPerson:string,
      /**  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  */  
   AutoOrderBasedDisc:boolean,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**  Total invoice amount of orders invoiced for this contract in base currency. This field has a true sign. (credit memos are negative).  */  
   TotalInvoiceAmt:number,
      /**  Total  amount of orders for this contract in base currency. This field has a true sign. (credit memos are negative).  */  
   TotalOrderAmt:number,
      /**  When matching, match demands to order releases by reference number.  */  
   MatchByRef:boolean,
      /**  When matching, match demands to order releases by ship by (reqdate) date.  */  
   MatchByReqDate:boolean,
      /**  When matching, match demands to order releases by quantity.  */  
   MatchByQty:boolean,
      /**  When matching, match demands to order releases by matching the first open demand and the first open release.  All subsequent open demands and releases not already matched will be matched.  Subsequent demands and releases are determined by querying the tables by reqdate.  */  
   MatchByOpen:boolean,
      /**  Indicates where reference matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByRef is false.  */  
   MatchSeqRef:number,
      /**  Indicates where date matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByReqDate is false.  */  
   MatchSeqReqDate:number,
      /**  Indicates where quantity matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByQty is false.  */  
   MatchSeqQty:number,
      /**  Indicates where open matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByOpen is false.  */  
   MatchSeqOpen:number,
      /**  Hold for Review  */  
   OrderHoldForReview:boolean,
      /**  Flag to decide if the non matched schedules needs to be closed.  */  
   DemandCloseNoMatch:boolean,
      /**  Flag that state if the work flow error will be checked in every line.  */  
   WFLockByLine:boolean,
      /**  rate group code  */  
   RateGrpCode:string,
      /**  When true this field will indicate that Demand Schedules and Releases will only be matched if they meet all priorities listed in the Matching Priority List.  */  
   PerfectMatch:boolean,
      /**  A list of priorities in which the matching will be executed, first items are of higher priority than items at the last of the list.  */  
   MatchPriorityList:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  A LIST-DELIM delimited list of part options  */  
   MatchOptionAvailList:string,
      /**  A LIST-DELIM delimited list of part options  */  
   MatchOptSelectedList:string,
      /**  Address Name  */  
   Name:string,
      /**  Customer Address displays on Demand Contract Summary and Header Detail Screen  */  
   ContractAddressList:string,
      /**  FAX Number  */  
   FAXNum:string,
      /**  Phone Number  */  
   PhoneNum:string,
      /**  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  */  
   AvailBTCustList:string,
   BillToCustomerName:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   BaseCurrCurrName:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   BaseCurrCurrSymbol:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   BaseCurrCurrencyID:string,
      /**  Description of the currency  */  
   BaseCurrCurrDesc:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   BaseCurrDocumentDesc:string,
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
   CustomerBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustomerCustID:string,
      /**  The full name of the customer.  */  
   CustomerName:string,
      /**  Full description of the FOB Code.  */  
   FOBDescription:string,
      /**  Full description of Project Management Code.  */  
   ProjectIDDescription:string,
      /**  Description of the reservation priority. Example "High".  */  
   ReservePriDescription:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   ShipViaCodeWebDesc:string,
      /**  Full description for the shipping company (carrier).  */  
   ShipViaCodeDescription:string,
      /**  Full description of the terms which prints on sales orders and invoices.  */  
   TermsCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DmdCntHdrListTableset{
   DmdCntHdrList:Erp_Tablesets_DmdCntHdrListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DmdCntHdrRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  System assigned internal number to uniquely identify the demand contract record.  The number comes from Sequence DemandContractNum.  */  
   DemandContractNum:number,
      /**  Contains the Customer number that the demand contract is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  The unique identifier of the demand contract.  This must be unique for a customer.  */  
   DemandContract:string,
      /**  The start date of the demand contract.  */  
   StartDate:string,
      /**  The end date of the contract.  */  
   EndDate:string,
      /**  The number of days from today for which a scheduled quantity is considered firm.  */  
   FirmDays:number,
      /**  The trading partner name.  */  
   TradingPartnerName:string,
      /**  The setting for reconciling cumulative shipping quantities.  Values are:  PART - By Part  PO - By Part/PO  */  
   CUMMSetting:string,
      /**  An optional field that describes the FOB policy.  */  
   FOB:string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   ShipViaCode:string,
      /**   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of DemandContractHdr.CUSTNUM use the CUSTOMER.TERMS
field as the default.  */  
   TermsCode:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  */  
   LockRate:boolean,
      /**  Code used to relate a AllocPri record to the order.  Defaulted from Customer.AllocPriorityCode.  */  
   AllocPriorityCode:string,
      /**  Code used to relate a ReservePri record to the order.  Defaulted from Customer.ReservePriorityCode.  */  
   ReservePriorityCode:string,
      /**  Indicates if the order must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases with a ship date <= the given cutoff date alos have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "O" (Ship Order 100% complete)  */  
   ShipOrderComplete:boolean,
      /**  Comments about the demand contract.  */  
   ContractComments:string,
      /**  Mandatory entry and must be valid. Default as the system date.  */  
   ContractDate:string,
      /**  Project ID of the Project table record for this DemandContractHdr record. Can be blank.  */  
   ProjectID:string,
      /**  Indicates if this contract is in an "open" status.  When a contract is closed, all DemandHead records that are associated with the contract will also be set to closed.  */  
   OpenContract:boolean,
      /**  The user that entered the contract.  On new demand contracts use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   EntryPerson:string,
      /**  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  */  
   AutoOrderBasedDisc:boolean,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**  Total invoice amount of orders invoiced for this contract in base currency. This field has a true sign. (credit memos are negative).  */  
   TotalInvoiceAmt:number,
      /**  Total  amount of orders for this contract in base currency. This field has a true sign. (credit memos are negative).  */  
   TotalOrderAmt:number,
      /**  When matching, match demands to order releases by reference number.  */  
   MatchByRef:boolean,
      /**  When matching, match demands to order releases by ship by (reqdate) date.  */  
   MatchByReqDate:boolean,
      /**  When matching, match demands to order releases by quantity.  */  
   MatchByQty:boolean,
      /**  When matching, match demands to order releases by matching the first open demand and the first open release.  All subsequent open demands and releases not already matched will be matched.  Subsequent demands and releases are determined by querying the tables by reqdate.  */  
   MatchByOpen:boolean,
      /**  Indicates where reference matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByRef is false.  */  
   MatchSeqRef:number,
      /**  Indicates where date matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByReqDate is false.  */  
   MatchSeqReqDate:number,
      /**  Indicates where quantity matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByQty is false.  */  
   MatchSeqQty:number,
      /**  Indicates where open matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByOpen is false.  */  
   MatchSeqOpen:number,
      /**  Hold for Review  */  
   OrderHoldForReview:boolean,
      /**  Flag to decide if the non matched schedules needs to be closed.  */  
   DemandCloseNoMatch:boolean,
      /**  Flag that state if the work flow error will be checked in every line.  */  
   WFLockByLine:boolean,
      /**  rate group code  */  
   RateGrpCode:string,
      /**  When true this field will indicate that Demand Schedules and Releases will only be matched if they meet all priorities listed in the Matching Priority List.  */  
   PerfectMatch:boolean,
      /**  A list of priorities in which the matching will be executed, first items are of higher priority than items at the last of the list.  */  
   MatchPriorityList:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  This option should be defaulted to false. If the user manually turns on this flag then the system will match the schedules as it is working today. If that flag is turned off then the system will match the schedules  only and only if all the criterias selected in the matching options matches between the schedules and the releases.  */  
   AllowNonPerfectMatch:boolean,
      /**  A LIST-DELIM delimited list of part options  */  
   MatchOptionAvailList:string,
      /**  A LIST-DELIM delimited list of part options  */  
   MatchOptSelectedList:string,
      /**  When TRUE, the Cancel Non Matched logic will skip any schedule whose NeedByDate is from Today until the resulting date of adding UntilDays to TODAY  */  
   ExcludeUntil:boolean,
      /**  When TRUE, the Cancel Non Matched logic will skip any schedule whose NeedByDate is FROM the resulting date of substracting BeforeDays from TODAY and until TODAY  */  
   ExcludeBefore:boolean,
      /**  Number of days that will be added to TODAY when ExcludeUntil is TRUE. The Cancel Non Match logic will then skip any schedule whose NeedByDate is between TODAY and the resulting date (TODAY + UntilDays).  */  
   UntilDays:number,
      /**  Number of days that will be substracting TODAY, the resulting date will tell the Cancel Non Match to skip any schedule with a NeedByDate within this date and the current date.  */  
   BeforeDays:number,
      /**  Total invoice amount of orders invoiced for this contract in document currency. This field has a true sign. (credit memos are negative).  */  
   DocTotalInvoiceAmt:number,
      /**  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   Rpt1TotalInvoiceAmt:number,
      /**  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   Rpt2TotalInvoiceAmt:number,
      /**  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   Rpt3TotalInvoiceAmt:number,
      /**  Total amount of orders for this contract in document currency. This field has a true sign. (credit memos are negative).  */  
   DocTotalOrderAmt:number,
      /**  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   Rpt1TotalOrderAmt:number,
      /**  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   Rpt2TotalOrderAmt:number,
      /**  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  */  
   Rpt3TotalOrderAmt:number,
      /**  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  */  
   AvailBTCustList:string,
   BillToCustomerName:string,
      /**  Customer Address displays on Demand Contract Summary and Header Detail Screen  */  
   ContractAddressList:string,
      /**  FAX Number  */  
   FAXNum:string,
      /**  Address Name  */  
   Name:string,
      /**  Phone Number  */  
   PhoneNum:string,
   BaseCurrencyCode:string,
   CurrencySwitch:boolean,
      /**  The formatted Contract Address  */  
   ContractAddressFormatted:string,
      /**  List of available match options  */  
   MatchOptionsList:string,
   BitFlag:number,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeDocumentDesc:string,
   CustomerCustID:string,
   CustomerBTName:string,
   CustomerName:string,
   FOBDescription:string,
   ProjectIDDescription:string,
   ReservePriDescription:string,
   ShipViaCodeDescription:string,
   ShipViaCodeWebDesc:string,
   TermsCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtDemandContractTableset{
   DmdCntHdr:Erp_Tablesets_DmdCntHdrRow[],
   DmdCntHdrAttch:Erp_Tablesets_DmdCntHdrAttchRow[],
   DmdCntDtl:Erp_Tablesets_DmdCntDtlRow[],
   DmdCntDtlAttch:Erp_Tablesets_DmdCntDtlAttchRow[],
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
      @param custNum
      @param demandContract
   */  
export interface GetByCustNumDemandContract_input{
      /**  Customer Number  */  
   custNum:number,
      /**  Demand Contract  */  
   demandContract:string,
}

export interface GetByCustNumDemandContract_output{
   returnObj:Erp_Tablesets_DemandContractTableset[],
}

   /** Required : 
      @param demandContract
      @param customerID
   */  
export interface GetByDemandContractCustID_input{
      /**  DemandContract  */  
   demandContract:string,
      /**  Customer ID  */  
   customerID:string,
}

export interface GetByDemandContractCustID_output{
   returnObj:Erp_Tablesets_DemandContractTableset[],
}

   /** Required : 
      @param demandContract
      @param tradingPartnerName
   */  
export interface GetByDmdCntTradingPartner_input{
      /**  DemandContract  */  
   demandContract:string,
      /**  Trading Parner Name  */  
   tradingPartnerName:string,
}

export interface GetByDmdCntTradingPartner_output{
   returnObj:Erp_Tablesets_DemandContractTableset[],
}

   /** Required : 
      @param demandContractNum
   */  
export interface GetByID_input{
   demandContractNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_DemandContractTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_DemandContractTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_DemandContractTableset[],
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
      @param contractID
   */  
export interface GetContractNumByID_input{
      /**  Demand Contract ID  */  
   contractID:string,
}

export interface GetContractNumByID_output{
parameters : {
      /**  output parameters  */  
   contractNum:number,
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
   returnObj:Erp_Tablesets_DmdCntHdrListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param demandContractNum
      @param demandContractLine
   */  
export interface GetNewDmdCntDtlAttch_input{
   ds:Erp_Tablesets_DemandContractTableset[],
   demandContractNum:number,
   demandContractLine:number,
}

export interface GetNewDmdCntDtlAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandContractTableset[],
}
}

   /** Required : 
      @param ds
      @param demandContractNum
   */  
export interface GetNewDmdCntDtl_input{
   ds:Erp_Tablesets_DemandContractTableset[],
   demandContractNum:number,
}

export interface GetNewDmdCntDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandContractTableset[],
}
}

   /** Required : 
      @param ds
      @param demandContractNum
   */  
export interface GetNewDmdCntHdrAttch_input{
   ds:Erp_Tablesets_DemandContractTableset[],
   demandContractNum:number,
}

export interface GetNewDmdCntHdrAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandContractTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewDmdCntHdr_input{
   ds:Erp_Tablesets_DemandContractTableset[],
}

export interface GetNewDmdCntHdr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandContractTableset[],
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
      @param whereClauseDmdCntHdr
      @param whereClauseDmdCntHdrAttch
      @param whereClauseDmdCntDtl
      @param whereClauseDmdCntDtlAttch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseDmdCntHdr:string,
   whereClauseDmdCntHdrAttch:string,
   whereClauseDmdCntDtl:string,
   whereClauseDmdCntDtlAttch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_DemandContractTableset[],
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
      @param inputDMCNum
      @param inputDMCLine
      @param inputDMCPlant
   */  
export interface RefreshPlant_input{
      /**  The Demand Contract Num  */  
   inputDMCNum:number,
      /**  The Demand Contract Line  */  
   inputDMCLine:number,
      /**  The Demand Plant  */  
   inputDMCPlant:string,
}

export interface RefreshPlant_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtDemandContractTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtDemandContractTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_DemandContractTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandContractTableset[],
}
}

