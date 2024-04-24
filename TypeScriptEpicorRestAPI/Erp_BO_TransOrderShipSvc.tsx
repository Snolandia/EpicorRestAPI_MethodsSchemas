import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.TransOrderShipSvc
// Description: TransOrderShipSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/$metadata", {
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
   Description: Get TransOrderShips items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TransOrderShips
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipHeadRow
   */  
export function get_TransOrderShips(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TransOrderShips
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFShipHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TFShipHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TransOrderShips(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TransOrderShip item
   Description: Calls GetByID to retrieve the TransOrderShip item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TransOrderShip
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipHeadRow
   */  
export function get_TransOrderShips_Company_PackNum(Company:string, PackNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TFShipHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TFShipHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TransOrderShip for the service
   Description: Calls UpdateExt to update TransOrderShip. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TransOrderShip
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFShipHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TransOrderShips_Company_PackNum(Company:string, PackNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")", {
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
   Summary: Call UpdateExt to delete TransOrderShip item
   Description: Call UpdateExt to delete TransOrderShip item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TransOrderShip
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TransOrderShips_Company_PackNum(Company:string, PackNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")", {
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
   Description: Get TFShipDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TFShipDtls1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipDtlRow
   */  
export function get_TransOrderShips_Company_PackNum_TFShipDtls(Company:string, PackNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")/TFShipDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TFShipDtl item
   Description: Calls GetByID to retrieve the TFShipDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFShipDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipDtlRow
   */  
export function get_TransOrderShips_Company_PackNum_TFShipDtls_Company_PackNum_PackLine(Company:string, PackNum:string, PackLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TFShipDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")/TFShipDtls(" + Company + "," + PackNum + "," + PackLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TFShipDtlRow)
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
export function get_TransOrderShips_Company_PackNum_CartonTrkDtls(Company:string, PackNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CartonTrkDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")/CartonTrkDtls", {
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
export function get_TransOrderShips_Company_PackNum_CartonTrkDtls_Company_ShipmentType_PackNum_CaseNum(Company:string, PackNum:string, ShipmentType:string, CaseNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CartonTrkDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")/CartonTrkDtls(" + Company + "," + ShipmentType + "," + PackNum + "," + CaseNum + ")", {
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
   Description: Get TFShipHeadInsurances items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TFShipHeadInsurances1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipHeadInsuranceRow
   */  
export function get_TransOrderShips_Company_PackNum_TFShipHeadInsurances(Company:string, PackNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadInsuranceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")/TFShipHeadInsurances", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadInsuranceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TFShipHeadInsurance item
   Description: Calls GetByID to retrieve the TFShipHeadInsurance item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFShipHeadInsurance1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param InsuranceSeq Desc: InsuranceSeq   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipHeadInsuranceRow
   */  
export function get_TransOrderShips_Company_PackNum_TFShipHeadInsurances_Company_PackNum_InsuranceSeq(Company:string, PackNum:string, InsuranceSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TFShipHeadInsuranceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")/TFShipHeadInsurances(" + Company + "," + PackNum + "," + InsuranceSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TFShipHeadInsuranceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get TFShipHeadTrailers items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TFShipHeadTrailers1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipHeadTrailerRow
   */  
export function get_TransOrderShips_Company_PackNum_TFShipHeadTrailers(Company:string, PackNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadTrailerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")/TFShipHeadTrailers", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadTrailerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TFShipHeadTrailer item
   Description: Calls GetByID to retrieve the TFShipHeadTrailer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFShipHeadTrailer1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param LicensePlate Desc: LicensePlate   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipHeadTrailerRow
   */  
export function get_TransOrderShips_Company_PackNum_TFShipHeadTrailers_Company_PackNum_LicensePlate(Company:string, PackNum:string, LicensePlate:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TFShipHeadTrailerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")/TFShipHeadTrailers(" + Company + "," + PackNum + "," + LicensePlate + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TFShipHeadTrailerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get TFShipUPS items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TFShipUPS1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipUPSRow
   */  
export function get_TransOrderShips_Company_PackNum_TFShipUPS(Company:string, PackNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipUPSRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")/TFShipUPS", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipUPSRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TFShipUP item
   Description: Calls GetByID to retrieve the TFShipUP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFShipUP1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipUPSRow
   */  
export function get_TransOrderShips_Company_PackNum_TFShipUPS_Company_PackNum_UPSQVSeq(Company:string, PackNum:string, UPSQVSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TFShipUPSRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")/TFShipUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TFShipUPSRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get TFShipHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TFShipHeadAttches1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipHeadAttchRow
   */  
export function get_TransOrderShips_Company_PackNum_TFShipHeadAttches(Company:string, PackNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")/TFShipHeadAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TFShipHeadAttch item
   Description: Calls GetByID to retrieve the TFShipHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFShipHeadAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipHeadAttchRow
   */  
export function get_TransOrderShips_Company_PackNum_TFShipHeadAttches_Company_PackNum_DrawingSeq(Company:string, PackNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TFShipHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")/TFShipHeadAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TFShipHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get TFShipDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TFShipDtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipDtlRow
   */  
export function get_TFShipDtls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TFShipDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFShipDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TFShipDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TFShipDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TFShipDtl item
   Description: Calls GetByID to retrieve the TFShipDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFShipDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipDtlRow
   */  
export function get_TFShipDtls_Company_PackNum_PackLine(Company:string, PackNum:string, PackLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TFShipDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipDtls(" + Company + "," + PackNum + "," + PackLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TFShipDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TFShipDtl for the service
   Description: Calls UpdateExt to update TFShipDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TFShipDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFShipDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TFShipDtls_Company_PackNum_PackLine(Company:string, PackNum:string, PackLine:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipDtls(" + Company + "," + PackNum + "," + PackLine + ")", {
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
   Summary: Call UpdateExt to delete TFShipDtl item
   Description: Call UpdateExt to delete TFShipDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TFShipDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TFShipDtls_Company_PackNum_PackLine(Company:string, PackNum:string, PackLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipDtls(" + Company + "," + PackNum + "," + PackLine + ")", {
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
export function get_TFShipDtls_Company_PackNum_PackLine_ShipCOOs(Company:string, PackNum:string, PackLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipCOORow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipDtls(" + Company + "," + PackNum + "," + PackLine + ")/ShipCOOs", {
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
export function get_TFShipDtls_Company_PackNum_PackLine_ShipCOOs_Company_RelatedToFile_PackNum_PackLine_OrigCountry(Company:string, PackNum:string, PackLine:string, RelatedToFile:string, OrigCountry:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipCOORow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipDtls(" + Company + "," + PackNum + "," + PackLine + ")/ShipCOOs(" + Company + "," + RelatedToFile + "," + PackNum + "," + PackLine + "," + OrigCountry + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ShipCOOs", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ShipCOOs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ShipCOOs(" + Company + "," + RelatedToFile + "," + PackNum + "," + PackLine + "," + OrigCountry + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ShipCOOs(" + Company + "," + RelatedToFile + "," + PackNum + "," + PackLine + "," + OrigCountry + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ShipCOOs(" + Company + "," + RelatedToFile + "," + PackNum + "," + PackLine + "," + OrigCountry + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CartonTrkDtls", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CartonTrkDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CartonTrkDtls(" + Company + "," + ShipmentType + "," + PackNum + "," + CaseNum + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CartonTrkDtls(" + Company + "," + ShipmentType + "," + PackNum + "," + CaseNum + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CartonTrkDtls(" + Company + "," + ShipmentType + "," + PackNum + "," + CaseNum + ")", {
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
   Description: Get TFShipHeadInsurances items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TFShipHeadInsurances
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipHeadInsuranceRow
   */  
export function get_TFShipHeadInsurances(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadInsuranceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadInsurances", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadInsuranceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TFShipHeadInsurances
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFShipHeadInsuranceRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TFShipHeadInsuranceRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TFShipHeadInsurances(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadInsurances", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TFShipHeadInsurance item
   Description: Calls GetByID to retrieve the TFShipHeadInsurance item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFShipHeadInsurance
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param InsuranceSeq Desc: InsuranceSeq   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipHeadInsuranceRow
   */  
export function get_TFShipHeadInsurances_Company_PackNum_InsuranceSeq(Company:string, PackNum:string, InsuranceSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TFShipHeadInsuranceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadInsurances(" + Company + "," + PackNum + "," + InsuranceSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TFShipHeadInsuranceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TFShipHeadInsurance for the service
   Description: Calls UpdateExt to update TFShipHeadInsurance. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TFShipHeadInsurance
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param InsuranceSeq Desc: InsuranceSeq   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFShipHeadInsuranceRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TFShipHeadInsurances_Company_PackNum_InsuranceSeq(Company:string, PackNum:string, InsuranceSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadInsurances(" + Company + "," + PackNum + "," + InsuranceSeq + ")", {
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
   Summary: Call UpdateExt to delete TFShipHeadInsurance item
   Description: Call UpdateExt to delete TFShipHeadInsurance item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TFShipHeadInsurance
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param InsuranceSeq Desc: InsuranceSeq   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TFShipHeadInsurances_Company_PackNum_InsuranceSeq(Company:string, PackNum:string, InsuranceSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadInsurances(" + Company + "," + PackNum + "," + InsuranceSeq + ")", {
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
   Description: Get TFShipHeadTrailers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TFShipHeadTrailers
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipHeadTrailerRow
   */  
export function get_TFShipHeadTrailers(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadTrailerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadTrailers", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadTrailerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TFShipHeadTrailers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFShipHeadTrailerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TFShipHeadTrailerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TFShipHeadTrailers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadTrailers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TFShipHeadTrailer item
   Description: Calls GetByID to retrieve the TFShipHeadTrailer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFShipHeadTrailer
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param LicensePlate Desc: LicensePlate   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipHeadTrailerRow
   */  
export function get_TFShipHeadTrailers_Company_PackNum_LicensePlate(Company:string, PackNum:string, LicensePlate:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TFShipHeadTrailerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadTrailers(" + Company + "," + PackNum + "," + LicensePlate + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TFShipHeadTrailerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TFShipHeadTrailer for the service
   Description: Calls UpdateExt to update TFShipHeadTrailer. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TFShipHeadTrailer
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param LicensePlate Desc: LicensePlate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFShipHeadTrailerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TFShipHeadTrailers_Company_PackNum_LicensePlate(Company:string, PackNum:string, LicensePlate:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadTrailers(" + Company + "," + PackNum + "," + LicensePlate + ")", {
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
   Summary: Call UpdateExt to delete TFShipHeadTrailer item
   Description: Call UpdateExt to delete TFShipHeadTrailer item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TFShipHeadTrailer
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param LicensePlate Desc: LicensePlate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TFShipHeadTrailers_Company_PackNum_LicensePlate(Company:string, PackNum:string, LicensePlate:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadTrailers(" + Company + "," + PackNum + "," + LicensePlate + ")", {
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
   Description: Get TFShipUPS items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TFShipUPS
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipUPSRow
   */  
export function get_TFShipUPS(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipUPSRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipUPS", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipUPSRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TFShipUPS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFShipUPSRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TFShipUPSRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TFShipUPS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipUPS", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TFShipUP item
   Description: Calls GetByID to retrieve the TFShipUP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFShipUP
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipUPSRow
   */  
export function get_TFShipUPS_Company_PackNum_UPSQVSeq(Company:string, PackNum:string, UPSQVSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TFShipUPSRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TFShipUPSRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TFShipUP for the service
   Description: Calls UpdateExt to update TFShipUP. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TFShipUP
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFShipUPSRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TFShipUPS_Company_PackNum_UPSQVSeq(Company:string, PackNum:string, UPSQVSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")", {
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
   Summary: Call UpdateExt to delete TFShipUP item
   Description: Call UpdateExt to delete TFShipUP item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TFShipUP
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TFShipUPS_Company_PackNum_UPSQVSeq(Company:string, PackNum:string, UPSQVSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")", {
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
   Description: Get TFShipHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TFShipHeadAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipHeadAttchRow
   */  
export function get_TFShipHeadAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TFShipHeadAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFShipHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TFShipHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TFShipHeadAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TFShipHeadAttch item
   Description: Calls GetByID to retrieve the TFShipHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFShipHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipHeadAttchRow
   */  
export function get_TFShipHeadAttches_Company_PackNum_DrawingSeq(Company:string, PackNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TFShipHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TFShipHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TFShipHeadAttch for the service
   Description: Calls UpdateExt to update TFShipHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TFShipHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFShipHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TFShipHeadAttches_Company_PackNum_DrawingSeq(Company:string, PackNum:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete TFShipHeadAttch item
   Description: Call UpdateExt to delete TFShipHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TFShipHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TFShipHeadAttches_Company_PackNum_DrawingSeq(Company:string, PackNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/LegalNumGenOpts", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/LegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/SelectedSerialNumbers", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/SelectedSerialNumbers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/SNFormats", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/SNFormats", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseTFShipHead:string, whereClauseTFShipHeadAttch:string, whereClauseTFShipDtl:string, whereClauseShipCOO:string, whereClauseCartonTrkDtl:string, whereClauseTFShipHeadInsurance:string, whereClauseTFShipHeadTrailer:string, whereClauseTFShipUPS:string, whereClauseLegalNumGenOpts:string, whereClauseSelectedSerialNumbers:string, whereClauseSNFormat:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseTFShipHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTFShipHead=" + whereClauseTFShipHead
   }
   if(typeof whereClauseTFShipHeadAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTFShipHeadAttch=" + whereClauseTFShipHeadAttch
   }
   if(typeof whereClauseTFShipDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTFShipDtl=" + whereClauseTFShipDtl
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
   if(typeof whereClauseCartonTrkDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCartonTrkDtl=" + whereClauseCartonTrkDtl
   }
   if(typeof whereClauseTFShipHeadInsurance!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTFShipHeadInsurance=" + whereClauseTFShipHeadInsurance
   }
   if(typeof whereClauseTFShipHeadTrailer!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTFShipHeadTrailer=" + whereClauseTFShipHeadTrailer
   }
   if(typeof whereClauseTFShipUPS!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTFShipUPS=" + whereClauseTFShipUPS
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetRows" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetList" + params, {
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
   Summary: Invoke method ExpireDate
   Description: ExpireDate
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ExpireDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CallsCreateCustomerCartons", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CreateCustomerCartons", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CartonValidateWeight", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/DeletePhantomPacks", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/DeleteRangePhantomPacks", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetCartonPackaging", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/UpdatePackWeightWithCarton", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/UpdatePackCODWithCarton", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/UpdatePackDeclaredWithCarton", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CheckValidCartonWeight", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Assigns a legal number to the subcontract shipment.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/AssignLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: calculate the weight of a carton based upon Part.Weight.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CalculateWeight", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePackOutLotNum
   Description: This methods validates PackOut.LotNum field
   OperationID: ChangePackOutLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePackOutLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePackOutLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePackOutLotNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ChangePackOutLotNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ChangeStatus", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTFOrdDtlLotNum
   Description: This methods creates PartLot record if criteria is met in CheckTFOrdDtlLotNum
This method should run when the TFOrdDtl.LotNum field changes AND
after the running of CheckTFOrdDtlLotNum (which potentially returns questions/errors).
   OperationID: ChangeTFOrdDtlLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFOrdDtlLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFOrdDtlLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTFOrdDtlLotNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ChangeTFOrdDtlLotNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTFOrdDtlOurStockQty
   Description: This methods updates fields associated with TFOrdDtl.OurStockQty.
This method should run when the TFOrdDtl.DisplayShipQty field changes.
   OperationID: ChangeTFOrdDtlOurStockQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFOrdDtlOurStockQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFOrdDtlOurStockQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTFOrdDtlOurStockQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ChangeTFOrdDtlOurStockQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTFOrdDtlOurStockQtyUOM
   Description: This methods updates fields associated with TFOrdDtl.OurStockQty.
This method should run when the TFOrdDtl.SellingQtyUOM field changes.
   OperationID: ChangeTFOrdDtlOurStockQtyUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFOrdDtlOurStockQtyUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFOrdDtlOurStockQtyUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTFOrdDtlOurStockQtyUOM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ChangeTFOrdDtlOurStockQtyUOM", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTFOrdDtlPartNum
   Description: This method defaults fields associated with the partnum.
This method should run when the TFOrdDtl.PartNum field changes.
   OperationID: ChangeTFOrdDtlPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFOrdDtlPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFOrdDtlPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTFOrdDtlPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ChangeTFOrdDtlPartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTFOrdDtlWarehouseCode
   Description: This methods updates fields associated with TFOrdDtl.WarehouseCode.
This method should run when the TFOrdDtl.WarehouseCode field changes.
   OperationID: ChangeTFOrdDtlWarehouseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFOrdDtlWarehouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFOrdDtlWarehouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTFOrdDtlWarehouseCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ChangeTFOrdDtlWarehouseCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTFShipDtlLotNum
   Description: This methods creates PartLot record if criteria is met in CheckTFShipDtlLotNum
This method should run when the TFShipDtl.LotNum field changes AND
after the running of CheckTFShipDtlLotNum (which potentially returns questions/errors).
   OperationID: ChangeTFShipDtlLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFShipDtlLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFShipDtlLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTFShipDtlLotNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ChangeTFShipDtlLotNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTFShipDtlOurStockShippedQty
   Description: This methods updates fields associated with TFShipDtl.OurStockShippedQty.
This method should run when the TFShipDtl.DisplayShipQty field changes.
   OperationID: ChangeTFShipDtlOurStockShippedQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFShipDtlOurStockShippedQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFShipDtlOurStockShippedQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTFShipDtlOurStockShippedQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ChangeTFShipDtlOurStockShippedQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTFShipDtlPartNum
   Description: This method defaults fields associated with the partnum.
This method should run when the TFShipDtl.PartNum field changes.
   OperationID: ChangeTFShipDtlPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFShipDtlPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFShipDtlPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTFShipDtlPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ChangeTFShipDtlPartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTFShipDtlTFOrderLine
   Description: This methods updates TFShipDtl.ShippedQty if criteria is met in CheckTFShipDtlTFOrderLine
This method should run when the TFShipDtl.TFOrdLine field changes AND
after the running of CheckTFShipDtlTFOrderline (which potentially returns errors).
   OperationID: ChangeTFShipDtlTFOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFShipDtlTFOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFShipDtlTFOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTFShipDtlTFOrderLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ChangeTFShipDtlTFOrderLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTFShipDtlTFOrderNum
   Description: This methods validates the TFShipDtl.TFOrdNum field and updates associated fields.
This method should run when the TFShipDtl.TFOrdNum field changes.
   OperationID: ChangeTFShipDtlTFOrderNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFShipDtlTFOrderNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFShipDtlTFOrderNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTFShipDtlTFOrderNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ChangeTFShipDtlTFOrderNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTFShipDtlWarehouseCode
   Description: This methods updates fields associated with TFShipDtl.WarehouseCode.
This method should run when the TFShipDtl.WarehouseCode field changes.
   OperationID: ChangeTFShipDtlWarehouseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFShipDtlWarehouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFShipDtlWarehouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTFShipDtlWarehouseCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ChangeTFShipDtlWarehouseCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingTFShipDtlNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new tran qty
   OperationID: OnChangingTFShipDtlNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingTFShipDtlNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingTFShipDtlNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingTFShipDtlNumberOfPieces(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/OnChangingTFShipDtlNumberOfPieces", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingTFShipDtlAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangingTFShipDtlAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingTFShipDtlAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingTFShipDtlAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingTFShipDtlAttributeSet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/OnChangingTFShipDtlAttributeSet", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingTFOrdDtlNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new tran qty
   OperationID: OnChangingTFOrdDtlNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingTFOrdDtlNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingTFOrdDtlNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingTFOrdDtlNumberOfPieces(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/OnChangingTFOrdDtlNumberOfPieces", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingTFOrdDtlAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangingTFOrdDtlAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingTFOrdDtlAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingTFOrdDtlAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingTFOrdDtlAttributeSet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/OnChangingTFOrdDtlAttributeSet", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method TFShipDtl_OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: TFShipDtl_OnChangingRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TFShipDtl_OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TFShipDtl_OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TFShipDtl_OnChangingRevisionNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipDtl_OnChangingRevisionNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method TFOrdDtl_OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: TFOrdDtl_OnChangingRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TFOrdDtl_OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TFOrdDtl_OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TFOrdDtl_OnChangingRevisionNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFOrdDtl_OnChangingRevisionNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/OnChangeShipViaCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: This method should be called before the user can exit the TF Order in the UI to ensure that
the Quantity and Value Percents defined for Country of Origin records equal 100.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CheckCOOPercents", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckDirectOrderLine
   Description: This method is to be run before the CreateDirectOrderLine. Any message returned
needs to be displayed to the user.  If they answer no to any the messages
then don't run the CreateDirectOrderLine method.
   OperationID: CheckDirectOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDirectOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDirectOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDirectOrderLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CheckDirectOrderLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckOHQ
   Description: This method is to be run before the CreateDirectOrderLine check the on hand
quantity of the part.  It will return a message in inventoryMessage if the
on hand quantity is less than zero.  If inventory message isn't null, then
it needs to be displayed to the user.  If they answer no to the question
then don't run the CreateDirectOrderLine method.
   OperationID: CheckOHQ
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckOHQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOHQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckOHQ(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CheckOHQ", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPackOutBinNum
   Description: This methods validates PackOut.BinNum field
   OperationID: CheckPackOutBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPackOutBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackOutBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPackOutBinNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CheckPackOutBinNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPackOutLotNum
   Description: This methods validates PackOut.LotNum field
   OperationID: CheckPackOutLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPackOutLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackOutLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPackOutLotNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CheckPackOutLotNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPackOutOrderLine
   Description: This methods validates PackOut.OrderLine field
   OperationID: CheckPackOutOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPackOutOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackOutOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPackOutOrderLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CheckPackOutOrderLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPackOutPartNum
   Description: This methods validates PackOut.PartNum field
   OperationID: CheckPackOutPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPackOutPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackOutPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPackOutPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CheckPackOutPartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPackOutTFOrdNum
   Description: This methods validates PackOut.TFOrdNum field
   OperationID: CheckPackOutTFOrdNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPackOutTFOrdNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackOutTFOrdNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPackOutTFOrdNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CheckPackOutTFOrdNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPackOutWarehousecode
   Description: This methods validates PackOut.Warehousecode field
   OperationID: CheckPackOutWarehousecode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPackOutWarehousecode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackOutWarehousecode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPackOutWarehousecode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CheckPackOutWarehousecode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: This method checks to see if there are any questions or issues with the part entered
and returns a message, a part number and if any substitutes exist.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CheckPrePartInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckTFOrdDtlLotNum
   Description: This method checks to see if there are any questions or issues with the lotnum entered
and returns a message, run this before ChangeTFOrdDtlLotNum
   OperationID: CheckTFOrdDtlLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTFOrdDtlLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTFOrdDtlLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckTFOrdDtlLotNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CheckTFOrdDtlLotNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckTFShipDtl
   Description: This method is to be run before update to ask the user any question that need to be
answered before the record(s) can be saved.  If the user answers no to any one of
the questions, then the update method should not be called.
   OperationID: CheckTFShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTFShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTFShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckTFShipDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CheckTFShipDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckTFShipDtlLotNum
   Description: This method checks to see if there are any questions or issues with the lotnum entered
and returns a message, run this before ChangeTFShipDtlLotNum
   OperationID: CheckTFShipDtlLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTFShipDtlLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTFShipDtlLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckTFShipDtlLotNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CheckTFShipDtlLotNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckTFShipDtlTFOrderLine
   Description: This method validates the TFShipDtl.TFOrdLine and returns potential errors.
Run this before running ChangeTFShipDtl.TFOrdLine.
   OperationID: CheckTFShipDtlTFOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTFShipDtlTFOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTFShipDtlTFOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckTFShipDtlTFOrderLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CheckTFShipDtlTFOrderLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ClearConvertedManifest
   Description: Purpose: Clear TFShipHead Manifest fields when Unfreighting.
<param name="ipPackNum">Pack Num to clear Manifest fields</param>
Notes:
   OperationID: ClearConvertedManifest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearConvertedManifest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearConvertedManifest_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClearConvertedManifest(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ClearConvertedManifest", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Purpose: Populate TFShipHead Manifest fields.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ConvertToManifestUOM", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ConvertUOM", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateDirectOrder
   Description: This method takes the the TranDirectOrder dataset and create the Transfer Order
Header records.  It will also create and send back a new TFShipHed record for the
UI to update.  The GetNewDirectOrder method must be called first.
   OperationID: CreateDirectOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateDirectOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateDirectOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateDirectOrder(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CreateDirectOrder", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateDirectOrderLine
   Description: This method takes the TranDirectOrder dataset and creates the Transfer Order
Detail record.  It will also create and send back a new TFShipDtl record for the
UI to update.  The GetNewDirectOrderLine method must be called first.
The update method to create the TFShipHed record must also be run before
GetNewDirectOrderLine is called.
   OperationID: CreateDirectOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateDirectOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateDirectOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateDirectOrderLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CreateDirectOrderLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: This methods creates TFShipDtl records based on the quantities remaining to be
shipped from the transfer order.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CreateMassShipDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDirectOrderDS
   Description: This method takes the direct transfer order number tied to the packing slip
and returns the full Direct Order Dataset
   OperationID: GetDirectOrderDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDirectOrderDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDirectOrderDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDirectOrderDS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetDirectOrderDS", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDirectShipDate
   Description: Sets the transfer ship date base on fromplant, toplant, and needbydate.
It's calculated using the needby date and subtracting the transfers days
held in the PltTranDef Table.  To be called when the TFOrdDtl.NeedByDate changes
   OperationID: GetDirectShipDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDirectShipDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDirectShipDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDirectShipDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetDirectShipDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetLegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDirectOrder
   Description: This method creates the default empty Transfer Order Header for the user to update
before calling the CreateShipmentDirectOrder (update Order, new Shipment)
   OperationID: GetNewDirectOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDirectOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDirectOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDirectOrder(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetNewDirectOrder", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDirectOrderLine
   Description: This method creates an empty Transfer Order Detail record for the user to update
before calling the CreateShipmentDirectOrderLine (update TFOrdDtl, new TFShipDtl)
This method replaces the GetNewShipDtl method for Direct Order Shipments
The TFOrdHed record is sent back as well for constraint reasons
   OperationID: GetNewDirectOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDirectOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDirectOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDirectOrderLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetNewDirectOrderLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewFromOrder
   Description: This methods creates a new packing slip with header information pulled from
the transfer order header.
   OperationID: GetNewFromOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFromOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFromOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFromOrder(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetNewFromOrder", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewFromOrderWithPCID
   Description: This methods creates a new packing slip with header information pulled from
the transfer order header, preventing its execution when the transfer order have allocations with PCID.
   OperationID: GetNewFromOrderWithPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFromOrderWithPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFromOrderWithPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFromOrderWithPCID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetNewFromOrderWithPCID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
Parameters:
<param name="ipPkgCode">package code</param><param name="ds">Transfer Shipment data set</param>
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetPackaging", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
Parameters:
<param name="ipPkgClass">package class</param><param name="ds">Transfer Order Shipment data set</param>
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetPackClass", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
Parameters:
<param name="ds">The transfer order data set</param>
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetPayBTFlagDefaults", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
Parameters:
<param name="ipPkgCode">package code</param><param name="ds">Transfer PackOut data set</param>
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetPOPackaging", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
Parameters:
<param name="ipPkgClass">package class</param><param name="ds">Packout data set</param>
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetPOPackClass", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePOPartNum
   Description: Call this method when changing the packout part to maintain inventory tracking
   OperationID: ChangePOPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePOPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePOPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePOPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ChangePOPartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePORevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: ChangePORevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePORevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePORevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePORevisionNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ChangePORevisionNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetScale", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetSelectSerialNumbersParams", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetTranDocTypeID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetShipCOOTotals
   Description: Calculate Company of Origins totals in current tableset for certain Transfer Order Line.
The method is used in clients which don't have possibility to calculate it (in example Kinetic form)
   OperationID: GetShipCOOTotals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShipCOOTotals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShipCOOTotals_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetShipCOOTotals(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetShipCOOTotals", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: This method will be called to perform a change in the header status for the Pack Out screen.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/POChangeStatus", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method POCreateDtlList
   Description: This method copies the available Order Release lines to the PackOut datatable
for update
   OperationID: POCreateDtlList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POCreateDtlList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POCreateDtlList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POCreateDtlList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/POCreateDtlList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/POFindBuffer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: This method copies the available Carton Dtl lines to the PackOut datatable
for update
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/POGetDtlList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/POGetNewWithDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetDisablePackOut", {
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
   Summary: Invoke method POGetNew
   Description: This method creates a new packout record for the customer shipment packout
screen
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/POGetNew", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method POUndo
   Description: This methods simulates Undo.
   OperationID: POUndo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POUndo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POUndo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POUndo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/POUndo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: This method creates a new packout record to create TFShiphed and TFShipDtl records
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/POUpdate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method POUpdateHeader
   Description: This methods simulates Undo.
   OperationID: POUpdateHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POUpdateHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POUpdateHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POUpdateHeader(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/POUpdateHeader", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreDeleteDirectShip
   Description: This method needs to be called before deleting line items.  It asks the
user if they want to delete the TFOrdDtl as well as the TFShipDtl.
   OperationID: PreDeleteDirectShip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreDeleteDirectShip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreDeleteDirectShip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreDeleteDirectShip(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/PreDeleteDirectShip", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreDeselectSN
   Description: Sets PreDeselected before delete a TFOrdShipLine.
   OperationID: PreDeselectSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreDeselectSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreDeselectSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreDeselectSN(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/PreDeselectSN", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
Parameters:
<param name="ipQVEnable">logical indicating if the quantum view is to enabled/disabled</param><param name="ds">The transfer order data set</param>
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/SetUPSQVEnable", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
Parameters:
<param name="ipShipStatus">Shipment status</param><param name="ds">The transfer shipment data set</param>
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/SetUPSQVShipStatus", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreShipPack
   Description: Procedure to check in attribute sets are needed and valid.
If so, the transfer order shipment cannot be shipped
   OperationID: PreShipPack
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreShipPack_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreShipPack_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreShipPack(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/PreShipPack", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method EADValidation
   Description: Validate Ship Date is not before the Earliest Apply Date.
   OperationID: EADValidation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EADValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EADValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EADValidation(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/EADValidation", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ShipPackingSlip
   Description: This methods assigns the TFShipHead.Shipped field and updates/creates all of the
associated records (partbin, parttran, TFOrdHed, etc.) when a Packing Slip is shipped.
   OperationID: ShipPackingSlip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ShipPackingSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ShipPackingSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ShipPackingSlip(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ShipPackingSlip", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreUnShipPack
   Description: Procedure to know if the order or at least one line was already received in the target plant.
If so, the transfer order shipment cannot be unshipped
   OperationID: PreUnShipPack
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUnShipPack_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUnShipPack_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreUnShipPack(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/PreUnShipPack", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnShipPackingSlip
   Description: This methods assigns the TFShipHead.Shipped field and updates/deletes all of the
associated records (parttran) when a Packing Slip is unshipped. Also potentially creates
partbin and partdtl records.
   OperationID: UnShipPackingSlip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnShipPackingSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnShipPackingSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnShipPackingSlip(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/UnShipPackingSlip", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ValidateBinCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePartNum
   Description: Purpose: This method is to be called when the Part Number field changes
<param name="ipPartNum">Part Number</param>
   OperationID: ValidatePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ValidatePartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ValidateSN", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/VoidLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method WarnNegativeBinOH
   OperationID: WarnNegativeBinOH
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WarnNegativeBinOH_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WarnNegativeBinOH_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WarnNegativeBinOH(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/WarnNegativeBinOH", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method WarnNegativeBinQty
   Description: Procedure used to warn if negative inventory in Bin.
   OperationID: WarnNegativeBinQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WarnNegativeBinQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WarnNegativeBinQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WarnNegativeBinQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/WarnNegativeBinQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method WarnNegativeLotOH
   OperationID: WarnNegativeLotOH
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WarnNegativeLotOH_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WarnNegativeLotOH_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WarnNegativeLotOH(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/WarnNegativeLotOH", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsSerialTracked
   Description: Purpose:  Returns true only if ipPart is serial tracked, and the Plant owning
ipWhse has full serial tracking enabled.
   OperationID: IsSerialTracked
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsSerialTracked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsSerialTracked_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsSerialTracked(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/IsSerialTracked", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetAvailTranDocTypes", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GenerateDigitalSignature", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetEnablePackageControl", {
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
   Summary: Invoke method ChangePCID
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ChangePCID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTFShipHeadTFOrdNum
   OperationID: ChangeTFShipHeadTFOrdNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFShipHeadTFOrdNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFShipHeadTFOrdNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTFShipHeadTFOrdNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ChangeTFShipHeadTFOrdNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/RemovePCID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTFShipHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFShipHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTFShipHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFShipHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTFShipHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetNewTFShipHead", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTFShipHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFShipHeadAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTFShipHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFShipHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTFShipHeadAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetNewTFShipHeadAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTFShipDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTFShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTFShipDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetNewTFShipDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetNewShipCOO", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetNewCartonTrkDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTFShipHeadInsurance
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFShipHeadInsurance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTFShipHeadInsurance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFShipHeadInsurance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTFShipHeadInsurance(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetNewTFShipHeadInsurance", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTFShipHeadTrailer
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFShipHeadTrailer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTFShipHeadTrailer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFShipHeadTrailer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTFShipHeadTrailer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetNewTFShipHeadTrailer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTFShipUPS
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFShipUPS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTFShipUPS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFShipUPS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTFShipUPS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetNewTFShipUPS", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SNFormatRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SelectedSerialNumbersRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipCOORow{
   "odatametadata":string,
   "value":Erp_Tablesets_ShipCOORow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TFShipDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TFShipHeadAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadInsuranceRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TFShipHeadInsuranceRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TFShipHeadListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TFShipHeadRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadTrailerRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TFShipHeadTrailerRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipUPSRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TFShipUPSRow[],
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

export interface Erp_Tablesets_TFShipDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Packing slip number that this detail record is linked with.  */  
   "PackNum":number,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  */  
   "PackLine":number,
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
      /**  Weight Unit of measure...qualifies the weight field value. (Lb, Oz, Gr...).  */  
   "NetWeightUOM":string,
      /**  Lot Number is defaulted as Job Number.  */  
   "LotNum":string,
      /**  The Part's Net Weight * (SellingJobShipQty + SellingInventoryShipQty)  */  
   "TotalNetWeight":number,
      /**   Identifies the warehouse for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area warehouse (Site.DefShipWhse) otherwise it's blank.  */  
   "WIPWarehouseCode":string,
      /**   Identifies the warehouse bin for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area bin (Site.DefShipBin) otherwise it's blank.  */  
   "WIPBinNum":string,
      /**  This field along with Company and TFOrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   "TFOrdLine":number,
      /**  Quantity ,using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   "OurStockQty":number,
      /**  Actual quantity ,using Our U/M, shipped from Stock.  Updated via the shipping process.  */  
   "OurStockShippedQty":number,
      /**  requestdate  */  
   "requestdate":string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   "TFOrdNum":string,
      /**  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  */  
   "TFLineNum":string,
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
      /**  Calculated price for the item being transferred.  */  
   "UnitPrice":number,
      /**  Unit Price.  */  
   "DocUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitPrice":number,
      /**  Quantity picked from inventory that was not manually allocated. This quantity is automatically added to PartAlloc such when inventory is picked, it is considered allocated to this Transfer Order.  This quantity is in the IUM unit of measure.  */  
   "PickedAutoAllocatedQty":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PCID  */  
   "PCID":string,
      /**  If AMM is licensed this column will hold how much of this shipment was allocated prior to the shipment in case this shipment is ever "unshipped"  */  
   "AllocatedShippedQty":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
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
      /**  Are there available serial numbers?  */  
   "AvailSerialNumbers":boolean,
      /**  direct-transfer  */  
   "direct_transfer":boolean,
      /**  OurStockShippedQty * DimConvFactor  */  
   "DisplayShipQty":number,
      /**  Indicates if the Shipment line has been shipped  */  
   "LineShipped":boolean,
      /**  Current Shipment in OrderUOM  */  
   "OrderShipmentQty":number,
      /**  UOM from Transfer Order  */  
   "OrderUOM":string,
      /**  Used by the freight web service  */  
   "PartAESExp":string,
      /**  Used by the freight web service  */  
   "PartECNNumber":string,
      /**  Used by freight web service  */  
   "PartExpLicNumber":string,
      /**  used by freight web service  */  
   "PartExpLicType":string,
      /**  Used by the freight web service  */  
   "PartHazClass":string,
      /**  Used by the freight web service  */  
   "PartHazGvrnmtID":string,
      /**  Used by the freight web service  */  
   "PartHazItem":boolean,
      /**  Used by the freight web service  */  
   "PartHazPackInstr":string,
      /**  Used by the freight web service  */  
   "PartHazSub":string,
      /**  Used by the freight web service  */  
   "PartHazTechName":string,
      /**  Used by the freight web service  */  
   "PartHTS":string,
      /**  Used by the freight web service  */  
   "PartNAFTAOrigCountry":string,
      /**  Used by the freight web service  */  
   "PartNAFTAPref":string,
      /**  Used by the freight web service  */  
   "PartNAFTAProd":string,
      /**  Used by the freight web service  */  
   "PartOrigCountry":string,
      /**  Used by the freight web service  */  
   "PartSchedBcode":string,
      /**  Used by the freight web service  */  
   "PartUseHTSDesc":boolean,
      /**  Indicates if the Shipment line has been received  */  
   "Received":boolean,
      /**  The remaining quantity  */  
   "RemainingQty":number,
      /**  The request quantity  */  
   "RequestQty":number,
      /**  The shipped quantity  */  
   "ShippedQty":number,
      /**  Ship Status of the Transfer Order Shipment line, copied from the Transfer Order Shipment header.  */  
   "ShipStatus":string,
      /**  Currency Code  */  
   "CurrencyCode":string,
      /**  Enable Attribute Set Search  */  
   "EnableAttributeSetSearch":boolean,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   "DispNumberOfPieces":number,
   "BitFlag":number,
   "DynAttrValueSetDescription":string,
   "DynAttrValueSetShortDescription":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumPricePerCode":string,
   "PartNumPartDescription":string,
   "PartNumIUM":string,
   "PartNumSalesUM":string,
   "PartNumSellingFactor":number,
   "PartNumTrackLots":boolean,
   "PartNumAttrClassID":string,
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TFShipHeadAttchRow{
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

export interface Erp_Tablesets_TFShipHeadInsuranceRow{
      /**  Company  */  
   "Company":string,
      /**  PackNum  */  
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

export interface Erp_Tablesets_TFShipHeadListRow{
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
      /**  The Site that shipment was made from.  */  
   "Plant":string,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   "TrackingNumber":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  */  
   "ExternalDeliveryNote":boolean,
      /**  External  ID  */  
   "ExternalID":string,
      /**  directtransfer  */  
   "directtransfer":boolean,
      /**  Site Identifier.  This field cannot be blank.  */  
   "ToPlant":string,
      /**  Shipped flag  */  
   "Shipped":boolean,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  Is a Saturday delivery acceptable  */  
   "SatDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
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
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   "ShipStatus":string,
      /**  Group the shipment belongs to for "Staging"  */  
   "ShipGroup":string,
      /**  Package Weight  */  
   "Weight":number,
      /**  Package Code  */  
   "PkgCode":string,
      /**  NMFC Packaging Classification code.  */  
   "PkgClass":string,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
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
      /**  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  */  
   "BinNum":string,
      /**  Bill of Lading Number the packing slip is linked to  */  
   "BOLNum":number,
      /**  Added for international shipping, Is a commercial invoice required  */  
   "CommercialInvoice":boolean,
      /**  Bill of Lading line number linked to  */  
   "BOLLine":number,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   "ShipExprtDeclartn":boolean,
      /**  For International shipping.  Certificate of Orgin required.  */  
   "CertOfOrigin":boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   "LetterOfInstr":boolean,
      /**  International Shipping - HazardousShipment  */  
   "HazardousShipment":boolean,
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
      /**  International Shipping. Frieght Forwarder ID  */  
   "FFID":string,
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
      /**  Is this an International shipment  */  
   "IntrntlShip":boolean,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   "IndividualPackIDs":boolean,
      /**  Freight Forwarder Third address line  */  
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
      /**  UPS Quantum View Ship from Name  */  
   "UPSQVShipFromName":string,
      /**  UPS Quantum View Memo  */  
   "UPSQVMemo":string,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   "PkgLength":number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   "PkgWidth":number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   "PkgHeight":number,
      /**  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  */  
   "PhantomPack":boolean,
      /**   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   "PkgSizeUOM":string,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   "WeightUOM":string,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Indicates if the document has been printed.  */  
   "DocumentPrinted":boolean,
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
      /**  Indicates the inventory warehouse in the ShipTo Site.  */  
   "WarehouseCode":string,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Display for the Ship From Address  */  
   "DspFromAddr":string,
      /**  Display for the Ship To Address  */  
   "DspShipAddr":string,
      /**  Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  */  
   "TranStatus":string,
      /**  Extended description for the TranStatus that comes from PlantTran table. Where 'Open' = 'Not Received', 'Closed' = 'Received' and '' = 'Not Shipped'  */  
   "TranStatusDescription":string,
      /**  Carton Height  */  
   "CartonHeight":number,
      /**  Carton length  */  
   "CartonLength":number,
      /**  Carton Width  */  
   "CartonWidth":number,
      /**  The sum of the value of the items in the carton.  List prices - dscount + sales tax for each item.  */  
   "CartonContentValue":number,
      /**  Set to Y if the carton is the last one being shiped to the customer.  Set to N when the sum of the quantity packed does not equl the quantity ordered for each line.  */  
   "LastCartonFlag":boolean,
      /**  Carton Stage number.  */  
   "CartonStageNbr":string,
      /**  Flag to control if the Shipped flag is enabled/disabled  */  
   "EnableShipped":boolean,
      /**  Translated field of ShipStatus  */  
   "SlipStatus":string,
      /**  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  */  
   "EnableWeight":boolean,
      /**  Indicates if the manifest interface is enabled.  */  
   "ManifestFlag":boolean,
      /**  Zero indicates the height prompt is to be enabled.  */  
   "PkgHeightEnable":number,
      /**  Zero indicates the length is enabled.  */  
   "PkgLenEnable":number,
      /**  Zero indicates the width is enabled.  */  
   "PkgWidthEnable":number,
      /**  1 = disable / 0 = enable  */  
   "PkgSizeUOMEnable":number,
      /**  Indicates if changes can occur after the document has been printed  */  
   "AllowChgAfterPrint":boolean,
      /**  Indicates if assign legal number option is available.  */  
   "EnableAssignLegNum":boolean,
      /**  Indicates if the void legal number option is available  */  
   "EnableVoidLegNum":boolean,
      /**  Indicates if a legal number configuration exists for subcontract shipments  */  
   "HasLegNumCnfg":boolean,
      /**  Intended for internal use.  Indicates if prices are to be calculated  */  
   "CalcPSPrices":boolean,
      /**  Indicates if the transaction document type is available for input  */  
   "EnableTranDocType":boolean,
      /**  Description of delivery type  */  
   "DeliveryTypeDescription":string,
      /**  Full description for the shipping company (carrier).  */  
   "FreightedShipViaCodeDescription":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "FreightedShipViaCodeWebDesc":string,
      /**  Full description of the Packaging Classification.  */  
   "PackClssDescription":string,
      /**  Full description of Packing Code.  */  
   "PackingDescription":string,
      /**  Full description for the shipping company (carrier).  */  
   "ShipViaDescription":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "ShipViaWebDesc":string,
      /**  Description  */  
   "TranDocTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TFShipHeadRow{
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
      /**  The Site that shipment was made from.  */  
   "Plant":string,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   "TrackingNumber":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  */  
   "ExternalDeliveryNote":boolean,
      /**  External  ID  */  
   "ExternalID":string,
      /**  directtransfer  */  
   "directtransfer":boolean,
      /**  Site Identifier.  This field cannot be blank.  */  
   "ToPlant":string,
      /**  Shipped flag  */  
   "Shipped":boolean,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  Is a Saturday delivery acceptable  */  
   "SatDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
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
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   "ShipStatus":string,
      /**  Group the shipment belongs to for "Staging"  */  
   "ShipGroup":string,
      /**  Package Weight  */  
   "Weight":number,
      /**  Package Code  */  
   "PkgCode":string,
      /**  NMFC Packaging Classification code.  */  
   "PkgClass":string,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
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
      /**  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  */  
   "BinNum":string,
      /**  Bill of Lading Number the packing slip is linked to  */  
   "BOLNum":number,
      /**  Added for international shipping, Is a commercial invoice required  */  
   "CommercialInvoice":boolean,
      /**  Bill of Lading line number linked to  */  
   "BOLLine":number,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   "ShipExprtDeclartn":boolean,
      /**  For International shipping.  Certificate of Orgin required.  */  
   "CertOfOrigin":boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   "LetterOfInstr":boolean,
      /**  International Shipping - HazardousShipment  */  
   "HazardousShipment":boolean,
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
      /**  International Shipping. Frieght Forwarder ID  */  
   "FFID":string,
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
      /**  Is this an International shipment  */  
   "IntrntlShip":boolean,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   "IndividualPackIDs":boolean,
      /**  Freight Forwarder Third address line  */  
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
      /**  UPS Quantum View Ship from Name  */  
   "UPSQVShipFromName":string,
      /**  UPS Quantum View Memo  */  
   "UPSQVMemo":string,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   "PkgLength":number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   "PkgWidth":number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   "PkgHeight":number,
      /**  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  */  
   "PhantomPack":boolean,
      /**   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   "PkgSizeUOM":string,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   "WeightUOM":string,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Indicates if the document has been printed.  */  
   "DocumentPrinted":boolean,
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
      /**  Indicates the inventory warehouse in the ShipTo Site.  */  
   "WarehouseCode":string,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
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
      /**  AGShippingWay  */  
   "AGShippingWay":string,
      /**  AGCOTMark  */  
   "AGCOTMark":boolean,
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
      /**  The sum of the value of the items in the carton.  List prices - dscount + sales tax for each item.  */  
   "CartonContentValue":number,
      /**  Carton Height  */  
   "CartonHeight":number,
      /**  Carton length  */  
   "CartonLength":number,
      /**  Carton Stage number.  */  
   "CartonStageNbr":string,
      /**  Carton Width  */  
   "CartonWidth":number,
      /**  Display for the Ship From Address  */  
   "DspFromAddr":string,
      /**  Display for the Ship To Address  */  
   "DspShipAddr":string,
      /**  Indicates if assign legal number option is available.  */  
   "EnableAssignLegNum":boolean,
      /**  Flag to control if the Shipped flag is enabled/disabled  */  
   "EnableShipped":boolean,
      /**  Indicates if the transaction document type is available for input  */  
   "EnableTranDocType":boolean,
      /**  Indicates if the void legal number option is available  */  
   "EnableVoidLegNum":boolean,
      /**  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  */  
   "EnableWeight":boolean,
      /**  Indicates if a legal number configuration exists for subcontract shipments  */  
   "HasLegNumCnfg":boolean,
      /**  Set to Y if the carton is the last one being shiped to the customer.  Set to N when the sum of the quantity packed does not equl the quantity ordered for each line.  */  
   "LastCartonFlag":boolean,
   "LegalNumberMessage":string,
      /**  Indicates if the manifest interface is enabled.  */  
   "ManifestFlag":boolean,
      /**  Zero indicates the height prompt is to be enabled.  */  
   "PkgHeightEnable":number,
      /**  Zero indicates the length is enabled.  */  
   "PkgLenEnable":number,
      /**  1 = disable / 0 = enable  */  
   "PkgSizeUOMEnable":number,
      /**  Zero indicates the width is enabled.  */  
   "PkgWidthEnable":number,
      /**  Translated field of ShipStatus  */  
   "SlipStatus":string,
      /**  Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  */  
   "TranStatus":string,
      /**  Extended description for the TranStatus that comes from PlantTran table. Where 'Open' = 'Not Received', 'Closed' = 'Received' and '' = 'Not Shipped'  */  
   "TranStatusDescription":string,
   "VNAccordingToDemand":string,
   "VNCarrier":string,
   "VNContractNumber":string,
   "VNDate":string,
   "VNFor":string,
   "VNFrom":string,
      /**  Indicates if changes can occur after the document has been printed  */  
   "AllowChgAfterPrint":boolean,
      /**  Intended for internal use.  Indicates if prices are to be calculated  */  
   "CalcPSPrices":boolean,
   "DspDigitalSignature":string,
   "QSUseBOL":boolean,
   "QSUseIntl":boolean,
   "QSUseCO":boolean,
      /**  PCID  */  
   "PCID":string,
      /**  Logical indicating if the package control functionality should be enabled.  */  
   "EnablePackageControl":boolean,
      /**  Transfer order number  */  
   "TFOrdNum":string,
      /**  Estimated Date of Arrival  */  
   "MXETADate":string,
      /**  Estimated Time of Arrival  */  
   "MXETATime":number,
      /**  Estimated Date of Departure  */  
   "MXETDDate":string,
      /**  Estimated Time of Departure  */  
   "MXETDTime":number,
   "EnablePhantom":boolean,
   "PhantomCasesExist":boolean,
      /**  Vehicle Weight (in tons)  */  
   "MXVehicleWeight":number,
      /**  A unique Carta Porte identification number assigned by Epicor  */  
   "MXIdCCP":string,
      /**  Customs Regime for Export transaction.  */  
   "MXCustomsRegime":string,
      /**  Check box to specify the use of reverse logistic, collection or devolution services when shipping goods.  */  
   "MXReverseLogistics":boolean,
   "BitFlag":number,
   "AGInvoicingPointDescription":string,
   "AGLegalNumCnfgDescription":string,
   "DeliveryTypeDescription":string,
   "FreightedShipViaCodeDescription":string,
   "FreightedShipViaCodeWebDesc":string,
   "PackClssDescription":string,
   "PackingDescription":string,
   "ShipViaWebDesc":string,
   "ShipViaDescription":string,
   "TranDocTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TFShipHeadTrailerRow{
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

export interface Erp_Tablesets_TFShipUPSRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  UPS Quantum View Sequence  */  
   "UPSQVSeq":number,
      /**  Email Address  */  
   "EmailAddress":string,
      /**  Notify Email address when shipped  */  
   "ShipmentNotify":boolean,
      /**  Logical indicating if the Email Address is to be notified of a failed shipment.  */  
   "FailureNotify":boolean,
      /**  Logical indicating if the Email Address is to be notified of delivery.  */  
   "DeliveryNotify":boolean,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   "PackNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Logical indicating if the UPS Quantum View fields are to be enabled  */  
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
      @param ipPackNum
      @param ds
   */  
export interface AssignLegalNumber_input{
      /**  Packing Slip number  */  
   ipPackNum:number,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface AssignLegalNumber_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
   opLegalNumMsg:string,
}
}

   /** Required : 
      @param CartonNumber
   */  
export interface CalculateWeight_input{
      /**  Carton Number  */  
   CartonNumber:number,
}

export interface CalculateWeight_output{
parameters : {
      /**  output parameters  */  
   CalculatedWeight:number,
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
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface CallsCreateCustomerCartons_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
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
      @param ipPackNum
      @param ipPCID
      @param ds
   */  
export interface ChangePCID_input{
   ipPackNum:number,
   ipPCID:string,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface ChangePCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
   opAlreadyScannedPackNum:number,
}
}

   /** Required : 
      @param partNum
      @param ds
   */  
export interface ChangePOPartNum_input{
      /**  The new part number  */  
   partNum:string,
   ds:Erp_Tablesets_PackOutTableset[],
}

export interface ChangePOPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackOutTableset[],
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface ChangePORevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_PackOutTableset[],
}

export interface ChangePORevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackOutTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangePackOutLotNum_input{
   ds:Erp_Tablesets_PackOutTableset[],
}

export interface ChangePackOutLotNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackOutTableset[],
}
}

   /** Required : 
      @param ipShipHedRowID
      @param ipStatus
      @param ds
   */  
export interface ChangeStatus_input{
      /**  Unique Identifier for the Transfer Order Shipment  */  
   ipShipHedRowID:string,
      /**  Selected Status.
           Valid Options: Open, Close, Void, UnVoid, Freight, UnFreight, Stage  */  
   ipStatus:string,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface ChangeStatus_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeTFOrdDtlLotNum_input{
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}

export interface ChangeTFOrdDtlLotNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}
}

   /** Required : 
      @param ipProposedSellingQtyUOM
      @param ds
   */  
export interface ChangeTFOrdDtlOurStockQtyUOM_input{
      /**  The new proposed TFOrdDtl.SellingQtyUOM value  */  
   ipProposedSellingQtyUOM:string,
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}

export interface ChangeTFOrdDtlOurStockQtyUOM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}
}

   /** Required : 
      @param ipProposedOurStockQty
      @param ds
   */  
export interface ChangeTFOrdDtlOurStockQty_input{
      /**  The new proposed TFOrdDtl.DisplayShipQty value  */  
   ipProposedOurStockQty:number,
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}

export interface ChangeTFOrdDtlOurStockQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeTFOrdDtlPartNum_input{
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}

export interface ChangeTFOrdDtlPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}
}

   /** Required : 
      @param ipProposedWarehouseCode
      @param ds
   */  
export interface ChangeTFOrdDtlWarehouseCode_input{
      /**  The new proposed TFOrdDtl.WarehouseCode value  */  
   ipProposedWarehouseCode:string,
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}

export interface ChangeTFOrdDtlWarehouseCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeTFShipDtlLotNum_input{
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface ChangeTFShipDtlLotNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param packNum
      @param packLine
      @param ipProposedOurStockShippedQty
      @param ds
   */  
export interface ChangeTFShipDtlOurStockShippedQty_input{
      /**  Pack Number to be modified  */  
   packNum:number,
      /**  Pack Line to be modified  */  
   packLine:number,
      /**  The new proposed TFShipDtl.DisplayShipQty value  */  
   ipProposedOurStockShippedQty:number,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface ChangeTFShipDtlOurStockShippedQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
   outMessage:string,
   outNegQtyAction:string,
   outNetWeight:number,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeTFShipDtlPartNum_input{
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface ChangeTFShipDtlPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeTFShipDtlTFOrderLine_input{
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface ChangeTFShipDtlTFOrderLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param ipProposedTFOrdNum
      @param ds
   */  
export interface ChangeTFShipDtlTFOrderNum_input{
      /**  The new proposed TFShipDtl.TFOrdNum value  */  
   ipProposedTFOrdNum:string,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface ChangeTFShipDtlTFOrderNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param packNum
      @param packLine
      @param ipProposedWarehouseCode
      @param ds
   */  
export interface ChangeTFShipDtlWarehouseCode_input{
      /**  Pack Number to be modified  */  
   packNum:number,
      /**  Pack Line to be modified  */  
   packLine:number,
      /**  The new proposed TFShipDtl.WarehouseCode value  */  
   ipProposedWarehouseCode:string,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface ChangeTFShipDtlWarehouseCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param ipProposedTFOrdNum
      @param ds
   */  
export interface ChangeTFShipHeadTFOrdNum_input{
   ipProposedTFOrdNum:string,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface ChangeTFShipHeadTFOrdNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param iPackNum
      @param iPackLine
   */  
export interface CheckCOOPercents_input{
      /**  The pack number  */  
   iPackNum:number,
      /**  The pack line number  */  
   iPackLine:number,
}

export interface CheckCOOPercents_output{
}

   /** Required : 
      @param tfShipHeadSysRowID
      @param ds
   */  
export interface CheckDirectOrderLine_input{
   tfShipHeadSysRowID:string,
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}

export interface CheckDirectOrderLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TranDirectOrderTableset[],
   allocationMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CheckOHQ_input{
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}

export interface CheckOHQ_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TranDirectOrderTableset[],
   inventoryMessage:string,
}
}

   /** Required : 
      @param ds
      @param ipBinNum
   */  
export interface CheckPackOutBinNum_input{
   ds:Erp_Tablesets_PackOutTableset[],
      /**  The new proposed BinNum value  */  
   ipBinNum:string,
}

export interface CheckPackOutBinNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackOutTableset[],
}
}

   /** Required : 
      @param ds
      @param ipLotNum
   */  
export interface CheckPackOutLotNum_input{
   ds:Erp_Tablesets_PackOutTableset[],
      /**  The new proposed LotNum value  */  
   ipLotNum:string,
}

export interface CheckPackOutLotNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackOutTableset[],
   vMsgText:string,
   vMsgType:string,
}
}

   /** Required : 
      @param ds
      @param ipOrderLine
   */  
export interface CheckPackOutOrderLine_input{
   ds:Erp_Tablesets_PackOutTableset[],
      /**  The new proposed OrderLine value  */  
   ipOrderLine:number,
}

export interface CheckPackOutOrderLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackOutTableset[],
}
}

   /** Required : 
      @param ds
      @param ipPartNum
   */  
export interface CheckPackOutPartNum_input{
   ds:Erp_Tablesets_PackOutTableset[],
      /**  The new proposed PartNum value  */  
   ipPartNum:string,
}

export interface CheckPackOutPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackOutTableset[],
}
}

   /** Required : 
      @param ds
      @param ipTFOrdNum
   */  
export interface CheckPackOutTFOrdNum_input{
   ds:Erp_Tablesets_PackOutTableset[],
      /**  The new proposed TFOrdNum value  */  
   ipTFOrdNum:string,
}

export interface CheckPackOutTFOrdNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackOutTableset[],
}
}

   /** Required : 
      @param ds
      @param ipWarehousecode
   */  
export interface CheckPackOutWarehousecode_input{
   ds:Erp_Tablesets_PackOutTableset[],
      /**  The new proposed Warehousecode value  */  
   ipWarehousecode:string,
}

export interface CheckPackOutWarehousecode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackOutTableset[],
}
}

   /** Required : 
      @param partNum
   */  
export interface CheckPrePartInfo_input{
      /**  The input-output part number to validate and it gets returned  */  
   partNum:string,
}

export interface CheckPrePartInfo_output{
parameters : {
      /**  output parameters  */  
   partNum:string,
   vMsgText:string,
   vSubAvail:boolean,
   vMsgType:string,
}
}

   /** Required : 
      @param ipLotNum
      @param ipPartNum
   */  
export interface CheckTFOrdDtlLotNum_input{
      /**  The lotnum to validate  */  
   ipLotNum:string,
      /**  The value of the TFOrdDtl.PartNum used to locate partlot records  */  
   ipPartNum:string,
}

export interface CheckTFOrdDtlLotNum_output{
parameters : {
      /**  output parameters  */  
   vMsgText:string,
   vMsgType:string,
}
}

   /** Required : 
      @param ipLotNum
      @param ipPartNum
   */  
export interface CheckTFShipDtlLotNum_input{
      /**  The lotnum to validate  */  
   ipLotNum:string,
      /**  The value of the TFShipDtl.PartNum used to locate partlot records  */  
   ipPartNum:string,
}

export interface CheckTFShipDtlLotNum_output{
parameters : {
      /**  output parameters  */  
   vMsgText:string,
   vMsgType:string,
}
}

   /** Required : 
      @param ipPackNum
      @param ipPackLine
      @param ipProposedTFOrdLine
      @param ds
   */  
export interface CheckTFShipDtlTFOrderLine_input{
      /**  The packnum value of the TFShipDtl to check  */  
   ipPackNum:number,
      /**  The packline value of the TFShipDtl to check  */  
   ipPackLine:number,
      /**  The proposed TFOrdline value  */  
   ipProposedTFOrdLine:number,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface CheckTFShipDtlTFOrderLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface CheckTFShipDtl_input{
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface CheckTFShipDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
   allocationMessage:string,
   cMessage:string,
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
export interface ClearConvertedManifest_input{
   ipPackNum:number,
}

export interface ClearConvertedManifest_output{
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
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface CreateCustomerCartons_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param ipShipHeadRowID
      @param ds
      @param ds1
   */  
export interface CreateDirectOrderLine_input{
      /**  Unique Identifier for the Transfer Order Shipment  */  
   ipShipHeadRowID:string,
   ds:Erp_Tablesets_TransOrderShipTableset[],
   ds1:Erp_Tablesets_TranDirectOrderTableset[],
}

export interface CreateDirectOrderLine_output{
   returnObj:Erp_Tablesets_TransOrderShipTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
   ds1:Erp_Tablesets_TranDirectOrderTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface CreateDirectOrder_input{
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}

export interface CreateDirectOrder_output{
   returnObj:Erp_Tablesets_TransOrderShipTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}
}

   /** Required : 
      @param packNum
      @param orderNum
      @param ds
   */  
export interface CreateMassShipDtl_input{
      /**  Your existing packing slip number  */  
   packNum:number,
      /**  The transfer order number  */  
   orderNum:string,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface CreateMassShipDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
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
      @param ds
   */  
export interface DeletePhantomPacks_input{
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface DeletePhantomPacks_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
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
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface DeleteRangePhantomPacks_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param ShipDate
   */  
export interface EADValidation_input{
      /**  Shipment Date  */  
   ShipDate:string,
}

export interface EADValidation_output{
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

export interface Erp_Tablesets_TFOrdDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  Will be blank unless a header is tied to the table  */  
   TFOrdNum:string,
      /**  This field along with Company and TFOrdNum make up the unique key to  link to the TFOrdHed table. The system generates this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   TFOrdLine:number,
      /**  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  */  
   OpenLine:boolean,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Quantity ,using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   OurStockQty:number,
      /**  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  */  
   WarehouseCode:string,
      /**  Actual quantity ,using Our U/M, shipped from Stock.  Updated via the shipping process.  */  
   OurStockShippedQty:number,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  Site Identifier.  This field cannot be blank.  */  
   ToPlant:string,
      /**  Indicates an Unfirm Transfer Order.  Similar to JobFirm  */  
   OrderFirm:boolean,
      /**  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for OrderDtl.RequestDate.  */  
   RequestDate:string,
      /**  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  */  
   NeedByDate:string,
      /**  Shipped flag  */  
   Shipped:boolean,
      /**  Indicates if the Order was created through MRP or by UI Entry.  If Manual and Unfirm, MRP will not delete the Order  */  
   ManualOrder:boolean,
      /**  Job number of the job supplying the parts for this record (FromSite)  */  
   SupplyJobNum:string,
      /**  Job number of the job demand for the parts on this record (ToSite)  */  
   DemandJobNum:string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   ShipViaCode:string,
      /**  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  */  
   TFLineNum:string,
      /**  Received Quantity  */  
   ReceivedQty:number,
      /**  Additional quantity beyond the initial requirement to be transferred  */  
   AdditionalQty:number,
      /**  Date transfer suggestion went firm  */  
   FirmDate:string,
      /**  User who made the transfer suggestion firm  */  
   FirmUser:string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  */  
   DemandAsmSeq:number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  */  
   DemandMtlSeq:number,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  */  
   SupplyAsmSeq:number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  */  
   SupplyMtlSeq:number,
      /**  Indicates if this requirement/receipt affects stock.  */  
   StockTrans:boolean,
      /**   Unit of Measure code of the order quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   OurStockQtyUOM:string,
      /**   Unit of Measure code of the selling quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   SellingQtyUOM:string,
      /**  Selling Quantity  */  
   SellingQty:number,
      /**  Selling Shipped Quantity  */  
   SellingShippedQty:number,
      /**  Indicates if the transfer order line is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   SelectForPicking:boolean,
      /**  The transfer order "Staging" warehouse for the transfer order line.  Defaults from the system default warehouse (Site.DefTFOrdPickWhse).  */  
   StagingWarehouseCode:string,
      /**  The transfer order "Staging" bin for the transfer order line.  Defaults from the system default bin (Site.DefTFOrdPickBin).  */  
   StagingBinNum:string,
      /**   A non blank character indicates that the transfer order line could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  */  
   PickError:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ContractID  */  
   ContractID:string,
      /**  LinkToContract  */  
   LinkToContract:boolean,
      /**  Transfer Orders are multi plant while Planning Contracts are plant specific. TransferContractID field is designed to select a new planning contract valid for the plant that supplies the demand. ContractID field keeps the ContractID valid for the demand plant.  */  
   TransferContractID:string,
      /**  Transfer Orders are multi plant while Planning Contracts are plant specific. TransferLinkToContract field is designed to work for TransferContractID valid for the plant that suppies the demand. LinkToContract works for ContractID field valid for the demand plant.  */  
   TransferLinkToContract:boolean,
      /**  Related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Indicates if the transfer order line should be added or removed from the fulfillment queue.  */  
   PartAllocQueueAction:string,
      /**  This flag indicates if the transfer order line is ready to be fulfilled.  */  
   ReadyToFulfill:boolean,
   AvailSerialNumbers:boolean,
   BinNum:string,
   DimCode:string,
      /**  DimCodeDimCodeDescription  */  
   DimCodeDimCodeDescription:string,
   DimConvFactor:number,
      /**  OurStockQty * DimConvFactor  */  
   DisplayShipQty:number,
   DUM:string,
   FromPlantDesc:string,
      /**  Inventory UOM that the Transfer Order Detail is allocated against.  */  
   InvtyUOM:string,
      /**  Descriptive Text of OpenLine Field  */  
   LineStatus:string,
   LotNum:string,
   Packages:number,
   PCID:string,
   PkgClass:string,
      /**  PkgClassDescription  */  
   PkgClassDescription:string,
   PkgCode:string,
      /**  PkgCodeDescription  */  
   PkgCodeDescription:string,
   RequiredQty:number,
   Selected:boolean,
   StagingBinDesc:string,
      /**  This order inventory quantity  */  
   ThisOrderInvtyQty:number,
   ToPlantDesc:string,
   TotNetWeight:number,
   Weight:number,
   CreateOrder:boolean,
   EnableAttributeSetSearch:boolean,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
      /**  Error Status Display  */  
   ErrorStatusDisplay:string,
      /**  True if this release is in the fulfillment queue.  */  
   InPartAllocQueue:boolean,
      /**  Show Fulfillment Queue Actions  */  
   ShowFulfillmentQueueActions:boolean,
   BitFlag:number,
   DynAttrValueSetShortDescription:string,
   DynAttrValueSetDescription:string,
   PartDescTrackInventoryAttributes:boolean,
   PartDescAttrClassID:string,
   PartDescPricePerCode:string,
   PartDescTrackSerialNum:boolean,
   PartDescPartDescription:string,
   PartDescTrackDimension:boolean,
   PartDescSalesUM:string,
   PartDescIUM:string,
   PartDescSellingFactor:number,
   PartDescTrackLots:boolean,
   PartDescTrackInventoryByRevision:boolean,
   ShipViaCodeDescription:string,
   ShipViaCodeWebDesc:string,
   StageWhseCodeDescription:string,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TFOrdHedRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   TFOrdNum:string,
      /**  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  */  
   OpenOrder:boolean,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  Site Identifier.  This field cannot be blank.  */  
   ToPlant:string,
      /**  This is used as one of the selection parameters on the Order entry edit reports. The intent is for users to be able to select orders that they have entered for hard copy edit.On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   EntryPerson:string,
      /**  Mandatory entry and must be valid. Default as the system date.  */  
   OrderDate:string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   ShipViaCode:string,
      /**  Used to establish shipping comments about the overall order. These will copied into the packing slip header file as defaults.  */  
   ShipComment:string,
      /**  Contains picking  comments about the overall order. These will be printed on the picking lists.  */  
   PickListComment:string,
      /**  Shipped flag  */  
   Shipped:boolean,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
      /**  The Legal Number of the record.  */  
   LegalNumber:string,
      /**  Indicates the inventory warehouse in the ShipTo Site.  */  
   WarehouseCode:string,
      /**  Indicates that the One Time ShipTo information defined for this release should be used.  */  
   UseOTS:boolean,
      /**  One Time ShipTo Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time ShipTo first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time ShipTo second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time ShipTo third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portionof the One Time ShipTo address.  */  
   OTSCity:string,
      /**  The state or provine portion of the One Time ShipTo address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo address.  */  
   OTSZip:string,
      /**  One Time ShipTo contact name.  */  
   OTSContact:string,
   OTSCountryNum:number,
      /**  Phone number for the One Time ShipTo.  */  
   OTSPhoneNum:string,
      /**  Fax Number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  This flag indicates if the transfer order is ready to be fulfilled.  */  
   ReadyToFulfill:boolean,
   ToPlantDesc:string,
   FromPlantDesc:string,
   NeedByDate:string,
   RequestDate:string,
      /**  Show Fulfillment Queue Actions  */  
   ShowFulfillmentQueueActions:boolean,
      /**  Flag to indicate if details need to be refreshed after changing the header.  */  
   UpdateDtlRecords:boolean,
   BitFlag:number,
   EntryPersonName:string,
   ShipViaDescription:string,
   ShipViaWebDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TFShipDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  */  
   PackLine:number,
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
      /**  Weight Unit of measure...qualifies the weight field value. (Lb, Oz, Gr...).  */  
   NetWeightUOM:string,
      /**  Lot Number is defaulted as Job Number.  */  
   LotNum:string,
      /**  The Part's Net Weight * (SellingJobShipQty + SellingInventoryShipQty)  */  
   TotalNetWeight:number,
      /**   Identifies the warehouse for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area warehouse (Site.DefShipWhse) otherwise it's blank.  */  
   WIPWarehouseCode:string,
      /**   Identifies the warehouse bin for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area bin (Site.DefShipBin) otherwise it's blank.  */  
   WIPBinNum:string,
      /**  This field along with Company and TFOrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   TFOrdLine:number,
      /**  Quantity ,using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   OurStockQty:number,
      /**  Actual quantity ,using Our U/M, shipped from Stock.  Updated via the shipping process.  */  
   OurStockShippedQty:number,
      /**  requestdate  */  
   requestdate:string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   TFOrdNum:string,
      /**  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  */  
   TFLineNum:string,
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
      /**  Calculated price for the item being transferred.  */  
   UnitPrice:number,
      /**  Unit Price.  */  
   DocUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
      /**  Quantity picked from inventory that was not manually allocated. This quantity is automatically added to PartAlloc such when inventory is picked, it is considered allocated to this Transfer Order.  This quantity is in the IUM unit of measure.  */  
   PickedAutoAllocatedQty:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PCID  */  
   PCID:string,
      /**  If AMM is licensed this column will hold how much of this shipment was allocated prior to the shipment in case this shipment is ever "unshipped"  */  
   AllocatedShippedQty:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
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
      /**  Are there available serial numbers?  */  
   AvailSerialNumbers:boolean,
      /**  direct-transfer  */  
   direct_transfer:boolean,
      /**  OurStockShippedQty * DimConvFactor  */  
   DisplayShipQty:number,
      /**  Indicates if the Shipment line has been shipped  */  
   LineShipped:boolean,
      /**  Current Shipment in OrderUOM  */  
   OrderShipmentQty:number,
      /**  UOM from Transfer Order  */  
   OrderUOM:string,
      /**  Used by the freight web service  */  
   PartAESExp:string,
      /**  Used by the freight web service  */  
   PartECNNumber:string,
      /**  Used by freight web service  */  
   PartExpLicNumber:string,
      /**  used by freight web service  */  
   PartExpLicType:string,
      /**  Used by the freight web service  */  
   PartHazClass:string,
      /**  Used by the freight web service  */  
   PartHazGvrnmtID:string,
      /**  Used by the freight web service  */  
   PartHazItem:boolean,
      /**  Used by the freight web service  */  
   PartHazPackInstr:string,
      /**  Used by the freight web service  */  
   PartHazSub:string,
      /**  Used by the freight web service  */  
   PartHazTechName:string,
      /**  Used by the freight web service  */  
   PartHTS:string,
      /**  Used by the freight web service  */  
   PartNAFTAOrigCountry:string,
      /**  Used by the freight web service  */  
   PartNAFTAPref:string,
      /**  Used by the freight web service  */  
   PartNAFTAProd:string,
      /**  Used by the freight web service  */  
   PartOrigCountry:string,
      /**  Used by the freight web service  */  
   PartSchedBcode:string,
      /**  Used by the freight web service  */  
   PartUseHTSDesc:boolean,
      /**  Indicates if the Shipment line has been received  */  
   Received:boolean,
      /**  The remaining quantity  */  
   RemainingQty:number,
      /**  The request quantity  */  
   RequestQty:number,
      /**  The shipped quantity  */  
   ShippedQty:number,
      /**  Ship Status of the Transfer Order Shipment line, copied from the Transfer Order Shipment header.  */  
   ShipStatus:string,
      /**  Currency Code  */  
   CurrencyCode:string,
      /**  Enable Attribute Set Search  */  
   EnableAttributeSetSearch:boolean,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
   BitFlag:number,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PartNumTrackDimension:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumPricePerCode:string,
   PartNumPartDescription:string,
   PartNumIUM:string,
   PartNumSalesUM:string,
   PartNumSellingFactor:number,
   PartNumTrackLots:boolean,
   PartNumAttrClassID:string,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TFShipHeadAttchRow{
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

export interface Erp_Tablesets_TFShipHeadInsuranceRow{
      /**  Company  */  
   Company:string,
      /**  PackNum  */  
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

export interface Erp_Tablesets_TFShipHeadListRow{
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
      /**  The Site that shipment was made from.  */  
   Plant:string,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   TrackingNumber:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  */  
   ExternalDeliveryNote:boolean,
      /**  External  ID  */  
   ExternalID:string,
      /**  directtransfer  */  
   directtransfer:boolean,
      /**  Site Identifier.  This field cannot be blank.  */  
   ToPlant:string,
      /**  Shipped flag  */  
   Shipped:boolean,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
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
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   ShipStatus:string,
      /**  Group the shipment belongs to for "Staging"  */  
   ShipGroup:string,
      /**  Package Weight  */  
   Weight:number,
      /**  Package Code  */  
   PkgCode:string,
      /**  NMFC Packaging Classification code.  */  
   PkgClass:string,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
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
      /**  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  */  
   BinNum:string,
      /**  Bill of Lading Number the packing slip is linked to  */  
   BOLNum:number,
      /**  Added for international shipping, Is a commercial invoice required  */  
   CommercialInvoice:boolean,
      /**  Bill of Lading line number linked to  */  
   BOLLine:number,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   ShipExprtDeclartn:boolean,
      /**  For International shipping.  Certificate of Orgin required.  */  
   CertOfOrigin:boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   LetterOfInstr:boolean,
      /**  International Shipping - HazardousShipment  */  
   HazardousShipment:boolean,
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
      /**  International Shipping. Frieght Forwarder ID  */  
   FFID:string,
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
      /**  Is this an International shipment  */  
   IntrntlShip:boolean,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   IndividualPackIDs:boolean,
      /**  Freight Forwarder Third address line  */  
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
      /**  UPS Quantum View Ship from Name  */  
   UPSQVShipFromName:string,
      /**  UPS Quantum View Memo  */  
   UPSQVMemo:string,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   PkgLength:number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   PkgWidth:number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   PkgHeight:number,
      /**  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  */  
   PhantomPack:boolean,
      /**   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   PkgSizeUOM:string,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   WeightUOM:string,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
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
      /**  Indicates the inventory warehouse in the ShipTo Site.  */  
   WarehouseCode:string,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Display for the Ship From Address  */  
   DspFromAddr:string,
      /**  Display for the Ship To Address  */  
   DspShipAddr:string,
      /**  Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  */  
   TranStatus:string,
      /**  Extended description for the TranStatus that comes from PlantTran table. Where 'Open' = 'Not Received', 'Closed' = 'Received' and '' = 'Not Shipped'  */  
   TranStatusDescription:string,
      /**  Carton Height  */  
   CartonHeight:number,
      /**  Carton length  */  
   CartonLength:number,
      /**  Carton Width  */  
   CartonWidth:number,
      /**  The sum of the value of the items in the carton.  List prices - dscount + sales tax for each item.  */  
   CartonContentValue:number,
      /**  Set to Y if the carton is the last one being shiped to the customer.  Set to N when the sum of the quantity packed does not equl the quantity ordered for each line.  */  
   LastCartonFlag:boolean,
      /**  Carton Stage number.  */  
   CartonStageNbr:string,
      /**  Flag to control if the Shipped flag is enabled/disabled  */  
   EnableShipped:boolean,
      /**  Translated field of ShipStatus  */  
   SlipStatus:string,
      /**  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  */  
   EnableWeight:boolean,
      /**  Indicates if the manifest interface is enabled.  */  
   ManifestFlag:boolean,
      /**  Zero indicates the height prompt is to be enabled.  */  
   PkgHeightEnable:number,
      /**  Zero indicates the length is enabled.  */  
   PkgLenEnable:number,
      /**  Zero indicates the width is enabled.  */  
   PkgWidthEnable:number,
      /**  1 = disable / 0 = enable  */  
   PkgSizeUOMEnable:number,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
      /**  Indicates if a legal number configuration exists for subcontract shipments  */  
   HasLegNumCnfg:boolean,
      /**  Intended for internal use.  Indicates if prices are to be calculated  */  
   CalcPSPrices:boolean,
      /**  Indicates if the transaction document type is available for input  */  
   EnableTranDocType:boolean,
      /**  Description of delivery type  */  
   DeliveryTypeDescription:string,
      /**  Full description for the shipping company (carrier).  */  
   FreightedShipViaCodeDescription:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   FreightedShipViaCodeWebDesc:string,
      /**  Full description of the Packaging Classification.  */  
   PackClssDescription:string,
      /**  Full description of Packing Code.  */  
   PackingDescription:string,
      /**  Full description for the shipping company (carrier).  */  
   ShipViaDescription:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   ShipViaWebDesc:string,
      /**  Description  */  
   TranDocTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TFShipHeadListTableset{
   TFShipHeadList:Erp_Tablesets_TFShipHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_TFShipHeadRow{
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
      /**  The Site that shipment was made from.  */  
   Plant:string,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   TrackingNumber:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  */  
   ExternalDeliveryNote:boolean,
      /**  External  ID  */  
   ExternalID:string,
      /**  directtransfer  */  
   directtransfer:boolean,
      /**  Site Identifier.  This field cannot be blank.  */  
   ToPlant:string,
      /**  Shipped flag  */  
   Shipped:boolean,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
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
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   ShipStatus:string,
      /**  Group the shipment belongs to for "Staging"  */  
   ShipGroup:string,
      /**  Package Weight  */  
   Weight:number,
      /**  Package Code  */  
   PkgCode:string,
      /**  NMFC Packaging Classification code.  */  
   PkgClass:string,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
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
      /**  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  */  
   BinNum:string,
      /**  Bill of Lading Number the packing slip is linked to  */  
   BOLNum:number,
      /**  Added for international shipping, Is a commercial invoice required  */  
   CommercialInvoice:boolean,
      /**  Bill of Lading line number linked to  */  
   BOLLine:number,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   ShipExprtDeclartn:boolean,
      /**  For International shipping.  Certificate of Orgin required.  */  
   CertOfOrigin:boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   LetterOfInstr:boolean,
      /**  International Shipping - HazardousShipment  */  
   HazardousShipment:boolean,
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
      /**  International Shipping. Frieght Forwarder ID  */  
   FFID:string,
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
      /**  Is this an International shipment  */  
   IntrntlShip:boolean,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   IndividualPackIDs:boolean,
      /**  Freight Forwarder Third address line  */  
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
      /**  UPS Quantum View Ship from Name  */  
   UPSQVShipFromName:string,
      /**  UPS Quantum View Memo  */  
   UPSQVMemo:string,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   PkgLength:number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   PkgWidth:number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   PkgHeight:number,
      /**  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  */  
   PhantomPack:boolean,
      /**   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   PkgSizeUOM:string,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   WeightUOM:string,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
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
      /**  Indicates the inventory warehouse in the ShipTo Site.  */  
   WarehouseCode:string,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
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
      /**  AGShippingWay  */  
   AGShippingWay:string,
      /**  AGCOTMark  */  
   AGCOTMark:boolean,
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
      /**  The sum of the value of the items in the carton.  List prices - dscount + sales tax for each item.  */  
   CartonContentValue:number,
      /**  Carton Height  */  
   CartonHeight:number,
      /**  Carton length  */  
   CartonLength:number,
      /**  Carton Stage number.  */  
   CartonStageNbr:string,
      /**  Carton Width  */  
   CartonWidth:number,
      /**  Display for the Ship From Address  */  
   DspFromAddr:string,
      /**  Display for the Ship To Address  */  
   DspShipAddr:string,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
      /**  Flag to control if the Shipped flag is enabled/disabled  */  
   EnableShipped:boolean,
      /**  Indicates if the transaction document type is available for input  */  
   EnableTranDocType:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
      /**  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  */  
   EnableWeight:boolean,
      /**  Indicates if a legal number configuration exists for subcontract shipments  */  
   HasLegNumCnfg:boolean,
      /**  Set to Y if the carton is the last one being shiped to the customer.  Set to N when the sum of the quantity packed does not equl the quantity ordered for each line.  */  
   LastCartonFlag:boolean,
   LegalNumberMessage:string,
      /**  Indicates if the manifest interface is enabled.  */  
   ManifestFlag:boolean,
      /**  Zero indicates the height prompt is to be enabled.  */  
   PkgHeightEnable:number,
      /**  Zero indicates the length is enabled.  */  
   PkgLenEnable:number,
      /**  1 = disable / 0 = enable  */  
   PkgSizeUOMEnable:number,
      /**  Zero indicates the width is enabled.  */  
   PkgWidthEnable:number,
      /**  Translated field of ShipStatus  */  
   SlipStatus:string,
      /**  Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  */  
   TranStatus:string,
      /**  Extended description for the TranStatus that comes from PlantTran table. Where 'Open' = 'Not Received', 'Closed' = 'Received' and '' = 'Not Shipped'  */  
   TranStatusDescription:string,
   VNAccordingToDemand:string,
   VNCarrier:string,
   VNContractNumber:string,
   VNDate:string,
   VNFor:string,
   VNFrom:string,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
      /**  Intended for internal use.  Indicates if prices are to be calculated  */  
   CalcPSPrices:boolean,
   DspDigitalSignature:string,
   QSUseBOL:boolean,
   QSUseIntl:boolean,
   QSUseCO:boolean,
      /**  PCID  */  
   PCID:string,
      /**  Logical indicating if the package control functionality should be enabled.  */  
   EnablePackageControl:boolean,
      /**  Transfer order number  */  
   TFOrdNum:string,
      /**  Estimated Date of Arrival  */  
   MXETADate:string,
      /**  Estimated Time of Arrival  */  
   MXETATime:number,
      /**  Estimated Date of Departure  */  
   MXETDDate:string,
      /**  Estimated Time of Departure  */  
   MXETDTime:number,
   EnablePhantom:boolean,
   PhantomCasesExist:boolean,
      /**  Vehicle Weight (in tons)  */  
   MXVehicleWeight:number,
      /**  A unique Carta Porte identification number assigned by Epicor  */  
   MXIdCCP:string,
      /**  Customs Regime for Export transaction.  */  
   MXCustomsRegime:string,
      /**  Check box to specify the use of reverse logistic, collection or devolution services when shipping goods.  */  
   MXReverseLogistics:boolean,
   BitFlag:number,
   AGInvoicingPointDescription:string,
   AGLegalNumCnfgDescription:string,
   DeliveryTypeDescription:string,
   FreightedShipViaCodeDescription:string,
   FreightedShipViaCodeWebDesc:string,
   PackClssDescription:string,
   PackingDescription:string,
   ShipViaWebDesc:string,
   ShipViaDescription:string,
   TranDocTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TFShipHeadTrailerRow{
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

export interface Erp_Tablesets_TFShipUPSRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  UPS Quantum View Sequence  */  
   UPSQVSeq:number,
      /**  Email Address  */  
   EmailAddress:string,
      /**  Notify Email address when shipped  */  
   ShipmentNotify:boolean,
      /**  Logical indicating if the Email Address is to be notified of a failed shipment.  */  
   FailureNotify:boolean,
      /**  Logical indicating if the Email Address is to be notified of delivery.  */  
   DeliveryNotify:boolean,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   PackNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Logical indicating if the UPS Quantum View fields are to be enabled  */  
   EnableQuantumView:boolean,
   ShipStatus:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TranDirectOrderTableset{
   TFOrdHed:Erp_Tablesets_TFOrdHedRow[],
   TFOrdDtl:Erp_Tablesets_TFOrdDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_TransOrderShipTableset{
   TFShipHead:Erp_Tablesets_TFShipHeadRow[],
   TFShipHeadAttch:Erp_Tablesets_TFShipHeadAttchRow[],
   TFShipDtl:Erp_Tablesets_TFShipDtlRow[],
   ShipCOO:Erp_Tablesets_ShipCOORow[],
   CartonTrkDtl:Erp_Tablesets_CartonTrkDtlRow[],
   TFShipHeadInsurance:Erp_Tablesets_TFShipHeadInsuranceRow[],
   TFShipHeadTrailer:Erp_Tablesets_TFShipHeadTrailerRow[],
   TFShipUPS:Erp_Tablesets_TFShipUPSRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtTransOrderShipTableset{
   TFShipHead:Erp_Tablesets_TFShipHeadRow[],
   TFShipHeadAttch:Erp_Tablesets_TFShipHeadAttchRow[],
   TFShipDtl:Erp_Tablesets_TFShipDtlRow[],
   ShipCOO:Erp_Tablesets_ShipCOORow[],
   CartonTrkDtl:Erp_Tablesets_CartonTrkDtlRow[],
   TFShipHeadInsurance:Erp_Tablesets_TFShipHeadInsuranceRow[],
   TFShipHeadTrailer:Erp_Tablesets_TFShipHeadTrailerRow[],
   TFShipUPS:Erp_Tablesets_TFShipUPSRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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

   /** Required : 
      @param ds
   */  
export interface GenerateDigitalSignature_input{
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface GenerateDigitalSignature_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

export interface GetAvailTranDocTypes_output{
parameters : {
      /**  output parameters  */  
   AvailTypes:string,
}
}

   /** Required : 
      @param packNum
   */  
export interface GetByID_input{
   packNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_TransOrderShipTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_TransOrderShipTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_TransOrderShipTableset[],
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
      /**  Table Name  */  
   tableName:string,
      /**  Field Name  */  
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param tfOrdNum
      @param ds
   */  
export interface GetDirectOrderDS_input{
      /**  Unique Identifier for the Transfer Order  */  
   tfOrdNum:string,
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}

export interface GetDirectOrderDS_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetDirectShipDate_input{
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}

export interface GetDirectShipDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}
}

export interface GetDisablePackOut_output{
   returnObj:boolean,
}

export interface GetEnablePackageControl_output{
      /**  bool  */  
   returnObj:boolean,
}

   /** Required : 
      @param ipPackNum
      @param ds
   */  
export interface GetLegalNumGenOpts_input{
      /**  Packing Slip number  */  
   ipPackNum:number,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface GetLegalNumGenOpts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
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
   returnObj:Erp_Tablesets_TFShipHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param shipmentType
      @param packNum
   */  
export interface GetNewCartonTrkDtl_input{
   ds:Erp_Tablesets_TransOrderShipTableset[],
   shipmentType:string,
   packNum:number,
}

export interface GetNewCartonTrkDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param TFOrdNum
      @param NeedByDate
      @param RequestDate
      @param ds
   */  
export interface GetNewDirectOrderLine_input{
      /**  Transfer Order Number  */  
   TFOrdNum:string,
      /**  NeedByDate  */  
   NeedByDate:string,
      /**  Ship Date  */  
   RequestDate:string,
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}

export interface GetNewDirectOrderLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewDirectOrder_input{
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}

export interface GetNewDirectOrder_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}
}

   /** Required : 
      @param ordNum
      @param checkPCID
      @param ds
   */  
export interface GetNewFromOrderWithPCID_input{
      /**  The transfer order number  */  
   ordNum:string,
      /**  When true, prevent orders that have allocations with PCID, from being created.  */  
   checkPCID:boolean,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface GetNewFromOrderWithPCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param ordNum
      @param ds
   */  
export interface GetNewFromOrder_input{
      /**  The transfer order number  */  
   ordNum:string,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface GetNewFromOrder_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param ds
      @param relatedToFile
      @param packNum
      @param packLine
   */  
export interface GetNewShipCOO_input{
   ds:Erp_Tablesets_TransOrderShipTableset[],
   relatedToFile:string,
   packNum:number,
   packLine:number,
}

export interface GetNewShipCOO_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param ds
      @param packNum
   */  
export interface GetNewTFShipDtl_input{
   ds:Erp_Tablesets_TransOrderShipTableset[],
   packNum:number,
}

export interface GetNewTFShipDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param ds
      @param packNum
   */  
export interface GetNewTFShipHeadAttch_input{
   ds:Erp_Tablesets_TransOrderShipTableset[],
   packNum:number,
}

export interface GetNewTFShipHeadAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param ds
      @param packNum
   */  
export interface GetNewTFShipHeadInsurance_input{
   ds:Erp_Tablesets_TransOrderShipTableset[],
   packNum:number,
}

export interface GetNewTFShipHeadInsurance_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param ds
      @param packNum
   */  
export interface GetNewTFShipHeadTrailer_input{
   ds:Erp_Tablesets_TransOrderShipTableset[],
   packNum:number,
}

export interface GetNewTFShipHeadTrailer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewTFShipHead_input{
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface GetNewTFShipHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param ds
      @param packNum
   */  
export interface GetNewTFShipUPS_input{
   ds:Erp_Tablesets_TransOrderShipTableset[],
   packNum:number,
}

export interface GetNewTFShipUPS_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
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
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface GetPackClass_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param ipPkgCode
      @param ds
   */  
export interface GetPackaging_input{
   ipPkgCode:string,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface GetPackaging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetPayBTFlagDefaults_input{
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface GetPayBTFlagDefaults_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param whereClauseTFShipHead
      @param whereClauseTFShipHeadAttch
      @param whereClauseTFShipDtl
      @param whereClauseShipCOO
      @param whereClauseCartonTrkDtl
      @param whereClauseTFShipHeadInsurance
      @param whereClauseTFShipHeadTrailer
      @param whereClauseTFShipUPS
      @param whereClauseLegalNumGenOpts
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSNFormat
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseTFShipHead:string,
   whereClauseTFShipHeadAttch:string,
   whereClauseTFShipDtl:string,
   whereClauseShipCOO:string,
   whereClauseCartonTrkDtl:string,
   whereClauseTFShipHeadInsurance:string,
   whereClauseTFShipHeadTrailer:string,
   whereClauseTFShipUPS:string,
   whereClauseLegalNumGenOpts:string,
   whereClauseSelectedSerialNumbers:string,
   whereClauseSNFormat:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_TransOrderShipTableset[],
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
   ScaleID:string,
}
}

   /** Required : 
      @param ipPartNum
      @param attributeSetID
      @param ipWarehouseCode
      @param ipBinNum
      @param ipQuantity
      @param ipUOM
      @param ipTransType
      @param ipSourceRowID
   */  
export interface GetSelectSerialNumbersParams_input{
      /**  Part Number  */  
   ipPartNum:string,
   attributeSetID:number,
      /**  Warehouse Code  */  
   ipWarehouseCode:string,
      /**  Bin Num  */  
   ipBinNum:string,
      /**  Quantity  */  
   ipQuantity:number,
      /**  UOM  */  
   ipUOM:string,
      /**  TransType  */  
   ipTransType:string,
      /**  sourceRowID  */  
   ipSourceRowID:string,
}

export interface GetSelectSerialNumbersParams_output{
   returnObj:Erp_Tablesets_SelectSerialNumbersParamsTableset[],
}

   /** Required : 
      @param iPackNum
      @param iPackLine
      @param ds
   */  
export interface GetShipCOOTotals_input{
      /**  Pack Number  */  
   iPackNum:number,
      /**  Pack Line Number  */  
   iPackLine:number,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface GetShipCOOTotals_output{
parameters : {
      /**  output parameters  */  
   totalQuantityPercent:number,
   totalValuePercent:number,
}
}

   /** Required : 
      @param ipTranDocTypeID
      @param ds
   */  
export interface GetTranDocTypeID_input{
      /**  TranDocTypeID supplied  */  
   ipTranDocTypeID:string,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface GetTranDocTypeID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
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
      @param ipPart
      @param ipWhse
   */  
export interface IsSerialTracked_input{
      /**  Part  */  
   ipPart:string,
   ipWhse:string,
}

export interface IsSerialTracked_output{
   returnObj:boolean,
}

   /** Required : 
      @param shipViaCode
      @param ds
   */  
export interface OnChangeShipViaCode_input{
      /**  New ShipVia Code  */  
   shipViaCode:string,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface OnChangeShipViaCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param attributeSetID
      @param ds
   */  
export interface OnChangingTFOrdDtlAttributeSet_input{
   attributeSetID:number,
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}

export interface OnChangingTFOrdDtlAttributeSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}
}

   /** Required : 
      @param numberOfPieces
      @param ds
   */  
export interface OnChangingTFOrdDtlNumberOfPieces_input{
   numberOfPieces:number,
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}

export interface OnChangingTFOrdDtlNumberOfPieces_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}
}

   /** Required : 
      @param attributeSetID
      @param ds
   */  
export interface OnChangingTFShipDtlAttributeSet_input{
   attributeSetID:number,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface OnChangingTFShipDtlAttributeSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param numberOfPieces
      @param ds
   */  
export interface OnChangingTFShipDtlNumberOfPieces_input{
   numberOfPieces:number,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface OnChangingTFShipDtlNumberOfPieces_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param ipStatus
      @param ds
   */  
export interface POChangeStatus_input{
      /**  Selected Status
            Valid Options: Open, Close, Void, UnVoid, Freight, UnFreight, Stage  */  
   ipStatus:string,
   ds:Erp_Tablesets_PackOutTableset[],
}

export interface POChangeStatus_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackOutTableset[],
}
}

   /** Required : 
      @param ipOrderNum
      @param ipPackNum
      @param ds
   */  
export interface POCreateDtlList_input{
      /**  TFOrdNum value  */  
   ipOrderNum:string,
      /**  PackNum value  */  
   ipPackNum:number,
   ds:Erp_Tablesets_PackOutTableset[],
}

export interface POCreateDtlList_output{
parameters : {
      /**  output parameters  */  
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
   Found:number,
   Rowident:string,
   ds:Erp_Tablesets_PackOutTableset[],
}
}

   /** Required : 
      @param ipPackNum
   */  
export interface POGetDtlList_input{
      /**  Carton to get the detail lines from  */  
   ipPackNum:number,
}

export interface POGetDtlList_output{
   returnObj:Erp_Tablesets_PackOutTableset[],
}

   /** Required : 
      @param ipPackNum
   */  
export interface POGetNewWithDtl_input{
   ipPackNum:number,
}

export interface POGetNewWithDtl_output{
   returnObj:Erp_Tablesets_PackOutTableset[],
}

   /** Required : 
      @param ipPackNum
   */  
export interface POGetNew_input{
      /**  Packing number  */  
   ipPackNum:number,
}

export interface POGetNew_output{
   returnObj:Erp_Tablesets_PackOutTableset[],
}

   /** Required : 
      @param ds
   */  
export interface POUndo_input{
   ds:Erp_Tablesets_PackOutTableset[],
}

export interface POUndo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackOutTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface POUpdateHeader_input{
   ds:Erp_Tablesets_PackOutTableset[],
}

export interface POUpdateHeader_output{
   returnObj:Erp_Tablesets_TransOrderShipTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PackOutTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface POUpdate_input{
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
      @param PackNum
      @param PackLine
   */  
export interface PreDeleteDirectShip_input{
      /**  Pack number.  */  
   PackNum:number,
      /**  Pack line number.  */  
   PackLine:number,
}

export interface PreDeleteDirectShip_output{
parameters : {
      /**  output parameters  */  
   cMessage:string,
}
}

   /** Required : 
      @param ipPackNum
      @param ipPackLine
      @param ipPartNum
      @param ds
   */  
export interface PreDeselectSN_input{
   ipPackNum:number,
   ipPackLine:number,
   ipPartNum:string,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface PreDeselectSN_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param ipTFShipHeadRowID
   */  
export interface PreShipPack_input{
      /**  TFShipHead.SysRowID  */  
   ipTFShipHeadRowID:string,
}

export interface PreShipPack_output{
parameters : {
      /**  output parameters  */  
   cErrorMsg:string,
}
}

   /** Required : 
      @param proposedShipped
      @param ipTFShipHeadRowID
   */  
export interface PreUnShipPack_input{
      /**  Proposed value from UI  */  
   proposedShipped:boolean,
      /**  TFShipHead.SysRowID  */  
   ipTFShipHeadRowID:string,
}

export interface PreUnShipPack_output{
}

   /** Required : 
      @param ipPackNum
      @param ipPCID
      @param ds
   */  
export interface RemovePCID_input{
      /**  ipPackNum  */  
   ipPackNum:number,
      /**  ipPCID  */  
   ipPCID:string,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface RemovePCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
   opPCIDCount:number,
}
}

   /** Required : 
      @param ipQVEnable
      @param ds
   */  
export interface SetUPSQVEnable_input{
   ipQVEnable:boolean,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface SetUPSQVEnable_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param ipShipStatus
      @param ds
   */  
export interface SetUPSQVShipStatus_input{
   ipShipStatus:string,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface SetUPSQVShipStatus_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param ipTFShipHeadRowid
      @param ipReturn
   */  
export interface ShipPackingSlip_input{
      /**  The rowid of the TFShipHead to ship  */  
   ipTFShipHeadRowid:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
}

export interface ShipPackingSlip_output{
   returnObj:Erp_Tablesets_TransOrderShipTableset[],
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface TFOrdDtl_OnChangingRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}

export interface TFOrdDtl_OnChangingRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TranDirectOrderTableset[],
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface TFShipDtl_OnChangingRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface TFShipDtl_OnChangingRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param ipTFShipHeadRowid
      @param ipReturn
   */  
export interface UnShipPackingSlip_input{
      /**  The rowid of the TFShipHead to unship  */  
   ipTFShipHeadRowid:string,
      /**  Logical used to determine if you would like the dataset refreshed and brought back.  */  
   ipReturn:boolean,
}

export interface UnShipPackingSlip_output{
   returnObj:Erp_Tablesets_TransOrderShipTableset[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtTransOrderShipTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtTransOrderShipTableset[],
   errorsOccurred:boolean,
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
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface UpdatePackCODWithCarton_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
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
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface UpdatePackDeclaredWithCarton_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
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
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface UpdatePackWeightWithCarton_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
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
      @param ipPartNum
   */  
export interface ValidatePartNum_input{
   ipPartNum:string,
}

export interface ValidatePartNum_output{
}

   /** Required : 
      @param ipWarehouseCode
      @param ipPartNum
      @param attributeSetID
      @param ipTFOrdNum
      @param ipTFOrdLine
      @param serialNumber
   */  
export interface ValidateSN_input{
      /**  The Warhouse Code  */  
   ipWarehouseCode:string,
      /**  The Part Number  */  
   ipPartNum:string,
   attributeSetID:number,
      /**  The Transfer Order Number  */  
   ipTFOrdNum:string,
      /**  The Transfer Order Line  */  
   ipTFOrdLine:number,
      /**  Serial number to validate.  */  
   serialNumber:string,
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
   returnObj:Erp_Tablesets_TransOrderShipTableset[],
}

   /** Required : 
      @param ipBinNum
      @param ds
   */  
export interface WarnNegativeBinOH_input{
      /**  The new proposed TFShipDtl.BinNum value  */  
   ipBinNum:string,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface WarnNegativeBinOH_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
   outMessage:string,
   outNegQtyAction:string,
}
}

   /** Required : 
      @param ipDisplayQty
      @param ds
   */  
export interface WarnNegativeBinQty_input{
      /**  The new proposed TFShipDtl.DisplayShipQty value  */  
   ipDisplayQty:number,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface WarnNegativeBinQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
   outMessage:string,
   outNegQtyAction:string,
}
}

   /** Required : 
      @param packNum
      @param packLine
      @param ipLotNum
      @param ds
   */  
export interface WarnNegativeLotOH_input{
      /**  Pack Number to be modified  */  
   packNum:number,
      /**  Pack Line to be modified  */  
   packLine:number,
      /**  The new proposed TFShipDtl.LotNum value  */  
   ipLotNum:string,
   ds:Erp_Tablesets_TransOrderShipTableset[],
}

export interface WarnNegativeLotOH_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransOrderShipTableset[],
   outMessage:string,
   outNegQtyAction:string,
}
}

