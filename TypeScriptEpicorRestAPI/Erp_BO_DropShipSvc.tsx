import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.DropShipSvc
// Description: Business Object for Drop Shipment
// Version: v1
*/ 



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
   Description: Get DropShips items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DropShips
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DropShipHeadRow
   */  
export function get_DropShips(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DropShips
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DropShipHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.DropShipHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DropShips(requestBody:Erp_Tablesets_DropShipHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DropShip item
   Description: Calls GetByID to retrieve the DropShip item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DropShip
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DropShipHeadRow
   */  
export function get_DropShips_Company_VendorNum_PurPoint_PackSlip(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DropShipHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_DropShipHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DropShip for the service
   Description: Calls UpdateExt to update DropShip. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DropShip
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.DropShipHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DropShips_Company_VendorNum_PurPoint_PackSlip(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, requestBody:Erp_Tablesets_DropShipHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete DropShip item
   Description: Call UpdateExt to delete DropShip item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DropShip
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DropShips_Company_VendorNum_PurPoint_PackSlip(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
   Description: Get DropShipDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DropShipDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DropShipDtlRow
   */  
export function get_DropShips_Company_VendorNum_PurPoint_PackSlip_DropShipDtls(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/DropShipDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DropShipDtl item
   Description: Calls GetByID to retrieve the DropShipDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DropShipDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DropShipDtlRow
   */  
export function get_DropShips_Company_VendorNum_PurPoint_PackSlip_DropShipDtls_Company_VendorNum_PurPoint_PackSlip_PackLine(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DropShipDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/DropShipDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_DropShipDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get DropShipHeadTrailers items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DropShipHeadTrailers1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DropShipHeadTrailerRow
   */  
export function get_DropShips_Company_VendorNum_PurPoint_PackSlip_DropShipHeadTrailers(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipHeadTrailerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/DropShipHeadTrailers", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipHeadTrailerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DropShipHeadTrailer item
   Description: Calls GetByID to retrieve the DropShipHeadTrailer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DropShipHeadTrailer1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param LicensePlate Desc: LicensePlate   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DropShipHeadTrailerRow
   */  
export function get_DropShips_Company_VendorNum_PurPoint_PackSlip_DropShipHeadTrailers_Company_VendorNum_PurPoint_PackSlip_LicensePlate(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, LicensePlate:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DropShipHeadTrailerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/DropShipHeadTrailers(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + LicensePlate + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_DropShipHeadTrailerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get MXDropShipHeadInsurances items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MXDropShipHeadInsurances1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MXDropShipHeadInsuranceRow
   */  
export function get_DropShips_Company_VendorNum_PurPoint_PackSlip_MXDropShipHeadInsurances(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXDropShipHeadInsuranceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/MXDropShipHeadInsurances", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXDropShipHeadInsuranceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MXDropShipHeadInsurance item
   Description: Calls GetByID to retrieve the MXDropShipHeadInsurance item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MXDropShipHeadInsurance1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param InsuranceSeq Desc: InsuranceSeq   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MXDropShipHeadInsuranceRow
   */  
export function get_DropShips_Company_VendorNum_PurPoint_PackSlip_MXDropShipHeadInsurances_Company_VendorNum_PurPoint_PackSlip_InsuranceSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, InsuranceSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MXDropShipHeadInsuranceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/MXDropShipHeadInsurances(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + InsuranceSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_MXDropShipHeadInsuranceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get DropShipHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DropShipHeadAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DropShipHeadAttchRow
   */  
export function get_DropShips_Company_VendorNum_PurPoint_PackSlip_DropShipHeadAttches(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/DropShipHeadAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DropShipHeadAttch item
   Description: Calls GetByID to retrieve the DropShipHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DropShipHeadAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DropShipHeadAttchRow
   */  
export function get_DropShips_Company_VendorNum_PurPoint_PackSlip_DropShipHeadAttches_Company_VendorNum_PurPoint_PackSlip_DrawingSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DropShipHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShips(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/DropShipHeadAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_DropShipHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get DropShipDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DropShipDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DropShipDtlRow
   */  
export function get_DropShipDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DropShipDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DropShipDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.DropShipDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DropShipDtls(requestBody:Erp_Tablesets_DropShipDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DropShipDtl item
   Description: Calls GetByID to retrieve the DropShipDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DropShipDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DropShipDtlRow
   */  
export function get_DropShipDtls_Company_VendorNum_PurPoint_PackSlip_PackLine(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DropShipDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_DropShipDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DropShipDtl for the service
   Description: Calls UpdateExt to update DropShipDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DropShipDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.DropShipDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DropShipDtls_Company_VendorNum_PurPoint_PackSlip_PackLine(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, requestBody:Erp_Tablesets_DropShipDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete DropShipDtl item
   Description: Call UpdateExt to delete DropShipDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DropShipDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DropShipDtls_Company_VendorNum_PurPoint_PackSlip_PackLine(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
   Description: Get DropShipHeadTrailers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DropShipHeadTrailers
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DropShipHeadTrailerRow
   */  
export function get_DropShipHeadTrailers(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipHeadTrailerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipHeadTrailers", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipHeadTrailerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DropShipHeadTrailers
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DropShipHeadTrailerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.DropShipHeadTrailerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DropShipHeadTrailers(requestBody:Erp_Tablesets_DropShipHeadTrailerRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipHeadTrailers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DropShipHeadTrailer item
   Description: Calls GetByID to retrieve the DropShipHeadTrailer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DropShipHeadTrailer
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param LicensePlate Desc: LicensePlate   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DropShipHeadTrailerRow
   */  
export function get_DropShipHeadTrailers_Company_VendorNum_PurPoint_PackSlip_LicensePlate(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, LicensePlate:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DropShipHeadTrailerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipHeadTrailers(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + LicensePlate + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_DropShipHeadTrailerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DropShipHeadTrailer for the service
   Description: Calls UpdateExt to update DropShipHeadTrailer. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DropShipHeadTrailer
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param LicensePlate Desc: LicensePlate   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.DropShipHeadTrailerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DropShipHeadTrailers_Company_VendorNum_PurPoint_PackSlip_LicensePlate(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, LicensePlate:string, requestBody:Erp_Tablesets_DropShipHeadTrailerRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipHeadTrailers(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + LicensePlate + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete DropShipHeadTrailer item
   Description: Call UpdateExt to delete DropShipHeadTrailer item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DropShipHeadTrailer
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param LicensePlate Desc: LicensePlate   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DropShipHeadTrailers_Company_VendorNum_PurPoint_PackSlip_LicensePlate(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, LicensePlate:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipHeadTrailers(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + LicensePlate + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
   Description: Get MXDropShipHeadInsurances items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MXDropShipHeadInsurances
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MXDropShipHeadInsuranceRow
   */  
export function get_MXDropShipHeadInsurances(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXDropShipHeadInsuranceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/MXDropShipHeadInsurances", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXDropShipHeadInsuranceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MXDropShipHeadInsurances
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MXDropShipHeadInsuranceRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MXDropShipHeadInsuranceRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MXDropShipHeadInsurances(requestBody:Erp_Tablesets_MXDropShipHeadInsuranceRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/MXDropShipHeadInsurances", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MXDropShipHeadInsurance item
   Description: Calls GetByID to retrieve the MXDropShipHeadInsurance item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MXDropShipHeadInsurance
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param InsuranceSeq Desc: InsuranceSeq   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MXDropShipHeadInsuranceRow
   */  
export function get_MXDropShipHeadInsurances_Company_VendorNum_PurPoint_PackSlip_InsuranceSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, InsuranceSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MXDropShipHeadInsuranceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/MXDropShipHeadInsurances(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + InsuranceSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_MXDropShipHeadInsuranceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MXDropShipHeadInsurance for the service
   Description: Calls UpdateExt to update MXDropShipHeadInsurance. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MXDropShipHeadInsurance
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param InsuranceSeq Desc: InsuranceSeq   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MXDropShipHeadInsuranceRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MXDropShipHeadInsurances_Company_VendorNum_PurPoint_PackSlip_InsuranceSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, InsuranceSeq:string, requestBody:Erp_Tablesets_MXDropShipHeadInsuranceRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/MXDropShipHeadInsurances(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + InsuranceSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete MXDropShipHeadInsurance item
   Description: Call UpdateExt to delete MXDropShipHeadInsurance item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MXDropShipHeadInsurance
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param InsuranceSeq Desc: InsuranceSeq   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MXDropShipHeadInsurances_Company_VendorNum_PurPoint_PackSlip_InsuranceSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, InsuranceSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/MXDropShipHeadInsurances(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + InsuranceSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
   Description: Get DropShipHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DropShipHeadAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DropShipHeadAttchRow
   */  
export function get_DropShipHeadAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipHeadAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DropShipHeadAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DropShipHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.DropShipHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DropShipHeadAttches(requestBody:Erp_Tablesets_DropShipHeadAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipHeadAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DropShipHeadAttch item
   Description: Calls GetByID to retrieve the DropShipHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DropShipHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DropShipHeadAttchRow
   */  
export function get_DropShipHeadAttches_Company_VendorNum_PurPoint_PackSlip_DrawingSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DropShipHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipHeadAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_DropShipHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DropShipHeadAttch for the service
   Description: Calls UpdateExt to update DropShipHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DropShipHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.DropShipHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DropShipHeadAttches_Company_VendorNum_PurPoint_PackSlip_DrawingSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, DrawingSeq:string, requestBody:Erp_Tablesets_DropShipHeadAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipHeadAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + DrawingSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete DropShipHeadAttch item
   Description: Call UpdateExt to delete DropShipHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DropShipHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DropShipHeadAttches_Company_VendorNum_PurPoint_PackSlip_DrawingSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DropShipHeadAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + DrawingSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumGenOptsRow
   */  
export function get_LegalNumGenOpts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/LegalNumGenOpts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LegalNumGenOpts(requestBody:Erp_Tablesets_LegalNumGenOptsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/LegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   */  
export function get_LegalNumGenOpts_Company_LegalNumberID(Company:string, LegalNumberID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LegalNumGenOptsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LegalNumGenOpts_Company_LegalNumberID(Company:string, LegalNumberID:string, requestBody:Erp_Tablesets_LegalNumGenOptsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
   Description: Get PendingDropShipDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PendingDropShipDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PendingDropShipDtlRow
   */  
export function get_PendingDropShipDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PendingDropShipDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/PendingDropShipDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PendingDropShipDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PendingDropShipDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PendingDropShipDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PendingDropShipDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PendingDropShipDtls(requestBody:Erp_Tablesets_PendingDropShipDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/PendingDropShipDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PendingDropShipDtl item
   Description: Calls GetByID to retrieve the PendingDropShipDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PendingDropShipDtl
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PendingDropShipDtlRow
   */  
export function get_PendingDropShipDtls_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PendingDropShipDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/PendingDropShipDtls(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PendingDropShipDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PendingDropShipDtl for the service
   Description: Calls UpdateExt to update PendingDropShipDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PendingDropShipDtl
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PendingDropShipDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PendingDropShipDtls_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_PendingDropShipDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/PendingDropShipDtls(" + SysRowID + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete PendingDropShipDtl item
   Description: Call UpdateExt to delete PendingDropShipDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PendingDropShipDtl
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PendingDropShipDtls_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/PendingDropShipDtls(" + SysRowID + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SelectedSerialNumbersRow
   */  
export function get_SelectedSerialNumbers(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/SelectedSerialNumbers", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectedSerialNumbers(requestBody:Erp_Tablesets_SelectedSerialNumbersRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/SelectedSerialNumbers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   */  
export function get_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company:string, PartNum:string, SerialNumber:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SelectedSerialNumbersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company:string, PartNum:string, SerialNumber:string, requestBody:Erp_Tablesets_SelectedSerialNumbersRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SNFormatRow
   */  
export function get_SNFormats(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/SNFormats", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.SNFormatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SNFormats(requestBody:Erp_Tablesets_SNFormatRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/SNFormats", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.SNFormatRow
   */  
export function get_SNFormats_Company_PartNum_Plant(Company:string, PartNum:string, Plant:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SNFormatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SNFormats_Company_PartNum_Plant(Company:string, PartNum:string, Plant:string, requestBody:Erp_Tablesets_SNFormatRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DropShipHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipHeadListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseDropShipHead:string, whereClauseDropShipHeadAttch:string, whereClauseDropShipDtl:string, whereClauseDropShipHeadTrailer:string, whereClauseMXDropShipHeadInsurance:string, whereClauseLegalNumGenOpts:string, whereClausePendingDropShipDtl:string, whereClauseSelectedSerialNumbers:string, whereClauseSNFormat:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseDropShipHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDropShipHead=" + whereClauseDropShipHead
   }
   if(typeof whereClauseDropShipHeadAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDropShipHeadAttch=" + whereClauseDropShipHeadAttch
   }
   if(typeof whereClauseDropShipDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDropShipDtl=" + whereClauseDropShipDtl
   }
   if(typeof whereClauseDropShipHeadTrailer!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDropShipHeadTrailer=" + whereClauseDropShipHeadTrailer
   }
   if(typeof whereClauseMXDropShipHeadInsurance!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMXDropShipHeadInsurance=" + whereClauseMXDropShipHeadInsurance
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
   if(typeof whereClausePendingDropShipDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePendingDropShipDtl=" + whereClausePendingDropShipDtl
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

   return (new Promise<GetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRows_output)
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(vendorNum:string, purPoint:string, packSlip:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof vendorNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "vendorNum=" + vendorNum
   }
   if(typeof purPoint!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "purPoint=" + purPoint
   }
   if(typeof packSlip!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "packSlip=" + packSlip
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetByID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildCustomersToList
   Description: If the Order has releases to multiple Customer, this will return the list of available
Customers
   OperationID: BuildCustomersToList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildCustomersToList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildCustomersToList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildCustomersToList(requestBody:BuildCustomersToList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildCustomersToList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/BuildCustomersToList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as BuildCustomersToList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildShipToCustList
   Description: Return a list of Ship To Customers.
Customers
   OperationID: BuildShipToCustList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildShipToCustList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildShipToCustList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildShipToCustList(requestBody:BuildShipToCustList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildShipToCustList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/BuildShipToCustList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as BuildShipToCustList_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildShipToList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildShipToList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildShipToList(requestBody:BuildShipToList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildShipToList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/BuildShipToList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as BuildShipToList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDropShipDtlComplete
   Description: Updates the Complete of DropShipDtl.
   OperationID: ChangeDropShipDtlComplete
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDropShipDtlComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDropShipDtlComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDropShipDtlComplete(requestBody:ChangeDropShipDtlComplete_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDropShipDtlComplete_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/ChangeDropShipDtlComplete", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDropShipDtlComplete_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDropShipDtlIUM
   Description: Updates the IUM of DropShipDtl.
   OperationID: ChangeDropShipDtlIUM
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDropShipDtlIUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDropShipDtlIUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDropShipDtlIUM(requestBody:ChangeDropShipDtlIUM_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDropShipDtlIUM_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/ChangeDropShipDtlIUM", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDropShipDtlIUM_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDropShipDtlLotNum
   Description: Updates the LotNum of DropShipDtl.
   OperationID: ChangeDropShipDtlLotNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDropShipDtlLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDropShipDtlLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDropShipDtlLotNum(requestBody:ChangeDropShipDtlLotNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDropShipDtlLotNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/ChangeDropShipDtlLotNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDropShipDtlLotNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDropShipDtlOurQty
   Description: Updates the OurQty of DropShipDtl.
   OperationID: ChangeDropShipDtlOurQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDropShipDtlOurQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDropShipDtlOurQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDropShipDtlOurQty(requestBody:ChangeDropShipDtlOurQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDropShipDtlOurQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/ChangeDropShipDtlOurQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDropShipDtlOurQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDropShipDtlPOLine
   Description: Updates the POLine of DropShipDtl.
   OperationID: ChangeDropShipDtlPOLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDropShipDtlPOLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDropShipDtlPOLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDropShipDtlPOLine(requestBody:ChangeDropShipDtlPOLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDropShipDtlPOLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/ChangeDropShipDtlPOLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDropShipDtlPOLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDropShipDtlPONum
   Description: Updates the PONum of DropShipDtl.
   OperationID: ChangeDropShipDtlPONum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDropShipDtlPONum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDropShipDtlPONum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDropShipDtlPONum(requestBody:ChangeDropShipDtlPONum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDropShipDtlPONum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/ChangeDropShipDtlPONum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDropShipDtlPONum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDropShipDtlPORelNum
   Description: Updates the PORelNum of DropShipDtl.
   OperationID: ChangeDropShipDtlPORelNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDropShipDtlPORelNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDropShipDtlPORelNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDropShipDtlPORelNum(requestBody:ChangeDropShipDtlPORelNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDropShipDtlPORelNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/ChangeDropShipDtlPORelNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDropShipDtlPORelNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDropShipDtlVendorQty
   Description: Updates the VendorQty of DropShipDtl.
   OperationID: ChangeDropShipDtlVendorQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDropShipDtlVendorQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDropShipDtlVendorQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDropShipDtlVendorQty(requestBody:ChangeDropShipDtlVendorQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDropShipDtlVendorQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/ChangeDropShipDtlVendorQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDropShipDtlVendorQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDropShipHeadPONum
   Description: Call this method when the PONum changes on the DropShipHead.
   OperationID: ChangeDropShipHeadPONum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDropShipHeadPONum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDropShipHeadPONum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDropShipHeadPONum(requestBody:ChangeDropShipHeadPONum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDropShipHeadPONum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/ChangeDropShipHeadPONum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDropShipHeadPONum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDropShipHeadShipToCustNum
   Description: Call this method when the ShipToCustNum changes on the DropShipHead.
   OperationID: ChangeDropShipHeadShipToCustNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDropShipHeadShipToCustNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDropShipHeadShipToCustNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDropShipHeadShipToCustNum(requestBody:ChangeDropShipHeadShipToCustNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDropShipHeadShipToCustNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/ChangeDropShipHeadShipToCustNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDropShipHeadShipToCustNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDropShipHeadShipToNum
   Description: Call this method when the ShipToCustNum changes on the DropShipHead.
   OperationID: ChangeDropShipHeadShipToNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDropShipHeadShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDropShipHeadShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDropShipHeadShipToNum(requestBody:ChangeDropShipHeadShipToNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDropShipHeadShipToNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/ChangeDropShipHeadShipToNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDropShipHeadShipToNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new our qty
   OperationID: OnChangingNumberOfPieces
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingNumberOfPieces(requestBody:OnChangingNumberOfPieces_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingNumberOfPieces_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/OnChangingNumberOfPieces", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangingNumberOfPieces_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeShipViaCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeShipViaCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeShipViaCode(requestBody:OnChangeShipViaCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeShipViaCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/OnChangeShipViaCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeShipViaCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateMassDropShipDtl
   Description: The Create Mass Drop Ship method.
   OperationID: CreateMassDropShipDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateMassDropShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateMassDropShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateMassDropShipDtl(requestBody:CreateMassDropShipDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateMassDropShipDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/CreateMassDropShipDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CreateMassDropShipDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetOrderShipments
   Description: This method creates the data for the tables ShipDtl and DropShipDtl
   OperationID: GetOrderShipments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetOrderShipments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrderShipments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOrderShipments(requestBody:GetOrderShipments_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetOrderShipments_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/GetOrderShipments", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetOrderShipments_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPendingDtl
   Description: Updates PendingDropShipDtl.
   OperationID: GetPendingDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPendingDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPendingDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPendingDtl(requestBody:GetPendingDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPendingDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/GetPendingDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPendingDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPOInfo
   Description: This method returns default information for the PO Number and the new Vendor ID
information.
   OperationID: GetPOInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPOInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPOInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPOInfo(requestBody:GetPOInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPOInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/GetPOInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPOInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMXCartaPortePOInfo
   Description: Function to set Mexico Carta Porte fields default values
   OperationID: GetMXCartaPortePOInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetMXCartaPortePOInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMXCartaPortePOInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMXCartaPortePOInfo(requestBody:GetMXCartaPortePOInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetMXCartaPortePOInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/GetMXCartaPortePOInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetMXCartaPortePOInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPurPointInfo
   Description: This method returns default information for the Vendor Purchase Point.
   OperationID: GetPurPointInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPurPointInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPurPointInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPurPointInfo(requestBody:GetPurPointInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPurPointInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/GetPurPointInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPurPointInfo_output)
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
<param name="ipPartNum">ipPartNum</param><param name="ipAttributeSetID"></param><param name="ipQuantity">ipQuantity</param><param name="ipUOM">ipUOM</param><param name="ipVendNum">ipVendNum</param><param name="ipVendPP">ipVendPP</param><param name="ipPackSlip">ipPackSlip</param><param name="ipPackSlipLine">ipPackSlipLine</param><param name="ipPONum">PO Number</param><param name="ipPOLine">PO Line Number</param><param name="ipPORelNum">PO Release Number</param><returns></returns>
   OperationID: GetSelectSerialNumbersParams
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectSerialNumbersParams(requestBody:GetSelectSerialNumbersParams_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSelectSerialNumbersParams_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/GetSelectSerialNumbersParams", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetSelectSerialNumbersParams_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetShipToAddressMultiKey
   Description: This method builds the ShipTo Address
   OperationID: GetShipToAddressMultiKey
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetShipToAddressMultiKey_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShipToAddressMultiKey_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetShipToAddressMultiKey(requestBody:GetShipToAddressMultiKey_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetShipToAddressMultiKey_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/GetShipToAddressMultiKey", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetShipToAddressMultiKey_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetVendorInfo
   Description: This method returns default information for the Vendor.
   OperationID: GetVendorInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetVendorInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetVendorInfo(requestBody:GetVendorInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetVendorInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/GetVendorInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetVendorInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MarkShipmentLines
   Description: This method sets all the temp-table records to be drop shipped (Ship all button selected)
   OperationID: MarkShipmentLines
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MarkShipmentLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MarkShipmentLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MarkShipmentLines(requestBody:MarkShipmentLines_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MarkShipmentLines_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/MarkShipmentLines", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MarkShipmentLines_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PostUpdate
   Description: This method will return a message if a credit card drop shipment was processed
   OperationID: PostUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PostUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PostUpdate(requestBody:PostUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PostUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/PostUpdate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PostUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method processExtraCreditCharge
   OperationID: processExtraCreditCharge
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/processExtraCreditCharge_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/processExtraCreditCharge_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_processExtraCreditCharge(requestBody:processExtraCreditCharge_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<processExtraCreditCharge_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/processExtraCreditCharge", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as processExtraCreditCharge_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreChangeDropShipDtlLotNum
   Description: This method returns an error or question if the LotNum field does not exist
depending upon the security of the user
   OperationID: PreChangeDropShipDtlLotNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreChangeDropShipDtlLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreChangeDropShipDtlLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreChangeDropShipDtlLotNum(requestBody:PreChangeDropShipDtlLotNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreChangeDropShipDtlLotNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/PreChangeDropShipDtlLotNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PreChangeDropShipDtlLotNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreCreateMassReceipt
   Description: The Pre Create Mass Drop Ship method.
   OperationID: PreCreateMassReceipt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreCreateMassReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreCreateMassReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreCreateMassReceipt(requestBody:PreCreateMassReceipt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreCreateMassReceipt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/PreCreateMassReceipt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PreCreateMassReceipt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreUpdateDropShipDtl
   Description: This method is to be called right before the update method is called.
   OperationID: PreUpdateDropShipDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreUpdateDropShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdateDropShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreUpdateDropShipDtl(requestBody:PreUpdateDropShipDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreUpdateDropShipDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/PreUpdateDropShipDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PreUpdateDropShipDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UndoShipAll
   Description: This method re-sets all the temp-table records drop shipped (Undo Ship all button selected)
   OperationID: UndoShipAll
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UndoShipAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UndoShipAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UndoShipAll(requestBody:UndoShipAll_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UndoShipAll_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/UndoShipAll", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UndoShipAll_output)
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
<param name="ipPartNum">Part Number</param><param name="ipAttributeSetID"></param><param name="ipSerialNo">Serial Number</param><param name="ipVendNum">Vendor Number</param><param name="ipPurPoint">Pur Point</param><param name="ipPackNum">Pack Number</param><param name="ipPONum">PO Number</param><param name="ipPOLine">PO Line Number</param><param name="ipPORelNum">PO Release Number</param>
   OperationID: ValidateSN
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSN(requestBody:ValidateSN_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateSN_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/ValidateSN", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateSN_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AssignLegalNumber
   Description: Assigns a legal number to the drop shipment.
   OperationID: AssignLegalNumber
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AssignLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssignLegalNumber(requestBody:AssignLegalNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AssignLegalNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/AssignLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as AssignLegalNumber_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLegalNumGenOpts(requestBody:GetLegalNumGenOpts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLegalNumGenOpts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/GetLegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetLegalNumGenOpts_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/VoidLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VoidLegalNumber(requestBody:VoidLegalNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<VoidLegalNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/VoidLegalNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as VoidLegalNumber_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTranDocTypeID
   Description: Sets default values when the TranDocTypeID changes.
   OperationID: GetTranDocTypeID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTranDocTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTranDocTypeID(requestBody:GetTranDocTypeID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTranDocTypeID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/GetTranDocTypeID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetTranDocTypeID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMultiKeySearchPONum
   Description: On Column Change MultiKeySearch PONum.
   OperationID: OnChangeMultiKeySearchPONum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMultiKeySearchPONum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMultiKeySearchPONum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMultiKeySearchPONum(requestBody:OnChangeMultiKeySearchPONum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMultiKeySearchPONum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/OnChangeMultiKeySearchPONum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeMultiKeySearchPONum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildAddressField
   Description: Build Address Field.
   OperationID: BuildAddressField
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildAddressField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildAddressField_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildAddressField(requestBody:BuildAddressField_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildAddressField_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/BuildAddressField", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as BuildAddressField_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InitializeMultiKeySearchData
   Description: Initialize MultiKeySearch Data.
   OperationID: InitializeMultiKeySearchData
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/InitializeMultiKeySearchData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitializeMultiKeySearchData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InitializeMultiKeySearchData(requestBody:InitializeMultiKeySearchData_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<InitializeMultiKeySearchData_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/InitializeMultiKeySearchData", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as InitializeMultiKeySearchData_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildShipToCustListWithOutputParameters
   Description: Build ShipTo Customer List, with output parameters.
   OperationID: BuildShipToCustListWithOutputParameters
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildShipToCustListWithOutputParameters_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildShipToCustListWithOutputParameters_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildShipToCustListWithOutputParameters(requestBody:BuildShipToCustListWithOutputParameters_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildShipToCustListWithOutputParameters_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/BuildShipToCustListWithOutputParameters", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as BuildShipToCustListWithOutputParameters_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildShipToListWithParameters
   Description: Build ShipTo List, with out parameters.
   OperationID: BuildShipToListWithParameters
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildShipToListWithParameters_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildShipToListWithParameters_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildShipToListWithParameters(requestBody:BuildShipToListWithParameters_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildShipToListWithParameters_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/BuildShipToListWithParameters", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as BuildShipToListWithParameters_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method buildShipToAddressFieldMultiKey
   Description: build ShipTo Address.
   OperationID: buildShipToAddressFieldMultiKey
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/buildShipToAddressFieldMultiKey_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/buildShipToAddressFieldMultiKey_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_buildShipToAddressFieldMultiKey(requestBody:buildShipToAddressFieldMultiKey_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<buildShipToAddressFieldMultiKey_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/buildShipToAddressFieldMultiKey", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as buildShipToAddressFieldMultiKey_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteDropShipDtl
   Description: Delete DropShipDtl method when dataset has several DropShipDtl records in state 'Added'.
   OperationID: DeleteDropShipDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteDropShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteDropShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteDropShipDtl(requestBody:DeleteDropShipDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteDropShipDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DeleteDropShipDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteDropShipDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateMassDropShipDtlWithoutComplete
   Description: Mass Drop Shipment functionality. Generates list without duplicated lines.
   OperationID: CreateMassDropShipDtlWithoutComplete
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateMassDropShipDtlWithoutComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateMassDropShipDtlWithoutComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateMassDropShipDtlWithoutComplete(requestBody:CreateMassDropShipDtlWithoutComplete_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateMassDropShipDtlWithoutComplete_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/CreateMassDropShipDtlWithoutComplete", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CreateMassDropShipDtlWithoutComplete_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDropShipHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDropShipHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDropShipHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDropShipHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDropShipHead(requestBody:GetNewDropShipHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDropShipHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/GetNewDropShipHead", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewDropShipHead_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDropShipHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDropShipHeadAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDropShipHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDropShipHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDropShipHeadAttch(requestBody:GetNewDropShipHeadAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDropShipHeadAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/GetNewDropShipHeadAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewDropShipHeadAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDropShipDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDropShipDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDropShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDropShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDropShipDtl(requestBody:GetNewDropShipDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDropShipDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/GetNewDropShipDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewDropShipDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDropShipHeadTrailer
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDropShipHeadTrailer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDropShipHeadTrailer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDropShipHeadTrailer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDropShipHeadTrailer(requestBody:GetNewDropShipHeadTrailer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDropShipHeadTrailer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/GetNewDropShipHeadTrailer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewDropShipHeadTrailer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMXDropShipHeadInsurance
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMXDropShipHeadInsurance
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMXDropShipHeadInsurance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMXDropShipHeadInsurance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMXDropShipHeadInsurance(requestBody:GetNewMXDropShipHeadInsurance_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMXDropShipHeadInsurance_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/GetNewMXDropShipHeadInsurance", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewMXDropShipHeadInsurance_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:DeleteByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteByID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetBySysRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetBySysRowID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetBySysRowIDs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetBySysRowIDs_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:Update_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Update_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Update_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:UpdateExt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateExt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateExt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DropShipDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipHeadAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DropShipHeadAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DropShipHeadListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DropShipHeadRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipHeadTrailerRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DropShipHeadTrailerRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumGenOptsRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXDropShipHeadInsuranceRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MXDropShipHeadInsuranceRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PendingDropShipDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PendingDropShipDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SNFormatRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SelectedSerialNumbersRow,
}

export interface Erp_Tablesets_DropShipDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The unique identifier for the drop shipment.  */  
   "PackSlip":string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system.  */  
   "PackLine":number,
      /**  Purchase order being drop shipped.  */  
   "PONum":number,
      /**  The line number of the purchase order being drop shipped.  */  
   "POLine":number,
      /**  The release number of the purchase order being drop shipped.  */  
   "PORelNum":number,
      /**  Part Num defaulted from the PO release.  */  
   "PartNum":string,
      /**  Part revision number.  */  
   "RevisionNum":string,
      /**  Supplier's part num. Defaulted from the PO release.  */  
   "VenPartNum":string,
      /**  Defaulted from the PO release.  */  
   "OrderNum":number,
      /**  Defaulted from the PO release.  */  
   "OrderLine":number,
      /**  Defaulted from the PO release.  */  
   "OrderRelNum":number,
      /**  An optional field that is used if the customer has a different Part number than the users internal part number. Defaulted from the SO release.  */  
   "XPartNum":string,
      /**  Field that contains the customer's revision.  */  
   "XRevisionNum":string,
      /**  This field will be automatically defaulted to the remaining quantity to be drop shipped. Receipt quantity in our unit of measure.  */  
   "OurQty":number,
      /**  Unit of Measure.  */  
   "IUM":string,
      /**  Unique lot number for the part.  */  
   "LotNum":string,
      /**  Holds any comments about the order line being shipped. This gets duplicated from the OrderDtl.ShipComment.  */  
   "ShipComment":string,
      /**  These comments will be copied into the Invoice detail.  */  
   "InvoiceComment":string,
      /**  Packing slip comments.  These are comments off of the invoice header.  */  
   "HeaderShipComment":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  This flag will be automatically set if the remaining quantity to be drop shipped equals to zero and will be automatically turned off if the remaining quantity is greater than zero.  */  
   "Complete":boolean,
      /**  The supplier that drops shipped the good from their inventory to our customer.  */  
   "VendorNum":number,
      /**  The supplier purchase point ID.  */  
   "PurPoint":string,
      /**  Defaults from PODetail LineDesc.  */  
   "LineDesc":string,
      /**  Unit cost base on our unit of measure. Default can be obtained from PODetail.UnitCost.  */  
   "OurUnitCost":number,
      /**  Item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost.  */  
   "DocUnitCost":number,
      /**  Quantity received against a purchase order in the vendors unit of measure.  */  
   "VendorQty":number,
      /**  Vendor's selling Unit of Measure.  */  
   "PUM":string,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the POdetail record.  */  
   "VendorUnitCost":number,
      /**  Receipt date. Mirror image of related DropShipHead.ReceiptDate.  */  
   "ReceiptDate":string,
      /**  A\P invoice entry sets this to "Yes" when the drop ship detail line is invoiced.  */  
   "APInvoiced":boolean,
      /**  A\R invoice entry sets this to "Yes" when the receipt detail line is invoiced.  */  
   "ARInvoiced":boolean,
      /**  Invoice Number from corresponding APInvHed record.  */  
   "APInvoiceNum":string,
      /**  Invoice Number Line from corresponding APInvDtl record.  */  
   "APInvoiceLine":number,
      /**  Invoice Number from corresponding InvcHead record.  */  
   "ARInvoiceNum":number,
      /**  Invoice Number Line from corresponding InvcDtl record.  */  
   "ARInvoiceLine":number,
      /**  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  */  
   "CostPerCode":string,
      /**  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  */  
   "TranReference":string,
      /**  Link to the related GLRefTyp.RefType. Not displayed.  */  
   "RefType":string,
      /**  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  */  
   "PurchCode":string,
      /**  Identifies a drop shipment line that is complete and ready to be invoiced.  */  
   "ReceivedShipped":boolean,
      /**  For Warranty drop shipments.  Defaults as DropShipHead.ReceiptDate. But can be maintained from the Service Call center.  */  
   "EffectiveDate":string,
      /**  Is Labor Cost Covered  */  
   "LabCovered":boolean,
      /**  The # of days, months, years the Labor is covered by warranty  */  
   "LaborDuration":number,
      /**  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   "LaborExpiration":string,
      /**  Whether the duration of warranty  is "Days"," Months"," years".  */  
   "LaborMod":string,
      /**  The latest of the 3 warranty expiration dates  */  
   "LastExpiration":string,
      /**  Are Material cost covered  */  
   "MatCovered":boolean,
      /**  The # of days, months, years the material is covered by warranty  */  
   "MaterialDuration":number,
      /**  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   "MaterialExpiration":string,
      /**  Whether the duration of warranty  is for "Days", " Months", "years".  */  
   "MaterialMod":string,
      /**  Are misc. Costs Covered  */  
   "MiscCovered":boolean,
      /**  The # of days, months, years the Misc. Charges are covered by warranty  */  
   "MiscDuration":number,
      /**  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   "MiscExpiration":string,
      /**  Whether the duration of warranty  is for "Days"," Months"," years".  */  
   "MiscMod":string,
      /**  This warranty covers On site visits  */  
   "Onsite":boolean,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   "WarrantyCode":string,
      /**  Warranty comments.  */  
   "WarrantyComment":string,
      /**  Duplicated from DropShipHead.CustNum.  */  
   "CustNum":number,
      /**  Duplicated from DropShipHead.ShipTotNum.  */  
   "ShipToNum":string,
      /**  Duplicated from DropShipHead.ShipToCustNum  */  
   "ShipToCustNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ProjProcessed  */  
   "ProjProcessed":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  Estimated Value  */  
   "MXEstValue":number,
      /**  Estimated Value Currency  */  
   "MXEstValueCurrencyCode":string,
      /**  Total Net Weight in kilograms  */  
   "MXTotalNetWeightKGM":number,
      /**  Hazardous Shipment  */  
   "MXHazardousShipment":boolean,
      /**  Hazardous Type  */  
   "MXHazardousType":string,
      /**  Package Type  */  
   "MXPackageType":string,
   "CurrencyCode":string,
   "POComment":string,
   "RemainingQty":number,
   "RemainingQtyUOM":string,
   "RequestedQty":number,
   "RequestedQtyUOM":string,
   "ShippedToDateQty":number,
   "ShippedToDateQtyUOM":string,
   "ThisShipmentQty":number,
   "ThisShipmentQtyUOM":string,
   "VendorCurrencyCode":string,
      /**  Interger value of CostPerCode  */  
   "CostPerFactor":number,
      /**  The formatted bill to address  */  
   "BillToAddrFormatted":string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   "DispNumberOfPieces":number,
   "BitFlag":number,
   "AttributeSetIDDescription":string,
   "AttributeSetIDShortDescription":string,
   "CustNumName":string,
   "CustNumCustID":string,
   "CustNumBTName":string,
   "PartNumPricePerCode":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumSalesUM":string,
   "PartNumIUM":string,
   "PartNumTrackLots":boolean,
   "PartNumPartDescription":string,
   "PartNumSellingFactor":number,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumAttrClassID":string,
   "PurPointCity":string,
   "PurPointCountry":string,
   "PurPointAddress1":string,
   "PurPointZip":string,
   "PurPointAddress3":string,
   "PurPointState":string,
   "PurPointName":string,
   "PurPointAddress2":string,
   "PurPointPrimPCon":number,
   "ShipToCustNumName":string,
   "ShipToCustNumCustID":string,
   "ShipToCustNumBTName":string,
   "ShipToNumInactive":boolean,
   "VendorNumZIP":string,
   "VendorNumDefaultFOB":string,
   "VendorNumState":string,
   "VendorNumName":string,
   "VendorNumTermsCode":string,
   "VendorNumAddress2":string,
   "VendorNumVendorID":string,
   "VendorNumCountry":string,
   "VendorNumAddress3":string,
   "VendorNumCity":string,
   "VendorNumCurrencyCode":string,
   "VendorNumAddress1":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DropShipHeadAttchRow{
   "Company":string,
   "VendorNum":number,
   "PurPoint":string,
   "PackSlip":string,
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

export interface Erp_Tablesets_DropShipHeadListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The unique identifier for the drop shipment.  */  
   "PackSlip":string,
      /**  The number of the purchase order that corresponds with the drop shipped goods.  */  
   "PONum":number,
      /**  The supplier that drops shipped the good from their inventory to our customer.  */  
   "VendorNum":number,
      /**  The supplier purchase point ID.  */  
   "PurPoint":string,
      /**  The ship to num related to this drop shipment.  */  
   "ShipToNum":string,
      /**  Identifies a drop shipment that is complete and ready to be invoiced.  */  
   "ReceivedShipped":boolean,
      /**  The user who created the drop shipment. This field will be auto populated when a user saves a new drop shipment.  */  
   "EntryPerson":string,
      /**  The date when the drop shipment was created. This field will be auto populated when a user saves a new drop shipment.  */  
   "EntryDate":string,
      /**  The user who marked the drop shipment as Received/Shipped. This field will be auto populated when a user turns on the received/shipped flag.  */  
   "ReceivePerson":string,
      /**  Date when the drop shipment was marked as Received/Shipped. This field will be auto populated. This field will be auto populated when a user turns on the received/shipped flag.  */  
   "ReceiptDate":string,
      /**  The ship via used to ship the goods from our supplier to our customer. This field will be defaulted from the PO selected in the above.  */  
   "ShipViaCode":string,
      /**  The tracking number used to track the shipment from our supplier to our customer.  */  
   "TrackingNumber":string,
      /**  This flag will be set once the packing slip has been invoiced in AP Invoice.  */  
   "APInvoiced":boolean,
      /**  This flag will be set on once the packing slip has been invoiced in AR Invoice.  */  
   "ARInvoiced":boolean,
      /**  Pack Num of the regular shipment created when flag ReceivedShipped is set.  */  
   "ShipmentPackNum":number,
      /**  Packing Slip of the regular receipt created when flag ReceivedShipped is set.  */  
   "ReceiptPackSlip":string,
      /**  Pack comments.  */  
   "ShipComment":string,
      /**  Contains comments about the overall Receipt.  */  
   "ReceiptComment":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Customer associated to the Drop Shioment.  */  
   "CustNum":number,
      /**  Bill To Customer Number  */  
   "BTCustNum":number,
      /**  Bill To Customer primary billing contact.  */  
   "BTConNum":number,
      /**  The Site that drop shipment was made from/to  */  
   "Plant":string,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  LegalNumber  */  
   "LegalNumber":string,
      /**  Address Information from Vendor or VendorPP  */  
   "AddrList":string,
      /**  Address Information from ShipToNum  */  
   "ShipToAddrList":string,
   "ShipToNumName":string,
      /**  Address information for DropShipHead.CustNum  */  
   "BillAddr":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustNumBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustNumCustID":string,
      /**  The full name of the customer.  */  
   "CustNumName":string,
      /**  City portion of the address  */  
   "PurPointCity":string,
      /**  First address line  */  
   "PurPointAddress1":string,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   "PurPointPrimPCon":number,
      /**  Second address line  */  
   "PurPointAddress2":string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   "PurPointCountry":string,
      /**  State portion of the address  */  
   "PurPointState":string,
      /**  Third address line  */  
   "PurPointAddress3":string,
      /**  Purchase Point Name...can't be blank.  */  
   "PurPointName":string,
      /**  Postal Code or Zip code portion of the address  */  
   "PurPointZip":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "ShipToCustNumBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "ShipToCustNumCustID":string,
      /**  The full name of the customer.  */  
   "ShipToCustNumName":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "ShipViaCodeWebDesc":string,
      /**  Full description for the shipping company (carrier).  */  
   "ShipViaCodeDescription":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorNumVendorID":string,
      /**  Third address line of the Supplier  */  
   "VendorNumAddress3":string,
      /**  A unique code that identifies the currency.  */  
   "VendorNumCurrencyCode":string,
      /**  Can be blank.  */  
   "VendorNumState":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNumZIP":string,
      /**  First address line of the Supplier  */  
   "VendorNumAddress1":string,
      /**  City portion of the address of the Supplier  */  
   "VendorNumCity":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNumDefaultFOB":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
      /**  Second address line of the Supplier  */  
   "VendorNumAddress2":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorNumCountry":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorNumName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DropShipHeadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The unique identifier for the drop shipment.  */  
   "PackSlip":string,
      /**  The number of the purchase order that corresponds with the drop shipped goods.  */  
   "PONum":number,
      /**  The supplier that drops shipped the good from their inventory to our customer.  */  
   "VendorNum":number,
      /**  The supplier purchase point ID.  */  
   "PurPoint":string,
      /**  The ship to num related to this drop shipment.  */  
   "ShipToNum":string,
      /**  Identifies a drop shipment that is complete and ready to be invoiced.  */  
   "ReceivedShipped":boolean,
      /**  The user who created the drop shipment. This field will be auto populated when a user saves a new drop shipment.  */  
   "EntryPerson":string,
      /**  The date when the drop shipment was created. This field will be auto populated when a user saves a new drop shipment.  */  
   "EntryDate":string,
      /**  The user who marked the drop shipment as Received/Shipped. This field will be auto populated when a user turns on the received/shipped flag.  */  
   "ReceivePerson":string,
      /**  Date when the drop shipment was marked as Received/Shipped. This field will be auto populated. This field will be auto populated when a user turns on the received/shipped flag.  */  
   "ReceiptDate":string,
      /**  The ship via used to ship the goods from our supplier to our customer. This field will be defaulted from the PO selected in the above.  */  
   "ShipViaCode":string,
      /**  The tracking number used to track the shipment from our supplier to our customer.  */  
   "TrackingNumber":string,
      /**  This flag will be set once the packing slip has been invoiced in AP Invoice.  */  
   "APInvoiced":boolean,
      /**  This flag will be set on once the packing slip has been invoiced in AR Invoice.  */  
   "ARInvoiced":boolean,
      /**  Pack Num of the regular shipment created when flag ReceivedShipped is set.  */  
   "ShipmentPackNum":number,
      /**  Packing Slip of the regular receipt created when flag ReceivedShipped is set.  */  
   "ReceiptPackSlip":string,
      /**  Pack comments.  */  
   "ShipComment":string,
      /**  Contains comments about the overall Receipt.  */  
   "ReceiptComment":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Customer associated to the Drop Shioment.  */  
   "CustNum":number,
      /**  Bill To Customer Number  */  
   "BTCustNum":number,
      /**  Bill To Customer primary billing contact.  */  
   "BTConNum":number,
      /**  The Site that drop shipment was made from/to  */  
   "Plant":string,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  TranDocTypeID  */  
   "TranDocTypeID":string,
      /**  LegalNumber  */  
   "LegalNumber":string,
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
      /**  Folio  */  
   "MXSerie":string,
      /**  Folio  */  
   "MXFolio":string,
      /**  Estimated Date and Time of Departure  */  
   "MXETD":string,
      /**  Estimated Date and Time of Departure  */  
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
   "MXVehicleLicensePlate":string,
      /**  Vehicle Type  */  
   "MXVehicleType":string,
      /**  Vehicle Year  */  
   "MXVehicleYear":number,
      /**  Driver  */  
   "MXDriverID":string,
      /**  MXCancelFiscalFolio  */  
   "MXCancelFiscalFolio":string,
      /**  Name of the ship reference that is going to be stored.  */  
   "EDIShipReferenceType":string,
      /**  Data this is going to be stored as ship reference.  */  
   "EDIShipReferenceData":string,
      /**  Estimated time when the shipment will arrive.  */  
   "EDIEstimatedDockDate":string,
      /**  Address Information from Vendor or VendorPP  */  
   "AddrList":string,
      /**  Address information for DropShipHead.CustNum  */  
   "BillAddr":string,
      /**  This field temporarily holds certain message(s) returned by credit card processing logic for internal processing.  */  
   "CreditCardMessage":string,
      /**  Address Information from ShipToNum  */  
   "ShipToAddrList":string,
   "ShipToNumName":string,
   "EnableAssignLegNum":boolean,
   "EnableVoidLegNum":boolean,
   "HasLegNumCnfg":boolean,
      /**  The formatted supplier name and address from AddrList  */  
   "SupplierNameAddrFormatted":string,
   "ShipToAddrFormatted":string,
      /**  The formatted bill to address  */  
   "BillToAddrFormatted":string,
      /**  Estimated Date of Arrival  */  
   "MXETADate":string,
      /**  Estimated Time of Arrival  */  
   "MXETATime":number,
      /**  Estimated Date of Departure  */  
   "MXETDDate":string,
      /**  Estimated Time of Departure  */  
   "MXETDTime":number,
      /**  Vehicle Weight (in tons)  */  
   "MXVehicleWeight":number,
      /**  A unique Carta Porte identification number assigned by Epicor  */  
   "MXIdCCP":string,
      /**  Customs Regime for Export transaction.  */  
   "MXCustomsRegime":string,
      /**  Check box to specify the use of reverse logistic, collection or devolution services when shipping goods.  */  
   "MXReverseLogistics":boolean,
   "BitFlag":number,
   "BTCustNumInactive":boolean,
   "CustNumInactive":boolean,
   "CustNumBTName":string,
   "CustNumCustID":string,
   "CustNumName":string,
   "PurPointZip":string,
   "PurPointAddress2":string,
   "PurPointPrimPCon":number,
   "PurPointCountry":string,
   "PurPointAddress3":string,
   "PurPointCity":string,
   "PurPointAddress1":string,
   "PurPointName":string,
   "PurPointState":string,
   "ShipToCustNumBTName":string,
   "ShipToCustNumCustID":string,
   "ShipToCustNumName":string,
   "ShipToCustNumInactive":boolean,
   "ShipToNumInactive":boolean,
   "ShipViaCodeDescription":string,
   "ShipViaCodeWebDesc":string,
   "TranDocTypeDescription":string,
   "VendorNumAddress1":string,
   "VendorNumVendorID":string,
   "VendorNumCity":string,
   "VendorNumState":string,
   "VendorNumCurrencyCode":string,
   "VendorNumAddress3":string,
   "VendorNumAddress2":string,
   "VendorNumDefaultFOB":string,
   "VendorNumName":string,
   "VendorNumZIP":string,
   "VendorNumTermsCode":string,
   "VendorNumCountry":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DropShipHeadTrailerRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Vendor Number  */  
   "VendorNum":number,
      /**  The Supplier Purchase Point  */  
   "PurPoint":string,
      /**  Packing Slip  */  
   "PackSlip":string,
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

export interface Erp_Tablesets_MXDropShipHeadInsuranceRow{
      /**  Company  */  
   "Company":string,
      /**  VendorNum  */  
   "VendorNum":number,
      /**  PurPoint  */  
   "PurPoint":string,
      /**  PackSlip  */  
   "PackSlip":string,
      /**  InsuranceSeq  */  
   "InsuranceSeq":number,
      /**  Type  */  
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

export interface Erp_Tablesets_PendingDropShipDtlRow{
   "Company":string,
   "LineDesc":string,
   "OurQuantity":number,
   "PartNum":string,
   "POLine":number,
   "PONum":number,
   "PurPoint":string,
   "UOM":string,
   "VendorNum":number,
   "OrderNum":number,
   "OrderLine":number,
   "OrderRelNum":number,
   "PORelNum":number,
   "PackSlip":string,
      /**  The Remaining Qty between Supplier Qty and Received Qty  */  
   "RemainingQty":number,
      /**  The Attribute Class for the part.  */  
   "AttrClassID":string,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   "DispNumberOfPieces":number,
   "TrackInventoryAttributes":boolean,
   "CurrencyCode":string,
   "RevisionNum":string,
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




//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ipVendorNum
      @param ipPurPoint
      @param ipPackSlip
      @param ds
   */  
export interface AssignLegalNumber_input{
      /**  Vendor No  */  
   ipVendorNum:number,
      /**  Purchase point  */  
   ipPurPoint:string,
      /**  Packing slip  */  
   ipPackSlip:string,
   ds:Erp_Tablesets_DropShipTableset[],
}

export interface AssignLegalNumber_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
   opLegalNumMsg:string,
}
}

   /** Required : 
      @param ipString
   */  
export interface BuildAddressField_input{
   ipString:string,
}

export interface BuildAddressField_output{
   returnObj:string,
}

   /** Required : 
      @param poNum
   */  
export interface BuildCustomersToList_input{
      /**  PO Number  */  
   poNum:number,
}

export interface BuildCustomersToList_output{
parameters : {
      /**  output parameters  */  
   customersToList:string,
}
}

   /** Required : 
      @param poNum
   */  
export interface BuildShipToCustListWithOutputParameters_input{
   poNum:number,
}

export interface BuildShipToCustListWithOutputParameters_output{
parameters : {
      /**  output parameters  */  
   shipToCustList:string,
   firstCustomerNum:number,
   firstCustomerID:string,
}
}

   /** Required : 
      @param poNum
   */  
export interface BuildShipToCustList_input{
      /**  PO Number  */  
   poNum:number,
}

export interface BuildShipToCustList_output{
parameters : {
      /**  output parameters  */  
   shipToCustList:string,
}
}

   /** Required : 
      @param poNum
      @param custNum
   */  
export interface BuildShipToListWithParameters_input{
   poNum:number,
   custNum:number,
}

export interface BuildShipToListWithParameters_output{
parameters : {
      /**  output parameters  */  
   shipToList:string,
   firstShipToNum:string,
}
}

   /** Required : 
      @param poNum
      @param custNum
   */  
export interface BuildShipToList_input{
      /**  PO Number  */  
   poNum:number,
      /**  Customer Number  */  
   custNum:number,
}

export interface BuildShipToList_output{
parameters : {
      /**  output parameters  */  
   shipToList:string,
}
}

   /** Required : 
      @param ds
      @param ipComplete
      @param ipPackLine
   */  
export interface ChangeDropShipDtlComplete_input{
   ds:Erp_Tablesets_DropShipTableset[],
      /**  The Complete value  */  
   ipComplete:boolean,
      /**  Selected pack line  */  
   ipPackLine:number,
}

export interface ChangeDropShipDtlComplete_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
   vMessage:string,
}
}

   /** Required : 
      @param ds
      @param ipIUM
      @param ipPackLine
   */  
export interface ChangeDropShipDtlIUM_input{
   ds:Erp_Tablesets_DropShipTableset[],
      /**  The IUM value  */  
   ipIUM:string,
      /**  Selected pack line  */  
   ipPackLine:number,
}

export interface ChangeDropShipDtlIUM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
   warnMsg:string,
}
}

   /** Required : 
      @param ds
      @param ipLotNum
      @param ipPackLine
   */  
export interface ChangeDropShipDtlLotNum_input{
   ds:Erp_Tablesets_DropShipTableset[],
      /**  The LotNum value  */  
   ipLotNum:string,
      /**  Selected pack line  */  
   ipPackLine:number,
}

export interface ChangeDropShipDtlLotNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
}
}

   /** Required : 
      @param ds
      @param ipOurQty
      @param ipPackLine
   */  
export interface ChangeDropShipDtlOurQty_input{
   ds:Erp_Tablesets_DropShipTableset[],
      /**  The OurQty value  */  
   ipOurQty:number,
      /**  Selected pack line  */  
   ipPackLine:number,
}

export interface ChangeDropShipDtlOurQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
   warnMsg:string,
}
}

   /** Required : 
      @param ds
      @param ipPOLine
      @param ipPackLine
   */  
export interface ChangeDropShipDtlPOLine_input{
   ds:Erp_Tablesets_DropShipTableset[],
      /**  The POLine value  */  
   ipPOLine:number,
      /**  Selected pack line  */  
   ipPackLine:number,
}

export interface ChangeDropShipDtlPOLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
   serialWarning:string,
}
}

   /** Required : 
      @param ds
      @param ipPONum
      @param ipPackLine
   */  
export interface ChangeDropShipDtlPONum_input{
   ds:Erp_Tablesets_DropShipTableset[],
      /**  The PONum value  */  
   ipPONum:number,
      /**  Selected pack line  */  
   ipPackLine:number,
}

export interface ChangeDropShipDtlPONum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
}
}

   /** Required : 
      @param ds
      @param ipPORelNum
      @param ipPackLine
   */  
export interface ChangeDropShipDtlPORelNum_input{
   ds:Erp_Tablesets_DropShipTableset[],
      /**  The PORelNum value  */  
   ipPORelNum:number,
      /**  Selected pack line  */  
   ipPackLine:number,
}

export interface ChangeDropShipDtlPORelNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
}
}

   /** Required : 
      @param ds
      @param ipVendorQty
      @param ipPackLine
   */  
export interface ChangeDropShipDtlVendorQty_input{
   ds:Erp_Tablesets_DropShipTableset[],
      /**  The VendorQty value  */  
   ipVendorQty:number,
      /**  Selected pack line  */  
   ipPackLine:number,
}

export interface ChangeDropShipDtlVendorQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
   warnMsg:string,
}
}

   /** Required : 
      @param ipPONum
      @param ds
   */  
export interface ChangeDropShipHeadPONum_input{
      /**  New PONum  */  
   ipPONum:number,
   ds:Erp_Tablesets_DropShipTableset[],
}

export interface ChangeDropShipHeadPONum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
}
}

   /** Required : 
      @param ipShipToCustNum
      @param ds
   */  
export interface ChangeDropShipHeadShipToCustNum_input{
      /**  New ShipToCustNum  */  
   ipShipToCustNum:number,
   ds:Erp_Tablesets_DropShipTableset[],
}

export interface ChangeDropShipHeadShipToCustNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
}
}

   /** Required : 
      @param ipShipToNum
      @param ds
   */  
export interface ChangeDropShipHeadShipToNum_input{
      /**  New ShipToNum  */  
   ipShipToNum:string,
   ds:Erp_Tablesets_DropShipTableset[],
}

export interface ChangeDropShipHeadShipToNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
}
}

   /** Required : 
      @param ipVendorNum
      @param ipPurPoint
      @param ipPackSlip
      @param ipPONum
      @param ds
   */  
export interface CreateMassDropShipDtlWithoutComplete_input{
   ipVendorNum:number,
   ipPurPoint:string,
   ipPackSlip:string,
   ipPONum:number,
   ds:Erp_Tablesets_DropShipTableset[],
}

export interface CreateMassDropShipDtlWithoutComplete_output{
parameters : {
      /**  output parameters  */  
   warnMsg:string,
   ds:Erp_Tablesets_DropShipTableset,
}
}

   /** Required : 
      @param ipVendorNum
      @param ipPurPoint
      @param ipPackSlip
      @param ipPONum
      @param ds
   */  
export interface CreateMassDropShipDtl_input{
      /**  The VendorNum value  */  
   ipVendorNum:number,
      /**  The PurPoint value  */  
   ipPurPoint:string,
      /**  The PackSlip value  */  
   ipPackSlip:string,
      /**  The PONum value  */  
   ipPONum:number,
   ds:Erp_Tablesets_DropShipTableset[],
}

export interface CreateMassDropShipDtl_output{
parameters : {
      /**  output parameters  */  
   warnMsg:string,
   ds:Erp_Tablesets_DropShipTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
   */  
export interface DeleteByID_input{
   vendorNum:number,
   purPoint:string,
   packSlip:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param ds
   */  
export interface DeleteDropShipDtl_input{
   ds:Erp_Tablesets_DropShipTableset[],
}

export interface DeleteDropShipDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
}
}

export interface Erp_Tablesets_DropShipDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The unique identifier for the drop shipment.  */  
   PackSlip:string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system.  */  
   PackLine:number,
      /**  Purchase order being drop shipped.  */  
   PONum:number,
      /**  The line number of the purchase order being drop shipped.  */  
   POLine:number,
      /**  The release number of the purchase order being drop shipped.  */  
   PORelNum:number,
      /**  Part Num defaulted from the PO release.  */  
   PartNum:string,
      /**  Part revision number.  */  
   RevisionNum:string,
      /**  Supplier's part num. Defaulted from the PO release.  */  
   VenPartNum:string,
      /**  Defaulted from the PO release.  */  
   OrderNum:number,
      /**  Defaulted from the PO release.  */  
   OrderLine:number,
      /**  Defaulted from the PO release.  */  
   OrderRelNum:number,
      /**  An optional field that is used if the customer has a different Part number than the users internal part number. Defaulted from the SO release.  */  
   XPartNum:string,
      /**  Field that contains the customer's revision.  */  
   XRevisionNum:string,
      /**  This field will be automatically defaulted to the remaining quantity to be drop shipped. Receipt quantity in our unit of measure.  */  
   OurQty:number,
      /**  Unit of Measure.  */  
   IUM:string,
      /**  Unique lot number for the part.  */  
   LotNum:string,
      /**  Holds any comments about the order line being shipped. This gets duplicated from the OrderDtl.ShipComment.  */  
   ShipComment:string,
      /**  These comments will be copied into the Invoice detail.  */  
   InvoiceComment:string,
      /**  Packing slip comments.  These are comments off of the invoice header.  */  
   HeaderShipComment:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  This flag will be automatically set if the remaining quantity to be drop shipped equals to zero and will be automatically turned off if the remaining quantity is greater than zero.  */  
   Complete:boolean,
      /**  The supplier that drops shipped the good from their inventory to our customer.  */  
   VendorNum:number,
      /**  The supplier purchase point ID.  */  
   PurPoint:string,
      /**  Defaults from PODetail LineDesc.  */  
   LineDesc:string,
      /**  Unit cost base on our unit of measure. Default can be obtained from PODetail.UnitCost.  */  
   OurUnitCost:number,
      /**  Item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost.  */  
   DocUnitCost:number,
      /**  Quantity received against a purchase order in the vendors unit of measure.  */  
   VendorQty:number,
      /**  Vendor's selling Unit of Measure.  */  
   PUM:string,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the POdetail record.  */  
   VendorUnitCost:number,
      /**  Receipt date. Mirror image of related DropShipHead.ReceiptDate.  */  
   ReceiptDate:string,
      /**  A\P invoice entry sets this to "Yes" when the drop ship detail line is invoiced.  */  
   APInvoiced:boolean,
      /**  A\R invoice entry sets this to "Yes" when the receipt detail line is invoiced.  */  
   ARInvoiced:boolean,
      /**  Invoice Number from corresponding APInvHed record.  */  
   APInvoiceNum:string,
      /**  Invoice Number Line from corresponding APInvDtl record.  */  
   APInvoiceLine:number,
      /**  Invoice Number from corresponding InvcHead record.  */  
   ARInvoiceNum:number,
      /**  Invoice Number Line from corresponding InvcDtl record.  */  
   ARInvoiceLine:number,
      /**  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  */  
   CostPerCode:string,
      /**  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  */  
   TranReference:string,
      /**  Link to the related GLRefTyp.RefType. Not displayed.  */  
   RefType:string,
      /**  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  */  
   PurchCode:string,
      /**  Identifies a drop shipment line that is complete and ready to be invoiced.  */  
   ReceivedShipped:boolean,
      /**  For Warranty drop shipments.  Defaults as DropShipHead.ReceiptDate. But can be maintained from the Service Call center.  */  
   EffectiveDate:string,
      /**  Is Labor Cost Covered  */  
   LabCovered:boolean,
      /**  The # of days, months, years the Labor is covered by warranty  */  
   LaborDuration:number,
      /**  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   LaborExpiration:string,
      /**  Whether the duration of warranty  is "Days"," Months"," years".  */  
   LaborMod:string,
      /**  The latest of the 3 warranty expiration dates  */  
   LastExpiration:string,
      /**  Are Material cost covered  */  
   MatCovered:boolean,
      /**  The # of days, months, years the material is covered by warranty  */  
   MaterialDuration:number,
      /**  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   MaterialExpiration:string,
      /**  Whether the duration of warranty  is for "Days", " Months", "years".  */  
   MaterialMod:string,
      /**  Are misc. Costs Covered  */  
   MiscCovered:boolean,
      /**  The # of days, months, years the Misc. Charges are covered by warranty  */  
   MiscDuration:number,
      /**  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   MiscExpiration:string,
      /**  Whether the duration of warranty  is for "Days"," Months"," years".  */  
   MiscMod:string,
      /**  This warranty covers On site visits  */  
   Onsite:boolean,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   WarrantyCode:string,
      /**  Warranty comments.  */  
   WarrantyComment:string,
      /**  Duplicated from DropShipHead.CustNum.  */  
   CustNum:number,
      /**  Duplicated from DropShipHead.ShipTotNum.  */  
   ShipToNum:string,
      /**  Duplicated from DropShipHead.ShipToCustNum  */  
   ShipToCustNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ProjProcessed  */  
   ProjProcessed:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Estimated Value  */  
   MXEstValue:number,
      /**  Estimated Value Currency  */  
   MXEstValueCurrencyCode:string,
      /**  Total Net Weight in kilograms  */  
   MXTotalNetWeightKGM:number,
      /**  Hazardous Shipment  */  
   MXHazardousShipment:boolean,
      /**  Hazardous Type  */  
   MXHazardousType:string,
      /**  Package Type  */  
   MXPackageType:string,
   CurrencyCode:string,
   POComment:string,
   RemainingQty:number,
   RemainingQtyUOM:string,
   RequestedQty:number,
   RequestedQtyUOM:string,
   ShippedToDateQty:number,
   ShippedToDateQtyUOM:string,
   ThisShipmentQty:number,
   ThisShipmentQtyUOM:string,
   VendorCurrencyCode:string,
      /**  Interger value of CostPerCode  */  
   CostPerFactor:number,
      /**  The formatted bill to address  */  
   BillToAddrFormatted:string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
   BitFlag:number,
   AttributeSetIDDescription:string,
   AttributeSetIDShortDescription:string,
   CustNumName:string,
   CustNumCustID:string,
   CustNumBTName:string,
   PartNumPricePerCode:string,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   PartNumSalesUM:string,
   PartNumIUM:string,
   PartNumTrackLots:boolean,
   PartNumPartDescription:string,
   PartNumSellingFactor:number,
   PartNumTrackInventoryAttributes:boolean,
   PartNumAttrClassID:string,
   PurPointCity:string,
   PurPointCountry:string,
   PurPointAddress1:string,
   PurPointZip:string,
   PurPointAddress3:string,
   PurPointState:string,
   PurPointName:string,
   PurPointAddress2:string,
   PurPointPrimPCon:number,
   ShipToCustNumName:string,
   ShipToCustNumCustID:string,
   ShipToCustNumBTName:string,
   ShipToNumInactive:boolean,
   VendorNumZIP:string,
   VendorNumDefaultFOB:string,
   VendorNumState:string,
   VendorNumName:string,
   VendorNumTermsCode:string,
   VendorNumAddress2:string,
   VendorNumVendorID:string,
   VendorNumCountry:string,
   VendorNumAddress3:string,
   VendorNumCity:string,
   VendorNumCurrencyCode:string,
   VendorNumAddress1:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DropShipHeadAttchRow{
   Company:string,
   VendorNum:number,
   PurPoint:string,
   PackSlip:string,
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

export interface Erp_Tablesets_DropShipHeadListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The unique identifier for the drop shipment.  */  
   PackSlip:string,
      /**  The number of the purchase order that corresponds with the drop shipped goods.  */  
   PONum:number,
      /**  The supplier that drops shipped the good from their inventory to our customer.  */  
   VendorNum:number,
      /**  The supplier purchase point ID.  */  
   PurPoint:string,
      /**  The ship to num related to this drop shipment.  */  
   ShipToNum:string,
      /**  Identifies a drop shipment that is complete and ready to be invoiced.  */  
   ReceivedShipped:boolean,
      /**  The user who created the drop shipment. This field will be auto populated when a user saves a new drop shipment.  */  
   EntryPerson:string,
      /**  The date when the drop shipment was created. This field will be auto populated when a user saves a new drop shipment.  */  
   EntryDate:string,
      /**  The user who marked the drop shipment as Received/Shipped. This field will be auto populated when a user turns on the received/shipped flag.  */  
   ReceivePerson:string,
      /**  Date when the drop shipment was marked as Received/Shipped. This field will be auto populated. This field will be auto populated when a user turns on the received/shipped flag.  */  
   ReceiptDate:string,
      /**  The ship via used to ship the goods from our supplier to our customer. This field will be defaulted from the PO selected in the above.  */  
   ShipViaCode:string,
      /**  The tracking number used to track the shipment from our supplier to our customer.  */  
   TrackingNumber:string,
      /**  This flag will be set once the packing slip has been invoiced in AP Invoice.  */  
   APInvoiced:boolean,
      /**  This flag will be set on once the packing slip has been invoiced in AR Invoice.  */  
   ARInvoiced:boolean,
      /**  Pack Num of the regular shipment created when flag ReceivedShipped is set.  */  
   ShipmentPackNum:number,
      /**  Packing Slip of the regular receipt created when flag ReceivedShipped is set.  */  
   ReceiptPackSlip:string,
      /**  Pack comments.  */  
   ShipComment:string,
      /**  Contains comments about the overall Receipt.  */  
   ReceiptComment:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Customer associated to the Drop Shioment.  */  
   CustNum:number,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**  Bill To Customer primary billing contact.  */  
   BTConNum:number,
      /**  The Site that drop shipment was made from/to  */  
   Plant:string,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  LegalNumber  */  
   LegalNumber:string,
      /**  Address Information from Vendor or VendorPP  */  
   AddrList:string,
      /**  Address Information from ShipToNum  */  
   ShipToAddrList:string,
   ShipToNumName:string,
      /**  Address information for DropShipHead.CustNum  */  
   BillAddr:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustNumBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustNumCustID:string,
      /**  The full name of the customer.  */  
   CustNumName:string,
      /**  City portion of the address  */  
   PurPointCity:string,
      /**  First address line  */  
   PurPointAddress1:string,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   PurPointPrimPCon:number,
      /**  Second address line  */  
   PurPointAddress2:string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   PurPointCountry:string,
      /**  State portion of the address  */  
   PurPointState:string,
      /**  Third address line  */  
   PurPointAddress3:string,
      /**  Purchase Point Name...can't be blank.  */  
   PurPointName:string,
      /**  Postal Code or Zip code portion of the address  */  
   PurPointZip:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   ShipToCustNumBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   ShipToCustNumCustID:string,
      /**  The full name of the customer.  */  
   ShipToCustNumName:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   ShipViaCodeWebDesc:string,
      /**  Full description for the shipping company (carrier).  */  
   ShipViaCodeDescription:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorNumVendorID:string,
      /**  Third address line of the Supplier  */  
   VendorNumAddress3:string,
      /**  A unique code that identifies the currency.  */  
   VendorNumCurrencyCode:string,
      /**  Can be blank.  */  
   VendorNumState:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNumZIP:string,
      /**  First address line of the Supplier  */  
   VendorNumAddress1:string,
      /**  City portion of the address of the Supplier  */  
   VendorNumCity:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNumDefaultFOB:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
      /**  Second address line of the Supplier  */  
   VendorNumAddress2:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorNumCountry:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorNumName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DropShipHeadListTableset{
   DropShipHeadList:Erp_Tablesets_DropShipHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DropShipHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The unique identifier for the drop shipment.  */  
   PackSlip:string,
      /**  The number of the purchase order that corresponds with the drop shipped goods.  */  
   PONum:number,
      /**  The supplier that drops shipped the good from their inventory to our customer.  */  
   VendorNum:number,
      /**  The supplier purchase point ID.  */  
   PurPoint:string,
      /**  The ship to num related to this drop shipment.  */  
   ShipToNum:string,
      /**  Identifies a drop shipment that is complete and ready to be invoiced.  */  
   ReceivedShipped:boolean,
      /**  The user who created the drop shipment. This field will be auto populated when a user saves a new drop shipment.  */  
   EntryPerson:string,
      /**  The date when the drop shipment was created. This field will be auto populated when a user saves a new drop shipment.  */  
   EntryDate:string,
      /**  The user who marked the drop shipment as Received/Shipped. This field will be auto populated when a user turns on the received/shipped flag.  */  
   ReceivePerson:string,
      /**  Date when the drop shipment was marked as Received/Shipped. This field will be auto populated. This field will be auto populated when a user turns on the received/shipped flag.  */  
   ReceiptDate:string,
      /**  The ship via used to ship the goods from our supplier to our customer. This field will be defaulted from the PO selected in the above.  */  
   ShipViaCode:string,
      /**  The tracking number used to track the shipment from our supplier to our customer.  */  
   TrackingNumber:string,
      /**  This flag will be set once the packing slip has been invoiced in AP Invoice.  */  
   APInvoiced:boolean,
      /**  This flag will be set on once the packing slip has been invoiced in AR Invoice.  */  
   ARInvoiced:boolean,
      /**  Pack Num of the regular shipment created when flag ReceivedShipped is set.  */  
   ShipmentPackNum:number,
      /**  Packing Slip of the regular receipt created when flag ReceivedShipped is set.  */  
   ReceiptPackSlip:string,
      /**  Pack comments.  */  
   ShipComment:string,
      /**  Contains comments about the overall Receipt.  */  
   ReceiptComment:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Customer associated to the Drop Shioment.  */  
   CustNum:number,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**  Bill To Customer primary billing contact.  */  
   BTConNum:number,
      /**  The Site that drop shipment was made from/to  */  
   Plant:string,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  TranDocTypeID  */  
   TranDocTypeID:string,
      /**  LegalNumber  */  
   LegalNumber:string,
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
      /**  Folio  */  
   MXSerie:string,
      /**  Folio  */  
   MXFolio:string,
      /**  Estimated Date and Time of Departure  */  
   MXETD:string,
      /**  Estimated Date and Time of Departure  */  
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
   MXVehicleLicensePlate:string,
      /**  Vehicle Type  */  
   MXVehicleType:string,
      /**  Vehicle Year  */  
   MXVehicleYear:number,
      /**  Driver  */  
   MXDriverID:string,
      /**  MXCancelFiscalFolio  */  
   MXCancelFiscalFolio:string,
      /**  Name of the ship reference that is going to be stored.  */  
   EDIShipReferenceType:string,
      /**  Data this is going to be stored as ship reference.  */  
   EDIShipReferenceData:string,
      /**  Estimated time when the shipment will arrive.  */  
   EDIEstimatedDockDate:string,
      /**  Address Information from Vendor or VendorPP  */  
   AddrList:string,
      /**  Address information for DropShipHead.CustNum  */  
   BillAddr:string,
      /**  This field temporarily holds certain message(s) returned by credit card processing logic for internal processing.  */  
   CreditCardMessage:string,
      /**  Address Information from ShipToNum  */  
   ShipToAddrList:string,
   ShipToNumName:string,
   EnableAssignLegNum:boolean,
   EnableVoidLegNum:boolean,
   HasLegNumCnfg:boolean,
      /**  The formatted supplier name and address from AddrList  */  
   SupplierNameAddrFormatted:string,
   ShipToAddrFormatted:string,
      /**  The formatted bill to address  */  
   BillToAddrFormatted:string,
      /**  Estimated Date of Arrival  */  
   MXETADate:string,
      /**  Estimated Time of Arrival  */  
   MXETATime:number,
      /**  Estimated Date of Departure  */  
   MXETDDate:string,
      /**  Estimated Time of Departure  */  
   MXETDTime:number,
      /**  Vehicle Weight (in tons)  */  
   MXVehicleWeight:number,
      /**  A unique Carta Porte identification number assigned by Epicor  */  
   MXIdCCP:string,
      /**  Customs Regime for Export transaction.  */  
   MXCustomsRegime:string,
      /**  Check box to specify the use of reverse logistic, collection or devolution services when shipping goods.  */  
   MXReverseLogistics:boolean,
   BitFlag:number,
   BTCustNumInactive:boolean,
   CustNumInactive:boolean,
   CustNumBTName:string,
   CustNumCustID:string,
   CustNumName:string,
   PurPointZip:string,
   PurPointAddress2:string,
   PurPointPrimPCon:number,
   PurPointCountry:string,
   PurPointAddress3:string,
   PurPointCity:string,
   PurPointAddress1:string,
   PurPointName:string,
   PurPointState:string,
   ShipToCustNumBTName:string,
   ShipToCustNumCustID:string,
   ShipToCustNumName:string,
   ShipToCustNumInactive:boolean,
   ShipToNumInactive:boolean,
   ShipViaCodeDescription:string,
   ShipViaCodeWebDesc:string,
   TranDocTypeDescription:string,
   VendorNumAddress1:string,
   VendorNumVendorID:string,
   VendorNumCity:string,
   VendorNumState:string,
   VendorNumCurrencyCode:string,
   VendorNumAddress3:string,
   VendorNumAddress2:string,
   VendorNumDefaultFOB:string,
   VendorNumName:string,
   VendorNumZIP:string,
   VendorNumTermsCode:string,
   VendorNumCountry:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DropShipHeadTrailerRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Vendor Number  */  
   VendorNum:number,
      /**  The Supplier Purchase Point  */  
   PurPoint:string,
      /**  Packing Slip  */  
   PackSlip:string,
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

export interface Erp_Tablesets_DropShipTableset{
   DropShipHead:Erp_Tablesets_DropShipHeadRow[],
   DropShipHeadAttch:Erp_Tablesets_DropShipHeadAttchRow[],
   DropShipDtl:Erp_Tablesets_DropShipDtlRow[],
   DropShipHeadTrailer:Erp_Tablesets_DropShipHeadTrailerRow[],
   MXDropShipHeadInsurance:Erp_Tablesets_MXDropShipHeadInsuranceRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   PendingDropShipDtl:Erp_Tablesets_PendingDropShipDtlRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
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

export interface Erp_Tablesets_MXDropShipHeadInsuranceRow{
      /**  Company  */  
   Company:string,
      /**  VendorNum  */  
   VendorNum:number,
      /**  PurPoint  */  
   PurPoint:string,
      /**  PackSlip  */  
   PackSlip:string,
      /**  InsuranceSeq  */  
   InsuranceSeq:number,
      /**  Type  */  
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

export interface Erp_Tablesets_OrderShipmentsRow{
   SellingShipmentQty:number,
   SellingShipmentUM:string,
      /**  OurInventoryShipQty * DimConvFactor - update inplace of OurInventoryShipQty  */  
   DisplayInvQty:number,
      /**  External field to be used in the SalesOrder Tracker to show the user the InvoiceNum linked to the  */  
   InvoiceNum:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.   This field comes directly from the table ShipHead.  */  
   LegalNumber:string,
      /**  The actual ship date for the packing slip. Default as system date.  This field comes directly from the ShipHead table.  */  
   ShipDate:string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  This field comes directly from the ShipHead table.  */  
   ShipViaCode:string,
      /**  The invoice legal number.  */  
   InvLegalNumber:string,
   OrderRelOurReqQty:number,
   PartCompany:string,
   PartPartNum:string,
      /**  Sales Kit flag. C = 'Component' P = 'Parent'.  */  
   KitFlag:string,
   KitCompIssue:boolean,
   KitBackFlush:boolean,
   KitCompShipComplete:boolean,
   ExtJobNum:string,
   LinkMsg:string,
   PONum:string,
   KitQtyFromInvEnabled:boolean,
   KitParentIssue:boolean,
   KitPartNum:string,
   KitBinNum:string,
   KitDescription:string,
   KitLotNum:string,
   KitSerialTracked:boolean,
   KitTrackLots:boolean,
   KitWarehouse:string,
   KitWarehouseCodeDesc:string,
   KitWhseList:string,
   KitBinNumEnabled:boolean,
      /**  Used by freight web service  */  
   PartAESExp:string,
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
      /**  Used by freight  web service  */  
   PartOrigCountry:string,
      /**  Used by freight web service  */  
   PartSchedBcode:string,
      /**  Used by freight web service  */  
   PartUseHTSDesc:boolean,
      /**  Packing slip number that this detail record is linked with  */  
   PackNum:number,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  */  
   PackLine:number,
      /**  The sales order line that this shipment detail line is linked to.  Must be valid in the OrderDtl file.  */  
   OrderLine:number,
      /**  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  */  
   OrderRelNum:number,
      /**  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This quantity is in the IUM unit of measure.  */  
   OurJobShipQty:number,
      /**  Job Number that supplied the quantity that was shipped. Defaulted from OrderRel.JobNum.  */  
   JobNum:string,
      /**  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation. This is not user maintainable. If this is a shipment from inventory use this part number to reduce the Part.Onhand qty.  */  
   PartNum:string,
      /**  Generated from field LineDesc  */  
   LineDesc:string,
      /**  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  */  
   RevisionNum:string,
      /**  Indicates the warehouse from which the quantity was shipped. This is only valid if the ShipDtl.Inventory quantity is > 0 and this is a valid part number.  The default should be retrieved from the OrderDtl.WareHseCode. .  */  
   WarehouseCode:string,
      /**  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  */  
   BinNum:string,
      /**  The shipto number. Used for warranty validation.  */  
   ShipToNum:string,
      /**  Indicates if the Packing Slip is complete and ready for invoicing.  This is a mirror image of ShipHead.ReadyToInvoice.  */  
   ReadyToInvoice:boolean,
   HeaderShipComment:string,
   KitParentLine:number,
   ChangedBy:string,
   ChangeDate:string,
   ChangeTime:number,
   InventoryShipUOM:string,
   JobShipUOM:string,
   TrackSerialNum:boolean,
   JobLotNum:string,
   SysRowID:string,
   SysRevID:number,
   BinType:string,
      /**  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  */  
   NotComplaint:boolean,
      /**  Displays the cause why the item is not compliant.  */  
   ComplianceMsg:string,
   DiscountPercent:number,
   Discount:number,
   DocDiscount:number,
   PricePerCode:string,
   Rpt1Discount:number,
   Rpt2Discount:number,
   Rpt3Discount:number,
   ExtPrice:number,
   DocExtPrice:number,
   Rpt1ExtPrice:number,
   Rpt2ExtPrice:number,
   Rpt3ExtPrice:number,
   UnitPrice:number,
   DocUnitPrice:number,
   Rpt1UnitPrice:number,
   Rpt2UnitPrice:number,
   Rpt3UnitPrice:number,
   PickedAutoAllocatedQty:number,
   ShipToCustNum:number,
   OurRemainQty:number,
   KitMassIssue:boolean,
      /**  Individual line content value that is used by the freight web service to calculate the total order value.  */  
   LineContentValue:number,
      /**  Logical indicating if receipt to a job is allowed.  This is determined by either the xasyst.shipnojob field or whether or not the sales order is linked to a job.  */  
   EnableJobFields:boolean,
      /**  Indicates if Order is on Hold  */  
   OrderHold:boolean,
   EnableInvSerialBtn:boolean,
   EnableMfgSerialBtn:boolean,
   EnablePOSerialBtn:boolean,
   LineTax:number,
   DocLineTax:number,
   CurrencyCode:string,
   Rpt1LineTax:number,
   Rpt2LineTax:number,
   Rpt3LineTax:number,
   VendorNum:number,
   PurPoint:string,
   PackSlip:string,
   CustNumName:string,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   PackNumShipStatus:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**  This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in  */  
   PartNumSellingFactor:number,
      /**  UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**  The sales order number that this detail shipment line is linked to. This is not directly maintainable, It is carried forward through from the ShipHead.OrderNum field.  */  
   OrderNum:number,
      /**  Company Identifier  */  
   Company:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OrderShipmentsTableset{
   OrderShipments:Erp_Tablesets_OrderShipmentsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PendingDropShipDtlRow{
   Company:string,
   LineDesc:string,
   OurQuantity:number,
   PartNum:string,
   POLine:number,
   PONum:number,
   PurPoint:string,
   UOM:string,
   VendorNum:number,
   OrderNum:number,
   OrderLine:number,
   OrderRelNum:number,
   PORelNum:number,
   PackSlip:string,
      /**  The Remaining Qty between Supplier Qty and Received Qty  */  
   RemainingQty:number,
      /**  The Attribute Class for the part.  */  
   AttrClassID:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
   TrackInventoryAttributes:boolean,
   CurrencyCode:string,
   RevisionNum:string,
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

export interface Erp_Tablesets_UpdExtDropShipTableset{
   DropShipHead:Erp_Tablesets_DropShipHeadRow[],
   DropShipHeadAttch:Erp_Tablesets_DropShipHeadAttchRow[],
   DropShipDtl:Erp_Tablesets_DropShipDtlRow[],
   DropShipHeadTrailer:Erp_Tablesets_DropShipHeadTrailerRow[],
   MXDropShipHeadInsurance:Erp_Tablesets_MXDropShipHeadInsuranceRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   PendingDropShipDtl:Erp_Tablesets_PendingDropShipDtlRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
   */  
export interface GetByID_input{
   vendorNum:number,
   purPoint:string,
   packSlip:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_DropShipTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_DropShipTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_DropShipTableset[],
}

   /** Required : 
      @param ipVendorNum
      @param ipPurPoint
      @param ipPackSlip
      @param ds
   */  
export interface GetLegalNumGenOpts_input{
      /**  Vendor No  */  
   ipVendorNum:number,
      /**  Purchase point  */  
   ipPurPoint:string,
      /**  Packing slip  */  
   ipPackSlip:string,
   ds:Erp_Tablesets_DropShipTableset[],
}

export interface GetLegalNumGenOpts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
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
   returnObj:Erp_Tablesets_DropShipHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetMXCartaPortePOInfo_input{
   ds:Erp_Tablesets_DropShipTableset[],
}

export interface GetMXCartaPortePOInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
   */  
export interface GetNewDropShipDtl_input{
   ds:Erp_Tablesets_DropShipTableset[],
   vendorNum:number,
   purPoint:string,
   packSlip:string,
}

export interface GetNewDropShipDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
   */  
export interface GetNewDropShipHeadAttch_input{
   ds:Erp_Tablesets_DropShipTableset[],
   vendorNum:number,
   purPoint:string,
   packSlip:string,
}

export interface GetNewDropShipHeadAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
   */  
export interface GetNewDropShipHeadTrailer_input{
   ds:Erp_Tablesets_DropShipTableset[],
   vendorNum:number,
   purPoint:string,
   packSlip:string,
}

export interface GetNewDropShipHeadTrailer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
   */  
export interface GetNewDropShipHead_input{
   ds:Erp_Tablesets_DropShipTableset[],
   vendorNum:number,
   purPoint:string,
}

export interface GetNewDropShipHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
   */  
export interface GetNewMXDropShipHeadInsurance_input{
   ds:Erp_Tablesets_DropShipTableset[],
   vendorNum:number,
   purPoint:string,
   packSlip:string,
}

export interface GetNewMXDropShipHeadInsurance_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
}
}

   /** Required : 
      @param ds
      @param orderNum
      @param orderLine
   */  
export interface GetOrderShipments_input{
   ds:Erp_Tablesets_OrderShipmentsTableset[],
      /**  Order Number  */  
   orderNum:number,
      /**  Order Line  */  
   orderLine:number,
}

export interface GetOrderShipments_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderShipmentsTableset,
}
}

   /** Required : 
      @param ds
      @param poNum
   */  
export interface GetPOInfo_input{
   ds:Erp_Tablesets_DropShipTableset[],
      /**  Proposed Purchase Order Number  */  
   poNum:number,
}

export interface GetPOInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
   vendorNum:number,
   purPoint:string,
}
}

   /** Required : 
      @param ds
      @param ipPONum
   */  
export interface GetPendingDtl_input{
   ds:Erp_Tablesets_DropShipTableset[],
      /**  The PO number  */  
   ipPONum:number,
}

export interface GetPendingDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
}
}

   /** Required : 
      @param ds
      @param purPoint
   */  
export interface GetPurPointInfo_input{
   ds:Erp_Tablesets_DropShipTableset[],
      /**  Proposed Purchase Point value  */  
   purPoint:string,
}

export interface GetPurPointInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
}
}

   /** Required : 
      @param whereClauseDropShipHead
      @param whereClauseDropShipHeadAttch
      @param whereClauseDropShipDtl
      @param whereClauseDropShipHeadTrailer
      @param whereClauseMXDropShipHeadInsurance
      @param whereClauseLegalNumGenOpts
      @param whereClausePendingDropShipDtl
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSNFormat
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseDropShipHead:string,
   whereClauseDropShipHeadAttch:string,
   whereClauseDropShipDtl:string,
   whereClauseDropShipHeadTrailer:string,
   whereClauseMXDropShipHeadInsurance:string,
   whereClauseLegalNumGenOpts:string,
   whereClausePendingDropShipDtl:string,
   whereClauseSelectedSerialNumbers:string,
   whereClauseSNFormat:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_DropShipTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipPartNum
      @param ipAttributeSetID
      @param ipQuantity
      @param ipUOM
      @param ipVendNum
      @param ipVendPP
      @param ipPackSlip
      @param ipPackSlipLine
      @param ipPONum
      @param ipPOLine
      @param ipPORelNum
   */  
export interface GetSelectSerialNumbersParams_input{
   ipPartNum:string,
   ipAttributeSetID:number,
   ipQuantity:number,
   ipUOM:string,
   ipVendNum:number,
   ipVendPP:string,
   ipPackSlip:string,
   ipPackSlipLine:number,
   ipPONum:number,
   ipPOLine:number,
   ipPORelNum:number,
}

export interface GetSelectSerialNumbersParams_output{
   returnObj:Erp_Tablesets_SelectSerialNumbersParamsTableset[],
}

   /** Required : 
      @param poNum
      @param custNum
      @param shipToNum
   */  
export interface GetShipToAddressMultiKey_input{
      /**  PO Num  */  
   poNum:number,
      /**  Cust Num  */  
   custNum:number,
      /**  Ship To Num  */  
   shipToNum:string,
}

export interface GetShipToAddressMultiKey_output{
parameters : {
      /**  output parameters  */  
   shipToListMult:string,
}
}

   /** Required : 
      @param ipTranDocTypeID
      @param ds
   */  
export interface GetTranDocTypeID_input{
      /**  Transaction Document Type  */  
   ipTranDocTypeID:string,
   ds:Erp_Tablesets_DropShipTableset[],
}

export interface GetTranDocTypeID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
}
}

   /** Required : 
      @param ds
      @param vendorID
   */  
export interface GetVendorInfo_input{
   ds:Erp_Tablesets_DropShipTableset[],
      /**  Proposed Vendor ID value  */  
   vendorID:string,
}

export interface GetVendorInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
   vendorNum:number,
   purPoint:string,
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
export interface InitializeMultiKeySearchData_input{
   ds:Erp_Tablesets_DropShipTableset[],
}

export interface InitializeMultiKeySearchData_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface MarkShipmentLines_input{
   ds:Erp_Tablesets_DropShipTableset[],
}

export interface MarkShipmentLines_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
}
}

   /** Required : 
      @param ipPONum
      @param ds
   */  
export interface OnChangeMultiKeySearchPONum_input{
   ipPONum:number,
   ds:Erp_Tablesets_DropShipTableset[],
}

export interface OnChangeMultiKeySearchPONum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
}
}

   /** Required : 
      @param shipViaCode
      @param ds
   */  
export interface OnChangeShipViaCode_input{
      /**  New ShipVia Code  */  
   shipViaCode:string,
   ds:Erp_Tablesets_DropShipTableset[],
}

export interface OnChangeShipViaCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
}
}

   /** Required : 
      @param numberOfPieces
      @param ipPackLine
      @param ds
   */  
export interface OnChangingNumberOfPieces_input{
   numberOfPieces:number,
      /**  Selected pack line  */  
   ipPackLine:number,
   ds:Erp_Tablesets_DropShipTableset[],
}

export interface OnChangingNumberOfPieces_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
   warnMsg:string,
}
}

   /** Required : 
      @param ipPackSlip
      @param ipVendorNum
      @param ipPurPoint
   */  
export interface PostUpdate_input{
      /**  Drop Ship Pack Slip  */  
   ipPackSlip:string,
      /**  Supplier  */  
   ipVendorNum:number,
      /**  Purchase Point  */  
   ipPurPoint:string,
}

export interface PostUpdate_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param ds
      @param ipLotNum
   */  
export interface PreChangeDropShipDtlLotNum_input{
   ds:Erp_Tablesets_DropShipTableset[],
      /**  The LotNum value  */  
   ipLotNum:string,
}

export interface PreChangeDropShipDtlLotNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
   questionMsg:string,
   errorMsg:string,
}
}

   /** Required : 
      @param ipVendorNum
      @param ipPurPoint
      @param ipPackSlip
      @param ipPONum
      @param ds
   */  
export interface PreCreateMassReceipt_input{
      /**  The VendorNum value  */  
   ipVendorNum:number,
      /**  The PurPoint value  */  
   ipPurPoint:string,
      /**  The PackSlip value  */  
   ipPackSlip:string,
      /**  The PONum value  */  
   ipPONum:number,
   ds:Erp_Tablesets_DropShipTableset[],
}

export interface PreCreateMassReceipt_output{
parameters : {
      /**  output parameters  */  
   warnMsg:string,
   ds:Erp_Tablesets_DropShipTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface PreUpdateDropShipDtl_input{
   ds:Erp_Tablesets_DropShipTableset[],
}

export interface PreUpdateDropShipDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
   qMessageStr:string,
   sMessageStr:string,
}
}

   /** Required : 
      @param ds
   */  
export interface UndoShipAll_input{
   ds:Erp_Tablesets_DropShipTableset[],
}

export interface UndoShipAll_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtDropShipTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtDropShipTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_DropShipTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipTableset,
}
}

   /** Required : 
      @param ipPartNum
      @param ipAttributeSetID
      @param ipSerialNo
      @param ipVendNum
      @param ipPurPoint
      @param ipPackNum
      @param ipPONum
      @param ipPOLine
      @param ipPORelNum
   */  
export interface ValidateSN_input{
   ipPartNum:string,
   ipAttributeSetID:number,
   ipSerialNo:string,
   ipVendNum:number,
   ipPurPoint:string,
   ipPackNum:string,
   ipPONum:number,
   ipPOLine:number,
   ipPORelNum:number,
}

export interface ValidateSN_output{
}

   /** Required : 
      @param ipVendorNum
      @param ipPurPoint
      @param ipPackSlip
      @param ipVoidedReason
   */  
export interface VoidLegalNumber_input{
      /**  Vendor No  */  
   ipVendorNum:number,
      /**  Purchase point  */  
   ipPurPoint:string,
      /**  Packing slip  */  
   ipPackSlip:string,
      /**  Reason for the void  */  
   ipVoidedReason:string,
}

export interface VoidLegalNumber_output{
   returnObj:Erp_Tablesets_DropShipTableset[],
}

   /** Required : 
      @param ipPONum
      @param ipShipToCustNum
      @param ipShipToNum
      @param ipAddrList
   */  
export interface buildShipToAddressFieldMultiKey_input{
   ipPONum:number,
   ipShipToCustNum:number,
   ipShipToNum:string,
   ipAddrList:string,
}

export interface buildShipToAddressFieldMultiKey_output{
   returnObj:string,
}

   /** Required : 
      @param docCmAmount
      @param depCheckRef
      @param lastInvoiceNum
   */  
export interface processExtraCreditCharge_input{
   docCmAmount:number,
   depCheckRef:string,
   lastInvoiceNum:number,
}

export interface processExtraCreditCharge_output{
}

