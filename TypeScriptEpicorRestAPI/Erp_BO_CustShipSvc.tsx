import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.CustShipSvc
// Description: Customer Shipment Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/$metadata", {
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
   Description: Get CustShips items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CustShips
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipHeadRow
   */  
export function get_CustShips(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CustShips
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustShips(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CustShip item
   Description: Calls GetByID to retrieve the CustShip item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustShip
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipHeadRow
   */  
export function get_CustShips_Company_PackNum(Company:string, PackNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CustShip for the service
   Description: Calls UpdateExt to update CustShip. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CustShip
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CustShips_Company_PackNum(Company:string, PackNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")", {
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
   Summary: Call UpdateExt to delete CustShip item
   Description: Call UpdateExt to delete CustShip item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CustShip
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CustShips_Company_PackNum(Company:string, PackNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")", {
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
   Description: Get CartonTrkDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CartonTrkDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CartonTrkDtlRow
   */  
export function get_CustShips_Company_PackNum_CartonTrkDtls(Company:string, PackNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CartonTrkDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/CartonTrkDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CartonTrkDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CartonTrkDtl item
   Description: Calls GetByID to retrieve the CartonTrkDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CartonTrkDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param ShipmentType Desc: ShipmentType   Required: True   Allow empty value : True
      @param CaseNum Desc: CaseNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CartonTrkDtlRow
   */  
export function get_CustShips_Company_PackNum_CartonTrkDtls_Company_ShipmentType_PackNum_CaseNum(Company:string, PackNum:string, ShipmentType:string, CaseNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CartonTrkDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/CartonTrkDtls(" + Company + "," + ShipmentType + "," + PackNum + "," + CaseNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CartonTrkDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ShipDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipDtlRow
   */  
export function get_CustShips_Company_PackNum_ShipDtls(Company:string, PackNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ShipDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipDtl item
   Description: Calls GetByID to retrieve the ShipDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipDtlRow
   */  
export function get_CustShips_Company_PackNum_ShipDtls_Company_PackNum_PackLine(Company:string, PackNum:string, PackLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ShipDtls(" + Company + "," + PackNum + "," + PackLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ShipHeadInsurances items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipHeadInsurances1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipHeadInsuranceRow
   */  
export function get_CustShips_Company_PackNum_ShipHeadInsurances(Company:string, PackNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadInsuranceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ShipHeadInsurances", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadInsuranceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipHeadInsurance item
   Description: Calls GetByID to retrieve the ShipHeadInsurance item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipHeadInsurance1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param InsuranceSeq Desc: InsuranceSeq   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipHeadInsuranceRow
   */  
export function get_CustShips_Company_PackNum_ShipHeadInsurances_Company_PackNum_InsuranceSeq(Company:string, PackNum:string, InsuranceSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipHeadInsuranceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ShipHeadInsurances(" + Company + "," + PackNum + "," + InsuranceSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipHeadInsuranceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ShipMiscs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipMiscs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipMiscRow
   */  
export function get_CustShips_Company_PackNum_ShipMiscs(Company:string, PackNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipMiscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ShipMiscs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipMiscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipMisc item
   Description: Calls GetByID to retrieve the ShipMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipMisc1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipMiscRow
   */  
export function get_CustShips_Company_PackNum_ShipMiscs_Company_PackNum_PackLine_SeqNum_SysRowID(Company:string, PackNum:string, PackLine:string, SeqNum:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipMiscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ShipMiscs(" + Company + "," + PackNum + "," + PackLine + "," + SeqNum + "," + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipMiscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ReplicatedPacks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ReplicatedPacks1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReplicatedPacksRow
   */  
export function get_CustShips_Company_PackNum_ReplicatedPacks(Company:string, PackNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReplicatedPacksRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ReplicatedPacks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReplicatedPacksRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ReplicatedPack item
   Description: Calls GetByID to retrieve the ReplicatedPack item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReplicatedPack1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ReplicatedPacksRow
   */  
export function get_CustShips_Company_PackNum_ReplicatedPacks_SysRowID(Company:string, PackNum:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ReplicatedPacksRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ReplicatedPacks(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ReplicatedPacksRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ShipHeadTrailers items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipHeadTrailers1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipHeadTrailerRow
   */  
export function get_CustShips_Company_PackNum_ShipHeadTrailers(Company:string, PackNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadTrailerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ShipHeadTrailers", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadTrailerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipHeadTrailer item
   Description: Calls GetByID to retrieve the ShipHeadTrailer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipHeadTrailer1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param LicensePlate Desc: LicensePlate   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipHeadTrailerRow
   */  
export function get_CustShips_Company_PackNum_ShipHeadTrailers_Company_PackNum_LicensePlate(Company:string, PackNum:string, LicensePlate:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipHeadTrailerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ShipHeadTrailers(" + Company + "," + PackNum + "," + LicensePlate + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipHeadTrailerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ShipUPS items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipUPS1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipUPSRow
   */  
export function get_CustShips_Company_PackNum_ShipUPS(Company:string, PackNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipUPSRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ShipUPS", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipUPSRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipUP item
   Description: Calls GetByID to retrieve the ShipUP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipUP1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipUPSRow
   */  
export function get_CustShips_Company_PackNum_ShipUPS_Company_PackNum_UPSQVSeq(Company:string, PackNum:string, UPSQVSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipUPSRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ShipUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipUPSRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ShipHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipHeadAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipHeadAttchRow
   */  
export function get_CustShips_Company_PackNum_ShipHeadAttches(Company:string, PackNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ShipHeadAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipHeadAttch item
   Description: Calls GetByID to retrieve the ShipHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipHeadAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipHeadAttchRow
   */  
export function get_CustShips_Company_PackNum_ShipHeadAttches_Company_PackNum_DrawingSeq(Company:string, PackNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CustShips(" + Company + "," + PackNum + ")/ShipHeadAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get CartonTrkDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CartonTrkDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CartonTrkDtlRow
   */  
export function get_CartonTrkDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CartonTrkDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CartonTrkDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CartonTrkDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CartonTrkDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CartonTrkDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CartonTrkDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CartonTrkDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CartonTrkDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CartonTrkDtl item
   Description: Calls GetByID to retrieve the CartonTrkDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CartonTrkDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ShipmentType Desc: ShipmentType   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param CaseNum Desc: CaseNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CartonTrkDtlRow
   */  
export function get_CartonTrkDtls_Company_ShipmentType_PackNum_CaseNum(Company:string, ShipmentType:string, PackNum:string, CaseNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CartonTrkDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CartonTrkDtls(" + Company + "," + ShipmentType + "," + PackNum + "," + CaseNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CartonTrkDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CartonTrkDtl for the service
   Description: Calls UpdateExt to update CartonTrkDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CartonTrkDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ShipmentType Desc: ShipmentType   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param CaseNum Desc: CaseNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CartonTrkDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CartonTrkDtls_Company_ShipmentType_PackNum_CaseNum(Company:string, ShipmentType:string, PackNum:string, CaseNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CartonTrkDtls(" + Company + "," + ShipmentType + "," + PackNum + "," + CaseNum + ")", {
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
   Summary: Call UpdateExt to delete CartonTrkDtl item
   Description: Call UpdateExt to delete CartonTrkDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CartonTrkDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ShipmentType Desc: ShipmentType   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param CaseNum Desc: CaseNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CartonTrkDtls_Company_ShipmentType_PackNum_CaseNum(Company:string, ShipmentType:string, PackNum:string, CaseNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CartonTrkDtls(" + Company + "," + ShipmentType + "," + PackNum + "," + CaseNum + ")", {
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
   Description: Get ShipDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipDtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipDtlRow
   */  
export function get_ShipDtls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ShipDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipDtl item
   Description: Calls GetByID to retrieve the ShipDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipDtlRow
   */  
export function get_ShipDtls_Company_PackNum_PackLine(Company:string, PackNum:string, PackLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls(" + Company + "," + PackNum + "," + PackLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ShipDtl for the service
   Description: Calls UpdateExt to update ShipDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ShipDtls_Company_PackNum_PackLine(Company:string, PackNum:string, PackLine:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls(" + Company + "," + PackNum + "," + PackLine + ")", {
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
   Summary: Call UpdateExt to delete ShipDtl item
   Description: Call UpdateExt to delete ShipDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ShipDtls_Company_PackNum_PackLine(Company:string, PackNum:string, PackLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls(" + Company + "," + PackNum + "," + PackLine + ")", {
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
   Description: Get ShipCOOs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipCOOs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipCOORow
   */  
export function get_ShipDtls_Company_PackNum_PackLine_ShipCOOs(Company:string, PackNum:string, PackLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipCOORow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls(" + Company + "," + PackNum + "," + PackLine + ")/ShipCOOs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipCOORow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipCOO item
   Description: Calls GetByID to retrieve the ShipCOO item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipCOO1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param OrigCountry Desc: OrigCountry   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipCOORow
   */  
export function get_ShipDtls_Company_PackNum_PackLine_ShipCOOs_Company_RelatedToFile_PackNum_PackLine_OrigCountry(Company:string, PackNum:string, PackLine:string, RelatedToFile:string, OrigCountry:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipCOORow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls(" + Company + "," + PackNum + "," + PackLine + ")/ShipCOOs(" + Company + "," + RelatedToFile + "," + PackNum + "," + PackLine + "," + OrigCountry + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipCOORow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ShipDtlPackagings items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipDtlPackagings1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipDtlPackagingRow
   */  
export function get_ShipDtls_Company_PackNum_PackLine_ShipDtlPackagings(Company:string, PackNum:string, PackLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlPackagingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls(" + Company + "," + PackNum + "," + PackLine + ")/ShipDtlPackagings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlPackagingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipDtlPackaging item
   Description: Calls GetByID to retrieve the ShipDtlPackaging item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipDtlPackaging1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipDtlPackagingRow
   */  
export function get_ShipDtls_Company_PackNum_PackLine_ShipDtlPackagings_Company_PackNum_PackLine(Company:string, PackNum:string, PackLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipDtlPackagingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls(" + Company + "," + PackNum + "," + PackLine + ")/ShipDtlPackagings(" + Company + "," + PackNum + "," + PackLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipDtlPackagingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ShipDtlTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipDtlTaxes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipDtlTaxRow
   */  
export function get_ShipDtls_Company_PackNum_PackLine_ShipDtlTaxes(Company:string, PackNum:string, PackLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls(" + Company + "," + PackNum + "," + PackLine + ")/ShipDtlTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipDtlTax item
   Description: Calls GetByID to retrieve the ShipDtlTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipDtlTax1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipDtlTaxRow
   */  
export function get_ShipDtls_Company_PackNum_PackLine_ShipDtlTaxes_Company_PackNum_PackLine_TaxCode_RateCode_ECAcquisitionSeq(Company:string, PackNum:string, PackLine:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipDtlTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls(" + Company + "," + PackNum + "," + PackLine + ")/ShipDtlTaxes(" + Company + "," + PackNum + "," + PackLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipDtlTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ShipDtlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipDtlAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipDtlAttchRow
   */  
export function get_ShipDtls_Company_PackNum_PackLine_ShipDtlAttches(Company:string, PackNum:string, PackLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls(" + Company + "," + PackNum + "," + PackLine + ")/ShipDtlAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipDtlAttch item
   Description: Calls GetByID to retrieve the ShipDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipDtlAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipDtlAttchRow
   */  
export function get_ShipDtls_Company_PackNum_PackLine_ShipDtlAttches_Company_PackNum_PackLine_DrawingSeq(Company:string, PackNum:string, PackLine:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtls(" + Company + "," + PackNum + "," + PackLine + ")/ShipDtlAttches(" + Company + "," + PackNum + "," + PackLine + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ShipCOOs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipCOOs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipCOORow
   */  
export function get_ShipCOOs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipCOORow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipCOOs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipCOORow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipCOOs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipCOORow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipCOORow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ShipCOOs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipCOOs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipCOO item
   Description: Calls GetByID to retrieve the ShipCOO item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipCOO
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param OrigCountry Desc: OrigCountry   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipCOORow
   */  
export function get_ShipCOOs_Company_RelatedToFile_PackNum_PackLine_OrigCountry(Company:string, RelatedToFile:string, PackNum:string, PackLine:string, OrigCountry:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipCOORow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipCOOs(" + Company + "," + RelatedToFile + "," + PackNum + "," + PackLine + "," + OrigCountry + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipCOORow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ShipCOO for the service
   Description: Calls UpdateExt to update ShipCOO. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipCOO
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param OrigCountry Desc: OrigCountry   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipCOORow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ShipCOOs_Company_RelatedToFile_PackNum_PackLine_OrigCountry(Company:string, RelatedToFile:string, PackNum:string, PackLine:string, OrigCountry:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipCOOs(" + Company + "," + RelatedToFile + "," + PackNum + "," + PackLine + "," + OrigCountry + ")", {
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
   Summary: Call UpdateExt to delete ShipCOO item
   Description: Call UpdateExt to delete ShipCOO item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipCOO
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param OrigCountry Desc: OrigCountry   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ShipCOOs_Company_RelatedToFile_PackNum_PackLine_OrigCountry(Company:string, RelatedToFile:string, PackNum:string, PackLine:string, OrigCountry:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipCOOs(" + Company + "," + RelatedToFile + "," + PackNum + "," + PackLine + "," + OrigCountry + ")", {
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
   Description: Get ShipDtlPackagings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipDtlPackagings
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipDtlPackagingRow
   */  
export function get_ShipDtlPackagings(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlPackagingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlPackagings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlPackagingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipDtlPackagings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipDtlPackagingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipDtlPackagingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ShipDtlPackagings(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlPackagings", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipDtlPackaging item
   Description: Calls GetByID to retrieve the ShipDtlPackaging item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipDtlPackaging
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipDtlPackagingRow
   */  
export function get_ShipDtlPackagings_Company_PackNum_PackLine(Company:string, PackNum:string, PackLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipDtlPackagingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlPackagings(" + Company + "," + PackNum + "," + PackLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipDtlPackagingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ShipDtlPackaging for the service
   Description: Calls UpdateExt to update ShipDtlPackaging. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipDtlPackaging
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipDtlPackagingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ShipDtlPackagings_Company_PackNum_PackLine(Company:string, PackNum:string, PackLine:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlPackagings(" + Company + "," + PackNum + "," + PackLine + ")", {
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
   Summary: Call UpdateExt to delete ShipDtlPackaging item
   Description: Call UpdateExt to delete ShipDtlPackaging item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipDtlPackaging
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ShipDtlPackagings_Company_PackNum_PackLine(Company:string, PackNum:string, PackLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlPackagings(" + Company + "," + PackNum + "," + PackLine + ")", {
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
   Description: Get ShipDtlTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipDtlTaxes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipDtlTaxRow
   */  
export function get_ShipDtlTaxes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipDtlTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipDtlTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipDtlTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ShipDtlTaxes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlTaxes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipDtlTax item
   Description: Calls GetByID to retrieve the ShipDtlTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipDtlTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipDtlTaxRow
   */  
export function get_ShipDtlTaxes_Company_PackNum_PackLine_TaxCode_RateCode_ECAcquisitionSeq(Company:string, PackNum:string, PackLine:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipDtlTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlTaxes(" + Company + "," + PackNum + "," + PackLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipDtlTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ShipDtlTax for the service
   Description: Calls UpdateExt to update ShipDtlTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipDtlTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipDtlTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ShipDtlTaxes_Company_PackNum_PackLine_TaxCode_RateCode_ECAcquisitionSeq(Company:string, PackNum:string, PackLine:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlTaxes(" + Company + "," + PackNum + "," + PackLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Summary: Call UpdateExt to delete ShipDtlTax item
   Description: Call UpdateExt to delete ShipDtlTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipDtlTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ShipDtlTaxes_Company_PackNum_PackLine_TaxCode_RateCode_ECAcquisitionSeq(Company:string, PackNum:string, PackLine:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlTaxes(" + Company + "," + PackNum + "," + PackLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Description: Get ShipDtlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipDtlAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipDtlAttchRow
   */  
export function get_ShipDtlAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipDtlAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipDtlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipDtlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ShipDtlAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipDtlAttch item
   Description: Calls GetByID to retrieve the ShipDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipDtlAttchRow
   */  
export function get_ShipDtlAttches_Company_PackNum_PackLine_DrawingSeq(Company:string, PackNum:string, PackLine:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlAttches(" + Company + "," + PackNum + "," + PackLine + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ShipDtlAttch for the service
   Description: Calls UpdateExt to update ShipDtlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipDtlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ShipDtlAttches_Company_PackNum_PackLine_DrawingSeq(Company:string, PackNum:string, PackLine:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlAttches(" + Company + "," + PackNum + "," + PackLine + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete ShipDtlAttch item
   Description: Call UpdateExt to delete ShipDtlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ShipDtlAttches_Company_PackNum_PackLine_DrawingSeq(Company:string, PackNum:string, PackLine:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipDtlAttches(" + Company + "," + PackNum + "," + PackLine + "," + DrawingSeq + ")", {
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
   Description: Get ShipHeadInsurances items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipHeadInsurances
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipHeadInsuranceRow
   */  
export function get_ShipHeadInsurances(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadInsuranceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadInsurances", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadInsuranceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipHeadInsurances
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipHeadInsuranceRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipHeadInsuranceRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ShipHeadInsurances(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadInsurances", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipHeadInsurance item
   Description: Calls GetByID to retrieve the ShipHeadInsurance item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipHeadInsurance
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param InsuranceSeq Desc: InsuranceSeq   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipHeadInsuranceRow
   */  
export function get_ShipHeadInsurances_Company_PackNum_InsuranceSeq(Company:string, PackNum:string, InsuranceSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipHeadInsuranceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadInsurances(" + Company + "," + PackNum + "," + InsuranceSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipHeadInsuranceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ShipHeadInsurance for the service
   Description: Calls UpdateExt to update ShipHeadInsurance. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipHeadInsurance
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param InsuranceSeq Desc: InsuranceSeq   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipHeadInsuranceRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ShipHeadInsurances_Company_PackNum_InsuranceSeq(Company:string, PackNum:string, InsuranceSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadInsurances(" + Company + "," + PackNum + "," + InsuranceSeq + ")", {
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
   Summary: Call UpdateExt to delete ShipHeadInsurance item
   Description: Call UpdateExt to delete ShipHeadInsurance item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipHeadInsurance
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param InsuranceSeq Desc: InsuranceSeq   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ShipHeadInsurances_Company_PackNum_InsuranceSeq(Company:string, PackNum:string, InsuranceSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadInsurances(" + Company + "," + PackNum + "," + InsuranceSeq + ")", {
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
   Description: Get ShipMiscs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipMiscs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipMiscRow
   */  
export function get_ShipMiscs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipMiscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipMiscs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipMiscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipMiscs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipMiscRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipMiscRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ShipMiscs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipMiscs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipMisc item
   Description: Calls GetByID to retrieve the ShipMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipMisc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipMiscRow
   */  
export function get_ShipMiscs_Company_PackNum_PackLine_SeqNum_SysRowID(Company:string, PackNum:string, PackLine:string, SeqNum:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipMiscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipMiscs(" + Company + "," + PackNum + "," + PackLine + "," + SeqNum + "," + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipMiscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ShipMisc for the service
   Description: Calls UpdateExt to update ShipMisc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipMisc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipMiscRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ShipMiscs_Company_PackNum_PackLine_SeqNum_SysRowID(Company:string, PackNum:string, PackLine:string, SeqNum:string, SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipMiscs(" + Company + "," + PackNum + "," + PackLine + "," + SeqNum + "," + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete ShipMisc item
   Description: Call UpdateExt to delete ShipMisc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipMisc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ShipMiscs_Company_PackNum_PackLine_SeqNum_SysRowID(Company:string, PackNum:string, PackLine:string, SeqNum:string, SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipMiscs(" + Company + "," + PackNum + "," + PackLine + "," + SeqNum + "," + SysRowID + ")", {
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
   Description: Get ReplicatedPacks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ReplicatedPacks
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReplicatedPacksRow
   */  
export function get_ReplicatedPacks(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReplicatedPacksRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ReplicatedPacks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReplicatedPacksRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ReplicatedPacks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ReplicatedPacksRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ReplicatedPacksRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReplicatedPacks(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ReplicatedPacks", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ReplicatedPack item
   Description: Calls GetByID to retrieve the ReplicatedPack item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReplicatedPack
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ReplicatedPacksRow
   */  
export function get_ReplicatedPacks_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ReplicatedPacksRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ReplicatedPacks(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ReplicatedPacksRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ReplicatedPack for the service
   Description: Calls UpdateExt to update ReplicatedPack. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ReplicatedPack
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ReplicatedPacksRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ReplicatedPacks_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ReplicatedPacks(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete ReplicatedPack item
   Description: Call UpdateExt to delete ReplicatedPack item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ReplicatedPack
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ReplicatedPacks_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ReplicatedPacks(" + SysRowID + ")", {
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
   Description: Get ShipHeadTrailers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipHeadTrailers
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipHeadTrailerRow
   */  
export function get_ShipHeadTrailers(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadTrailerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadTrailers", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadTrailerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipHeadTrailers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipHeadTrailerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipHeadTrailerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ShipHeadTrailers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadTrailers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipHeadTrailer item
   Description: Calls GetByID to retrieve the ShipHeadTrailer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipHeadTrailer
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param LicensePlate Desc: LicensePlate   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipHeadTrailerRow
   */  
export function get_ShipHeadTrailers_Company_PackNum_LicensePlate(Company:string, PackNum:string, LicensePlate:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipHeadTrailerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadTrailers(" + Company + "," + PackNum + "," + LicensePlate + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipHeadTrailerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ShipHeadTrailer for the service
   Description: Calls UpdateExt to update ShipHeadTrailer. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipHeadTrailer
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param LicensePlate Desc: LicensePlate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipHeadTrailerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ShipHeadTrailers_Company_PackNum_LicensePlate(Company:string, PackNum:string, LicensePlate:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadTrailers(" + Company + "," + PackNum + "," + LicensePlate + ")", {
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
   Summary: Call UpdateExt to delete ShipHeadTrailer item
   Description: Call UpdateExt to delete ShipHeadTrailer item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipHeadTrailer
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param LicensePlate Desc: LicensePlate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ShipHeadTrailers_Company_PackNum_LicensePlate(Company:string, PackNum:string, LicensePlate:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadTrailers(" + Company + "," + PackNum + "," + LicensePlate + ")", {
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
   Description: Get ShipUPS items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipUPS
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipUPSRow
   */  
export function get_ShipUPS(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipUPSRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipUPS", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipUPSRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipUPS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipUPSRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipUPSRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ShipUPS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipUPS", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipUP item
   Description: Calls GetByID to retrieve the ShipUP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipUP
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipUPSRow
   */  
export function get_ShipUPS_Company_PackNum_UPSQVSeq(Company:string, PackNum:string, UPSQVSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipUPSRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipUPSRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ShipUP for the service
   Description: Calls UpdateExt to update ShipUP. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipUP
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipUPSRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ShipUPS_Company_PackNum_UPSQVSeq(Company:string, PackNum:string, UPSQVSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")", {
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
   Summary: Call UpdateExt to delete ShipUP item
   Description: Call UpdateExt to delete ShipUP item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipUP
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ShipUPS_Company_PackNum_UPSQVSeq(Company:string, PackNum:string, UPSQVSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")", {
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
   Description: Get ShipHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipHeadAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipHeadAttchRow
   */  
export function get_ShipHeadAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipHeadAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ShipHeadAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipHeadAttch item
   Description: Calls GetByID to retrieve the ShipHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipHeadAttchRow
   */  
export function get_ShipHeadAttches_Company_PackNum_DrawingSeq(Company:string, PackNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ShipHeadAttch for the service
   Description: Calls UpdateExt to update ShipHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ShipHeadAttches_Company_PackNum_DrawingSeq(Company:string, PackNum:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete ShipHeadAttch item
   Description: Call UpdateExt to delete ShipHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ShipHeadAttches_Company_PackNum_DrawingSeq(Company:string, PackNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipHeadAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")", {
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
   Description: Get LegalNumberGenerates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumberGenerates
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumberGenerateRow
   */  
export function get_LegalNumberGenerates(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumberGenerateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/LegalNumberGenerates", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumberGenerateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumberGenerates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumberGenerateRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumberGenerateRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LegalNumberGenerates(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/LegalNumberGenerates", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LegalNumberGenerate item
   Description: Calls GetByID to retrieve the LegalNumberGenerate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumberGenerate
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumberGenerateRow
   */  
export function get_LegalNumberGenerates_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LegalNumberGenerateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/LegalNumberGenerates(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LegalNumberGenerateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LegalNumberGenerate for the service
   Description: Calls UpdateExt to update LegalNumberGenerate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumberGenerate
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumberGenerateRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LegalNumberGenerates_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/LegalNumberGenerates(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete LegalNumberGenerate item
   Description: Call UpdateExt to delete LegalNumberGenerate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumberGenerate
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LegalNumberGenerates_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/LegalNumberGenerates(" + SysRowID + ")", {
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
   Description: Get LegalNumGenOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumGenOpts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumGenOptsRow
   */  
export function get_LegalNumGenOpts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/LegalNumGenOpts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LegalNumGenOpts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/LegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LegalNumGenOpt item
   Description: Calls GetByID to retrieve the LegalNumGenOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumGenOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   */  
export function get_LegalNumGenOpts_Company_LegalNumberID(Company:string, LegalNumberID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LegalNumGenOptsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LegalNumGenOptsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LegalNumGenOpt for the service
   Description: Calls UpdateExt to update LegalNumGenOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumGenOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LegalNumGenOpts_Company_LegalNumberID(Company:string, LegalNumberID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
   Summary: Call UpdateExt to delete LegalNumGenOpt item
   Description: Call UpdateExt to delete LegalNumGenOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumGenOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LegalNumGenOpts_Company_LegalNumberID(Company:string, LegalNumberID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
   Description: Get SalesKitCompIssues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SalesKitCompIssues
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesKitCompIssueRow
   */  
export function get_SalesKitCompIssues(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesKitCompIssueRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SalesKitCompIssues", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesKitCompIssueRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SalesKitCompIssues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SalesKitCompIssueRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SalesKitCompIssueRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SalesKitCompIssues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SalesKitCompIssues", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the SalesKitCompIssue item
   Description: Calls GetByID to retrieve the SalesKitCompIssue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SalesKitCompIssue
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SalesKitCompIssueRow
   */  
export function get_SalesKitCompIssues_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SalesKitCompIssueRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SalesKitCompIssues(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SalesKitCompIssueRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SalesKitCompIssue for the service
   Description: Calls UpdateExt to update SalesKitCompIssue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SalesKitCompIssue
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SalesKitCompIssueRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SalesKitCompIssues_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SalesKitCompIssues(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete SalesKitCompIssue item
   Description: Call UpdateExt to delete SalesKitCompIssue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SalesKitCompIssue
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SalesKitCompIssues_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SalesKitCompIssues(" + SysRowID + ")", {
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
   Description: Get SelectedIDNumbers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SelectedIDNumbers
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SelectedIDNumbersRow
   */  
export function get_SelectedIDNumbers(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedIDNumbersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SelectedIDNumbers", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedIDNumbersRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SelectedIDNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SelectedIDNumbersRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SelectedIDNumbersRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectedIDNumbers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SelectedIDNumbers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the SelectedIDNumber item
   Description: Calls GetByID to retrieve the SelectedIDNumber item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SelectedIDNumber
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SelectedIDNumbersRow
   */  
export function get_SelectedIDNumbers_Company_PackNum_PackLine_SeqNum(Company:string, PackNum:string, PackLine:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SelectedIDNumbersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SelectedIDNumbers(" + Company + "," + PackNum + "," + PackLine + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SelectedIDNumbersRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SelectedIDNumber for the service
   Description: Calls UpdateExt to update SelectedIDNumber. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SelectedIDNumber
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SelectedIDNumbersRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SelectedIDNumbers_Company_PackNum_PackLine_SeqNum(Company:string, PackNum:string, PackLine:string, SeqNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SelectedIDNumbers(" + Company + "," + PackNum + "," + PackLine + "," + SeqNum + ")", {
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
   Summary: Call UpdateExt to delete SelectedIDNumber item
   Description: Call UpdateExt to delete SelectedIDNumber item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SelectedIDNumber
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SelectedIDNumbers_Company_PackNum_PackLine_SeqNum(Company:string, PackNum:string, PackLine:string, SeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SelectedIDNumbers(" + Company + "," + PackNum + "," + PackLine + "," + SeqNum + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SelectedSerialNumbers", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SelectedSerialNumbers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
   Description: Get ShipTaxSums items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipTaxSums
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipTaxSumRow
   */  
export function get_ShipTaxSums(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipTaxSumRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipTaxSums", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipTaxSumRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipTaxSums
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipTaxSumRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipTaxSumRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ShipTaxSums(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipTaxSums", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipTaxSum item
   Description: Calls GetByID to retrieve the ShipTaxSum item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipTaxSum
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLIne Desc: PackLIne   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipTaxSumRow
   */  
export function get_ShipTaxSums_Company_PackNum_PackLIne_TaxCode_RateCode(Company:string, PackNum:string, PackLIne:string, TaxCode:string, RateCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipTaxSumRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipTaxSums(" + Company + "," + PackNum + "," + PackLIne + "," + TaxCode + "," + RateCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipTaxSumRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ShipTaxSum for the service
   Description: Calls UpdateExt to update ShipTaxSum. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipTaxSum
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLIne Desc: PackLIne   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipTaxSumRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ShipTaxSums_Company_PackNum_PackLIne_TaxCode_RateCode(Company:string, PackNum:string, PackLIne:string, TaxCode:string, RateCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipTaxSums(" + Company + "," + PackNum + "," + PackLIne + "," + TaxCode + "," + RateCode + ")", {
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
   Summary: Call UpdateExt to delete ShipTaxSum item
   Description: Call UpdateExt to delete ShipTaxSum item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipTaxSum
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLIne Desc: PackLIne   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ShipTaxSums_Company_PackNum_PackLIne_TaxCode_RateCode(Company:string, PackNum:string, PackLIne:string, TaxCode:string, RateCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ShipTaxSums(" + Company + "," + PackNum + "," + PackLIne + "," + TaxCode + "," + RateCode + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SNFormats", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SNFormats", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadListRow)
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
export function get_GetRows(whereClauseShipHead:string, whereClauseShipHeadAttch:string, whereClauseCartonTrkDtl:string, whereClauseShipDtl:string, whereClauseShipDtlAttch:string, whereClauseShipCOO:string, whereClauseShipDtlPackaging:string, whereClauseShipDtlTax:string, whereClauseShipHeadInsurance:string, whereClauseShipMisc:string, whereClauseReplicatedPacks:string, whereClauseShipHeadTrailer:string, whereClauseShipUPS:string, whereClauseLegalNumberGenerate:string, whereClauseLegalNumGenOpts:string, whereClauseSalesKitCompIssue:string, whereClauseSelectedIDNumbers:string, whereClauseSelectedSerialNumbers:string, whereClauseShipTaxSum:string, whereClauseSNFormat:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseShipHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseShipHead=" + whereClauseShipHead
   }
   if(typeof whereClauseShipHeadAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseShipHeadAttch=" + whereClauseShipHeadAttch
   }
   if(typeof whereClauseCartonTrkDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCartonTrkDtl=" + whereClauseCartonTrkDtl
   }
   if(typeof whereClauseShipDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseShipDtl=" + whereClauseShipDtl
   }
   if(typeof whereClauseShipDtlAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseShipDtlAttch=" + whereClauseShipDtlAttch
   }
   if(typeof whereClauseShipCOO!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseShipCOO=" + whereClauseShipCOO
   }
   if(typeof whereClauseShipDtlPackaging!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseShipDtlPackaging=" + whereClauseShipDtlPackaging
   }
   if(typeof whereClauseShipDtlTax!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseShipDtlTax=" + whereClauseShipDtlTax
   }
   if(typeof whereClauseShipHeadInsurance!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseShipHeadInsurance=" + whereClauseShipHeadInsurance
   }
   if(typeof whereClauseShipMisc!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseShipMisc=" + whereClauseShipMisc
   }
   if(typeof whereClauseReplicatedPacks!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseReplicatedPacks=" + whereClauseReplicatedPacks
   }
   if(typeof whereClauseShipHeadTrailer!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseShipHeadTrailer=" + whereClauseShipHeadTrailer
   }
   if(typeof whereClauseShipUPS!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseShipUPS=" + whereClauseShipUPS
   }
   if(typeof whereClauseLegalNumberGenerate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLegalNumberGenerate=" + whereClauseLegalNumberGenerate
   }
   if(typeof whereClauseLegalNumGenOpts!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLegalNumGenOpts=" + whereClauseLegalNumGenOpts
   }
   if(typeof whereClauseSalesKitCompIssue!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSalesKitCompIssue=" + whereClauseSalesKitCompIssue
   }
   if(typeof whereClauseSelectedIDNumbers!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSelectedIDNumbers=" + whereClauseSelectedIDNumbers
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
   if(typeof whereClauseShipTaxSum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseShipTaxSum=" + whereClauseShipTaxSum
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetRows" + params, {
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
export function get_GetByID(packNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof packNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "packNum=" + packNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetList" + params, {
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
   Summary: Invoke method CheckAttributeSetsOnShipDtlLines
   Description: Purpose:     validate shipDtl lines for valid attribute sets
Notes:
<param name="iPackNum">current packNum</param><param name="markAsShipped">mark as shipped true or false</param><param name="cErrorMsg">any errors returned to user</param>
   OperationID: CheckAttributeSetsOnShipDtlLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckAttributeSetsOnShipDtlLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAttributeSetsOnShipDtlLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckAttributeSetsOnShipDtlLines(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CheckAttributeSetsOnShipDtlLines", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method StageWarning
   Description: Purpose:
Parameters:  none
Notes:
<param name="iPackNum">Serial number to validate.</param><param name="ipShipmentType">shipment type</param><param name="iWarning">Serial Number Voided flag</param>
   OperationID: StageWarning
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StageWarning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StageWarning_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_StageWarning(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/StageWarning", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UndoShipAll
   Description: This method re-sets all the temp-table records shipped (Undo Ship all button selected)
   OperationID: UndoShipAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UndoShipAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UndoShipAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UndoShipAll(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/UndoShipAll", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateManifestChargeAmts
   Description: Purpose:  Calculate the CODAmount and DeclaredAmt
<param name="ipAmountType">COD or DeclaredAmt</param><param name="ipAction">Yes = recalculate No = reset to zero</param><param name="ds">Customer Shipment data set </param>
Notes:  Update the COD Amount and/or Declared Insurance amounts for manifesting purposes.
   OperationID: UpdateManifestChargeAmts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateManifestChargeAmts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateManifestChargeAmts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateManifestChargeAmts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/UpdateManifestChargeAmts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateMaster
   Description: <param name="ds"></param>
<param name="doValidateCreditHold">If true run validate credit hold logic</param>
<param name="doCheckShipDtl">If true run checkShipDtl logic</param>
<param name="doLotValidation">If true run lot validation logic</param>
<param name="doCheckOrderComplete">If true run Check Order Complete logic</param>
<param name="doPostUpdate">If true perform post update logic</param>
<param name="doCheckCompliance">If true perform check compliance logic</param>
<param name="ipShippedFlagChanged">If true then refresh data for ReadyToInvoice changed</param>
<param name="ipPackNum">PackNum being updated</param>
<param name="ipBTCustNum">Bill to customer number for credit hold validation</param>
<param name="opReleaseMessage">If the Order release is closed, this asks if the user wants to continue</param>
<param name="opCompleteMessage">If the order complete status has changed, this would alert the user to any problems (yes/no)</param>
<param name="opShippingMessage">Alerts to any potential shipping error </param>
<param name="opLotMessage">If the lot doesn't exist, ask the user if they'd like to create it </param>
<param name="opInventoryMessage">If the inventory will go negative, ask user if they want to continue </param>
<param name="opLockQtyMessage">If the OrderDtl.LockQty=true and release 1 is being set to ship complete, ask user if they want to continue </param>
<param name="opAllocationMessage">If this transaction overrides a allocation, ask user if they want to continue </param>
<param name="opPartListNeedsAttr">List of parts that require lot attributes entered</param>
<param name="opLotListNeedsAttr">List of lots related to opPartListNeedsAttr that require lot attributes entered</param>
<param name="shipCreditMsg">possible output message from validateCreditHoldCore</param>
<param name="cError">Will be true if a hard error is encountered in validateCreditHoldCore</param>
<param name="compError">Will be true if a hard error is encountered in checkOrderCompleteCore</param>
<param name="msg">possible output message from checkOrderCompleteCore</param>
<param name="opPostUpdMessage">possible output message from postUpdateCore or checkOrderCore</param>
<param name="updateComplete">Indicates that the Update process did run</param>
<param name="checkComplianceError">Indicates whether the check compliance logic encountered non-compliance lines</param>
<param name="changeStatusError">Indicates whether the change status logic encountered errors</param>
<param name="checkShipDtlAgain">Whether to check ShipDtl records for errors</param>
   OperationID: UpdateMaster
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateMaster_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateMaster_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateMaster(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/UpdateMaster", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdatePackCODWithCarton
   Description: Purpose: Update pack COD amounts
<param name="ipPackNum">Pack Number to process</param><param name="ipCaseNum">Case Number to set value to zero</param><param name="ipOldCOD">Previous COD</param><param name="ipCOD">Current Case COD</param><param name="ipFlag">Current COD flag value</param><param name="ds">Customer Shipment data set</param>
Notes:
   OperationID: UpdatePackCODWithCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePackCODWithCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePackCODWithCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdatePackCODWithCarton(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/UpdatePackCODWithCarton", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdatePackDeclaredWithCarton
   Description: Purpose:  Update Pack Delcared Value Amounts
<param name="ipPackNum">Pack Number to process</param><param name="ipCaseNum">Case Number to set value to zero </param><param name="ipOldDeclared">Previous COD</param><param name="ipDeclared">Current Case COD</param><param name="ipDeclaredFlag">current setting of declared insurance</param><param name="ds">Customer Shipment data set</param>
Notes:
   OperationID: UpdatePackDeclaredWithCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePackDeclaredWithCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePackDeclaredWithCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdatePackDeclaredWithCarton(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/UpdatePackDeclaredWithCarton", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdatePackWeightWithCarton
   Description: Purpose:Update the Pack Weight with the carton weight
<param name="ipPackNum">Pack Number to process</param><param name="ipOldWeight">Previous weight</param><param name="ipWeight">Current Case weight</param><param name="ds">Customer Shipment data set</param>
Notes:
   OperationID: UpdatePackWeightWithCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePackWeightWithCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePackWeightWithCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdatePackWeightWithCarton(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/UpdatePackWeightWithCarton", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateBinCode
   Description: Purpose: Validate the bin.
<param name="ipWhse">Warehouse code used to edit bin</param><param name="ipBinNum">Bin Code to validate</param>
Notes:
   OperationID: ValidateBinCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateBinCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBinCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateBinCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ValidateBinCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePackNum
   Description: Purpose:  Validate PCID VOid Pack List
Parameters:  none
Notes:
<param name="ipPackNum">Packing Slip Number </param><param name="_success">Error flag.</param>
   OperationID: ValidatePackNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePackNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePackNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePackNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ValidatePackNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateCreditHold
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipValPackNum">Packing Slip Number </param><param name="ipValBTCustNum">Bill To Customer Number.</param><param name="opCreditMessage">Credit Message.</param><param name="opcError">Error flag.</param>
   OperationID: ValidateCreditHold
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCreditHold_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCreditHold_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateCreditHold(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ValidateCreditHold", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateCreditHoldPO
   Description: Purpose:
Notes:
<param name="ipOrderNum">Order Number </param><param name="ipPackNum">Pack Number</param><param name="opCreditMessage">Credit Message.</param><param name="opAgingMessage">aging message</param>
   OperationID: ValidateCreditHoldPO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCreditHoldPO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCreditHoldPO_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateCreditHoldPO(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ValidateCreditHoldPO", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateCreditHoldSSC
   Description: Purpose:     THIS IS CALLED FROM STAGE SHIP CONFIRM UI
Parameters:  none
Notes:
<param name="ipPackNum">Packing Slip Number </param><param name="ipShipmentType">Shipment Type </param><param name="opCreditMessage">Credit Message.</param><param name="opcError">Error flag.</param>
   OperationID: ValidateCreditHoldSSC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCreditHoldSSC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCreditHoldSSC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateCreditHoldSSC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ValidateCreditHoldSSC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateKitPart
   Description: This method will validate the kit part when changing lines in the Sales Kit
Component Issue grid
   OperationID: ValidateKitPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateKitPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateKitPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateKitPart(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ValidateKitPart", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateLocationIDNumbers
   Description: Purpose:  Validate if the Location IDNum already exist for the Part.
Parameters:  none
Notes:
<param name="IDNumList">ID Number List </param><param name="ipPartNum">Part Number </param><param name="ipIDNumProposed">ID Number Proposed </param><param name="ipPackNum">PackNum</param><param name="ipPackLine">PackLine</param>
   OperationID: ValidateLocationIDNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateLocationIDNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateLocationIDNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateLocationIDNumbers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ValidateLocationIDNumbers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipSerialNum">Serial number to validate.</param><param name="ipPartNum">Part number</param><param name="ipAttributeSetID">Attribute Set</param><param name="ipJobNum">Job number</param><param name="ipOurJobshipQty">Job Ship Quantity</param><param name="ipOurInvShipQty">Inventory Ship Quantity</param><param name="ipOrderNum">Order number</param><param name="ipOrderLine">Order Line number</param><param name="ipOrderRelNum">OrderRelease number</param><param name="ipShipFromWIP">Flag to indicate shipping from WIP</param><param name="ipWarehouseCode">Ship from warehouse</param><param name="ipBinNum">Ship from bin</param><param name="isVoided">Serial Number Voided flag</param>
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ValidateSN", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VoidLegalNumber
   Description: Voids the legal number.
   OperationID: VoidLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VoidLegalNumber(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/VoidLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAvailTranDocTypes
   Description: GetAvailTranDocTypes
   OperationID: GetAvailTranDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailTranDocTypes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetAvailTranDocTypes", {
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
   Summary: Invoke method GetCodeDescList
   Description: GetCodeDescList
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method NegativeInventoryTest
   Description: NegativeInventoryTest
   OperationID: NegativeInventoryTest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/NegativeInventoryTest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NegativeInventoryTest_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NegativeInventoryTest(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/NegativeInventoryTest", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPCBinOutLocation
   Description: Validate the shipment from location does not belong to a Planning Contract
   OperationID: CheckPCBinOutLocation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPCBinOutLocation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPCBinOutLocation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPCBinOutLocation(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CheckPCBinOutLocation", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPackageCodeAllocNegQty
   OperationID: CheckPackageCodeAllocNegQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPackageCodeAllocNegQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackageCodeAllocNegQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPackageCodeAllocNegQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CheckPackageCodeAllocNegQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPkgCodeQtyList
   OperationID: GetPkgCodeQtyList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPkgCodeQtyList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPkgCodeQtyList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPkgCodeQtyList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetPkgCodeQtyList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessNegQtyTest
   Description: This was created for Kinetic UI
   OperationID: ProcessNegQtyTest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessNegQtyTest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessNegQtyTest_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessNegQtyTest(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ProcessNegQtyTest", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateDigitalSignature
   Description: Generate Digital Signature
   OperationID: GenerateDigitalSignature
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateDigitalSignature_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateDigitalSignature_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateDigitalSignature(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GenerateDigitalSignature", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePCIDPackVerify
   Description: Overload to ChangePCID, will Check for every line of the Pack if it requires if it is compliant, or return a flag if the PCID was already scanned.
And Calculates the number of PCIDs with qty in a pack and/or the item part number for a given PCID if the ChangePCID logic is successful
   OperationID: ChangePCIDPackVerify
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCIDPackVerify_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCIDPackVerify_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePCIDPackVerify(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ChangePCIDPackVerify", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PackVerifyCalcPackPCIDCount
   Description: Calculates the number of PCIDs with qty in a pack
   OperationID: PackVerifyCalcPackPCIDCount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PackVerifyCalcPackPCIDCount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PackVerifyCalcPackPCIDCount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PackVerifyCalcPackPCIDCount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/PackVerifyCalcPackPCIDCount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PackVerifyPerformPackVerification
   Description: For the pack verify UI form: performs the pack verification to indicate if the verification is complete
   OperationID: PackVerifyPerformPackVerification
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PackVerifyPerformPackVerification_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PackVerifyPerformPackVerification_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PackVerifyPerformPackVerification(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/PackVerifyPerformPackVerification", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingDispNumberOfPieces
   Description: Logic for when the number of pieces is changing
   OperationID: OnChangingDispNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingDispNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingDispNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingDispNumberOfPieces(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/OnChangingDispNumberOfPieces", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/OnChangingRevisionNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingRevisionNumPackOut
   OperationID: OnChangingRevisionNumPackOut
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNumPackOut_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNumPackOut_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingRevisionNumPackOut(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/OnChangingRevisionNumPackOut", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/OnChangingAttributeSet", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPackTaxID
   Description: Customer Tax Id check
   OperationID: CheckPackTaxID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPackTaxID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackTaxID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPackTaxID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CheckPackTaxID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPackTaxIDForPackNum
   Description: Customer Tax Id check for a given pack number
   OperationID: CheckPackTaxIDForPackNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPackTaxIDForPackNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackTaxIDForPackNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPackTaxIDForPackNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CheckPackTaxIDForPackNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetShippedFromPackout
   Description: Updates shipped status on customer shipment when set from Pack out
   OperationID: SetShippedFromPackout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetShippedFromPackout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetShippedFromPackout_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetShippedFromPackout(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SetShippedFromPackout", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewShipHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewShipHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetNewShipHead", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewShipHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipHeadAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewShipHeadAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetNewShipHeadAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCartonTrkDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCartonTrkDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCartonTrkDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCartonTrkDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCartonTrkDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetNewCartonTrkDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewShipDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewShipDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetNewShipDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewShipDtlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipDtlAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipDtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipDtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewShipDtlAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetNewShipDtlAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewShipCOO
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipCOO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipCOO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipCOO_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewShipCOO(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetNewShipCOO", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewShipDtlTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipDtlTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipDtlTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipDtlTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewShipDtlTax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetNewShipDtlTax", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewShipHeadInsurance
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipHeadInsurance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipHeadInsurance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipHeadInsurance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewShipHeadInsurance(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetNewShipHeadInsurance", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewShipMisc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipMisc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipMisc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipMisc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewShipMisc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetNewShipMisc", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewShipHeadTrailer
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipHeadTrailer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipHeadTrailer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipHeadTrailer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewShipHeadTrailer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetNewShipHeadTrailer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewShipUPS
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipUPS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipUPS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipUPS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewShipUPS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetNewShipUPS", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExpireDate
   OperationID: ExpireDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExpireDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExpireDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExpireDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ExpireDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CallsCreateCustomerCartons
   Description: Purpose:  Create Phantom Customer Cartons
Parameters:
<param name="ipPackNum">Current packNum</param><param name="ipNbrCartonsToCreate">Number of cartons or cases to create</param><param name="ipPkgCode">Package Code to use when creating cartons</param><param name="ipPkgLength">length to use when creating cartons</param><param name="ipPkgWidth">Width to use when creating cartons</param><param name="ipPkgHeight">Height to use when creating cartons</param><param name="ipRecalcAmts">Logical indicating if the amounts are to be recalculated</param><param name="ipZeroWeight">Logical indicating if the weights are recalculated</param><param name="ds"></param>
Notes:  Called from Kinetic so first need to dirty rows
   OperationID: CallsCreateCustomerCartons
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CallsCreateCustomerCartons_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CallsCreateCustomerCartons_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CallsCreateCustomerCartons(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CallsCreateCustomerCartons", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateCustomerCartons
   Description: Purpose:  Create Phantom Customer Cartons
Parameters:
<param name="ipNbrCartonsToCreate">Number of cartons or cases to create</param><param name="ipPkgCode">Package Code to use when creating cartons</param><param name="ipPkgLength">length to use when creating cartons</param><param name="ipPkgWidth">Width to use when creating cartons</param><param name="ipPkgHeight">Height to use when creating cartons</param><param name="ipRecalcAmts">Logical indicating if the amounts are to be recalculated</param><param name="ipZeroWeight">Logical indicating if the weights are recalculated</param><param name="ds"></param>
Notes:
   OperationID: CreateCustomerCartons
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateCustomerCartons_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateCustomerCartons_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateCustomerCartons(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CreateCustomerCartons", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AllowUndoExternalDN
   Description: This method exists soley for the purpose of allowing security for
unchecking the external delivery note flag to be defined
   OperationID: AllowUndoExternalDN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AllowUndoExternalDN_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AllowUndoExternalDN(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/AllowUndoExternalDN", {
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
   Summary: Invoke method AskForShipToChange
   Description: Checks if user must be asked for take a different Shipping Information
   OperationID: AskForShipToChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AskForShipToChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AskForShipToChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AskForShipToChange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/AskForShipToChange", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AssignLegalNumber
   Description: Assigns a legal number to the customer shipment.
   OperationID: AssignLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssignLegalNumber(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/AssignLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPackageControlPackVoid
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipPackNum">ipPackNum</param>
   OperationID: GetPackageControlPackVoid
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPackageControlPackVoid_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackageControlPackVoid_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPackageControlPackVoid(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetPackageControlPackVoid", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VoidPackSlip
   Description: Purpose:
Parameters:  none
Notes:
<param name="packNum">Pack Num</param><param name="ds">Package Control pack Void data set</param>
   OperationID: VoidPackSlip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidPackSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidPackSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VoidPackSlip(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/VoidPackSlip", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildCompSerMatch
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipPartNum">ipPartNum</param><param name="ipRevNum">ipRevNum</param><param name="ipSerialNumbers">ipSerialNumbers</param>
   OperationID: BuildCompSerMatch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildCompSerMatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildCompSerMatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildCompSerMatch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/BuildCompSerMatch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildSerialMatchingParams
   Description: This method fills the SerialMatchingParams Dataset with information
   OperationID: BuildSerialMatchingParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildSerialMatchingParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildSerialMatchingParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildSerialMatchingParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/BuildSerialMatchingParams", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildShipToCustomerList
   Description: If the Order has releases to multiple Customers, this will return the list of available
Customer shiptos to select from
   OperationID: BuildShipToCustomerList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildShipToCustomerList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildShipToCustomerList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildShipToCustomerList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/BuildShipToCustomerList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildShipToList
   Description: If the Order has releases to multiple shipto's, this will return the list of available
shiptos to select from
   OperationID: BuildShipToList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildShipToList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildShipToList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildShipToList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/BuildShipToList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CalculateWeight
   Description: Purpose:  calculate the weight of a carton based upon Part.Weight.
<param name="cartonNumber">PackID </param><param name="calculatedWeight">calculated weight</param>
   OperationID: CalculateWeight
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateWeight_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateWeight_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalculateWeight(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CalculateWeight", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CancelVoid
   Description: This method clears the void flag on the Pack Slip
   OperationID: CancelVoid
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CancelVoid_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CancelVoid_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CancelVoid(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CancelVoid", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CanStage
   Description: This method check that a shipment can be staged
   OperationID: CanStage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CanStage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CanStage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CanStage(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CanStage", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CartonValidateWeight
   Description: Purpose:
<param name="ipWeight"> weight to validate</param>
Notes:
   OperationID: CartonValidateWeight
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CartonValidateWeight_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CartonValidateWeight_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CartonValidateWeight(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CartonValidateWeight", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeIncotermCode
   Description: This method checks incoterm
   OperationID: ChangeIncotermCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeIncotermCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeIncotermCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeIncotermCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ChangeIncotermCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeShipCmpl
   Description: This method performs validations when the ShipDtl.ShipCmpl field changes
   OperationID: ChangeShipCmpl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipCmpl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipCmpl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeShipCmpl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ChangeShipCmpl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeShipDtlMFCustID
   Description: Method to call when changing the Mark For Customer ID on the ShipDtl record.
Validates the Mark For Customer ID and ressets the ShipToNum to the Customer default.
   OperationID: ChangeShipDtlMFCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipDtlMFCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipDtlMFCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeShipDtlMFCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ChangeShipDtlMFCustID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeShipDtlMFShipToNum
   Description: Update ShipDtl information with values from the Mark For when the Mark For is changed.
   OperationID: ChangeShipDtlMFShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipDtlMFShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipDtlMFShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeShipDtlMFShipToNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ChangeShipDtlMFShipToNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeShipDtlUseOTMF
   Description: Method to call when changing the UseOTMF field the ShipDtl record.
Refreshes the address list and contact info
   OperationID: ChangeShipDtlUseOTMF
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipDtlUseOTMF_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipDtlUseOTMF_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeShipDtlUseOTMF(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ChangeShipDtlUseOTMF", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeShipHeadShipToCustID
   Description: Executed when ShipToCustID has changed in the Ship Header
   OperationID: ChangeShipHeadShipToCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipHeadShipToCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipHeadShipToCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeShipHeadShipToCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ChangeShipHeadShipToCustID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeShipMiscPrcnt
   Description: This method populates the miscellaneous amount fields after
a miscellaneous charge percentage has been changed
   OperationID: ChangeShipMiscPrcnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipMiscPrcnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipMiscPrcnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeShipMiscPrcnt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ChangeShipMiscPrcnt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeShipMiscAmount
   Description: This method populates the miscellaneous amount fields after
a miscellaneous charge amount has been changed, if doc amount is changed a new non-doc amount is calculated, and vice versa
DspMiscAmt is the base currency amount column, DocMiscAmt is the ShipHead currency amount column.
"DocDspMiscAmt" column is not  because there is no "InDocMiscAmt" column, the DocMiscAmt is simply the currency equivalent of
DspMiscAmt which in turn is either the MiscAmt or InMiscAmt value depending on the InPrice setting
   OperationID: ChangeShipMiscAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipMiscAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipMiscAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeShipMiscAmount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ChangeShipMiscAmount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeStatus
   Description: This method will be called to perform a change in the header status.
   OperationID: ChangeStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeStatus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ChangeStatus", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePCID
   Description: NOTE - Customer Shipment Entry and HHPackOutEnty are now calling ChangePCIDPackVerify rather than ChangePCID
in order to give more functionality of 'Removing' a PCID when entered more than once.
Check for every line of the Pack if it requires if it is compliant.
   OperationID: ChangePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePCID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ChangePCID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeWarrantyToFSA
   Description: This method will update the value of the warrantySendToFSA field, if the warranty is sync with the FSA Integration.
   OperationID: ChangeWarrantyToFSA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeWarrantyToFSA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeWarrantyToFSA_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeWarrantyToFSA(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ChangeWarrantyToFSA", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RemovePCID
   Description: Back out pack detail lines related to a PCID
   OperationID: RemovePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemovePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemovePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemovePCID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/RemovePCID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckCompliance
   Description: Check for every line of the Pack if it requires if it is compliant.
   OperationID: CheckCompliance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCompliance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCompliance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCompliance(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CheckCompliance", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckCOOPercents
   Description: Checks to see if the Qty percent and value percent fields total 100 percent.
   OperationID: CheckCOOPercents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCOOPercents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCOOPercents_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCOOPercents(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CheckCOOPercents", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckCNCustomsDeclarationBillLine
   Description: Purpose:  Check Declaration Bill Line
Parameters:
<param name="bBeforeUpdate">if True - method is called before updating</param><param name="sMessage">Warning</param><param name="ds"></param>
   OperationID: CheckCNCustomsDeclarationBillLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCNCustomsDeclarationBillLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCNCustomsDeclarationBillLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCNCustomsDeclarationBillLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CheckCNCustomsDeclarationBillLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckOrder
   Description: This method check releases related with this pack were refused to close because non shipped pack existing.
   OperationID: CheckOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckOrder(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CheckOrder", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckOrderComplete
   Description: This method is to be run before update Shipped flag (true) to check if order or line of the pack needs
to be shipped complete, and ask the user if he wants to continue. If the user answers no, then the update method should not be called.
   OperationID: CheckOrderComplete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckOrderComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOrderComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckOrderComplete(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CheckOrderComplete", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPrePartInfo
   OperationID: CheckPrePartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPrePartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPrePartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPrePartInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CheckPrePartInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckReadyToInvoice
   OperationID: CheckReadyToInvoice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckReadyToInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckReadyToInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckReadyToInvoice(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CheckReadyToInvoice", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckShipDtl
   OperationID: CheckShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckShipDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CheckShipDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckValidCartonWeight
   Description: Purpose: Ensure the carton weight is valid.
<param name="ipPackNum">Pack Num to validate weights</param>
Notes:
   OperationID: CheckValidCartonWeight
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckValidCartonWeight_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckValidCartonWeight_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckValidCartonWeight(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CheckValidCartonWeight", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ClearConvertedManifestUOMFields
   Description: Purpose: Clear ShipHead Manifest fields when Unfreighting.
<param name="ipPackNum">Pack Num to clear Manifest fields</param>
Notes:
   OperationID: ClearConvertedManifestUOMFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearConvertedManifestUOMFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearConvertedManifestUOMFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClearConvertedManifestUOMFields(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ClearConvertedManifestUOMFields", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ConvertToManifestUOM
   Description: Purpose: Populate ShipHead Manifest fields.
<param name="ipPackNum">Pack Num to populate Manifest fields</param>
Notes:
   OperationID: ConvertToManifestUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvertToManifestUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertToManifestUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConvertToManifestUOM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ConvertToManifestUOM", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ConvertUOM
   Description: This method converts a qty from one UOM to another
   OperationID: ConvertUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvertUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConvertUOM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ConvertUOM", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateLot
   Description: Necessary method to create New Lot numbers for parts without attributes during the process of creating a pack.
   OperationID: CreateLot
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateLot_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateLot_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateLot(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CreateLot", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateMassShipDtl
   Description: This method copies the available Order Release lines to the ShipDtl datatable
for update
   OperationID: CreateMassShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateMassShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateMassShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateMassShipDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CreateMassShipDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeletePhantomPacks
   Description: Purpose:
<param name="ds">Customer Shipment data set </param>
Notes:
   OperationID: DeletePhantomPacks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeletePhantomPacks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeletePhantomPacks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeletePhantomPacks(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/DeletePhantomPacks", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteRangePhantomPacks
   Description: Purpose:
<param name="ipFromCase">First case number to start deletes</param><param name="ipToCase">Last case number to delete</param><param name="ds">Customer Shipment data set </param>
Notes:
   OperationID: DeleteRangePhantomPacks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteRangePhantomPacks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRangePhantomPacks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteRangePhantomPacks(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/DeleteRangePhantomPacks", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExpressShip
   Description: This method checks if the shipment is able to ship.
   OperationID: ExpressShip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExpressShip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExpressShip(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ExpressShip", {
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
   Summary: Invoke method GetCartonPackaging
   Description: Purpose: Obtain the carton pacakcing specs
<param name="ipPkgCode">package code</param><param name="opPkgHeight">package height</param><param name="opPkgWidth">package width</param><param name="opPkgLength">package length</param>
Notes:
   OperationID: GetCartonPackaging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCartonPackaging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCartonPackaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCartonPackaging(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetCartonPackaging", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCustShipOrdTrk
   Description: Get Customer Shipments for the Order.
   OperationID: GetCustShipOrdTrk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustShipOrdTrk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustShipOrdTrk_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCustShipOrdTrk(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetCustShipOrdTrk", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetHeadOrderInfo
   Description: This method displays the customer/address information when the OrderNum field
in the header changes. Should only be called for new Customer Shipments, or
Customer Shipments w/o lines
   OperationID: GetHeadOrderInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetHeadOrderInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHeadOrderInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetHeadOrderInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetHeadOrderInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetEnablePackageControl
   OperationID: GetEnablePackageControl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEnablePackageControl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEnablePackageControl(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetEnablePackageControl", {
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
   Summary: Invoke method GetDisablePackOut
   Description: Get value of DisablePackOut from Plant Configuration.
   OperationID: GetDisablePackOut
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDisablePackOut_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDisablePackOut(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetDisablePackOut", {
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
   Summary: Invoke method GetJobDtlInfo
   Description: This method defaults the ShipDtl fields with the JobNum field changes
   OperationID: GetJobDtlInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJobDtlInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJobDtlInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetJobDtlInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetJobDtlInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetJobInfo
   Description: This method populates the Order and Address fields after the JobNum field has been populated
   OperationID: GetJobInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJobInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJobInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetJobInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetJobInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetJobSupOpSeq
   Description: This method Gets the Job Suboperations Sequence Numbers to retrive the Serial Numbers Selected for the PartNum
   OperationID: GetJobSupOpSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJobSupOpSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJobSupOpSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetJobSupOpSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetJobSupOpSeq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLegalNumGenOpts
   Description: Returns the legal number generation options.
   OperationID: GetLegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLegalNumGenOpts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetLegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method POGetLegalNumGenOpts
   Description: Returns the legal number generation options.
   OperationID: POGetLegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POGetLegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POGetLegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POGetLegalNumGenOpts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/POGetLegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AfterChangedShipDtlOrderNum
   Description: Purpose:
<param name="ipSalesOrder">Sales Order</param><param name="ipPackNum">Pack Number</param><param name="ds">Customer Shipment data set</param>
Notes:  Default manifest information from the sales order. Used from Kinetic UI.
   OperationID: AfterChangedShipDtlOrderNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AfterChangedShipDtlOrderNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AfterChangedShipDtlOrderNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AfterChangedShipDtlOrderNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/AfterChangedShipDtlOrderNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetManifestInfo
   Description: Purpose:
<param name="ipSalesOrder">Sales Order</param><param name="ipPackNum">Pack Number</param><param name="ds">Customer Shipment data set</param>
Notes:  Default manifest information from the sales order.
   OperationID: GetManifestInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetManifestInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetManifestInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetManifestInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetManifestInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewOrdrShipDtl
   Description: Creates a new ShipDtl record, but defaulting the order number (if provided) as well
as other data from the OrderHed record.
   OperationID: GetNewOrdrShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewOrdrShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOrdrShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewOrdrShipDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetNewOrdrShipDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewOrdrShipUPS
   Description: Creates a new ShipUS record,
   OperationID: GetNewOrdrShipUPS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewOrdrShipUPS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOrdrShipUPS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewOrdrShipUPS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetNewOrdrShipUPS", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetOrderInfo
   Description: This method displays the customer/address information when the OrderNum field changes
Should only be called for new Customer Shipments, or Customer Shipments w/o lines
   OperationID: GetOrderInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOrderInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrderInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOrderInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetOrderInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetOrderLineInfo
   Description: This method defaults the ShipDtl fields with the OrderLine fields
change
   OperationID: GetOrderLineInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOrderLineInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrderLineInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOrderLineInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetOrderLineInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetOrderRelInfo
   Description: This method defaults the ShipDtl fields with the OrderRel fields
change
   OperationID: GetOrderRelInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOrderRelInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrderRelInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOrderRelInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetOrderRelInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPackaging
   Description: Purpose:
<param name="ipPkgCode">package code</param><param name="ds">Customer Shipment data set </param>
Notes:
   OperationID: GetPackaging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPackaging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPackaging(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetPackaging", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPackClass
   Description: Purpose:
<param name="ipPkgClass">package class</param><param name="ds">Customer Shipment data set </param>
Notes:
   OperationID: GetPackClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPackClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPackClass(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetPackClass", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPackOutPartXRef
   Description: This method defaults PackOut fields when the PartNum field changes
   OperationID: GetPackOutPartXRef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPackOutPartXRef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackOutPartXRef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPackOutPartXRef(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetPackOutPartXRef", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PartNumChangeUserPrompts
   Description: This method is called before GetPartInfo to determine if the user wants to continue based on questionString prompt
   OperationID: PartNumChangeUserPrompts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartNumChangeUserPrompts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartNumChangeUserPrompts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartNumChangeUserPrompts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/PartNumChangeUserPrompts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPartInfo
   Description: This method defaults ShipDtl fields when the PartNum field changes
   OperationID: GetPartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetPartInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPayBTFlagDefaults
   Description: Purpose:
<param name="ipOrderNum">First sales order on shipment</param><param name="ipPayFlag"> Pay Flag to retrieve defaults</param><param name="ds">The customer shipment data set </param>
Notes:
   OperationID: GetPayBTFlagDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPayBTFlagDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPayBTFlagDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPayBTFlagDefaults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetPayBTFlagDefaults", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPOPackaging
   Description: Purpose:
<param name="ipPkgCode">package code</param><param name="ds">Customer PackOut data set </param>
Notes:
   OperationID: GetPOPackaging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPOPackaging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPOPackaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPOPackaging(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetPOPackaging", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPOPackClass
   Description: Purpose:
<param name="ipPkgClass">package class</param><param name="ds">Packout data set </param>
Notes:
   OperationID: GetPOPackClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPOPackClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPOPackClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPOPackClass(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetPOPackClass", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetQtyInfo
   Description: This method defaults the ShipDtl Netweight and Quantity fields when the
ShipDtl.DisplayInvQty or ShipDtl.OurJobShipQty fields change
   OperationID: GetQtyInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQtyInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQtyInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQtyInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetQtyInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Calls the normal GetRows method and then constructs a custom data set combining Head/Dtl fields for the contact tracker.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetRowsContactTracker", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsCustomerTrackerAndSort
   Description: Calls the normal GetRows method and then constructs a custom data set combining Job and Order fields for the customer tracker.
   OperationID: GetRowsCustomerTrackerAndSort
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTrackerAndSort_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTrackerAndSort_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCustomerTrackerAndSort(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetRowsCustomerTrackerAndSort", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Calls the normal GetRows method and then constructs a custom data set combining Head/Dtl fields for the customer tracker.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetRowsCustomerTracker", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsForCashReceipt
   Description: Invokes GetRows filtering on shipments for the specified Cash Receipt
   OperationID: GetRowsForCashReceipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForCashReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForCashReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForCashReceipt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetRowsForCashReceipt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsForInvoice
   Description: Invokes GetRows filtering on shipments for the specified Invoice
   OperationID: GetRowsForInvoice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForInvoice(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetRowsForInvoice", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsForQuote
   Description: Invokes GetRows filtering on shipments for the specified Quote
   OperationID: GetRowsForQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForQuote(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetRowsForQuote", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetScale
   Description: Calls GetDefaultScale
   OperationID: GetScale
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetScale_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetScale_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetScale(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetScale", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSelectIDNumbersParams
   Description: Returns specific data needed to continue with selecting ID Numbers
   OperationID: GetSelectIDNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectIDNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectIDNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectIDNumbersParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetSelectIDNumbersParams", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipPartNum">ipPartNum</param><param name="ipAttributeSetID">ipAttributeSetID</param><param name="ipQuantity">ipQuantity</param><param name="ipUOM">ipUOM</param><param name="ipPackNum">ipPackNum</param><param name="ipPackLine">ipPackLine</param><param name="ipTranType">ipTranType</param><param name="ipJobNum">ipJobNum</param><param name="ipWhseCode">ipWhseCode</param><param name="ipBinNum">ipBinNum</param><param name="ipLotNum">ipLotNum</param><param name="ipFromPO">ipFromPO</param><param name="ipOrderNum">ipOrderNum</param><param name="ipOrderLine">ipOrderLine</param><param name="ipOrderRelNum">ipOrderRelNum</param><param name="ipSysRowID">ipSysRowID</param><returns></returns>
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetSelectSerialNumbersParams", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetShipmentRelationshipMap
   Description: Returns a serialized json string to show a Relationship Map for Shipment
   OperationID: GetShipmentRelationshipMap
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShipmentRelationshipMap_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShipmentRelationshipMap_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetShipmentRelationshipMap(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetShipmentRelationshipMap", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateSelectIDNumParams
   Description: Purpose: Generate Select ID Number Parameters related to Location Management.
Parameters:  none
Notes:
<param name="SNList">Serial Number List </param><param name="ipPartNum">PartNum</param><param name="ipPackNum">PackNum</param><param name="ipPackLine">PackLine</param><param name="ipJobNum">JobNum</param><param name="ipUom">UOM</param><param name="ipFromMfg">Called from Mfg</param>
   OperationID: GenerateSelectIDNumParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateSelectIDNumParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateSelectIDNumParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateSelectIDNumParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GenerateSelectIDNumParams", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateLocationIDNum
   Description: This method will be used to create records in LocationIDNum table
   OperationID: GenerateLocationIDNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateLocationIDNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateLocationIDNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateLocationIDNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GenerateLocationIDNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetShipMiscDefaults
   Description: This method populates the Description and miscellaneous amount fields after
a miscellaneous charge code has been selected
   OperationID: GetShipMiscDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShipMiscDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShipMiscDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetShipMiscDefaults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetShipMiscDefaults", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetShipToAddr
   Description: This method displays the shipto address information when the ShipToNum field changes
Should only be called on new Shipments or if the Shipment has no lines and if
the MultipleShippers flag is yes
   OperationID: GetShipToAddr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShipToAddr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShipToAddr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetShipToAddr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetShipToAddr", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTranDocTypeID
   Description: Sets default values when the TranDocTypeID changes
   OperationID: GetTranDocTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTranDocTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTranDocTypeID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetTranDocTypeID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CalculateWarrantyExpiration
   Description: Calculates the expiration date fields based on effective date to the specified line/rel
   OperationID: CalculateWarrantyExpiration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateWarrantyExpiration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateWarrantyExpiration_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalculateWarrantyExpiration(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CalculateWarrantyExpiration", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetWarrantyInfo
   Description: set warranty info to ship detail fields related to warranty
   OperationID: GetWarrantyInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWarrantyInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWarrantyInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetWarrantyInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetWarrantyInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ClearWarrantyInfo
   Description: clears warranty fields on the specified orderLine/orderrelnum
   OperationID: ClearWarrantyInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearWarrantyInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearWarrantyInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClearWarrantyInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ClearWarrantyInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetWhseInfo
   Description: This method defaults the ShipDtl Warehouse and bin fields when the warehousecode changes
   OperationID: GetWhseInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWhseInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWhseInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetWhseInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/GetWhseInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method HHCreateMassShipDtl
   Description: This method copies the available Order Release lines to the ShipDtl datatable
for update
   OperationID: HHCreateMassShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HHCreateMassShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HHCreateMassShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HHCreateMassShipDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/HHCreateMassShipDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method HHGetOrderInfo
   Description: This method sets the defaults quantities and Primary Bins fields as CreateMassShipment complements
This method is used for HandHelds Version
   OperationID: HHGetOrderInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HHGetOrderInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HHGetOrderInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HHGetOrderInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/HHGetOrderInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method HHSetDtlDefaultValues
   Description: OBSOLETE - OBSOLETE - OBSOLETE - OBSOLETE - OBSOLETE - OBSOLETE - OBSOLETE - OBSOLETE - OBSOLETE
Use MarkShipmentLines instead (the same logic that is used by the regular screen)
OBSOLETE - OBSOLETE - OBSOLETE - OBSOLETE - OBSOLETE - OBSOLETE - OBSOLETE - OBSOLETE - OBSOLETE
This method sets the defaults quantities and Primary Bins fields as CreateMassShipment complements
This method is used for HandHelds Version
   OperationID: HHSetDtlDefaultValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HHSetDtlDefaultValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HHSetDtlDefaultValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HHSetDtlDefaultValues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/HHSetDtlDefaultValues", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MarkShipmentLines
   Description: This method sets all the temp-table records to be shipped (Ship all button selected)
   OperationID: MarkShipmentLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MarkShipmentLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MarkShipmentLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MarkShipmentLines(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/MarkShipmentLines", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PhantomStatusCheck
   Description: Purpose :Check the phantom status
<param name="ipPackNum">pack number to check status</param>
Notes:
   OperationID: PhantomStatusCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PhantomStatusCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PhantomStatusCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PhantomStatusCheck(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/PhantomStatusCheck", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method POChangeStage
   Description: This method will be called to perform a change in the pack stage.
   OperationID: POChangeStage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POChangeStage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POChangeStage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POChangeStage(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/POChangeStage", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method POChangeStatus
   Description: This method will be called to perform a change in the header status from the pack Out
screen.
   OperationID: POChangeStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POChangeStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POChangeStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POChangeStatus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/POChangeStatus", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method POFindBuffer
   Description: This method returns a count order of lines that match the incomming scanned criteria.
If there is only 1 match, it will copy the order dtl data into the returning record.
If there is no unique match, logical fields are updated to que the UI as to what need
to be prompted in order to find a matching order dtl.
   OperationID: POFindBuffer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POFindBuffer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POFindBuffer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POFindBuffer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/POFindBuffer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method POFindBufWhseBinLot
   Description: The purpose of this method is to return a unique PackOut.PackLine number if the
warehouse or bin or lot changes.  If it finds the match of an available shipdtl
then it will return the rowident of the matching shipdtl. IF not the line number
of the PackOut is incremented.
   OperationID: POFindBufWhseBinLot
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POFindBufWhseBinLot_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POFindBufWhseBinLot_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POFindBufWhseBinLot(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/POFindBufWhseBinLot", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method POGetDtlList
   Description: This method copies the available Order Release lines to the PackOut datatable for update
from HHVerifyForm (advanced PCID): ipPackMode = blank, ipOrderNum = 0, PCID = blank
   OperationID: POGetDtlList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POGetDtlList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POGetDtlList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POGetDtlList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/POGetDtlList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method POGetNew
   Description: This method creates a new packout record for the customer shipment packout
screen. can pass in a OrderNum or PackNum or Both.
   OperationID: POGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POGetNew(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/POGetNew", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreatePackForChangePCID
   Description: This method executes GetNewShipHead and saves to the db and returns the new PackNum to support the entry
of a PCID in packout entry when the pack has not yet been created. Not called by Classic UIApp
   OperationID: CreatePackForChangePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreatePackForChangePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreatePackForChangePCID(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/CreatePackForChangePCID", {
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
   Summary: Invoke method POGetNewWithDtl
   Description: Return a tableset populated with PackOut header and detail list.
   OperationID: POGetNewWithDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POGetNewWithDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POGetNewWithDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POGetNewWithDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/POGetNewWithDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteKitComponents
   Description: Delete the kit components when the line/release is changed
   OperationID: DeleteKitComponents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteKitComponents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteKitComponents_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteKitComponents(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/DeleteKitComponents", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateOrderRelOnKitChildren
   Description: Update the kit components with new release number
   OperationID: UpdateOrderRelOnKitChildren
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateOrderRelOnKitChildren_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateOrderRelOnKitChildren_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateOrderRelOnKitChildren(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/UpdateOrderRelOnKitChildren", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method POGetShipTo
   Description: This method sets the ttPackOut ShipTo name/address display fields
screen
   OperationID: POGetShipTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POGetShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POGetShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POGetShipTo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/POGetShipTo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PostUpdate
   Description: This method will return a message if a credit card shipment was processed
during update or there are warning messages regarding outbound lower level serial tracking
   OperationID: PostUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PostUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PostUpdate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/PostUpdate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method POUpdate
   Description: This method creates a new packout record to create Shiphead and shipdtl records
   OperationID: POUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POUpdate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/POUpdate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method POUpdateAndDisplay
   Description: This method creates a new packout record to create Shiphead and shipdtl records
   OperationID: POUpdateAndDisplay
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POUpdateAndDisplay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POUpdateAndDisplay_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POUpdateAndDisplay(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/POUpdateAndDisplay", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method POValidateOrder
   Description: This method sets the service contract invoiced flag to match the shiphead flag
   OperationID: POValidateOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POValidateOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POValidateOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POValidateOrder(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/POValidateOrder", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method POValidateOrderRel
   Description: Purpose: Verify the newly entered order rel is for the same bill to and shipto
Parameters:
<param name="ipPackNum">pack number</param><param name="ipOrderNum">sales order number</param><param name="ipOrderLine">sales order line number</param><param name="ipOrderRelNum">sales order release number</param>
Notes:
   OperationID: POValidateOrderRel
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POValidateOrderRel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POValidateOrderRel_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POValidateOrderRel(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/POValidateOrderRel", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method POValidatePart
   Description: Validates whether the provided part is valid or not for a given sales order.
   OperationID: POValidatePart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POValidatePart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POValidatePart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POValidatePart(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/POValidatePart", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreCreateMassShipDtl
   Description: This method checks to see if it's okay to copy the available Order Release lines
to the ShipDtl datatable for update in Mass Shipments
   OperationID: PreCreateMassShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreCreateMassShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreCreateMassShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreCreateMassShipDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/PreCreateMassShipDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePickeOrdersIsSelected
   Description: This method executes the picked order view OnChanging logic for PickedOrders.IsSelected for the CustShip Kinetic UI / Picked Orders form
WinForm does all of this within the UIApps MaintTransaction IsSelected OnChanging method. This method executes the logic for
ProcessKitChildren plus the logic to select/deselect any related PickedOrders rows in the ds per the logic in UIapps
   OperationID: OnChangePickeOrdersIsSelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePickeOrdersIsSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePickeOrdersIsSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePickeOrdersIsSelected(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/OnChangePickeOrdersIsSelected", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessKitChildern
   Description: This method checks if UI should process the components of the kit parent
   OperationID: ProcessKitChildern
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessKitChildern_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessKitChildern_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessKitChildern(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ProcessKitChildern", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PrePickedOrders
   Description: This method is run right before PickedOrders.  If not all of the line details have
been picked to ship a question will be returned to the user.  If yes, then
call PickedOrders, if no allow the user to pick another order
   OperationID: PrePickedOrders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePickedOrders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePickedOrders_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrePickedOrders(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/PrePickedOrders", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PrintSlip
   Description: This method prints the Customer Packing Slip
   OperationID: PrintSlip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrintSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrintSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrintSlip(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/PrintSlip", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessMassShipKit
   Description: Purpose:
Parameters:  none
Notes:
   OperationID: ProcessMassShipKit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessMassShipKit_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessMassShipKit(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ProcessMassShipKit", {
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
   Summary: Invoke method ProcessPickedOrder
   Description: This method creates the packing slip for the selected picked order (desktop)
Will only process picked orders marked as selected.
   OperationID: ProcessPickedOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessPickedOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessPickedOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessPickedOrder(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ProcessPickedOrder", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessPickedOrderHH
   Description: This method creates the packing slip for the selected picked order (handheld)
Will also process other releases for the same order
   OperationID: ProcessPickedOrderHH
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessPickedOrderHH_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessPickedOrderHH_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessPickedOrderHH(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/ProcessPickedOrderHH", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RebuildShipUPS
   Description: Purpose: Rebuild the shipUPS records
<param name="ipPackNum">Packnum to update</param><param name="ds">The customer shipment data set </param>
   OperationID: RebuildShipUPS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RebuildShipUPS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RebuildShipUPS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RebuildShipUPS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/RebuildShipUPS", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetUPSQVEnable
   Description: Purpose:
<param name="ipQVEnable">logical indicating if the quantum view is to enabled/disabled</param><param name="ds">The customer shipment data set </param>
Notes:
   OperationID: SetUPSQVEnable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetUPSQVEnable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUPSQVEnable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetUPSQVEnable(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SetUPSQVEnable", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeUPSQuantumView
   Description: Purpose:
<param name="ipPackNum">current packNum</param><param name="ipQVEnable">logical indicating if the quantum view is to enabled/disabled</param><param name="ds">The customer shipment data set </param>
Notes:  This was created for Kinetic UI
   OperationID: OnChangeUPSQuantumView
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeUPSQuantumView_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUPSQuantumView_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeUPSQuantumView(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/OnChangeUPSQuantumView", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeShipViaCode
   Description: Function to set default values related to ShipVia
   OperationID: OnChangeShipViaCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeShipViaCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeShipViaCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeShipViaCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/OnChangeShipViaCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetUPSQVShipStatus
   Description: Purpose:
<param name="ipShipStatus">Shipment status</param><param name="ds">The customer shipment data set </param>
Notes:
   OperationID: SetUPSQVShipStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetUPSQVShipStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUPSQVShipStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetUPSQVShipStatus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSvc/SetUPSQVShipStatus", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CartonTrkDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CartonTrkDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumGenOptsRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumberGenerateRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumberGenerateRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReplicatedPacksRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ReplicatedPacksRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SNFormatRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesKitCompIssueRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SalesKitCompIssueRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedIDNumbersRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SelectedIDNumbersRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SelectedSerialNumbersRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipCOORow{
   "odatametadata":string,
   "value":Erp_Tablesets_ShipCOORow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ShipDtlAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlPackagingRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ShipDtlPackagingRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ShipDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlTaxRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ShipDtlTaxRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ShipHeadAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadInsuranceRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ShipHeadInsuranceRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ShipHeadListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ShipHeadRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadTrailerRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ShipHeadTrailerRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipMiscRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ShipMiscRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipTaxSumRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ShipTaxSumRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipUPSRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ShipUPSRow[],
}

export interface Erp_Tablesets_CartonTrkDtlRow{
      /**  Company ID  */  
   "Company":string,
      /**  Defines the type of shipment the tracking number is for.  Shipment type is either Misc for miscellaneous, Sales for Customer shipments, Sub for subcontractor shipments Transfer for Transfer order shipment or Master for Masterpack Shipments.  */  
   "ShipmentType":string,
      /**  The pack number associated with the tracking number.  */  
   "PackNum":number,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last CartonTrkDtl record for PackNum and add 1. This number is not displayed to the user.  The case number the user sees is the concatenation of the Packnum and this number separated by a dash.  */  
   "CaseNum":number,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   "PkgLength":number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   "PkgHeight":number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   "PkgWidth":number,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   "TrackingNumber":string,
      /**  Package Weight  */  
   "PkgWeight":number,
      /**  Prefer COD delivery.  Reserved for future development.  */  
   "CODFlag":boolean,
      /**  Cashier's Check or Money order is required on COD Delivery
Reserved for future development.  */  
   "CODCheck":boolean,
      /**  Amount due on Cashier's check or money order.  Reserved for future development.  */  
   "CODAmount":number,
      /**  Flag to indicate that an insurance value was declared on delivery.  Reserved for future development.  */  
   "DeclaredValueFlag":boolean,
      /**  Declared Insurance Amount.  Reserved for future development.  */  
   "DeclaredValue":number,
      /**  Unit of Measure the Manifest system expects the pack sizet to be measured in.  */  
   "ManifestSizeUOM":string,
      /**  Unit of Measure of the Manifest system expects the pack to be weighed in.  */  
   "ManifestWtUOM":string,
      /**  Package Weight in the Manifest System's unit of measure.  */  
   "ManifestWeight":number,
      /**  The pack length in the Manifest Unit of Measure.  */  
   "ManifestLength":number,
      /**  The pack width in the manifest unit of measure.  */  
   "ManifestWidth":number,
      /**  The pack height in the manifest unit of measure.  */  
   "ManifestHeight":number,
      /**  Collect On Delivery Value  */  
   "CODValue":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Concatenated field consisting of PackNum and CaseNum separated by a dash.  */  
   "CaseID":string,
      /**  Status of the shipment.  */  
   "PackStatus":string,
      /**  logical used by UI for row rules  */  
   "PhantomPack":boolean,
   "CapturePt":string,
      /**  Logical indicating if the phantom cartonTrkDtl fields are to be enabled.  This is based upon whether or not the workstation is setup for manifesting.  */  
   "EnablePhantom":boolean,
   "KitPartAttrClassID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LegalNumGenOptsRow{
   "Company":string,
   "LegalNumberID":string,
   "TransYear":number,
   "TransYearSuffix":string,
   "DspTransYear":string,
      /**  Indicates if DspTransYear should be displayed when prompting for a manual number.  */  
   "ShowDspTransYear":boolean,
   "Prefix":string,
      /**  The list of prefixes that can be selected by the user for manual numbers.  */  
   "PrefixList":string,
      /**  The suffix portion of the legal number.  */  
   "NumberSuffix":string,
      /**  Indicates if the prefix can be entered by the user.  */  
   "EnablePrefix":boolean,
      /**  Indicates if the suffix (number) can be entered by the user.  */  
   "EnableSuffix":boolean,
   "NumberOption":string,
   "DocumentDate":string,
   "GenerationType":string,
   "Description":string,
   "TransPeriod":number,
      /**  Prefix for the period  */  
   "PeriodPrefix":string,
   "ShowTransPeriod":boolean,
      /**  Used when the full legal number is entered  */  
   "LegalNumber":string,
   "TranDocTypeID":string,
   "TranDocTypeID2":string,
   "GenerationOption":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LegalNumberGenerateRow{
      /**  Company Identifier.  */  
   "Company":string,
   "NumberType":string,
   "NumberYear":number,
      /**  The legal number prefix  */  
   "NumberPrefix":string,
   "NumberSuffix":string,
   "PrefixList":string,
   "GenerationType":string,
   "EnableNumberPrefix":boolean,
   "EnableNumberSuffix":boolean,
   "NumberOption":string,
      /**  Unique identifier of the Legal Number record  */  
   "LegalNumberNum":number,
   "DocumentDate":string,
   "AdditionalParams":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ReplicatedPacksRow{
      /**  Company ID  */  
   "Company":string,
      /**  Parent Pack ID that is used to create the replicated packs.  */  
   "PackNum":number,
      /**  This is the pack num that was generated based upon the parent pack num.  */  
   "ReplicatedPackNum":number,
   "SysRowID":string,
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

export interface Erp_Tablesets_SalesKitCompIssueRow{
   "KitPartNum":string,
   "KitDescription":string,
   "KitWarehouseCodeDesc":string,
   "KitWarehouse":string,
   "KitWhseList":string,
   "PackNum":number,
   "PackLine":number,
   "KitQtyFromInv":number,
   "KitIUM":string,
   "KitLotNum":string,
   "KitBinNum":string,
   "OrderNum":number,
   "OrderLine":number,
   "OrderRelNum":number,
   "KitBinNumEnabled":boolean,
   "KitTrackLots":boolean,
   "KitSerialTracked":boolean,
   "KitQtyFromInvEnabled":boolean,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SelectedIDNumbersRow{
      /**  Company  */  
   "Company":string,
   "IDNumber":string,
   "JobNum":string,
   "PackLine":number,
   "PackNum":number,
   "PartNum":string,
   "SeqNum":number,
   "SerialNumber":string,
      /**  RowID of the source record for this ID number  */  
   "SourceRowID":string,
   "TransType":string,
   "SysRowID":string,
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

export interface Erp_Tablesets_ShipCOORow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique part number that identifies this part.  */  
   "PartNum":string,
      /**  CountryNum for Country of Origin  */  
   "OrigCountry":number,
      /**  Qty percent of this part which is from this country of origin.  */  
   "QtyPerc":number,
      /**  Value percent of this part from this country of origin.  */  
   "ValuePerc":number,
      /**  Is this the primary country of origin for this part  */  
   "Primary":boolean,
      /**  The master file to which the country of origin is related. ?ShipDtl?, ?MscShpDt?, ?TFShipDtl?, and ?SubShipD?  */  
   "RelatedToFile":string,
      /**  Packing slip number that this detail record is linked with.  */  
   "PackNum":number,
      /**  An integer that uniquely identifies a detail record within a Packing slip.  */  
   "PackLine":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "CountryDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ShipDtlAttchRow{
   "Company":string,
   "PackNum":number,
   "PackLine":number,
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

export interface Erp_Tablesets_ShipDtlPackagingRow{
   "Company":string,
   "PackNum":number,
   "PackLine":number,
   "ParentPkgNum":number,
   "TranDocTypeID":string,
   "TranDocTypeDesc":string,
   "PkgCode":string,
   "PkgCodeDesc":string,
   "PkgSerialNum":string,
   "PkgLength":number,
   "PkgWidth":number,
   "PkgHeight":number,
   "SizeUOM":string,
   "Weight":number,
   "WeightUOM":string,
   "LegalNumber":string,
   "PartNum":string,
   "OurQty":number,
   "IUM":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ShipDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Packing slip number that this detail record is linked with.  */  
   "PackNum":number,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  */  
   "PackLine":number,
      /**   The sales order number that this detail shipment line is linked to.
This is not directly maintainable, It is carried forward through from the ShipHead.OrderNum field.  */  
   "OrderNum":number,
      /**  The sales order line that this shipment detail line is linked to.  Must be valid in the OrderDtl file.  */  
   "OrderLine":number,
      /**  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  */  
   "OrderRelNum":number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   "LineType":string,
      /**  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand.  This quantity is in the IUM unit of measure.  */  
   "OurInventoryShipQty":number,
      /**  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This quantity is in the IUM unit of measure.  */  
   "OurJobShipQty":number,
      /**  Job Number that supplied the quantity that was shipped. Defaulted from OrderRel.JobNum.  */  
   "JobNum":string,
      /**  Number of Packages  */  
   "Packages":number,
      /**  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation. This is not user maintainable. If this is a shipment from inventory use this part number to reduce the Part.Onhand qty.  */  
   "PartNum":string,
      /**  Line Description  */  
   "LineDesc":string,
      /**  Unit of measure...duplicated from the OrderDtl.IUM...Not user maintainable.  */  
   "IUM":string,
      /**  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  */  
   "RevisionNum":string,
      /**   Holds any comments about the order line being shipped.  Viewed as an Editor widget.

This gets duplicated from the OrderDtl.ShipComment.  */  
   "ShipComment":string,
      /**  Indicates if this shipment should mark the order release as being shipped complete. Only one ShipDtl for a release can be marked as being complete. As the user toggles this field it also sets the OrderRel.ShipCmpl field and adjusts the PartBin.OnHand, PartWhse.AllocQty if necessary.  */  
   "ShipCmpl":boolean,
      /**   Indicates the warehouse from which the quantity was shipped. This is only valid if the ShipDtl.Inventory quantity is > 0 and this is a valid part number.

The default should be retrieved from the OrderDtl.WareHseCode. .  */  
   "WarehouseCode":string,
      /**  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  */  
   "BinNum":string,
      /**  Indicates if this transaction affected inventory at time of creation.  */  
   "UpdatedInventory":boolean,
      /**   An optional field that is used if the customer has a different  Part number  than the users internal part number.
This field is defaulted from the OrderDtl.XPartNum.  */  
   "XPartNum":string,
      /**  Optional field that contains the customers revision. Default from the OrderDtl.XRevisionNum field.  */  
   "XRevisionNum":string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table. This is duplicated from the OrderRel.ShpConNum.  */  
   "ShpConNum":number,
      /**  Indicates if this shipment line item will be invoiced for time and materials. This is not maintainable from within shipment entry. It is duplicated from the OrderDtl.TMBilling. The "Get Shipments" function of Invoice Entry uses this flag to automatically create invoices in a "On Hold" status. The idea is that these type of invoices need to be generated to act as a method of tracking invoice requirements, but they cannot yet be invoiced until all the costs are known. At which time the user will enter the appropriate charges, take it off "Hold" and complete the billing process.  */  
   "TMBilling":boolean,
      /**  A flag which indicates "invoicing" status. This is a mirror image of ShipHead.Invoiced field. See ShipHead.Invoiced for further info.  */  
   "Invoiced":boolean,
      /**  Weight Unit of measure...qualifies the weight field value. (Lb, Oz, Gr...). Defaulted from XASyst.DefaultWUM  */  
   "WUM":string,
      /**  Lot Number is for Inventory Shipments.  */  
   "LotNum":string,
      /**  Unique dimension code for the part.  */  
   "DimCode":string,
      /**  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  */  
   "DUM":string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   "DimConvFactor":number,
      /**  These comments will be copied into the Invoice detail.  */  
   "InvoiceComment":string,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   "WarrantyCode":string,
      /**  Customer number that the shipment is for.  Duplicated from ShipHead.CustNum.  Used to allow efficient browsing of the ShipDtl records for a specific customer.  */  
   "CustNum":number,
      /**  The shipto number. Used for warranty validation.  */  
   "ShipToNum":string,
      /**  For Warranty shipments.  Defaults as Shiphead.shipdate. But can be maintained from the Service Call center.  */  
   "EffectiveDate":string,
      /**  The # of days, months, years the material is covered by warranty  */  
   "MaterialDuration":number,
      /**  The # of days, months, years the Labor is covered by warranty  */  
   "LaborDuration":number,
      /**  The # of days, months, years the Misc. Charges are covered by warranty  */  
   "MiscDuration":number,
      /**  Whether the duration of warranty  is for "Days", " Months", "years".  */  
   "MaterialMod":string,
      /**  Whether the duration of warranty  is "Days"," Months"," years".  */  
   "LaborMod":string,
      /**  Whether the duration of warranty  is for "Days"," Months"," years".  */  
   "MiscMod":string,
      /**  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   "MaterialExpiration":string,
      /**  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   "LaborExpiration":string,
      /**  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   "MiscExpiration":string,
      /**  The latest of the 3 warranty expiration dates  */  
   "LastExpiration":string,
      /**  Editor widget for Warranty comments.  */  
   "WarrantyComment":string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   "ContractNum":number,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   "ContractCode":string,
      /**  This warranty covers On site visits  */  
   "Onsite":boolean,
      /**  Are Material cost covered  */  
   "MatCovered":boolean,
      /**  Is Labor Cost Covered  */  
   "LabCovered":boolean,
      /**  Are misc. Costs Covered  */  
   "MiscCovered":boolean,
      /**  Site that the shipment is from.  Duplicated from ShipHead.Site.  Used to allow efficient browsing of the ShipDtl records.  */  
   "Plant":string,
      /**  Indicates if the Packing Slip is complete and ready for invoicing.  This is a mirror image of ShipHead.ReadyToInvoice.  */  
   "ReadyToInvoice":boolean,
      /**  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand. This quantity is a mirror of field OurInventoryShipQty except it is in the SUM unit of measure.  */  
   "SellingInventoryShipQty":number,
      /**  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This field is a mirror of OurJobShipQty except it is in the SUM unit of measure.  */  
   "SellingJobShipQty":number,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "SellingFactor":number,
      /**  Selling Unit of Measure...duplicated from the OrderDtl.SUM...Not user maintainable.  */  
   "SalesUM":string,
      /**  The Part's Net Weight * (SellingJobShipQty + SellingInventoryShipQty)  */  
   "TotalNetWeight":number,
      /**   Identifies the warehouse for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area warehouse (Site.DefShipWhse) otherwise it's blank.  */  
   "WIPWarehouseCode":string,
      /**   Identifies the warehouse bin for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area bin (Site.DefShipBin) otherwise it's blank.  */  
   "WIPBinNum":string,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "SellingFactorDirection":string,
      /**  Packing slip comments.  These are comments off of the invoice header.  */  
   "HeaderShipComment":string,
      /**  The packline of the kit parent  */  
   "KitParentLine":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Unit of Measure of the quantity shipped from Inventory (OurInventoryShipQty). Must be a valid UOM. If Part is Multi-UOM tracking then only the Tracking UOMs are valid otherwise all UOM's of the Parts UOMClass are valid.  */  
   "InventoryShipUOM":string,
      /**  Unit of Measure of the quantity shipped from the Job (OurJobShipQty)  */  
   "JobShipUOM":string,
      /**  Indicates whether the ShipDtl.PartNum is serial tracked. Required as a db field rather than using the link to PartNumTrackSerialNum to allow validations based on the ShipDtl table rather than the ttShipDtl table. Default is No.  */  
   "TrackSerialNum":boolean,
      /**  Lot Number is for Job Shipments.  */  
   "JobLotNum":string,
      /**  Identifies the type of Bin is being used (valid values are 'Std', 'Cust', 'Supp').  Associated with field ShipDtl.BinNum  */  
   "BinType":string,
      /**  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  */  
   "NotCompliant":boolean,
      /**  Displays the cause why the item is not compliant.  */  
   "ComplianceMsg":string,
      /**  Unit price discount percent.  */  
   "DiscountPercent":number,
      /**   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   "PricePerCode":string,
      /**  A flat discount amount for the line item.  It can be zero.  */  
   "Discount":number,
      /**  A flat discount amount for the line item.  */  
   "DocDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Discount":number,
      /**  Extended Price for the invoice line item.  */  
   "ExtPrice":number,
      /**  Extended Price for the invoice line item.  */  
   "DocExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ExtPrice":number,
      /**  Unit Price.  */  
   "UnitPrice":number,
      /**  Unit Price.  */  
   "DocUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitPrice":number,
      /**  Quantity picked from inventory that was not manually allocated. This quantity is automatically added to PartAlloc such when inventory is picked, it is considered allocated to this Order.  This quantity is in the IUM unit of measure.  */  
   "PickedAutoAllocatedQty":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  A flat discount amount for the line item includes taxes.  It can be zero.  */  
   "InDiscount":number,
      /**  A flat discount amount for the line item includes taxes.  */  
   "DocInDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InDiscount":number,
      /**  Extended Price for the invoice line item including taxes.  */  
   "InExtPrice":number,
      /**  Extended Price for the invoice line item including taxes.  */  
   "DocInExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InExtPrice":number,
      /**  Unit Price including taxes.  */  
   "InUnitPrice":number,
      /**  Unit Price including taxes.  */  
   "DocInUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InUnitPrice":number,
      /**  Indicates that the tax is included in the unit price  */  
   "InPrice":boolean,
      /**  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  */  
   "MFCustNum":number,
      /**  The ShipTo ID to be used for this record. This MUST BE VALID IN THE SHIPTO file.  */  
   "MFShipToNum":string,
      /**  Indicates that the One Time Mark For information defined for this record should be used.  */  
   "UseOTMF":boolean,
      /**  One Time Mark For Name of the ShipTo.  */  
   "OTMFName":string,
      /**  One Time Mark For first line of the ShipTo address.  */  
   "OTMFAddress1":string,
      /**  One Time Mark For second line of the ShipTo address.  */  
   "OTMFAddress2":string,
      /**  One Time Mark For third line of the ShipTo address.  */  
   "OTMFAddress3":string,
      /**  City portion of the One Time Mark For address.  */  
   "OTMFCity":string,
      /**  The state or province portion of the One Time Mark For address.  */  
   "OTMFState":string,
      /**  The zip or postal code portion of the One Time Mark For address.  */  
   "OTMFZIP":string,
      /**  One Time Mark For Contact Name  */  
   "OTMFContact":string,
      /**  Fax number for the One Time Mark For.  */  
   "OTMFFaxNum":string,
      /**  Phone number for the One Time Mark For  */  
   "OTMFPhoneNum":string,
      /**  Country number for the One Time Mark For  */  
   "OTMFCountryNum":number,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   "RenewalNbr":number,
      /**  ShipOvers  */  
   "ShipOvers":boolean,
      /**  AllowedOvers  */  
   "AllowedOvers":number,
      /**  AllowedUnders  */  
   "AllowedUnders":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  This is the quantity being shipped that was not already previously allocated, and could not be auto allocated.  */  
   "NotAllocatedQty":number,
      /**  PCID  */  
   "PCID":string,
      /**  PCID Item Sequence  */  
   "PCIDItemSeq":number,
      /**  The dockingstation of the shipto address.  For future use.  */  
   "DockingStation":string,
      /**  For future use.  */  
   "UseShipDtlInfo":boolean,
      /**  PkgCodePartNum  */  
   "PkgCodePartNum":string,
      /**  CustContainerPartNum  */  
   "CustContainerPartNum":string,
      /**  LabelType  */  
   "LabelType":string,
      /**  Indicates that the warranty will be sent to FSA  */  
   "WarrantySendToFSA":boolean,
      /**  When the shipment line is marked as "send as equipment", it will create an Installation in Epicor FSA.  */  
   "FSAEquipment":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Number of pieces for this attribute set based on OurInventoryShipQty.  */  
   "InventoryNumberOfPieces":number,
      /**  Number of pieces for this attribute set based on OurJobShipQty.  */  
   "JobNumberOfPieces":number,
      /**  Estimated Value  */  
   "MXEstValue":number,
      /**  Estimated Value Currency  */  
   "MXEstValueCurrencyCode":string,
      /**  Hazardous Shipment  */  
   "MXHazardousShipment":boolean,
      /**  Hazardous Type  */  
   "MXHazardousType":string,
      /**  Package Type  */  
   "MXPackageType":string,
      /**  CNDeclarationBillLine  */  
   "CNDeclarationBillLine":number,
      /**  This is the quantity being shipped from manufacturing that was not already previously allocated, and could not be auto allocated.  */  
   "JobNotAllocatedQty":number,
      /**  Quantity picked from manufacturing that was not manually allocated.  */  
   "JobPickedAutoAllocatedQty":number,
      /**  Flag to indicate if Order/Line/Rel is Buy To Order  */  
   "BuyToOrder":boolean,
      /**  The date and time that the record was last changed  */  
   "ChangeDateTime":string,
   "CurrencyCode":string,
      /**  Delimited list of available Dimension codes for line  */  
   "DimCodeList":string,
      /**  OurInventoryShipQty * DimConvFactor - update inplace of OurInventoryShipQty  */  
   "DisplayInvQty":number,
   "DocLineTax":number,
      /**  Is Drop Shipment.  */  
   "DropShip":boolean,
      /**  Indicates if a detail line has errors to be corrected before leaving packing slip  */  
   "DtlError":boolean,
   "EnableInvIDBtn":boolean,
   "EnableInvSerialBtn":boolean,
      /**  Logical indicating if receipt to a job is allowed.  This is determined by either the xasyst.shipnojob field or whether or not the sales order is linked to a job.  */  
   "EnableJobFields":boolean,
   "EnableKitIDBtn":boolean,
   "EnableMfgIDBtn":boolean,
   "EnableMfgSerialBtn":boolean,
   "EnableOBInvSerialBtn":boolean,
   "EnableOBMfgSerialBtn":boolean,
      /**  Boolean indicating if the package control functionality should be enabled.  */  
   "EnablePackageControl":boolean,
   "EnablePOSerialBtn":boolean,
   "ExtJobNum":string,
   "FSAInstallationCost":number,
   "FSAInstallationOrderLine":number,
   "FSAInstallationOrderNum":number,
      /**  Indicates if the equipment requires an installation prior being marked as “Installed” on a Location in Epicor FSA. If true, at shipment it will create a service order for the installation service in FSA.  */  
   "FSAInstallationRequired":boolean,
   "FSAInstallationType":string,
      /**  Equal to true if opening Location ID Diaglog  */  
   "GetLocIDNum":boolean,
      /**  The invoice legal number.  */  
   "InvLegalNumber":string,
      /**  External field to be used in the SalesOrder Tracker to show the user the InvoiceNum linked to the shipment.  */  
   "InvoiceNum":number,
   "KitBackFlush":boolean,
   "KitBinNum":string,
   "KitCompIssue":boolean,
   "KitCompShipComplete":boolean,
   "KitDescription":string,
      /**  Sales Kit flag.  C = 'Component'  P = 'Parent'.  */  
   "KitFlag":string,
   "KitIUM":string,
   "KitLotNum":string,
   "KitMassIssue":boolean,
   "KitParentIssue":boolean,
   "KitPartNum":string,
   "KitQtyFromInv":number,
   "KitQtyFromInvEnabled":boolean,
   "KitSerialTracked":boolean,
   "KitTrackLots":boolean,
   "KitWarehouse":string,
   "KitWarehouseCodeDesc":string,
   "KitWhseList":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.   This field comes directly from the table ShipHead.  */  
   "LegalNumber":string,
      /**  Individual line content value that is used by the freight web service to calculate the total order value.  */  
   "LineContentValue":number,
   "LineTax":number,
   "LinkMsg":string,
      /**  Contains the Mark For Address  */  
   "MarkForAddrList":string,
   "MFCustID":string,
      /**  Indicates if Order is on Hold  */  
   "OrderHold":boolean,
   "OrderRelOurReqQty":number,
   "OurJobShipIUM":string,
   "OurJobShippedQty":number,
   "OurRemainQty":number,
   "OurRemainUM":string,
   "OurReqQty":number,
   "OurReqUM":string,
   "OurShippedQty":number,
   "OurShippedUM":string,
   "OurStockShippedQty":number,
      /**  Packing slip for drop shipment.  */  
   "PackSlip":string,
      /**  Used by freight web service  */  
   "PartAESExp":string,
   "PartCompany":string,
      /**  Used by freight web service  */  
   "PartECNNumber":string,
      /**  Used by freight web service  */  
   "PartExpLicNumber":string,
      /**  Used by freight web service  */  
   "PartExpLicType":string,
      /**  Used by freight web service  */  
   "PartHazClass":string,
      /**  Used by freight web service  */  
   "PartHazGvrnmtID":string,
      /**  Used by freight web service  */  
   "PartHazItem":boolean,
      /**  Used by freight web service  */  
   "PartHazPackInstr":string,
      /**  Used by freight web service  */  
   "PartHazSub":string,
      /**  Used by freight web service  */  
   "PartHazTechName":string,
      /**  Used by freight web service  */  
   "PartHTS":string,
      /**  Used by freight web service  */  
   "PartNAFTAOrigCountry":string,
      /**  Used by freight web service  */  
   "PartNAFTAPref":string,
      /**  Used by freight web service  */  
   "PartNAFTAProd":string,
      /**  Used by freight web service  */  
   "PartOrigCountry":string,
   "PartPartNum":string,
      /**  Used by freight web service  */  
   "PartSchedBcode":string,
      /**  Used by freight web service  */  
   "PartUseHTSDesc":boolean,
   "PONum":string,
      /**  Project of the related Order Line  */  
   "ProjectID":string,
      /**  The supplier purchase point ID.  */  
   "PurPoint":string,
   "RequestDate":string,
   "Rpt1LineTax":number,
   "Rpt2LineTax":number,
   "Rpt3LineTax":number,
   "SelectedLocationIDQty":number,
   "SellingRemainQty":number,
   "SellingRemainUM":string,
   "SellingReqQty":number,
   "SellingReqUM":string,
   "SellingShipmentQty":number,
   "SellingShipmentUM":string,
   "SellingShippedQty":number,
   "SellingShippedUM":string,
      /**  The actual ship date for the packing slip. Default as system date.  This field comes directly from the ShipHead table.  */  
   "ShipDate":string,
   "ShipToWarning":string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  This field comes directly from the ShipHead table.  */  
   "ShipViaCode":string,
      /**  Indicates if Part is a stock Part  */  
   "StockPart":boolean,
   "TrackID":boolean,
   "TranLocationIDQty":number,
      /**  The supplier that drops shipped the good from their inventory to our customer.  */  
   "VendorNum":number,
   "WhseList":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "KitAttributeSetID":number,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  The Full Description of the Attribute Set.  */  
   "KitAttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "KitAttributeSetShortDescription":string,
   "KitPartAttrClassID":string,
   "EnableAttributeSetSearch":boolean,
      /**  Mark For address formatted for kinetic.  */  
   "MarkForAddrFormatted":string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   "DispInventoryNumberOfPieces":number,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   "DispJobNumberOfPieces":number,
   "KitRevisionNum":string,
   "CNDeclarationBill":string,
   "BitFlag":number,
   "BinNumDescription":string,
   "ContractCodeContractDescription":string,
   "CustNumSendToFSA":boolean,
   "CustNumName":string,
   "CustNumCustID":string,
   "CustNumBTName":string,
   "DimensionDimCodeDescription":string,
   "JobNumPartDescription":string,
   "LotPartLotDescription":string,
   "MFShipToNumInactive":boolean,
   "OrderLineProdCode":string,
   "OrderLineLineDesc":string,
   "OrderNumPSCurrCode":string,
   "OrderNumCardMemberName":string,
   "OrderNumCurrencyCode":string,
   "OTMFCountryDescription":string,
   "PackNumUseOTS":boolean,
   "PackNumShipStatus":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumAttrClassID":string,
   "PartNumSendToFSA":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumPricePerCode":string,
   "PartNumSellingFactor":number,
   "PartNumSalesUM":string,
   "PartNumIUM":string,
   "PartNumTrackLots":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumPartDescription":string,
   "PartNumWarrantyCode":string,
   "PartNumFSAEquipment":boolean,
   "PartNumTrackInventoryAttributes":boolean,
   "PlantName":string,
   "WarehouseCodeDescription":string,
   "WarrantyCodeSendToFSA":boolean,
   "WarrantyCodeWarrDescription":string,
   "WIPWarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
   "UD_SysRevID":string,
   "PCID2_c":string,
   "PCID3_c":string,
   "PCID4_c":string,
   "PCID5_c":string,
   "PCIDType1_c":string,
   "PCIDType2_c":string,
   "PCIDType3_c":string,
   "PCIDType4_c":string,
   "PCIDType5_c":string,
}

export interface Erp_Tablesets_ShipDtlTaxRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Packing slip number that this detail record is linked with.  */  
   "PackNum":number,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  */  
   "PackLine":number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  InvcDtl.TaxCode and InvcDtl/InvcMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount ((Qty*unitprice)-discount) or if this is for a InvcMisc record InvcMisc.Amount.  */  
   "ReportableAmt":number,
      /**  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  InvcDtl.TaxCode and InvcDtl/InvcMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount ((Qty*unitprice)-discount) or if this is for a InvcMisc record InvcMisc.Amount.  */  
   "DocReportableAmt":number,
      /**  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (invcdtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the InvcDt/InvcMisc.TaxCat and the InvcTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  */  
   "TaxableAmt":number,
      /**  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (invcdtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the InvcDt/InvcMisc.TaxCat and the InvcTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  */  
   "DocTaxableAmt":number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   "Percent":number,
      /**  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the InvcDtl.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the InvcDtl.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  */  
   "TaxAmt":number,
      /**  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the InvcDtl.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the InvcDtl.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  */  
   "DocTaxAmt":number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   "Manual":boolean,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Reverse Charge.  */  
   "ReverseCharge":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  Rate Code  */  
   "RateCode":string,
      /**  Collection Type  */  
   "CollectionType":number,
      /**  Timing of when to report taxes  */  
   "Timing":number,
      /**  Exemption Type  */  
   "ExemptType":number,
      /**  Exemption Percent  */  
   "ExemptPercent":number,
      /**  Resolution Number  */  
   "ResolutionNum":string,
      /**  Resolution Date  */  
   "ResolutionDate":string,
      /**  Tax Rate Date  */  
   "TaxRateDate":string,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   "DefTaxableAmt":number,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   "DocDefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DefTaxableAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   "DefTaxAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   "DocDefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DefTaxAmt":number,
      /**  This record was manually added (not in Liability) but will use the standard calculations  */  
   "ManAdd":boolean,
      /**  Deducatable Tax Amount  */  
   "DedTaxAmt":number,
      /**  Deducatable Tax Amount  */  
   "DocDedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DedTaxAmt":number,
      /**   Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  */  
   "ECAcquisitionSeq":number,
      /**  Fixed Tax Amount  */  
   "FixedAmount":number,
      /**  Document Fixed Tax Amount  */  
   "DocFixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1FixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2FixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3FixedAmount":number,
      /**  A flat discount amount for the tax.  */  
   "Discount":number,
      /**  A flat discount amount for the tax converted to the customers currency.  */  
   "DocDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Discount":number,
      /**  Unique Identifier for Legal Text  */  
   "TextCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
   "DescCollectionType":string,
   "TaxDescription":string,
   "TaxTotal":number,
   "DisplaySymbol":string,
   "DocDisplaySymbol":string,
      /**  The date and time that the record was last changed  */  
   "ChangeDateTime":string,
   "BitFlag":number,
   "RateCodeDescription":string,
   "SalesTaxDescDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ShipHeadAttchRow{
   "Company":string,
   "PackNum":number,
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

export interface Erp_Tablesets_ShipHeadInsuranceRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Packing Slip  */  
   "PackNum":number,
      /**  InsuranceSeq  */  
   "InsuranceSeq":number,
      /**  Insurance Type  */  
   "Type":string,
      /**  Insurance Company Name  */  
   "CompanyName":string,
      /**  Insurance Policy Number  */  
   "PolicyNum":string,
      /**  Insurance Premium  */  
   "Premium":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ShipHeadListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   "PackNum":number,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   "ShipDate":string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  */  
   "ShipViaCode":string,
      /**  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  */  
   "ShipPerson":string,
      /**  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  */  
   "EntryPerson":string,
      /**  An optional field which can be used to enter a shipping log reference #.  */  
   "ShipLog":string,
      /**  An optional field that will be printed on the shipping labels for this packing slip.  */  
   "LabelComment":string,
      /**  Packing slip comments.  This will print on the Packing Slip.  */  
   "ShipComment":string,
      /**  Used internally to indicate if the user has pulled this packing slip into invoice processing.  This does NOT ensure that the packing slip has been invoiced.  Only that it was functionally pulled into the invoice process.  This may also be set to "Yes" if the user does not want to use the shipments for generating invoices.  This is condition is indicated when ArSyst.SaveShipments = No.  Under this condition Shipping Entry would initialize "invoiced" to Yes, preventing invoice entry from pulling them in.  This feature would normally be used during the startup period when they do not yet have A/R fully implemented.  */  
   "Invoiced":boolean,
      /**  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   "ShipToNum":string,
      /**  Indicates if the Packing Slip is complete and ready for invoicing. The invoice entry "Get Shipments" function will only select where ShipHead.ReadyToInvoice = Yes  */  
   "ReadyToInvoice":boolean,
      /**  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  */  
   "CustNum":number,
      /**  The Site that shipment was made from.  */  
   "Plant":string,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   "TrackingNumber":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  A flag indicating if this is shipment voided.  This flag is updated via input from the user.  Once a shipment has been voided it can no longer be updated or invoiced.  */  
   "Voided":boolean,
      /**  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  */  
   "ExternalDeliveryNote":boolean,
      /**  External  ID  */  
   "ExternalID":string,
      /**  Iinter Company Received flag  */  
   "ICReceived":boolean,
      /**  Cross reference Packing Slip number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   "XRefPackNum":string,
      /**  Populated from OrderHed.BTCustNum.  */  
   "BTCustNum":number,
      /**  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  */  
   "BTConNum":number,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   "ShipStatus":string,
      /**  Group the shipment belongs to for "Staging"  */  
   "ShipGroup":string,
      /**  Package Code  */  
   "PkgCode":string,
      /**  NMFC Packaging Classification code.  */  
   "PkgClass":string,
      /**  Package Weight  */  
   "Weight":number,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  Is a Saturday delivery acceptable  */  
   "SatDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
      /**  Verbal Confirmation required  */  
   "VerbalConf":boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   "Hazmat":boolean,
      /**  Documents Only delivery  */  
   "DocOnly":boolean,
      /**  Reference Notes for the delivery  */  
   "RefNotes":string,
      /**  Apply Handling Charge to shipment  */  
   "ApplyChrg":boolean,
      /**  Handling Charge Amount  */  
   "ChrgAmount":number,
      /**  Prefer COD delivery  */  
   "COD":boolean,
      /**  Add Freight COD Amount owed  */  
   "CODFreight":boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   "CODCheck":boolean,
      /**  Amount due on Cashier's check or money order  */  
   "CODAmount":number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   "GroundType":string,
      /**  Indicates whether to send an email notification of delivery  */  
   "NotifyFlag":boolean,
      /**  The list of email address to notify about a delivery  */  
   "NotifyEMail":string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   "DeclaredIns":boolean,
      /**  Declared Insurance Amount  */  
   "DeclaredAmt":number,
      /**  Transaction Number returned by the Manifest Engine  */  
   "MFTransNum":string,
      /**  Manifest Call Tag Number  */  
   "MFCallTag":string,
      /**  Manifest Pickup Number  */  
   "MFPickupNum":string,
      /**  Manifest Discount Freight Amount  */  
   "MFDiscFreight":number,
      /**  Manifest Template Code  */  
   "MFTemplate":string,
      /**  Manifest flag to use 3 party billing  */  
   "MFUse3B":boolean,
      /**  Manifest's 3rd Party Billing Account  */  
   "MF3BAccount":string,
      /**  Manifest Dimension Weight  */  
   "MFDimWeight":number,
      /**  Manifest Delivery Zone  */  
   "MFZone":string,
      /**  Manifest Published Freight Amount  */  
   "MFFreightAmt":number,
      /**  Manifest Other Amount  */  
   "MFOtherAmt":number,
      /**  Manifest Oversized flag  */  
   "MFOversized":boolean,
      /**  Is a Service Saturday delivery acceptable  */  
   "ServSatDelivery":boolean,
      /**  Is a Service Saturday pickup available  */  
   "ServSatPickup":boolean,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
      /**  Service Auto POD flag  */  
   "ServPOD":boolean,
      /**  AOD  */  
   "ServAOD":boolean,
      /**  Service Home Delivery allowed  */  
   "ServHomeDel":boolean,
      /**  Service Home Delivery Type Code  */  
   "DeliveryType":string,
      /**  Service Home Delivery date  */  
   "ServDeliveryDate":string,
      /**  Home delivery phone number  */  
   "ServPhone":string,
      /**  Service Delivery Instructions  */  
   "ServInstruct":string,
      /**  Service Signature release is on file  */  
   "ServRelease":boolean,
      /**  Service Signature Release authorization number  */  
   "ServAuthNum":string,
      /**  Service Reference 1  */  
   "ServRef1":string,
      /**  Service Reference 2  */  
   "ServRef2":string,
      /**  Service Reference 3  */  
   "ServRef3":string,
      /**  Service Reference 4  */  
   "ServRef4":string,
      /**  Service Reference 5  */  
   "ServRef5":string,
      /**  Bill of Lading Number the packing slip is linked to  */  
   "BOLNum":number,
      /**  Bill of Lading line number linked to  */  
   "BOLLine":number,
      /**  Added for international shipping, Is a commercial invoice required  */  
   "CommercialInvoice":boolean,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   "ShipExprtDeclartn":boolean,
      /**  For International shipping.  Certificate of Orgin required.  */  
   "CertOfOrigin":boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   "LetterOfInstr":boolean,
      /**  International Shipping - HazardousShipment  */  
   "HazardousShipment":boolean,
      /**  Is this an International shipment  */  
   "IntrntlShip":boolean,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   "PayFlag":string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   "PayAccount":string,
      /**  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  */  
   "PayBTAddress1":string,
      /**  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  */  
   "PayBTAddress2":string,
      /**  Shipping, The city portion of the Payer main address.  */  
   "PayBTCity":string,
      /**  The state or province portion of the shipment payer main address.  */  
   "PayBTState":string,
      /**  The zip or postal code portion of the shipping payers main address.  */  
   "PayBTZip":string,
      /**  The country of the main shipping payers address.  */  
   "PayBTCountry":string,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   "FFAddress1":string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   "FFAddress2":string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   "FFCity":string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   "FFState":string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   "FFZip":string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   "FFCountry":string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   "FFContact":string,
      /**  International Shipping. Frieght Forwarder company name  */  
   "FFCompName":string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   "FFPhoneNum":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  International Shipping. Frieght Forwarder ID  */  
   "FFID":string,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   "IndividualPackIDs":boolean,
      /**  Freight Forwarder Country portion of the address  */  
   "FFAddress3":string,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   "DeliveryConf":number,
      /**  Additional Handling flag  */  
   "AddlHdlgFlag":boolean,
      /**  Non Standard Packaging  */  
   "NonStdPkg":boolean,
      /**  Freight Forwarder Country portion of the address  */  
   "FFCountryNum":number,
      /**  Payer Bill To Third Address line  */  
   "PayBTAddress3":string,
      /**  Payer Bill To Country Number  */  
   "PayBTCountryNum":number,
      /**  Payer Bill To Phone Number  */  
   "PayBTPhone":string,
      /**  Way Bill Number  */  
   "WayBillNbr":string,
      /**  This is the ship via code the freighting system selected for shipping.  */  
   "FreightedShipViaCode":string,
      /**  UPS Quantum View  */  
   "UPSQuantumView":boolean,
      /**  UPS Quantum View From Name  */  
   "UPSQVShipFromName":string,
      /**  UPS Quantum View Memo  */  
   "UPSQVMemo":string,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   "PkgLength":number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   "PkgWidth":number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   "PkgHeight":number,
      /**  Defines if this document is marked as EDI Ready  */  
   "EDIReady":boolean,
      /**  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  */  
   "PhantomPack":boolean,
      /**  Pack ID of the pack this pack was replicated from.  This is used as a debugging tool and is not presented to the end user.  */  
   "ReplicatedFrom":number,
      /**  Informational field containing either Complete or Partial.  This is only popluated if the ReplicatedFrom field has a value.  This is used as a debugging tool and is not presented to the user.  */  
   "ReplicatedStat":string,
      /**   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   "PkgSizeUOM":string,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   "WeightUOM":string,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   "UseOTS":boolean,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Indicates if the document has been printed.  */  
   "DocumentPrinted":boolean,
      /**  The Sales Order number which contains the One Time ShipTo data. The OTSOrderNum along with the values ShipToNum are used to find the OrderHed or OrderRel to obtain the OTS.  */  
   "OTSOrderNum":number,
      /**  Indicates whether or not the taxes for this shipment have been calculated.  This field is used to identify those situations where the tax engine was called but did not generate any taxes because none were needed.  */  
   "TaxCalculated":boolean,
      /**  Date the taxes were calculated.  Used for informational and audit tracking purposes.  */  
   "TaxCalcDate":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   "Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Rounding":number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   "DocRounding":number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt1TotalTax":number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt2TotalTax":number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt3TotalTax":number,
      /**  Total order Amount. This field is an accumulation of the extended net amounts of the detail line items  */  
   "OrderAmt":number,
      /**  Total order Amount in customer currency. This field is an accumulation of the extended net amounts of the detail line items and rounded according to the Doc currency Round rule  */  
   "DocOrderAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1OrderAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2OrderAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3OrderAmt":number,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   "TaxRegionCode":string,
      /**   Order Total Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "TotalWHTax":number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "DocTotalWHTax":number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt1TotalWHTax":number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt2TotalWHTax":number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt3TotalWHTax":number,
      /**   Order Total Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "TotalSATax":number,
      /**   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "DocTotalSATax":number,
      /**   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt1TotalSATax":number,
      /**   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt2TotalSATax":number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt3TotalSATax":number,
      /**   Order Total Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "TotalTax":number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "DocTotalTax":number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "TotalDiscount":number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "Rpt1TotalDiscount":number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "Rpt2TotalDiscount":number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "Rpt3TotalDiscount":number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "DocTotalDiscount":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  */  
   "DeviceUOM":string,
      /**  Unit of Measure the Manifest system expects the pack sizet to be measured in.  */  
   "ManifestSizeUOM":string,
      /**  Unit of Measure of the Manifest system expects the pack to be weighed in.  */  
   "ManifestWtUOM":string,
      /**  Package Weight in the Manifest System's unit of measure.  */  
   "ManifestWeight":number,
      /**  The pack length in the Manifest Unit of Measure.  */  
   "ManifestLength":number,
      /**  The pack width in the manifest unit of measure.  */  
   "ManifestWidth":number,
      /**  The pack height in the manifest unit of measure.  */  
   "ManifestHeight":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Indicates that the tax is included in the unit price  */  
   "InPrice":boolean,
      /**  Flag to indicate that project billing Hold Product Invoice flag is true, it prevents this pack slip from being selected for invoicing.  */  
   "PBHoldNoInv":boolean,
      /**  Reconciled quantity for the packing slip  */  
   "ReconcileQty":number,
      /**  Last trading partner demand schedule processed that affected this packing slip  */  
   "ScheduleNumber":string,
      /**  Number of times the customer shipment has been shipped, that means it changed from non shipped status to shipped  */  
   "CounterASN":number,
      /**  Bank for Cash Receipts. Default is from 1) Sales Order 2)Bill To Customer 3) System Default(Company).  */  
   "OurBank":string,
      /**  It will be used to identify that the shipment will generate an invoice when it got shipped. If the first order release added to a pack belongs to an ERS order, then non ERS order releases will not be allowed in that pack and if the first order release added to a pack belongs to a non ERS order, then ERS order releases will not be allowed in that pack.  */  
   "ERSOrder":boolean,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "OrderDate":string,
      /**  Comma delimited list of status types for lookup  */  
   "SlipStatus":string,
      /**  Shipping Address  */  
   "AddrList":string,
      /**  Billing Address  */  
   "BillAddr":string,
      /**  Indicates if Customer is on Credit Hold  */  
   "CreditHold":boolean,
      /**  Indicates if Order is on Hold  */  
   "OrderHold":boolean,
      /**  Flag indicating OrderRel's going to more than one shipTo  */  
   "MultipleShippers":boolean,
      /**  Indicates whether to hide/view ExternalDeliveryNote field  */  
   "SendShipment":boolean,
      /**  CustID associated with ShipHeadHead.BTCustNum.  */  
   "BTCustID":string,
      /**  CustName associated with ShipHead.BTCustNum.  */  
   "BTCustomerName":string,
      /**  Used by the manifest system.  Sum of the value of items in the carton.  Item price - discount + sales tax.  */  
   "CartonContentValue":number,
      /**  Set to Y if the carton is the last one being shiped to the customer.  If the sum of the quantity packed does not equal the quantity ordered for each line in the carton the value is No.  */  
   "LastCartonFlag":boolean,
      /**  Carton Stage Number.  */  
   "CartonStageNbr":string,
   "EnableShipped":boolean,
      /**  Order Number for new cartons.  */  
   "OrderNum":number,
      /**  Indicates whether the Carton has lines or not.  */  
   "HasCartonLines":boolean,
      /**  Displays the contents of XaSyst.StagingReq  */  
   "StagingReq":boolean,
      /**  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  */  
   "EnableWeight":boolean,
      /**  Indicates if the manifest interface is enabled.  */  
   "ManifestFlag":boolean,
      /**  A zero indicates the Packing height is to be enabled.  */  
   "PkgHeightEnable":number,
      /**  Indicates if package length is to be enabled.  If the value is zero the prompt is enabled.  */  
   "PkgLenEnable":number,
      /**  A zero indicates the packaging width field is to be enabled.  */  
   "PkgWidthEnable":number,
      /**  Used to enable users to default the Carton Trk Dtl package settings.  Initial value defaults to the ShipHead.PkgCode.  However, this field does NOT have to be the same as the ShipHead.PkgCode.  */  
   "CtnPkgCode":string,
      /**  Number of packs to replicate  */  
   "ReplicateCount":number,
      /**  Logical indicating if CartonTrkDtl records exist for this pack.  Used by the UI for row rules.  */  
   "PhantomCasesExist":boolean,
      /**  Logical indicating if the PhantomPack checkbox is to be enabled.  */  
   "EnablePhantom":boolean,
      /**  Pack ID of the Masterpack this shipment is on.  */  
   "MasterpackPackNum":number,
   "PkgSizeUOMEnable":number,
   "ShipToNumName":string,
      /**  Indicates if changes can occur after the document has been printed  */  
   "AllowChgAfterPrint":boolean,
      /**  Indicates if assign legal number option is available.  */  
   "EnableAssignLegNum":boolean,
      /**  Indicates if the void legal number option is available  */  
   "EnableVoidLegNum":boolean,
      /**  Indicates if a legal number configuration exists for customer shipments  */  
   "HasLegNumCnfg":boolean,
      /**  Document Total tax amount from ShipDtl Tax for Collection type 'Invoice'  */  
   "DocTaxAmt":number,
   "DocWithholdingTaxAmt":number,
      /**  Intended for internal UI use.  Identifies whether or not taxes are generated for shipdtls.  */  
   "EnableTax":boolean,
   "TaxAmt":number,
   "Rpt1TaxAmt":number,
   "Rpt2TaxAmt":number,
   "Rpt3TaxAmt":number,
      /**  Indicates if TranDocTypeID is available for input.  */  
   "EnableTranDocType":boolean,
      /**  The flag to indicate if Tax Inclusive Pricing should be on display  */  
   "DisplayInPrice":boolean,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCodeCurrName":string,
      /**  Description of the currency  */  
   "CurrencyCodeCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCodeCurrSymbol":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCodeCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyCodeDocumentDesc":string,
      /**  The full name of the customer.  */  
   "CustomerName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustomerBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustomerCustID":string,
      /**  Description of delivery type  */  
   "DeliveryTypeDescription":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "FreightedShipViaCodeWebDesc":string,
      /**  Full description for the shipping company (carrier).  */  
   "FreightedShipViaCodeDescription":string,
      /**  Full description of the bank account.  */  
   "OurBankDescription":string,
      /**  The Bank's full name.  */  
   "OurBankBankName":string,
      /**  Master pack packnum  */  
   "PackToMasterpackDtlPackNum":number,
      /**  The full name of the customer.  */  
   "ShipToCustName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "ShipToCustBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "ShipToCustCustID":string,
      /**  Full description for the shipping company (carrier).  */  
   "ShipViaCodeDescription":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "ShipViaCodeWebDesc":string,
      /**  Full description for the Tax Region.  */  
   "TaxRegionDescription":string,
      /**  Description  */  
   "TranDocTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ShipHeadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   "PackNum":number,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   "ShipDate":string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  */  
   "ShipViaCode":string,
      /**  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  */  
   "ShipPerson":string,
      /**  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  */  
   "EntryPerson":string,
      /**  An optional field which can be used to enter a shipping log reference #.  */  
   "ShipLog":string,
      /**  An optional field that will be printed on the shipping labels for this packing slip.  */  
   "LabelComment":string,
      /**  Packing slip comments.  This will print on the Packing Slip.  */  
   "ShipComment":string,
      /**  Used internally to indicate if the user has pulled this packing slip into invoice processing.  This does NOT ensure that the packing slip has been invoiced.  Only that it was functionally pulled into the invoice process.  This may also be set to "Yes" if the user does not want to use the shipments for generating invoices.  This is condition is indicated when ArSyst.SaveShipments = No.  Under this condition Shipping Entry would initialize "invoiced" to Yes, preventing invoice entry from pulling them in.  This feature would normally be used during the startup period when they do not yet have A/R fully implemented.  */  
   "Invoiced":boolean,
      /**  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   "ShipToNum":string,
      /**  Indicates if the Packing Slip is complete and ready for invoicing. The invoice entry "Get Shipments" function will only select where ShipHead.ReadyToInvoice = Yes  */  
   "ReadyToInvoice":boolean,
      /**  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  */  
   "CustNum":number,
      /**  The Site that shipment was made from.  */  
   "Plant":string,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   "TrackingNumber":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  A flag indicating if this is shipment voided.  This flag is updated via input from the user.  Once a shipment has been voided it can no longer be updated or invoiced.  */  
   "Voided":boolean,
      /**  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  */  
   "ExternalDeliveryNote":boolean,
      /**  External  ID  */  
   "ExternalID":string,
      /**  Iinter Company Received flag  */  
   "ICReceived":boolean,
      /**  Cross reference Packing Slip number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   "XRefPackNum":string,
      /**  Populated from OrderHed.BTCustNum.  */  
   "BTCustNum":number,
      /**  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  */  
   "BTConNum":number,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   "ShipStatus":string,
      /**  Group the shipment belongs to for "Staging"  */  
   "ShipGroup":string,
      /**  Package Code  */  
   "PkgCode":string,
      /**  NMFC Packaging Classification code.  */  
   "PkgClass":string,
      /**  Package Weight  */  
   "Weight":number,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  Is a Saturday delivery acceptable  */  
   "SatDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
      /**  Verbal Confirmation required  */  
   "VerbalConf":boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   "Hazmat":boolean,
      /**  Documents Only delivery  */  
   "DocOnly":boolean,
      /**  Reference Notes for the delivery  */  
   "RefNotes":string,
      /**  Apply Handling Charge to shipment  */  
   "ApplyChrg":boolean,
      /**  Handling Charge Amount  */  
   "ChrgAmount":number,
      /**  Prefer COD delivery  */  
   "COD":boolean,
      /**  Add Freight COD Amount owed  */  
   "CODFreight":boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   "CODCheck":boolean,
      /**  Amount due on Cashier's check or money order  */  
   "CODAmount":number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   "GroundType":string,
      /**  Indicates whether to send an email notification of delivery  */  
   "NotifyFlag":boolean,
      /**  The list of email address to notify about a delivery  */  
   "NotifyEMail":string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   "DeclaredIns":boolean,
      /**  Declared Insurance Amount  */  
   "DeclaredAmt":number,
      /**  Transaction Number returned by the Manifest Engine  */  
   "MFTransNum":string,
      /**  Manifest Call Tag Number  */  
   "MFCallTag":string,
      /**  Manifest Pickup Number  */  
   "MFPickupNum":string,
      /**  Manifest Discount Freight Amount  */  
   "MFDiscFreight":number,
      /**  Manifest Template Code  */  
   "MFTemplate":string,
      /**  Manifest flag to use 3 party billing  */  
   "MFUse3B":boolean,
      /**  Manifest's 3rd Party Billing Account  */  
   "MF3BAccount":string,
      /**  Manifest Dimension Weight  */  
   "MFDimWeight":number,
      /**  Manifest Delivery Zone  */  
   "MFZone":string,
      /**  Manifest Published Freight Amount  */  
   "MFFreightAmt":number,
      /**  Manifest Other Amount  */  
   "MFOtherAmt":number,
      /**  Manifest Oversized flag  */  
   "MFOversized":boolean,
      /**  Is a Service Saturday delivery acceptable  */  
   "ServSatDelivery":boolean,
      /**  Is a Service Saturday pickup available  */  
   "ServSatPickup":boolean,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
      /**  Service Auto POD flag  */  
   "ServPOD":boolean,
      /**  AOD  */  
   "ServAOD":boolean,
      /**  Service Home Delivery allowed  */  
   "ServHomeDel":boolean,
      /**  Service Home Delivery Type Code  */  
   "DeliveryType":string,
      /**  Service Home Delivery date  */  
   "ServDeliveryDate":string,
      /**  Home delivery phone number  */  
   "ServPhone":string,
      /**  Service Delivery Instructions  */  
   "ServInstruct":string,
      /**  Service Signature release is on file  */  
   "ServRelease":boolean,
      /**  Service Signature Release authorization number  */  
   "ServAuthNum":string,
      /**  Service Reference 1  */  
   "ServRef1":string,
      /**  Service Reference 2  */  
   "ServRef2":string,
      /**  Service Reference 3  */  
   "ServRef3":string,
      /**  Service Reference 4  */  
   "ServRef4":string,
      /**  Service Reference 5  */  
   "ServRef5":string,
      /**  Bill of Lading Number the packing slip is linked to  */  
   "BOLNum":number,
      /**  Bill of Lading line number linked to  */  
   "BOLLine":number,
      /**  Added for international shipping, Is a commercial invoice required  */  
   "CommercialInvoice":boolean,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   "ShipExprtDeclartn":boolean,
      /**  For International shipping.  Certificate of Orgin required.  */  
   "CertOfOrigin":boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   "LetterOfInstr":boolean,
      /**  International Shipping - HazardousShipment  */  
   "HazardousShipment":boolean,
      /**  Is this an International shipment  */  
   "IntrntlShip":boolean,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   "PayFlag":string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   "PayAccount":string,
      /**  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  */  
   "PayBTAddress1":string,
      /**  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  */  
   "PayBTAddress2":string,
      /**  Shipping, The city portion of the Payer main address.  */  
   "PayBTCity":string,
      /**  The state or province portion of the shipment payer main address.  */  
   "PayBTState":string,
      /**  The zip or postal code portion of the shipping payers main address.  */  
   "PayBTZip":string,
      /**  The country of the main shipping payers address.  */  
   "PayBTCountry":string,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   "FFAddress1":string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   "FFAddress2":string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   "FFCity":string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   "FFState":string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   "FFZip":string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   "FFCountry":string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   "FFContact":string,
      /**  International Shipping. Frieght Forwarder company name  */  
   "FFCompName":string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   "FFPhoneNum":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  International Shipping. Frieght Forwarder ID  */  
   "FFID":string,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   "IndividualPackIDs":boolean,
      /**  Freight Forwarder Country portion of the address  */  
   "FFAddress3":string,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   "DeliveryConf":number,
      /**  Additional Handling flag  */  
   "AddlHdlgFlag":boolean,
      /**  Non Standard Packaging  */  
   "NonStdPkg":boolean,
      /**  Freight Forwarder Country portion of the address  */  
   "FFCountryNum":number,
      /**  Payer Bill To Third Address line  */  
   "PayBTAddress3":string,
      /**  Payer Bill To Country Number  */  
   "PayBTCountryNum":number,
      /**  Payer Bill To Phone Number  */  
   "PayBTPhone":string,
      /**  Way Bill Number  */  
   "WayBillNbr":string,
      /**  This is the ship via code the freighting system selected for shipping.  */  
   "FreightedShipViaCode":string,
      /**  UPS Quantum View  */  
   "UPSQuantumView":boolean,
      /**  UPS Quantum View From Name  */  
   "UPSQVShipFromName":string,
      /**  UPS Quantum View Memo  */  
   "UPSQVMemo":string,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   "PkgLength":number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   "PkgWidth":number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   "PkgHeight":number,
      /**  Defines if this document is marked as EDI Ready  */  
   "EDIReady":boolean,
      /**  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  */  
   "PhantomPack":boolean,
      /**  Pack ID of the pack this pack was replicated from.  This is used as a debugging tool and is not presented to the end user.  */  
   "ReplicatedFrom":number,
      /**  Informational field containing either Complete or Partial.  This is only popluated if the ReplicatedFrom field has a value.  This is used as a debugging tool and is not presented to the user.  */  
   "ReplicatedStat":string,
      /**   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   "PkgSizeUOM":string,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   "WeightUOM":string,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   "UseOTS":boolean,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Indicates if the document has been printed.  */  
   "DocumentPrinted":boolean,
      /**  The Sales Order number which contains the One Time ShipTo data. The OTSOrderNum along with the values ShipToNum are used to find the OrderHed or OrderRel to obtain the OTS.  */  
   "OTSOrderNum":number,
      /**  Indicates whether or not the taxes for this shipment have been calculated.  This field is used to identify those situations where the tax engine was called but did not generate any taxes because none were needed.  */  
   "TaxCalculated":boolean,
      /**  Date the taxes were calculated.  Used for informational and audit tracking purposes.  */  
   "TaxCalcDate":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   "Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Rounding":number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   "DocRounding":number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt1TotalTax":number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt2TotalTax":number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt3TotalTax":number,
      /**  Total order Amount. This field is an accumulation of the extended net amounts of the detail line items  */  
   "OrderAmt":number,
      /**  Total order Amount in customer currency. This field is an accumulation of the extended net amounts of the detail line items and rounded according to the Doc currency Round rule  */  
   "DocOrderAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1OrderAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2OrderAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3OrderAmt":number,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   "TaxRegionCode":string,
      /**   Order Total Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "TotalWHTax":number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "DocTotalWHTax":number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt1TotalWHTax":number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt2TotalWHTax":number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt3TotalWHTax":number,
      /**   Order Total Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "TotalSATax":number,
      /**   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "DocTotalSATax":number,
      /**   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt1TotalSATax":number,
      /**   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt2TotalSATax":number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt3TotalSATax":number,
      /**   Order Total Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "TotalTax":number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "DocTotalTax":number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "TotalDiscount":number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "Rpt1TotalDiscount":number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "Rpt2TotalDiscount":number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "Rpt3TotalDiscount":number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "DocTotalDiscount":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  */  
   "DeviceUOM":string,
      /**  Unit of Measure the Manifest system expects the pack sizet to be measured in.  */  
   "ManifestSizeUOM":string,
      /**  Unit of Measure of the Manifest system expects the pack to be weighed in.  */  
   "ManifestWtUOM":string,
      /**  Package Weight in the Manifest System's unit of measure.  */  
   "ManifestWeight":number,
      /**  The pack length in the Manifest Unit of Measure.  */  
   "ManifestLength":number,
      /**  The pack width in the manifest unit of measure.  */  
   "ManifestWidth":number,
      /**  The pack height in the manifest unit of measure.  */  
   "ManifestHeight":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Indicates that the tax is included in the unit price  */  
   "InPrice":boolean,
      /**  Flag to indicate that project billing Hold Product Invoice flag is true, it prevents this pack slip from being selected for invoicing.  */  
   "PBHoldNoInv":boolean,
      /**  Reconciled quantity for the packing slip  */  
   "ReconcileQty":number,
      /**  Last trading partner demand schedule processed that affected this packing slip  */  
   "ScheduleNumber":string,
      /**  Number of times the customer shipment has been shipped, that means it changed from non shipped status to shipped  */  
   "CounterASN":number,
      /**  Bank for Cash Receipts. Default is from 1) Sales Order 2)Bill To Customer 3) System Default(Company).  */  
   "OurBank":string,
      /**  It will be used to identify that the shipment will generate an invoice when it got shipped. If the first order release added to a pack belongs to an ERS order, then non ERS order releases will not be allowed in that pack and if the first order release added to a pack belongs to a non ERS order, then ERS order releases will not be allowed in that pack.  */  
   "ERSOrder":boolean,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**  ShipOvers  */  
   "ShipOvers":boolean,
      /**  WIPackSlipCreated  */  
   "WIPackSlipCreated":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AGAuthorizationCode  */  
   "AGAuthorizationCode":string,
      /**  AGAuthorizationDate  */  
   "AGAuthorizationDate":string,
      /**  AGCarrierCUIT  */  
   "AGCarrierCUIT":string,
      /**  AGCOTMark  */  
   "AGCOTMark":boolean,
      /**  AGDocumentLetter  */  
   "AGDocumentLetter":string,
      /**  AGInvoicingPoint  */  
   "AGInvoicingPoint":string,
      /**  AGLegalNumber  */  
   "AGLegalNumber":string,
      /**  AGPrintingControlType  */  
   "AGPrintingControlType":string,
      /**  AGTrackLicense  */  
   "AGTrackLicense":string,
      /**  DispatchReason  */  
   "DispatchReason":string,
      /**  AGShippingWay  */  
   "AGShippingWay":string,
      /**  Our Supplier Code  */  
   "OurSupplierCode":string,
      /**  ASNPrintedDate  */  
   "ASNPrintedDate":string,
      /**  EDIShipToNum  */  
   "EDIShipToNum":string,
      /**  MXIncoterm  */  
   "MXIncoterm":string,
      /**  CreatedOn  */  
   "CreatedOn":string,
      /**  DigitalSignature  */  
   "DigitalSignature":string,
      /**  SignedOn  */  
   "SignedOn":string,
      /**  SignedBy  */  
   "SignedBy":string,
      /**  FirstPrintDate  */  
   "FirstPrintDate":string,
      /**  DocCopyNum  */  
   "DocCopyNum":number,
      /**  Declaration Bill  */  
   "CNDeclarationBill":string,
      /**  Sample  */  
   "CNSample":boolean,
      /**  Bonded  */  
   "CNBonded":boolean,
      /**  Creation date and time  */  
   "MXCertifiedTimestamp":string,
      /**  Certificate Serial Number  */  
   "MXCertificateSN":string,
      /**  Certificate  */  
   "MXCertificate":string,
      /**  Fiscal Folio (UUID)  */  
   "MXFiscalFolio":string,
      /**  SAT Certificate Serial Number  */  
   "MXSATCertificateSN":string,
      /**  Digital Seal  */  
   "MXDigitalSeal":string,
      /**  SAT Seal  */  
   "MXSATSeal":string,
      /**  Original String  */  
   "MXOriginalString":string,
      /**  TFD Original String  */  
   "MXOriginalStringTFD":string,
      /**  Serie  */  
   "MXSerie":string,
      /**  Folio  */  
   "MXFolio":string,
      /**  Estimated Date and Time of Departure  */  
   "MXETD":string,
      /**  Estimated Date and Time of Arrival  */  
   "MXETA":string,
      /**  Distance in Km  */  
   "MXDistance":number,
      /**  Permit Type  */  
   "MXPermitType":string,
      /**  Permit Number  */  
   "MXPermitNum":string,
      /**  Carta Porte Status  */  
   "MXCartaPorteStatus":string,
      /**  Vehicle License Plate  */  
   "VehicleLicensePlate":string,
      /**  Vehicle Type  */  
   "VehicleType":string,
      /**  Vehicle Year  */  
   "VehicleYear":number,
      /**  Driver  */  
   "DriverID":string,
      /**  MXCancelFiscalFolio  */  
   "MXCancelFiscalFolio":string,
      /**  Incoterm Code  */  
   "IncotermCode":string,
      /**  Incoterm Location  */  
   "IncotermLocation":string,
      /**  Shipping Address  */  
   "AddrList":string,
      /**  Indicates if changes can occur after the document has been printed  */  
   "AllowChgAfterPrint":boolean,
      /**  Billing Address  */  
   "BillAddr":string,
      /**  CustID associated with ShipHeadHead.BTCustNum.  */  
   "BTCustID":string,
      /**  CustName associated with ShipHead.BTCustNum.  */  
   "BTCustomerName":string,
      /**  Used by the manifest system.  Sum of the value of items in the carton.  Item price - discount + sales tax.  */  
   "CartonContentValue":number,
      /**  Carton Stage Number.  */  
   "CartonStageNbr":string,
      /**  The date and time that the record was last changed  */  
   "ChangeDateTime":string,
      /**  Internal field for temporary storage of check order messages.  */  
   "CheckOrderMessage":string,
      /**  This field temporarily holds certain message(s) returned by credit card processing logic for internal processing.  */  
   "CreditCardMessage":string,
      /**  Indicates if Customer is on Credit Hold  */  
   "CreditHold":boolean,
      /**  Used to enable users to default the Carton Trk Dtl package settings.  Initial value defaults to the ShipHead.PkgCode.  However, this field does NOT have to be the same as the ShipHead.PkgCode.  */  
   "CtnPkgCode":string,
      /**  The flag to indicate if Tax Inclusive Pricing should be on display  */  
   "DisplayInPrice":boolean,
      /**  Document Total tax amount from ShipDtl Tax for Collection type 'Invoice'  */  
   "DocTaxAmt":number,
   "DocWithholdingTaxAmt":number,
      /**  Internal flag to indicate if post update processing should be done.  */  
   "DoPostUpdate":boolean,
   "DspDigitalSignature":string,
      /**  Indicates if assign legal number option is available.  */  
   "EnableAssignLegNum":boolean,
      /**  Logical indicating if the package control functionality should be enabled.  */  
   "EnablePackageControl":boolean,
      /**  Logical indicating if the PhantomPack checkbox is to be enabled.  */  
   "EnablePhantom":boolean,
   "EnableShipped":boolean,
      /**  Intended for internal UI use.  Identifies whether or not taxes are generated for shipdtls.  */  
   "EnableTax":boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   "EnableTranDocType":boolean,
      /**  Indicates if the void legal number option is available  */  
   "EnableVoidLegNum":boolean,
      /**  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  */  
   "EnableWeight":boolean,
      /**  True if the update is being called from Master Pack (needed for validation)  */  
   "FromMasterPack":boolean,
      /**  Indicates whether the Carton has lines or not.  */  
   "HasCartonLines":boolean,
      /**  Indicates if a legal number configuration exists for customer shipments  */  
   "HasLegNumCnfg":boolean,
      /**  Set to Y if the carton is the last one being shiped to the customer.  If the sum of the quantity packed does not equal the quantity ordered for each line in the carton the value is No.  */  
   "LastCartonFlag":boolean,
   "LegalNumberMessage":string,
      /**  Indicates if the manifest interface is enabled.  */  
   "ManifestFlag":boolean,
      /**  Pack ID of the Masterpack this shipment is on.  */  
   "MasterpackPackNum":number,
      /**  Flag indicating OrderRel's going to more than one shipTo  */  
   "MultipleShippers":boolean,
   "OrderDate":string,
      /**  Indicates if Order is on Hold  */  
   "OrderHold":boolean,
      /**  Order Number for new cartons.  */  
   "OrderNum":number,
   "PCID":string,
      /**  Logical indicating if CartonTrkDtl records exist for this pack.  Used by the UI for row rules.  */  
   "PhantomCasesExist":boolean,
      /**  A zero indicates the Packing height is to be enabled.  */  
   "PkgHeightEnable":number,
      /**  Indicates if package length is to be enabled.  If the value is zero the prompt is enabled.  */  
   "PkgLenEnable":number,
   "PkgSizeUOMEnable":number,
      /**  A zero indicates the packaging width field is to be enabled.  */  
   "PkgWidthEnable":number,
      /**  Internal field for temporary storage of post update messages.  */  
   "PostUpdMessage":string,
   "QSUseBOL":boolean,
   "QSUseCO":boolean,
   "QSUseIntl":boolean,
      /**  Internal field for update processing that is true if ReadyToInvoice has been changed.  */  
   "ReadyToInvoiceChanged":boolean,
      /**  Number of packs to replicate  */  
   "ReplicateCount":number,
   "Rpt1TaxAmt":number,
   "Rpt2TaxAmt":number,
   "Rpt3TaxAmt":number,
      /**  Indicates whether to hide/view ExternalDeliveryNote field  */  
   "SendShipment":boolean,
   "ShipToNumName":string,
      /**  Comma delimited list of status types for lookup  */  
   "SlipStatus":string,
      /**  Carton Stage Ship Status  */  
   "StageShipped":boolean,
      /**  Displays the contents of XaSyst.StagingReq  */  
   "StagingReq":boolean,
      /**  Internal field for temporary storage of status change messages.  */  
   "StatusChgMessage":string,
   "TaxAmt":number,
      /**  Internal field for temporary storage of auto invoicing messages.  */  
   "AutoInvoiceMessage":string,
      /**  Ship To address formatted for Kinetic.  */  
   "ShipToAddressFormatted":string,
      /**  Sold To address formatted  */  
   "SoldToAddressFormatted":string,
      /**  Estimated Date of Arrival  */  
   "MXETADate":string,
      /**  Estimated Time of Arrival  */  
   "MXETATime":number,
      /**  Estimated Date of Departure  */  
   "MXETDDate":string,
      /**  Estimated Time of Departure  */  
   "MXETDTime":number,
      /**  Flag indicating whether to enable Incoterm Location  */  
   "EnableIncotermLocation":boolean,
      /**  Vehicle Weight (in tons)  */  
   "MXVehicleWeight":number,
      /**  A unique Carta Porte identification number assigned by Epicor  */  
   "MXIdCCP":string,
      /**  Customs Regime for Export transaction  */  
   "MXCustomsRegime":string,
      /**  Check box to specify the use of reverse logistic, collection or devolution services when shipping goods.  */  
   "MXReverseLogistics":boolean,
   "BitFlag":number,
   "AGInvoicingPointDescription":string,
   "BTCustNumInactive":boolean,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrName":string,
   "CustomerSendToFSA":boolean,
   "CustomerInactive":boolean,
   "CustomerBTName":string,
   "CustomerCustID":string,
   "CustomerName":string,
   "DeliveryTypeDescription":string,
   "FreightedShipViaCodeDescription":string,
   "FreightedShipViaCodeWebDesc":string,
   "IncotermsDescription":string,
   "OurBankBankName":string,
   "OurBankDescription":string,
   "ShipToCustInactive":boolean,
   "ShipToCustBTName":string,
   "ShipToCustCustID":string,
   "ShipToCustName":string,
   "ShipToNumInactive":boolean,
   "ShipViaCodeDescription":string,
   "ShipViaCodeWebDesc":string,
   "TaxRegionDescription":string,
   "TranDocTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
   "UD_SysRevID":string,
   "Review_c":boolean,
}

export interface Erp_Tablesets_ShipHeadTrailerRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Packing Slip  */  
   "PackNum":number,
      /**  License Plate for Trailer  */  
   "LicensePlate":string,
      /**  Type of Trailer  */  
   "Type":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ShipMiscRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Packing slip number of the ShipHead record that this record is related to.  */  
   "PackNum":number,
      /**   The packing slip line number of the ShipDtl record that this record is related to.
NOTE: This is always zero.  Currently ShipMisc records are only related to the ShipHead record.  */  
   "PackLine":number,
      /**  An integer assigned by the system which is used as one of the components of the unique index for this record.  */  
   "SeqNum":number,
      /**  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  */  
   "MiscCode":string,
      /**  Description of the miscellaneous charge. This will be printed on the Packing Slip and transferred over to invoice processing. The default is provided by MiscChrg.Description, but it's overrideable by the user. This can't be blank.  */  
   "Description":string,
      /**  The amount of the Miscellaneous Charge/Credit. Can't be zero. Use MiscChrg.MiscAmt as a default.  */  
   "MiscAmt":number,
      /**  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  */  
   "SourceDBRecid":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  The amount of the Miscellaneous Charge/Credit including taxes. Can't be zero. Use MiscChrg.MiscAmt as a default.  */  
   "InMiscAmt":number,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   "Percentage":number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   "Type":string,
      /**  WIIsAutoCreatedMisc  */  
   "WIIsAutoCreatedMisc":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The amount of the MiscAmt converted to the ShipHead CurrencyCode  */  
   "DocMiscAmt":number,
      /**  The date and time that the record was last changed  */  
   "ChangeDateTime":string,
      /**  The amount of misc charge on display. If the Tax Liability is flagged as Tax Inclusive Pricing then this amount is InMiscAmount else this amount is MiscAmt.  */  
   "DspMiscAmt":number,
   "BitFlag":number,
   "MiscCodeDescription":string,
   "PackNumShipStatus":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ShipTaxSumRow{
   "Company":string,
   "CurrencyCode":string,
      /**  Currency display switch  */  
   "CurrencySwitch":boolean,
      /**  Currency display symbol  */  
   "DisplaySymbol":string,
      /**  DocDisplaySymbol  */  
   "DocDisplaySymbol":string,
      /**  Document reportable amount.  */  
   "DocReportableAmt":number,
      /**  Document taxable amount.  */  
   "DocTaxableAmt":number,
      /**  Document tax amount.  */  
   "DocTaxAmt":number,
      /**  Pack ID  */  
   "PackNum":number,
      /**  pack line  */  
   "PackLIne":number,
      /**  Percent  */  
   "Percent":number,
   "RateCode":string,
   "ReportableAmt":number,
   "Rpt1ReportableAmt":number,
   "Rpt1TaxableAmt":number,
   "Rpt1TaxAmt":number,
   "Rpt2ReportableAmt":number,
   "Rpt2TaxableAmt":number,
   "Rpt2TaxAmt":number,
   "Rpt3ReportableAmt":number,
   "Rpt3TaxableAmt":number,
   "Rpt3TaxAmt":number,
   "TaxableAmt":number,
   "TaxAmt":number,
   "TaxCode":string,
   "TaxDescription":string,
   "RateCodeDesc":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ShipUPSRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   "PackNum":number,
      /**  UPS Quantum View Sequence  */  
   "UPSQVSeq":number,
      /**  UPS Emailaddress  */  
   "EmailAddress":string,
      /**  Notify Emailaddress when shipped  */  
   "ShipmentNotify":boolean,
      /**  Logical indicating if the Email Address is to be notified of a failed shipment.  */  
   "FailureNotify":boolean,
      /**  Logical indicating if the Email Address is to be notified of delivery.  */  
   "DeliveryNotify":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Logical indicating if the UPS email fields are to be enabled.  */  
   "EnableQuantumView":boolean,
   "ShipStatus":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ipSalesOrder
      @param ipPackNum
      @param ds
   */  
export interface AfterChangedShipDtlOrderNum_input{
   ipSalesOrder:number,
   ipPackNum:number,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface AfterChangedShipDtlOrderNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

export interface AllowUndoExternalDN_output{
}

   /** Required : 
      @param iPackNum
      @param iOrderNum
      @param iOrderLine
      @param iOrderRelNum
      @param askUser
   */  
export interface AskForShipToChange_input{
      /**  Pack Number  */  
   iPackNum:number,
      /**  Order Number  */  
   iOrderNum:number,
      /**  Order Line Number  */  
   iOrderLine:number,
      /**  Release Number  */  
   iOrderRelNum:number,
      /**  Tells if the user must be asked for changing the Shipping Information  */  
   askUser:boolean,
}

export interface AskForShipToChange_output{
parameters : {
      /**  output parameters  */  
   askUser:boolean,
}
}

   /** Required : 
      @param ipPackNum
      @param ds
   */  
export interface AssignLegalNumber_input{
      /**  Packing Slip number  */  
   ipPackNum:number,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface AssignLegalNumber_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
   opLegalNumMsg:string,
}
}

   /** Required : 
      @param ipPartNum
      @param ipRevNum
      @param ipSerialNumbers
   */  
export interface BuildCompSerMatch_input{
   ipPartNum:string,
   ipRevNum:string,
   ipSerialNumbers:string,
}

export interface BuildCompSerMatch_output{
   returnObj:Erp_Tablesets_LLCompSerMatchTableset[],
}

   /** Required : 
      @param ds
      @param ds1
      @param packLine
   */  
export interface BuildSerialMatchingParams_input{
   ds:Erp_Tablesets_SerialMatchingParamsTableset[],
   ds1:Erp_Tablesets_CustShipTableset[],
      /**  Detail Line Number to update  */  
   packLine:number,
}

export interface BuildSerialMatchingParams_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialMatchingParamsTableset[],
}
}

   /** Required : 
      @param orderNum
   */  
export interface BuildShipToCustomerList_input{
      /**  Order Number  */  
   orderNum:number,
}

export interface BuildShipToCustomerList_output{
parameters : {
      /**  output parameters  */  
   shipToCustomerList:string,
}
}

   /** Required : 
      @param orderNum
      @param iShipToCustNum
   */  
export interface BuildShipToList_input{
      /**  Order Number  */  
   orderNum:number,
      /**  Ship To Customer ID  */  
   iShipToCustNum:number,
}

export interface BuildShipToList_output{
parameters : {
      /**  output parameters  */  
   shipToList:string,
}
}

   /** Required : 
      @param ds
      @param orderLine
      @param orderRelNum
      @param effectiveDate
   */  
export interface CalculateWarrantyExpiration_input{
   ds:Erp_Tablesets_CustShipTableset[],
   orderLine:number,
   orderRelNum:number,
   effectiveDate:string,
}

export interface CalculateWarrantyExpiration_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param cartonNumber
   */  
export interface CalculateWeight_input{
   cartonNumber:number,
}

export interface CalculateWeight_output{
parameters : {
      /**  output parameters  */  
   calculatedWeight:number,
}
}

   /** Required : 
      @param ipPackNum
      @param ipNbrCartonsToCreate
      @param ipPkgCode
      @param ipPkgLength
      @param ipPkgWidth
      @param ipPkgHeight
      @param ipRecalcAmts
      @param ipZeroWeight
      @param ds
   */  
export interface CallsCreateCustomerCartons_input{
   ipPackNum:number,
   ipNbrCartonsToCreate:number,
   ipPkgCode:string,
   ipPkgLength:number,
   ipPkgWidth:number,
   ipPkgHeight:number,
   ipRecalcAmts:boolean,
   ipZeroWeight:boolean,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface CallsCreateCustomerCartons_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ipShipHedRowID
   */  
export interface CanStage_input{
      /**  Unique Identifier for the Transfer Order Shipment  */  
   ipShipHedRowID:string,
}

export interface CanStage_output{
}

   /** Required : 
      @param packNum
      @param ds
   */  
export interface CancelVoid_input{
      /**  Packing Slip Number  */  
   packNum:number,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface CancelVoid_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ipWeight
   */  
export interface CartonValidateWeight_input{
   ipWeight:number,
}

export interface CartonValidateWeight_output{
}

   /** Required : 
      @param ds
   */  
export interface ChangeIncotermCode_input{
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface ChangeIncotermCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ipSource
      @param ipPackNum
      @param ipPCID
      @param ds
   */  
export interface ChangePCIDPackVerify_input{
      /**  ipSource  */  
   ipSource:string,
      /**  ipPackNum  */  
   ipPackNum:number,
      /**  ipPCID  */  
   ipPCID:string,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface ChangePCIDPackVerify_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
   opAlreadyScannedPackNum:number,
   opPCIDCount:number,
   opItemPartNum:string,
}
}

   /** Required : 
      @param ipSource
      @param ipPackNum
      @param ipPCID
      @param ds
   */  
export interface ChangePCID_input{
      /**  ipSource  */  
   ipSource:string,
      /**  ipPackNum  */  
   ipPackNum:number,
      /**  ipPCID  */  
   ipPCID:string,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface ChangePCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param packLine
      @param shipCmpl
   */  
export interface ChangeShipCmpl_input{
   ds:Erp_Tablesets_CustShipTableset[],
      /**  Detail Line Number to update  */  
   packLine:number,
      /**  Proposed ShipCmpl change  */  
   shipCmpl:boolean,
}

export interface ChangeShipCmpl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
   questionString:string,
}
}

   /** Required : 
      @param ipMFCustID
      @param ds
   */  
export interface ChangeShipDtlMFCustID_input{
      /**  The proposed Mark For Customer ID  */  
   ipMFCustID:string,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface ChangeShipDtlMFCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ProposedMFShipToNum
      @param ds
   */  
export interface ChangeShipDtlMFShipToNum_input{
      /**  The Proposed Mark For ShipToNum  */  
   ProposedMFShipToNum:string,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface ChangeShipDtlMFShipToNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeShipDtlUseOTMF_input{
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface ChangeShipDtlUseOTMF_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param iShipToCustID
      @param ds
   */  
export interface ChangeShipHeadShipToCustID_input{
      /**  Ship To Customer ID  */  
   iShipToCustID:string,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface ChangeShipHeadShipToCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param newMiscAmt
      @param docAmtChanged
   */  
export interface ChangeShipMiscAmount_input{
   ds:Erp_Tablesets_CustShipTableset[],
      /**  Proposed Miscellaneous Change Percentage  */  
   newMiscAmt:number,
      /**  True if the change was to the DocMiscAmt, false if the change is to DspMiscAmt  */  
   docAmtChanged:boolean,
}

export interface ChangeShipMiscAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param newPrcnt
   */  
export interface ChangeShipMiscPrcnt_input{
   ds:Erp_Tablesets_CustShipTableset[],
      /**  Proposed Miscellaneous Change Percentage  */  
   newPrcnt:number,
}

export interface ChangeShipMiscPrcnt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ipShipHedRowID
      @param ipStatus
      @param ipResetCODCharges
      @param ipResetInsCharges
      @param ds
   */  
export interface ChangeStatus_input{
      /**  Unique Identifier for the Transfer Order Shipment  */  
   ipShipHedRowID:string,
      /**  Selected Status.
           Valid Options: Open, Close, Void, UnVoid, Freight, UnFreight, Stage  */  
   ipStatus:string,
      /**  Indicates if the CODAmount is to be reset to zero  */  
   ipResetCODCharges:boolean,
      /**  Indicates if the DeclaredAmt is to be reset to zero  */  
   ipResetInsCharges:boolean,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface ChangeStatus_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeWarrantyToFSA_input{
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface ChangeWarrantyToFSA_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param iPackNum
      @param markAsShipped
   */  
export interface CheckAttributeSetsOnShipDtlLines_input{
   iPackNum:number,
   markAsShipped:boolean,
}

export interface CheckAttributeSetsOnShipDtlLines_output{
parameters : {
      /**  output parameters  */  
   cErrorMsg:string,
}
}

   /** Required : 
      @param bBeforeUpdate
      @param ds
   */  
export interface CheckCNCustomsDeclarationBillLine_input{
   bBeforeUpdate:boolean,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface CheckCNCustomsDeclarationBillLine_output{
parameters : {
      /**  output parameters  */  
   sMessage:string,
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param iPackNum
      @param iPackLine
   */  
export interface CheckCOOPercents_input{
      /**  The current PackNum  */  
   iPackNum:number,
      /**  The current PackLine  */  
   iPackLine:number,
}

export interface CheckCOOPercents_output{
}

   /** Required : 
      @param ipPackNum
      @param ds
   */  
export interface CheckCompliance_input{
      /**  Current PackNum.  */  
   ipPackNum:number,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface CheckCompliance_output{
parameters : {
      /**  output parameters  */  
   opCompliant:boolean,
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param ipPackNum
      @param ipShipmentType
   */  
export interface CheckOrderComplete_input{
   ds:Erp_Tablesets_CustShipTableset[],
      /**  Pack Num to validate  */  
   ipPackNum:number,
      /**  Type of shipment to validate  */  
   ipShipmentType:string,
}

export interface CheckOrderComplete_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
   msg:string,
}
}

   /** Required : 
      @param packNum
   */  
export interface CheckOrder_input{
      /**  The Pack Number to check out  */  
   packNum:number,
}

export interface CheckOrder_output{
parameters : {
      /**  output parameters  */  
   msg:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CheckPCBinOutLocation_input{
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface CheckPCBinOutLocation_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
   lineNum:number,
   belongToAnotherPC:boolean,
   pcOutsideMessage:string,
}
}

   /** Required : 
      @param packNum
   */  
export interface CheckPackTaxIDForPackNum_input{
   packNum:number,
}

export interface CheckPackTaxIDForPackNum_output{
parameters : {
      /**  output parameters  */  
   errorMessage:string,
}
}

   /** Required : 
      @param packNum
      @param shipToNum
      @param otsOrderNum
   */  
export interface CheckPackTaxID_input{
   packNum:number,
   shipToNum:string,
   otsOrderNum:number,
}

export interface CheckPackTaxID_output{
parameters : {
      /**  output parameters  */  
   errMessage:string,
}
}

   /** Required : 
      @param ipcalledFrom
      @param ipPackNumList
      @param ipPkgCode
      @param ipPkgCodeQty
   */  
export interface CheckPackageCodeAllocNegQty_input{
   ipcalledFrom:string,
   ipPackNumList:object
   ipPkgCode:string,
   ipPkgCodeQty:number,
}

export interface CheckPackageCodeAllocNegQty_output{
parameters : {
      /**  output parameters  */  
   opWarning:string,
   opAction:string,
   opAllocWarning:string,
   opAllocAction:string,
}
}

   /** Required : 
      @param partNum
      @param orderNum
      @param orderLine
   */  
export interface CheckPrePartInfo_input{
      /**  Customer Shipment data set  */  
   partNum:string,
      /**  Pack Num to validate  */  
   orderNum:number,
      /**  Type of shipment to validate  */  
   orderLine:number,
}

export interface CheckPrePartInfo_output{
parameters : {
      /**  output parameters  */  
   partNum:string,
   vMsgText:string,
   vSubAvail:boolean,
   vMsgType:string,
   origPartNum:string,
}
}

   /** Required : 
      @param readyToInvoice
      @param ds
   */  
export interface CheckReadyToInvoice_input{
      /**  Customer Shipment data set  */  
   readyToInvoice:boolean,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface CheckReadyToInvoice_output{
parameters : {
      /**  output parameters  */  
   legalNumberMessage:string,
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface CheckShipDtl_input{
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface CheckShipDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
   releaseMessage:string,
   completeMessage:string,
   shippingMessage:string,
   lotMessage:string,
   inventoryMessage:string,
   lockQtyMessage:string,
   allocationMessage:string,
}
}

   /** Required : 
      @param ipPackNum
   */  
export interface CheckValidCartonWeight_input{
   ipPackNum:number,
}

export interface CheckValidCartonWeight_output{
}

   /** Required : 
      @param ipPackNum
   */  
export interface ClearConvertedManifestUOMFields_input{
   ipPackNum:number,
}

export interface ClearConvertedManifestUOMFields_output{
}

   /** Required : 
      @param ds
      @param orderLine
      @param orderRelNum
   */  
export interface ClearWarrantyInfo_input{
   ds:Erp_Tablesets_CustShipTableset[],
   orderLine:number,
   orderRelNum:number,
}

export interface ClearWarrantyInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ipPackNum
   */  
export interface ConvertToManifestUOM_input{
   ipPackNum:number,
}

export interface ConvertToManifestUOM_output{
}

   /** Required : 
      @param partNum
      @param baseQty
      @param baseUOM
      @param convUOM
   */  
export interface ConvertUOM_input{
      /**  Part number  */  
   partNum:string,
      /**  Qty you wish to convert  */  
   baseQty:number,
      /**  UOM baseQty is specified in  */  
   baseUOM:string,
      /**  UOM to convert to  */  
   convUOM:string,
}

export interface ConvertUOM_output{
parameters : {
      /**  output parameters  */  
   convQty:number,
}
}

   /** Required : 
      @param ipNbrCartonsToCreate
      @param ipPkgCode
      @param ipPkgLength
      @param ipPkgWidth
      @param ipPkgHeight
      @param ipRecalcAmts
      @param ipZeroWeight
      @param ds
   */  
export interface CreateCustomerCartons_input{
   ipNbrCartonsToCreate:number,
   ipPkgCode:string,
   ipPkgLength:number,
   ipPkgWidth:number,
   ipPkgHeight:number,
   ipRecalcAmts:boolean,
   ipZeroWeight:boolean,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface CreateCustomerCartons_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param LotMessage
      @param PartListNeedsAttr
      @param LotListNeedsAttr
      @param ds
   */  
export interface CreateLot_input{
      /**  Lot Message presented to the user showing lines that needed to be created  */  
   LotMessage:string,
      /**  Parts requiring attributes to know if to exclude from the partlot create  */  
   PartListNeedsAttr:string,
      /**  Lots requiring attributes to know if to exclude from the partlot create  */  
   LotListNeedsAttr:string,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface CreateLot_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param packNum
      @param orderNum
      @param ds
   */  
export interface CreateMassShipDtl_input{
      /**  Pack Number to add new shipment lines to  */  
   packNum:number,
      /**  Order Number to create shipment lines from  */  
   orderNum:number,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface CreateMassShipDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

export interface CreatePackForChangePCID_output{
parameters : {
      /**  output parameters  */  
   opPackNum:number,
}
}

   /** Required : 
      @param packNum
   */  
export interface DeleteByID_input{
   packNum:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param ipPackNum
      @param ipPackLine
      @param ds
   */  
export interface DeleteKitComponents_input{
   ipPackNum:number,
   ipPackLine:number,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface DeleteKitComponents_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface DeletePhantomPacks_input{
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface DeletePhantomPacks_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ipFromCase
      @param ipToCase
      @param ds
   */  
export interface DeleteRangePhantomPacks_input{
   ipFromCase:number,
   ipToCase:number,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface DeleteRangePhantomPacks_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

export interface Erp_Tablesets_CartonTrkDtlRow{
      /**  Company ID  */  
   Company:string,
      /**  Defines the type of shipment the tracking number is for.  Shipment type is either Misc for miscellaneous, Sales for Customer shipments, Sub for subcontractor shipments Transfer for Transfer order shipment or Master for Masterpack Shipments.  */  
   ShipmentType:string,
      /**  The pack number associated with the tracking number.  */  
   PackNum:number,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last CartonTrkDtl record for PackNum and add 1. This number is not displayed to the user.  The case number the user sees is the concatenation of the Packnum and this number separated by a dash.  */  
   CaseNum:number,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   PkgLength:number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   PkgHeight:number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   PkgWidth:number,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   TrackingNumber:string,
      /**  Package Weight  */  
   PkgWeight:number,
      /**  Prefer COD delivery.  Reserved for future development.  */  
   CODFlag:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery
Reserved for future development.  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order.  Reserved for future development.  */  
   CODAmount:number,
      /**  Flag to indicate that an insurance value was declared on delivery.  Reserved for future development.  */  
   DeclaredValueFlag:boolean,
      /**  Declared Insurance Amount.  Reserved for future development.  */  
   DeclaredValue:number,
      /**  Unit of Measure the Manifest system expects the pack sizet to be measured in.  */  
   ManifestSizeUOM:string,
      /**  Unit of Measure of the Manifest system expects the pack to be weighed in.  */  
   ManifestWtUOM:string,
      /**  Package Weight in the Manifest System's unit of measure.  */  
   ManifestWeight:number,
      /**  The pack length in the Manifest Unit of Measure.  */  
   ManifestLength:number,
      /**  The pack width in the manifest unit of measure.  */  
   ManifestWidth:number,
      /**  The pack height in the manifest unit of measure.  */  
   ManifestHeight:number,
      /**  Collect On Delivery Value  */  
   CODValue:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Concatenated field consisting of PackNum and CaseNum separated by a dash.  */  
   CaseID:string,
      /**  Status of the shipment.  */  
   PackStatus:string,
      /**  logical used by UI for row rules  */  
   PhantomPack:boolean,
   CapturePt:string,
      /**  Logical indicating if the phantom cartonTrkDtl fields are to be enabled.  This is based upon whether or not the workstation is setup for manifesting.  */  
   EnablePhantom:boolean,
   KitPartAttrClassID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CustShipCustTrkRow{
      /**  From ShipHead.PackNum  */  
   PackNum:number,
      /**  From ShipHead.ShipDate  */  
   ShipDate:string,
      /**  From ShipHead.OrderNum  */  
   OrderNum:number,
      /**  From ShipHead.ReadyToInvoice  */  
   ReadyToInvoice:boolean,
      /**  From ShipHead.Invoiced  */  
   Invoiced:boolean,
      /**  From ShipHead.ShipViaCode  */  
   ShipViaCode:string,
      /**  From ShipHead.TrackingNumber  */  
   TrackingNumber:string,
      /**  From ShipHead.ShipPerson  */  
   ShipPerson:string,
      /**  From ShipHead.Plant  */  
   Plant:string,
      /**  From ShipHead.CustNum  */  
   CustNum:number,
      /**  From ShipDtl.PackLine  */  
   PackLine:number,
      /**  From ShipDtl.OrderLine  */  
   OrderLine:number,
      /**  From ShipDtl.PartNum  */  
   PartNum:string,
      /**  From ShipDtl.LineDesc  */  
   LineDesc:string,
      /**  From ShipDtl.SellingInventoryShipQty  */  
   SellingInventoryShipQty:number,
      /**  From ShipDtl.SellingJobShipQty  */  
   SellingJobShipQty:number,
      /**  From ShipDtl.SalesUM  */  
   SalesUM:string,
      /**  From OrderRel.ReqDate  */  
   RequestDate:string,
      /**  From OrderRel.NeedByDate  */  
   NeedByDate:string,
      /**  From ShipDtl.ShipToNum  */  
   ShipToNum:string,
      /**  Calculated as ShipHead.ShipDate - OrderRel.ReqDate  */  
   OnTime:number,
      /**  From ShipHead.Company  */  
   Company:string,
      /**  from ShipHead.LegalNumber  */  
   LegalNumber:string,
      /**  from ShipDtl.RevisionNum  */  
   RevisionNum:string,
      /**  from ShipDtl.XPartNum  */  
   XPartNum:string,
      /**  from ShipDtl.XRevisionNum  */  
   XRevisionNum:string,
      /**  Populated from OrderHed.BTCustNum  */  
   BTCustNum:number,
      /**  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  */  
   BTConNum:number,
      /**  CustID associated with ShipHeadHead.BTCustNum.  */  
   BTCustID:string,
      /**  CustName associated with ShipHead.BTCustNum  */  
   BTCustomerName:string,
      /**  The full customer's name.  */  
   CustomerName:string,
      /**  The name for the ship to location.  */  
   ShipToName:string,
      /**  The customer ID.  */  
   CustID:string,
   InventoryShipUOM:string,
   JobShipUOM:string,
   OurInventoryShipQty:number,
   OurJobShipQty:number,
   SellingShipmentQty:number,
   VendorNum:number,
   PurPoint:string,
   PackSlip:string,
   DropShip:boolean,
   InvoiceNum:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CustShipCustTrkTableset{
   CustShipCustTrk:Erp_Tablesets_CustShipCustTrkRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CustShipOrdTrkRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   PackNum:number,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   ShipDate:string,
      /**  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  */  
   ShipPerson:string,
      /**  An optional field which can be used to enter a shipping log reference #.  */  
   ShipLog:string,
      /**  Used internally to indicate if the user has pulled this packing slip into invoice processing.  This does NOT ensure that the packing slip has been invoiced.  Only that it was functionally pulled into the invoice process.  This may also be set to "Yes" if the user does not want to use the shipments for generating invoices.  This is condition is indicated when ArSyst.SaveShipments = No.  Under this condition Shipping Entry would initialize "invoiced" to Yes, preventing invoice entry from pulling  */  
   Invoiced:boolean,
      /**  Indicates if the Packing Slip is complete and ready for invoicing. The invoice entry "Get Shipments" function will only select where ShipHead.ReadyToInvoice = Yes  */  
   ReadyToInvoice:boolean,
      /**  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  */  
   CustNum:number,
      /**  The Plant that shipment was made from.  */  
   Plant:string,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   TrackingNumber:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  A flag indicating if this is shipment voided.  This flag is updated via input from the user.  Once a shipment has been voided it can no longer be updated or invoiced.  */  
   Voided:boolean,
      /**  Populated from OrderHed.BTCustNum.  */  
   BTCustNum:number,
      /**  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  */  
   BTConNum:number,
   ShipStatus:string,
   ShipGroup:string,
   PkgCode:string,
   PkgClass:string,
   Weight:number,
   ResDelivery:boolean,
   SatDelivery:boolean,
   SatPickup:boolean,
   VerbalConf:boolean,
   Hazmat:boolean,
   DocOnly:boolean,
   RefNotes:string,
   ApplyChrg:boolean,
   ChrgAmount:number,
   COD:boolean,
   CODFreight:boolean,
   CODCheck:boolean,
   CODAmount:number,
   GroundType:string,
   NotifyFlag:boolean,
   NotifyEMail:string,
   DeclaredIns:boolean,
   DeclaredAmt:number,
   MFTransNum:string,
   MFCallTag:string,
   MFPickupNum:string,
   MFDiscFreight:number,
   MFTemplate:string,
   MFUse3B:boolean,
   MF3BAccount:string,
   MFDimWeight:number,
   MFZone:string,
   MFFreightAmt:number,
   MFOtherAmt:number,
   MFOversized:boolean,
   ServSatDelivery:boolean,
   ServSatPickup:boolean,
   ServSignature:boolean,
   ServAlert:boolean,
   ServPOD:boolean,
   ServAOD:boolean,
   ServHomeDel:boolean,
   DeliveryType:string,
   ServDeliveryDate:string,
   ServPhone:string,
   ServInstruct:string,
   ServRelease:boolean,
   ServAuthNum:string,
   ServRef1:string,
   ServRef2:string,
   ServRef3:string,
   ServRef4:string,
   ServRef5:string,
   BOLNum:number,
   BOLLine:number,
   PONum:string,
      /**  Indicates if Order is on Hold  */  
   OrderHold:boolean,
   JobNum:string,
      /**  CustID associated with ShipHeadHead.BTCustNum.  */  
   BTCustID:string,
      /**  Carton Height  */  
   CartonHeight:number,
      /**  Carton Width  */  
   CartonWidth:number,
      /**  Carton Length  */  
   CartonLength:number,
      /**  Used by the manifest system.  Sum of the value of items in the carton.  Item price - discount + sales tax.  */  
   CartonContentValue:number,
      /**  Set to Y if the carton is the last one being shiped to the customer.  If the sum of the quantity packed does not equal the quantity ordered for each line in the carton the value is No.  */  
   LastCartonFlag:boolean,
      /**  Ship to name for the manifest  */  
   ManifestShipToName:string,
      /**  Manifest Ship To Addres  */  
   ManifestShipToAddress:string,
      /**  Manifest ship to city  */  
   ManifestShipToCity:string,
      /**  State or region value  */  
   ManifestShipToRegion:string,
      /**  Zip Code  */  
   ManifestShipToPostalCode:string,
      /**  ship to country  */  
   ManifestShipToCountry:string,
      /**  Ship to Territory  */  
   ManifestShipToTerritory:string,
      /**  Ship to Attention  */  
   ManifestShipToAttention:string,
      /**  Phone number  */  
   ManifestShipToPhone:string,
      /**  Fax Number  */  
   ManifestShipToFax:string,
      /**  Sold To Name  */  
   ManifestSoldToName:string,
      /**  Sold To Address  */  
   ManifestSoldToAddress:string,
      /**  Sold To City  */  
   ManifestSoldToCity:string,
      /**  Sold To State/Region  */  
   ManifestSoldToRegion:string,
      /**  Sold To Postal Cod  */  
   ManifestSoldToPostalCode:string,
      /**  Sold To Country  */  
   ManifestSoldToCountry:string,
   ManifestSoldToTerritory:string,
      /**  Sold To Attention  */  
   ManifestSoldToAttention:string,
      /**  Sold to Phone number  */  
   ManifestSoldToPhone:string,
      /**  Sold To Fax Number  */  
   ManifestSoldToFax:string,
      /**  Carton Stage Number.  */  
   CartonStageNbr:string,
      /**   The sales order number that this detail shipment line is linked to.
This is not directly maintainable, It is carried forward through from the ShipHead.OrderNum field.  */  
   OrderNum:number,
      /**  The sales order line that this shipment detail line is linked to.  Must be valid in the OrderDtl file.  */  
   OrderLine:number,
      /**  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  */  
   OrderRelNum:number,
   PkgHeight:number,
   PkgLength:number,
   PkgSizeUOM:string,
   PkgWidth:number,
   WeightUOM:string,
   DropShip:boolean,
   PackSlip:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CustShipOrdTrkTableset{
   CustShipOrdTrk:Erp_Tablesets_CustShipOrdTrkRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CustShipPickedOrdersTableset{
   PickedOrders:Erp_Tablesets_PickedOrdersRow[],
   MtlQueue:Erp_Tablesets_MtlQueueRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CustShipTableset{
   ShipHead:Erp_Tablesets_ShipHeadRow[],
   ShipHeadAttch:Erp_Tablesets_ShipHeadAttchRow[],
   CartonTrkDtl:Erp_Tablesets_CartonTrkDtlRow[],
   ShipDtl:Erp_Tablesets_ShipDtlRow[],
   ShipDtlAttch:Erp_Tablesets_ShipDtlAttchRow[],
   ShipCOO:Erp_Tablesets_ShipCOORow[],
   ShipDtlPackaging:Erp_Tablesets_ShipDtlPackagingRow[],
   ShipDtlTax:Erp_Tablesets_ShipDtlTaxRow[],
   ShipHeadInsurance:Erp_Tablesets_ShipHeadInsuranceRow[],
   ShipMisc:Erp_Tablesets_ShipMiscRow[],
   ReplicatedPacks:Erp_Tablesets_ReplicatedPacksRow[],
   ShipHeadTrailer:Erp_Tablesets_ShipHeadTrailerRow[],
   ShipUPS:Erp_Tablesets_ShipUPSRow[],
   LegalNumberGenerate:Erp_Tablesets_LegalNumberGenerateRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   SalesKitCompIssue:Erp_Tablesets_SalesKitCompIssueRow[],
   SelectedIDNumbers:Erp_Tablesets_SelectedIDNumbersRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   ShipTaxSum:Erp_Tablesets_ShipTaxSumRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_LLComSerMatchRow{
   ParentPartNum:string,
   ParentPartDesc:string,
   ChildPartNum:string,
   ChildPartDesc:string,
   SerialNumber:string,
   ParentSerialNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LLCompSerMatchTableset{
   LLComSerMatch:Erp_Tablesets_LLComSerMatchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_LegalNumGenOptsRow{
   Company:string,
   LegalNumberID:string,
   TransYear:number,
   TransYearSuffix:string,
   DspTransYear:string,
      /**  Indicates if DspTransYear should be displayed when prompting for a manual number.  */  
   ShowDspTransYear:boolean,
   Prefix:string,
      /**  The list of prefixes that can be selected by the user for manual numbers.  */  
   PrefixList:string,
      /**  The suffix portion of the legal number.  */  
   NumberSuffix:string,
      /**  Indicates if the prefix can be entered by the user.  */  
   EnablePrefix:boolean,
      /**  Indicates if the suffix (number) can be entered by the user.  */  
   EnableSuffix:boolean,
   NumberOption:string,
   DocumentDate:string,
   GenerationType:string,
   Description:string,
   TransPeriod:number,
      /**  Prefix for the period  */  
   PeriodPrefix:string,
   ShowTransPeriod:boolean,
      /**  Used when the full legal number is entered  */  
   LegalNumber:string,
   TranDocTypeID:string,
   TranDocTypeID2:string,
   GenerationOption:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LegalNumberGenerateRow{
      /**  Company Identifier.  */  
   Company:string,
   NumberType:string,
   NumberYear:number,
      /**  The legal number prefix  */  
   NumberPrefix:string,
   NumberSuffix:string,
   PrefixList:string,
   GenerationType:string,
   EnableNumberPrefix:boolean,
   EnableNumberSuffix:boolean,
   NumberOption:string,
      /**  Unique identifier of the Legal Number record  */  
   LegalNumberNum:number,
   DocumentDate:string,
   AdditionalParams:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MtlQueueRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time(seconds since midnight) when transaction was created.  */  
   SysTime:number,
      /**  Number assigned by the system to uniquely identify the record.  Created by using the database sequence "MtlQueueSeq".  */  
   MtlQueueSeq:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Part Number of item in the container.  */  
   PartNum:string,
      /**  Quantity  */  
   Quantity:number,
      /**   Internal flag to indicate the type of transaction that this request is for.  This will control which functions are invoked for processing.
The same codes as in PartTran are used.  However, there are some additional codes also. 
They are; GET-WIP,  RTN-WIP, RTN-MTL, PUT-MTL, PUT-WIP, PICK-SO, PICK-JOB, PICK-TFO, BIN-REPLENISH, BIN-CONSOLIDATE, PICK-SO-XDOCK, PICK-JOB-XDOCK, PICK-TFO-XDOCK  */  
   TranType:string,
      /**   Used as a translatable prefix for the Reference field.
For example for a purchase receipt of stock it has "PS", (Packing Slip). For display purposes this is field is translated, then concatenated with the value in the Refernce field. 
Other values are "Job",  */  
   ReferencePrefix:string,
      /**  Contains a reference about the request. May contain Job/Asm/Seq, WrkCtr,  Packing Slip #,  Sales Order, etc...depending on the TranType.  */  
   Reference:string,
      /**  Employee ID that made the request.  */  
   RequestedByEmpID:string,
      /**  Employee ID that has selected this record from the queue for processing.  */  
   SelectedByEmpID:string,
      /**  Job Number that the request is related to.  This allows sorting by Job, which provides the user a method of working on all the requests for a specific job.  */  
   JobNum:string,
      /**  Job Assembly Sequence.  */  
   AssemblySeq:number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "O" = Job Operation (JobOper).  */  
   JobSeqType:string,
      /**  Seq # of the related specific material or operation record.  For WIP parts it's the operation sequence that created the part. For raw materials it's the related JobMtl.MtlSeq.  */  
   JobSeq:number,
      /**  Warehouse Code where item is to be found. For example a Get Raw Material request of a stocked part  would be the warehouse  the requirement was allocated against (JobMtl.WareHouseCode).  A "Move of a WIP part" will contain the Warehouse defined by the WrkCenter.PutWhse...  */  
   FromWhse:string,
      /**  Warehouse bin where item is to be found. For example a Get Raw Material request of a stocked part  would be the Primary Bin of the part/warehouse, if no primary bin, then the first Bin in the warehouse which contains this part, else blank.  A "Move of a WIP part" will contain the bin defined by the WrkCenter.PutBin...  */  
   FromBinNum:string,
      /**  Warehouse where item should be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputWhse).  */  
   ToWhse:string,
      /**  Warehouse bin where item is to be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputBin).  */  
   ToBinNum:string,
      /**  Assembly sequence of the operation that completed quantity of the job operation  will be moved to.  */  
   NextAssemblySeq:number,
      /**  Sequence of the operation that completed quantity of the job operation will be moved to.  */  
   NextJobSeq:number,
      /**  Date the this request is needed by.  Defaults, to current system date.  */  
   NeedByDate:string,
      /**  Time (seconds since midnight) that request is need by.  */  
   NeedByTime:number,
      /**  Vendor number of the related purchase receipt (RcvDtl).  Company,VendorNum, PurPoint, PackSlip,Packline are used to provide the link to the related RcvDtl record.  */  
   VendorNum:number,
      /**  Vendor purchase point id of the related purchase receipt (RcvDtl).  */  
   PurPoint:string,
      /**  Vendors Packing Slip # of the related RcvDtl.  */  
   PackSlip:string,
      /**  Vendors Packing Slip line  # of the related RcvDtl.  */  
   PackLine:number,
      /**   Order number job is making parts for. (See JobProd.OrderNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

OrderNum pertains only to "make to order" requirements.  
Provides relationship to the JobProd for "make to order" requirements.  */  
   OrderNum:number,
      /**  Related Sales order line number.  */  
   OrderLine:number,
      /**  Related sales order release number.  */  
   OrderRelNum:number,
      /**   Job that this job is making parts for. (See JobProd.TargetJobNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

TargetJobNum pertains only to "make to job" requirements.  
Provides relationship to the JobProd for "make to Job" requirements.  */  
   TargetJobNum:string,
      /**  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  */  
   TargetAssemblySeq:number,
      /**  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  */  
   TargetMtlSeq:number,
      /**  Part Revision number  */  
   RevisionNum:string,
      /**  A description of the Part.  */  
   PartDescription:string,
      /**  Internal unit of measure.  */  
   IUM:string,
      /**  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  */  
   PONum:number,
      /**  The PO line # which is being received. Only applicable for PO receipt transactions.  */  
   POLine:number,
      /**  Purchase Order Release # which is being received.  */  
   PORelNum:number,
      /**  Indicates if this MtlQueue is visible to the user on the Material Queue browse.  Set based on the users response to make a "move  request" when reporting quantities.  Set to true visible), if a move request is made.  This was implemented to keep track of labor quantity reported without making a move request.  The move request will then reflect the total quantity to move instead of what was reported on the labor transaction that requested the move.  Regardless of making a "Move Request" labor quantity reporting always creates/updates a MtlQueue record.  */  
   Visible:boolean,
      /**  Return Material Authorization number of related RMAHead.  */  
   RMANum:number,
      /**  Line number of the related RMADtl record.  */  
   RMALine:number,
      /**  RMAReceipt number of the related RMARcpt record.  */  
   RMAReceipt:number,
      /**  RMADisp number of the related RMADisp record.  */  
   RMADisp:number,
      /**  The related NonConf.TranID number. Used to link the MtlQueue table to the NonConf table.  */  
   NCTranID:number,
      /**  Lot Number of the part.  */  
   LotNum:string,
      /**  Indicates this record has been locked by a Advanced Shipping user and is not available for processing by any other user.  */  
   Lock:boolean,
      /**  Used by Advanced Shipping to designate which queue this record is in.  Advanced Shipping queues can prioritize and process records.  */  
   QueueID:string,
      /**  Sequence of this record within an Advanced Shipping Queue.  */  
   QueuePickSeq:number,
      /**  This is an internal sequence number for grouping MtlQueue records.  */  
   ReleaseForPickingSeq:number,
      /**  Warehouse Group that was assigned to this transaction.  */  
   WhseGroupCode:string,
      /**   The status of the transaction of the material.  Valid values:
MGMT-LOCK - Manager locked, RELEASED - Released, HOLD - On Hold, USER-LOCK - Locked for a user, ORDER-HOLD - On Hold for Order Based Picking, QUALITY-HOLD - On Hold for Quality Control, and PICK-PACK - Three step allocation Pick-Pack Method  */  
   TranStatus:string,
      /**  The Wave that was assigned during the allocation process.  */  
   WaveNum:number,
      /**  Transaction Priority.  Valid values are 1,2,3,4,5,6,7,8,9.  One is the highest priority.  */  
   Priority:number,
      /**  Transaction Source  */  
   TranSource:string,
      /**  When the TranStatus, AssignedToEmpID or Priority are modified, this value is updated with the ID of the Manager making the change.  */  
   LastMgrChangeEmpID:string,
      /**  Employee ID that was selected by the Warehouse Manager to process record from the queue.  */  
   AssignedToEmpID:string,
      /**  Transfer Order for which Demand is being satisfied.  */  
   TargetTFOrdNum:string,
      /**  Transfer Order Line for which Demand is being satisfied.  */  
   TargetTFOrdLine:number,
      /**  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  */  
   PackStation:string,
      /**  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  */  
   DistributionType:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Package Control Identification Number  */  
   PCID:string,
      /**  Related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  Last Used PCID on the selected line.  */  
   LastUsedPCID:string,
      /**  The PCID from which the material movement will occur.  */  
   FromPCID:string,
      /**  The PCID to which the material movement will occur.  */  
   ToPCID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  AttributeValueSeq  */  
   AttributeValueSeq:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
   CustID:string,
   CustTerritoryID:string,
      /**  Indicates whether Transfer Order Selector Flag should be disabled.  */  
   DisableTO:boolean,
      /**  From Inventory Selector Flag  */  
   FromInv:boolean,
      /**  From Manufacturing Selector Flag  */  
   FromJob:boolean,
      /**  From Purchasing Selector Flag  */  
   FromPO:boolean,
      /**  From Transfer Order Selector Flag  */  
   FromTO:boolean,
   FromWhseDesc:string,
      /**  Service Order Number from FSA. Only available in FSA Request Workbench.  */  
   FSAServiceOrderNumber:number,
      /**  Service Order Resource Num from FSA. Only available in FSA Request Workbench.  */  
   FSAServiceOrderResourceNum:number,
   HoldStatus:boolean,
   LeadTime:number,
   MaxMfgLotSize:number,
   MfgLeadTime:number,
   MinMfgLotSize:number,
   NeedByTimeDisp:string,
   NonStock:boolean,
      /**  Holds the result of checking sub-menu security.  NO indicates the current user does not have permission to carry out the indicated TranType.  */  
   OkToProcess:boolean,
   OnHandQtySite:number,
   OnHandQtyWhse:number,
   PlantName:string,
   PrimWhseCode:string,
   PrimWhseDesc:string,
   RequestedByEmpName:string,
      /**  Indicates whether an error occured in processing.  */  
   RequestError:boolean,
      /**  Message used to return status information after processing.  */  
   RequestMsg:string,
      /**  Is this material queue row part of the employees warehouse group  */  
   SameWhseGroupEmp:boolean,
   SelectedByEmpName:string,
      /**  Used by user to select rows for mass processing  */  
   SelectedForProcessing:boolean,
   ShipToCity:string,
   ShipToCountry:string,
      /**  Customer Ship To Name  */  
   ShipToName:string,
   ShipToNum:string,
   ShipToState:string,
   ShipToZIP:string,
      /**  Sort priority from highest to lowest (1,2,3,4,5,6,7,8,9,0)  */  
   SortByPriority:number,
      /**  Transfer, Sales Kit, Manufactured or Purchased.  */  
   SourceTypeDesc:string,
   ToWhseDesc:string,
   TransferLeadTime:number,
   TransferPlant:string,
      /**  Readable tran type (used in Replenishment Workbench)  */  
   TranTypeDesc:string,
   VendorNumName:string,
   VendorNumVendorID:string,
      /**  Value is true if this mtlqueue record is related to a wave. False if it is not.  */  
   WaveRelated:boolean,
      /**  Customer Sales Territory Region Code  */  
   CustRegionCode:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Display (decimal) number of pieces for inventory tracked parts.  */  
   DispNumberOfPieces:number,
   BitFlag:number,
   AssemblySeqDescription:string,
   JobNumPartDescription:string,
   OrderLineLineDesc:string,
   OrderNumCurrencyCode:string,
   OrderNumCardMemberName:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumSalesUM:string,
   PartNumPartDescription:string,
   PartNumTrackLots:boolean,
   PartNumPricePerCode:string,
   PartNumSellingFactor:number,
   PartNumIUM:string,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   PartNumAttrClassID:string,
   POLinePartNum:string,
   POLineVenPartNum:string,
   POLineLineDesc:string,
   RMALineLineDesc:string,
   VendorNumAddress1:string,
   VendorNumCity:string,
   VendorNumAddress3:string,
   VendorNumDefaultFOB:string,
   VendorNumCurrencyCode:string,
   VendorNumTermsCode:string,
   VendorNumCountry:string,
   VendorNumVendorID_:string,
   VendorNumState:string,
   VendorNumZIP:string,
   VendorNumName_:string,
   VendorNumAddress2:string,
   WarehouseGroupCodeWhseGroupDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_POSNFormatRow{
      /**  Company  */  
   Company:string,
   HasSerialNumbers:boolean,
      /**  Whether or not to have leading zeroes  */  
   LeadingZeroes:boolean,
      /**  Number of digits in the serial number  */  
   NumberOfDigits:number,
      /**  PartNum  */  
   PartNum:string,
      /**  Serial Number base data type  */  
   SNBaseDataType:string,
      /**  Serial Number format  */  
   SNFormat:string,
      /**  Current Prefix setting  */  
   SNPrefix:string,
   Plant:string,
   SNLastUsedSeq:string,
   SNMask:string,
   SNMaskPrefix:string,
   SNMaskSuffix:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_POSelectedSerialNumbersRow{
      /**  Company  */  
   Company:string,
      /**  Used to flag previously selected serial numbers as deselected  */  
   Deselected:boolean,
   KitWhseList:string,
      /**  PartNum  */  
   PartNum:string,
      /**  True if this serial numbered part passed inspection  */  
   PassedInspection:boolean,
      /**  Reason code description  */  
   ReasonCodeDesc:string,
      /**  Reason code type = s  */  
   ReasonCodeType:string,
      /**  Reference field  */  
   Reference:string,
      /**  Scrapped flag  */  
   Scrapped:boolean,
      /**  Scrapped reason code  */  
   ScrappedReasonCode:string,
      /**  SerialNumber  */  
   SerialNumber:string,
      /**  Base number used to create the serial number  */  
   SNBaseNumber:string,
   SNPrefix:string,
      /**  RowID of the source record for this serial number  */  
   SourceRowID:string,
      /**  TransType of the record that created this serial number  */  
   TransType:string,
      /**  Voided flag  */  
   Voided:boolean,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  */  
   RawSerialNum:string,
      /**  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  */  
   KBLbrAction:number,
      /**  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  */  
   KBLbrActionDesc:string,
      /**  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  */  
   PreventDeselect:boolean,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   poLinkValues:string,
      /**  The mask that was used to generate the serial number  */  
   SNMask:string,
      /**  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  */  
   NotSavedToDB:boolean,
      /**  Used only by SN Assignment, needed here to keep POSelectedSerialNumbers in sync with SelectedSerialNumbers  */  
   XRefPartNum:string,
      /**  Used only by SN Assignment: needed here to keep POSelctedSerialNumbers in sync with SelectedSerialNumbers  */  
   XRefPartType:string,
   PreDeselected:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PackOutRow{
   Company:string,
   PackNum:number,
   ShipViaCode:string,
   EntryPerson:string,
   LabelComment:string,
   ShipComment:string,
   ShipToNum:string,
   CustNum:number,
   PackLine:number,
   OrderNum:number,
   OrderLine:number,
   OrderRelNum:number,
   LineType:string,
   OurInventoryShipQty:number,
   OurJobShipQty:number,
   JobNum:string,
   PartNum:string,
   LineDesc:string,
   RevisionNum:string,
   ShipCmpl:boolean,
   BinNum:string,
   ShpConNum:number,
   LotNum:string,
   DimCode:string,
   DUM:string,
   DimConvFactor:number,
   InvoiceComment:string,
   ShipStatus:string,
   Stage:string,
   BTCustomerName:string,
   BTConNum:number,
   BTCustID:string,
   InvQty:number,
   PackQty:number,
   ShipAddr:string,
   StockPart:boolean,
   CustName:string,
   KitPartNum:string,
   PartNumTrackSerialNum:boolean,
   PartNumPartDescription:string,
   KitNumPartDescription:string,
   KitPartRev:string,
   PartNumTrackDimension:boolean,
   TotRelQty:number,
   PromptPartRev:boolean,
   PromptKitRevision:boolean,
   PromptJobNum:boolean,
   PromptOrderRel:boolean,
   PromptKit:boolean,
   AutoQuantity:boolean,
   PromptOrderLine:boolean,
   ToPlant:string,
   FromPlant:string,
   FromAddr:string,
   PackMode:string,
   WarehouseCode:string,
   PartNumTrackLots:boolean,
   TFOrdNum:string,
   BTCustNum:number,
   AssemblySeq:number,
   OprSeq:number,
   VendorNum:number,
   PurPoint:string,
   WarehouseCodeDescription:string,
   NumMatchs:number,
      /**  Unique identifer for the PackOut dataset  */  
   PackOutNum:number,
   Plant:string,
   IsInvoiced:boolean,
   MFTransNum:string,
   TrackingNumber:string,
   MFCallTag:string,
   MFPickUpNum:string,
   MFZone:string,
   MFFreightAmt:number,
   MFDiscFreight:number,
   MFOtherAmt:number,
   MFOversized:boolean,
   MFTemplate:string,
   MFDimWeight:number,
   ShipDate:string,
   VendorID:string,
   Quantity:number,
   TotPackedQty:number,
   RemainQty:number,
   ShipViaDescription:string,
      /**  Set from ShipHead.HasCartonLines  */  
   HasCartonLines:boolean,
   PONum:number,
   POLine:number,
   PORelNum:number,
      /**  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  */  
   EnableWeight:boolean,
   ShipStatusXlate:string,
   PkgCode:string,
   PkgClass:string,
   KitFlag:string,
      /**  Height of packaging  */  
   PkgHeight:number,
      /**  If zero the packaging height prompt is enabled.  */  
   PkgHeightEnable:number,
      /**  Length of packaging  */  
   PkgLength:number,
      /**  Zero indicates the length is to be enabled.  */  
   PkgLenEnable:number,
      /**  Width of packaging  */  
   PkgWidth:number,
      /**  Zero indicates the width prompt is enabled.  */  
   PkgWidthEnable:number,
   WayBillNbr:string,
   FreightedShipViaCode:string,
      /**  COD Amount  */  
   CODAmount:number,
      /**  Decared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Logical indicating this pack has phantom cases.  Used by UI to disable phantom controlled fields.  */  
   PhantomPack:boolean,
      /**  Pack weight.  */  
   Weight:number,
      /**  Masterpack PackID this pack is on.  */  
   MasterpackPackNum:number,
      /**  Enables the Warehouse and Bin fields on the UIApp  */  
   EnableWhseBin:boolean,
      /**  0 indicates Pkg Size UOM should be enabled  */  
   PkgSizeUOMEnable:number,
   PkgSizeUOM:string,
   WeightUOM:string,
   InventoryShipUOM:string,
   JobShipUOM:string,
   EnablePOSerialBtn:boolean,
   DocumentPrinted:boolean,
      /**  Ship To Customer  */  
   ShipToCustNum:number,
      /**  Boolean indicating if the package control functionality should be enabled.  */  
   EnablePackageControl:boolean,
   PCID:string,
   ShipToWarning:string,
      /**  temp message to display newly created legal number  */  
   LegalNumberMessage:string,
      /**  Legal Number associated with pack  */  
   LegalNumber:string,
      /**  TranDocTypeID associated with Pack.  */  
   TranDocTypeID:string,
      /**  TranDocType Description associated with this Pack  */  
   TranDocTypeDescription:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
   PartNumAttrClassID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   KitAttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   KitAttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   KitAttributeSetShortDescription:string,
   PartNumTrackInventoryAttributes:boolean,
   EnableAttributeSetSearch:boolean,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
      /**  Indicates if a legal number configuration exists for pack out  */  
   HasLegNumCnfg:boolean,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   EnableTranDocType:boolean,
   TrackInventoryByRevision:boolean,
   ReadyToInvoice:boolean,
      /**  Indicates if Ready to Invoice is enabled or not  */  
   EnableReadyToInvoice:boolean,
      /**  Indicates if the record is inactive.  */  
   ShipToInactive:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PackOutTableset{
   PackOut:Erp_Tablesets_PackOutRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   POSelectedSerialNumbers:Erp_Tablesets_POSelectedSerialNumbersRow[],
   POSNFormat:Erp_Tablesets_POSNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PackageControlPackVoidRow{
   Company:string,
   CustContainerPartNum:string,
   CustID:string,
   EDIShipToNum:string,
   LineDesc:string,
   Name:string,
   OurDock:string,
   PackLine:number,
   PackNum:number,
   PartNum:string,
   Plant:string,
   ShipComment:string,
   ShipToNum:string,
   ShipStatus:string,
      /**  Legal Number associated with the PackNum record.  */  
   LegalNumber:string,
   AttrClassID:string,
      /**  Description  */  
   AttributeSetDescription:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   RevisionNum:string,
   PartTrackInventoryByRevision:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PackageControlPackVoidTableset{
   PackageControlPackVoid:Erp_Tablesets_PackageControlPackVoidRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PickedOrdersRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Sales Order Number  */  
   OrderNum:number,
      /**  Sales order Line number that this order release is linked to.  */  
   OrderLine:number,
      /**  The release number assigned by the system.  The user never sees this field. It  is used as a foreign key in other files (such as ShipDtl) to tie those records back to the release record.  */  
   OrderRelNum:number,
      /**  Warehouse picked item is located in.  */  
   WarehouseCode:string,
      /**  Warehouse Bin picked item is located in.  */  
   BinNum:string,
      /**  Job that is supplying the allocated quantity.  This is blank for a shipment from stock.  */  
   SupplyJobNum:string,
      /**  Lot Number of the parts that were picked.  */  
   LotNum:string,
      /**  Picked quantity.  Our units.  */  
   Quantity:number,
      /**  Unit of Measure that Quantity is specified in. Must be a valid UOM.  */  
   UOM:string,
      /**  Date which the item needs to be shipped by in order to meet the customers due date. Mirror image of OrderRel.ReqDate.  Duplicated here for sorting purposes.  */  
   ReqDate:string,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum for sorting purposes.  */  
   CustNum:number,
      /**   ShipTo ID of sales order release.
Duplicated from OrderRel.ShipToNum for sorting purposes.  */  
   ShipToNum:string,
      /**  Ship Via ID duplicated from the OrderRel.ShipViaCode.  Used in the process of generating packing slips from the PickedOrder table.  Each PickedOrders record will become a ShipDtl.   A new Packing slip will be created for each break of Company/Site/Ship Da  */  
   ShipViaCode:string,
      /**  The picked part number.  Normally this would be the same as what's on the related OrderDtl. However, it may be different to allow for substitute parts.  */  
   PartNum:string,
      /**  Sales Order Release has been picked.  */  
   Complete:boolean,
      /**  Populated from OrderHed.BTCustNum  */  
   BTCustNum:number,
      /**  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  */  
   BTConNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PCID  */  
   PCID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  The Hold Product Invoices flag value for the Project  */  
   HoldPrdInv:boolean,
   IsSelected:boolean,
   IsVisible:boolean,
      /**  Contains OTS address  */  
   OTSAddr:string,
   ParentPCID:string,
      /**  The ProjectID  */  
   ProjectID:string,
      /**  The Invoicing Method of the Project  */  
   ConInvMeth:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
   BitFlag:number,
   BinNumDescription:string,
   CustNumName:string,
   CustNumBTName:string,
   CustNumCustID:string,
   OrderLineLineDesc:string,
   OrderNumCurrencyCode:string,
   OrderNumCardMemberName:string,
   PartNumAttrClassID:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumTrackDimension:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumSellingFactor:number,
   PartNumPartDescription:string,
   PartNumTrackLots:boolean,
   PartNumIUM:string,
   PartNumPricePerCode:string,
   PartNumSalesUM:string,
   ShipViaCodeWebDesc:string,
   ShipViaCodeDescription:string,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ReplicatedPacksRow{
      /**  Company ID  */  
   Company:string,
      /**  Parent Pack ID that is used to create the replicated packs.  */  
   PackNum:number,
      /**  This is the pack num that was generated based upon the parent pack num.  */  
   ReplicatedPackNum:number,
   SysRowID:string,
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

export interface Erp_Tablesets_SalesKitCompIssueRow{
   KitPartNum:string,
   KitDescription:string,
   KitWarehouseCodeDesc:string,
   KitWarehouse:string,
   KitWhseList:string,
   PackNum:number,
   PackLine:number,
   KitQtyFromInv:number,
   KitIUM:string,
   KitLotNum:string,
   KitBinNum:string,
   OrderNum:number,
   OrderLine:number,
   OrderRelNum:number,
   KitBinNumEnabled:boolean,
   KitTrackLots:boolean,
   KitSerialTracked:boolean,
   KitQtyFromInvEnabled:boolean,
   SysRowID:string,
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

export interface Erp_Tablesets_SelectedIDNumbersRow{
      /**  Company  */  
   Company:string,
   IDNumber:string,
   JobNum:string,
   PackLine:number,
   PackNum:number,
   PartNum:string,
   SeqNum:number,
   SerialNumber:string,
      /**  RowID of the source record for this ID number  */  
   SourceRowID:string,
   TransType:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
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

export interface Erp_Tablesets_SerialMatchingParamsTableset{
   serialNumbersToMatch:Erp_Tablesets_serialNumbersToMatchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ShipCOORow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  CountryNum for Country of Origin  */  
   OrigCountry:number,
      /**  Qty percent of this part which is from this country of origin.  */  
   QtyPerc:number,
      /**  Value percent of this part from this country of origin.  */  
   ValuePerc:number,
      /**  Is this the primary country of origin for this part  */  
   Primary:boolean,
      /**  The master file to which the country of origin is related. ?ShipDtl?, ?MscShpDt?, ?TFShipDtl?, and ?SubShipD?  */  
   RelatedToFile:string,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  An integer that uniquely identifies a detail record within a Packing slip.  */  
   PackLine:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   CountryDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ShipDtlAttchRow{
   Company:string,
   PackNum:number,
   PackLine:number,
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

export interface Erp_Tablesets_ShipDtlPackagingRow{
   Company:string,
   PackNum:number,
   PackLine:number,
   ParentPkgNum:number,
   TranDocTypeID:string,
   TranDocTypeDesc:string,
   PkgCode:string,
   PkgCodeDesc:string,
   PkgSerialNum:string,
   PkgLength:number,
   PkgWidth:number,
   PkgHeight:number,
   SizeUOM:string,
   Weight:number,
   WeightUOM:string,
   LegalNumber:string,
   PartNum:string,
   OurQty:number,
   IUM:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ShipDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  */  
   PackLine:number,
      /**   The sales order number that this detail shipment line is linked to.
This is not directly maintainable, It is carried forward through from the ShipHead.OrderNum field.  */  
   OrderNum:number,
      /**  The sales order line that this shipment detail line is linked to.  Must be valid in the OrderDtl file.  */  
   OrderLine:number,
      /**  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  */  
   OrderRelNum:number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   LineType:string,
      /**  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand.  This quantity is in the IUM unit of measure.  */  
   OurInventoryShipQty:number,
      /**  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This quantity is in the IUM unit of measure.  */  
   OurJobShipQty:number,
      /**  Job Number that supplied the quantity that was shipped. Defaulted from OrderRel.JobNum.  */  
   JobNum:string,
      /**  Number of Packages  */  
   Packages:number,
      /**  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation. This is not user maintainable. If this is a shipment from inventory use this part number to reduce the Part.Onhand qty.  */  
   PartNum:string,
      /**  Line Description  */  
   LineDesc:string,
      /**  Unit of measure...duplicated from the OrderDtl.IUM...Not user maintainable.  */  
   IUM:string,
      /**  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  */  
   RevisionNum:string,
      /**   Holds any comments about the order line being shipped.  Viewed as an Editor widget.

This gets duplicated from the OrderDtl.ShipComment.  */  
   ShipComment:string,
      /**  Indicates if this shipment should mark the order release as being shipped complete. Only one ShipDtl for a release can be marked as being complete. As the user toggles this field it also sets the OrderRel.ShipCmpl field and adjusts the PartBin.OnHand, PartWhse.AllocQty if necessary.  */  
   ShipCmpl:boolean,
      /**   Indicates the warehouse from which the quantity was shipped. This is only valid if the ShipDtl.Inventory quantity is > 0 and this is a valid part number.

The default should be retrieved from the OrderDtl.WareHseCode. .  */  
   WarehouseCode:string,
      /**  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  */  
   BinNum:string,
      /**  Indicates if this transaction affected inventory at time of creation.  */  
   UpdatedInventory:boolean,
      /**   An optional field that is used if the customer has a different  Part number  than the users internal part number.
This field is defaulted from the OrderDtl.XPartNum.  */  
   XPartNum:string,
      /**  Optional field that contains the customers revision. Default from the OrderDtl.XRevisionNum field.  */  
   XRevisionNum:string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table. This is duplicated from the OrderRel.ShpConNum.  */  
   ShpConNum:number,
      /**  Indicates if this shipment line item will be invoiced for time and materials. This is not maintainable from within shipment entry. It is duplicated from the OrderDtl.TMBilling. The "Get Shipments" function of Invoice Entry uses this flag to automatically create invoices in a "On Hold" status. The idea is that these type of invoices need to be generated to act as a method of tracking invoice requirements, but they cannot yet be invoiced until all the costs are known. At which time the user will enter the appropriate charges, take it off "Hold" and complete the billing process.  */  
   TMBilling:boolean,
      /**  A flag which indicates "invoicing" status. This is a mirror image of ShipHead.Invoiced field. See ShipHead.Invoiced for further info.  */  
   Invoiced:boolean,
      /**  Weight Unit of measure...qualifies the weight field value. (Lb, Oz, Gr...). Defaulted from XASyst.DefaultWUM  */  
   WUM:string,
      /**  Lot Number is for Inventory Shipments.  */  
   LotNum:string,
      /**  Unique dimension code for the part.  */  
   DimCode:string,
      /**  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  */  
   DUM:string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   DimConvFactor:number,
      /**  These comments will be copied into the Invoice detail.  */  
   InvoiceComment:string,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   WarrantyCode:string,
      /**  Customer number that the shipment is for.  Duplicated from ShipHead.CustNum.  Used to allow efficient browsing of the ShipDtl records for a specific customer.  */  
   CustNum:number,
      /**  The shipto number. Used for warranty validation.  */  
   ShipToNum:string,
      /**  For Warranty shipments.  Defaults as Shiphead.shipdate. But can be maintained from the Service Call center.  */  
   EffectiveDate:string,
      /**  The # of days, months, years the material is covered by warranty  */  
   MaterialDuration:number,
      /**  The # of days, months, years the Labor is covered by warranty  */  
   LaborDuration:number,
      /**  The # of days, months, years the Misc. Charges are covered by warranty  */  
   MiscDuration:number,
      /**  Whether the duration of warranty  is for "Days", " Months", "years".  */  
   MaterialMod:string,
      /**  Whether the duration of warranty  is "Days"," Months"," years".  */  
   LaborMod:string,
      /**  Whether the duration of warranty  is for "Days"," Months"," years".  */  
   MiscMod:string,
      /**  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   MaterialExpiration:string,
      /**  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   LaborExpiration:string,
      /**  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   MiscExpiration:string,
      /**  The latest of the 3 warranty expiration dates  */  
   LastExpiration:string,
      /**  Editor widget for Warranty comments.  */  
   WarrantyComment:string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   ContractNum:number,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   ContractCode:string,
      /**  This warranty covers On site visits  */  
   Onsite:boolean,
      /**  Are Material cost covered  */  
   MatCovered:boolean,
      /**  Is Labor Cost Covered  */  
   LabCovered:boolean,
      /**  Are misc. Costs Covered  */  
   MiscCovered:boolean,
      /**  Site that the shipment is from.  Duplicated from ShipHead.Site.  Used to allow efficient browsing of the ShipDtl records.  */  
   Plant:string,
      /**  Indicates if the Packing Slip is complete and ready for invoicing.  This is a mirror image of ShipHead.ReadyToInvoice.  */  
   ReadyToInvoice:boolean,
      /**  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand. This quantity is a mirror of field OurInventoryShipQty except it is in the SUM unit of measure.  */  
   SellingInventoryShipQty:number,
      /**  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This field is a mirror of OurJobShipQty except it is in the SUM unit of measure.  */  
   SellingJobShipQty:number,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingFactor:number,
      /**  Selling Unit of Measure...duplicated from the OrderDtl.SUM...Not user maintainable.  */  
   SalesUM:string,
      /**  The Part's Net Weight * (SellingJobShipQty + SellingInventoryShipQty)  */  
   TotalNetWeight:number,
      /**   Identifies the warehouse for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area warehouse (Site.DefShipWhse) otherwise it's blank.  */  
   WIPWarehouseCode:string,
      /**   Identifies the warehouse bin for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area bin (Site.DefShipBin) otherwise it's blank.  */  
   WIPBinNum:string,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   SellingFactorDirection:string,
      /**  Packing slip comments.  These are comments off of the invoice header.  */  
   HeaderShipComment:string,
      /**  The packline of the kit parent  */  
   KitParentLine:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Unit of Measure of the quantity shipped from Inventory (OurInventoryShipQty). Must be a valid UOM. If Part is Multi-UOM tracking then only the Tracking UOMs are valid otherwise all UOM's of the Parts UOMClass are valid.  */  
   InventoryShipUOM:string,
      /**  Unit of Measure of the quantity shipped from the Job (OurJobShipQty)  */  
   JobShipUOM:string,
      /**  Indicates whether the ShipDtl.PartNum is serial tracked. Required as a db field rather than using the link to PartNumTrackSerialNum to allow validations based on the ShipDtl table rather than the ttShipDtl table. Default is No.  */  
   TrackSerialNum:boolean,
      /**  Lot Number is for Job Shipments.  */  
   JobLotNum:string,
      /**  Identifies the type of Bin is being used (valid values are 'Std', 'Cust', 'Supp').  Associated with field ShipDtl.BinNum  */  
   BinType:string,
      /**  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  */  
   NotCompliant:boolean,
      /**  Displays the cause why the item is not compliant.  */  
   ComplianceMsg:string,
      /**  Unit price discount percent.  */  
   DiscountPercent:number,
      /**   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   PricePerCode:string,
      /**  A flat discount amount for the line item.  It can be zero.  */  
   Discount:number,
      /**  A flat discount amount for the line item.  */  
   DocDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt1Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt2Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt3Discount:number,
      /**  Extended Price for the invoice line item.  */  
   ExtPrice:number,
      /**  Extended Price for the invoice line item.  */  
   DocExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExtPrice:number,
      /**  Unit Price.  */  
   UnitPrice:number,
      /**  Unit Price.  */  
   DocUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
      /**  Quantity picked from inventory that was not manually allocated. This quantity is automatically added to PartAlloc such when inventory is picked, it is considered allocated to this Order.  This quantity is in the IUM unit of measure.  */  
   PickedAutoAllocatedQty:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  A flat discount amount for the line item includes taxes.  It can be zero.  */  
   InDiscount:number,
      /**  A flat discount amount for the line item includes taxes.  */  
   DocInDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt1InDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt2InDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt3InDiscount:number,
      /**  Extended Price for the invoice line item including taxes.  */  
   InExtPrice:number,
      /**  Extended Price for the invoice line item including taxes.  */  
   DocInExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InExtPrice:number,
      /**  Unit Price including taxes.  */  
   InUnitPrice:number,
      /**  Unit Price including taxes.  */  
   DocInUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InUnitPrice:number,
      /**  Indicates that the tax is included in the unit price  */  
   InPrice:boolean,
      /**  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  */  
   MFCustNum:number,
      /**  The ShipTo ID to be used for this record. This MUST BE VALID IN THE SHIPTO file.  */  
   MFShipToNum:string,
      /**  Indicates that the One Time Mark For information defined for this record should be used.  */  
   UseOTMF:boolean,
      /**  One Time Mark For Name of the ShipTo.  */  
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
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
      /**  ShipOvers  */  
   ShipOvers:boolean,
      /**  AllowedOvers  */  
   AllowedOvers:number,
      /**  AllowedUnders  */  
   AllowedUnders:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  This is the quantity being shipped that was not already previously allocated, and could not be auto allocated.  */  
   NotAllocatedQty:number,
      /**  PCID  */  
   PCID:string,
      /**  PCID Item Sequence  */  
   PCIDItemSeq:number,
      /**  The dockingstation of the shipto address.  For future use.  */  
   DockingStation:string,
      /**  For future use.  */  
   UseShipDtlInfo:boolean,
      /**  PkgCodePartNum  */  
   PkgCodePartNum:string,
      /**  CustContainerPartNum  */  
   CustContainerPartNum:string,
      /**  LabelType  */  
   LabelType:string,
      /**  Indicates that the warranty will be sent to FSA  */  
   WarrantySendToFSA:boolean,
      /**  When the shipment line is marked as "send as equipment", it will create an Installation in Epicor FSA.  */  
   FSAEquipment:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set based on OurInventoryShipQty.  */  
   InventoryNumberOfPieces:number,
      /**  Number of pieces for this attribute set based on OurJobShipQty.  */  
   JobNumberOfPieces:number,
      /**  Estimated Value  */  
   MXEstValue:number,
      /**  Estimated Value Currency  */  
   MXEstValueCurrencyCode:string,
      /**  Hazardous Shipment  */  
   MXHazardousShipment:boolean,
      /**  Hazardous Type  */  
   MXHazardousType:string,
      /**  Package Type  */  
   MXPackageType:string,
      /**  CNDeclarationBillLine  */  
   CNDeclarationBillLine:number,
      /**  This is the quantity being shipped from manufacturing that was not already previously allocated, and could not be auto allocated.  */  
   JobNotAllocatedQty:number,
      /**  Quantity picked from manufacturing that was not manually allocated.  */  
   JobPickedAutoAllocatedQty:number,
      /**  Flag to indicate if Order/Line/Rel is Buy To Order  */  
   BuyToOrder:boolean,
      /**  The date and time that the record was last changed  */  
   ChangeDateTime:string,
   CurrencyCode:string,
      /**  Delimited list of available Dimension codes for line  */  
   DimCodeList:string,
      /**  OurInventoryShipQty * DimConvFactor - update inplace of OurInventoryShipQty  */  
   DisplayInvQty:number,
   DocLineTax:number,
      /**  Is Drop Shipment.  */  
   DropShip:boolean,
      /**  Indicates if a detail line has errors to be corrected before leaving packing slip  */  
   DtlError:boolean,
   EnableInvIDBtn:boolean,
   EnableInvSerialBtn:boolean,
      /**  Logical indicating if receipt to a job is allowed.  This is determined by either the xasyst.shipnojob field or whether or not the sales order is linked to a job.  */  
   EnableJobFields:boolean,
   EnableKitIDBtn:boolean,
   EnableMfgIDBtn:boolean,
   EnableMfgSerialBtn:boolean,
   EnableOBInvSerialBtn:boolean,
   EnableOBMfgSerialBtn:boolean,
      /**  Boolean indicating if the package control functionality should be enabled.  */  
   EnablePackageControl:boolean,
   EnablePOSerialBtn:boolean,
   ExtJobNum:string,
   FSAInstallationCost:number,
   FSAInstallationOrderLine:number,
   FSAInstallationOrderNum:number,
      /**  Indicates if the equipment requires an installation prior being marked as “Installed” on a Location in Epicor FSA. If true, at shipment it will create a service order for the installation service in FSA.  */  
   FSAInstallationRequired:boolean,
   FSAInstallationType:string,
      /**  Equal to true if opening Location ID Diaglog  */  
   GetLocIDNum:boolean,
      /**  The invoice legal number.  */  
   InvLegalNumber:string,
      /**  External field to be used in the SalesOrder Tracker to show the user the InvoiceNum linked to the shipment.  */  
   InvoiceNum:number,
   KitBackFlush:boolean,
   KitBinNum:string,
   KitCompIssue:boolean,
   KitCompShipComplete:boolean,
   KitDescription:string,
      /**  Sales Kit flag.  C = 'Component'  P = 'Parent'.  */  
   KitFlag:string,
   KitIUM:string,
   KitLotNum:string,
   KitMassIssue:boolean,
   KitParentIssue:boolean,
   KitPartNum:string,
   KitQtyFromInv:number,
   KitQtyFromInvEnabled:boolean,
   KitSerialTracked:boolean,
   KitTrackLots:boolean,
   KitWarehouse:string,
   KitWarehouseCodeDesc:string,
   KitWhseList:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.   This field comes directly from the table ShipHead.  */  
   LegalNumber:string,
      /**  Individual line content value that is used by the freight web service to calculate the total order value.  */  
   LineContentValue:number,
   LineTax:number,
   LinkMsg:string,
      /**  Contains the Mark For Address  */  
   MarkForAddrList:string,
   MFCustID:string,
      /**  Indicates if Order is on Hold  */  
   OrderHold:boolean,
   OrderRelOurReqQty:number,
   OurJobShipIUM:string,
   OurJobShippedQty:number,
   OurRemainQty:number,
   OurRemainUM:string,
   OurReqQty:number,
   OurReqUM:string,
   OurShippedQty:number,
   OurShippedUM:string,
   OurStockShippedQty:number,
      /**  Packing slip for drop shipment.  */  
   PackSlip:string,
      /**  Used by freight web service  */  
   PartAESExp:string,
   PartCompany:string,
      /**  Used by freight web service  */  
   PartECNNumber:string,
      /**  Used by freight web service  */  
   PartExpLicNumber:string,
      /**  Used by freight web service  */  
   PartExpLicType:string,
      /**  Used by freight web service  */  
   PartHazClass:string,
      /**  Used by freight web service  */  
   PartHazGvrnmtID:string,
      /**  Used by freight web service  */  
   PartHazItem:boolean,
      /**  Used by freight web service  */  
   PartHazPackInstr:string,
      /**  Used by freight web service  */  
   PartHazSub:string,
      /**  Used by freight web service  */  
   PartHazTechName:string,
      /**  Used by freight web service  */  
   PartHTS:string,
      /**  Used by freight web service  */  
   PartNAFTAOrigCountry:string,
      /**  Used by freight web service  */  
   PartNAFTAPref:string,
      /**  Used by freight web service  */  
   PartNAFTAProd:string,
      /**  Used by freight web service  */  
   PartOrigCountry:string,
   PartPartNum:string,
      /**  Used by freight web service  */  
   PartSchedBcode:string,
      /**  Used by freight web service  */  
   PartUseHTSDesc:boolean,
   PONum:string,
      /**  Project of the related Order Line  */  
   ProjectID:string,
      /**  The supplier purchase point ID.  */  
   PurPoint:string,
   RequestDate:string,
   Rpt1LineTax:number,
   Rpt2LineTax:number,
   Rpt3LineTax:number,
   SelectedLocationIDQty:number,
   SellingRemainQty:number,
   SellingRemainUM:string,
   SellingReqQty:number,
   SellingReqUM:string,
   SellingShipmentQty:number,
   SellingShipmentUM:string,
   SellingShippedQty:number,
   SellingShippedUM:string,
      /**  The actual ship date for the packing slip. Default as system date.  This field comes directly from the ShipHead table.  */  
   ShipDate:string,
   ShipToWarning:string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  This field comes directly from the ShipHead table.  */  
   ShipViaCode:string,
      /**  Indicates if Part is a stock Part  */  
   StockPart:boolean,
   TrackID:boolean,
   TranLocationIDQty:number,
      /**  The supplier that drops shipped the good from their inventory to our customer.  */  
   VendorNum:number,
   WhseList:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   KitAttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  The Full Description of the Attribute Set.  */  
   KitAttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   KitAttributeSetShortDescription:string,
   KitPartAttrClassID:string,
   EnableAttributeSetSearch:boolean,
      /**  Mark For address formatted for kinetic.  */  
   MarkForAddrFormatted:string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispInventoryNumberOfPieces:number,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispJobNumberOfPieces:number,
   KitRevisionNum:string,
   CNDeclarationBill:string,
   BitFlag:number,
   BinNumDescription:string,
   ContractCodeContractDescription:string,
   CustNumSendToFSA:boolean,
   CustNumName:string,
   CustNumCustID:string,
   CustNumBTName:string,
   DimensionDimCodeDescription:string,
   JobNumPartDescription:string,
   LotPartLotDescription:string,
   MFShipToNumInactive:boolean,
   OrderLineProdCode:string,
   OrderLineLineDesc:string,
   OrderNumPSCurrCode:string,
   OrderNumCardMemberName:string,
   OrderNumCurrencyCode:string,
   OTMFCountryDescription:string,
   PackNumUseOTS:boolean,
   PackNumShipStatus:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumAttrClassID:string,
   PartNumSendToFSA:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumPricePerCode:string,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   PartNumIUM:string,
   PartNumTrackLots:boolean,
   PartNumTrackDimension:boolean,
   PartNumPartDescription:string,
   PartNumWarrantyCode:string,
   PartNumFSAEquipment:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PlantName:string,
   WarehouseCodeDescription:string,
   WarrantyCodeSendToFSA:boolean,
   WarrantyCodeWarrDescription:string,
   WIPWarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
   UD_SysRevID:string,
   PCID2_c:string,
   PCID3_c:string,
   PCID4_c:string,
   PCID5_c:string,
   PCIDType1_c:string,
   PCIDType2_c:string,
   PCIDType3_c:string,
   PCIDType4_c:string,
   PCIDType5_c:string,
}

export interface Erp_Tablesets_ShipDtlTaxRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  */  
   PackLine:number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  InvcDtl.TaxCode and InvcDtl/InvcMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount ((Qty*unitprice)-discount) or if this is for a InvcMisc record InvcMisc.Amount.  */  
   ReportableAmt:number,
      /**  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  InvcDtl.TaxCode and InvcDtl/InvcMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount ((Qty*unitprice)-discount) or if this is for a InvcMisc record InvcMisc.Amount.  */  
   DocReportableAmt:number,
      /**  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (invcdtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the InvcDt/InvcMisc.TaxCat and the InvcTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  */  
   TaxableAmt:number,
      /**  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (invcdtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the InvcDt/InvcMisc.TaxCat and the InvcTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  */  
   DocTaxableAmt:number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   Percent:number,
      /**  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the InvcDtl.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the InvcDtl.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  */  
   TaxAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the InvcDtl.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the InvcDtl.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  */  
   DocTaxAmt:number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   Manual:boolean,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Reverse Charge.  */  
   ReverseCharge:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Rate Code  */  
   RateCode:string,
      /**  Collection Type  */  
   CollectionType:number,
      /**  Timing of when to report taxes  */  
   Timing:number,
      /**  Exemption Type  */  
   ExemptType:number,
      /**  Exemption Percent  */  
   ExemptPercent:number,
      /**  Resolution Number  */  
   ResolutionNum:string,
      /**  Resolution Date  */  
   ResolutionDate:string,
      /**  Tax Rate Date  */  
   TaxRateDate:string,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   DefTaxableAmt:number,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   DocDefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DefTaxableAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   DefTaxAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   DocDefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DefTaxAmt:number,
      /**  This record was manually added (not in Liability) but will use the standard calculations  */  
   ManAdd:boolean,
      /**  Deducatable Tax Amount  */  
   DedTaxAmt:number,
      /**  Deducatable Tax Amount  */  
   DocDedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DedTaxAmt:number,
      /**   Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  */  
   ECAcquisitionSeq:number,
      /**  Fixed Tax Amount  */  
   FixedAmount:number,
      /**  Document Fixed Tax Amount  */  
   DocFixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt1FixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt2FixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt3FixedAmount:number,
      /**  A flat discount amount for the tax.  */  
   Discount:number,
      /**  A flat discount amount for the tax converted to the customers currency.  */  
   DocDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt1Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt2Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt3Discount:number,
      /**  Unique Identifier for Legal Text  */  
   TextCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CurrencyCode:string,
   CurrencySwitch:boolean,
   DescCollectionType:string,
   TaxDescription:string,
   TaxTotal:number,
   DisplaySymbol:string,
   DocDisplaySymbol:string,
      /**  The date and time that the record was last changed  */  
   ChangeDateTime:string,
   BitFlag:number,
   RateCodeDescription:string,
   SalesTaxDescDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ShipHeadAttchRow{
   Company:string,
   PackNum:number,
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

export interface Erp_Tablesets_ShipHeadInsuranceRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Packing Slip  */  
   PackNum:number,
      /**  InsuranceSeq  */  
   InsuranceSeq:number,
      /**  Insurance Type  */  
   Type:string,
      /**  Insurance Company Name  */  
   CompanyName:string,
      /**  Insurance Policy Number  */  
   PolicyNum:string,
      /**  Insurance Premium  */  
   Premium:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ShipHeadListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   PackNum:number,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   ShipDate:string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  */  
   ShipViaCode:string,
      /**  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  */  
   ShipPerson:string,
      /**  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  */  
   EntryPerson:string,
      /**  An optional field which can be used to enter a shipping log reference #.  */  
   ShipLog:string,
      /**  An optional field that will be printed on the shipping labels for this packing slip.  */  
   LabelComment:string,
      /**  Packing slip comments.  This will print on the Packing Slip.  */  
   ShipComment:string,
      /**  Used internally to indicate if the user has pulled this packing slip into invoice processing.  This does NOT ensure that the packing slip has been invoiced.  Only that it was functionally pulled into the invoice process.  This may also be set to "Yes" if the user does not want to use the shipments for generating invoices.  This is condition is indicated when ArSyst.SaveShipments = No.  Under this condition Shipping Entry would initialize "invoiced" to Yes, preventing invoice entry from pulling them in.  This feature would normally be used during the startup period when they do not yet have A/R fully implemented.  */  
   Invoiced:boolean,
      /**  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   ShipToNum:string,
      /**  Indicates if the Packing Slip is complete and ready for invoicing. The invoice entry "Get Shipments" function will only select where ShipHead.ReadyToInvoice = Yes  */  
   ReadyToInvoice:boolean,
      /**  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  */  
   CustNum:number,
      /**  The Site that shipment was made from.  */  
   Plant:string,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   TrackingNumber:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  A flag indicating if this is shipment voided.  This flag is updated via input from the user.  Once a shipment has been voided it can no longer be updated or invoiced.  */  
   Voided:boolean,
      /**  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  */  
   ExternalDeliveryNote:boolean,
      /**  External  ID  */  
   ExternalID:string,
      /**  Iinter Company Received flag  */  
   ICReceived:boolean,
      /**  Cross reference Packing Slip number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   XRefPackNum:string,
      /**  Populated from OrderHed.BTCustNum.  */  
   BTCustNum:number,
      /**  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  */  
   BTConNum:number,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   ShipStatus:string,
      /**  Group the shipment belongs to for "Staging"  */  
   ShipGroup:string,
      /**  Package Code  */  
   PkgCode:string,
      /**  NMFC Packaging Classification code.  */  
   PkgClass:string,
      /**  Package Weight  */  
   Weight:number,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Verbal Confirmation required  */  
   VerbalConf:boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Transaction Number returned by the Manifest Engine  */  
   MFTransNum:string,
      /**  Manifest Call Tag Number  */  
   MFCallTag:string,
      /**  Manifest Pickup Number  */  
   MFPickupNum:string,
      /**  Manifest Discount Freight Amount  */  
   MFDiscFreight:number,
      /**  Manifest Template Code  */  
   MFTemplate:string,
      /**  Manifest flag to use 3 party billing  */  
   MFUse3B:boolean,
      /**  Manifest's 3rd Party Billing Account  */  
   MF3BAccount:string,
      /**  Manifest Dimension Weight  */  
   MFDimWeight:number,
      /**  Manifest Delivery Zone  */  
   MFZone:string,
      /**  Manifest Published Freight Amount  */  
   MFFreightAmt:number,
      /**  Manifest Other Amount  */  
   MFOtherAmt:number,
      /**  Manifest Oversized flag  */  
   MFOversized:boolean,
      /**  Is a Service Saturday delivery acceptable  */  
   ServSatDelivery:boolean,
      /**  Is a Service Saturday pickup available  */  
   ServSatPickup:boolean,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Auto POD flag  */  
   ServPOD:boolean,
      /**  AOD  */  
   ServAOD:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
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
      /**  Bill of Lading Number the packing slip is linked to  */  
   BOLNum:number,
      /**  Bill of Lading line number linked to  */  
   BOLLine:number,
      /**  Added for international shipping, Is a commercial invoice required  */  
   CommercialInvoice:boolean,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   ShipExprtDeclartn:boolean,
      /**  For International shipping.  Certificate of Orgin required.  */  
   CertOfOrigin:boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   LetterOfInstr:boolean,
      /**  International Shipping - HazardousShipment  */  
   HazardousShipment:boolean,
      /**  Is this an International shipment  */  
   IntrntlShip:boolean,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   PayFlag:string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   PayAccount:string,
      /**  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  */  
   PayBTAddress1:string,
      /**  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  */  
   PayBTAddress2:string,
      /**  Shipping, The city portion of the Payer main address.  */  
   PayBTCity:string,
      /**  The state or province portion of the shipment payer main address.  */  
   PayBTState:string,
      /**  The zip or postal code portion of the shipping payers main address.  */  
   PayBTZip:string,
      /**  The country of the main shipping payers address.  */  
   PayBTCountry:string,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   FFAddress1:string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   FFAddress2:string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   FFCity:string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   FFState:string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   FFZip:string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   FFCountry:string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   FFContact:string,
      /**  International Shipping. Frieght Forwarder company name  */  
   FFCompName:string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   FFPhoneNum:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  International Shipping. Frieght Forwarder ID  */  
   FFID:string,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   IndividualPackIDs:boolean,
      /**  Freight Forwarder Country portion of the address  */  
   FFAddress3:string,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   DeliveryConf:number,
      /**  Additional Handling flag  */  
   AddlHdlgFlag:boolean,
      /**  Non Standard Packaging  */  
   NonStdPkg:boolean,
      /**  Freight Forwarder Country portion of the address  */  
   FFCountryNum:number,
      /**  Payer Bill To Third Address line  */  
   PayBTAddress3:string,
      /**  Payer Bill To Country Number  */  
   PayBTCountryNum:number,
      /**  Payer Bill To Phone Number  */  
   PayBTPhone:string,
      /**  Way Bill Number  */  
   WayBillNbr:string,
      /**  This is the ship via code the freighting system selected for shipping.  */  
   FreightedShipViaCode:string,
      /**  UPS Quantum View  */  
   UPSQuantumView:boolean,
      /**  UPS Quantum View From Name  */  
   UPSQVShipFromName:string,
      /**  UPS Quantum View Memo  */  
   UPSQVMemo:string,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   PkgLength:number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   PkgWidth:number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   PkgHeight:number,
      /**  Defines if this document is marked as EDI Ready  */  
   EDIReady:boolean,
      /**  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  */  
   PhantomPack:boolean,
      /**  Pack ID of the pack this pack was replicated from.  This is used as a debugging tool and is not presented to the end user.  */  
   ReplicatedFrom:number,
      /**  Informational field containing either Complete or Partial.  This is only popluated if the ReplicatedFrom field has a value.  This is used as a debugging tool and is not presented to the user.  */  
   ReplicatedStat:string,
      /**   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   PkgSizeUOM:string,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   WeightUOM:string,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   UseOTS:boolean,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  The Sales Order number which contains the One Time ShipTo data. The OTSOrderNum along with the values ShipToNum are used to find the OrderHed or OrderRel to obtain the OTS.  */  
   OTSOrderNum:number,
      /**  Indicates whether or not the taxes for this shipment have been calculated.  This field is used to identify those situations where the tax engine was called but did not generate any taxes because none were needed.  */  
   TaxCalculated:boolean,
      /**  Date the taxes were calculated.  Used for informational and audit tracking purposes.  */  
   TaxCalcDate:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt2Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt3Rounding:number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   DocRounding:number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt1TotalTax:number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt2TotalTax:number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt3TotalTax:number,
      /**  Total order Amount. This field is an accumulation of the extended net amounts of the detail line items  */  
   OrderAmt:number,
      /**  Total order Amount in customer currency. This field is an accumulation of the extended net amounts of the detail line items and rounded according to the Doc currency Round rule  */  
   DocOrderAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1OrderAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2OrderAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3OrderAmt:number,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**   Order Total Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   TotalWHTax:number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   DocTotalWHTax:number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt1TotalWHTax:number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt2TotalWHTax:number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt3TotalWHTax:number,
      /**   Order Total Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   TotalSATax:number,
      /**   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   DocTotalSATax:number,
      /**   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt1TotalSATax:number,
      /**   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt2TotalSATax:number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt3TotalSATax:number,
      /**   Order Total Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   TotalTax:number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   DocTotalTax:number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   TotalDiscount:number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt1TotalDiscount:number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt2TotalDiscount:number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt3TotalDiscount:number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   DocTotalDiscount:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  */  
   DeviceUOM:string,
      /**  Unit of Measure the Manifest system expects the pack sizet to be measured in.  */  
   ManifestSizeUOM:string,
      /**  Unit of Measure of the Manifest system expects the pack to be weighed in.  */  
   ManifestWtUOM:string,
      /**  Package Weight in the Manifest System's unit of measure.  */  
   ManifestWeight:number,
      /**  The pack length in the Manifest Unit of Measure.  */  
   ManifestLength:number,
      /**  The pack width in the manifest unit of measure.  */  
   ManifestWidth:number,
      /**  The pack height in the manifest unit of measure.  */  
   ManifestHeight:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Indicates that the tax is included in the unit price  */  
   InPrice:boolean,
      /**  Flag to indicate that project billing Hold Product Invoice flag is true, it prevents this pack slip from being selected for invoicing.  */  
   PBHoldNoInv:boolean,
      /**  Reconciled quantity for the packing slip  */  
   ReconcileQty:number,
      /**  Last trading partner demand schedule processed that affected this packing slip  */  
   ScheduleNumber:string,
      /**  Number of times the customer shipment has been shipped, that means it changed from non shipped status to shipped  */  
   CounterASN:number,
      /**  Bank for Cash Receipts. Default is from 1) Sales Order 2)Bill To Customer 3) System Default(Company).  */  
   OurBank:string,
      /**  It will be used to identify that the shipment will generate an invoice when it got shipped. If the first order release added to a pack belongs to an ERS order, then non ERS order releases will not be allowed in that pack and if the first order release added to a pack belongs to a non ERS order, then ERS order releases will not be allowed in that pack.  */  
   ERSOrder:boolean,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   OrderDate:string,
      /**  Comma delimited list of status types for lookup  */  
   SlipStatus:string,
      /**  Shipping Address  */  
   AddrList:string,
      /**  Billing Address  */  
   BillAddr:string,
      /**  Indicates if Customer is on Credit Hold  */  
   CreditHold:boolean,
      /**  Indicates if Order is on Hold  */  
   OrderHold:boolean,
      /**  Flag indicating OrderRel's going to more than one shipTo  */  
   MultipleShippers:boolean,
      /**  Indicates whether to hide/view ExternalDeliveryNote field  */  
   SendShipment:boolean,
      /**  CustID associated with ShipHeadHead.BTCustNum.  */  
   BTCustID:string,
      /**  CustName associated with ShipHead.BTCustNum.  */  
   BTCustomerName:string,
      /**  Used by the manifest system.  Sum of the value of items in the carton.  Item price - discount + sales tax.  */  
   CartonContentValue:number,
      /**  Set to Y if the carton is the last one being shiped to the customer.  If the sum of the quantity packed does not equal the quantity ordered for each line in the carton the value is No.  */  
   LastCartonFlag:boolean,
      /**  Carton Stage Number.  */  
   CartonStageNbr:string,
   EnableShipped:boolean,
      /**  Order Number for new cartons.  */  
   OrderNum:number,
      /**  Indicates whether the Carton has lines or not.  */  
   HasCartonLines:boolean,
      /**  Displays the contents of XaSyst.StagingReq  */  
   StagingReq:boolean,
      /**  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  */  
   EnableWeight:boolean,
      /**  Indicates if the manifest interface is enabled.  */  
   ManifestFlag:boolean,
      /**  A zero indicates the Packing height is to be enabled.  */  
   PkgHeightEnable:number,
      /**  Indicates if package length is to be enabled.  If the value is zero the prompt is enabled.  */  
   PkgLenEnable:number,
      /**  A zero indicates the packaging width field is to be enabled.  */  
   PkgWidthEnable:number,
      /**  Used to enable users to default the Carton Trk Dtl package settings.  Initial value defaults to the ShipHead.PkgCode.  However, this field does NOT have to be the same as the ShipHead.PkgCode.  */  
   CtnPkgCode:string,
      /**  Number of packs to replicate  */  
   ReplicateCount:number,
      /**  Logical indicating if CartonTrkDtl records exist for this pack.  Used by the UI for row rules.  */  
   PhantomCasesExist:boolean,
      /**  Logical indicating if the PhantomPack checkbox is to be enabled.  */  
   EnablePhantom:boolean,
      /**  Pack ID of the Masterpack this shipment is on.  */  
   MasterpackPackNum:number,
   PkgSizeUOMEnable:number,
   ShipToNumName:string,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
      /**  Indicates if a legal number configuration exists for customer shipments  */  
   HasLegNumCnfg:boolean,
      /**  Document Total tax amount from ShipDtl Tax for Collection type 'Invoice'  */  
   DocTaxAmt:number,
   DocWithholdingTaxAmt:number,
      /**  Intended for internal UI use.  Identifies whether or not taxes are generated for shipdtls.  */  
   EnableTax:boolean,
   TaxAmt:number,
   Rpt1TaxAmt:number,
   Rpt2TaxAmt:number,
   Rpt3TaxAmt:number,
      /**  Indicates if TranDocTypeID is available for input.  */  
   EnableTranDocType:boolean,
      /**  The flag to indicate if Tax Inclusive Pricing should be on display  */  
   DisplayInPrice:boolean,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCodeCurrName:string,
      /**  Description of the currency  */  
   CurrencyCodeCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCodeCurrSymbol:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCodeCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyCodeDocumentDesc:string,
      /**  The full name of the customer.  */  
   CustomerName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustomerBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustomerCustID:string,
      /**  Description of delivery type  */  
   DeliveryTypeDescription:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   FreightedShipViaCodeWebDesc:string,
      /**  Full description for the shipping company (carrier).  */  
   FreightedShipViaCodeDescription:string,
      /**  Full description of the bank account.  */  
   OurBankDescription:string,
      /**  The Bank's full name.  */  
   OurBankBankName:string,
      /**  Master pack packnum  */  
   PackToMasterpackDtlPackNum:number,
      /**  The full name of the customer.  */  
   ShipToCustName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   ShipToCustBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   ShipToCustCustID:string,
      /**  Full description for the shipping company (carrier).  */  
   ShipViaCodeDescription:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   ShipViaCodeWebDesc:string,
      /**  Full description for the Tax Region.  */  
   TaxRegionDescription:string,
      /**  Description  */  
   TranDocTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ShipHeadListTableset{
   ShipHeadList:Erp_Tablesets_ShipHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ShipHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   PackNum:number,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   ShipDate:string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  */  
   ShipViaCode:string,
      /**  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  */  
   ShipPerson:string,
      /**  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  */  
   EntryPerson:string,
      /**  An optional field which can be used to enter a shipping log reference #.  */  
   ShipLog:string,
      /**  An optional field that will be printed on the shipping labels for this packing slip.  */  
   LabelComment:string,
      /**  Packing slip comments.  This will print on the Packing Slip.  */  
   ShipComment:string,
      /**  Used internally to indicate if the user has pulled this packing slip into invoice processing.  This does NOT ensure that the packing slip has been invoiced.  Only that it was functionally pulled into the invoice process.  This may also be set to "Yes" if the user does not want to use the shipments for generating invoices.  This is condition is indicated when ArSyst.SaveShipments = No.  Under this condition Shipping Entry would initialize "invoiced" to Yes, preventing invoice entry from pulling them in.  This feature would normally be used during the startup period when they do not yet have A/R fully implemented.  */  
   Invoiced:boolean,
      /**  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   ShipToNum:string,
      /**  Indicates if the Packing Slip is complete and ready for invoicing. The invoice entry "Get Shipments" function will only select where ShipHead.ReadyToInvoice = Yes  */  
   ReadyToInvoice:boolean,
      /**  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  */  
   CustNum:number,
      /**  The Site that shipment was made from.  */  
   Plant:string,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   TrackingNumber:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  A flag indicating if this is shipment voided.  This flag is updated via input from the user.  Once a shipment has been voided it can no longer be updated or invoiced.  */  
   Voided:boolean,
      /**  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  */  
   ExternalDeliveryNote:boolean,
      /**  External  ID  */  
   ExternalID:string,
      /**  Iinter Company Received flag  */  
   ICReceived:boolean,
      /**  Cross reference Packing Slip number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   XRefPackNum:string,
      /**  Populated from OrderHed.BTCustNum.  */  
   BTCustNum:number,
      /**  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  */  
   BTConNum:number,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   ShipStatus:string,
      /**  Group the shipment belongs to for "Staging"  */  
   ShipGroup:string,
      /**  Package Code  */  
   PkgCode:string,
      /**  NMFC Packaging Classification code.  */  
   PkgClass:string,
      /**  Package Weight  */  
   Weight:number,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Verbal Confirmation required  */  
   VerbalConf:boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Transaction Number returned by the Manifest Engine  */  
   MFTransNum:string,
      /**  Manifest Call Tag Number  */  
   MFCallTag:string,
      /**  Manifest Pickup Number  */  
   MFPickupNum:string,
      /**  Manifest Discount Freight Amount  */  
   MFDiscFreight:number,
      /**  Manifest Template Code  */  
   MFTemplate:string,
      /**  Manifest flag to use 3 party billing  */  
   MFUse3B:boolean,
      /**  Manifest's 3rd Party Billing Account  */  
   MF3BAccount:string,
      /**  Manifest Dimension Weight  */  
   MFDimWeight:number,
      /**  Manifest Delivery Zone  */  
   MFZone:string,
      /**  Manifest Published Freight Amount  */  
   MFFreightAmt:number,
      /**  Manifest Other Amount  */  
   MFOtherAmt:number,
      /**  Manifest Oversized flag  */  
   MFOversized:boolean,
      /**  Is a Service Saturday delivery acceptable  */  
   ServSatDelivery:boolean,
      /**  Is a Service Saturday pickup available  */  
   ServSatPickup:boolean,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Auto POD flag  */  
   ServPOD:boolean,
      /**  AOD  */  
   ServAOD:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
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
      /**  Bill of Lading Number the packing slip is linked to  */  
   BOLNum:number,
      /**  Bill of Lading line number linked to  */  
   BOLLine:number,
      /**  Added for international shipping, Is a commercial invoice required  */  
   CommercialInvoice:boolean,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   ShipExprtDeclartn:boolean,
      /**  For International shipping.  Certificate of Orgin required.  */  
   CertOfOrigin:boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   LetterOfInstr:boolean,
      /**  International Shipping - HazardousShipment  */  
   HazardousShipment:boolean,
      /**  Is this an International shipment  */  
   IntrntlShip:boolean,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   PayFlag:string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   PayAccount:string,
      /**  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  */  
   PayBTAddress1:string,
      /**  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  */  
   PayBTAddress2:string,
      /**  Shipping, The city portion of the Payer main address.  */  
   PayBTCity:string,
      /**  The state or province portion of the shipment payer main address.  */  
   PayBTState:string,
      /**  The zip or postal code portion of the shipping payers main address.  */  
   PayBTZip:string,
      /**  The country of the main shipping payers address.  */  
   PayBTCountry:string,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   FFAddress1:string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   FFAddress2:string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   FFCity:string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   FFState:string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   FFZip:string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   FFCountry:string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   FFContact:string,
      /**  International Shipping. Frieght Forwarder company name  */  
   FFCompName:string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   FFPhoneNum:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  International Shipping. Frieght Forwarder ID  */  
   FFID:string,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   IndividualPackIDs:boolean,
      /**  Freight Forwarder Country portion of the address  */  
   FFAddress3:string,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   DeliveryConf:number,
      /**  Additional Handling flag  */  
   AddlHdlgFlag:boolean,
      /**  Non Standard Packaging  */  
   NonStdPkg:boolean,
      /**  Freight Forwarder Country portion of the address  */  
   FFCountryNum:number,
      /**  Payer Bill To Third Address line  */  
   PayBTAddress3:string,
      /**  Payer Bill To Country Number  */  
   PayBTCountryNum:number,
      /**  Payer Bill To Phone Number  */  
   PayBTPhone:string,
      /**  Way Bill Number  */  
   WayBillNbr:string,
      /**  This is the ship via code the freighting system selected for shipping.  */  
   FreightedShipViaCode:string,
      /**  UPS Quantum View  */  
   UPSQuantumView:boolean,
      /**  UPS Quantum View From Name  */  
   UPSQVShipFromName:string,
      /**  UPS Quantum View Memo  */  
   UPSQVMemo:string,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   PkgLength:number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   PkgWidth:number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   PkgHeight:number,
      /**  Defines if this document is marked as EDI Ready  */  
   EDIReady:boolean,
      /**  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  */  
   PhantomPack:boolean,
      /**  Pack ID of the pack this pack was replicated from.  This is used as a debugging tool and is not presented to the end user.  */  
   ReplicatedFrom:number,
      /**  Informational field containing either Complete or Partial.  This is only popluated if the ReplicatedFrom field has a value.  This is used as a debugging tool and is not presented to the user.  */  
   ReplicatedStat:string,
      /**   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   PkgSizeUOM:string,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   WeightUOM:string,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   UseOTS:boolean,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  The Sales Order number which contains the One Time ShipTo data. The OTSOrderNum along with the values ShipToNum are used to find the OrderHed or OrderRel to obtain the OTS.  */  
   OTSOrderNum:number,
      /**  Indicates whether or not the taxes for this shipment have been calculated.  This field is used to identify those situations where the tax engine was called but did not generate any taxes because none were needed.  */  
   TaxCalculated:boolean,
      /**  Date the taxes were calculated.  Used for informational and audit tracking purposes.  */  
   TaxCalcDate:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt2Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt3Rounding:number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   DocRounding:number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt1TotalTax:number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt2TotalTax:number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt3TotalTax:number,
      /**  Total order Amount. This field is an accumulation of the extended net amounts of the detail line items  */  
   OrderAmt:number,
      /**  Total order Amount in customer currency. This field is an accumulation of the extended net amounts of the detail line items and rounded according to the Doc currency Round rule  */  
   DocOrderAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1OrderAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2OrderAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3OrderAmt:number,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**   Order Total Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   TotalWHTax:number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   DocTotalWHTax:number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt1TotalWHTax:number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt2TotalWHTax:number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt3TotalWHTax:number,
      /**   Order Total Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   TotalSATax:number,
      /**   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   DocTotalSATax:number,
      /**   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt1TotalSATax:number,
      /**   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt2TotalSATax:number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt3TotalSATax:number,
      /**   Order Total Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   TotalTax:number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   DocTotalTax:number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   TotalDiscount:number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt1TotalDiscount:number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt2TotalDiscount:number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt3TotalDiscount:number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   DocTotalDiscount:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  */  
   DeviceUOM:string,
      /**  Unit of Measure the Manifest system expects the pack sizet to be measured in.  */  
   ManifestSizeUOM:string,
      /**  Unit of Measure of the Manifest system expects the pack to be weighed in.  */  
   ManifestWtUOM:string,
      /**  Package Weight in the Manifest System's unit of measure.  */  
   ManifestWeight:number,
      /**  The pack length in the Manifest Unit of Measure.  */  
   ManifestLength:number,
      /**  The pack width in the manifest unit of measure.  */  
   ManifestWidth:number,
      /**  The pack height in the manifest unit of measure.  */  
   ManifestHeight:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Indicates that the tax is included in the unit price  */  
   InPrice:boolean,
      /**  Flag to indicate that project billing Hold Product Invoice flag is true, it prevents this pack slip from being selected for invoicing.  */  
   PBHoldNoInv:boolean,
      /**  Reconciled quantity for the packing slip  */  
   ReconcileQty:number,
      /**  Last trading partner demand schedule processed that affected this packing slip  */  
   ScheduleNumber:string,
      /**  Number of times the customer shipment has been shipped, that means it changed from non shipped status to shipped  */  
   CounterASN:number,
      /**  Bank for Cash Receipts. Default is from 1) Sales Order 2)Bill To Customer 3) System Default(Company).  */  
   OurBank:string,
      /**  It will be used to identify that the shipment will generate an invoice when it got shipped. If the first order release added to a pack belongs to an ERS order, then non ERS order releases will not be allowed in that pack and if the first order release added to a pack belongs to a non ERS order, then ERS order releases will not be allowed in that pack.  */  
   ERSOrder:boolean,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  ShipOvers  */  
   ShipOvers:boolean,
      /**  WIPackSlipCreated  */  
   WIPackSlipCreated:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AGAuthorizationCode  */  
   AGAuthorizationCode:string,
      /**  AGAuthorizationDate  */  
   AGAuthorizationDate:string,
      /**  AGCarrierCUIT  */  
   AGCarrierCUIT:string,
      /**  AGCOTMark  */  
   AGCOTMark:boolean,
      /**  AGDocumentLetter  */  
   AGDocumentLetter:string,
      /**  AGInvoicingPoint  */  
   AGInvoicingPoint:string,
      /**  AGLegalNumber  */  
   AGLegalNumber:string,
      /**  AGPrintingControlType  */  
   AGPrintingControlType:string,
      /**  AGTrackLicense  */  
   AGTrackLicense:string,
      /**  DispatchReason  */  
   DispatchReason:string,
      /**  AGShippingWay  */  
   AGShippingWay:string,
      /**  Our Supplier Code  */  
   OurSupplierCode:string,
      /**  ASNPrintedDate  */  
   ASNPrintedDate:string,
      /**  EDIShipToNum  */  
   EDIShipToNum:string,
      /**  MXIncoterm  */  
   MXIncoterm:string,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  DigitalSignature  */  
   DigitalSignature:string,
      /**  SignedOn  */  
   SignedOn:string,
      /**  SignedBy  */  
   SignedBy:string,
      /**  FirstPrintDate  */  
   FirstPrintDate:string,
      /**  DocCopyNum  */  
   DocCopyNum:number,
      /**  Declaration Bill  */  
   CNDeclarationBill:string,
      /**  Sample  */  
   CNSample:boolean,
      /**  Bonded  */  
   CNBonded:boolean,
      /**  Creation date and time  */  
   MXCertifiedTimestamp:string,
      /**  Certificate Serial Number  */  
   MXCertificateSN:string,
      /**  Certificate  */  
   MXCertificate:string,
      /**  Fiscal Folio (UUID)  */  
   MXFiscalFolio:string,
      /**  SAT Certificate Serial Number  */  
   MXSATCertificateSN:string,
      /**  Digital Seal  */  
   MXDigitalSeal:string,
      /**  SAT Seal  */  
   MXSATSeal:string,
      /**  Original String  */  
   MXOriginalString:string,
      /**  TFD Original String  */  
   MXOriginalStringTFD:string,
      /**  Serie  */  
   MXSerie:string,
      /**  Folio  */  
   MXFolio:string,
      /**  Estimated Date and Time of Departure  */  
   MXETD:string,
      /**  Estimated Date and Time of Arrival  */  
   MXETA:string,
      /**  Distance in Km  */  
   MXDistance:number,
      /**  Permit Type  */  
   MXPermitType:string,
      /**  Permit Number  */  
   MXPermitNum:string,
      /**  Carta Porte Status  */  
   MXCartaPorteStatus:string,
      /**  Vehicle License Plate  */  
   VehicleLicensePlate:string,
      /**  Vehicle Type  */  
   VehicleType:string,
      /**  Vehicle Year  */  
   VehicleYear:number,
      /**  Driver  */  
   DriverID:string,
      /**  MXCancelFiscalFolio  */  
   MXCancelFiscalFolio:string,
      /**  Incoterm Code  */  
   IncotermCode:string,
      /**  Incoterm Location  */  
   IncotermLocation:string,
      /**  Shipping Address  */  
   AddrList:string,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
      /**  Billing Address  */  
   BillAddr:string,
      /**  CustID associated with ShipHeadHead.BTCustNum.  */  
   BTCustID:string,
      /**  CustName associated with ShipHead.BTCustNum.  */  
   BTCustomerName:string,
      /**  Used by the manifest system.  Sum of the value of items in the carton.  Item price - discount + sales tax.  */  
   CartonContentValue:number,
      /**  Carton Stage Number.  */  
   CartonStageNbr:string,
      /**  The date and time that the record was last changed  */  
   ChangeDateTime:string,
      /**  Internal field for temporary storage of check order messages.  */  
   CheckOrderMessage:string,
      /**  This field temporarily holds certain message(s) returned by credit card processing logic for internal processing.  */  
   CreditCardMessage:string,
      /**  Indicates if Customer is on Credit Hold  */  
   CreditHold:boolean,
      /**  Used to enable users to default the Carton Trk Dtl package settings.  Initial value defaults to the ShipHead.PkgCode.  However, this field does NOT have to be the same as the ShipHead.PkgCode.  */  
   CtnPkgCode:string,
      /**  The flag to indicate if Tax Inclusive Pricing should be on display  */  
   DisplayInPrice:boolean,
      /**  Document Total tax amount from ShipDtl Tax for Collection type 'Invoice'  */  
   DocTaxAmt:number,
   DocWithholdingTaxAmt:number,
      /**  Internal flag to indicate if post update processing should be done.  */  
   DoPostUpdate:boolean,
   DspDigitalSignature:string,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
      /**  Logical indicating if the package control functionality should be enabled.  */  
   EnablePackageControl:boolean,
      /**  Logical indicating if the PhantomPack checkbox is to be enabled.  */  
   EnablePhantom:boolean,
   EnableShipped:boolean,
      /**  Intended for internal UI use.  Identifies whether or not taxes are generated for shipdtls.  */  
   EnableTax:boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   EnableTranDocType:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
      /**  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  */  
   EnableWeight:boolean,
      /**  True if the update is being called from Master Pack (needed for validation)  */  
   FromMasterPack:boolean,
      /**  Indicates whether the Carton has lines or not.  */  
   HasCartonLines:boolean,
      /**  Indicates if a legal number configuration exists for customer shipments  */  
   HasLegNumCnfg:boolean,
      /**  Set to Y if the carton is the last one being shiped to the customer.  If the sum of the quantity packed does not equal the quantity ordered for each line in the carton the value is No.  */  
   LastCartonFlag:boolean,
   LegalNumberMessage:string,
      /**  Indicates if the manifest interface is enabled.  */  
   ManifestFlag:boolean,
      /**  Pack ID of the Masterpack this shipment is on.  */  
   MasterpackPackNum:number,
      /**  Flag indicating OrderRel's going to more than one shipTo  */  
   MultipleShippers:boolean,
   OrderDate:string,
      /**  Indicates if Order is on Hold  */  
   OrderHold:boolean,
      /**  Order Number for new cartons.  */  
   OrderNum:number,
   PCID:string,
      /**  Logical indicating if CartonTrkDtl records exist for this pack.  Used by the UI for row rules.  */  
   PhantomCasesExist:boolean,
      /**  A zero indicates the Packing height is to be enabled.  */  
   PkgHeightEnable:number,
      /**  Indicates if package length is to be enabled.  If the value is zero the prompt is enabled.  */  
   PkgLenEnable:number,
   PkgSizeUOMEnable:number,
      /**  A zero indicates the packaging width field is to be enabled.  */  
   PkgWidthEnable:number,
      /**  Internal field for temporary storage of post update messages.  */  
   PostUpdMessage:string,
   QSUseBOL:boolean,
   QSUseCO:boolean,
   QSUseIntl:boolean,
      /**  Internal field for update processing that is true if ReadyToInvoice has been changed.  */  
   ReadyToInvoiceChanged:boolean,
      /**  Number of packs to replicate  */  
   ReplicateCount:number,
   Rpt1TaxAmt:number,
   Rpt2TaxAmt:number,
   Rpt3TaxAmt:number,
      /**  Indicates whether to hide/view ExternalDeliveryNote field  */  
   SendShipment:boolean,
   ShipToNumName:string,
      /**  Comma delimited list of status types for lookup  */  
   SlipStatus:string,
      /**  Carton Stage Ship Status  */  
   StageShipped:boolean,
      /**  Displays the contents of XaSyst.StagingReq  */  
   StagingReq:boolean,
      /**  Internal field for temporary storage of status change messages.  */  
   StatusChgMessage:string,
   TaxAmt:number,
      /**  Internal field for temporary storage of auto invoicing messages.  */  
   AutoInvoiceMessage:string,
      /**  Ship To address formatted for Kinetic.  */  
   ShipToAddressFormatted:string,
      /**  Sold To address formatted  */  
   SoldToAddressFormatted:string,
      /**  Estimated Date of Arrival  */  
   MXETADate:string,
      /**  Estimated Time of Arrival  */  
   MXETATime:number,
      /**  Estimated Date of Departure  */  
   MXETDDate:string,
      /**  Estimated Time of Departure  */  
   MXETDTime:number,
      /**  Flag indicating whether to enable Incoterm Location  */  
   EnableIncotermLocation:boolean,
      /**  Vehicle Weight (in tons)  */  
   MXVehicleWeight:number,
      /**  A unique Carta Porte identification number assigned by Epicor  */  
   MXIdCCP:string,
      /**  Customs Regime for Export transaction  */  
   MXCustomsRegime:string,
      /**  Check box to specify the use of reverse logistic, collection or devolution services when shipping goods.  */  
   MXReverseLogistics:boolean,
   BitFlag:number,
   AGInvoicingPointDescription:string,
   BTCustNumInactive:boolean,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrName:string,
   CustomerSendToFSA:boolean,
   CustomerInactive:boolean,
   CustomerBTName:string,
   CustomerCustID:string,
   CustomerName:string,
   DeliveryTypeDescription:string,
   FreightedShipViaCodeDescription:string,
   FreightedShipViaCodeWebDesc:string,
   IncotermsDescription:string,
   OurBankBankName:string,
   OurBankDescription:string,
   ShipToCustInactive:boolean,
   ShipToCustBTName:string,
   ShipToCustCustID:string,
   ShipToCustName:string,
   ShipToNumInactive:boolean,
   ShipViaCodeDescription:string,
   ShipViaCodeWebDesc:string,
   TaxRegionDescription:string,
   TranDocTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
   UD_SysRevID:string,
   Review_c:boolean,
}

export interface Erp_Tablesets_ShipHeadTrailerRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Packing Slip  */  
   PackNum:number,
      /**  License Plate for Trailer  */  
   LicensePlate:string,
      /**  Type of Trailer  */  
   Type:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ShipMiscRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Packing slip number of the ShipHead record that this record is related to.  */  
   PackNum:number,
      /**   The packing slip line number of the ShipDtl record that this record is related to.
NOTE: This is always zero.  Currently ShipMisc records are only related to the ShipHead record.  */  
   PackLine:number,
      /**  An integer assigned by the system which is used as one of the components of the unique index for this record.  */  
   SeqNum:number,
      /**  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  */  
   MiscCode:string,
      /**  Description of the miscellaneous charge. This will be printed on the Packing Slip and transferred over to invoice processing. The default is provided by MiscChrg.Description, but it's overrideable by the user. This can't be blank.  */  
   Description:string,
      /**  The amount of the Miscellaneous Charge/Credit. Can't be zero. Use MiscChrg.MiscAmt as a default.  */  
   MiscAmt:number,
      /**  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  */  
   SourceDBRecid:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  The amount of the Miscellaneous Charge/Credit including taxes. Can't be zero. Use MiscChrg.MiscAmt as a default.  */  
   InMiscAmt:number,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   Percentage:number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   Type:string,
      /**  WIIsAutoCreatedMisc  */  
   WIIsAutoCreatedMisc:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The amount of the MiscAmt converted to the ShipHead CurrencyCode  */  
   DocMiscAmt:number,
      /**  The date and time that the record was last changed  */  
   ChangeDateTime:string,
      /**  The amount of misc charge on display. If the Tax Liability is flagged as Tax Inclusive Pricing then this amount is InMiscAmount else this amount is MiscAmt.  */  
   DspMiscAmt:number,
   BitFlag:number,
   MiscCodeDescription:string,
   PackNumShipStatus:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ShipTaxSumRow{
   Company:string,
   CurrencyCode:string,
      /**  Currency display switch  */  
   CurrencySwitch:boolean,
      /**  Currency display symbol  */  
   DisplaySymbol:string,
      /**  DocDisplaySymbol  */  
   DocDisplaySymbol:string,
      /**  Document reportable amount.  */  
   DocReportableAmt:number,
      /**  Document taxable amount.  */  
   DocTaxableAmt:number,
      /**  Document tax amount.  */  
   DocTaxAmt:number,
      /**  Pack ID  */  
   PackNum:number,
      /**  pack line  */  
   PackLIne:number,
      /**  Percent  */  
   Percent:number,
   RateCode:string,
   ReportableAmt:number,
   Rpt1ReportableAmt:number,
   Rpt1TaxableAmt:number,
   Rpt1TaxAmt:number,
   Rpt2ReportableAmt:number,
   Rpt2TaxableAmt:number,
   Rpt2TaxAmt:number,
   Rpt3ReportableAmt:number,
   Rpt3TaxableAmt:number,
   Rpt3TaxAmt:number,
   TaxableAmt:number,
   TaxAmt:number,
   TaxCode:string,
   TaxDescription:string,
   RateCodeDesc:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ShipUPSRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   PackNum:number,
      /**  UPS Quantum View Sequence  */  
   UPSQVSeq:number,
      /**  UPS Emailaddress  */  
   EmailAddress:string,
      /**  Notify Emailaddress when shipped  */  
   ShipmentNotify:boolean,
      /**  Logical indicating if the Email Address is to be notified of a failed shipment.  */  
   FailureNotify:boolean,
      /**  Logical indicating if the Email Address is to be notified of delivery.  */  
   DeliveryNotify:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Logical indicating if the UPS email fields are to be enabled.  */  
   EnableQuantumView:boolean,
   ShipStatus:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtCustShipTableset{
   ShipHead:Erp_Tablesets_ShipHeadRow[],
   ShipHeadAttch:Erp_Tablesets_ShipHeadAttchRow[],
   CartonTrkDtl:Erp_Tablesets_CartonTrkDtlRow[],
   ShipDtl:Erp_Tablesets_ShipDtlRow[],
   ShipDtlAttch:Erp_Tablesets_ShipDtlAttchRow[],
   ShipCOO:Erp_Tablesets_ShipCOORow[],
   ShipDtlPackaging:Erp_Tablesets_ShipDtlPackagingRow[],
   ShipDtlTax:Erp_Tablesets_ShipDtlTaxRow[],
   ShipHeadInsurance:Erp_Tablesets_ShipHeadInsuranceRow[],
   ShipMisc:Erp_Tablesets_ShipMiscRow[],
   ReplicatedPacks:Erp_Tablesets_ReplicatedPacksRow[],
   ShipHeadTrailer:Erp_Tablesets_ShipHeadTrailerRow[],
   ShipUPS:Erp_Tablesets_ShipUPSRow[],
   LegalNumberGenerate:Erp_Tablesets_LegalNumberGenerateRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   SalesKitCompIssue:Erp_Tablesets_SalesKitCompIssueRow[],
   SelectedIDNumbers:Erp_Tablesets_SelectedIDNumbersRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   ShipTaxSum:Erp_Tablesets_ShipTaxSumRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_serialNumbersToMatchRow{
   Company:string,
   JobNum:string,
   PartNum:string,
   RevisionNum:string,
   AssemblySeq:number,
   SerialNumber:string,
   validSerialNo:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ExpirationDate
      @param EffectiveDAte
      @param Duration
      @param modifier
   */  
export interface ExpireDate_input{
   ExpirationDate:string,
   EffectiveDAte:string,
   Duration:number,
   modifier:string,
}

export interface ExpireDate_output{
   returnObj:string,
}

export interface ExpressShip_output{
}

   /** Required : 
      @param ds
   */  
export interface GenerateDigitalSignature_input{
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface GenerateDigitalSignature_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param ipPackNum
      @param ipPackLine
      @param ipFromMfg
   */  
export interface GenerateLocationIDNum_input{
   ds:Erp_Tablesets_CustShipTableset[],
      /**  PackNum  */  
   ipPackNum:number,
      /**  PackLine  */  
   ipPackLine:number,
      /**  Called from Mfg  */  
   ipFromMfg:boolean,
}

export interface GenerateLocationIDNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param SNList
      @param ipPartNum
      @param ipPackNum
      @param ipPackLine
      @param ipJobNum
      @param ipUom
      @param ipFromMfg
   */  
export interface GenerateSelectIDNumParams_input{
   SNList:string,
   ipPartNum:string,
   ipPackNum:number,
   ipPackLine:number,
   ipJobNum:string,
   ipUom:string,
   ipFromMfg:boolean,
}

export interface GenerateSelectIDNumParams_output{
   returnObj:Erp_Tablesets_CustShipTableset[],
}

export interface GetAvailTranDocTypes_output{
parameters : {
      /**  output parameters  */  
   AvailTranDocTypes:string,
}
}

   /** Required : 
      @param packNum
   */  
export interface GetByID_input{
   packNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CustShipTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CustShipTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CustShipTableset[],
}

   /** Required : 
      @param ipPkgCode
   */  
export interface GetCartonPackaging_input{
   ipPkgCode:string,
}

export interface GetCartonPackaging_output{
parameters : {
      /**  output parameters  */  
   opPkgHeight:number,
   opPkgWidth:number,
   opPkgLength:number,
}
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
      /**  ipTableName  */  
   tableName:string,
      /**  ipFieldName  */  
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param orderNum
   */  
export interface GetCustShipOrdTrk_input{
      /**  Order Number  */  
   orderNum:number,
}

export interface GetCustShipOrdTrk_output{
   returnObj:Erp_Tablesets_CustShipOrdTrkTableset[],
}

export interface GetDisablePackOut_output{
   returnObj:boolean,
}

export interface GetEnablePackageControl_output{
      /**  bool  */  
   returnObj:boolean,
}

   /** Required : 
      @param orderNum
      @param ds
   */  
export interface GetHeadOrderInfo_input{
      /**  Proposed change to OrderNum  */  
   orderNum:number,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface GetHeadOrderInfo_output{
parameters : {
      /**  output parameters  */  
   creditMessage:string,
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param packLine
      @param jobNum
   */  
export interface GetJobDtlInfo_input{
   ds:Erp_Tablesets_CustShipTableset[],
      /**  Detail Line Number to update  */  
   packLine:number,
      /**  Proposed change to JobNum field  */  
   jobNum:string,
}

export interface GetJobDtlInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param jobNum
      @param ds
   */  
export interface GetJobInfo_input{
      /**  proposed JobNum change on ShipDtl  */  
   jobNum:string,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface GetJobInfo_output{
parameters : {
      /**  output parameters  */  
   creditMessage:string,
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param jobNum
      @param partNum
   */  
export interface GetJobSupOpSeq_input{
      /**  JobNum field  */  
   jobNum:string,
      /**  The part number to validate  */  
   partNum:string,
}

export interface GetJobSupOpSeq_output{
parameters : {
      /**  output parameters  */  
   mtlSeq:string,
}
}

   /** Required : 
      @param ipPackNum
      @param ds
   */  
export interface GetLegalNumGenOpts_input{
      /**  Packing Slip number  */  
   ipPackNum:number,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface GetLegalNumGenOpts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
   opPromptForNum:boolean,
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
   returnObj:Erp_Tablesets_ShipHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipSalesOrder
      @param ipPackNum
      @param ds
   */  
export interface GetManifestInfo_input{
   ipSalesOrder:number,
   ipPackNum:number,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface GetManifestInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param shipmentType
      @param packNum
   */  
export interface GetNewCartonTrkDtl_input{
   ds:Erp_Tablesets_CustShipTableset[],
   shipmentType:string,
   packNum:number,
}

export interface GetNewCartonTrkDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param packNum
      @param orderNum
   */  
export interface GetNewOrdrShipDtl_input{
   ds:Erp_Tablesets_CustShipTableset[],
      /**  Pack ID  */  
   packNum:number,
      /**  Order number to default in the new record (optional)  */  
   orderNum:number,
}

export interface GetNewOrdrShipDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param packNum
   */  
export interface GetNewOrdrShipUPS_input{
   ds:Erp_Tablesets_CustShipTableset[],
      /**  Pack ID  */  
   packNum:number,
}

export interface GetNewOrdrShipUPS_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param relatedToFile
      @param packNum
      @param packLine
   */  
export interface GetNewShipCOO_input{
   ds:Erp_Tablesets_CustShipTableset[],
   relatedToFile:string,
   packNum:number,
   packLine:number,
}

export interface GetNewShipCOO_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param packNum
      @param packLine
   */  
export interface GetNewShipDtlAttch_input{
   ds:Erp_Tablesets_CustShipTableset[],
   packNum:number,
   packLine:number,
}

export interface GetNewShipDtlAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param packNum
      @param packLine
      @param taxCode
      @param rateCode
   */  
export interface GetNewShipDtlTax_input{
   ds:Erp_Tablesets_CustShipTableset[],
   packNum:number,
   packLine:number,
   taxCode:string,
   rateCode:string,
}

export interface GetNewShipDtlTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param packNum
   */  
export interface GetNewShipDtl_input{
   ds:Erp_Tablesets_CustShipTableset[],
   packNum:number,
}

export interface GetNewShipDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param packNum
   */  
export interface GetNewShipHeadAttch_input{
   ds:Erp_Tablesets_CustShipTableset[],
   packNum:number,
}

export interface GetNewShipHeadAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param packNum
   */  
export interface GetNewShipHeadInsurance_input{
   ds:Erp_Tablesets_CustShipTableset[],
   packNum:number,
}

export interface GetNewShipHeadInsurance_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param packNum
   */  
export interface GetNewShipHeadTrailer_input{
   ds:Erp_Tablesets_CustShipTableset[],
   packNum:number,
}

export interface GetNewShipHeadTrailer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewShipHead_input{
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface GetNewShipHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param packNum
      @param packLine
      @param seqNum
   */  
export interface GetNewShipMisc_input{
   ds:Erp_Tablesets_CustShipTableset[],
   packNum:number,
   packLine:number,
   seqNum:number,
}

export interface GetNewShipMisc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param packNum
   */  
export interface GetNewShipUPS_input{
   ds:Erp_Tablesets_CustShipTableset[],
   packNum:number,
}

export interface GetNewShipUPS_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param orderNum
      @param ds
   */  
export interface GetOrderInfo_input{
      /**  Proposed change to OrderNum  */  
   orderNum:number,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface GetOrderInfo_output{
parameters : {
      /**  output parameters  */  
   creditMessage:string,
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param packLine
      @param orderLine
      @param subsPart
   */  
export interface GetOrderLineInfo_input{
   ds:Erp_Tablesets_CustShipTableset[],
      /**  Detail Line Number to update  */  
   packLine:number,
      /**  Proposed Orderline change  */  
   orderLine:number,
      /**  Proposed substitute PartNum  */  
   subsPart:string,
}

export interface GetOrderLineInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param packLine
      @param orderRelNum
      @param allowNewShipTo
   */  
export interface GetOrderRelInfo_input{
   ds:Erp_Tablesets_CustShipTableset[],
      /**  Detail Line Number to update  */  
   packLine:number,
      /**  Proposed OrderRelease change  */  
   orderRelNum:number,
      /**  Allow to take new ShipTo from release  */  
   allowNewShipTo:boolean,
}

export interface GetOrderRelInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ipPkgClass
      @param ds
   */  
export interface GetPOPackClass_input{
   ipPkgClass:string,
   ds:Erp_Tablesets_PackOutTableset[],
}

export interface GetPOPackClass_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackOutTableset[],
}
}

   /** Required : 
      @param ipPkgCode
      @param ds
   */  
export interface GetPOPackaging_input{
   ipPkgCode:string,
   ds:Erp_Tablesets_PackOutTableset[],
}

export interface GetPOPackaging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackOutTableset[],
}
}

   /** Required : 
      @param ipPkgClass
      @param ds
   */  
export interface GetPackClass_input{
   ipPkgClass:string,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface GetPackClass_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param packLine
      @param partNum
      @param SysRowID
      @param rowType
   */  
export interface GetPackOutPartXRef_input{
   ds:Erp_Tablesets_PackOutTableset[],
      /**  Detail Line Number to update  */  
   packLine:number,
      /**  Proposed PartNumber change  */  
   partNum:string,
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   SysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
}

export interface GetPackOutPartXRef_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackOutTableset[],
   partNum:string,
   serialWarning:string,
   questionString:string,
   multipleMatch:boolean,
}
}

   /** Required : 
      @param ipPackNum
   */  
export interface GetPackageControlPackVoid_input{
   ipPackNum:number,
}

export interface GetPackageControlPackVoid_output{
   returnObj:Erp_Tablesets_PackageControlPackVoidTableset[],
}

   /** Required : 
      @param ipPkgCode
      @param ds
   */  
export interface GetPackaging_input{
   ipPkgCode:string,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface GetPackaging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param packLine
      @param partNum
      @param SysRowID
      @param rowType
   */  
export interface GetPartInfo_input{
   ds:Erp_Tablesets_CustShipTableset[],
      /**  Detail Line Number to update  */  
   packLine:number,
      /**  Proposed PartNumber change  */  
   partNum:string,
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   SysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
}

export interface GetPartInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
   partNum:string,
   serialWarning:string,
   questionString:string,
   multipleMatch:boolean,
   idWarning:string,
}
}

   /** Required : 
      @param ipOrderNum
      @param ipPayFlag
      @param ds
   */  
export interface GetPayBTFlagDefaults_input{
   ipOrderNum:number,
   ipPayFlag:string,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface GetPayBTFlagDefaults_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ipPackNum
   */  
export interface GetPkgCodeQtyList_input{
   ipPackNum:number,
}

export interface GetPkgCodeQtyList_output{
parameters : {
      /**  output parameters  */  
   opPkgCodeList:any[],
}
}

   /** Required : 
      @param ds
      @param packLine
      @param displayInvQty
      @param ourJobShipQty
   */  
export interface GetQtyInfo_input{
   ds:Erp_Tablesets_CustShipTableset[],
      /**  Detail Line Number to update  */  
   packLine:number,
      /**  Proposed change to Inventory Qty field  */  
   displayInvQty:number,
      /**  Proposed change to OurJobShipQty field  */  
   ourJobShipQty:number,
}

export interface GetQtyInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param whereClauseShipHead
      @param whereClauseShipHeadAttch
      @param whereClauseShipDtl
      @param whereClauseShipDtlAttch
      @param whereClauseShipMisc
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSerialNumberSearch
      @param whereClauseSNFormat
      @param contactName
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsContactTracker_input{
      /**  Whereclause for ShipHead table.  */  
   whereClauseShipHead:string,
      /**  Whereclause for ShipHeadAttch table.  */  
   whereClauseShipHeadAttch:string,
      /**  Whereclause for ShipDtl table.  */  
   whereClauseShipDtl:string,
      /**  Whereclause for ShipDtlAttch table.  */  
   whereClauseShipDtlAttch:string,
      /**  Whereclause for ShipMisc table.  */  
   whereClauseShipMisc:string,
      /**  Whereclause for SelectedSerialNumbers table.  */  
   whereClauseSelectedSerialNumbers:string,
      /**  Whereclause for SerialNumberSearches table.  */  
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
   returnObj:Erp_Tablesets_CustShipCustTrkTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseShipHead
      @param whereClauseShipHeadAttch
      @param whereClauseShipDtl
      @param whereClauseShipDtlAttch
      @param whereClauseShipMisc
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSerialNumberSearch
      @param whereClauseSNFormat
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustomerTrackerAndSort_input{
      /**  Whereclause for ShipHead table.  */  
   whereClauseShipHead:string,
      /**  Whereclause for ShipHeadAttch table.  */  
   whereClauseShipHeadAttch:string,
      /**  Whereclause for ShipDtl table.  */  
   whereClauseShipDtl:string,
      /**  Whereclause for ShipDtlAttch table.  */  
   whereClauseShipDtlAttch:string,
      /**  Whereclause for ShipMisc table.  */  
   whereClauseShipMisc:string,
      /**  Whereclause for SelectedSerialNumbers table.  */  
   whereClauseSelectedSerialNumbers:string,
      /**  Whereclause for SerialNumberSearch table.  */  
   whereClauseSerialNumberSearch:string,
      /**  Whereclause for SNFormat table.  */  
   whereClauseSNFormat:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsCustomerTrackerAndSort_output{
   returnObj:Erp_Tablesets_CustShipCustTrkTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseShipHead
      @param whereClauseShipHeadAttch
      @param whereClauseShipDtl
      @param whereClauseShipDtlAttch
      @param whereClauseShipMisc
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSerialNumberSearch
      @param whereClauseSNFormat
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustomerTracker_input{
      /**  Whereclause for ShipHead table.  */  
   whereClauseShipHead:string,
      /**  Whereclause for ShipHeadAttch table.  */  
   whereClauseShipHeadAttch:string,
      /**  Whereclause for ShipDtl table.  */  
   whereClauseShipDtl:string,
      /**  Whereclause for ShipDtlAttch table.  */  
   whereClauseShipDtlAttch:string,
      /**  Whereclause for ShipMisc table.  */  
   whereClauseShipMisc:string,
      /**  Whereclause for SelectedSerialNumbers table.  */  
   whereClauseSelectedSerialNumbers:string,
      /**  Whereclause for SerialNumberSearches table.  */  
   whereClauseSerialNumberSearch:string,
      /**  Whereclause for SNFormat table.  */  
   whereClauseSNFormat:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsCustomerTracker_output{
   returnObj:Erp_Tablesets_CustShipCustTrkTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseShipHead
      @param whereClauseShipHeadAttch
      @param whereClauseCartonTrkDtl
      @param whereClauseShipDtl
      @param whereClauseShipDtlAttch
      @param whereClauseShipCOO
      @param whereClauseShipDtlPackaging
      @param whereClauseShipDtlTax
      @param whereClauseShipHeadInsurance
      @param whereClauseShipMisc
      @param whereClauseReplicatedPacks
      @param whereClauseShipHeadTrailer
      @param whereClauseShipUPS
      @param whereClauseLegalNumberGenerate
      @param whereClauseLegalNumGenOpts
      @param whereClauseSalesKitCompIssue
      @param whereClauseSelectedIDNumbers
      @param whereClauseSelectedSerialNumbers
      @param whereClauseShipTaxSum
      @param whereClauseSNFormat
      @param groupID
      @param headNum
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForCashReceipt_input{
   whereClauseShipHead:string,
   whereClauseShipHeadAttch:string,
   whereClauseCartonTrkDtl:string,
   whereClauseShipDtl:string,
   whereClauseShipDtlAttch:string,
   whereClauseShipCOO:string,
   whereClauseShipDtlPackaging:string,
   whereClauseShipDtlTax:string,
   whereClauseShipHeadInsurance:string,
   whereClauseShipMisc:string,
   whereClauseReplicatedPacks:string,
   whereClauseShipHeadTrailer:string,
   whereClauseShipUPS:string,
   whereClauseLegalNumberGenerate:string,
   whereClauseLegalNumGenOpts:string,
   whereClauseSalesKitCompIssue:string,
   whereClauseSelectedIDNumbers:string,
   whereClauseSelectedSerialNumbers:string,
   whereClauseShipTaxSum:string,
   whereClauseSNFormat:string,
   groupID:string,
   headNum:number,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsForCashReceipt_output{
   returnObj:Erp_Tablesets_CustShipTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseShipHead
      @param whereClauseShipHeadAttch
      @param whereClauseCartonTrkDtl
      @param whereClauseShipDtl
      @param whereClauseShipDtlAttch
      @param whereClauseShipCOO
      @param whereClauseShipDtlPackaging
      @param whereClauseShipDtlTax
      @param whereClauseShipHeadInsurance
      @param whereClauseShipMisc
      @param whereClauseReplicatedPacks
      @param whereClauseShipHeadTrailer
      @param whereClauseShipUPS
      @param whereClauseLegalNumberGenerate
      @param whereClauseLegalNumGenOpts
      @param whereClauseSalesKitCompIssue
      @param whereClauseSelectedIDNumbers
      @param whereClauseSelectedSerialNumbers
      @param whereClauseShipTaxSum
      @param whereClauseSNFormat
      @param invoiceNum
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForInvoice_input{
   whereClauseShipHead:string,
   whereClauseShipHeadAttch:string,
   whereClauseCartonTrkDtl:string,
   whereClauseShipDtl:string,
   whereClauseShipDtlAttch:string,
   whereClauseShipCOO:string,
   whereClauseShipDtlPackaging:string,
   whereClauseShipDtlTax:string,
   whereClauseShipHeadInsurance:string,
   whereClauseShipMisc:string,
   whereClauseReplicatedPacks:string,
   whereClauseShipHeadTrailer:string,
   whereClauseShipUPS:string,
   whereClauseLegalNumberGenerate:string,
   whereClauseLegalNumGenOpts:string,
   whereClauseSalesKitCompIssue:string,
   whereClauseSelectedIDNumbers:string,
   whereClauseSelectedSerialNumbers:string,
   whereClauseShipTaxSum:string,
   whereClauseSNFormat:string,
   invoiceNum:number,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsForInvoice_output{
   returnObj:Erp_Tablesets_CustShipTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseShipHead
      @param whereClauseShipHeadAttch
      @param whereClauseCartonTrkDtl
      @param whereClauseShipDtl
      @param whereClauseShipDtlAttch
      @param whereClauseShipCOO
      @param whereClauseShipDtlPackaging
      @param whereClauseShipDtlTax
      @param whereClauseShipHeadInsurance
      @param whereClauseShipMisc
      @param whereClauseReplicatedPacks
      @param whereClauseShipHeadTrailer
      @param whereClauseShipUPS
      @param whereClauseLegalNumberGenerate
      @param whereClauseLegalNumGenOpts
      @param whereClauseSalesKitCompIssue
      @param whereClauseSelectedIDNumbers
      @param whereClauseSelectedSerialNumbers
      @param whereClauseShipTaxSum
      @param whereClauseSNFormat
      @param quoteNum
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForQuote_input{
   whereClauseShipHead:string,
   whereClauseShipHeadAttch:string,
   whereClauseCartonTrkDtl:string,
   whereClauseShipDtl:string,
   whereClauseShipDtlAttch:string,
   whereClauseShipCOO:string,
   whereClauseShipDtlPackaging:string,
   whereClauseShipDtlTax:string,
   whereClauseShipHeadInsurance:string,
   whereClauseShipMisc:string,
   whereClauseReplicatedPacks:string,
   whereClauseShipHeadTrailer:string,
   whereClauseShipUPS:string,
   whereClauseLegalNumberGenerate:string,
   whereClauseLegalNumGenOpts:string,
   whereClauseSalesKitCompIssue:string,
   whereClauseSelectedIDNumbers:string,
   whereClauseSelectedSerialNumbers:string,
   whereClauseShipTaxSum:string,
   whereClauseSNFormat:string,
   quoteNum:number,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsForQuote_output{
   returnObj:Erp_Tablesets_CustShipTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseShipHead
      @param whereClauseShipHeadAttch
      @param whereClauseCartonTrkDtl
      @param whereClauseShipDtl
      @param whereClauseShipDtlAttch
      @param whereClauseShipCOO
      @param whereClauseShipDtlPackaging
      @param whereClauseShipDtlTax
      @param whereClauseShipHeadInsurance
      @param whereClauseShipMisc
      @param whereClauseReplicatedPacks
      @param whereClauseShipHeadTrailer
      @param whereClauseShipUPS
      @param whereClauseLegalNumberGenerate
      @param whereClauseLegalNumGenOpts
      @param whereClauseSalesKitCompIssue
      @param whereClauseSelectedIDNumbers
      @param whereClauseSelectedSerialNumbers
      @param whereClauseShipTaxSum
      @param whereClauseSNFormat
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseShipHead:string,
   whereClauseShipHeadAttch:string,
   whereClauseCartonTrkDtl:string,
   whereClauseShipDtl:string,
   whereClauseShipDtlAttch:string,
   whereClauseShipCOO:string,
   whereClauseShipDtlPackaging:string,
   whereClauseShipDtlTax:string,
   whereClauseShipHeadInsurance:string,
   whereClauseShipMisc:string,
   whereClauseReplicatedPacks:string,
   whereClauseShipHeadTrailer:string,
   whereClauseShipUPS:string,
   whereClauseLegalNumberGenerate:string,
   whereClauseLegalNumGenOpts:string,
   whereClauseSalesKitCompIssue:string,
   whereClauseSelectedIDNumbers:string,
   whereClauseSelectedSerialNumbers:string,
   whereClauseShipTaxSum:string,
   whereClauseSNFormat:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CustShipTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param workstationID
   */  
export interface GetScale_input{
      /**  Workstation ID  */  
   workstationID:string,
}

export interface GetScale_output{
parameters : {
      /**  output parameters  */  
   scaleID:string,
}
}

   /** Required : 
      @param partNum
      @param shipQty
      @param shipUOM
   */  
export interface GetSelectIDNumbersParams_input{
   partNum:string,
   shipQty:number,
   shipUOM:string,
}

export interface GetSelectIDNumbersParams_output{
parameters : {
      /**  output parameters  */  
   convShipQty:number,
}
}

   /** Required : 
      @param ipPartNum
      @param ipAttributeSetID
      @param ipQuantity
      @param ipUOM
      @param ipPackNum
      @param ipPackLine
      @param ipTranType
      @param ipJobNum
      @param ipWhseCode
      @param ipBinNum
      @param ipLotNum
      @param ipFromPO
      @param ipOrderNum
      @param ipOrderLine
      @param ipOrderRelNum
      @param ipSysRowID
   */  
export interface GetSelectSerialNumbersParams_input{
   ipPartNum:string,
   ipAttributeSetID:number,
   ipQuantity:number,
   ipUOM:string,
   ipPackNum:number,
   ipPackLine:number,
   ipTranType:string,
   ipJobNum:string,
   ipWhseCode:string,
   ipBinNum:string,
   ipLotNum:string,
   ipFromPO:boolean,
   ipOrderNum:number,
   ipOrderLine:number,
   ipOrderRelNum:number,
   ipSysRowID:string,
}

export interface GetSelectSerialNumbersParams_output{
   returnObj:Erp_Tablesets_SelectSerialNumbersParamsTableset[],
}

   /** Required : 
      @param ds
      @param miscCode
   */  
export interface GetShipMiscDefaults_input{
   ds:Erp_Tablesets_CustShipTableset[],
      /**  Proposed Miscellaneous Code change  */  
   miscCode:string,
}

export interface GetShipMiscDefaults_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param shipToNum
   */  
export interface GetShipToAddr_input{
   ds:Erp_Tablesets_CustShipTableset[],
      /**  Proposed ShipTo Number change  */  
   shipToNum:string,
}

export interface GetShipToAddr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param packNum
      @param maxNumOfCards
   */  
export interface GetShipmentRelationshipMap_input{
   packNum:number,
   maxNumOfCards:number,
}

export interface GetShipmentRelationshipMap_output{
   returnObj:string,
}

   /** Required : 
      @param ipTranDocTypeID
      @param ds
   */  
export interface GetTranDocTypeID_input{
      /**  TranDocTypeID supplied  */  
   ipTranDocTypeID:string,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface GetTranDocTypeID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param warrantyCode
      @param orderLine
      @param orderRelNum
   */  
export interface GetWarrantyInfo_input{
   ds:Erp_Tablesets_CustShipTableset[],
   warrantyCode:string,
   orderLine:number,
   orderRelNum:number,
}

export interface GetWarrantyInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param packLine
      @param whseCode
      @param whseField
   */  
export interface GetWhseInfo_input{
   ds:Erp_Tablesets_CustShipTableset[],
      /**  Detail Line Number to update  */  
   packLine:number,
      /**  Proposed WarehouseCode change  */  
   whseCode:string,
      /**  Warehouse field that is being changed  */  
   whseField:string,
}

export interface GetWhseInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param packNum
      @param orderNum
      @param ds
   */  
export interface HHCreateMassShipDtl_input{
      /**  Pack Number to add new shipment lines to  */  
   packNum:number,
      /**  Order Number to create shipment lines from  */  
   orderNum:number,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface HHCreateMassShipDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param orderNum
      @param ds
   */  
export interface HHGetOrderInfo_input{
      /**  Proposed change to OrderNum  */  
   orderNum:number,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface HHGetOrderInfo_output{
parameters : {
      /**  output parameters  */  
   creditMessage:string,
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface HHSetDtlDefaultValues_input{
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface HHSetDtlDefaultValues_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
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
export interface MarkShipmentLines_input{
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface MarkShipmentLines_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ipPartNum
      @param ipWarehouseCode
      @param ipBinNum
      @param ipLotNum
      @param ipAttributeSetID
      @param ipPCID
      @param ipDimCode
      @param ipDimConvFactor
      @param ipTranQty
   */  
export interface NegativeInventoryTest_input{
      /**  ipPartNum  */  
   ipPartNum:string,
      /**  ipWarehouseCode  */  
   ipWarehouseCode:string,
      /**  ipBinNum  */  
   ipBinNum:string,
      /**  ipLotNum  */  
   ipLotNum:string,
      /**  ipAttributeSetID  */  
   ipAttributeSetID:number,
      /**  ipPCID  */  
   ipPCID:string,
      /**  ipDimCode  */  
   ipDimCode:string,
      /**  ipDimConvFactor  */  
   ipDimConvFactor:number,
      /**  ipTranQty  */  
   ipTranQty:number,
}

export interface NegativeInventoryTest_output{
parameters : {
      /**  output parameters  */  
   opNegQtyAction:string,
   pcMessage:string,
}
}

   /** Required : 
      @param ipOrderNum
      @param ipOrderLine
      @param pickedOrderRowSysRowID
      @param oldIsSelected
      @param ds
   */  
export interface OnChangePickeOrdersIsSelected_input{
      /**  input order number  */  
   ipOrderNum:number,
      /**  input order line  */  
   ipOrderLine:number,
      /**  SysRowID of the PickedOrders row being changed  */  
   pickedOrderRowSysRowID:string,
      /**  New value for IsSelected  */  
   oldIsSelected:boolean,
   ds:Erp_Tablesets_CustShipPickedOrdersTableset[],
}

export interface OnChangePickeOrdersIsSelected_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipPickedOrdersTableset[],
}
}

   /** Required : 
      @param shipViaCode
      @param ds
   */  
export interface OnChangeShipViaCode_input{
      /**  New ShipVia Code  */  
   shipViaCode:string,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface OnChangeShipViaCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ipPackNum
      @param ipQVEnable
      @param ds
   */  
export interface OnChangeUPSQuantumView_input{
   ipPackNum:number,
   ipQVEnable:boolean,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface OnChangeUPSQuantumView_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param attributeSetID
      @param ds
   */  
export interface OnChangingAttributeSet_input{
   attributeSetID:number,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface OnChangingAttributeSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param numberOfPieces
      @param shippingFrom
      @param ds
   */  
export interface OnChangingDispNumberOfPieces_input{
      /**  The proposed numberOfPieces  */  
   numberOfPieces:number,
      /**  The Number of Pieces field that is changing (INVENTORY or JOB)  */  
   shippingFrom:string,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface OnChangingDispNumberOfPieces_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingRevisionNumPackOut_input{
   revisionNum:string,
   ds:Erp_Tablesets_PackOutTableset[],
}

export interface OnChangingRevisionNumPackOut_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackOutTableset[],
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface OnChangingRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface POChangeStage_input{
   ds:Erp_Tablesets_PackOutTableset[],
}

export interface POChangeStage_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackOutTableset[],
}
}

   /** Required : 
      @param ipStatus
      @param ipResetCODCharges
      @param ipResetInsCharges
      @param ds
   */  
export interface POChangeStatus_input{
      /**  Selected Status.
           Valid Options: Open, Close, Void, UnVoid, Freight, UnFreight, Stage  */  
   ipStatus:string,
      /**  Indicates if the CODAmount is to be reset to zero  */  
   ipResetCODCharges:boolean,
      /**  Indicates if the DeclaredAmt is to be reset to zero  */  
   ipResetInsCharges:boolean,
   ds:Erp_Tablesets_PackOutTableset[],
}

export interface POChangeStatus_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackOutTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface POFindBufWhseBinLot_input{
   ds:Erp_Tablesets_PackOutTableset[],
}

export interface POFindBufWhseBinLot_output{
parameters : {
      /**  output parameters  */  
   found:number,
   rowident:string,
   ds:Erp_Tablesets_PackOutTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface POFindBuffer_input{
   ds:Erp_Tablesets_PackOutTableset[],
}

export interface POFindBuffer_output{
parameters : {
      /**  output parameters  */  
   found:number,
   rowident:string,
   ds:Erp_Tablesets_PackOutTableset[],
}
}

   /** Required : 
      @param ipPackNum
      @param ipPCID
      @param ipOrderNum
      @param ipPackMode
   */  
export interface POGetDtlList_input{
      /**  Pack Number  */  
   ipPackNum:number,
      /**  PCID  */  
   ipPCID:string,
      /**  Order to get detail from  */  
   ipOrderNum:number,
      /**  Pack Mode  */  
   ipPackMode:string,
}

export interface POGetDtlList_output{
   returnObj:Erp_Tablesets_PackOutTableset[],
parameters : {
      /**  output parameters  */  
   cWarning:string,
}
}

   /** Required : 
      @param ipPackNum
      @param ds
   */  
export interface POGetLegalNumGenOpts_input{
      /**  Packing Slip number  */  
   ipPackNum:number,
   ds:Erp_Tablesets_PackOutTableset[],
}

export interface POGetLegalNumGenOpts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackOutTableset[],
   opPromptForNum:boolean,
}
}

   /** Required : 
      @param ipOrderNum
      @param ipPackNum
      @param ipPCID
      @param ipPackMode
   */  
export interface POGetNewWithDtl_input{
   ipOrderNum:number,
   ipPackNum:number,
   ipPCID:string,
   ipPackMode:string,
}

export interface POGetNewWithDtl_output{
   returnObj:Erp_Tablesets_PackOutTableset[],
parameters : {
      /**  output parameters  */  
   pcWarningMsg:string,
   cWarning:string,
}
}

   /** Required : 
      @param ipOrderNum
      @param ipPackNum
   */  
export interface POGetNew_input{
      /**  Order Number  */  
   ipOrderNum:number,
      /**  Pack Num  */  
   ipPackNum:number,
}

export interface POGetNew_output{
   returnObj:Erp_Tablesets_PackOutTableset[],
parameters : {
      /**  output parameters  */  
   pcWarningMsg:string,
}
}

   /** Required : 
      @param ds
   */  
export interface POGetShipTo_input{
   ds:Erp_Tablesets_PackOutTableset[],
}

export interface POGetShipTo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackOutTableset[],
}
}

   /** Required : 
      @param ipSourceRowID
      @param poLinkValues
      @param currLine
      @param ds
   */  
export interface POUpdateAndDisplay_input{
      /**  RowIdent  */  
   ipSourceRowID:string,
      /**  poLinkValues  */  
   poLinkValues:string,
      /**  Pack Line  */  
   currLine:number,
   ds:Erp_Tablesets_PackOutTableset[],
}

export interface POUpdateAndDisplay_output{
parameters : {
      /**  output parameters  */  
   opPackNum:number,
   ds:Erp_Tablesets_PackOutTableset[],
   dspLegalNumMessage:string,
}
}

   /** Required : 
      @param ipSourceRowID
      @param poLinkValues
      @param ds
   */  
export interface POUpdate_input{
      /**  RowIdent  */  
   ipSourceRowID:string,
      /**  poLinkValues  */  
   poLinkValues:string,
   ds:Erp_Tablesets_PackOutTableset[],
}

export interface POUpdate_output{
parameters : {
      /**  output parameters  */  
   opPackNum:number,
   ds:Erp_Tablesets_PackOutTableset[],
}
}

   /** Required : 
      @param ipPackNum
      @param ipOrderNum
      @param ipOrderLine
      @param ipOrderRelNum
   */  
export interface POValidateOrderRel_input{
   ipPackNum:number,
   ipOrderNum:number,
   ipOrderLine:number,
   ipOrderRelNum:number,
}

export interface POValidateOrderRel_output{
}

   /** Required : 
      @param ipCustNum
      @param ipOrderNum
   */  
export interface POValidateOrder_input{
      /**  Customer Number  */  
   ipCustNum:number,
      /**  Order chose to add to carton  */  
   ipOrderNum:number,
}

export interface POValidateOrder_output{
parameters : {
      /**  output parameters  */  
   opVaildOrder:boolean,
}
}

   /** Required : 
      @param ipPartNum
      @param ipOrderNum
      @param ds
   */  
export interface POValidatePart_input{
      /**  Proposed part number.  */  
   ipPartNum:string,
      /**  Order number.  */  
   ipOrderNum:number,
   ds:Erp_Tablesets_PackOutTableset[],
}

export interface POValidatePart_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackOutTableset[],
   opValidPart:boolean,
   vMsgText:string,
   vSubAvail:boolean,
   vMsgType:string,
}
}

   /** Required : 
      @param ipPackNum
   */  
export interface PackVerifyCalcPackPCIDCount_input{
      /**  ipPackNum  */  
   ipPackNum:number,
}

export interface PackVerifyCalcPackPCIDCount_output{
   returnObj:number,
}

   /** Required : 
      @param ipPackNum
   */  
export interface PackVerifyPerformPackVerification_input{
      /**  The Pack Number for the verification  */  
   ipPackNum:number,
}

export interface PackVerifyPerformPackVerification_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   opErrorMessage:string,
}
}

   /** Required : 
      @param ds
      @param packLine
      @param partNum
   */  
export interface PartNumChangeUserPrompts_input{
   ds:Erp_Tablesets_CustShipTableset[],
      /**  Detail Line Number to update  */  
   packLine:number,
      /**  Proposed PartNumber change  */  
   partNum:string,
}

export interface PartNumChangeUserPrompts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
   serialWarning:string,
   questionString:string,
   idWarning:string,
}
}

   /** Required : 
      @param ipPackNum
   */  
export interface PhantomStatusCheck_input{
   ipPackNum:number,
}

export interface PhantomStatusCheck_output{
}

   /** Required : 
      @param ipPackNum
   */  
export interface PostUpdate_input{
      /**  Customer Shipment Number  */  
   ipPackNum:number,
}

export interface PostUpdate_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param packNum
      @param orderNum
      @param ds
   */  
export interface PreCreateMassShipDtl_input{
      /**  Pack Number to add new shipment lines to  */  
   packNum:number,
      /**  Order Number to create shipment lines from  */  
   orderNum:number,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface PreCreateMassShipDtl_output{
parameters : {
      /**  output parameters  */  
   warnMsg:string,
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface PrePickedOrders_input{
   ds:Erp_Tablesets_CustShipPickedOrdersTableset[],
}

export interface PrePickedOrders_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipPickedOrdersTableset[],
   vMessage:string,
}
}

   /** Required : 
      @param packNum
      @param printPreview
   */  
export interface PrintSlip_input{
      /**  The Packing Slip Number to print  */  
   packNum:number,
      /**  Flag if print should be previewed.  */  
   printPreview:boolean,
}

export interface PrintSlip_output{
}

   /** Required : 
      @param ipOrderNum
      @param ipOrderLine
   */  
export interface ProcessKitChildern_input{
      /**  input order number  */  
   ipOrderNum:number,
      /**  input order line  */  
   ipOrderLine:number,
}

export interface ProcessKitChildern_output{
   returnObj:boolean,
}

export interface ProcessMassShipKit_output{
}

   /** Required : 
      @param ipPackNum
   */  
export interface ProcessNegQtyTest_input{
      /**  current pack number  */  
   ipPackNum:number,
}

export interface ProcessNegQtyTest_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   opWarnMessage:string,
   opAskMessage:string,
   opStopMessage:string,
}
}

   /** Required : 
      @param pConsolidate
      @param skipDelete
      @param ds
   */  
export interface ProcessPickedOrderHH_input{
      /**  Consolidates Orders in a single Carton.  */  
   pConsolidate:boolean,
      /**  Skip Delete? (for testing purposes)  */  
   skipDelete:boolean,
   ds:Erp_Tablesets_CustShipPickedOrdersTableset[],
}

export interface ProcessPickedOrderHH_output{
   returnObj:Erp_Tablesets_ShipHeadListTableset[],
parameters : {
      /**  output parameters  */  
   vMessage:string,
   ds:Erp_Tablesets_CustShipPickedOrdersTableset[],
}
}

   /** Required : 
      @param pConsolidate
      @param skipDelete
      @param ds
   */  
export interface ProcessPickedOrder_input{
      /**  Consolidates Orders in a single Carton.  */  
   pConsolidate:boolean,
      /**  Skip Delete? (for testing purposes)  */  
   skipDelete:boolean,
   ds:Erp_Tablesets_CustShipPickedOrdersTableset[],
}

export interface ProcessPickedOrder_output{
   returnObj:Erp_Tablesets_ShipHeadListTableset[],
parameters : {
      /**  output parameters  */  
   vMessage:string,
   ds:Erp_Tablesets_CustShipPickedOrdersTableset[],
}
}

   /** Required : 
      @param ipPackNum
      @param ds
   */  
export interface RebuildShipUPS_input{
   ipPackNum:number,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface RebuildShipUPS_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ipSource
      @param ipPackNum
      @param ipPCID
      @param ds
   */  
export interface RemovePCID_input{
      /**  ipSource  */  
   ipSource:string,
      /**  ipPackNum  */  
   ipPackNum:number,
      /**  ipPCID  */  
   ipPCID:string,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface RemovePCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
   opPCIDCount:number,
}
}

   /** Required : 
      @param ds
      @param packNum
      @param shipped
      @param firstRun
   */  
export interface SetShippedFromPackout_input{
   ds:Erp_Tablesets_PackOutTableset[],
      /**  Pack Number  */  
   packNum:number,
      /**  Indicates if the shipment is shipped or not  */  
   shipped:boolean,
      /**  Indicates if this is the first run. Will be false if the first run returned messages that required user input and the user chose to continue  */  
   firstRun:boolean,
}

export interface SetShippedFromPackout_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackOutTableset[],
   opReleaseMessage:string,
   opCompleteMessage:string,
   opShippingMessage:string,
   opInventoryMessage:string,
   opLockQtyMessage:string,
   opAllocationMessage:string,
   shipCreditMsg:string,
   cError:boolean,
   msg:string,
   opPostUpdMessage:string,
   updateComplete:boolean,
   checkComplianceError:boolean,
}
}

   /** Required : 
      @param ipQVEnable
      @param ds
   */  
export interface SetUPSQVEnable_input{
   ipQVEnable:boolean,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface SetUPSQVEnable_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ipShipStatus
      @param ds
   */  
export interface SetUPSQVShipStatus_input{
   ipShipStatus:string,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface SetUPSQVShipStatus_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param iPackNum
      @param ipShipmentType
   */  
export interface StageWarning_input{
   iPackNum:number,
   ipShipmentType:string,
}

export interface StageWarning_output{
parameters : {
      /**  output parameters  */  
   iWarning:string,
}
}

   /** Required : 
      @param ds
   */  
export interface UndoShipAll_input{
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface UndoShipAll_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtCustShipTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCustShipTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ipAmountType
      @param ipAction
      @param ds
   */  
export interface UpdateManifestChargeAmts_input{
   ipAmountType:string,
   ipAction:boolean,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface UpdateManifestChargeAmts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
      @param doValidateCreditHold
      @param doCheckShipDtl
      @param doLotValidation
      @param doCheckOrderComplete
      @param doPostUpdate
      @param doCheckCompliance
      @param ipShippedFlagChanged
      @param ipPackNum
      @param ipBTCustNum
   */  
export interface UpdateMaster_input{
   ds:Erp_Tablesets_CustShipTableset[],
   doValidateCreditHold:boolean,
   doCheckShipDtl:boolean,
   doLotValidation:boolean,
   doCheckOrderComplete:boolean,
   doPostUpdate:boolean,
   doCheckCompliance:boolean,
   ipShippedFlagChanged:boolean,
   ipPackNum:number,
   ipBTCustNum:number,
}

export interface UpdateMaster_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
   opReleaseMessage:string,
   opCompleteMessage:string,
   opShippingMessage:string,
   opLotMessage:string,
   opInventoryMessage:string,
   opLockQtyMessage:string,
   opAllocationMessage:string,
   opPartListNeedsAttr:string,
   opLotListNeedsAttr:string,
   shipCreditMsg:string,
   cError:boolean,
   compError:boolean,
   msg:string,
   opPostUpdMessage:string,
   updateComplete:boolean,
   checkComplianceError:boolean,
   changeStatusError:boolean,
   checkShipDtlAgain:boolean,
}
}

   /** Required : 
      @param ipPackNum
      @param ipPackLine
      @param ipOrderRelNum
      @param ds
   */  
export interface UpdateOrderRelOnKitChildren_input{
   ipPackNum:number,
   ipPackLine:number,
   ipOrderRelNum:number,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface UpdateOrderRelOnKitChildren_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ipPackNum
      @param ipCaseNum
      @param ipOldCOD
      @param ipCOD
      @param ipFlag
      @param ds
   */  
export interface UpdatePackCODWithCarton_input{
   ipPackNum:number,
   ipCaseNum:number,
   ipOldCOD:number,
   ipCOD:number,
   ipFlag:boolean,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface UpdatePackCODWithCarton_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ipPackNum
      @param ipCaseNum
      @param ipOldDeclared
      @param ipDeclared
      @param ipDeclaredFlag
      @param ds
   */  
export interface UpdatePackDeclaredWithCarton_input{
   ipPackNum:number,
   ipCaseNum:number,
   ipOldDeclared:number,
   ipDeclared:number,
   ipDeclaredFlag:boolean,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface UpdatePackDeclaredWithCarton_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ipPackNum
      @param ipOldWeight
      @param ipWeight
      @param ds
   */  
export interface UpdatePackWeightWithCarton_input{
   ipPackNum:number,
   ipOldWeight:number,
   ipWeight:number,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface UpdatePackWeightWithCarton_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param ipWhse
      @param ipBinNum
   */  
export interface ValidateBinCode_input{
   ipWhse:string,
   ipBinNum:string,
}

export interface ValidateBinCode_output{
}

   /** Required : 
      @param ipOrderNum
      @param ipPackNum
   */  
export interface ValidateCreditHoldPO_input{
   ipOrderNum:number,
   ipPackNum:number,
}

export interface ValidateCreditHoldPO_output{
parameters : {
      /**  output parameters  */  
   opCreditMessage:string,
   opAgingMessage:string,
}
}

   /** Required : 
      @param ipPackNum
      @param ipShipmentType
   */  
export interface ValidateCreditHoldSSC_input{
   ipPackNum:number,
   ipShipmentType:string,
}

export interface ValidateCreditHoldSSC_output{
parameters : {
      /**  output parameters  */  
   opCreditMessage:string,
   opcError:boolean,
}
}

   /** Required : 
      @param ipValPackNum
      @param ipValBTCustNum
   */  
export interface ValidateCreditHold_input{
   ipValPackNum:number,
   ipValBTCustNum:number,
}

export interface ValidateCreditHold_output{
parameters : {
      /**  output parameters  */  
   opCreditMessage:string,
   opcError:boolean,
}
}

   /** Required : 
      @param packLine
      @param ds
   */  
export interface ValidateKitPart_input{
      /**  Detail Line Number to update  */  
   packLine:number,
   ds:Erp_Tablesets_CustShipTableset[],
}

export interface ValidateKitPart_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipTableset[],
}
}

   /** Required : 
      @param IDNumList
      @param ipPartNum
      @param ipIDNumProposed
      @param ipPackNum
      @param ipPackLine
   */  
export interface ValidateLocationIDNumbers_input{
   IDNumList:string,
   ipPartNum:string,
   ipIDNumProposed:string,
   ipPackNum:number,
   ipPackLine:number,
}

export interface ValidateLocationIDNumbers_output{
}

   /** Required : 
      @param ipPackNum
   */  
export interface ValidatePackNum_input{
   ipPackNum:number,
}

export interface ValidatePackNum_output{
parameters : {
      /**  output parameters  */  
   _success:boolean,
}
}

   /** Required : 
      @param ipSerialNum
      @param ipPartNum
      @param ipAttributeSetID
      @param ipJobNum
      @param ipOurJobshipQty
      @param ipOurInvShipQty
      @param ipOrderNum
      @param ipOrderLine
      @param ipOrderRelNum
      @param ipShipFromWIP
      @param ipWarehouseCode
      @param ipBinNum
   */  
export interface ValidateSN_input{
   ipSerialNum:string,
   ipPartNum:string,
   ipAttributeSetID:number,
   ipJobNum:string,
   ipOurJobshipQty:number,
   ipOurInvShipQty:number,
   ipOrderNum:number,
   ipOrderLine:number,
   ipOrderRelNum:number,
   ipShipFromWIP:boolean,
   ipWarehouseCode:string,
   ipBinNum:string,
}

export interface ValidateSN_output{
parameters : {
      /**  output parameters  */  
   isVoided:boolean,
}
}

   /** Required : 
      @param ipPackNum
      @param ipVoidedReason
   */  
export interface VoidLegalNumber_input{
      /**  Packing Slip number  */  
   ipPackNum:number,
      /**  Reason for the void  */  
   ipVoidedReason:string,
}

export interface VoidLegalNumber_output{
   returnObj:Erp_Tablesets_CustShipTableset[],
}

   /** Required : 
      @param packNum
      @param ds
   */  
export interface VoidPackSlip_input{
   packNum:number,
   ds:Erp_Tablesets_PackageControlPackVoidTableset[],
}

export interface VoidPackSlip_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackageControlPackVoidTableset[],
}
}

