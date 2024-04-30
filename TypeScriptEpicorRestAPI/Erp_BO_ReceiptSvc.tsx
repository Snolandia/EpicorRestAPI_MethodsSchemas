import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ReceiptSvc
// Description: Receipt Entry
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/$metadata", {
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
   Description: Get Receipts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Receipts
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvHeadRow
   */  
export function get_Receipts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Receipts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RcvHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RcvHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Receipts(requestBody:Erp_Tablesets_RcvHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts", {
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
   Summary: Calls GetByID to retrieve the Receipt item
   Description: Calls GetByID to retrieve the Receipt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Receipt
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
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RcvHeadRow
   */  
export function get_Receipts_Company_VendorNum_PurPoint_PackSlip(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RcvHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")", {
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
         resolve(data as Erp_Tablesets_RcvHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Receipt for the service
   Description: Calls UpdateExt to update Receipt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Receipt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RcvHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Receipts_Company_VendorNum_PurPoint_PackSlip(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, requestBody:Erp_Tablesets_RcvHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")", {
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
   Summary: Call UpdateExt to delete Receipt item
   Description: Call UpdateExt to delete Receipt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Receipt
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
export function delete_Receipts_Company_VendorNum_PurPoint_PackSlip(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")", {
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
   Description: Get RcvHeadTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RcvHeadTaxes1
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvHeadTaxRow
   */  
export function get_Receipts_Company_VendorNum_PurPoint_PackSlip_RcvHeadTaxes(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvHeadTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/RcvHeadTaxes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvHeadTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RcvHeadTax item
   Description: Calls GetByID to retrieve the RcvHeadTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvHeadTax1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RcvHeadTaxRow
   */  
export function get_Receipts_Company_VendorNum_PurPoint_PackSlip_RcvHeadTaxes_Company_VendorNum_PurPoint_PackSlip_TaxCode_RateCode_ECAcquisitionSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RcvHeadTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/RcvHeadTaxes(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
         resolve(data as Erp_Tablesets_RcvHeadTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get RcvDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RcvDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvDtlRow
   */  
export function get_Receipts_Company_VendorNum_PurPoint_PackSlip_RcvDtls(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/RcvDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RcvDtl item
   Description: Calls GetByID to retrieve the RcvDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RcvDtlRow
   */  
export function get_Receipts_Company_VendorNum_PurPoint_PackSlip_RcvDtls_Company_VendorNum_PurPoint_PackSlip_PackLine(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RcvDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/RcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")", {
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
         resolve(data as Erp_Tablesets_RcvDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get RcvMiscs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RcvMiscs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvMiscRow
   */  
export function get_Receipts_Company_VendorNum_PurPoint_PackSlip_RcvMiscs(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvMiscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/RcvMiscs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvMiscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RcvMisc item
   Description: Calls GetByID to retrieve the RcvMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvMisc1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param MiscSeq Desc: MiscSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RcvMiscRow
   */  
export function get_Receipts_Company_VendorNum_PurPoint_PackSlip_RcvMiscs_Company_VendorNum_PurPoint_PackSlip_MiscSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, MiscSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RcvMiscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/RcvMiscs(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + MiscSeq + ")", {
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
         resolve(data as Erp_Tablesets_RcvMiscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get RcvHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RcvHeadAttches1
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvHeadAttchRow
   */  
export function get_Receipts_Company_VendorNum_PurPoint_PackSlip_RcvHeadAttches(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/RcvHeadAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RcvHeadAttch item
   Description: Calls GetByID to retrieve the RcvHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvHeadAttch1
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
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RcvHeadAttchRow
   */  
export function get_Receipts_Company_VendorNum_PurPoint_PackSlip_RcvHeadAttches_Company_VendorNum_PurPoint_PackSlip_DrawingSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RcvHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/RcvHeadAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_RcvHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get RcvHeadTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RcvHeadTaxes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvHeadTaxRow
   */  
export function get_RcvHeadTaxes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvHeadTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvHeadTaxes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvHeadTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RcvHeadTaxes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RcvHeadTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RcvHeadTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RcvHeadTaxes(requestBody:Erp_Tablesets_RcvHeadTaxRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvHeadTaxes", {
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
   Summary: Calls GetByID to retrieve the RcvHeadTax item
   Description: Calls GetByID to retrieve the RcvHeadTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvHeadTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RcvHeadTaxRow
   */  
export function get_RcvHeadTaxes_Company_VendorNum_PurPoint_PackSlip_TaxCode_RateCode_ECAcquisitionSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RcvHeadTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvHeadTaxes(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
         resolve(data as Erp_Tablesets_RcvHeadTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RcvHeadTax for the service
   Description: Calls UpdateExt to update RcvHeadTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RcvHeadTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RcvHeadTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RcvHeadTaxes_Company_VendorNum_PurPoint_PackSlip_TaxCode_RateCode_ECAcquisitionSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, requestBody:Erp_Tablesets_RcvHeadTaxRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvHeadTaxes(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Summary: Call UpdateExt to delete RcvHeadTax item
   Description: Call UpdateExt to delete RcvHeadTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RcvHeadTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RcvHeadTaxes_Company_VendorNum_PurPoint_PackSlip_TaxCode_RateCode_ECAcquisitionSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvHeadTaxes(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Description: Get RcvDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RcvDtls
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvDtlRow
   */  
export function get_RcvDtls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RcvDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RcvDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RcvDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RcvDtls(requestBody:Erp_Tablesets_RcvDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls", {
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
   Summary: Calls GetByID to retrieve the RcvDtl item
   Description: Calls GetByID to retrieve the RcvDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RcvDtlRow
   */  
export function get_RcvDtls_Company_VendorNum_PurPoint_PackSlip_PackLine(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RcvDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")", {
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
         resolve(data as Erp_Tablesets_RcvDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RcvDtl for the service
   Description: Calls UpdateExt to update RcvDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RcvDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RcvDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RcvDtls_Company_VendorNum_PurPoint_PackSlip_PackLine(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, requestBody:Erp_Tablesets_RcvDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")", {
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
   Summary: Call UpdateExt to delete RcvDtl item
   Description: Call UpdateExt to delete RcvDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RcvDtl
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
export function delete_RcvDtls_Company_VendorNum_PurPoint_PackSlip_PackLine(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")", {
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
   Description: Get RcvDtlAttrValueSets items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RcvDtlAttrValueSets1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvDtlAttrValueSetRow
   */  
export function get_RcvDtls_Company_VendorNum_PurPoint_PackSlip_PackLine_RcvDtlAttrValueSets(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlAttrValueSetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")/RcvDtlAttrValueSets", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlAttrValueSetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RcvDtlAttrValueSet item
   Description: Calls GetByID to retrieve the RcvDtlAttrValueSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvDtlAttrValueSet1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param AttributeValueSeq Desc: AttributeValueSeq   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RcvDtlAttrValueSetRow
   */  
export function get_RcvDtls_Company_VendorNum_PurPoint_PackSlip_PackLine_RcvDtlAttrValueSets_Company_VendorNum_PurPoint_PackSlip_PackLine_AttributeValueSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, AttributeValueSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RcvDtlAttrValueSetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")/RcvDtlAttrValueSets(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + AttributeValueSeq + ")", {
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
         resolve(data as Erp_Tablesets_RcvDtlAttrValueSetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get RcvDtlTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RcvDtlTaxes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvDtlTaxRow
   */  
export function get_RcvDtls_Company_VendorNum_PurPoint_PackSlip_PackLine_RcvDtlTaxes(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")/RcvDtlTaxes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RcvDtlTax item
   Description: Calls GetByID to retrieve the RcvDtlTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvDtlTax1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RcvDtlTaxRow
   */  
export function get_RcvDtls_Company_VendorNum_PurPoint_PackSlip_PackLine_RcvDtlTaxes_Company_VendorNum_PurPoint_PackSlip_PackLine_TaxCode_RateCode_ECAcquisitionSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RcvDtlTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")/RcvDtlTaxes(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
         resolve(data as Erp_Tablesets_RcvDtlTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get RcvDuties items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RcvDuties1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvDutyRow
   */  
export function get_RcvDtls_Company_VendorNum_PurPoint_PackSlip_PackLine_RcvDuties(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDutyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")/RcvDuties", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDutyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RcvDuty item
   Description: Calls GetByID to retrieve the RcvDuty item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvDuty1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param DutySeq Desc: DutySeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RcvDutyRow
   */  
export function get_RcvDtls_Company_VendorNum_PurPoint_PackSlip_PackLine_RcvDuties_Company_VendorNum_PurPoint_PackSlip_PackLine_DutySeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, DutySeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RcvDutyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")/RcvDuties(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + DutySeq + ")", {
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
         resolve(data as Erp_Tablesets_RcvDutyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get RcvDtlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RcvDtlAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvDtlAttchRow
   */  
export function get_RcvDtls_Company_VendorNum_PurPoint_PackSlip_PackLine_RcvDtlAttches(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")/RcvDtlAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RcvDtlAttch item
   Description: Calls GetByID to retrieve the RcvDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvDtlAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RcvDtlAttchRow
   */  
export function get_RcvDtls_Company_VendorNum_PurPoint_PackSlip_PackLine_RcvDtlAttches_Company_VendorNum_PurPoint_PackSlip_PackLine_DrawingSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RcvDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")/RcvDtlAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_RcvDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get RcvDtlAttrValueSets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RcvDtlAttrValueSets
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvDtlAttrValueSetRow
   */  
export function get_RcvDtlAttrValueSets(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlAttrValueSetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlAttrValueSets", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlAttrValueSetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RcvDtlAttrValueSets
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RcvDtlAttrValueSetRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RcvDtlAttrValueSetRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RcvDtlAttrValueSets(requestBody:Erp_Tablesets_RcvDtlAttrValueSetRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlAttrValueSets", {
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
   Summary: Calls GetByID to retrieve the RcvDtlAttrValueSet item
   Description: Calls GetByID to retrieve the RcvDtlAttrValueSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvDtlAttrValueSet
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param AttributeValueSeq Desc: AttributeValueSeq   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RcvDtlAttrValueSetRow
   */  
export function get_RcvDtlAttrValueSets_Company_VendorNum_PurPoint_PackSlip_PackLine_AttributeValueSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, AttributeValueSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RcvDtlAttrValueSetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlAttrValueSets(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + AttributeValueSeq + ")", {
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
         resolve(data as Erp_Tablesets_RcvDtlAttrValueSetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RcvDtlAttrValueSet for the service
   Description: Calls UpdateExt to update RcvDtlAttrValueSet. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RcvDtlAttrValueSet
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param AttributeValueSeq Desc: AttributeValueSeq   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RcvDtlAttrValueSetRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RcvDtlAttrValueSets_Company_VendorNum_PurPoint_PackSlip_PackLine_AttributeValueSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, AttributeValueSeq:string, requestBody:Erp_Tablesets_RcvDtlAttrValueSetRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlAttrValueSets(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + AttributeValueSeq + ")", {
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
   Summary: Call UpdateExt to delete RcvDtlAttrValueSet item
   Description: Call UpdateExt to delete RcvDtlAttrValueSet item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RcvDtlAttrValueSet
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param AttributeValueSeq Desc: AttributeValueSeq   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RcvDtlAttrValueSets_Company_VendorNum_PurPoint_PackSlip_PackLine_AttributeValueSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, AttributeValueSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlAttrValueSets(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + AttributeValueSeq + ")", {
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
   Description: Get RcvDtlTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RcvDtlTaxes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvDtlTaxRow
   */  
export function get_RcvDtlTaxes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlTaxes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RcvDtlTaxes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RcvDtlTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RcvDtlTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RcvDtlTaxes(requestBody:Erp_Tablesets_RcvDtlTaxRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlTaxes", {
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
   Summary: Calls GetByID to retrieve the RcvDtlTax item
   Description: Calls GetByID to retrieve the RcvDtlTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvDtlTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RcvDtlTaxRow
   */  
export function get_RcvDtlTaxes_Company_VendorNum_PurPoint_PackSlip_PackLine_TaxCode_RateCode_ECAcquisitionSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RcvDtlTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlTaxes(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
         resolve(data as Erp_Tablesets_RcvDtlTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RcvDtlTax for the service
   Description: Calls UpdateExt to update RcvDtlTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RcvDtlTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RcvDtlTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RcvDtlTaxes_Company_VendorNum_PurPoint_PackSlip_PackLine_TaxCode_RateCode_ECAcquisitionSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, requestBody:Erp_Tablesets_RcvDtlTaxRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlTaxes(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Summary: Call UpdateExt to delete RcvDtlTax item
   Description: Call UpdateExt to delete RcvDtlTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RcvDtlTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RcvDtlTaxes_Company_VendorNum_PurPoint_PackSlip_PackLine_TaxCode_RateCode_ECAcquisitionSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlTaxes(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Description: Get RcvDuties items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RcvDuties
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvDutyRow
   */  
export function get_RcvDuties(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDutyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDuties", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDutyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RcvDuties
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RcvDutyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RcvDutyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RcvDuties(requestBody:Erp_Tablesets_RcvDutyRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDuties", {
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
   Summary: Calls GetByID to retrieve the RcvDuty item
   Description: Calls GetByID to retrieve the RcvDuty item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvDuty
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param DutySeq Desc: DutySeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RcvDutyRow
   */  
export function get_RcvDuties_Company_VendorNum_PurPoint_PackSlip_PackLine_DutySeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, DutySeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RcvDutyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDuties(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + DutySeq + ")", {
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
         resolve(data as Erp_Tablesets_RcvDutyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RcvDuty for the service
   Description: Calls UpdateExt to update RcvDuty. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RcvDuty
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param DutySeq Desc: DutySeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RcvDutyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RcvDuties_Company_VendorNum_PurPoint_PackSlip_PackLine_DutySeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, DutySeq:string, requestBody:Erp_Tablesets_RcvDutyRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDuties(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + DutySeq + ")", {
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
   Summary: Call UpdateExt to delete RcvDuty item
   Description: Call UpdateExt to delete RcvDuty item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RcvDuty
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param DutySeq Desc: DutySeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RcvDuties_Company_VendorNum_PurPoint_PackSlip_PackLine_DutySeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, DutySeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDuties(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + DutySeq + ")", {
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
   Description: Get RcvDtlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RcvDtlAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvDtlAttchRow
   */  
export function get_RcvDtlAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RcvDtlAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RcvDtlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RcvDtlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RcvDtlAttches(requestBody:Erp_Tablesets_RcvDtlAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlAttches", {
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
   Summary: Calls GetByID to retrieve the RcvDtlAttch item
   Description: Calls GetByID to retrieve the RcvDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RcvDtlAttchRow
   */  
export function get_RcvDtlAttches_Company_VendorNum_PurPoint_PackSlip_PackLine_DrawingSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RcvDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_RcvDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RcvDtlAttch for the service
   Description: Calls UpdateExt to update RcvDtlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RcvDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RcvDtlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RcvDtlAttches_Company_VendorNum_PurPoint_PackSlip_PackLine_DrawingSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, DrawingSeq:string, requestBody:Erp_Tablesets_RcvDtlAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete RcvDtlAttch item
   Description: Call UpdateExt to delete RcvDtlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RcvDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RcvDtlAttches_Company_VendorNum_PurPoint_PackSlip_PackLine_DrawingSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + DrawingSeq + ")", {
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
   Description: Get RcvMiscs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RcvMiscs
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvMiscRow
   */  
export function get_RcvMiscs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvMiscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvMiscs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvMiscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RcvMiscs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RcvMiscRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RcvMiscRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RcvMiscs(requestBody:Erp_Tablesets_RcvMiscRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvMiscs", {
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
   Summary: Calls GetByID to retrieve the RcvMisc item
   Description: Calls GetByID to retrieve the RcvMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvMisc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param MiscSeq Desc: MiscSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RcvMiscRow
   */  
export function get_RcvMiscs_Company_VendorNum_PurPoint_PackSlip_MiscSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, MiscSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RcvMiscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvMiscs(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + MiscSeq + ")", {
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
         resolve(data as Erp_Tablesets_RcvMiscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RcvMisc for the service
   Description: Calls UpdateExt to update RcvMisc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RcvMisc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param MiscSeq Desc: MiscSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RcvMiscRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RcvMiscs_Company_VendorNum_PurPoint_PackSlip_MiscSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, MiscSeq:string, requestBody:Erp_Tablesets_RcvMiscRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvMiscs(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + MiscSeq + ")", {
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
   Summary: Call UpdateExt to delete RcvMisc item
   Description: Call UpdateExt to delete RcvMisc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RcvMisc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param MiscSeq Desc: MiscSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RcvMiscs_Company_VendorNum_PurPoint_PackSlip_MiscSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, MiscSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvMiscs(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + MiscSeq + ")", {
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
   Description: Get RcvMiscTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RcvMiscTaxes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param MiscSeq Desc: MiscSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvMiscTaxRow
   */  
export function get_RcvMiscs_Company_VendorNum_PurPoint_PackSlip_MiscSeq_RcvMiscTaxes(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, MiscSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvMiscTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvMiscs(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + MiscSeq + ")/RcvMiscTaxes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvMiscTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RcvMiscTax item
   Description: Calls GetByID to retrieve the RcvMiscTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvMiscTax1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param MiscSeq Desc: MiscSeq   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RcvMiscTaxRow
   */  
export function get_RcvMiscs_Company_VendorNum_PurPoint_PackSlip_MiscSeq_RcvMiscTaxes_Company_VendorNum_PurPoint_PackSlip_MiscSeq_TaxCode_RateCode_ECAcquisitionSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, MiscSeq:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RcvMiscTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvMiscs(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + MiscSeq + ")/RcvMiscTaxes(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + MiscSeq + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
         resolve(data as Erp_Tablesets_RcvMiscTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get RcvMiscTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RcvMiscTaxes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvMiscTaxRow
   */  
export function get_RcvMiscTaxes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvMiscTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvMiscTaxes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvMiscTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RcvMiscTaxes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RcvMiscTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RcvMiscTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RcvMiscTaxes(requestBody:Erp_Tablesets_RcvMiscTaxRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvMiscTaxes", {
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
   Summary: Calls GetByID to retrieve the RcvMiscTax item
   Description: Calls GetByID to retrieve the RcvMiscTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvMiscTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param MiscSeq Desc: MiscSeq   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RcvMiscTaxRow
   */  
export function get_RcvMiscTaxes_Company_VendorNum_PurPoint_PackSlip_MiscSeq_TaxCode_RateCode_ECAcquisitionSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, MiscSeq:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RcvMiscTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvMiscTaxes(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + MiscSeq + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
         resolve(data as Erp_Tablesets_RcvMiscTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RcvMiscTax for the service
   Description: Calls UpdateExt to update RcvMiscTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RcvMiscTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param MiscSeq Desc: MiscSeq   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RcvMiscTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RcvMiscTaxes_Company_VendorNum_PurPoint_PackSlip_MiscSeq_TaxCode_RateCode_ECAcquisitionSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, MiscSeq:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, requestBody:Erp_Tablesets_RcvMiscTaxRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvMiscTaxes(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + MiscSeq + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Summary: Call UpdateExt to delete RcvMiscTax item
   Description: Call UpdateExt to delete RcvMiscTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RcvMiscTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param MiscSeq Desc: MiscSeq   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RcvMiscTaxes_Company_VendorNum_PurPoint_PackSlip_MiscSeq_TaxCode_RateCode_ECAcquisitionSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, MiscSeq:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvMiscTaxes(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + MiscSeq + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Description: Get RcvHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RcvHeadAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvHeadAttchRow
   */  
export function get_RcvHeadAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvHeadAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RcvHeadAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RcvHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RcvHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RcvHeadAttches(requestBody:Erp_Tablesets_RcvHeadAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvHeadAttches", {
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
   Summary: Calls GetByID to retrieve the RcvHeadAttch item
   Description: Calls GetByID to retrieve the RcvHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvHeadAttch
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
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RcvHeadAttchRow
   */  
export function get_RcvHeadAttches_Company_VendorNum_PurPoint_PackSlip_DrawingSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RcvHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvHeadAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_RcvHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RcvHeadAttch for the service
   Description: Calls UpdateExt to update RcvHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RcvHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RcvHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RcvHeadAttches_Company_VendorNum_PurPoint_PackSlip_DrawingSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, DrawingSeq:string, requestBody:Erp_Tablesets_RcvHeadAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvHeadAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete RcvHeadAttch item
   Description: Call UpdateExt to delete RcvHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RcvHeadAttch
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
export function delete_RcvHeadAttches_Company_VendorNum_PurPoint_PackSlip_DrawingSeq(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvHeadAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + DrawingSeq + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/LegalNumGenOpts", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/LegalNumGenOpts", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
   Description: Get PendingRcvDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PendingRcvDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PendingRcvDtlRow
   */  
export function get_PendingRcvDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PendingRcvDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/PendingRcvDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PendingRcvDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PendingRcvDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PendingRcvDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PendingRcvDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PendingRcvDtls(requestBody:Erp_Tablesets_PendingRcvDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/PendingRcvDtls", {
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
   Summary: Calls GetByID to retrieve the PendingRcvDtl item
   Description: Calls GetByID to retrieve the PendingRcvDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PendingRcvDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORel Desc: PORel   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PendingRcvDtlRow
   */  
export function get_PendingRcvDtls_Company_VendorNum_PurPoint_PackSlip_PONum_POLine_PORel(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PONum:string, POLine:string, PORel:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PendingRcvDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/PendingRcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PONum + "," + POLine + "," + PORel + ")", {
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
         resolve(data as Erp_Tablesets_PendingRcvDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PendingRcvDtl for the service
   Description: Calls UpdateExt to update PendingRcvDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PendingRcvDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORel Desc: PORel   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PendingRcvDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PendingRcvDtls_Company_VendorNum_PurPoint_PackSlip_PONum_POLine_PORel(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PONum:string, POLine:string, PORel:string, requestBody:Erp_Tablesets_PendingRcvDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/PendingRcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PONum + "," + POLine + "," + PORel + ")", {
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
   Summary: Call UpdateExt to delete PendingRcvDtl item
   Description: Call UpdateExt to delete PendingRcvDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PendingRcvDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORel Desc: PORel   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PendingRcvDtls_Company_VendorNum_PurPoint_PackSlip_PONum_POLine_PORel(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PONum:string, POLine:string, PORel:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/PendingRcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PONum + "," + POLine + "," + PORel + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SelectedSerialNumbers", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SelectedSerialNumbers", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SNFormats", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SNFormats", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", {
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
   Description: Get SupplierXRefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SupplierXRefs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SupplierXRefRow
   */  
export function get_SupplierXRefs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SupplierXRefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SupplierXRefs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SupplierXRefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SupplierXRefs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SupplierXRefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.SupplierXRefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SupplierXRefs(requestBody:Erp_Tablesets_SupplierXRefRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SupplierXRefs", {
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
   Summary: Calls GetByID to retrieve the SupplierXRef item
   Description: Calls GetByID to retrieve the SupplierXRef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SupplierXRef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param VendNum Desc: VendNum   Required: True
      @param VendPartNum Desc: VendPartNum   Required: True   Allow empty value : True
      @param MfgNum Desc: MfgNum   Required: True
      @param MfgPartNum Desc: MfgPartNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.SupplierXRefRow
   */  
export function get_SupplierXRefs_Company_PartNum_VendNum_VendPartNum_MfgNum_MfgPartNum(Company:string, PartNum:string, VendNum:string, VendPartNum:string, MfgNum:string, MfgPartNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SupplierXRefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", {
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
         resolve(data as Erp_Tablesets_SupplierXRefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SupplierXRef for the service
   Description: Calls UpdateExt to update SupplierXRef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SupplierXRef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param VendNum Desc: VendNum   Required: True
      @param VendPartNum Desc: VendPartNum   Required: True   Allow empty value : True
      @param MfgNum Desc: MfgNum   Required: True
      @param MfgPartNum Desc: MfgPartNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.SupplierXRefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SupplierXRefs_Company_PartNum_VendNum_VendPartNum_MfgNum_MfgPartNum(Company:string, PartNum:string, VendNum:string, VendPartNum:string, MfgNum:string, MfgPartNum:string, requestBody:Erp_Tablesets_SupplierXRefRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", {
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
   Summary: Call UpdateExt to delete SupplierXRef item
   Description: Call UpdateExt to delete SupplierXRef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SupplierXRef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param VendNum Desc: VendNum   Required: True
      @param VendPartNum Desc: VendPartNum   Required: True   Allow empty value : True
      @param MfgNum Desc: MfgNum   Required: True
      @param MfgPartNum Desc: MfgPartNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SupplierXRefs_Company_PartNum_VendNum_VendPartNum_MfgNum_MfgPartNum(Company:string, PartNum:string, VendNum:string, VendPartNum:string, MfgNum:string, MfgPartNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvHeadListRow)
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
export function get_GetRows(whereClauseRcvHead:string, whereClauseRcvHeadAttch:string, whereClauseRcvHeadTax:string, whereClauseRcvDtl:string, whereClauseRcvDtlAttch:string, whereClauseRcvDtlAttrValueSet:string, whereClauseRcvDtlTax:string, whereClauseRcvDuty:string, whereClauseRcvMisc:string, whereClauseRcvMiscTax:string, whereClauseLegalNumGenOpts:string, whereClausePendingRcvDtl:string, whereClauseSelectedSerialNumbers:string, whereClauseSNFormat:string, whereClauseSupplierXRef:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseRcvHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRcvHead=" + whereClauseRcvHead
   }
   if(typeof whereClauseRcvHeadAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRcvHeadAttch=" + whereClauseRcvHeadAttch
   }
   if(typeof whereClauseRcvHeadTax!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRcvHeadTax=" + whereClauseRcvHeadTax
   }
   if(typeof whereClauseRcvDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRcvDtl=" + whereClauseRcvDtl
   }
   if(typeof whereClauseRcvDtlAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRcvDtlAttch=" + whereClauseRcvDtlAttch
   }
   if(typeof whereClauseRcvDtlAttrValueSet!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRcvDtlAttrValueSet=" + whereClauseRcvDtlAttrValueSet
   }
   if(typeof whereClauseRcvDtlTax!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRcvDtlTax=" + whereClauseRcvDtlTax
   }
   if(typeof whereClauseRcvDuty!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRcvDuty=" + whereClauseRcvDuty
   }
   if(typeof whereClauseRcvMisc!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRcvMisc=" + whereClauseRcvMisc
   }
   if(typeof whereClauseRcvMiscTax!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRcvMiscTax=" + whereClauseRcvMiscTax
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
   if(typeof whereClausePendingRcvDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePendingRcvDtl=" + whereClausePendingRcvDtl
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
   if(typeof whereClauseSupplierXRef!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSupplierXRef=" + whereClauseSupplierXRef
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetRows" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetList" + params, {
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
   Summary: Invoke method MassReceiptsGeneratePCIDUpdate
   Description: This method updates the new PCID Generated data for all RcvDtls selected via Mass Receipt.
   OperationID: MassReceiptsGeneratePCIDUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MassReceiptsGeneratePCIDUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassReceiptsGeneratePCIDUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MassReceiptsGeneratePCIDUpdate(requestBody:MassReceiptsGeneratePCIDUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MassReceiptsGeneratePCIDUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/MassReceiptsGeneratePCIDUpdate", {
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
         resolve(data as MassReceiptsGeneratePCIDUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedTaxManual
   Description: Method to call when changing the manual tax calculation value on a line or indirect cost tax record. Updates RcvDtlTax / RcvMiscTax
tax amounts based on the new value of the flag back to system-calculated tax.
   OperationID: OnChangedTaxManual
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangedTaxManual_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedTaxManual_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedTaxManual(requestBody:OnChangedTaxManual_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangedTaxManual_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangedTaxManual", {
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
         resolve(data as OnChangedTaxManual_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTaxFixedAmount
   Description: Method to call when changing the fixed amount on the RcvDtlTax table currently
   OperationID: OnChangeTaxFixedAmount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTaxFixedAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxFixedAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTaxFixedAmount(requestBody:OnChangeTaxFixedAmount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTaxFixedAmount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeTaxFixedAmount", {
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
         resolve(data as OnChangeTaxFixedAmount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTaxReportableAmt
   Description: Method to call when changing the reportable amount on either RcvMiscTax or RcvDtlTax
reportable amounts based on the new reportable amount.
   OperationID: OnChangeTaxReportableAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTaxReportableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxReportableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTaxReportableAmt(requestBody:OnChangeTaxReportableAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTaxReportableAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeTaxReportableAmt", {
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
         resolve(data as OnChangeTaxReportableAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTaxTaxableAmt
   Description: Method to call when changing the taxable amount on either RcvMiscTax or RcvDtlTax
taxable amounts based on the new taxable amount.
   OperationID: OnChangeTaxTaxableAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTaxTaxableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxTaxableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTaxTaxableAmt(requestBody:OnChangeTaxTaxableAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTaxTaxableAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeTaxTaxableAmt", {
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
         resolve(data as OnChangeTaxTaxableAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTaxTaxAmt
   Description: Method to call when changing the tax amount on a either a RcvMiscTax or a RcvDtlTax row
tax amounts based on the new tax amount.
   OperationID: OnChangeTaxTaxAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTaxTaxAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxTaxAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTaxTaxAmt(requestBody:OnChangeTaxTaxAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTaxTaxAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeTaxTaxAmt", {
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
         resolve(data as OnChangeTaxTaxAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTaxDeductable
   Description: Method to call when changing the tax deductable on a Release line tax record.
   OperationID: OnChangeTaxDeductable
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTaxDeductable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxDeductable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTaxDeductable(requestBody:OnChangeTaxDeductable_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTaxDeductable_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeTaxDeductable", {
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
         resolve(data as OnChangeTaxDeductable_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTaxTaxCode
   Description: Method to call when changing the tax code on a the RcvMiscTax or RcvDtlTax.  Validates the tax code and
updates RcvDtlTax tax amounts based on the new tax code.
   OperationID: OnChangeTaxTaxCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTaxTaxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxTaxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTaxTaxCode(requestBody:OnChangeTaxTaxCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTaxTaxCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeTaxTaxCode", {
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
         resolve(data as OnChangeTaxTaxCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTaxRateCode
   Description: Method to call when changing the rate code on a tax record related to Release Tax Line.  Validates the rate and tax code
   OperationID: OnChangeTaxRateCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTaxRateCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxRateCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTaxRateCode(requestBody:OnChangeTaxRateCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTaxRateCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeTaxRateCode", {
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
         resolve(data as OnChangeTaxRateCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTaxPercent
   Description: Method to call when changing the tax percent on a tax release line record.  Updates RcvDtlTax
tax amounts based on the new tax percent only when one tax record exists.
   OperationID: OnChangeTaxPercent
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTaxPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTaxPercent(requestBody:OnChangeTaxPercent_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTaxPercent_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeTaxPercent", {
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
         resolve(data as OnChangeTaxPercent_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDutyTariffCode
   Description: This method should be invoked when the Tariff Code changes. This method will validate
the tariffcode and defaults the duty amount.
   OperationID: OnChangeDutyTariffCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDutyTariffCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDutyTariffCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDutyTariffCode(requestBody:OnChangeDutyTariffCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDutyTariffCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeDutyTariffCode", {
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
         resolve(data as OnChangeDutyTariffCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscApplyDate
   Description: This method should be invoked when the Apply Date in RcvMisc changes.
This method will validate the date and get new exchange rate.
   OperationID: OnChangeMiscApplyDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscApplyDate(requestBody:OnChangeMiscApplyDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscApplyDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeMiscApplyDate", {
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
         resolve(data as OnChangeMiscApplyDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscCharge
   Description: This method should be invoked when the Miscellaneous Charge ID changes. This
method will validate the misc. charge and pull in the new default information.
   OperationID: OnChangeMiscCharge
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscCharge_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscCharge_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscCharge(requestBody:OnChangeMiscCharge_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscCharge_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeMiscCharge", {
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
         resolve(data as OnChangeMiscCharge_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscCurrencyCode
   Description: This method should be invoked when the Currency Code in RcvMisc changes.
This method will validate the currency code and pull in the new default information.
   OperationID: OnChangeMiscCurrencyCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscCurrencyCode(requestBody:OnChangeMiscCurrencyCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscCurrencyCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeMiscCurrencyCode", {
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
         resolve(data as OnChangeMiscCurrencyCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscDocActualAmt
   Description: This method should be invoked when the RcvMisc.ActualAmt changes. This
method will validate the amount and convert it to the base currency.
   OperationID: OnChangeMiscDocActualAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscDocActualAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscDocActualAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscDocActualAmt(requestBody:OnChangeMiscDocActualAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscDocActualAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeMiscDocActualAmt", {
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
         resolve(data as OnChangeMiscDocActualAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscExchangeRate
   Description: This method should be invoked when the Currency Exchange Rate in RcvMisc changes.
   OperationID: OnChangeMiscExchangeRate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscExchangeRate(requestBody:OnChangeMiscExchangeRate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscExchangeRate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeMiscExchangeRate", {
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
         resolve(data as OnChangeMiscExchangeRate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscInvoiceLine
   Description: This method should be invoked when the Invoice Line in RcvMisc changes.
This method will validate the invoice line and pull in the new default information.
   OperationID: OnChangeMiscInvoiceLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscInvoiceLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscInvoiceLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscInvoiceLine(requestBody:OnChangeMiscInvoiceLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscInvoiceLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeMiscInvoiceLine", {
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
         resolve(data as OnChangeMiscInvoiceLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscInvoiceNum
   Description: This method should be invoked when the Invoice Number in RcvMisc changes.
This method will validate the invoice number and pull in the new default information.
   OperationID: OnChangeMiscInvoiceNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscInvoiceNum(requestBody:OnChangeMiscInvoiceNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscInvoiceNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeMiscInvoiceNum", {
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
         resolve(data as OnChangeMiscInvoiceNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscMscNum
   Description: This method should be invoked when the MscNum in RcvMisc changes.
This method will validate the MscNum and pull in the new default information.
   OperationID: OnChangeMiscMscNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscMscNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscMscNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscMscNum(requestBody:OnChangeMiscMscNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscMscNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeMiscMscNum", {
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
         resolve(data as OnChangeMiscMscNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscPercent
   Description: This method should be invoked when the RcvMisc.Percentage changes.
This method will calculate the amount and convert it to the base currency.
   OperationID: OnChangeMiscPercent
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscPercent(requestBody:OnChangeMiscPercent_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscPercent_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeMiscPercent", {
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
         resolve(data as OnChangeMiscPercent_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscRateGrp
   Description: This method should be invoked when the Currency Rate Group in RcvMisc changes.
This method will validate the rate group and get new exchange rate.
   OperationID: OnChangeMiscRateGrp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscRateGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscRateGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscRateGrp(requestBody:OnChangeMiscRateGrp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscRateGrp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeMiscRateGrp", {
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
         resolve(data as OnChangeMiscRateGrp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscTaxCatID
   Description: This method should be invoked when TaxCatID changes. It will retrieve the default tax flag based on entered Tax Cat ID.
   OperationID: OnChangeMiscTaxCatID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscTaxCatID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscTaxCatID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscTaxCatID(requestBody:OnChangeMiscTaxCatID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscTaxCatID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeMiscTaxCatID", {
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
         resolve(data as OnChangeMiscTaxCatID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMiscVendor
   Description: This method should be invoked when the vendor ID in RcvMisc changes.
This method will validate the vendor and pull in the new default vendor information.
   OperationID: OnChangeMiscVendor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMiscVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMiscVendor(requestBody:OnChangeMiscVendor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMiscVendor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeMiscVendor", {
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
         resolve(data as OnChangeMiscVendor_output)
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
<param name="ipPartNum">ipPartNum</param><param name="ipAttributeSetID">ipAttributeSetID</param><param name="ipQuantity">ipQuantity</param><param name="ipUOM">ipUOM</param><param name="ipVendNum">ipVendNum</param><param name="ipVendPP">ipVendPP</param><param name="ipPackSlip">ipPackSlip</param><param name="ipPackSlipLine">ipPackSlipLine</param><param name="ipJobNum">ipJobNum</param><param name="ipAsmSeq">ipAssmSeq</param><param name="ipSubOprSeq">ipSubOprSeq</param><param name="ipReceivedTo">ipReceivedTo</param><returns></returns>
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetSelectSerialNumbersParams", {
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
   Summary: Invoke method GetSNStatus
   OperationID: GetSNStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSNStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSNStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSNStatus(requestBody:GetSNStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSNStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetSNStatus", {
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
         resolve(data as GetSNStatus_output)
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
<param name="ipPartNum">Part Number</param><param name="ipAttributeSetID">Serial Number</param><param name="ipSerialNo">Serial Number</param><param name="ipVendorNum">Vendor Number</param><param name="ipJobNum">Job Number</param><param name="ipAsmSeq">Vendor Number</param><param name="ipSubOprSeq">Job Operation Number</param><param name="ipPackSlip">Pack Slip</param><param name="ipPackLine">Pack Slip Line</param><param name="ipReceivedTo">Received To</param><param name="ipJobSeqType">Job Sequence type</param><param name="warningMsg">Warning Message</param>
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/ValidateSN", {
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
   Summary: Invoke method CheckMassReceiptChangeWhseBin
   Description: This method is obsolete use OnChangeDtlWarehouseCode / OnChangeDtlBin instead.
            
If warehouse or bin is changed in MassReceipts and this is a Planning Contract receipt
then we need to validate against the Contract
   OperationID: CheckMassReceiptChangeWhseBin
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckMassReceiptChangeWhseBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckMassReceiptChangeWhseBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckMassReceiptChangeWhseBin(requestBody:CheckMassReceiptChangeWhseBin_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckMassReceiptChangeWhseBin_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CheckMassReceiptChangeWhseBin", {
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
         resolve(data as CheckMassReceiptChangeWhseBin_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CommitRcvDtl
   Description: This method creates the Lines Received from MassReceipt option directly
into the DB. This was done for performance purposes.
   OperationID: CommitRcvDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CommitRcvDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CommitRcvDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CommitRcvDtl(requestBody:CommitRcvDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CommitRcvDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CommitRcvDtl", {
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
         resolve(data as CommitRcvDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateMassReceipts
   Description: This method is used to populate the ShipDtl datatable for Mass Receipts
and Intercompany Receipt linking
   OperationID: CreateMassReceipts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateMassReceipts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateMassReceipts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateMassReceipts(requestBody:CreateMassReceipts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateMassReceipts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CreateMassReceipts", {
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
         resolve(data as CreateMassReceipts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method HHCanEditPackSlip
   Description: This method was developed for HandHeld version to validate if a
pack slipt exist. In the handheld version users can't edit the lines.
   OperationID: HHCanEditPackSlip
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/HHCanEditPackSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HHCanEditPackSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HHCanEditPackSlip(requestBody:HHCanEditPackSlip_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<HHCanEditPackSlip_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/HHCanEditPackSlip", {
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
         resolve(data as HHCanEditPackSlip_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method HHOnChangeDtlPartNum
   Description: This method is called by HHPOReceipt when a Part is entered.  It will check for multiple parts using the LibFindpart library.  It will then find the first open PO line for the entered part and populate the RcvDtl with the details for the PODetail and PORel.
   OperationID: HHOnChangeDtlPartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/HHOnChangeDtlPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HHOnChangeDtlPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HHOnChangeDtlPartNum(requestBody:HHOnChangeDtlPartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<HHOnChangeDtlPartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/HHOnChangeDtlPartNum", {
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
         resolve(data as HHOnChangeDtlPartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method HHOnChangeDtlPOLine
   Description: This method is called by HHPOReceipt when a PO Line is entered.  It will make sure an open PO line exists for the entered Part and Line and populate the RcvDtl with details for the PODetail and PORel.
   OperationID: HHOnChangeDtlPOLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/HHOnChangeDtlPOLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HHOnChangeDtlPOLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HHOnChangeDtlPOLine(requestBody:HHOnChangeDtlPOLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<HHOnChangeDtlPOLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/HHOnChangeDtlPOLine", {
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
         resolve(data as HHOnChangeDtlPOLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method HHOnChangeDtlPORelNum
   Description: This method is called by HHPOReceipt when a PO Release Number is entered.  It will make sure an open PO line exists for the entered Part, Line and Release and populate the RcvDtl with details for the PODetail and PORel.
   OperationID: HHOnChangeDtlPORelNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/HHOnChangeDtlPORelNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HHOnChangeDtlPORelNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HHOnChangeDtlPORelNum(requestBody:HHOnChangeDtlPORelNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<HHOnChangeDtlPORelNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/HHOnChangeDtlPORelNum", {
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
         resolve(data as HHOnChangeDtlPORelNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method HHValRecDocReq
   Description: This method is to be called by the Hand Held PO Receipt program.
It can be called before or after calling the update for the RcvDtl.
It checks to see if receipt documents are required for a given Part/Lot number.
If they are then message text is returned in the infoMsg parameter.
The client displays this in a message box.
Note: For Hand Held this is only an informational and not an exception.
   OperationID: HHValRecDocReq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/HHValRecDocReq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HHValRecDocReq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HHValRecDocReq(requestBody:HHValRecDocReq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<HHValRecDocReq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/HHValRecDocReq", {
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
         resolve(data as HHValRecDocReq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateSMIReceiptAttrPart
   Description: This method is used to Validate if the Receipt Line contains a Part with Track inventory Attributes and the POType equals SMI
and Intercompany Receipt linking
   OperationID: ValidateSMIReceiptAttrPart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateSMIReceiptAttrPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSMIReceiptAttrPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSMIReceiptAttrPart(requestBody:ValidateSMIReceiptAttrPart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateSMIReceiptAttrPart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/ValidateSMIReceiptAttrPart", {
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
         resolve(data as ValidateSMIReceiptAttrPart_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRcvHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRcvHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRcvHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRcvHead(requestBody:GetNewRcvHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRcvHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetNewRcvHead", {
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
         resolve(data as GetNewRcvHead_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRcvHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRcvHeadAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRcvHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRcvHeadAttch(requestBody:GetNewRcvHeadAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRcvHeadAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetNewRcvHeadAttch", {
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
         resolve(data as GetNewRcvHeadAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRcvHeadTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRcvHeadTax
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRcvHeadTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvHeadTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRcvHeadTax(requestBody:GetNewRcvHeadTax_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRcvHeadTax_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetNewRcvHeadTax", {
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
         resolve(data as GetNewRcvHeadTax_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRcvDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRcvDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRcvDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRcvDtl(requestBody:GetNewRcvDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRcvDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetNewRcvDtl", {
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
         resolve(data as GetNewRcvDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRcvDtlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRcvDtlAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRcvDtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvDtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRcvDtlAttch(requestBody:GetNewRcvDtlAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRcvDtlAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetNewRcvDtlAttch", {
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
         resolve(data as GetNewRcvDtlAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRcvDtlAttrValueSet
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRcvDtlAttrValueSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRcvDtlAttrValueSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvDtlAttrValueSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRcvDtlAttrValueSet(requestBody:GetNewRcvDtlAttrValueSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRcvDtlAttrValueSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetNewRcvDtlAttrValueSet", {
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
         resolve(data as GetNewRcvDtlAttrValueSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRcvDtlTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRcvDtlTax
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRcvDtlTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvDtlTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRcvDtlTax(requestBody:GetNewRcvDtlTax_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRcvDtlTax_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetNewRcvDtlTax", {
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
         resolve(data as GetNewRcvDtlTax_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRcvDuty
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRcvDuty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRcvDuty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvDuty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRcvDuty(requestBody:GetNewRcvDuty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRcvDuty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetNewRcvDuty", {
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
         resolve(data as GetNewRcvDuty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRcvMisc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRcvMisc
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRcvMisc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvMisc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRcvMisc(requestBody:GetNewRcvMisc_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRcvMisc_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetNewRcvMisc", {
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
         resolve(data as GetNewRcvMisc_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRcvMiscTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRcvMiscTax
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRcvMiscTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvMiscTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRcvMiscTax(requestBody:GetNewRcvMiscTax_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRcvMiscTax_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetNewRcvMiscTax", {
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
         resolve(data as GetNewRcvMiscTax_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/UpdateExt", {
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

   /**  
   Summary: Invoke method GetMtlQueueSeqValue
   Description: Search for the MtlQueueSeq value from the MtlQueue row related to the current Non Conformance.
   OperationID: GetMtlQueueSeqValue
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetMtlQueueSeqValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlQueueSeqValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMtlQueueSeqValue(requestBody:GetMtlQueueSeqValue_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetMtlQueueSeqValue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetMtlQueueSeqValue", {
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
         resolve(data as GetMtlQueueSeqValue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AssignLegalNumber
   Description: Assign Legal Number to Packing Slip.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/AssignLegalNumber", {
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
   Summary: Invoke method CalculateReceiptTaxes
   Description: CALCULATE VANTAGE\TAX CONNECT TAX CALCULATIONS UI NEEDS TO CALL A SAVE BEFORE CALLING THIS PROCEDURE
   OperationID: CalculateReceiptTaxes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CalculateReceiptTaxes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateReceiptTaxes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalculateReceiptTaxes(requestBody:CalculateReceiptTaxes_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CalculateReceiptTaxes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CalculateReceiptTaxes", {
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
         resolve(data as CalculateReceiptTaxes_output)
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
<param name="sMessage">Warning</param><param name="ds"></param>
   OperationID: CheckCNCustomsDeclarationBillLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckCNCustomsDeclarationBillLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCNCustomsDeclarationBillLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCNCustomsDeclarationBillLine(requestBody:CheckCNCustomsDeclarationBillLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckCNCustomsDeclarationBillLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CheckCNCustomsDeclarationBillLine", {
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
         resolve(data as CheckCNCustomsDeclarationBillLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CNPreUpdate
   Description: Purpose:  Method should be called before Update to check China specific data
Parameters:
<param name="sMessage">Warning</param><param name="ds"></param>
   OperationID: CNPreUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CNPreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CNPreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CNPreUpdate(requestBody:CNPreUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CNPreUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CNPreUpdate", {
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
         resolve(data as CNPreUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckCompliance
   Description: .
   OperationID: CheckCompliance
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckCompliance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCompliance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCompliance(requestBody:CheckCompliance_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckCompliance_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CheckCompliance", {
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
         resolve(data as CheckCompliance_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckContainersBeforeUpdate
   Description: This method is to be called right before the update of a ContainerReceipt.  If
there is a discrepancy between the quantities, serial numbers the
user is asked if they are sure they want to continue.
            
qQuestion and sQuestion are provided so the UI can format the message box
and make it easier for the end user to read the text.
   OperationID: CheckContainersBeforeUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckContainersBeforeUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckContainersBeforeUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckContainersBeforeUpdate(requestBody:CheckContainersBeforeUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckContainersBeforeUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CheckContainersBeforeUpdate", {
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
         resolve(data as CheckContainersBeforeUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckForDefaultRcvInfo
   Description: This method is to be run right after the form opens to determine whether the
default receiving warehouse and bin have been populated for the cur-plant.
If not, the form will close.
   OperationID: CheckForDefaultRcvInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckForDefaultRcvInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckForDefaultRcvInfo(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckForDefaultRcvInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CheckForDefaultRcvInfo", {
          method: 'post',
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
         resolve(data as CheckForDefaultRcvInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckShipmentReceived
   Description: Validates if the Shipment has been received
   OperationID: CheckShipmentReceived
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckShipmentReceived_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckShipmentReceived_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckShipmentReceived(requestBody:CheckShipmentReceived_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckShipmentReceived_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CheckShipmentReceived", {
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
         resolve(data as CheckShipmentReceived_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ContainerReceiptsBeforeUpdate
   Description: This is invoked before the Update in Container Receipts. The following checks are done:
1. Return a warning message if any of the partial receipt lines needs to recalculate container landed costs
2. Return a warning if there is a discrepancy between the quantities
3. Return a warning if there are none compliant lines
4. Return a bool indicating if user input is required for legal numbers
   OperationID: ContainerReceiptsBeforeUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ContainerReceiptsBeforeUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ContainerReceiptsBeforeUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ContainerReceiptsBeforeUpdate(requestBody:ContainerReceiptsBeforeUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ContainerReceiptsBeforeUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/ContainerReceiptsBeforeUpdate", {
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
         resolve(data as ContainerReceiptsBeforeUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ContainerReceiptsUpdate
   Description: Invokes ReceiveContainerUpdateCore but returns an updated ContainerTrackingTableset
   OperationID: ContainerReceiptsUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ContainerReceiptsUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ContainerReceiptsUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ContainerReceiptsUpdate(requestBody:ContainerReceiptsUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ContainerReceiptsUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/ContainerReceiptsUpdate", {
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
         resolve(data as ContainerReceiptsUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateMaterialQueueForPCID
   Description: This will invoke a shared function that will check that there are no Staged items on the PCID and if not, retrieves the first Item on the PCID that is associated with a Receipt line and creates a MtlQueue using these details.
   OperationID: CreateMaterialQueueForPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateMaterialQueueForPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateMaterialQueueForPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateMaterialQueueForPCID(requestBody:CreateMaterialQueueForPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateMaterialQueueForPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CreateMaterialQueueForPCID", {
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
         resolve(data as CreateMaterialQueueForPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DisburseLandedCost
   Description: This method is used to disburse the Total Landed Cost across the receipt details.
The RcvDtl records will be updated to distribute the receipt Indirect Costs according
to the specified disburse method.  The Specific DutyAmt if available will be divided
equally among lines or by the percentage of the line's duties against total duties.
   OperationID: DisburseLandedCost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DisburseLandedCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DisburseLandedCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DisburseLandedCost(requestBody:DisburseLandedCost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DisburseLandedCost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/DisburseLandedCost", {
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
         resolve(data as DisburseLandedCost_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAvailTranDocTypes
   Description: Get "POReceipt" TranDocTypes in a filter string.
   OperationID: GetAvailTranDocTypes
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetAvailTranDocTypes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetAvailTranDocTypes", {
          method: 'post',
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
         resolve(data as GetAvailTranDocTypes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:GetCodeDescList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCodeDescList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetCodeDescList", {
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
         resolve(data as GetCodeDescList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetExistingRcvHead
   Description: Check if RcvHead information exists in DB. If so, data in CurrentTableSet is replaced.
   OperationID: GetExistingRcvHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetExistingRcvHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExistingRcvHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetExistingRcvHead(requestBody:GetExistingRcvHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetExistingRcvHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetExistingRcvHead", {
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
         resolve(data as GetExistingRcvHead_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListReceipts
   Description: <param name="whereClauseRcvDtl">Whereclause for RcvDtl table.</param>
<param name="pageSize">Page size.</param>
<param name="absolutePage">Absolute page.</param>
<param name="morePages">More pages.</param>
<returns>Epicor.Mfg.BO.InvcCustTrkDataSet</returns>
   OperationID: GetListReceipts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListReceipts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListReceipts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListReceipts(requestBody:GetListReceipts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListReceipts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetListReceipts", {
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
         resolve(data as GetListReceipts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetContainerReceiptPartTranPKs
   Description: Returns PartTran primary key details of a Container Receipt for the Pack Slip / PO Num / Vendor Num entered
   OperationID: GetContainerReceiptPartTranPKs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetContainerReceiptPartTranPKs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContainerReceiptPartTranPKs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContainerReceiptPartTranPKs(requestBody:GetContainerReceiptPartTranPKs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetContainerReceiptPartTranPKs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetContainerReceiptPartTranPKs", {
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
         resolve(data as GetContainerReceiptPartTranPKs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPartTranPKs
   Description: Returns PartTran primary key details for the Pack Slip / PO Num / Vendor Num entered
   OperationID: GetPartTranPKs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPartTranPKs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartTranPKs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartTranPKs(requestBody:GetPartTranPKs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPartTranPKs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetPartTranPKs", {
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
         resolve(data as GetPartTranPKs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPendingDtl
   Description: Updates Receipt data set with PendingDtl.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetPendingDtl", {
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
   Summary: Invoke method ValidatePONum
   Description: Validates if the Purchase Order Exists
   OperationID: ValidatePONum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidatePONum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePONum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePONum(requestBody:ValidatePONum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidatePONum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/ValidatePONum", {
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
         resolve(data as ValidatePONum_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetPOInfo", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetPurPointInfo", {
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
   Summary: Invoke method GetRowsForAPInvoice
   Description: Invokes GetRows filtering on Receipts for the specified Invoice
   OperationID: GetRowsForAPInvoice
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsForAPInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForAPInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForAPInvoice(requestBody:GetRowsForAPInvoice_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsForAPInvoice_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetRowsForAPInvoice", {
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
         resolve(data as GetRowsForAPInvoice_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsForPayment
   Description: Invokes GetRows filtering on Receipts for the specified Payment
   OperationID: GetRowsForPayment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsForPayment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForPayment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForPayment(requestBody:GetRowsForPayment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsForPayment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetRowsForPayment", {
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
         resolve(data as GetRowsForPayment_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsForPO
   Description: Invokes GetRows filtering on Receipts for the specified PO
   OperationID: GetRowsForPO
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsForPO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForPO_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForPO(requestBody:GetRowsForPO_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsForPO_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetRowsForPO", {
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
         resolve(data as GetRowsForPO_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetReceiptDetailsFromContainer
   Description: Similar function to RecieveContainer, written to obtain the RcvDetail records for the Container Landed costs tracker
   OperationID: GetReceiptDetailsFromContainer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetReceiptDetailsFromContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReceiptDetailsFromContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReceiptDetailsFromContainer(requestBody:GetReceiptDetailsFromContainer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetReceiptDetailsFromContainer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetReceiptDetailsFromContainer", {
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
         resolve(data as GetReceiptDetailsFromContainer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetReceiptRelationshipMap
   Description: Returns a serialized json string to show a Relationship Map for Receipt
   OperationID: GetReceiptRelationshipMap
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetReceiptRelationshipMap_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReceiptRelationshipMap_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReceiptRelationshipMap(requestBody:GetReceiptRelationshipMap_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetReceiptRelationshipMap_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetReceiptRelationshipMap", {
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
         resolve(data as GetReceiptRelationshipMap_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetWarningPOClosed
   Description: Set cWarning to POClosed if PO is Closed,  OpenOrder = false
   OperationID: GetWarningPOClosed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetWarningPOClosed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWarningPOClosed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetWarningPOClosed(requestBody:GetWarningPOClosed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetWarningPOClosed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetWarningPOClosed", {
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
         resolve(data as GetWarningPOClosed_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportReceipt
   Description: This method imports the Receipt Head record from the IMRcvHead table.  It returns
the unique key information on the newly created Receipt header needed to import
the detail lines.  The detail records are imported by processing Mass Receipts for
the same IntQueId as indicated here.
   OperationID: ImportReceipt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportReceipt(requestBody:ImportReceipt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportReceipt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/ImportReceipt", {
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
         resolve(data as ImportReceipt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InitializeLandedCost
   Description: This method is used to populate the MassReceipt dataset for use in Landed Costs
it also returns the default recovery account information
   OperationID: InitializeLandedCost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/InitializeLandedCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitializeLandedCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InitializeLandedCost(requestBody:InitializeLandedCost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<InitializeLandedCost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/InitializeLandedCost", {
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
         resolve(data as InitializeLandedCost_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsContainerReceived
   OperationID: IsContainerReceived
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsContainerReceived_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsContainerReceived_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsContainerReceived(requestBody:IsContainerReceived_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsContainerReceived_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/IsContainerReceived", {
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
         resolve(data as IsContainerReceived_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreUpdate
   Description: This method will return a record in the LegalNumberGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreUpdate(requestBody:PreUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/PreUpdate", {
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
         resolve(data as PreUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessLandedCosts
   Description: This method is used to process the Landed Costs into the RcvHead and RcvDtl tables
All the MassReceipt records need to be marked as modified for this
   OperationID: ProcessLandedCosts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessLandedCosts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessLandedCosts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessLandedCosts(requestBody:ProcessLandedCosts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessLandedCosts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/ProcessLandedCosts", {
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
         resolve(data as ProcessLandedCosts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessIM
   Description: Finish processing a successful IC import
   OperationID: ProcessIM
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessIM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessIM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessIM(requestBody:ProcessIM_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessIM_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/ProcessIM", {
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
         resolve(data as ProcessIM_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReceiveAll
   Description: This method updates the Quantity for the lines created from MassReceipt
   OperationID: ReceiveAll
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReceiveAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiveAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReceiveAll(requestBody:ReceiveAll_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReceiveAll_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/ReceiveAll", {
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
         resolve(data as ReceiveAll_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReceiveAllLines
   Description: Sets ttRcvDtl.Received to true in all lines selected for MassReceipt.
   OperationID: ReceiveAllLines
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReceiveAllLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiveAllLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReceiveAllLines(requestBody:ReceiveAllLines_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReceiveAllLines_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/ReceiveAllLines", {
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
         resolve(data as ReceiveAllLines_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReceiveContainerUsingArrivedDate
   Description: Purpose:  Gather existing rvcdtls and create new ones for remaining balances using a specific ArrivedDate.
This method builds the receipt data for a Container.
<param name="ds">Epicor.Mfg.BO.ReceiptDataSet</param><param name="inContainerID">ContainerID</param><param name="ipArrivedDate">Arrived Date to use for new receipt lines</param><returns>Epicor.Mfg.BO.ContainerTrackingDataSet</returns>
Notes:
   OperationID: ReceiveContainerUsingArrivedDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReceiveContainerUsingArrivedDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiveContainerUsingArrivedDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReceiveContainerUsingArrivedDate(requestBody:ReceiveContainerUsingArrivedDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReceiveContainerUsingArrivedDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/ReceiveContainerUsingArrivedDate", {
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
         resolve(data as ReceiveContainerUsingArrivedDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreReceiveContainer
   Description: Purpose:  Check to see if we can run ReceiveContainer.
Checks modules and for the existence of the
<param name="inContainerID">ContainerID</param><returns>Epicor.Mfg.BO.ContainerTrackingDataSet</returns>
Notes:
   OperationID: PreReceiveContainer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreReceiveContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreReceiveContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreReceiveContainer(requestBody:PreReceiveContainer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreReceiveContainer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/PreReceiveContainer", {
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
         resolve(data as PreReceiveContainer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReceiveContainer
   Description: Purpose:  Gather existing rvcdtls and create new ones for remaining balances.
This method builds the receipt data for a Container.
<param name="ds">Epicor.Mfg.BO.ReceiptDataSet</param><param name="inContainerID">ContainerID</param><returns>Epicor.Mfg.BO.ContainerTrackingDataSet</returns>
Notes:
   OperationID: ReceiveContainer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReceiveContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiveContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReceiveContainer(requestBody:ReceiveContainer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReceiveContainer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/ReceiveContainer", {
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
         resolve(data as ReceiveContainer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReceiveContainerUpdateUsingArriveDate
   Description: Mass Receive the po lines on a container with ArrivedDate specified to control the calcUnitCost currency conversion date.
   OperationID: ReceiveContainerUpdateUsingArriveDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReceiveContainerUpdateUsingArriveDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiveContainerUpdateUsingArriveDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReceiveContainerUpdateUsingArriveDate(requestBody:ReceiveContainerUpdateUsingArriveDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReceiveContainerUpdateUsingArriveDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/ReceiveContainerUpdateUsingArriveDate", {
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
         resolve(data as ReceiveContainerUpdateUsingArriveDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReceiveContainerUpdate
   Description: Mass Receive the po lines on a container.
   OperationID: ReceiveContainerUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReceiveContainerUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiveContainerUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReceiveContainerUpdate(requestBody:ReceiveContainerUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReceiveContainerUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/ReceiveContainerUpdate", {
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
         resolve(data as ReceiveContainerUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetPrimaryBin
   Description: Set the Part Warehouse's Primary Bin when the Warehouse is changed.
   OperationID: SetPrimaryBin
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetPrimaryBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetPrimaryBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetPrimaryBin(requestBody:SetPrimaryBin_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetPrimaryBin_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SetPrimaryBin", {
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
         resolve(data as SetPrimaryBin_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeRevisionNum
   Description: Processing when the Receipt Revision Number changes
   OperationID: OnChangeRevisionNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeRevisionNum(requestBody:OnChangeRevisionNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeRevisionNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeRevisionNum", {
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
         resolve(data as OnChangeRevisionNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeContainerHdrArrivedDate
   Description: This method should be invoked when the ContainerHeader ArrivedDate changes in the container receipt form.
This method will validate whether any POs associated with the container have a different currency rate based on the old arived date
than would be the currency rate based on the new arrived date.
opNeedsRecalc = true is returned if the UI needs to run logic to refresh the RcvDtl records in the ds
   OperationID: OnChangeContainerHdrArrivedDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeContainerHdrArrivedDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeContainerHdrArrivedDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeContainerHdrArrivedDate(requestBody:OnChangeContainerHdrArrivedDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeContainerHdrArrivedDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeContainerHdrArrivedDate", {
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
         resolve(data as OnChangeContainerHdrArrivedDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ResetLandedCostDisbursements
   Description: Initialize landed cost amounts to 0 and updates the landed cost disburse method.
   OperationID: ResetLandedCostDisbursements
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ResetLandedCostDisbursements_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetLandedCostDisbursements_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ResetLandedCostDisbursements(requestBody:ResetLandedCostDisbursements_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ResetLandedCostDisbursements_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/ResetLandedCostDisbursements", {
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
         resolve(data as ResetLandedCostDisbursements_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateMaster
   Description: Perform all validations associated with the Update.  We have combined all method calls that were being called
at update into this one method.  Making multiple BL calls is a performance issue and this increases performance.
   OperationID: UpdateMaster
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateMaster_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateMaster_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateMaster(requestBody:UpdateMaster_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateMaster_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/UpdateMaster", {
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
         resolve(data as UpdateMaster_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateMRPONum
   Description: This method validates that the PO Number is a valid PO before the Mass Receipts UI calls
   OperationID: ValidateMRPONum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateMRPONum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMRPONum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateMRPONum(requestBody:ValidateMRPONum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateMRPONum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/ValidateMRPONum", {
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
         resolve(data as ValidateMRPONum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateReceiptRecords
   Description: Check if the receipt records exists.
   OperationID: ValidateReceiptRecords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateReceiptRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateReceiptRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateReceiptRecords(requestBody:ValidateReceiptRecords_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateReceiptRecords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/ValidateReceiptRecords", {
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
         resolve(data as ValidateReceiptRecords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VoidLegalNumber
   Description: Voids the Legal Number and removes it from the Packing slip.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/VoidLegalNumber", {
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
   Summary: Invoke method CheckIfAttributeQtyMismatch
   Description: Validates if there is a remaining qty difference between the attribute quantity and the receipt line quantity
   OperationID: CheckIfAttributeQtyMismatch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckIfAttributeQtyMismatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIfAttributeQtyMismatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckIfAttributeQtyMismatch(requestBody:CheckIfAttributeQtyMismatch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckIfAttributeQtyMismatch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CheckIfAttributeQtyMismatch", {
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
         resolve(data as CheckIfAttributeQtyMismatch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckHdrBeforeUpdate
   Description: This method will return three warning messages if the Receipt Header changes
any of the UpliftPercent, ReceiptDate and ArrivedDate. The user will be asked
if the changes should be applied to all the Receipt Details as well. This method
should be called before the Update method is called.
   OperationID: CheckHdrBeforeUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckHdrBeforeUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckHdrBeforeUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckHdrBeforeUpdate(requestBody:CheckHdrBeforeUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckHdrBeforeUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CheckHdrBeforeUpdate", {
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
         resolve(data as CheckHdrBeforeUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckLCAmtBeforeUpdate
   Description: This method will return a warning message if any of the partial receipt lines
needs to recalculate container landed costs. The user will be asked if he wants to
continue to receive the line(s) or undo update to review the container landed
costs first.
   OperationID: CheckLCAmtBeforeUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckLCAmtBeforeUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckLCAmtBeforeUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckLCAmtBeforeUpdate(requestBody:CheckLCAmtBeforeUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckLCAmtBeforeUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CheckLCAmtBeforeUpdate", {
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
         resolve(data as CheckLCAmtBeforeUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckOnLeaveHead
   Description: This method needs to be run when leaving the RcvHead record either by going to another
RcvHead record or leaving the screen.  It checks that the landed cost has been evenly
disbursed between all the lines.  If not, the landed cost needs to be corrected before
leaving
It also verifies that attachements have been entered for all the parts which require them.
   OperationID: CheckOnLeaveHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckOnLeaveHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOnLeaveHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckOnLeaveHead(requestBody:CheckOnLeaveHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckOnLeaveHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CheckOnLeaveHead", {
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
         resolve(data as CheckOnLeaveHead_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPOClosedInfo
   Description: This method checks how many numbers of PO Releases are closed in the current PONum
   OperationID: CheckPOClosedInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckPOClosedInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPOClosedInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPOClosedInfo(requestBody:CheckPOClosedInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckPOClosedInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CheckPOClosedInfo", {
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
         resolve(data as CheckPOClosedInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExistsRcvHead
   Description: Check if RcvHead already exists in DB.
   OperationID: ExistsRcvHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExistsRcvHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsRcvHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExistsRcvHead(requestBody:ExistsRcvHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExistsRcvHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/ExistsRcvHead", {
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
         resolve(data as ExistsRcvHead_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExistsRcvHeadWithDifferentPO
   Description: Check if the already existing RcvHead has a different PONum than the one that is being tried to receive.
   OperationID: ExistsRcvHeadWithDifferentPO
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExistsRcvHeadWithDifferentPO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsRcvHeadWithDifferentPO_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExistsRcvHeadWithDifferentPO(requestBody:ExistsRcvHeadWithDifferentPO_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExistsRcvHeadWithDifferentPO_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/ExistsRcvHeadWithDifferentPO", {
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
         resolve(data as ExistsRcvHeadWithDifferentPO_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByIdChkContainerID
   Description: This method throws an error if the entered pack slip is for a container receipt,
used in place of GetByID
   OperationID: GetByIdChkContainerID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetByIdChkContainerID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIdChkContainerID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIdChkContainerID(requestBody:GetByIdChkContainerID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByIdChkContainerID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetByIdChkContainerID", {
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
         resolve(data as GetByIdChkContainerID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRcvHeadWithPONum
   Description: Override of GetNewRcvHead() but with PONum so that we it can be used to default values
   OperationID: GetNewRcvHeadWithPONum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRcvHeadWithPONum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvHeadWithPONum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRcvHeadWithPONum(requestBody:GetNewRcvHeadWithPONum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRcvHeadWithPONum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetNewRcvHeadWithPONum", {
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
         resolve(data as GetNewRcvHeadWithPONum_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetVendorInfo", {
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
   Summary: Invoke method RcvHeadNegInvCheck
   Description: Called to check for negative inventory on RcvHead before delete or unreceive
   OperationID: RcvHeadNegInvCheck
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RcvHeadNegInvCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RcvHeadNegInvCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RcvHeadNegInvCheck(requestBody:RcvHeadNegInvCheck_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RcvHeadNegInvCheck_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvHeadNegInvCheck", {
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
         resolve(data as RcvHeadNegInvCheck_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeHdrReceived
   Description: This method should be invoked when the Received flag in RcvHead has changed.
   OperationID: OnChangeHdrReceived
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeHdrReceived_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeHdrReceived_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeHdrReceived(requestBody:OnChangeHdrReceived_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeHdrReceived_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeHdrReceived", {
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
         resolve(data as OnChangeHdrReceived_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeHdrTaxRegionCode
   Description: Change RcvHead Tax Region Code
   OperationID: OnChangeHdrTaxRegionCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeHdrTaxRegionCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeHdrTaxRegionCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeHdrTaxRegionCode(requestBody:OnChangeHdrTaxRegionCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeHdrTaxRegionCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeHdrTaxRegionCode", {
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
         resolve(data as OnChangeHdrTaxRegionCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeContainerImportFld
   Description: This method is to be run from Container Receipt Entry when import Number or Imported From values
are changed on the Container.
   OperationID: OnChangeContainerImportFld
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeContainerImportFld_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeContainerImportFld_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeContainerImportFld(requestBody:OnChangeContainerImportFld_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeContainerImportFld_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeContainerImportFld", {
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
         resolve(data as OnChangeContainerImportFld_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedHeaderTaxManual
   Description: Method to call when the Manual Tax Flag has Changed from True to False.  Updates RcvHeadTax
tax amounts based on the new tax percent.
   OperationID: OnChangedHeaderTaxManual
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangedHeaderTaxManual_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedHeaderTaxManual_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedHeaderTaxManual(requestBody:OnChangedHeaderTaxManual_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangedHeaderTaxManual_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangedHeaderTaxManual", {
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
         resolve(data as OnChangedHeaderTaxManual_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeHeaderTaxFixedAmount
   Description: Method to call when changing the fixed amount on a tax record.  Updates RcvHeadTax
tax amounts based on the new fixed amount.
   OperationID: OnChangeHeaderTaxFixedAmount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeHeaderTaxFixedAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeHeaderTaxFixedAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeHeaderTaxFixedAmount(requestBody:OnChangeHeaderTaxFixedAmount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeHeaderTaxFixedAmount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeHeaderTaxFixedAmount", {
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
         resolve(data as OnChangeHeaderTaxFixedAmount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeHeaderTaxTaxPercent
   Description: Method to call when changing the tax percent on a tax record.  Updates RcvHeadTax
tax amounts based on the new tax percent.
   OperationID: OnChangeHeaderTaxTaxPercent
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeHeaderTaxTaxPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeHeaderTaxTaxPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeHeaderTaxTaxPercent(requestBody:OnChangeHeaderTaxTaxPercent_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeHeaderTaxTaxPercent_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeHeaderTaxTaxPercent", {
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
         resolve(data as OnChangeHeaderTaxTaxPercent_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeHeaderTaxRateCode
   Description: Method to call when changing the tax percent on a tax record.  Updates RcvHeadTax
tax amounts based on the new tax percent.
   OperationID: OnChangeHeaderTaxRateCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeHeaderTaxRateCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeHeaderTaxRateCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeHeaderTaxRateCode(requestBody:OnChangeHeaderTaxRateCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeHeaderTaxRateCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeHeaderTaxRateCode", {
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
         resolve(data as OnChangeHeaderTaxRateCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeHeaderTaxRateCodeMaster
   Description: Method to call when changing the rate code on a tax record.  Validates the rate and tax code
   OperationID: OnChangeHeaderTaxRateCodeMaster
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeHeaderTaxRateCodeMaster_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeHeaderTaxRateCodeMaster_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeHeaderTaxRateCodeMaster(requestBody:OnChangeHeaderTaxRateCodeMaster_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeHeaderTaxRateCodeMaster_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeHeaderTaxRateCodeMaster", {
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
         resolve(data as OnChangeHeaderTaxRateCodeMaster_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeHeaderTaxReportableAmt
   Description: Method to call when changing the taxable amount on a tax record.  Updates RcvHeadTax
tax amounts based on the new taxable amount.
   OperationID: OnChangeHeaderTaxReportableAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeHeaderTaxReportableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeHeaderTaxReportableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeHeaderTaxReportableAmt(requestBody:OnChangeHeaderTaxReportableAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeHeaderTaxReportableAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeHeaderTaxReportableAmt", {
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
         resolve(data as OnChangeHeaderTaxReportableAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeHeaderTaxTaxableAmt
   Description: Method to call when changing the taxable amount on a tax record.  Updates RcvHeadTax
tax amounts based on the new taxable amount.
   OperationID: OnChangeHeaderTaxTaxableAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeHeaderTaxTaxableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeHeaderTaxTaxableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeHeaderTaxTaxableAmt(requestBody:OnChangeHeaderTaxTaxableAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeHeaderTaxTaxableAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeHeaderTaxTaxableAmt", {
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
         resolve(data as OnChangeHeaderTaxTaxableAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeHeaderTaxTaxAmt
   Description: Method to call when changing the fixed tax amount on a tax record.  Updates RcvHeadTax
tax amounts based on the new tax amount.
   OperationID: OnChangeHeaderTaxTaxAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeHeaderTaxTaxAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeHeaderTaxTaxAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeHeaderTaxTaxAmt(requestBody:OnChangeHeaderTaxTaxAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeHeaderTaxTaxAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeHeaderTaxTaxAmt", {
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
         resolve(data as OnChangeHeaderTaxTaxAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeHeaderTaxTaxCode
   Description: Method to call when changing the tax code on a RcvHeadTax record.  Validates the tax code and
updates RcvHeadTax tax amounts based on the new tax code.
   OperationID: OnChangeHeaderTaxTaxCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeHeaderTaxTaxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeHeaderTaxTaxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeHeaderTaxTaxCode(requestBody:OnChangeHeaderTaxTaxCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeHeaderTaxTaxCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeHeaderTaxTaxCode", {
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
         resolve(data as OnChangeHeaderTaxTaxCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeHeaderTaxTaxDeductable
   Description: Method to call when changing the tax deductable on a tax record.  Updates RcvHeadTax
tax amounts based on the new tax percent.
   OperationID: OnChangeHeaderTaxTaxDeductable
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeHeaderTaxTaxDeductable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeHeaderTaxTaxDeductable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeHeaderTaxTaxDeductable(requestBody:OnChangeHeaderTaxTaxDeductable_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeHeaderTaxTaxDeductable_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeHeaderTaxTaxDeductable", {
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
         resolve(data as OnChangeHeaderTaxTaxDeductable_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AutoSetToLocation
   Description: This procedure sets RcvDtl.SetToLocation to yes in given data set.
If the receipt line is associated with a PCID then only update if the PCID is EMPTY.
If mass receipts only update if not associated with a PCID regardless of status.
   OperationID: AutoSetToLocation
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AutoSetToLocation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoSetToLocation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AutoSetToLocation(requestBody:AutoSetToLocation_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AutoSetToLocation_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/AutoSetToLocation", {
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
         resolve(data as AutoSetToLocation_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AutoSetToLocationToDflt
   Description: This procedure sets RcvDtl.SetToLocation to yes in given data set.
To be used to set the part location or the default receiving whse
from plant/company depending on the preset SetToLocation flag
If the receipt line is associated with a PCID then only update if the PCID is EMPTY.
If mass receipts only update if not associated with a PCID regardless of status.
   OperationID: AutoSetToLocationToDflt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AutoSetToLocationToDflt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoSetToLocationToDflt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AutoSetToLocationToDflt(requestBody:AutoSetToLocationToDflt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AutoSetToLocationToDflt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/AutoSetToLocationToDflt", {
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
         resolve(data as AutoSetToLocationToDflt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckDtlBeforeUpdate
   Description: This method is to be called right before the update method is called.  If there
is a discrepancy between the vendorqty and ourqty, the user will be asked if they're
sure they want to continue.
   OperationID: CheckDtlBeforeUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckDtlBeforeUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDtlBeforeUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDtlBeforeUpdate(requestBody:CheckDtlBeforeUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckDtlBeforeUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CheckDtlBeforeUpdate", {
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
         resolve(data as CheckDtlBeforeUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckDtlCompliance
   Description: .
   OperationID: CheckDtlCompliance
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckDtlCompliance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDtlCompliance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDtlCompliance(requestBody:CheckDtlCompliance_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckDtlCompliance_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CheckDtlCompliance", {
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
         resolve(data as CheckDtlCompliance_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckDtlJobStatus
   Description: This method is to be run before the GetDtlPOLine and GetDtlPORel and GetDtlJobInfo methods
are called If the Job/PO to a closed or complete job, a question or a warning will be returned
   OperationID: CheckDtlJobStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckDtlJobStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDtlJobStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDtlJobStatus(requestBody:CheckDtlJobStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckDtlJobStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CheckDtlJobStatus", {
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
         resolve(data as CheckDtlJobStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckDtlLotInfo
   Description: This method returns an error or question if the LotNum field does not exist
depending upon the security of the user
   OperationID: CheckDtlLotInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckDtlLotInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDtlLotInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDtlLotInfo(requestBody:CheckDtlLotInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckDtlLotInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CheckDtlLotInfo", {
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
         resolve(data as CheckDtlLotInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckDtlSeqChange
   Description: This method is run when the JobSeq field is changed along with GetSeqInfo.
If the JobMtl is marked as IssuedComplete, the user is asked whether they are sure
they want to change the sequence number.  Only move forward if the answer is yes.
   OperationID: CheckDtlSeqChange
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckDtlSeqChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDtlSeqChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDtlSeqChange(requestBody:CheckDtlSeqChange_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckDtlSeqChange_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CheckDtlSeqChange", {
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
         resolve(data as CheckDtlSeqChange_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckDtlSSN
   Description: This method tests to see if Serial Numbers exist that may be deleted if the
ReceivedTo field or PartNum changes.  The update method assumes the user answered yes
and will delete the Serial Numbers.
   OperationID: CheckDtlSSN
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckDtlSSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDtlSSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDtlSSN(requestBody:CheckDtlSSN_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckDtlSSN_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CheckDtlSSN", {
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
         resolve(data as CheckDtlSSN_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckIssuedComplete
   Description: This method is to be run after the IssuedComplete flag is changed.  Any questions
returned require a yes/no response from the user.
   OperationID: CheckIssuedComplete
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckIssuedComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIssuedComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckIssuedComplete(requestBody:CheckIssuedComplete_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckIssuedComplete_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CheckIssuedComplete", {
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
         resolve(data as CheckIssuedComplete_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckReceivedComplete
   Description: This method is to be run after the ReceivedComplete flag is changed.  Any questions
returned require a yes/no response from the user.
   OperationID: CheckReceivedComplete
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckReceivedComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckReceivedComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckReceivedComplete(requestBody:CheckReceivedComplete_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckReceivedComplete_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CheckReceivedComplete", {
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
         resolve(data as CheckReceivedComplete_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckSupplierPrice
   Description: This method validates that if Supplier Price was change it satisfies Company options.
   OperationID: CheckSupplierPrice
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckSupplierPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSupplierPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckSupplierPrice(requestBody:CheckSupplierPrice_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckSupplierPrice_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CheckSupplierPrice", {
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
         resolve(data as CheckSupplierPrice_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method chkUnReceive
   Description: Checks if the SMI Receipt has been transfered to a standard BIN
   OperationID: chkUnReceive
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/chkUnReceive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/chkUnReceive_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_chkUnReceive(requestBody:chkUnReceive_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<chkUnReceive_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/chkUnReceive", {
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
         resolve(data as chkUnReceive_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreatePartLot
   Description: Purpose: Create a PartLot on the fly
Parameters:  none
Notes:
   OperationID: CreatePartLot
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreatePartLot_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreatePartLot_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreatePartLot(requestBody:CreatePartLot_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreatePartLot_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/CreatePartLot", {
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
         resolve(data as CreatePartLot_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDtlAssemblyInfo
   Description: This method updates the dataset when the AssemblySeq number changes
   OperationID: GetDtlAssemblyInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDtlAssemblyInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlAssemblyInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDtlAssemblyInfo(requestBody:GetDtlAssemblyInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDtlAssemblyInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetDtlAssemblyInfo", {
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
         resolve(data as GetDtlAssemblyInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDtlJobInfo
   Description: This method default the  Job Information when the RcvDtl.JobNum field changes
   OperationID: GetDtlJobInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDtlJobInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlJobInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDtlJobInfo(requestBody:GetDtlJobInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDtlJobInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetDtlJobInfo", {
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
         resolve(data as GetDtlJobInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDtlLotInfo
   Description: This method updates the unitCost when the LotNum field changes
   OperationID: GetDtlLotInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDtlLotInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlLotInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDtlLotInfo(requestBody:GetDtlLotInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDtlLotInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetDtlLotInfo", {
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
         resolve(data as GetDtlLotInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDtlPartInfo
   Description: This method updates the dataset when the part number has changed.
CheckDtlSSN should be run first.
   OperationID: GetDtlPartInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDtlPartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlPartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDtlPartInfo(requestBody:GetDtlPartInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDtlPartInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetDtlPartInfo", {
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
         resolve(data as GetDtlPartInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDtlPOInfo
   Description: This method updates the dataset when the detail Line PONum field has changed.
   OperationID: GetDtlPOInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDtlPOInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlPOInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDtlPOInfo(requestBody:GetDtlPOInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDtlPOInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetDtlPOInfo", {
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
         resolve(data as GetDtlPOInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDtlPOLineInfo
   Description: This method updates the dataset when the detail Line POLine field has changed.
   OperationID: GetDtlPOLineInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDtlPOLineInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlPOLineInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDtlPOLineInfo(requestBody:GetDtlPOLineInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDtlPOLineInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetDtlPOLineInfo", {
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
         resolve(data as GetDtlPOLineInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDtlPORelInfo
   Description: This method updates the dataset when the detail Line PORelNum field has changed.
   OperationID: GetDtlPORelInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDtlPORelInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlPORelInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDtlPORelInfo(requestBody:GetDtlPORelInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDtlPORelInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetDtlPORelInfo", {
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
         resolve(data as GetDtlPORelInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDtlQtyInfo
   Description: This method updates the dataset when the InputOurQty field changes
   OperationID: GetDtlQtyInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDtlQtyInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlQtyInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDtlQtyInfo(requestBody:GetDtlQtyInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDtlQtyInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetDtlQtyInfo", {
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
         resolve(data as GetDtlQtyInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateOurQtyFromAttributes
   Description: This method gets total and sets OurQty when the InputOurQty field changes
   OperationID: UpdateOurQtyFromAttributes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateOurQtyFromAttributes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateOurQtyFromAttributes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateOurQtyFromAttributes(requestBody:UpdateOurQtyFromAttributes_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateOurQtyFromAttributes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/UpdateOurQtyFromAttributes", {
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
         resolve(data as UpdateOurQtyFromAttributes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDtlRcvdToInfo
   Description: This method is run when the ReceivedTo field is changed after the CheckSSN method is called
   OperationID: GetDtlRcvdToInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDtlRcvdToInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlRcvdToInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDtlRcvdToInfo(requestBody:GetDtlRcvdToInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDtlRcvdToInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetDtlRcvdToInfo", {
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
         resolve(data as GetDtlRcvdToInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDtlSeqInfo
   Description: This method updates the dataset when the JobSeq field changes.  Fields will be defaulted
from JobMtl for PUR-MTL and from JobOper for PUR-SUB.
   OperationID: GetDtlSeqInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDtlSeqInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlSeqInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDtlSeqInfo(requestBody:GetDtlSeqInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDtlSeqInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetDtlSeqInfo", {
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
         resolve(data as GetDtlSeqInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDtlVenQtyInfo
   Description: This method updates the dataset when the VendorQty field changes
   OperationID: GetDtlVenQtyInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDtlVenQtyInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlVenQtyInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDtlVenQtyInfo(requestBody:GetDtlVenQtyInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDtlVenQtyInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetDtlVenQtyInfo", {
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
         resolve(data as GetDtlVenQtyInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLotImportInfo
   Description: This method should be called from Container Receipt Entry and Receipt Entry when the
ImportNumber or ImportedFromDesc values have changed for a receipt line.
   OperationID: GetLotImportInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLotImportInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLotImportInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLotImportInfo(requestBody:GetLotImportInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLotImportInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetLotImportInfo", {
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
         resolve(data as GetLotImportInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRcvDtlMisc
   Description: This method creates a new Miscellaneous receipt line entry
   OperationID: GetNewRcvDtlMisc
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRcvDtlMisc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvDtlMisc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRcvDtlMisc(requestBody:GetNewRcvDtlMisc_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRcvDtlMisc_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetNewRcvDtlMisc", {
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
         resolve(data as GetNewRcvDtlMisc_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPartXRefInfo
   Description: This method will review if the entered part exists in any other PartXRef table.
CheckDtlSSN should be run first.
   OperationID: GetPartXRefInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartXRefInfo(requestBody:GetPartXRefInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPartXRefInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetPartXRefInfo", {
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
         resolve(data as GetPartXRefInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DisplayWarnMsg
   OperationID: DisplayWarnMsg
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DisplayWarnMsg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DisplayWarnMsg_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DisplayWarnMsg(requestBody:DisplayWarnMsg_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DisplayWarnMsg_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/DisplayWarnMsg", {
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
         resolve(data as DisplayWarnMsg_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LCChangeLCAmt
   Description: This method updates the dataset record when the LCAmt field changes
   OperationID: LCChangeLCAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LCChangeLCAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LCChangeLCAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LCChangeLCAmt(requestBody:LCChangeLCAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LCChangeLCAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/LCChangeLCAmt", {
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
         resolve(data as LCChangeLCAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedDtlPOTransValue
   Description: This method should be invoked when the POTransValue of RcvDtl has changed.
   OperationID: OnChangedDtlPOTransValue
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangedDtlPOTransValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedDtlPOTransValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedDtlPOTransValue(requestBody:OnChangedDtlPOTransValue_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangedDtlPOTransValue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangedDtlPOTransValue", {
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
         resolve(data as OnChangedDtlPOTransValue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDtlBinNum
   Description: This method should be invoked when the BinNum on the receipt line changes
If the receipt line is associated with a planning contract it will validate if the Bin against the planning contract header.
   OperationID: OnChangeDtlBinNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDtlBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDtlBinNum(requestBody:OnChangeDtlBinNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDtlBinNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeDtlBinNum", {
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
         resolve(data as OnChangeDtlBinNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDtlCommodity
   Description: This method should be invoked when the CommodityCode in RcvDtl changes.
This method will validate the commodity code and get defaults.
   OperationID: OnChangeDtlCommodity
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDtlCommodity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlCommodity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDtlCommodity(requestBody:OnChangeDtlCommodity_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDtlCommodity_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeDtlCommodity", {
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
         resolve(data as OnChangeDtlCommodity_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDtlCountryNum
   Description: This method should be invoked when the OrigCountryNum in RcvDtl changes.
This method will validate country of origin.
   OperationID: OnChangeDtlCountryNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDtlCountryNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlCountryNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDtlCountryNum(requestBody:OnChangeDtlCountryNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDtlCountryNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeDtlCountryNum", {
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
         resolve(data as OnChangeDtlCountryNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDtlLCIndCost
   Description: This method should be invoked when the LCIndCost in RcvDtl changes.
This method will validate the manually disbursed indirect cost.
   OperationID: OnChangeDtlLCIndCost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDtlLCIndCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlLCIndCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDtlLCIndCost(requestBody:OnChangeDtlLCIndCost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDtlLCIndCost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeDtlLCIndCost", {
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
         resolve(data as OnChangeDtlLCIndCost_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRcvDtlLCIndCost
   Description: Get sum of LCIndCost value for RcvDtl rows
   OperationID: GetRcvDtlLCIndCost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRcvDtlLCIndCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRcvDtlLCIndCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRcvDtlLCIndCost(requestBody:GetRcvDtlLCIndCost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRcvDtlLCIndCost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/GetRcvDtlLCIndCost", {
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
         resolve(data as GetRcvDtlLCIndCost_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDtlPCID
   Description: This method should be invoked when the Receipt line PCID has changed and it will validate if it exists on the Inventory (EMPTY / STOCK) or
Staged (EMPTY / ARRIVED) PCID tables. If the PCID is not EMPTY and it is situated in a different location to that of the receipt line it will change the
warehouse / bin on the receipt line to match that of the PCID Header.
   OperationID: OnChangeDtlPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDtlPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDtlPCID(requestBody:OnChangeDtlPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDtlPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeDtlPCID", {
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
         resolve(data as OnChangeDtlPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDtlPOSelected
   Description: This method is called when a PO has been selected on Mass Receipt process.
Returns an Exception or a Warning if the PO is not approved/confirmed, depending on Company Config.
   OperationID: OnChangeDtlPOSelected
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDtlPOSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlPOSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDtlPOSelected(requestBody:OnChangeDtlPOSelected_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDtlPOSelected_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeDtlPOSelected", {
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
         resolve(data as OnChangeDtlPOSelected_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDtlSelectedSinglePO
   Description: This method is called when a PO has been selected on Mass Receipt process. This method checks a single PO
and does not send the ReceiptTableset for better performance.
Returns an Exception or a Warning if the PO is not approved/confirmed, depending on Company Config.
   OperationID: OnChangeDtlSelectedSinglePO
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDtlSelectedSinglePO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlSelectedSinglePO_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDtlSelectedSinglePO(requestBody:OnChangeDtlSelectedSinglePO_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDtlSelectedSinglePO_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeDtlSelectedSinglePO", {
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
         resolve(data as OnChangeDtlSelectedSinglePO_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDtlReceived
   Description: This method should be invoked when the Received flag in RcvDtl has changed.
   OperationID: OnChangeDtlReceived
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDtlReceived_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlReceived_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDtlReceived(requestBody:OnChangeDtlReceived_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDtlReceived_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeDtlReceived", {
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
         resolve(data as OnChangeDtlReceived_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDtlReceiptType
   Description: This method should be invoked when the Receipt Type in RcvDtl has changed.
   OperationID: OnChangeDtlReceiptType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDtlReceiptType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlReceiptType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDtlReceiptType(requestBody:OnChangeDtlReceiptType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDtlReceiptType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeDtlReceiptType", {
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
         resolve(data as OnChangeDtlReceiptType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDtlReceiptTypeTranType
   Description: /// This method should be invoked when the Receipt Type or TranType in RcvDtl has changed. This will reset all fields.
   OperationID: OnChangeDtlReceiptTypeTranType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDtlReceiptTypeTranType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlReceiptTypeTranType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDtlReceiptTypeTranType(requestBody:OnChangeDtlReceiptTypeTranType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDtlReceiptTypeTranType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeDtlReceiptTypeTranType", {
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
         resolve(data as OnChangeDtlReceiptTypeTranType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDtlSupplierPrice
   Description: This method should be invoked when the Supplier Price in RcvDtl changes.
This method calculates Base and Reporting values.
   OperationID: OnChangeDtlSupplierPrice
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDtlSupplierPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlSupplierPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDtlSupplierPrice(requestBody:OnChangeDtlSupplierPrice_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDtlSupplierPrice_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeDtlSupplierPrice", {
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
         resolve(data as OnChangeDtlSupplierPrice_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDtlTaxCatID
   Description: This method should be invoked when TaxCatID changes and is used to set the Taxable flag
   OperationID: OnChangeDtlTaxCatID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDtlTaxCatID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlTaxCatID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDtlTaxCatID(requestBody:OnChangeDtlTaxCatID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDtlTaxCatID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeDtlTaxCatID", {
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
         resolve(data as OnChangeDtlTaxCatID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDtlTaxExempt
   Description: This method should be invoked when TaxExempt changes and is used to set the Taxable flag
   OperationID: OnChangeDtlTaxExempt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDtlTaxExempt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlTaxExempt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDtlTaxExempt(requestBody:OnChangeDtlTaxExempt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDtlTaxExempt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeDtlTaxExempt", {
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
         resolve(data as OnChangeDtlTaxExempt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDtlUpliftPercent
   Description: This method should be invoked when the UpliftPercent in RcvDtl changes.
This method will validate the UpliftPercent and calculate the Uplift Indirect Cost.
   OperationID: OnChangeDtlUpliftPercent
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDtlUpliftPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlUpliftPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDtlUpliftPercent(requestBody:OnChangeDtlUpliftPercent_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDtlUpliftPercent_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeDtlUpliftPercent", {
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
         resolve(data as OnChangeDtlUpliftPercent_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeReceiptDate
   Description: This method should be invoked when the Receipt Date on the header or on the lines changes.
If the receipt date is from header, it must receive as parameter partNum = "" and poLine = 0, otherwise you must receive the correct values.
In this method you can identify the lines where the receipt date can be changed or not.
   OperationID: OnChangeReceiptDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeReceiptDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeReceiptDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeReceiptDate(requestBody:OnChangeReceiptDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeReceiptDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeReceiptDate", {
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
         resolve(data as OnChangeReceiptDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDtlWareHouseCode
   Description: This method should be invoked when the Warehouse on the receipt line changes.
If the receipt line is associated with a planning contract it will validate that the warehouse matches that of a contract and will prompt the user to confirm.
If the receipt line contains serial numbers it will check if the warehouse supports full tracking and if not will warn the user that it will delete the serial numbers.
   OperationID: OnChangeDtlWareHouseCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDtlWareHouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlWareHouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDtlWareHouseCode(requestBody:OnChangeDtlWareHouseCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDtlWareHouseCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeDtlWareHouseCode", {
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
         resolve(data as OnChangeDtlWareHouseCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeInspReq
   Description: This method updates the dataset when the Inspection Required flag changes
   OperationID: OnChangeInspReq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeInspReq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInspReq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeInspReq(requestBody:OnChangeInspReq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeInspReq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/OnChangeInspReq", {
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
         resolve(data as OnChangeInspReq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RcvDtlNegInvCheck
   Description: Called to check for negative inventory on RcvDtl before delete or unreceive
   OperationID: RcvDtlNegInvCheck
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RcvDtlNegInvCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RcvDtlNegInvCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RcvDtlNegInvCheck(requestBody:RcvDtlNegInvCheck_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RcvDtlNegInvCheck_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlNegInvCheck", {
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
         resolve(data as RcvDtlNegInvCheck_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetToLocation
   Description: This method gets the Warehouse and Bin to the defaults for the Part/Job
   OperationID: SetToLocation
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetToLocation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetToLocation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetToLocation(requestBody:SetToLocation_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetToLocation_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SetToLocation", {
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
         resolve(data as SetToLocation_output)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumGenOptsRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PendingRcvDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PendingRcvDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RcvDtlAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlAttrValueSetRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RcvDtlAttrValueSetRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RcvDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlTaxRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RcvDtlTaxRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDutyRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RcvDutyRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvHeadAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RcvHeadAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RcvHeadListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RcvHeadRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvHeadTaxRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RcvHeadTaxRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvMiscRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RcvMiscRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvMiscTaxRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RcvMiscTaxRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SNFormatRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SelectedSerialNumbersRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SupplierXRefRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SupplierXRefRow,
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

export interface Erp_Tablesets_PendingRcvDtlRow{
   "Company":string,
   "VendorNum":number,
   "PurPoint":string,
   "PackSlip":string,
   "PONum":number,
   "POLine":number,
   "PORel":number,
   "PartNum":string,
   "LineDesc":string,
   "OurQuantity":number,
   "UOM":string,
   "JobNum":string,
   "Type":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RcvDtlAttchRow{
   "Company":string,
   "VendorNum":number,
   "PurPoint":string,
   "PackSlip":string,
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

export interface Erp_Tablesets_RcvDtlAttrValueSetRow{
      /**  Company Indentifier.  */  
   "Company":string,
      /**  The internal key that is used to tie back to the Supplier master file.  */  
   "VendorNum":number,
      /**  The Supplier purchase point ID.  */  
   "PurPoint":string,
      /**  Supplier Packing Slip #.  */  
   "PackSlip":string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  */  
   "PackLine":number,
      /**  Unique identifier for this Attribute Value for this receipt detail.  */  
   "AttributeValueSeq":number,
      /**  Dynamic Attribute Value Set ID for this receipt detail.  */  
   "AttributeSetID":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  Unit of Measure.  */  
   "IUM":string,
      /**  Receipt quantity in our unit of measure for this attribute set.  */  
   "OurQty":number,
      /**  Indicates whether the Attribute Value was auto-generated by the system.  */  
   "AutoGenerated":boolean,
      /**  Supplier selling Unit of Measure.  */  
   "PUM":string,
      /**  Quantity received against a purchase order in the Supplier unit of measure.  */  
   "VendorQty":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Unit of measure for the NumberOfPieces.  */  
   "NumberOfPiecesUOM":string,
      /**  Indicates if the receipt is pending inspection.  Set to Yes  if InspectionReq = Yes. Set to No after receipt has been inspected.  */  
   "InspectionPending":boolean,
      /**  Indicates if this receipt will be categorized as requiring inspection. It is set to Yes if any of the related Vendor, PartClass, PoDetail, JobMtl, JobOper have their RcvInspectionReq field = Yes.  */  
   "InspectionReq":boolean,
      /**  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  */  
   "InspectorID":string,
      /**  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  */  
   "InspectedBy":string,
      /**  Date when item was inspected.  */  
   "InspectedDate":string,
      /**  Time of day when inspection transaction was recorded.  */  
   "InspectedTime":number,
      /**  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  */  
   "PassedQty":number,
      /**  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  */  
   "FailedQty":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RcvDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  The Vendors purchase point ID.  */  
   "PurPoint":string,
      /**  Vendors Packing Slip #.  */  
   "PackSlip":string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  */  
   "PackLine":number,
      /**   A\P invoice entry sets this to "Yes" when the receipt detail line is invoiced.  A value of NO either means that the system was not configured to 'Save Receipts for Invoicing" when the receipt line was created or that it has not yet been invoiced via A/P.
(See RcvHead.SaveForInvoicing, RcvHead.Invoiced)  */  
   "Invoiced":boolean,
      /**  Invoice Number on which this receipt detail was invoiced. This is updated from the A\P invoice entry process.  */  
   "InvoiceNum":string,
      /**  The invoice line on which this receipt detail was invoiced. Updated by the A\P invoice entry process.  */  
   "InvoiceLine":number,
      /**  Our Part Number of the item that has been received. Captured from the related PODetail.PartNum for receipts of PO item. Entered by the user for miscellaneous receipts in which case it can't be blank. It must be valid in the Part file for receipt to stock.  */  
   "PartNum":string,
      /**  Warehouse ID that received the item.  Only applicable for receipt to stock. Must be valid in the PartWhse file.  */  
   "WareHouseCode":string,
      /**  Identifies the Bin location of the warehouse which received the item. Only applicable for a receipt of Stock.  */  
   "BinNum":string,
      /**  Receipt quantity in our unit of measure.  */  
   "OurQty":number,
      /**  Unit of Measure.  */  
   "IUM":string,
      /**  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  */  
   "OurUnitCost":number,
      /**  Job Number that received the item. Only applicable for receipt to Job.  */  
   "JobNum":string,
      /**  Job Assembly Sequence # that the receipt was made against. Only applicable for receipt to job.  */  
   "AssemblySeq":number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "S" = SubContract Operation (JobOper).  */  
   "JobSeqType":string,
      /**  Seq # of specific material or subcontract operation record to which this receipt was made against. Only applicable for a receipt to job.  */  
   "JobSeq":number,
      /**  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  */  
   "PONum":number,
      /**  The PO line # which is being received. Only applicable for PO receipt transactions.  */  
   "POLine":number,
      /**  Purchase Order Release # which is being received.  */  
   "PORelNum":number,
      /**  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  */  
   "TranReference":string,
      /**  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   "PartDescription":string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  */  
   "RevisionNum":string,
      /**  Quantity received against a purchase order in the vendors unit of measure.  */  
   "VendorQty":number,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  */  
   "VendorUnitCost":number,
      /**  An internal flag which indicates if this is a receipt of a Purchase Order (P) or Miscellaneous (M) item. If "P" then this record is related to a PORel record. If "M" there is no PO reference. the transaction.  */  
   "ReceiptType":string,
      /**  Indicates where the item is received to. Items can be received to a Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN")  */  
   "ReceivedTo":string,
      /**   Indicates if this receipt transaction should flag the related purchase order release (PORel) as being received complete (PORel.OpenRelease = No).  When the user toggles this field   Receipt entry considers it  a direct update to the PORel.OpenRelease flag.  What we mean is that the user can change the PORel.OpenRelease flag by maintaining this field on  ANY related receipt transaction for the PORel. Therefore this field should not be used to determine the true status of the PORel record.
Receipt Entry allows displays this field based on the current setting of PORel.OpenRelease field. Another point is that if the a receipt transaction is update to a different PO/Line/Release the original PORel will be reopened if there are no other receipt detail records that indicate the release is closed.  All this Open/Close logic occurs in the write trigger of RcvDtl.  */  
   "ReceivedComplete":boolean,
      /**   Indicates if this receipt transaction should flag the related job material/subcontract as being issued complete. (JobMtl.IssuedComplete/JobOper.OpComplete)   When the user toggles this field Receipt entry considers it  a direct update to the job record.  What we mean is that the user can change the status of the job record by maintaining this field on  ANY related receipt transaction. Therefore this field should not be used to determine the true status of the JobMtl/JobOper record.
Receipt Entry allows displays this field based on the current status of JobMtl/JobOper field. Another point is that if the a receipt transaction is update to a different job record, the original Job record will be reopened if there are no other receipt detail records that indicate that it is complete.  All this Open/Close logic occurs in the write trigger of RcvDtl.  */  
   "IssuedComplete":boolean,
      /**  Vendor's selling Unit of Measure.  */  
   "PUM":string,
      /**  Vendor's Part Number. Defaulted from PODetail.  */  
   "VenPartNum":string,
      /**  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  */  
   "CostPerCode":string,
      /**  Lot Number  */  
   "LotNum":string,
      /**  Number of labels  */  
   "NumLabels":number,
      /**  Unique dimension code for the part.  */  
   "DimCode":string,
      /**  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  */  
   "DUM":string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   "DimConvFactor":number,
      /**  Indicates if this receipt will be categorized as requiring inspection. It is set to Yes if any of the related Vendor, PartClass, PoDetail, JobMtl, JobOper have their RcvInspectionReq field = Yes.  */  
   "InspectionReq":boolean,
      /**   Indicates if the receipt is pending inspection.
Set to Yes  if InspectionReq = Yes. Set to No after receipt has been inspected.  */  
   "InspectionPending":boolean,
      /**  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  */  
   "InspectorID":string,
      /**  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  */  
   "InspectedBy":string,
      /**  Date when item was inspected.  */  
   "InspectedDate":string,
      /**   Time of day when inspection transaction was recorded.
(seconds since midnight format)  */  
   "InspectedTime":number,
      /**  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  */  
   "PassedQty":number,
      /**  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  */  
   "FailedQty":number,
      /**  Receipt date. Mirror image of related RCVHead.ReceiptDate.  Maintained by the RcvHead/RcvDtl write triggers.  */  
   "ReceiptDate":string,
      /**  DMRs use Reason type "D".  Only used if failing quantity from inspection.  */  
   "ReasonCode":string,
      /**  Total Purchase Price Variance amount placed on a receipt in inspection when the variance is received.  Only set if the receipt is currently in inspection (not moved to DMR, job, or stock).  */  
   "TotCostVariance":number,
      /**  Weight  */  
   "Weight":number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   "WeightUOM":string,
      /**  Indicates if the transaction is a non-conformance type transaction.  */  
   "NonConformnce":boolean,
      /**  The material burden rate for this part.  */  
   "MtlBurRate":number,
      /**   Mtl Bur Unit cost base on our unit of measure. The mtl burden rate
defaults from the Part file.  */  
   "OurMtlBurUnitCost":number,
      /**  Link to the related GLRefTyp.RefType. Not displayed.  */  
   "RefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "RefCode":string,
      /**  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  */  
   "PurchCode":string,
      /**  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  */  
   "LCFlag":boolean,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   "GlbVendorNum":number,
      /**  Global Purchase Point identifier.  Used in Consolidated Purchasing.  */  
   "GlbPurPoint":string,
      /**  Global Packing Slip identifier.  Used in Consolidated Purchasing.  */  
   "GlbPackSlip":string,
      /**  Global Packing Slip Line identifier.  Used in Consolidated Purchasing.  */  
   "GlbPackLine":number,
      /**  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  */  
   "DocUnitCost":number,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   "ContainerID":number,
      /**  Container volume, frequently specified in cubic sq feet.  */  
   "Volume":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitCost":number,
      /**  Order Num related to the purchase order that is being received. Used only for Buy To Order POs.  */  
   "OrderNum":number,
      /**  The line number of the sales order related to the purchase order that is being received. Used only for Buy To Order POs.  */  
   "OrderLine":number,
      /**  The release number of the sales order line related to the purchase order that is being received. Used only for Buy To Order POs.  */  
   "OrderRelNum":number,
      /**  Country Number of the Origin Country (defaults from Part Country of Origin).  */  
   "OrigCountryNum":number,
      /**  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  */  
   "UpliftPercent":number,
      /**  Duty Amount portion of the landed cost for this receipt line.  */  
   "LCDutyAmt":number,
      /**  Indirect Cost portion of the landed cost for this receipt line.  */  
   "LCIndCost":number,
      /**  This is by default the PO line value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  */  
   "POTransValue":number,
      /**  This is the PO Base Transaction Value plus all indirect costs which are marked to include as transaction value costs.  */  
   "ExtTransValue":number,
      /**  Flag to indicate that the receipt line has been received.  */  
   "Received":boolean,
      /**  Harmonized System (HS) goods classification code.  */  
   "CommodityCode":string,
      /**  Identifier of associated PO ('Std', 'CMI', 'SMI')  */  
   "POType":string,
      /**  Flag representing whether or not this receipt was auto generated by the consumption process (GenSMIReceipt.p).  This is only pertinent for SMI type PO Receipts.  */  
   "AutoReceipt":boolean,
      /**   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  if Part.NetVolumeUOM is not known.  */  
   "VolumeUOM":string,
      /**  The date the shipment detail arrived. Defaults as current system date.  */  
   "ArrivedDate":string,
      /**  This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "LCSpecLineDutyAmt":number,
      /**  The total Landed Cost Amount applied for this receipt line.  This is the actual cost that will determine the MtlBurUnitCost of the receipt transaction.  */  
   "AppliedRcptLCAmt":number,
      /**  The total Uplift Indirect Cost Amount of the receipt line. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "LCUpliftIndCost":number,
      /**  The total amount of disbursed landed cost for this receipt detail.  This amount includes the duties and indirect costs per receipt line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "LCAmt":number,
      /**  This field holds the applied variance amount for the landed costs.  */  
   "AppliedLCVariance":number,
      /**  Landed Cost calculated Mtl Bur Unit Cost based on our unit of measure.  The value of this field is copied to the OurMtlBurUnitCost when the Landed Cost is disbursed and applied to the receipt line.  */  
   "LCMtlBurUnitCost":number,
      /**  PO currency value of this field  */  
   "DocVendorUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt1VendorUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2VendorUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3VendorUnitCost":number,
      /**  Indicates if the item on the line is not compliant on its destination, that can be Inventory, Job Material, Job Subcontract, Sales Order.  */  
   "NotCompliant":boolean,
      /**  Displays the cause why the item is not compliant.  */  
   "ComplianceMsg":string,
      /**  This is the customer number associated with the managed customer defined in the whsebin for CMI type PO transactions.  Originally defaults from PORel.MangCustNum.  */  
   "MangCustNum":number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegNumCnfg.  */  
   "LegalNumber":string,
      /**  Relation between this RcvDtl and the ShipHead.PackNum where this Intercompany Shipment originated.  */  
   "ICPackNum":number,
      /**  Shipment Received  */  
   "ShipRcv":string,
      /**  Stores the number of the import document.  Can be different from value on header.  */  
   "ImportNum":string,
      /**  Stores the Country from which the document is imported.  Can be different from value on header.  */  
   "ImportedFrom":number,
      /**  Location description from which the document is imported.  Can be different from Header value.  */  
   "ImportedFromDesc":string,
      /**  Gross Weight  */  
   "GrossWeight":number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t.  */  
   "GrossWeightUOM":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  It indicates the option of what type of quantity will be able to be changed in the POLine. The actual options are "Our" and "Supplier"  */  
   "QtyOption":string,
      /**  When True, the Supplier Quantity field is entered directly instead of being calculated from Our Quantity with a UOM conversion  */  
   "ConvOverride":boolean,
      /**  ContractID  */  
   "ContractID":string,
      /**  Used to identify what has been consumed during an SMI Receipt for a particular transaction.  */  
   "SMITransNum":number,
      /**  PCID  */  
   "PCID":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  Delivered  */  
   "Delivered":boolean,
      /**  DeliveredComments  */  
   "DeliveredComments":string,
      /**  Internal usage for inclusive taxes - Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  */  
   "InOurCost":number,
      /**  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  */  
   "DocInUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InUnitCost":number,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  */  
   "InVendorUnitCost":number,
      /**  PO currency value of this field  */  
   "DocInVendorUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InVendorUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InVendorUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InVendorUnitCost":number,
      /**  Value that indicates the remaining quantity of the receipt that is waiting to be invoiced.  */  
   "SupplierUnInvcReceiptQty":number,
      /**  Value that indicates the un-invoiced quantity of the receipt.  */  
   "OurUnInvcReceiptQty":number,
      /**  ** NOT USED TO BE DROPPED 10.2 ** The Tax Liability for this Receipt line  */  
   "TaxRegionCode":string,
      /**  Indicates the Tax Category for this Receipt line. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  */  
   "TaxCatID":string,
      /**  Indicates if the Receipt line is Taxable  */  
   "Taxable":boolean,
      /**  Indicates if this item is exempt from tax for this receipt line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the tax info.  */  
   "TaxExempt":string,
      /**  This flag determines whether any manual taxes were created for a receipt line, if this is set to True the tax engine will not calculate any receipt detail line tax information  */  
   "NoTaxRecalc":boolean,
      /**  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  */  
   "InAppliedLCVariance":number,
      /**  Internal usage for inclusive taxes - The total Landed Cost Amount applied for this receipt line.  This is the actual cost that will determine the MtlBurUnitCost of the receipt transaction.  */  
   "InAppliedRcptLCAmt":number,
      /**  Internal usage for inclusive taxes - The total amount of disbursed landed cost for this receipt detail.  This amount includes the duties and indirect costs per receipt line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "InLCAmt":number,
      /**  Internal usage for inclusive taxes - Duty Amount portion of the landed cost for this receipt line.  */  
   "InLCDutyAmt":number,
      /**  Internal usage for inclusive taxes - Indirect Cost portion of the landed cost for this receipt line.  */  
   "InLCIndCost":number,
      /**  Internal usage for inclusive taxes - Landed Cost calculated Mtl Bur Unit Cost based on our unit of measure.  The value of this field is copied to the OurMtlBurUnitCost when the Landed Cost is disbursed and applied to the receipt line.  */  
   "InLCMtlBurUnitCost":number,
      /**  Internal usage for inclusive taxes - This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "InLCSpecLineDutyAmt":number,
      /**  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the receipt line. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "InLCUpliftIndCost":number,
      /**  Internal usage for inclusive taxes - This is by default the PO line value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  */  
   "InPOTransValue":number,
      /**  ProjProcessed  */  
   "ProjProcessed":boolean,
      /**  This will contain the non deductable tax portion for this Receipt line.  This will be calculated based on the Receipt Header or Receipt Line tax records depending on the Tax Liability type and Company Tax Configuration.  */  
   "ExtNonRecoverableCost":number,
      /**  Related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  AttributeBackoutRequired  */  
   "AttributeBackoutRequired":boolean,
      /**  CNDeclarationBillLine  */  
   "CNDeclarationBillLine":number,
      /**  Flag to indicate if landed cost info can be updated.  */  
   "AllowLCUpdate":boolean,
   "AsmPartDescription":string,
      /**  Consolidated PO flag.  Used in Consolidated Purchasing.  */  
   "ConsolidatedPO":boolean,
      /**  This is the extended cost of the container detail item this RcvDtl entry is tied to.  */  
   "ContainerExtCost":number,
      /**  Container Detail Landed Cost Amount  */  
   "ContainerLCAmt":number,
   "ContractOrder":boolean,
      /**  Interger value of CostPerCode  */  
   "CostPerFactor":number,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
      /**  Flag to set disable/enable the InspectionReq field.  */  
   "DisableInspection":boolean,
      /**  Indicates whether the IUM or DUM field should be displayed/enabled  */  
   "DisplayUMField":string,
      /**  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  */  
   "DocScrUnitCost":number,
      /**  PO currency value of this field  */  
   "DocScrVendorUnitCost":number,
      /**  DropShipment  */  
   "DropShipment":boolean,
      /**  PORel.DueDate  */  
   "DueDate":string,
   "EnableBin":boolean,
      /**  Indicates whether to enable/disable the dimension fields  */  
   "EnableDim":boolean,
      /**  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  */  
   "EnableInventoryAttributes":boolean,
   "EnableLot":boolean,
      /**  Internal flag used for the row rules to control whether the PCID columns should be enabled or not.  */  
   "EnablePCID":boolean,
      /**  Indicates whether to Enable the Serial Number button  */  
   "EnableSN":boolean,
      /**  Use this field to enable\disable the Supplier Part XRef button  */  
   "EnableSupplierXRef":boolean,
      /**  Flag to indicate if PO Trans Value can be updated.  */  
   "EnableTransValue":boolean,
      /**  Flag to indicate if UpliftPercent can be updated.  */  
   "EnableUplift":boolean,
   "EnableWhse":boolean,
      /**  Extended receipt detail cost.  */  
   "ExtCost":number,
      /**  This is true when using the Receive To PCID option in HH PO Receipt.  */  
   "HHReceiveToPCID":boolean,
      /**  OurQty not divided by dimension conversion factor for entry.  */  
   "InputOurQty":number,
      /**  Flag used to switch other Received To's to Pur-Ins  */  
   "InspectionFlag":boolean,
      /**  Link to the IMRcvDtl table  */  
   "IntQueID":number,
   "JobIUM":string,
   "JobPartNum":string,
   "JobRequiredQty":number,
   "LegalNumberMessage":string,
   "MangCustID":string,
   "MangCustName":string,
      /**  Flag to indicate if LCIdCost can be manually updated.  */  
   "ManualLC":boolean,
      /**  Indicates if created through Mass Receipts  */  
   "MassReceipt":boolean,
   "OnTime":string,
   "OpenRelease":boolean,
   "OrderQty":number,
      /**  Our Remaining Quantity  */  
   "OurRemQty":number,
      /**  Linked to the outbound container flag taken from either the PkgControlStageHeader / PkgControlHeader.  */  
   "PCIDOutboundContainer":boolean,
      /**  Package Control Header Status  */  
   "PkgControlStatus":string,
      /**  The Plant to which the warehouse belongs to  */  
   "Plant":string,
   "POComment":string,
      /**  PO Line Due Date  */  
   "PODueDate":string,
   "POFactor":number,
   "POFactorDirection":string,
   "POHold":boolean,
   "POIUM":string,
   "POPUM":string,
      /**  The total quantity that has arrived for this purchase order release.  */  
   "PORelArrivedQty":number,
      /**  Indicates the current status of the release. This field is maintained by the System automatically. The possible values are: Open (O), Arrived (A), Inspection (I), Received (R), Closed (C), Voided (V).  */  
   "PORelStatus":string,
   "RcvdSMIQty":number,
      /**  PORel Received Qty for MassReceipts  */  
   "ReceivedQty":number,
   "RemainingSMIQty":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ScrUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ScrVendorUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ScrUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ScrVendorUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ScrUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ScrVendorUnitCost":number,
      /**  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  */  
   "ScrOurUnitCost":number,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine  */  
   "ScrVendorUnitCost":number,
   "SearchPONum":number,
   "Selected":boolean,
      /**  This boolean is set by the user in Receipt Entry to initiate the SetToLocation logic for this line.  */  
   "SetToLocation":boolean,
      /**  When this flag is true, skip the Material Queue creation logic for the current RcvDtl line.  */  
   "SkipMaterialQueueCreation":boolean,
   "SMIComplete":boolean,
   "SNStusChanged":boolean,
      /**  MtlSeq used in PrintTag option  */  
   "TagMtlSeq":number,
      /**  Operation Sequence used in PrintTag  */  
   "TagOprSeq":number,
   "ThisTranQty":number,
   "ThisTranUOM":string,
      /**  Total amount.  This is the sum of all the other total fields.  */  
   "TotalAmt":number,
      /**  Total dedicated Tax amount.  */  
   "TotDedTaxAmt":number,
      /**  Total duties amount.  This is the sum of RcvDtl.LCSpecLineDutyAmt + RcvDtl.LCDutyAmt  */  
   "TotDutiesAmt":number,
      /**  Receipt line amount using vendor unit cost.  */  
   "TotLineAmt":number,
      /**  Total Self Assessed Tax amount  */  
   "TotSATaxAmt":number,
      /**  Total tax amount.  This is the sum of RcvHeadTax.TaxAmt  */  
   "TotTaxAmt":number,
      /**  Total WithHolding Tax amount  */  
   "TotWHTaxAmt":number,
      /**   Indicates what the item is being purchased for.  Items can be purchased for Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN").
FYI: This field indirectly sets the JobSeqType field via the write trigger. It can itself be set from the JobSeqType. System keeps them compatible. JobSeqType/TranType values are; M =PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN.  */  
   "TranType":string,
   "UsePurchaseCode":boolean,
   "VendorCurrSymbol":string,
   "VenRemQty":number,
      /**  It is true, if RcvDtl.ReceipteType = 'P' and XbSyst.AllowUpdSuppPrice is true.  */  
   "AllowUpdSuppPrice":boolean,
      /**  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity.  */  
   "AttributeQtyMismatch":boolean,
      /**  Indicates if the status of the PCID has changed since the receipt took place.  */  
   "PCIDStatusChanged":boolean,
   "CNDeclarationBill":string,
   "SerialNoAttributeSetID":number,
   "BitFlag":number,
   "AssemblySeqDescription":string,
   "BinNumDescription":string,
   "CommodityDescription":string,
   "CountryNumDescription":string,
   "DimCodeDimCodeDescription":string,
   "InspectorIDName":string,
   "InvoiceNumDescription":string,
   "JobNumPartDescription":string,
   "PackSlipInPrice":boolean,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumPartDescription":string,
   "PartNumIUM":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumTrackLots":boolean,
   "PartNumPricePerCode":string,
   "PartNumSellingFactor":number,
   "PartNumSalesUM":string,
   "PartNumAttrClassID":string,
   "POLineVenPartNum":string,
   "POLineLineDesc":string,
   "POLinePartNum":string,
   "PONumConfirmed":boolean,
   "PONumApprovalStatus":string,
   "PONumShipToConName":string,
   "PONumShipName":string,
   "PONumApprove":boolean,
   "PurchCodePurchDesc":string,
   "PurPointZip":string,
   "PurPointState":string,
   "PurPointCity":string,
   "PurPointPrimPCon":number,
   "PurPointAddress2":string,
   "PurPointAddress3":string,
   "PurPointAddress1":string,
   "PurPointCountry":string,
   "PurPointName":string,
   "TaxCatIDDescription":string,
   "VendorNumCurrencyCode":string,
   "VendorNumDefaultFOB":string,
   "VendorNumAddress1":string,
   "VendorNumTermsCode":string,
   "VendorNumState":string,
   "VendorNumCountry":string,
   "VendorNumZIP":string,
   "VendorNumName":string,
   "VendorNumVendorID":string,
   "VendorNumAddress3":string,
   "VendorNumAddress2":string,
   "VendorNumCity":string,
   "WareHouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RcvDtlTaxRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  The Vendors purchase point ID.  */  
   "PurPoint":string,
      /**  Vendors Packing Slip #.  */  
   "PackSlip":string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  */  
   "PackLine":number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**  Tax Rate Code.  */  
   "RateCode":string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   "ECAcquisitionSeq":number,
      /**  ReportableAmt  */  
   "ReportableAmt":number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   "DocReportableAmt":number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   "TaxableAmt":number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   "DocTaxableAmt":number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   "Percent":number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   "TaxAmt":number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   "DocTaxAmt":number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   "Manual":boolean,
      /**  Userid of the user who created this record  */  
   "CreatedBy":string,
      /**  Date and time when this record was created  */  
   "CreatedOn":string,
      /**  Userid of the user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  Date and time of the last change to this record  */  
   "ChangedOn":string,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
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
      /**  CollectionType  */  
   "CollectionType":number,
      /**  Timing of when to report taxes  */  
   "Timing":number,
      /**  Exemption Type  */  
   "ExemptType":number,
      /**  Exemption Percent  */  
   "ExemptPercent":number,
      /**  Resolution Number  */  
   "ResolutionNum":string,
      /**  Resolution date.  */  
   "ResolutionDate":string,
      /**  Date to determine the tax rate.  */  
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
      /**  Unique Identifier for Legal Text  */  
   "TextCode":string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "TaxAmtVar":number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "DocTaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmtVar":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
   "DocScrDedTaxAmt":number,
   "DocScrReportableAmt":number,
   "DocScrTaxableAmt":number,
   "DocScrTaxAmt":number,
   "DocScrTaxAmtVar":number,
   "Rpt1ScrDedTaxAmt":number,
   "Rpt1ScrReportableAmt":number,
   "Rpt1ScrTaxableAmt":number,
   "Rpt1ScrTaxAmt":number,
   "Rpt1ScrTaxAmtVar":number,
   "Rpt2ScrDedTaxAmt":number,
   "Rpt2ScrReportableAmt":number,
   "Rpt2ScrTaxableAmt":number,
   "Rpt2ScrTaxAmt":number,
   "Rpt2ScrTaxAmtVar":number,
   "Rpt3ScrDedTaxAmt":number,
   "Rpt3ScrReportableAmt":number,
   "Rpt3ScrTaxableAmt":number,
   "Rpt3ScrTaxAmt":number,
   "Rpt3ScrTaxAmtVar":number,
   "ScrDedTaxAmt":number,
   "ScrReportableAmt":number,
   "ScrTaxableAmt":number,
   "ScrTaxAmt":number,
   "ScrTaxAmtVar":number,
      /**  Document Fixed Tax Amount  */  
   "DocScrFixedAmount":number,
      /**  Display Fixed Amount in base currency.  */  
   "ScrFixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ScrFixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ScrFixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ScrFixedAmount":number,
      /**  Collection Type Description  */  
   "DescCollectionType":string,
   "BitFlag":number,
   "RateCodeDescription":string,
   "RcvDtlPONum":number,
   "TaxCodeDescription":string,
   "VendorCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RcvDutyRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  The Vendors purchase point ID.  */  
   "PurPoint":string,
      /**  Vendors Packing Slip #.  */  
   "PackSlip":string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  */  
   "PackLine":number,
      /**  Unique Number automatically assigned which is used along with VendorNum, PurPoint, PackSlip and PackLine to uniquely identify the Duty record within the Receipt Line.  */  
   "DutySeq":number,
      /**  Tariff Code must be for a Preference Scheme that is linked to the Country of Origin.  */  
   "TariffCode":string,
      /**   Duty Amount is calculated based on PO Release Value, Shipment Qty, Tariff Rate, Tariff Percent and Tariff Specific Amount.
Formula: (Total Shipment Qty * Tariff Rate) + (Total Shipment Value * Tariff Percent) + Specific Duty Amount  */  
   "DutyAmt":number,
      /**  Receipt Line Duty Comments  */  
   "CommentText":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Duty Amount is calculated based on PO Release Value, Shipment Qty, Tariff Rate, Tariff Percent and Tariff Specific Amount.  */  
   "InDutyAmt":number,
      /**  Flag to indicate if landed cost info can be updated.  */  
   "AllowLCUpdate":boolean,
      /**   Duty Amount is calculated based on PO Release Value, Shipment Qty, Tariff Rate, Tariff Percent and Tariff Specific Amount.
Formula: (Total Shipment Qty * Tariff Rate) + (Total Shipment Value * Tariff Percent) + Specific Duty Amount  */  
   "ScrDutyAmt":number,
   "BitFlag":number,
   "TariffDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RcvHeadAttchRow{
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

export interface Erp_Tablesets_RcvHeadListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  The Vendors purchase point ID.  */  
   "PurPoint":string,
      /**  Vendors Packing Slip #.  */  
   "PackSlip":string,
      /**  Receipt Date. Defaults as current system date.  */  
   "ReceiptDate":string,
      /**  Person that entered the transaction. It is set to the DCD-USERID that was logged on when the record was created . This is not maintainable by the user. This is could be used as a selection parameter for reporting and browsing.  */  
   "EntryPerson":string,
      /**  An internal flag that indicates this receipt document is to be saved for retrieval by A\P invoice entry. This is set based on the value stored in APSyst.SaveForInvoicing.  */  
   "SaveForInvoicing":boolean,
      /**  An internal flag that indicates "ALL" the details items on this receipt document have been invoiced. This is set to "Yes" when there are no related RcvDtl records where RcvDtl.Invoiced = No. This flag along with the SaveForInvoicing flag are used to present a list of uninvoiced packing slips.  */  
   "Invoiced":boolean,
      /**  Contains comments about the overall Receipt.  */  
   "ReceiptComment":string,
      /**  Short name or initials of person who actually did the receiving. A totally optional field which can be used for internal reference.  */  
   "ReceivePerson":string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia.  */  
   "ShipViaCode":string,
      /**  The system date when this record was created.  */  
   "EntryDate":string,
      /**  Site that received the goods.  */  
   "Plant":string,
      /**  Purchase order number that uniquely identifies the purchase order.  */  
   "PONum":number,
      /**  Reference field for Landed Costs  */  
   "LCReference":string,
      /**  Comment field for Landed Costs  */  
   "LCComment":string,
      /**  Total amount of landed cost spread amongst the lines.  This amount includes all duties and indirect costs of all lines.  */  
   "LandedCost":number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  This field holds the variance amount for the landed costs.  */  
   "LCVariance":number,
      /**  Indicates if linked to a inter-company shipment  */  
   "ICLinked":boolean,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   "GlbVendorNum":number,
      /**  Global Purchase Point identifier.  Used in Consolidated Purchasing.  */  
   "GlbPurPoint":string,
      /**  Global Packing Slip identifier.  Used in Consolidated Purchasing.  */  
   "GlbPackSlip":string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   "ContainerID":number,
      /**  Weight  */  
   "Weight":number,
      /**  Identifies how the landed cost was disbursed among the container details.  Valid options are Volume (only for po releases tied to a container), Weight, Value and Manual.  */  
   "LCDisburseMethod":string,
      /**  This is a flag representing whether or not this is a receipt that was auto generated.  It could only be true if it is associated with an SMI type PO.  */  
   "AutoReceipt":boolean,
      /**  Indicates the type of transaction that created this auto receipt.  This field will only be populated if AutoReceipt = true.  */  
   "AutoTranType":string,
      /**  POType Identifier of the associated PO ('Std', 'CMI', or 'SMI')  */  
   "POType":string,
      /**  The unique number of the PartTran record that was the source of this transaction.  This field will only be populated if AutoReceipt = true.  */  
   "AutoTranID":number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  */  
   "WeightUOM":string,
      /**  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  */  
   "UpliftPercent":number,
      /**  This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the receipt lines using the line tariffs as a factor.  */  
   "SpecDutyAmt":number,
      /**  The total Landed Cost Amount disbursed for this receipt.  */  
   "AppliedLCAmt":number,
      /**  The total Duty Amount of the entire receipt.  */  
   "LCDutyAmt":number,
      /**  The total Indirect Cost Amount of the entire receipt.  */  
   "LCIndCost":number,
      /**  Flag to indicate if all of the receipt duties and indirect costs needs to be applied or disbursed.  */  
   "ApplyToLC":boolean,
      /**  Flag to indicate if the entire receipt has been completely received.  */  
   "Received":boolean,
      /**  The date the shipment arrived. Defaults as current system date.  */  
   "ArrivedDate":string,
      /**  The total Landed Cost Amount applied for this receipt.  */  
   "AppliedRcptLCAmt":number,
      /**  The total Uplift Indirect Cost Amount of the receipt. The total LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and SpecDutyAmt.  */  
   "LCUpliftIndCost":number,
      /**  This field holds the applied variance amount for the landed costs.  */  
   "AppliedLCVariance":number,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Stores the number of the import document.  Default value for lines.  */  
   "ImportNum":string,
      /**  Stores the Country from which the document is imported.  Default value for lines.  */  
   "ImportedFrom":number,
      /**  Location description from which the document is imported.  Default value for lines.  */  
   "ImportedFromDesc":string,
      /**  Gross Weight  */  
   "GrossWeight":number,
      /**   Qualifies the unit of measure of the GrossWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t  if Part.GrossWeightUOM is not known.  */  
   "GrossWeightUOM":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Address Information from Vendor or VendorPP  */  
   "AddrList":string,
   "LegalNumberMessage":string,
      /**  Display field used for container landed costs.  */  
   "DispLandedCost":number,
      /**  This field is used to hold the original total landed cost for containers for all plants.  */  
   "OrigLandedCost":number,
   "POTypeDesc":string,
      /**  Flag to indicate if record can be updated.  */  
   "AllowLCUpdate":boolean,
      /**  Flag to indicate if UpliftPercent should be enabled.  */  
   "AllowUplift":boolean,
      /**  Flag to indicate if details need to be refreshed after changing the UpliftPercent from header.  */  
   "UpdateDtlRecs":boolean,
      /**  Logical used to indicate if all details have been received.  */  
   "eshReceived":boolean,
      /**  Logical indicating whether or not the receipt has been fully received.  If yes then the receipt has only been partially received.  */  
   "PartialReceipt":boolean,
      /**  Landed cost message used to inform the user on retrieval of data that the applied and landed costs do not equal.  */  
   "LCMessage":string,
      /**  Flag to indicate if receipt details need to be refreshed after changing the Receipt Date from header.  */  
   "UpdateDtlRcptDate":boolean,
      /**  Flag to indicate if receipt details need to be refreshed after changing the Arrival Date from header.  */  
   "UpdateDtlArvdDate":boolean,
   "PurPointState":string,
   "PurPointPrimPCon":number,
   "PurPointAddress1":string,
   "PurPointCity":string,
   "PurPointCountry":string,
   "PurPointAddress3":string,
   "PurPointAddress2":string,
   "PurPointZip":string,
   "PurPointName":string,
   "ShipViaCodeDescription":string,
   "ShipViaCodeWebDesc":string,
   "VendorNumTermsCode":string,
   "VendorNumCountry":string,
   "VendorNumAddress1":string,
   "VendorNumZIP":string,
   "VendorNumCurrencyCode":string,
   "VendorNumName":string,
   "VendorNumDefaultFOB":string,
   "VendorNumAddress2":string,
   "VendorNumState":string,
   "VendorNumAddress3":string,
   "VendorNumCity":string,
   "VendorNumVendorID":string,
   "vrPONumShipToConName":string,
   "vrPONumShipName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RcvHeadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  The Vendors purchase point ID.  */  
   "PurPoint":string,
      /**  Vendors Packing Slip #.  */  
   "PackSlip":string,
      /**  Receipt Date. Defaults as current system date.  */  
   "ReceiptDate":string,
      /**  Person that entered the transaction. It is set to the DCD-USERID that was logged on when the record was created . This is not maintainable by the user. This is could be used as a selection parameter for reporting and browsing.  */  
   "EntryPerson":string,
      /**  An internal flag that indicates this receipt document is to be saved for retrieval by A\P invoice entry. This is set based on the value stored in APSyst.SaveForInvoicing.  */  
   "SaveForInvoicing":boolean,
      /**  An internal flag that indicates "ALL" the details items on this receipt document have been invoiced. This is set to "Yes" when there are no related RcvDtl records where RcvDtl.Invoiced = No. This flag along with the SaveForInvoicing flag are used to present a list of uninvoiced packing slips.  */  
   "Invoiced":boolean,
      /**  Contains comments about the overall Receipt.  */  
   "ReceiptComment":string,
      /**  Short name or initials of person who actually did the receiving. A totally optional field which can be used for internal reference.  */  
   "ReceivePerson":string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia.  */  
   "ShipViaCode":string,
      /**  The system date when this record was created.  */  
   "EntryDate":string,
      /**  Site that received the goods.  */  
   "Plant":string,
      /**  Purchase order number that uniquely identifies the purchase order.  */  
   "PONum":number,
      /**  Reference field for Landed Costs  */  
   "LCReference":string,
      /**  Comment field for Landed Costs  */  
   "LCComment":string,
      /**  Total amount of landed cost spread amongst the lines.  This amount includes all duties and indirect costs of all lines.  */  
   "LandedCost":number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  This field holds the variance amount for the landed costs.  */  
   "LCVariance":number,
      /**  Indicates if linked to a inter-company shipment  */  
   "ICLinked":boolean,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   "GlbVendorNum":number,
      /**  Global Purchase Point identifier.  Used in Consolidated Purchasing.  */  
   "GlbPurPoint":string,
      /**  Global Packing Slip identifier.  Used in Consolidated Purchasing.  */  
   "GlbPackSlip":string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   "ContainerID":number,
      /**  Weight  */  
   "Weight":number,
      /**  Identifies how the landed cost was disbursed among the container details.  Valid options are Volume (only for po releases tied to a container), Weight, Value and Manual.  */  
   "LCDisburseMethod":string,
      /**  This is a flag representing whether or not this is a receipt that was auto generated.  It could only be true if it is associated with an SMI type PO.  */  
   "AutoReceipt":boolean,
      /**  Indicates the type of transaction that created this auto receipt.  This field will only be populated if AutoReceipt = true.  */  
   "AutoTranType":string,
      /**  POType Identifier of the associated PO ('Std', 'CMI', or 'SMI')  */  
   "POType":string,
      /**  The unique number of the PartTran record that was the source of this transaction.  This field will only be populated if AutoReceipt = true.  */  
   "AutoTranID":number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  */  
   "WeightUOM":string,
      /**  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  */  
   "UpliftPercent":number,
      /**  This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the receipt lines using the line tariffs as a factor.  */  
   "SpecDutyAmt":number,
      /**  The total Landed Cost Amount disbursed for this receipt.  */  
   "AppliedLCAmt":number,
      /**  The total Duty Amount of the entire receipt.  */  
   "LCDutyAmt":number,
      /**  The total Indirect Cost Amount of the entire receipt.  */  
   "LCIndCost":number,
      /**  Flag to indicate if all of the receipt duties and indirect costs needs to be applied or disbursed.  */  
   "ApplyToLC":boolean,
      /**  Flag to indicate if the entire receipt has been completely received.  */  
   "Received":boolean,
      /**  The date the shipment arrived. Defaults as current system date.  */  
   "ArrivedDate":string,
      /**  The total Landed Cost Amount applied for this receipt.  */  
   "AppliedRcptLCAmt":number,
      /**  The total Uplift Indirect Cost Amount of the receipt. The total LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and SpecDutyAmt.  */  
   "LCUpliftIndCost":number,
      /**  This field holds the applied variance amount for the landed costs.  */  
   "AppliedLCVariance":number,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Stores the number of the import document.  Default value for lines.  */  
   "ImportNum":string,
      /**  Stores the Country from which the document is imported.  Default value for lines.  */  
   "ImportedFrom":number,
      /**  Location description from which the document is imported.  Default value for lines.  */  
   "ImportedFromDesc":string,
      /**  Gross Weight  */  
   "GrossWeight":number,
      /**   Qualifies the unit of measure of the GrossWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t  if Part.GrossWeightUOM is not known.  */  
   "GrossWeightUOM":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  The Tax Liability for this Receipt  */  
   "TaxRegionCode":string,
      /**  Tax Point  */  
   "TaxPoint":string,
      /**  Date Used to calculate Tax Rates  */  
   "TaxRateDate":string,
      /**  Indicates that the tax is included in the unit price  */  
   "InPrice":boolean,
      /**  ** NOT USED TO BE DROPPED 10.2 ** This flag determines whether any manual taxes were created for a header miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  */  
   "HdrTaxNoUpdt":boolean,
      /**  Tax Rate Group Code - FUTUREUSE  */  
   "TaxRateGrpCode":string,
      /**  The flag indicates that taxes have been calculated.  Once the flag is true is should never be changed back to false.  This will be set to true when any receipt line is marked as received, or when taxes have been calculated via the Calculate All Taxes menu option.  */  
   "TaxesCalculated":boolean,
      /**  Internal usage for inclusive taxes - The total Landed Cost Amount disbursed for this receipt.  */  
   "InAppliedLCAmt":number,
      /**  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  */  
   "InAppliedLCVariance":number,
      /**  Internal usage for inclusive taxes - The total Landed Cost Amount applied for this receipt.  */  
   "InAppliedRcptLCAmt":number,
      /**  Internal usage for inclusive taxes - Total amount of landed cost spread amongst the lines.  This amount includes all duties and indirect costs of all lines.  */  
   "InLandedCost":number,
      /**  Internal usage for inclusive taxes - The total Duty Amount of the entire receipt.  */  
   "InLCDutyAmt":number,
      /**  Internal usage for inclusive taxes - The total Indirect Cost Amount of the entire receipt.  */  
   "InLCIndCost":number,
      /**  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the receipt. The total LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and SpecDutyAmt.  */  
   "InLCUpliftIndCost":number,
      /**  Internal usage for inclusive taxes - This field holds the variance amount for the landed costs.  */  
   "InLCVariance":number,
      /**  Internal usage for inclusive taxes - This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the receipt lines using the line tariffs as a factor.  */  
   "InSpecDutyAmt":number,
      /**  Declaration Bill  */  
   "CNDeclarationBill":string,
      /**  Bonded  */  
   "CNBonded":boolean,
      /**  APTaxRoundOption  */  
   "APTaxRoundOption":number,
      /**  Address Information from Vendor or VendorPP  */  
   "AddrList":string,
      /**  Logical indicating whether or not the receipt has been fully received.  If yes then the receipt has only been partially received.  */  
   "PartialReceipt":boolean,
   "POLine":number,
   "PORel":number,
   "POTypeDesc":string,
   "ShipViaDesc":string,
      /**  Total amount.  This is the sum of all the other total fields.  */  
   "TotalAmt":number,
      /**  Total dedicated Tax amount.  */  
   "TotDedTaxAmt":number,
      /**  Total duties amount.  This is the sum of RcvHead.SpecDutyAmt + RcvHead.LCDutyAmt  */  
   "TotDutiesAmt":number,
      /**  Total Gross Weight of all receipt lines  */  
   "TotGrossWeight":number,
      /**  Qualifies the unit of measure of the Gross Weight field.  */  
   "TotGrossWeightUOM":string,
      /**  Total Indirect Costs amount.  This is a sum of all RcvMisc.ActualAmt.  */  
   "TotIndirectCostsAmt":number,
      /**  Total amount for all receipt lines.  This is the sum of RcvDtl.POTransValue.  */  
   "TotLinesAmt":number,
      /**  Total Self Assessed Tax amount  */  
   "TotSATaxAmt":number,
      /**  Total tax amount.  This is the sum of RcvHeadTax.TaxAmt  */  
   "TotTaxAmt":number,
      /**  Total Weight of all receipt lines  */  
   "TotWeight":number,
      /**  Qualifies the unit of measure of the Weight field.  */  
   "TotWeightUOM":string,
      /**  Total WithHolding Tax amount  */  
   "TotWHTaxAmt":number,
      /**  Flag to indicate if receipt details need to be refreshed after changing the Arrival Date from header.  */  
   "UpdateDtlArvdDate":boolean,
      /**  Flag to indicate if receipt details need to be refreshed after changing the Receipt Date from header.  */  
   "UpdateDtlRcptDate":boolean,
      /**  Flag to indicate if details need to be refreshed after changing the UpliftPercent from header.  */  
   "UpdateDtlRecs":boolean,
      /**  Flag to indicate if record can be updated.  */  
   "AllowLCUpdate":boolean,
      /**  Flag to indicate if UpliftPercent should be enabled.  */  
   "AllowUplift":boolean,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Display field used for container landed costs.  */  
   "DispLandedCost":number,
      /**  Logical used to indicate if all details have been received.  */  
   "eshReceived":boolean,
   "IntQueID":number,
      /**  Landed cost message used to inform the user on retrieval of data that the applied and landed costs do not equal.  */  
   "LCMessage":string,
   "LegalNumberMessage":string,
      /**  This field is used to hold the original total landed cost for containers for all plants.  */  
   "OrigLandedCost":number,
      /**  The formatted address Information from Vendor or VendorPP  */  
   "AddrListFormatted":string,
   "BitFlag":number,
   "PurPointName":string,
   "PurPointCountry":string,
   "PurPointState":string,
   "PurPointAddress3":string,
   "PurPointAddress1":string,
   "PurPointPrimPCon":number,
   "PurPointAddress2":string,
   "PurPointCity":string,
   "PurPointZip":string,
   "ShipViaCodeWebDesc":string,
   "ShipViaCodeDescription":string,
   "TaxRegionCodeDescription":string,
   "VendorNumState":string,
   "VendorNumTermsCode":string,
   "VendorNumVendorID":string,
   "VendorNumAddress2":string,
   "VendorNumCity":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCurrencyCode":string,
   "VendorNumName":string,
   "VendorNumZIP":string,
   "VendorNumCountry":string,
   "VendorNumAddress3":string,
   "VendorNumAddress1":string,
   "vrPONumCNBonded":boolean,
   "vrPONumShipToConName":string,
   "vrPONumShipName":string,
   "XbSystReceiptTaxCalculate":boolean,
   "XbSystAPTaxLnLevel":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RcvHeadTaxRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  The Vendors purchase point ID.  */  
   "PurPoint":string,
      /**  Vendors Packing Slip #.  */  
   "PackSlip":string,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**  Tax Rate Code.  */  
   "RateCode":string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   "ECAcquisitionSeq":number,
      /**  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcReportableAmt.  */  
   "ReportableAmt":number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   "DocReportableAmt":number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   "TaxableAmt":number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   "DocTaxableAmt":number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   "Percent":number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   "TaxAmt":number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   "DocTaxAmt":number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   "Manual":boolean,
      /**  Userid of the user who created this record  */  
   "CreatedBy":string,
      /**  Date and time when this record was created  */  
   "CreatedOn":string,
      /**  Userid of the user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  Date and time of the last change to this record  */  
   "ChangedOn":string,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
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
      /**  Date to determine the tax rate.  */  
   "TaxRateDate":string,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   "DefTaxableAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
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
      /**  TextCode  */  
   "TextCode":string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "TaxAmtVar":number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "DocTaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmtVar":number,
      /**  flag to indicate if this record is used only to total detail records,  */  
   "SummaryOnly":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BaseCurrSymbol":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
   "CurrSymbol":string,
      /**  Collection Type Description  */  
   "DescCollectionType":string,
   "EnableSuperGRate":boolean,
   "Rpt1ScrDedTaxAmt":number,
      /**  Display field for Rpt1ScrFixedAmount  */  
   "Rpt1ScrFixedAmount":number,
   "Rpt1ScrReportableAmt":number,
   "Rpt1ScrTaxableAmt":number,
   "Rpt1ScrTaxAmt":number,
   "Rpt1ScrTaxAmtVar":number,
   "Rpt2ScrDedTaxAmt":number,
      /**  Display field for Rpt2FixedAmount  */  
   "Rpt2ScrFixedAmount":number,
   "Rpt2ScrReportableAmt":number,
   "Rpt2ScrTaxableAmt":number,
   "Rpt2ScrTaxAmt":number,
   "Rpt2ScrTaxAmtVar":number,
   "Rpt3ScrDedTaxAmt":number,
      /**  Display field for Rpt3rFixedAmount  */  
   "Rpt3ScrFixedAmount":number,
   "Rpt3ScrReportableAmt":number,
   "Rpt3ScrTaxableAmt":number,
   "Rpt3ScrTaxAmt":number,
   "Rpt3ScrTaxAmtVar":number,
   "ScrDedTaxAmt":number,
   "ScrDocDedTaxAmt":number,
      /**  Doc Fixed Amount  */  
   "ScrDocFixedAmount":number,
   "ScrDocReportableAmt":number,
   "ScrDocTaxableAmt":number,
   "ScrDocTaxAmt":number,
   "ScrDocTaxAmtVar":number,
      /**  FixedAmount  */  
   "ScrFixedAmount":number,
   "ScrReportableAmt":number,
   "ScrTaxableAmt":number,
   "ScrTaxAmt":number,
   "ScrTaxAmtVar":number,
   "BitFlag":number,
   "RateCodeDescription":string,
   "TaxCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RcvMiscRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  The Vendors purchase point ID.  */  
   "PurPoint":string,
      /**  Vendors Packing Slip #.  */  
   "PackSlip":string,
      /**  Unique Number automatically assigned within the Company/VendorNum/PurPoint/PackSlip to uniquely identify each Indirect Costs for this receipt.  */  
   "MiscSeq":number,
      /**  Miscellaneous Charge ID that is flagged for Landed Cost  */  
   "MiscCode":string,
      /**  Flag to indicate if the Indirect Cost is to be excluded from the Landed Cost calculation.  Disabled when IncTransValue is checked.  */  
   "ExcludeFromLC":boolean,
      /**  Flag to indicate if the Indirect Cost is to be included in the Transaction Value (statistical value) which is used to calculate duties.  Disabled when the ExcludeFromLC is checked.  */  
   "IncTransValue":boolean,
      /**  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  */  
   "LCDisburseMethod":string,
      /**  Actual Miscellaneous Charge Amount.  */  
   "ActualAmt":number,
      /**  Actual Miscellaneous Charge Amount in the currency specified.  */  
   "DocActualAmt":number,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   "LockRate":boolean,
      /**  Receipt Indirect Cost Comments  */  
   "CommentText":string,
      /**  Reporting currency value of the Actual Amount.  */  
   "Rpt1ActualAmt":number,
      /**  Reporting currency value of the Actual Amount.  */  
   "Rpt2ActualAmt":number,
      /**  Reporting currency value of the Actual Amount.  */  
   "Rpt3ActualAmt":number,
      /**  The date that will be used to get the exchange rate if the indirect cost is not associated with an invoice miscellaneous charge.  */  
   "ApplyDate":string,
      /**  Unique identifier of the currency rate group.  */  
   "RateGrpCode":string,
      /**  Invoice Number from corresponding APInvMsc record.  */  
   "InvoiceNum":string,
      /**  Invoice Line from corresponding APInvMsc record.  */  
   "InvoiceLine":number,
      /**  The unique sequence number identifying the AP invoice miscellaneous charge.  */  
   "MscNum":number,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   "Percentage":number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   "Type":string,
      /**  VendorNum duplicated from the corresponding APInvHed record.  Not directly maintainable by the operator.  */  
   "APInvVendorNum":number,
      /**  Reference to RcvDtl.PackLine. An integer that uniquely identifies a detail record within a Packing slip.  */  
   "PackLine":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates the Tax Category for this Receipt Misc. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  */  
   "TaxCatID":string,
      /**  Indicates if the Indirect Cost is taxable  */  
   "Taxable":boolean,
      /**  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  */  
   "NoTaxRecalc":boolean,
      /**  Actual Miscellaneous Charge Amount.  */  
   "InActualAmt":number,
      /**  Actual Miscellaneous Charge Amount in the currency specified.  */  
   "DocInActualAmt":number,
      /**  Reporting currency value of the Actual Amount.  */  
   "Rpt1InActualAmt":number,
      /**  Reporting currency value of the Actual Amount.  */  
   "Rpt2InActualAmt":number,
      /**  Reporting currency value of the Actual Amount.  */  
   "Rpt3InActualAmt":number,
      /**  Exchange rate that will be used for this indirect cost.  */  
   "ExchangeRate":number,
      /**  Label for the exchange rate  */  
   "RateLabel":string,
      /**  Total dedicated Tax amount.  */  
   "TotDedTaxAmt":number,
      /**  Total Self Assessed Tax amount  */  
   "TotSATaxAmt":number,
      /**  Total tax amount  */  
   "TotTaxAmt":number,
      /**  Flag to indicate if landed cost info can be updated.  */  
   "AllowLCUpdate":boolean,
      /**  Currency.CurrSymbol for currency "BASE"  */  
   "BaseCurrSymbol":string,
      /**  Actual Miscellaneous Charge Amount - Screen value.  */  
   "ScrActualAmt":number,
      /**  Reporting currency value of the Actual Amount - Screen value.  */  
   "Rpt1ScrActualAmt":number,
      /**  Reporting currency value of the Actual Amount - Screen value.  */  
   "Rpt2ScrActualAmt":number,
      /**  Reporting currency value of the Actual Amount - Screen value  */  
   "Rpt3ScrActualAmt":number,
      /**  Actual Miscellaneous Charge Amount in the currency specified - Screen value  */  
   "DocScrActualAmt":number,
   "BitFlag":number,
   "APInvVendorName":string,
   "APInvVendorVendorID":string,
   "CurrencyCurrSymbol":string,
   "CurrencyCurrencyID":string,
   "CurrencyDocumentDesc":string,
   "CurrencyCurrDesc":string,
   "CurrencyCurrName":string,
   "PurMiscLCDisburseMethod":string,
   "PurMiscLCCurrencyCode":string,
   "PurMiscDescription":string,
   "PurMiscLCAmount":number,
   "RateGrpDescription":string,
   "RcvHeadReceiptDate":string,
   "RcvHeadInPrice":boolean,
   "TaxCatIDDescription":string,
   "VendorName":string,
   "VendorVendorID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RcvMiscTaxRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  The Vendors purchase point ID.  */  
   "PurPoint":string,
      /**  Vendors Packing Slip #.  */  
   "PackSlip":string,
      /**  Unique Number automatically assigned within the Company/VendorNum/PurPoint/PackSlip to uniquely identify each Indirect Costs for this receipt.  */  
   "MiscSeq":number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**  Tax Rate Code.  */  
   "RateCode":string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   "ECAcquisitionSeq":number,
      /**  ** NOT USED TO BE DROPPED 10.2 ** Miscellaneous Charge ID that is flagged for Landed Cost  */  
   "MiscCode":string,
      /**  ReportableAmt  */  
   "ReportableAmt":number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   "DocReportableAmt":number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   "TaxableAmt":number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   "DocTaxableAmt":number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   "Percent":number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   "TaxAmt":number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   "DocTaxAmt":number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   "Manual":boolean,
      /**  Userid of the user who created this record  */  
   "CreatedBy":string,
      /**  Date and time when this record was created  */  
   "CreatedOn":string,
      /**  Userid of the user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  Date and time of the last change to this record  */  
   "ChangedOn":string,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
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
      /**  CollectionType  */  
   "CollectionType":number,
      /**  Timing of when to report taxes  */  
   "Timing":number,
      /**  Exemption Type  */  
   "ExemptType":number,
      /**  Exemption Percent  */  
   "ExemptPercent":number,
      /**  Resolution Number  */  
   "ResolutionNum":string,
      /**  Resolution date.  */  
   "ResolutionDate":string,
      /**  Date to determine the tax rate.  */  
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
      /**  Unique Identifier for Legal Text  */  
   "TextCode":string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "TaxAmtVar":number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "DocTaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmtVar":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
   "DocScrDedTaxAmt":number,
   "DocScrReportableAmt":number,
   "DocScrTaxableAmt":number,
   "DocScrTaxAmt":number,
   "DocScrTaxAmtVar":number,
   "Rpt1ScrDedTaxAmt":number,
   "Rpt1ScrReportableAmt":number,
   "Rpt1ScrTaxableAmt":number,
   "Rpt1ScrTaxAmt":number,
   "Rpt1ScrTaxAmtVar":number,
   "Rpt2ScrDedTaxAmt":number,
   "Rpt2ScrReportableAmt":number,
   "Rpt2ScrTaxableAmt":number,
   "Rpt2ScrTaxAmt":number,
   "Rpt2ScrTaxAmtVar":number,
   "Rpt3ScrDedTaxAmt":number,
   "Rpt3ScrReportableAmt":number,
   "Rpt3ScrTaxableAmt":number,
   "Rpt3ScrTaxAmt":number,
   "Rpt3ScrTaxAmtVar":number,
   "ScrDedTaxAmt":number,
   "ScrReportableAmt":number,
   "ScrTaxableAmt":number,
   "ScrTaxAmt":number,
   "ScrTaxAmtVar":number,
      /**  Collection Type Description  */  
   "DescCollectionType":string,
      /**  Display Fixed Amount in base currency.  */  
   "ScrFixedAmount":number,
      /**  Document Fixed Tax Amount  */  
   "DocScrFixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ScrFixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ScrFixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ScrFixedAmount":number,
   "BitFlag":number,
   "RateCodeDescription":string,
   "RcvMiscCurrencyCode":string,
   "TaxCodeDescription":string,
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

export interface Erp_Tablesets_SupplierXRefRow{
   "Company":string,
   "MfgID":string,
   "MfgName":string,
   "MfgNum":number,
   "MfgPartNum":string,
   "PartNum":string,
   "POReference":boolean,
   "Receipt":boolean,
   "VendNum":number,
   "VendPartNum":string,
   "Invoice":boolean,
      /**  RcvXRefNum  */  
   "RcvXRefNum":number,
   "Inspected":boolean,
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
      @param vendorNum
      @param purPoint
      @param packSlip
      @param checkforManualPrompt
      @param ds
   */  
export interface AssignLegalNumber_input{
      /**  Vendor Number  */  
   vendorNum:number,
      /**  Purchase Point  */  
   purPoint:string,
      /**  Packing Slip  */  
   packSlip:string,
      /**  If true then Get Legal Number defaults and check if Generate Type is manual and set RequiresUserInput appropriately, otherwise just generate Legal Number  */  
   checkforManualPrompt:boolean,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface AssignLegalNumber_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
   RequiresUserInput:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface AutoSetToLocationToDflt_input{
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface AutoSetToLocationToDflt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface AutoSetToLocation_input{
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface AutoSetToLocation_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface CNPreUpdate_input{
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface CNPreUpdate_output{
parameters : {
      /**  output parameters  */  
   sMessage:string,
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param calledFromUI
      @param ds
   */  
export interface CalculateReceiptTaxes_input{
   vendorNum:number,
   purPoint:string,
   packSlip:string,
   calledFromUI:boolean,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface CalculateReceiptTaxes_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface CheckCNCustomsDeclarationBillLine_input{
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface CheckCNCustomsDeclarationBillLine_output{
parameters : {
      /**  output parameters  */  
   sMessage:string,
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param ds
   */  
export interface CheckCompliance_input{
      /**  Vendor Number  */  
   vendorNum:number,
      /**  Purchase Point Number  */  
   purPoint:string,
      /**  Receipt Packing Slip Number  */  
   packSlip:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface CheckCompliance_output{
parameters : {
      /**  output parameters  */  
   compliant:boolean,
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface CheckContainersBeforeUpdate_input{
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface CheckContainersBeforeUpdate_output{
parameters : {
      /**  output parameters  */  
   qMessageStr:string,
   qQuestion:string,
   sMessageStr:string,
   sQuestion:string,
   lMessageStr:string,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packLine
      @param packSlip
   */  
export interface CheckDtlBeforeUpdate_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  Receipt Packing Number  */  
   packSlip:string,
}

export interface CheckDtlBeforeUpdate_output{
parameters : {
      /**  output parameters  */  
   qMessageStr:string,
   sMessageStr:string,
   lcMessageStr:string,
   pcMessageStr:string,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packLine
      @param packSlip
   */  
export interface CheckDtlCompliance_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  Receipt Packing Number  */  
   packSlip:string,
}

export interface CheckDtlCompliance_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
   qMessageStr:string,
   pcMessageStr:string,
}
}

   /** Required : 
      @param poNum
      @param poLine
      @param poRelNum
      @param jobNum
   */  
export interface CheckDtlJobStatus_input{
      /**  Purchase Order Number for Receipt  */  
   poNum:number,
      /**  Purchase Order Line  */  
   poLine:number,
      /**  Purchase Order Release  */  
   poRelNum:number,
      /**  Job Number  */  
   jobNum:string,
}

export interface CheckDtlJobStatus_output{
parameters : {
      /**  output parameters  */  
   poQuestion:string,
   questionMsg:string,
   warnMsg:string,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param lotNum
   */  
export interface CheckDtlLotInfo_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  New Lot Number to validate  */  
   lotNum:string,
}

export interface CheckDtlLotInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
   questionMsg:string,
   errorMsg:string,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param receivedTo
      @param partNum
   */  
export interface CheckDtlSSN_input{
      /**  Vendor Number  */  
   vendorNum:number,
      /**  Vendor Purchase Point ID  */  
   purPoint:string,
      /**  Packing Slip Number  */  
   packSlip:string,
      /**  Packing Slip Line  */  
   packLine:number,
      /**  Receipt ReceivedTo field (proposed or current)  */  
   receivedTo:string,
      /**  Proposed Receipt Part Number (proposed or current)  */  
   partNum:string,
}

export interface CheckDtlSSN_output{
parameters : {
      /**  output parameters  */  
   vMessage:string,
   vWMessage:string,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param jobSeq
   */  
export interface CheckDtlSeqChange_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  The proposed JobSeq value  */  
   jobSeq:number,
}

export interface CheckDtlSeqChange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
   vMessage:string,
}
}

export interface CheckForDefaultRcvInfo_output{
}

   /** Required : 
      @param ds
   */  
export interface CheckHdrBeforeUpdate_input{
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface CheckHdrBeforeUpdate_output{
parameters : {
      /**  output parameters  */  
   opUpliftWarnMsg:string,
   opReceiptWarnMsg:string,
   opArriveWarnMsg:string,
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param sysRowID
   */  
export interface CheckIfAttributeQtyMismatch_input{
   sysRowID:string,
}

export interface CheckIfAttributeQtyMismatch_output{
      /**  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity  */  
   returnObj:boolean,
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param issuedComplete
   */  
export interface CheckIssuedComplete_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
   issuedComplete:boolean,
}

export interface CheckIssuedComplete_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
   vMessage:string,
}
}

   /** Required : 
      @param ipVendorNum
      @param ipPurPoint
      @param ipPackSlip
      @param ipPackLine
      @param ds
   */  
export interface CheckLCAmtBeforeUpdate_input{
      /**  Receipt Vendor Number  */  
   ipVendorNum:number,
      /**  Receipt Purchase Point  */  
   ipPurPoint:string,
      /**  Receipt Packing Number  */  
   ipPackSlip:string,
      /**  Receipt Line to check  */  
   ipPackLine:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface CheckLCAmtBeforeUpdate_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param contractID
      @param whse
      @param bin
   */  
export interface CheckMassReceiptChangeWhseBin_input{
      /**  contractID  */  
   contractID:string,
      /**  warehouse  */  
   whse:string,
      /**  bin  */  
   bin:string,
}

export interface CheckMassReceiptChangeWhseBin_output{
parameters : {
      /**  output parameters  */  
   warnMsg:string,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
   */  
export interface CheckOnLeaveHead_input{
      /**  Vendor Number of the Receipt  */  
   vendorNum:number,
      /**  Purchase Point of the Receipt  */  
   purPoint:string,
      /**  Packing Slip number of the Receipt  */  
   packSlip:string,
}

export interface CheckOnLeaveHead_output{
parameters : {
      /**  output parameters  */  
   warnMsg:string,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
   */  
export interface CheckPOClosedInfo_input{
      /**  Vendor Number of Receipt  */  
   vendorNum:number,
      /**  Purchase Point of Receipt  */  
   purPoint:string,
      /**  Packing Slip number of Receipt  */  
   packSlip:string,
}

export interface CheckPOClosedInfo_output{
parameters : {
      /**  output parameters  */  
   warnMsg:string,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param receivedComplete
   */  
export interface CheckReceivedComplete_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
   receivedComplete:boolean,
}

export interface CheckReceivedComplete_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
   vMessage:string,
}
}

   /** Required : 
      @param packSlip
      @param poNum
      @param vendorNum
   */  
export interface CheckShipmentReceived_input{
      /**  The PackSlip number  */  
   packSlip:string,
      /**  The PO number  */  
   poNum:number,
      /**  The Vendor number  */  
   vendorNum:number,
}

export interface CheckShipmentReceived_output{
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param suppPrice
   */  
export interface CheckSupplierPrice_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  new Supplier Price  */  
   suppPrice:number,
}

export interface CheckSupplierPrice_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
   warningMsg:string,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param ds
   */  
export interface CommitRcvDtl_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface CommitRcvDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ContainerReceiptsBeforeUpdate_input{
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface ContainerReceiptsBeforeUpdate_output{
parameters : {
      /**  output parameters  */  
   lcMessage:string,
   qtyMessage:string,
   compliantMessage:string,
   legalRequiresUserInput:boolean,
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param dsReceipt
      @param dsContainerTracking
      @param inContainerID
      @param ipArrivedDate
      @param inCreateNewPoRels
   */  
export interface ContainerReceiptsUpdate_input{
   dsReceipt:Erp_Tablesets_ReceiptTableset[],
   dsContainerTracking:Erp_Tablesets_ContainerTrackingTableset[],
   inContainerID:number,
   ipArrivedDate:string,
   inCreateNewPoRels:string,
}

export interface ContainerReceiptsUpdate_output{
parameters : {
      /**  output parameters  */  
   dsReceipt:Erp_Tablesets_ReceiptTableset,
   dsContainerTracking:Erp_Tablesets_ContainerTrackingTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param intQueId
      @param poNum
      @param ds
   */  
export interface CreateMassReceipts_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Intercompany Queue ID for Intercompany Receipts  */  
   intQueId:number,
      /**  PO Number for Purchase Order Receipts  */  
   poNum:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface CreateMassReceipts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param pcid
   */  
export interface CreateMaterialQueueForPCID_input{
      /**  The PCID to create MtlQueue record for  */  
   pcid:string,
}

export interface CreateMaterialQueueForPCID_output{
}

   /** Required : 
      @param partNum
      @param lotNum
   */  
export interface CreatePartLot_input{
   partNum:string,
   lotNum:string,
}

export interface CreatePartLot_output{
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
      @param vendorNum
      @param purPoint
      @param packSlip
   */  
export interface DisburseLandedCost_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
}

export interface DisburseLandedCost_output{
}

   /** Required : 
      @param PartTranType
      @param JobNum
      @param AsmSeq
      @param JobSeq
   */  
export interface DisplayWarnMsg_input{
   PartTranType:string,
   JobNum:string,
   AsmSeq:number,
   JobSeq:number,
}

export interface DisplayWarnMsg_output{
parameters : {
      /**  output parameters  */  
   pcMsg:string,
}
}

export interface Erp_Tablesets_ContainerDetailAttchRow{
   Company:string,
   ContainerID:number,
   PONum:number,
   POLine:number,
   PORelNum:number,
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

export interface Erp_Tablesets_ContainerDetailRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   ContainerID:number,
      /**  The quantity of the PO Release that is shipped on this container.  */  
   ContainerShipQty:number,
      /**  UOM of Shipment Quantity.  */  
   ShipQtyUOm:string,
      /**  Free form text describing the container detail.  */  
   Comment:string,
      /**  Purchase order number that uniquely identifies the purchase order on this container.  */  
   PONum:number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number on this container  */  
   POLine:number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order on this container.  */  
   PORelNum:number,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  Amount of space consumed in the container by this detail line, often specified in cubic square feet.  */  
   Volume:number,
      /**   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  if Part.NetVolumeUOM is not known.  */  
   VolumeUOM:string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID.  */  
   PurPoint:string,
      /**  The total amount of disbursed landed cost for this container detail.  This amount includes the duties and indirect costs per container shipment line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   LCAmt:number,
      /**  Nett Weight  */  
   Weight:number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  */  
   NetWeightUOM:string,
      /**  Unit cost based on our unit of measure.  */  
   OurUnitCost:number,
      /**  Unit cost based on our unit of measure in document currency.  */  
   DocOurUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt1OurUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2OurUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3OurUnitCost:number,
      /**  Country Number of the Origin Country from the PO?s Supplier Purchase Point.  */  
   OrigCountryNum:number,
      /**  Container shipment line reference or name.  */  
   ContainerLineRef:string,
      /**  Arrived Quantity as reported in the receipt line.  */  
   ArrivedQty:number,
      /**  Unit of Measure of the Arrived Qty.  */  
   ArrivedQtyUOM:string,
      /**  Received Quantity as reported in the receipt line.  */  
   ReceivedQty:number,
      /**  Unit of Measure of the Received Qty  */  
   ReceivedQtyUOM:string,
      /**  The current status of the container shipment.  Valid values are: Ordered, Shipped, Imported, Arrived and Received.  */  
   ShipStatus:string,
      /**  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  */  
   UpliftPercent:number,
      /**  The total Duty Amount portion of the landed cost for this container detail. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   LCDutyAmt:number,
      /**  The total Indirect Cost portion of the landed cost for this container detail. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   LCIndCost:number,
      /**  This is by default the PO release value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  */  
   POTransValue:number,
      /**  This is the PO Base Transaction Value plus all indirect costs which are marked to include as transaction value costs.  */  
   ExtTransValue:number,
      /**  The date the container shipment detail is received. Defaults as current system date.  */  
   ReceivedDate:string,
      /**  Harmonized System (HS) goods classification code.  */  
   CommodityCode:string,
      /**  The date the container shipment detail arrived. Defaults as current system date.  */  
   ArrivedDate:string,
      /**  This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   LCSpecLineDutyAmt:number,
      /**  The total Landed Cost Amount received for this container shipment line.  */  
   AppliedRcptLCAmt:number,
      /**  The total Uplift Indirect Cost Amount of the container shipment line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   LCUpliftIndCost:number,
      /**  This field holds the applied variance amount for the landed costs.  */  
   AppliedLCVariance:number,
      /**  Gross Weight  */  
   GrossWeight:number,
      /**   Qualifies the unit of measure of the GrossWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t  if Part.NetWeightUOM is not known.  */  
   GrossWeightUOM:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates the Tax Category for this Receipt line. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  */  
   TaxCatID:string,
      /**  Indicates if the Receipt line is Taxable  */  
   Taxable:boolean,
      /**  Indicates if this item is exempt from tax for this receipt line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the tax info.  */  
   TaxExempt:string,
      /**  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  */  
   InAppliedLCVariance:number,
      /**  Internal usage for inclusive taxes - The total Landed Cost Amount received for this container shipment line.  */  
   InAppliedRcptLCAmt:number,
      /**  Internal usage for inclusive taxes - This is the PO Base Transaction Value plus all indirect costs which are marked to include as transaction value costs.  */  
   InExtTransValue:number,
      /**  Internal usage for inclusive taxes - The total amount of disbursed landed cost for this container detail.  This amount includes the duties and indirect costs per container shipment line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   InLCAmt:number,
      /**  Internal usage for inclusive taxes - The total Duty Amount portion of the landed cost for this container detail. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   InLCDutyAmt:number,
      /**  Internal usage for inclusive taxes - The total Indirect Cost portion of the landed cost for this container detail. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   InLCIndCost:number,
      /**  Internal usage for inclusive taxes - The total amount of disbursed landed cost for this container detail.  This amount includes the duties and indirect costs per container shipment line.The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   InLCSpecLineDutyAmt:number,
      /**  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the container shipment line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   InLCUpliftIndCost:number,
      /**  Internal usage for inclusive taxes -This is by default the PO release value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  */  
   InPOTransValue:number,
      /**  This flag determines whether any manual taxes were created for a receipt line, if this is set to True the tax engine will not calculate any receipt detail line tax information  */  
   NoTaxRecalc:boolean,
   BaseWeight:number,
   BaseWeightUOM:string,
      /**  Logical used by row rules to determine whether or not the container detail line is read only.  */  
   ContainerShipped:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  Flag to indicate if PO Trans Value can be updated.  */  
   EnableTransValue:boolean,
      /**  Flag to indicate if UpliftPercent can be updated.  */  
   EnableUplift:boolean,
      /**  Extended container detail unit cost  */  
   ExtCost:number,
   IUM:string,
      /**  Flag to indicate if LCIdCost can be manually updated.  */  
   ManualLC:boolean,
      /**  Indicates if the PO release tied to this detail entry is open or closed.  */  
   OpenPoRelease:boolean,
   PartNum:string,
   PlantName:string,
   PoLineDesc:string,
      /**  Quantity already received on this PO Release  */  
   PORelRcvdQty:number,
      /**  Remaining Qty  */  
   PORelRemQty:number,
   PUM:string,
      /**  Container Detail Shipped Date  */  
   ShipDate:string,
   SupplierPartNum:string,
      /**  The Tax Liability for the associated purchase order.  */  
   TaxRegionCode:string,
      /**  Full description of Tax Region.  */  
   TaxRegionDescription:string,
   ThisTranQty:number,
   ThisTranUOM:string,
      /**  Total dedicated Tax amount  */  
   TotDedTaxAmt:number,
      /**  Total Self Assessed Tax amount  */  
   TotSATaxAmt:number,
      /**  Total tax amount.  This is the sum of ContainerDetailTax.TaxAmt.  */  
   TotTaxAmt:number,
      /**  Logical indicates to the UI when a key field has been changed.  Set this to yes if this is the row you want the UI to find and display.  */  
   UpdatedKeyRow:boolean,
      /**  Logical indicating that a valid po number, po line and po release has been entered and the user may not update the other container detail values.  */  
   ValidPOInfoEntered:boolean,
      /**  Flag to indicate if record can be updated.  */  
   AllowUpdate:boolean,
   BaseVolume:number,
   BaseVolumeUOM:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Optional field that contains our revision. Default from the PartRev.RevisionNum field.  */  
   RevisionNum:string,
   BitFlag:number,
   CommodityDescription:string,
   ContainerHeaderContainerDescription:string,
   ContainerHeaderShipDate:string,
   CountryNumDescription:string,
   POHeaderInPrice:boolean,
   PORelBTOOrderNum:number,
   PORelBTOOrderLine:number,
   PORelRefCodeDesc:string,
   PORelPurchasingFactor:number,
   PORelXRelQty:number,
   PORelOpenRelease:boolean,
   PORelRelQty:number,
   PORelNeedByDate:string,
   PORelBTOOrderRelNum:number,
   PORelPromiseDt:string,
   PORelPurchasingFactorDirection:string,
   PORelArrivedQty:number,
   PORelDueDate:string,
   PORelPlant:string,
   TaxCatIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContainerDetailTaxRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   ContainerID:number,
      /**  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  */  
   PONum:number,
      /**  The PO line # which is being received. Only applicable for PO receipt transactions.  */  
   POLine:number,
      /**  Purchase Order Release # which is being received.  */  
   PORelNum:number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Tax Rate Code.  */  
   RateCode:string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   ECAcquisitionSeq:number,
      /**  ReportableAmt  */  
   ReportableAmt:number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   DocReportableAmt:number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   TaxableAmt:number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   DocTaxableAmt:number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   Percent:number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   TaxAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   DocTaxAmt:number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   Manual:boolean,
      /**  Userid of the user who created this record  */  
   CreatedBy:string,
      /**  Date and time when this record was created  */  
   CreatedOn:string,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  Date and time when the record was last changed.  */  
   ChangedOn:string,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
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
      /**  CollectionType  */  
   CollectionType:number,
      /**  Timing of when to report taxes  */  
   Timing:number,
      /**  Exemption Type  */  
   ExemptType:number,
      /**  Exemption Percent  */  
   ExemptPercent:number,
      /**  Resolution Number  */  
   ResolutionNum:string,
      /**  Resolution date.  */  
   ResolutionDate:string,
      /**  Date to determine the tax rate.  */  
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
      /**  Unique Identifier for Legal Text  */  
   TextCode:string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   DocTaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmtVar:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BaseCurrSymbol:string,
   CurrencyCode:string,
   CurrencySwitch:boolean,
   CurrSymbol:string,
      /**  Collection Type Description  */  
   DescCollectionType:string,
   EnableSuperGRate:string,
   Rpt1ScrDedTaxAmt:number,
   Rpt1ScrFixedAmount:number,
   Rpt1ScrReportableAmt:number,
   Rpt1ScrTaxableAmt:number,
   Rpt1ScrTaxAmt:number,
   Rpt1ScrTaxAmtVar:number,
   Rpt2ScrDedTaxAmt:number,
   Rpt2ScrFixedAmount:number,
   Rpt2ScrReportableAmt:number,
   Rpt2ScrTaxableAmt:number,
   Rpt2ScrTaxAmt:number,
   Rpt2ScrTaxAmtVar:number,
   Rpt3ScrDedTaxAmt:number,
   Rpt3ScrFixedAmount:number,
   Rpt3ScrReportableAmt:number,
   Rpt3ScrTaxableAmt:number,
   Rpt3ScrTaxAmt:number,
   Rpt3ScrTaxAmtVar:number,
   ScrDedTaxAmt:number,
   DocScrDedTaxAmt:number,
   DocScrFixedAmount:number,
   DocScrReportableAmt:number,
   DocScrTaxableAmt:number,
   DocScrTaxAmt:number,
   DocScrTaxAmtVar:number,
      /**  Display Fixed Amount in base currency.  */  
   ScrFixedAmount:number,
   ScrReportableAmt:number,
   ScrTaxableAmt:number,
   ScrTaxAmt:number,
   ScrTaxAmtVar:number,
   BitFlag:number,
   RateCodeDescription:string,
   TaxCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContainerDutyRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   ContainerID:number,
      /**  Purchase order number that uniquely identifies the purchase order on this container.  */  
   PONum:number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number on this container  */  
   POLine:number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order on this container.  */  
   PORelNum:number,
      /**  Unique Number automatically assigned which is used along with ContainerID, PONum, POLine and PORelNum to uniquely identify the Duty record within the Container Shipment Line.  */  
   DutySeq:number,
      /**  Tariff Code must be for a Preference Scheme that is linked to the Country of Origin.  */  
   TariffCode:string,
      /**   Duty Amount is calculated based on PO Release Value, Shipment Qty, Tariff Rate, Tariff Percent and Tariff Specific Amount.
Formula: (Total Shipment Qty * Tariff Rate) + (Total Shipment Value * Tariff Percent) + Specific Duty Amount  */  
   DutyAmt:number,
      /**  Container Duty Comments  */  
   CommentText:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  InDutyAmt  */  
   InDutyAmt:number,
      /**  Flag to indicate if record can be updated.  */  
   AllowUpdate:boolean,
      /**   Duty Amount is calculated based on PO Release Value, Shipment Qty, Tariff Rate, Tariff Percent and Tariff Specific Amount.
Formula: (Total Shipment Qty * Tariff Rate) + (Total Shipment Value * Tariff Percent) + Specific Duty Amount - Screen Value  */  
   ScrDutyAmt:number,
   BitFlag:number,
   POHeaderTaxRegionCode:string,
   POHeaderInPrice:boolean,
   TariffDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContainerHeaderAttchRow{
   Company:string,
   ContainerID:number,
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

export interface Erp_Tablesets_ContainerHeaderRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   ContainerID:number,
      /**  Date the container is to ship.  */  
   ShipDate:string,
      /**  Logical indicating if the container has shipped.  */  
   Shipped:boolean,
      /**  Class of this container.  Must be a valid entry in the ContainerClass master file.  */  
   ContainerClass:string,
      /**  Total cost to ship this container.  This is defaulted to the value on the ContainerClass but can be overridden by the end user. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   ContainerCost:number,
      /**   Lead time it takes for this container to reach its destination.  This is a buffer amount used to offset the shipping date to identify when a shipment is due to arrive.  For example if the shipping days is 30 and the ship date of the container is January 1, the expected arrival date of the container is January 31.

This is intiially defaulted to the value on the ContainerClass but can be overridden by the end user.  */  
   ShippingDays:number,
      /**  Notes/comments about the container shipment.  */  
   ContainerComments:string,
      /**  Free form text that describes this particular container.  */  
   ContainerDescription:string,
      /**  Determines if a new PO release is created at receipt when the quantity received is less than the quantity shipped.  The new PO Rel quantity is the difference between the ship quantity and the receipt quantity.  */  
   NewPoRelAtReceipt:boolean,
      /**  Container volume, frequently specified in cubic sq feet.  */  
   Volume:number,
      /**   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default.
Having a Volume UOM will provides the ability to calculate total volume  */  
   VolumeUOM:string,
      /**  Volume cost of the container.  This is calculated by dividing the container cost by the Volume.  */  
   CostPerVolume:number,
      /**  The container reference is typically the shipping company's assigned container ID.  */  
   ContainerReference:string,
      /**  Reference information for landed cost.  */  
   LCReference:string,
      /**  Landed Cost Comments  */  
   LCComment:string,
      /**  This field holds the variance amount for the landed costs.  */  
   LCVariance:number,
      /**  Identifies how the landed cost (container cost) was disbursed among the container details.  Valid options are Volume (default), Weight, Value and Manual.  */  
   LCDisburseMethod:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Currency Date  */  
   CurrencyDate:string,
      /**  Total cost to ship this container in the doc currency.  */  
   DocContainerCost:number,
      /**  Valid values = "Short" and "Create".   At the time a container is shipped, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the shipping quantity and a new PO release is created for the difference between the original po release quantity and the ship quantity.  This is an optional field.  */  
   PORelShipOption:string,
      /**  Reporting currency value of this field  */  
   Rpt1ContainerCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2ContainerCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3ContainerCost:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Valid Loading Port ID where goods are loaded on the vessel.  */  
   LoadPortID:string,
      /**  Valid port location where goods are unloaded.  */  
   DechargePortID:string,
      /**  Descriptive code assigned by user which uniquely identifies a shipping method (carrier) master record.  */  
   ShipViaCode:string,
      /**  Descriptive code assigned by user which uniquely identifies the fob record.  */  
   FOB:string,
      /**  Number of Containers in this shipment.  */  
   ContainerCount:number,
      /**  Number of Packages in this shipment.  */  
   PackageCount:number,
      /**  Total Weight of the shipment.  */  
   Weight:number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  */  
   WeightUOM:string,
      /**  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  */  
   UpliftPercent:number,
      /**  This key links the record to the Vendor file.  */  
   VendorNum:number,
      /**  Carrier (Supplier) Contact number.  Unique identifier for the contact record.  */  
   ConNum:number,
      /**  Bill of Lading Number  */  
   BOLading:string,
      /**  Bill of Exchange Number  */  
   BOExchange:string,
      /**  The current status of the container shipment.  Valid values are: Ordered, Shipped, Imported, Arrived and Received.  */  
   ShipStatus:string,
      /**  Valid values = "Short" and "Create".   When the container arrives, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the arrived quantity and a new PO release is created for the difference between the original po release quantity and the arrived quantity.  This is an optional field.  */  
   PORelRcptOption:string,
      /**  Stores the number of the import document.  */  
   ImportNum:string,
      /**  Name of the vessel containing the shipment.  */  
   Vessel:string,
      /**  This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the shipment lines using the line tariffs as a factor.  */  
   SpecDutyAmt:number,
      /**  The total Landed Cost Amount disbursed or applied to this container shipment.  */  
   AppliedLCAmt:number,
      /**  This is the total Duty Amount of all container shipment lines. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   ContainerDutyAmt:number,
      /**  This is the total Indirect Cost Amount of the container shipment.  The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   ContainerIndCost:number,
      /**  Flag to indicate if all of the shipment duties and indirect costs needs to be applied or disbursed.  */  
   ApplyToLC:boolean,
      /**  The date the container shipment arrived. Defaults as current system date.  */  
   ArrivedDate:string,
      /**  The date the container shipment is received. Defaults as current system date.  */  
   ReceivedDate:string,
      /**  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  */  
   PurPoint:string,
      /**  The total Landed Cost Amount received for this container shipment.  */  
   AppliedRcptLCAmt:number,
      /**  The total Uplift Indirect Cost Amount of the container shipment. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   UpliftIndCost:number,
      /**  The date that the Container Shipment is due to arrive.  */  
   DueDate:string,
      /**  This field holds the applied variance amount for the landed costs.  */  
   AppliedLCVariance:number,
      /**  Stores the Country from which the document is imported.  */  
   ImportedFrom:number,
      /**  Location description from which the document is imported.  */  
   ImportedFromDesc:string,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
      /**  The Legal Number of the record.  */  
   LegalNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  **NOT USED - REMOVE**  */  
   AdditionalShippingDays:number,
      /**  **NOT USED - Remove **  */  
   EstimatedArrivalDate:string,
      /**  Set from the earliest need by date set against the po releases.  */  
   NeedByDate:string,
      /**  Specifies the date on which the supplier has promised to deliver the container.  */  
   PromiseDate:string,
      /**  Reflects whether taxes have been calculated  */  
   TaxesCalculated:boolean,
      /**  Internal usage for inclusive taxes -The total Landed Cost Amount disbursed or applied to this container shipment.  */  
   InAppliedLCAmt:number,
      /**  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  */  
   InAppliedLCVariance:number,
      /**  Internal usage for inclusive taxes - The total Landed Cost Amount received for this container shipment.  */  
   InAppliedRcptLCAmt:number,
      /**  Internal usage for inclusive taxes - Total cost to ship this container.  This is defaulted to the value on the ContainerClass but can be overridden by the end user. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   InContainerCost:number,
      /**  Internal usage for inclusive taxes - This is the total Duty Amount of all container shipment lines. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   InContainerDutyAmt:number,
      /**  Internal usage for inclusive taxes - This is the total Indirect Cost Amount of the container shipment.  The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   InContainerIndCost:number,
      /**  Internal usage for inclusive taxes - Total cost to ship this container in the doc currency.  */  
   InDocContainerCost:number,
      /**  ** NOT USED TO BE DROPPED 10.2 **  */  
   InLCAppliedAmt:number,
      /**  Internal usage for inclusive taxes - This field holds the variance amount for the landed costs.  */  
   InLCVariance:number,
      /**  Internal usage for inclusive taxes - This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the shipment lines using the line tariffs as a factor.  */  
   InSpecDutyAmt:number,
      /**  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the container shipment. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  */  
   InUpliftIndCost:number,
      /**  ContainerID in display format.  */  
   DisplayContainerID:string,
      /**  Display Receipt Status  */  
   DispRcptStatus:string,
      /**  Display Ship Status.  */  
   DispShipStatus:string,
      /**   Flag poplulated from XbSyst.ReceiptTaxCalculate 
Determines if taxes can be calculated at update or via action menu  */  
   EnableCalcTaxes:boolean,
      /**  Flag to indicate if record can be updated after Receipt.  */  
   EnableLCAfterRcpt:boolean,
      /**  Flag to indicate if container details can be split into another container shipment.  */  
   EnableSplitContainer:boolean,
      /**  Flag to indicate if indirect costs can be transferred into another container shipment.  */  
   EnableTransferCost:boolean,
      /**  Flag to indicate if UpliftPercent should be enabled.  */  
   EnableUplift:boolean,
      /**  Logical used to indicate if all po rels for the current plant have been received.  */  
   eshReceived:boolean,
      /**  Landed Cost account for display  */  
   LCAccount:string,
      /**  Account Description  */  
   LCAccountDesc:string,
      /**  Amount of Landed Cost applied  */  
   LCAppliedAmt:number,
      /**  Landed cost message used to inform the user on retrieval of data that the applied and container costs do not equal.  */  
   LCMessage:string,
      /**  Logical indicating whether or not the container has been fully receipt.  If yes then the container has only been partially received.  */  
   PartialReceipt:boolean,
      /**  Flag to indicate that all container receipt details will be "received" automatically.  */  
   ReceiveAll:boolean,
      /**  Logical indicating whether or not on ship date change or shipping days change the po release due dates are to be upated.  */  
   ResetPORelDates:boolean,
   SkipLandedCost:boolean,
      /**  Test Import Fields "ImportNumber" and "ImportedFromDesc" to see if the Receipt Line had already non empty values for these fields and the Lot is set for this Receipt Line.  */  
   TestImportFields:boolean,
      /**  Total amount.  This is the sum of all the other total fields.  */  
   TotalAmt:number,
      /**  Total shipment value  */  
   TotalExtCost:number,
      /**  Total weight of the items shipped on the container detail.  */  
   TotalWeight:number,
      /**  Total Deductable Tax Amount  */  
   TotDedTaxAmt:number,
      /**  Total duties amount.  */  
   TotDutiesAmt:number,
      /**  Total Indirect Costs amount.  */  
   TotIndirectCostsAmt:number,
      /**  Total amount for all Container Lines  */  
   TotLinesAmt:number,
      /**  Total Self Assessed Tax Amount  */  
   TotSATaxAmt:number,
      /**  Total Tax amount.  */  
   TotTaxAmt:number,
      /**  Total WithHolding Tax Amount  */  
   TotWHTaxAmt:number,
      /**  Flag to indicate if container details need to be refreshed after changing the UpliftPercent from header.  */  
   UpdateDtlRecs:boolean,
   UpdIndCosts:boolean,
      /**  Flag to indicate if record can be updated.  */  
   AllowUpdate:boolean,
      /**   Flag poplulated from XbSyst.APTaxLnLevel.  
Determines if taxes are calculated at line level (true) or document level (false)  */  
   EnableTaxAtLineLevel:boolean,
      /**  Tax Point  */  
   TaxPoint:string,
      /**  Date Used to calculate Tax Rates  */  
   TaxRateDate:string,
      /**  Determine if the Apply Landed Cost button in Kinetic should be disabled.  */  
   DisableApplyLandedCost:boolean,
      /**  Flag to determine for Kinetic if use can leave the Container Header record/screen.  */  
   OkToLeaveContainerHead:boolean,
   BitFlag:number,
   ContainerClassDescription:string,
   DechargePortDescription:string,
   DechargePortPortID:string,
   FOBDescription:string,
   LoadPortPortID:string,
   LoadPortDescription:string,
   ShipViaCodeDescription:string,
   ShipViaCodeWebDesc:string,
   VendCntPhoneNum:string,
   VendCntName:string,
   VendCntFaxNum:string,
   VendCntEmailAddress:string,
   VendorCountry:string,
   VendorState:string,
   VendorZIP:string,
   VendorCity:string,
   VendorVendorID:string,
   VendorTermsCode:string,
   VendorName:string,
   VendorAddress3:string,
   VendorDefaultFOB:string,
   VendorAddress1:string,
   VendorCurrencyCode:string,
   VendorAddress2:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContainerHeaderTaxRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   ContainerID:number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Tax Rate Code.  */  
   RateCode:string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   ECAcquisitionSeq:number,
      /**  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcReportableAmt.  */  
   ReportableAmt:number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   DocReportableAmt:number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   TaxableAmt:number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   DocTaxableAmt:number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   Percent:number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   TaxAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   DocTaxAmt:number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   Manual:boolean,
      /**  Userid of the user who created this record  */  
   CreatedBy:string,
      /**  Date and time when this record was created  */  
   CreatedOn:string,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  Date and time when the record was last changed.  */  
   ChangedOn:string,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
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
      /**  Date to determine the tax rate.  */  
   TaxRateDate:string,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   DefTaxableAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
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
      /**  TextCode  */  
   TextCode:string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   DocTaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmtVar:number,
      /**  flag to indicate if this record is used only to total detail records,  */  
   SummaryOnly:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BaseCurrSymbol:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencySwitch:boolean,
   CurrSymbol:string,
      /**  Collection Type Description  */  
   DescCollectionType:string,
   EnableSuperGRate:boolean,
   Rpt1ScrDedTaxAmt:number,
      /**  Display field for Rpt1ScrFixedAmount  */  
   Rpt1ScrFixedAmount:number,
   Rpt1ScrReportableAmt:number,
   Rpt1ScrTaxableAmt:number,
   Rpt1ScrTaxAmt:number,
   Rpt1ScrTaxAmtVar:number,
   Rpt2ScrDedTaxAmt:number,
      /**  Display field for Rpt2FixedAmount  */  
   Rpt2ScrFixedAmount:number,
   Rpt2ScrReportableAmt:number,
   Rpt2ScrTaxableAmt:number,
   Rpt2ScrTaxAmt:number,
   Rpt2ScrTaxAmtVar:number,
   Rpt3ScrDedTaxAmt:number,
      /**  Display field for Rpt3rFixedAmount  */  
   Rpt3ScrFixedAmount:number,
   Rpt3ScrReportableAmt:number,
   Rpt3ScrTaxableAmt:number,
   Rpt3ScrTaxAmt:number,
   Rpt3ScrTaxAmtVar:number,
   ScrDedTaxAmt:number,
   ScrDocDedTaxAmt:number,
      /**  Doc Fixed Amount  */  
   ScrDocFixedAmount:number,
   ScrDocReportableAmt:number,
   ScrDocTaxableAmt:number,
   ScrDocTaxAmt:number,
   ScrDocTaxAmtVar:number,
      /**  FixedAmount  */  
   ScrFixedAmount:number,
   ScrReportableAmt:number,
   ScrTaxableAmt:number,
   ScrTaxAmt:number,
   ScrTaxAmtVar:number,
   BitFlag:number,
   RateCodeDescription:string,
   TaxCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContainerMiscRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   ContainerID:number,
      /**  Unique Number automatically assigned within the ContainerID to uniquely identify each Indirect Costs for this container shipment.  */  
   MiscSeq:number,
      /**  Miscellaneous Charge ID that is flagged for Landed Cost  */  
   MiscCode:string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  */  
   VendorNum:number,
      /**  Invoice Number from corresponding APInvMsc record.  */  
   InvoiceNum:string,
      /**  Invoice Line from corresponding APInvMsc record.  */  
   InvoiceLine:number,
      /**  The unique sequence number identifying the AP invoice miscellaneous charge.  */  
   MscNum:number,
      /**  Flag to indicate if the Indirect Cost is to be excluded from the Landed Cost calculation.  Disabled when IncTransValue is checked.  */  
   ExcludeFromLC:boolean,
      /**  Flag to indicate if the Indirect Cost is to be included in the Transaction Value (statistical value) which is used to calculate duties.  Disabled when the ExcludeFromLC is checked.  */  
   IncTransValue:boolean,
      /**  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  */  
   LCDisburseMethod:string,
      /**  Estimated Amount used in landed cost calculation if actual amount is not available.  */  
   EstimateAmt:number,
      /**  Estimated Amount in currency specified.  */  
   DocEstimateAmt:number,
      /**  Actual Amount coming from the posted AP invoice miscellaneous charge.  */  
   ActualAmt:number,
      /**  Actual Amount in currency specified.  */  
   DocActualAmt:number,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**  Container Indirect Cost Comments  */  
   CommentText:string,
      /**  Reporting currency value of the Estimated Amount.  */  
   Rpt1EstimateAmt:number,
      /**  Reporting currency value of the Estimated Amount.  */  
   Rpt2EstimateAmt:number,
      /**  Reporting currency value of the Estimated Amount.  */  
   Rpt3EstimateAmt:number,
      /**  Reporting currency value of the Actual Amount.  */  
   Rpt1ActualAmt:number,
      /**  Reporting currency value of the Actual Amount.  */  
   Rpt2ActualAmt:number,
      /**  Reporting currency value of the Actual Amount.  */  
   Rpt3ActualAmt:number,
      /**  The date that will be used to get the exchange rate if the indirect cost is not associated with an invoice miscellaneous charge.  */  
   ApplyDate:string,
      /**  Unique identifier of the currency rate group.  */  
   RateGrpCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Historical Doc Estimate Amount  */  
   DocHstEstimateAmt:number,
      /**  Historical Estimate Amount  */  
   HstEstimateAmt:number,
      /**  Historical Rpt1 Estimate Amount  */  
   Rpt1HstEstimateAmt:number,
      /**  Historical Rpt2 Estimate Amount  */  
   Rpt2HstEstimateAmt:number,
      /**  Historical Rpt3 Estimate Amount  */  
   Rpt3HstEstimateAmt:number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   Type:string,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   Percentage:number,
      /**  Indicates the Tax Category for this Indirect Cost. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  */  
   TaxCatID:string,
      /**  Indicates if the Indirect Cost is Taxable  */  
   Taxable:boolean,
      /**  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  */  
   NoTaxRecalc:boolean,
      /**  The Tax Liability for this Receipt  */  
   TaxRegionCode:string,
      /**  Internal usage for inclusive taxes - Estimated Amount used in landed cost calculation if actual amount is not available.  */  
   InEstimateAmt:number,
      /**  Internal usage for inclusive taxes - Estimated Amount in currency specified.  */  
   DocInEstimateAmt:number,
      /**  Internal usage for inclusive taxes - Reporting currency value of the Estimated Amount.  */  
   Rpt1InEstimateAmt:number,
      /**  Internal usage for inclusive taxes - Reporting currency value of the Estimated Amount.  */  
   Rpt2InEstimateAmt:number,
      /**  Internal usage for inclusive taxes - Reporting currency value of the Estimated Amount.  */  
   Rpt3InEstimateAmt:number,
      /**  Internal usage for inclusive taxes - Historical Estimate Amount  */  
   InHstEstimateAmt:number,
      /**  Internal usage for inclusive taxes - Historical Doc Estimate Amount  */  
   DocInHstEstimateAmt:number,
      /**  Internal usage for inclusive taxes - Historical Rpt1 Estimate Amount  */  
   Rpt1InHstEstimateAmt:number,
      /**  Internal usage for inclusive taxes - Historical Rpt2 Estimate Amount  */  
   Rpt2InHstEstimateAmt:number,
      /**  Internal usage for inclusive taxes - Historical Rpt3 Estimate Amount  */  
   Rpt3InHstEstimateAmt:number,
      /**  Indicates that the tax is included in the unit price  */  
   InPrice:boolean,
      /**  Flag to indicate if record can be updated.  */  
   AllowUpdate:boolean,
      /**  Currency.CurrSymbol for currency "BASE"  */  
   BaseCurrSymbol:string,
      /**  Total dedicated Tax amount.  */  
   TotDedTaxAmt:number,
      /**  Total Self Assessed Tax amount  */  
   TotSATaxAmt:number,
      /**  Total tax amount  */  
   TotTaxAmt:number,
      /**  Exchange rate that will be used for this indirect cost.  */  
   ExchangeRate:number,
      /**  Label for ExchangeRate  */  
   RateLabel:string,
      /**  Estimated Amount used in landed cost calculation if actual amount is not available - Screen Value  */  
   ScrEstimateAmt:number,
      /**  Reporting currency value of the Estimated Amount - Screen Value  */  
   Rpt1ScrEstimateAmt:number,
      /**  Reporting currency value of the Estimated Amount - Screen value  */  
   Rpt2ScrEstimateAmt:number,
      /**  Reporting currency value of the Estimated Amount - Screen value  */  
   Rpt3ScrEstimateAmt:number,
      /**  Historical Estimate Amount - Screen value  */  
   ScrHstEstimateAmt:number,
      /**  Historical Rpt1 Estimate Amount - Screen value  */  
   Rpt1ScrHstEstimateAmt:number,
      /**  Historical Rpt2 Estimate Amount - Screen value  */  
   Rpt2ScrHstEstimateAmt:number,
      /**  Historical Rpt3 Estimate Amount - Screen value  */  
   Rpt3ScrHstEstimateAmt:number,
      /**  Estimated Amount in currency specified - Screen value  */  
   DocScrEstimateAmt:number,
      /**  Estimated Amount used in landed cost calculation if actual amount is not available - Screen Value  */  
   DocScrHstEstimateAmt:number,
   BitFlag:number,
   CurrencyCurrName:string,
   CurrencyCurrSymbol:string,
   CurrencyDocumentDesc:string,
   CurrencyCurrencyID:string,
   CurrencyCurrDesc:string,
   PurMiscLCAmount:number,
   PurMiscLCCurrencyCode:string,
   PurMiscDescription:string,
   PurMiscLCDisburseMethod:string,
   RateGrpDescription:string,
   TaxCatIDDescription:string,
   TaxRegionCodeDescription:string,
   VendorCurrencyCode:string,
   VendorDefaultFOB:string,
   VendorAddress3:string,
   VendorState:string,
   VendorCity:string,
   VendorVendorID:string,
   VendorTermsCode:string,
   VendorName:string,
   VendorAddress2:string,
   VendorAddress1:string,
   VendorZIP:string,
   VendorCountry:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContainerMiscTaxRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   ContainerID:number,
      /**  Unique Number automatically assigned within the Company/VendorNum/PurPoint/PackSlip to uniquely identify each Indirect Costs for this receipt.  */  
   MiscSeq:number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Tax Rate Code.  */  
   RateCode:string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   ECAcquisitionSeq:number,
      /**  ** NOT USED TO BE DROPPED 10.2 ** The Miscellaneous Charge Code. This must be valid in the PurMisc master file.  */  
   MiscCode:string,
      /**  ReportableAmt  */  
   ReportableAmt:number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   DocReportableAmt:number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   TaxableAmt:number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   DocTaxableAmt:number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   Percent:number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   TaxAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   DocTaxAmt:number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   Manual:boolean,
      /**  Userid of the user who created this record  */  
   CreatedBy:string,
      /**  Date and time when this record was created  */  
   CreatedOn:string,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  Date and time when the record was last changed.  */  
   ChangedOn:string,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
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
      /**  CollectionType  */  
   CollectionType:number,
      /**  Timing of when to report taxes  */  
   Timing:number,
      /**  Exemption Type  */  
   ExemptType:number,
      /**  Exemption Percent  */  
   ExemptPercent:number,
      /**  Resolution Number  */  
   ResolutionNum:string,
      /**  Resolution date.  */  
   ResolutionDate:string,
      /**  Date to determine the tax rate.  */  
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
      /**  Unique Identifier for Legal Text  */  
   TextCode:string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   DocTaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmtVar:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CurrencyCode:string,
   CurrencySwitch:boolean,
   DocScrDedTaxAmt:number,
   DocScrReportableAmt:number,
   DocScrTaxableAmt:number,
   DocScrTaxAmt:number,
   DocScrTaxAmtVar:number,
   Rpt1ScrDedTaxAmt:number,
   Rpt1ScrReportableAmt:number,
   Rpt1ScrTaxableAmt:number,
   Rpt1ScrTaxAmt:number,
   Rpt1ScrTaxAmtVar:number,
   Rpt2ScrDedTaxAmt:number,
   Rpt2ScrReportableAmt:number,
   Rpt2ScrTaxableAmt:number,
   Rpt2ScrTaxAmt:number,
   Rpt2ScrTaxAmtVar:number,
   Rpt3ScrDedTaxAmt:number,
   Rpt3ScrReportableAmt:number,
   Rpt3ScrTaxableAmt:number,
   Rpt3ScrTaxAmt:number,
   Rpt3ScrTaxAmtVar:number,
   ScrDedTaxAmt:number,
   ScrReportableAmt:number,
   ScrTaxableAmt:number,
   ScrTaxAmt:number,
   ScrTaxAmtVar:number,
   Rpt1ScrFixedAmount:number,
   Rpt2ScrFixedAmount:number,
   Rpt3ScrFixedAmount:number,
   DocScrFixedAmount:number,
      /**  Display Fixed Amount in base currency.  */  
   ScrFixedAmount:number,
      /**  Collection Type Description  */  
   DescCollectionType:string,
   BitFlag:number,
   ContainerMiscApplyDate:string,
   ContainerMiscInPrice:boolean,
   ContainerMiscCurrencyCode:string,
   RateCodeDescription:string,
   TaxCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ContainerTrackingTableset{
   ContainerHeader:Erp_Tablesets_ContainerHeaderRow[],
   ContainerHeaderAttch:Erp_Tablesets_ContainerHeaderAttchRow[],
   ContainerDetail:Erp_Tablesets_ContainerDetailRow[],
   ContainerDetailAttch:Erp_Tablesets_ContainerDetailAttchRow[],
   ContainerDetailTax:Erp_Tablesets_ContainerDetailTaxRow[],
   ContainerDuty:Erp_Tablesets_ContainerDutyRow[],
   ContainerHeaderTax:Erp_Tablesets_ContainerHeaderTaxRow[],
   ContainerMisc:Erp_Tablesets_ContainerMiscRow[],
   ContainerMiscTax:Erp_Tablesets_ContainerMiscTaxRow[],
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

export interface Erp_Tablesets_MassReceiptRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID.  */  
   PurPoint:string,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  */  
   PackLine:number,
      /**   A\P invoice entry sets this to "Yes" when the receipt detail line is invoiced.  A value of NO either means that the system was not configured to 'Save Receipts for Invoicing" when the receipt line was created or that it has not yet been invoiced via A/P.
(See RcvHead.SaveForInvoicing, RcvHead.Invoiced)  */  
   Invoiced:boolean,
      /**  Our Part Number of the item that has been received. Captured from the related PODetail.PartNum for receipts of PO item. Entered by the user for miscellaneous receipts in which case it can't be blank. It must be valid in the Part file for receipt to stock.  */  
   PartNum:string,
      /**  Warehouse ID that received the item.  Only applicable for receipt to stock. Must be valid in the PartWhse file.  */  
   WareHouseCode:string,
      /**  Identifies the Bin location of the warehouse which received the item. Only applicable for a receipt of Stock.  */  
   BinNum:string,
      /**  Receipt quantity in our unit of measure.  */  
   OurQty:number,
      /**  Unit of Measure.  */  
   IUM:string,
      /**  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  */  
   OurUnitCost:number,
      /**  Job Number that received the item. Only applicable for receipt to Job.  */  
   JobNum:string,
      /**  Job Assembly Sequence # that the receipt was made against. Only applicable for receipt to job.  */  
   AssemblySeq:number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "S" = SubContract Operation (JobOper).  */  
   JobSeqType:string,
      /**  Seq # of specific material or subcontract operation record to which this receipt was made against. Only applicable for a receipt to job.  */  
   JobSeq:number,
      /**  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  */  
   PONum:number,
      /**  The PO line # which is being received. Only applicable for PO receipt transactions.  */  
   POLine:number,
      /**  Purchase Order Release # which is being received.  */  
   PORelNum:number,
      /**  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   PartDescription:string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  */  
   RevisionNum:string,
      /**  Quantity received against a purchase order in the vendors unit of measure.  */  
   VendorQty:number,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  */  
   VendorUnitCost:number,
      /**  An internal flag which indicates if this is a receipt of a Purchase Order (P) or Miscellaneous (M) item. If "P" then this record is related to a PORel record. If "M" there is no PO reference. the transaction.  */  
   ReceiptType:string,
      /**  Indicates where the item is received to. Items can be received to a Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN")  */  
   ReceivedTo:string,
      /**   Indicates if this receipt transaction should flag the related purchase order release (PORel) as being received complete (PORel.OpenRelease = No).  When the user toggles this field   Receipt entry considers it  a direct update to the PORel.OpenRelease flag.  What we mean is that the user can change the PORel.OpenRelease flag by maintaining this field on  ANY related receipt transaction for the PORel. Therefore this field should not be used to determine the true status of the PORel record.
Receipt Entry allows displays this field based on the current setting of PORel.OpenRelease field. Another point is that if the a receipt transaction is update to a different PO/Line/Release the original PORel will be reopened if there are no other receipt detail records that indicate the release is closed.  All this Open/Close logic occurs in the write trigger of RcvDtl.  */  
   ReceivedComplete:boolean,
      /**   Indicates if this receipt transaction should flag the related job material/subcontract as being issued complete. (JobMtl.IssuedComplete/JobOper.OpComplete)   When the user toggles this field Receipt entry considers it  a direct update to the job record.  What we mean is that the user can change the status of the job record by maintaining this field on  ANY related receipt transaction. Therefore this field should not be used to determine the true status of the JobMtl/JobOper record.
Receipt Entry allows displays this field based on the current status of JobMtl/JobOper field. Another point is that if the a receipt transaction is update to a different job record, the original Job record will be reopened if there are no other receipt detail records that indicate that it is complete.  All this Open/Close logic occurs in the write trigger of RcvDtl.  */  
   IssuedComplete:boolean,
      /**  Vendor's selling Unit of Measure.  */  
   PUM:string,
      /**  Vendor's Part Number. Defaulted from PODetail.  */  
   VenPartNum:string,
      /**  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  */  
   CostPerCode:string,
      /**  Lot Number  */  
   LotNum:string,
      /**  Unique dimension code for the part.  */  
   DimCode:string,
      /**  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  */  
   DUM:string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   DimConvFactor:number,
      /**  Weight  */  
   Weight:number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   WeightUOM:string,
      /**   Mtl Bur Unit cost base on our unit of measure. The mtl burden rate
defaults from the Part file.  */  
   OurMtlBurUnitCost:number,
      /**  Link to the related GLRefTyp.RefType. Not displayed.  */  
   RefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  */  
   PurchCode:string,
      /**  The total amount of disbursed landed cost for this receipt detail.  This amount includes the duties and indirect costs per receipt line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   LCAmt:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   RefDisplayAccount:string,
   DueDate:string,
   TrackDims:boolean,
   PrevRcvDtlRec:boolean,
   TrackLots:boolean,
   CostPerFactor:number,
   PConvFactor:number,
   ReceivedQty:number,
   OurIQty:number,
   OrderQty:number,
   ErrorMsg:string,
      /**  Extended Costs for Landed Costs  */  
   ExtCost:number,
      /**  Used in Landed Costs  */  
   DisburseNum:number,
   LCVariance:number,
   ExtMtlBurCost:number,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  Weight converted to the base UOM defined for the system UOM weight class.  */  
   BaseWeight:number,
      /**  The base UOM defined for the sytem UOM weight class.  */  
   BaseWeightUOM:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MassReceiptTableset{
   MassReceipt:Erp_Tablesets_MassReceiptRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PendingRcvDtlRow{
   Company:string,
   VendorNum:number,
   PurPoint:string,
   PackSlip:string,
   PONum:number,
   POLine:number,
   PORel:number,
   PartNum:string,
   LineDesc:string,
   OurQuantity:number,
   UOM:string,
   JobNum:string,
   Type:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RcvDtlAttchRow{
   Company:string,
   VendorNum:number,
   PurPoint:string,
   PackSlip:string,
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

export interface Erp_Tablesets_RcvDtlAttrValueSetRow{
      /**  Company Indentifier.  */  
   Company:string,
      /**  The internal key that is used to tie back to the Supplier master file.  */  
   VendorNum:number,
      /**  The Supplier purchase point ID.  */  
   PurPoint:string,
      /**  Supplier Packing Slip #.  */  
   PackSlip:string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  */  
   PackLine:number,
      /**  Unique identifier for this Attribute Value for this receipt detail.  */  
   AttributeValueSeq:number,
      /**  Dynamic Attribute Value Set ID for this receipt detail.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Unit of Measure.  */  
   IUM:string,
      /**  Receipt quantity in our unit of measure for this attribute set.  */  
   OurQty:number,
      /**  Indicates whether the Attribute Value was auto-generated by the system.  */  
   AutoGenerated:boolean,
      /**  Supplier selling Unit of Measure.  */  
   PUM:string,
      /**  Quantity received against a purchase order in the Supplier unit of measure.  */  
   VendorQty:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Unit of measure for the NumberOfPieces.  */  
   NumberOfPiecesUOM:string,
      /**  Indicates if the receipt is pending inspection.  Set to Yes  if InspectionReq = Yes. Set to No after receipt has been inspected.  */  
   InspectionPending:boolean,
      /**  Indicates if this receipt will be categorized as requiring inspection. It is set to Yes if any of the related Vendor, PartClass, PoDetail, JobMtl, JobOper have their RcvInspectionReq field = Yes.  */  
   InspectionReq:boolean,
      /**  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  */  
   InspectorID:string,
      /**  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  */  
   InspectedBy:string,
      /**  Date when item was inspected.  */  
   InspectedDate:string,
      /**  Time of day when inspection transaction was recorded.  */  
   InspectedTime:number,
      /**  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  */  
   PassedQty:number,
      /**  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  */  
   FailedQty:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RcvDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID.  */  
   PurPoint:string,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  */  
   PackLine:number,
      /**   A\P invoice entry sets this to "Yes" when the receipt detail line is invoiced.  A value of NO either means that the system was not configured to 'Save Receipts for Invoicing" when the receipt line was created or that it has not yet been invoiced via A/P.
(See RcvHead.SaveForInvoicing, RcvHead.Invoiced)  */  
   Invoiced:boolean,
      /**  Invoice Number on which this receipt detail was invoiced. This is updated from the A\P invoice entry process.  */  
   InvoiceNum:string,
      /**  The invoice line on which this receipt detail was invoiced. Updated by the A\P invoice entry process.  */  
   InvoiceLine:number,
      /**  Our Part Number of the item that has been received. Captured from the related PODetail.PartNum for receipts of PO item. Entered by the user for miscellaneous receipts in which case it can't be blank. It must be valid in the Part file for receipt to stock.  */  
   PartNum:string,
      /**  Warehouse ID that received the item.  Only applicable for receipt to stock. Must be valid in the PartWhse file.  */  
   WareHouseCode:string,
      /**  Identifies the Bin location of the warehouse which received the item. Only applicable for a receipt of Stock.  */  
   BinNum:string,
      /**  Receipt quantity in our unit of measure.  */  
   OurQty:number,
      /**  Unit of Measure.  */  
   IUM:string,
      /**  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  */  
   OurUnitCost:number,
      /**  Job Number that received the item. Only applicable for receipt to Job.  */  
   JobNum:string,
      /**  Job Assembly Sequence # that the receipt was made against. Only applicable for receipt to job.  */  
   AssemblySeq:number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "S" = SubContract Operation (JobOper).  */  
   JobSeqType:string,
      /**  Seq # of specific material or subcontract operation record to which this receipt was made against. Only applicable for a receipt to job.  */  
   JobSeq:number,
      /**  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  */  
   PONum:number,
      /**  The PO line # which is being received. Only applicable for PO receipt transactions.  */  
   POLine:number,
      /**  Purchase Order Release # which is being received.  */  
   PORelNum:number,
      /**  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  */  
   TranReference:string,
      /**  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   PartDescription:string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  */  
   RevisionNum:string,
      /**  Quantity received against a purchase order in the vendors unit of measure.  */  
   VendorQty:number,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  */  
   VendorUnitCost:number,
      /**  An internal flag which indicates if this is a receipt of a Purchase Order (P) or Miscellaneous (M) item. If "P" then this record is related to a PORel record. If "M" there is no PO reference. the transaction.  */  
   ReceiptType:string,
      /**  Indicates where the item is received to. Items can be received to a Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN")  */  
   ReceivedTo:string,
      /**   Indicates if this receipt transaction should flag the related purchase order release (PORel) as being received complete (PORel.OpenRelease = No).  When the user toggles this field   Receipt entry considers it  a direct update to the PORel.OpenRelease flag.  What we mean is that the user can change the PORel.OpenRelease flag by maintaining this field on  ANY related receipt transaction for the PORel. Therefore this field should not be used to determine the true status of the PORel record.
Receipt Entry allows displays this field based on the current setting of PORel.OpenRelease field. Another point is that if the a receipt transaction is update to a different PO/Line/Release the original PORel will be reopened if there are no other receipt detail records that indicate the release is closed.  All this Open/Close logic occurs in the write trigger of RcvDtl.  */  
   ReceivedComplete:boolean,
      /**   Indicates if this receipt transaction should flag the related job material/subcontract as being issued complete. (JobMtl.IssuedComplete/JobOper.OpComplete)   When the user toggles this field Receipt entry considers it  a direct update to the job record.  What we mean is that the user can change the status of the job record by maintaining this field on  ANY related receipt transaction. Therefore this field should not be used to determine the true status of the JobMtl/JobOper record.
Receipt Entry allows displays this field based on the current status of JobMtl/JobOper field. Another point is that if the a receipt transaction is update to a different job record, the original Job record will be reopened if there are no other receipt detail records that indicate that it is complete.  All this Open/Close logic occurs in the write trigger of RcvDtl.  */  
   IssuedComplete:boolean,
      /**  Vendor's selling Unit of Measure.  */  
   PUM:string,
      /**  Vendor's Part Number. Defaulted from PODetail.  */  
   VenPartNum:string,
      /**  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  */  
   CostPerCode:string,
      /**  Lot Number  */  
   LotNum:string,
      /**  Number of labels  */  
   NumLabels:number,
      /**  Unique dimension code for the part.  */  
   DimCode:string,
      /**  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  */  
   DUM:string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   DimConvFactor:number,
      /**  Indicates if this receipt will be categorized as requiring inspection. It is set to Yes if any of the related Vendor, PartClass, PoDetail, JobMtl, JobOper have their RcvInspectionReq field = Yes.  */  
   InspectionReq:boolean,
      /**   Indicates if the receipt is pending inspection.
Set to Yes  if InspectionReq = Yes. Set to No after receipt has been inspected.  */  
   InspectionPending:boolean,
      /**  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  */  
   InspectorID:string,
      /**  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  */  
   InspectedBy:string,
      /**  Date when item was inspected.  */  
   InspectedDate:string,
      /**   Time of day when inspection transaction was recorded.
(seconds since midnight format)  */  
   InspectedTime:number,
      /**  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  */  
   PassedQty:number,
      /**  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  */  
   FailedQty:number,
      /**  Receipt date. Mirror image of related RCVHead.ReceiptDate.  Maintained by the RcvHead/RcvDtl write triggers.  */  
   ReceiptDate:string,
      /**  DMRs use Reason type "D".  Only used if failing quantity from inspection.  */  
   ReasonCode:string,
      /**  Total Purchase Price Variance amount placed on a receipt in inspection when the variance is received.  Only set if the receipt is currently in inspection (not moved to DMR, job, or stock).  */  
   TotCostVariance:number,
      /**  Weight  */  
   Weight:number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   WeightUOM:string,
      /**  Indicates if the transaction is a non-conformance type transaction.  */  
   NonConformnce:boolean,
      /**  The material burden rate for this part.  */  
   MtlBurRate:number,
      /**   Mtl Bur Unit cost base on our unit of measure. The mtl burden rate
defaults from the Part file.  */  
   OurMtlBurUnitCost:number,
      /**  Link to the related GLRefTyp.RefType. Not displayed.  */  
   RefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  */  
   PurchCode:string,
      /**  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  */  
   LCFlag:boolean,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   GlbVendorNum:number,
      /**  Global Purchase Point identifier.  Used in Consolidated Purchasing.  */  
   GlbPurPoint:string,
      /**  Global Packing Slip identifier.  Used in Consolidated Purchasing.  */  
   GlbPackSlip:string,
      /**  Global Packing Slip Line identifier.  Used in Consolidated Purchasing.  */  
   GlbPackLine:number,
      /**  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  */  
   DocUnitCost:number,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   ContainerID:number,
      /**  Container volume, frequently specified in cubic sq feet.  */  
   Volume:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitCost:number,
      /**  Order Num related to the purchase order that is being received. Used only for Buy To Order POs.  */  
   OrderNum:number,
      /**  The line number of the sales order related to the purchase order that is being received. Used only for Buy To Order POs.  */  
   OrderLine:number,
      /**  The release number of the sales order line related to the purchase order that is being received. Used only for Buy To Order POs.  */  
   OrderRelNum:number,
      /**  Country Number of the Origin Country (defaults from Part Country of Origin).  */  
   OrigCountryNum:number,
      /**  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  */  
   UpliftPercent:number,
      /**  Duty Amount portion of the landed cost for this receipt line.  */  
   LCDutyAmt:number,
      /**  Indirect Cost portion of the landed cost for this receipt line.  */  
   LCIndCost:number,
      /**  This is by default the PO line value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  */  
   POTransValue:number,
      /**  This is the PO Base Transaction Value plus all indirect costs which are marked to include as transaction value costs.  */  
   ExtTransValue:number,
      /**  Flag to indicate that the receipt line has been received.  */  
   Received:boolean,
      /**  Harmonized System (HS) goods classification code.  */  
   CommodityCode:string,
      /**  Identifier of associated PO ('Std', 'CMI', 'SMI')  */  
   POType:string,
      /**  Flag representing whether or not this receipt was auto generated by the consumption process (GenSMIReceipt.p).  This is only pertinent for SMI type PO Receipts.  */  
   AutoReceipt:boolean,
      /**   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  if Part.NetVolumeUOM is not known.  */  
   VolumeUOM:string,
      /**  The date the shipment detail arrived. Defaults as current system date.  */  
   ArrivedDate:string,
      /**  This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   LCSpecLineDutyAmt:number,
      /**  The total Landed Cost Amount applied for this receipt line.  This is the actual cost that will determine the MtlBurUnitCost of the receipt transaction.  */  
   AppliedRcptLCAmt:number,
      /**  The total Uplift Indirect Cost Amount of the receipt line. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   LCUpliftIndCost:number,
      /**  The total amount of disbursed landed cost for this receipt detail.  This amount includes the duties and indirect costs per receipt line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   LCAmt:number,
      /**  This field holds the applied variance amount for the landed costs.  */  
   AppliedLCVariance:number,
      /**  Landed Cost calculated Mtl Bur Unit Cost based on our unit of measure.  The value of this field is copied to the OurMtlBurUnitCost when the Landed Cost is disbursed and applied to the receipt line.  */  
   LCMtlBurUnitCost:number,
      /**  PO currency value of this field  */  
   DocVendorUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt1VendorUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2VendorUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3VendorUnitCost:number,
      /**  Indicates if the item on the line is not compliant on its destination, that can be Inventory, Job Material, Job Subcontract, Sales Order.  */  
   NotCompliant:boolean,
      /**  Displays the cause why the item is not compliant.  */  
   ComplianceMsg:string,
      /**  This is the customer number associated with the managed customer defined in the whsebin for CMI type PO transactions.  Originally defaults from PORel.MangCustNum.  */  
   MangCustNum:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegNumCnfg.  */  
   LegalNumber:string,
      /**  Relation between this RcvDtl and the ShipHead.PackNum where this Intercompany Shipment originated.  */  
   ICPackNum:number,
      /**  Shipment Received  */  
   ShipRcv:string,
      /**  Stores the number of the import document.  Can be different from value on header.  */  
   ImportNum:string,
      /**  Stores the Country from which the document is imported.  Can be different from value on header.  */  
   ImportedFrom:number,
      /**  Location description from which the document is imported.  Can be different from Header value.  */  
   ImportedFromDesc:string,
      /**  Gross Weight  */  
   GrossWeight:number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t.  */  
   GrossWeightUOM:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  It indicates the option of what type of quantity will be able to be changed in the POLine. The actual options are "Our" and "Supplier"  */  
   QtyOption:string,
      /**  When True, the Supplier Quantity field is entered directly instead of being calculated from Our Quantity with a UOM conversion  */  
   ConvOverride:boolean,
      /**  ContractID  */  
   ContractID:string,
      /**  Used to identify what has been consumed during an SMI Receipt for a particular transaction.  */  
   SMITransNum:number,
      /**  PCID  */  
   PCID:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  Delivered  */  
   Delivered:boolean,
      /**  DeliveredComments  */  
   DeliveredComments:string,
      /**  Internal usage for inclusive taxes - Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  */  
   InOurCost:number,
      /**  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  */  
   DocInUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt1InUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2InUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3InUnitCost:number,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  */  
   InVendorUnitCost:number,
      /**  PO currency value of this field  */  
   DocInVendorUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt1InVendorUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2InVendorUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3InVendorUnitCost:number,
      /**  Value that indicates the remaining quantity of the receipt that is waiting to be invoiced.  */  
   SupplierUnInvcReceiptQty:number,
      /**  Value that indicates the un-invoiced quantity of the receipt.  */  
   OurUnInvcReceiptQty:number,
      /**  ** NOT USED TO BE DROPPED 10.2 ** The Tax Liability for this Receipt line  */  
   TaxRegionCode:string,
      /**  Indicates the Tax Category for this Receipt line. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  */  
   TaxCatID:string,
      /**  Indicates if the Receipt line is Taxable  */  
   Taxable:boolean,
      /**  Indicates if this item is exempt from tax for this receipt line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the tax info.  */  
   TaxExempt:string,
      /**  This flag determines whether any manual taxes were created for a receipt line, if this is set to True the tax engine will not calculate any receipt detail line tax information  */  
   NoTaxRecalc:boolean,
      /**  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  */  
   InAppliedLCVariance:number,
      /**  Internal usage for inclusive taxes - The total Landed Cost Amount applied for this receipt line.  This is the actual cost that will determine the MtlBurUnitCost of the receipt transaction.  */  
   InAppliedRcptLCAmt:number,
      /**  Internal usage for inclusive taxes - The total amount of disbursed landed cost for this receipt detail.  This amount includes the duties and indirect costs per receipt line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   InLCAmt:number,
      /**  Internal usage for inclusive taxes - Duty Amount portion of the landed cost for this receipt line.  */  
   InLCDutyAmt:number,
      /**  Internal usage for inclusive taxes - Indirect Cost portion of the landed cost for this receipt line.  */  
   InLCIndCost:number,
      /**  Internal usage for inclusive taxes - Landed Cost calculated Mtl Bur Unit Cost based on our unit of measure.  The value of this field is copied to the OurMtlBurUnitCost when the Landed Cost is disbursed and applied to the receipt line.  */  
   InLCMtlBurUnitCost:number,
      /**  Internal usage for inclusive taxes - This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   InLCSpecLineDutyAmt:number,
      /**  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the receipt line. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   InLCUpliftIndCost:number,
      /**  Internal usage for inclusive taxes - This is by default the PO line value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  */  
   InPOTransValue:number,
      /**  ProjProcessed  */  
   ProjProcessed:boolean,
      /**  This will contain the non deductable tax portion for this Receipt line.  This will be calculated based on the Receipt Header or Receipt Line tax records depending on the Tax Liability type and Company Tax Configuration.  */  
   ExtNonRecoverableCost:number,
      /**  Related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  AttributeBackoutRequired  */  
   AttributeBackoutRequired:boolean,
      /**  CNDeclarationBillLine  */  
   CNDeclarationBillLine:number,
      /**  Flag to indicate if landed cost info can be updated.  */  
   AllowLCUpdate:boolean,
   AsmPartDescription:string,
      /**  Consolidated PO flag.  Used in Consolidated Purchasing.  */  
   ConsolidatedPO:boolean,
      /**  This is the extended cost of the container detail item this RcvDtl entry is tied to.  */  
   ContainerExtCost:number,
      /**  Container Detail Landed Cost Amount  */  
   ContainerLCAmt:number,
   ContractOrder:boolean,
      /**  Interger value of CostPerCode  */  
   CostPerFactor:number,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  Flag to set disable/enable the InspectionReq field.  */  
   DisableInspection:boolean,
      /**  Indicates whether the IUM or DUM field should be displayed/enabled  */  
   DisplayUMField:string,
      /**  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  */  
   DocScrUnitCost:number,
      /**  PO currency value of this field  */  
   DocScrVendorUnitCost:number,
      /**  DropShipment  */  
   DropShipment:boolean,
      /**  PORel.DueDate  */  
   DueDate:string,
   EnableBin:boolean,
      /**  Indicates whether to enable/disable the dimension fields  */  
   EnableDim:boolean,
      /**  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  */  
   EnableInventoryAttributes:boolean,
   EnableLot:boolean,
      /**  Internal flag used for the row rules to control whether the PCID columns should be enabled or not.  */  
   EnablePCID:boolean,
      /**  Indicates whether to Enable the Serial Number button  */  
   EnableSN:boolean,
      /**  Use this field to enable\disable the Supplier Part XRef button  */  
   EnableSupplierXRef:boolean,
      /**  Flag to indicate if PO Trans Value can be updated.  */  
   EnableTransValue:boolean,
      /**  Flag to indicate if UpliftPercent can be updated.  */  
   EnableUplift:boolean,
   EnableWhse:boolean,
      /**  Extended receipt detail cost.  */  
   ExtCost:number,
      /**  This is true when using the Receive To PCID option in HH PO Receipt.  */  
   HHReceiveToPCID:boolean,
      /**  OurQty not divided by dimension conversion factor for entry.  */  
   InputOurQty:number,
      /**  Flag used to switch other Received To's to Pur-Ins  */  
   InspectionFlag:boolean,
      /**  Link to the IMRcvDtl table  */  
   IntQueID:number,
   JobIUM:string,
   JobPartNum:string,
   JobRequiredQty:number,
   LegalNumberMessage:string,
   MangCustID:string,
   MangCustName:string,
      /**  Flag to indicate if LCIdCost can be manually updated.  */  
   ManualLC:boolean,
      /**  Indicates if created through Mass Receipts  */  
   MassReceipt:boolean,
   OnTime:string,
   OpenRelease:boolean,
   OrderQty:number,
      /**  Our Remaining Quantity  */  
   OurRemQty:number,
      /**  Linked to the outbound container flag taken from either the PkgControlStageHeader / PkgControlHeader.  */  
   PCIDOutboundContainer:boolean,
      /**  Package Control Header Status  */  
   PkgControlStatus:string,
      /**  The Plant to which the warehouse belongs to  */  
   Plant:string,
   POComment:string,
      /**  PO Line Due Date  */  
   PODueDate:string,
   POFactor:number,
   POFactorDirection:string,
   POHold:boolean,
   POIUM:string,
   POPUM:string,
      /**  The total quantity that has arrived for this purchase order release.  */  
   PORelArrivedQty:number,
      /**  Indicates the current status of the release. This field is maintained by the System automatically. The possible values are: Open (O), Arrived (A), Inspection (I), Received (R), Closed (C), Voided (V).  */  
   PORelStatus:string,
   RcvdSMIQty:number,
      /**  PORel Received Qty for MassReceipts  */  
   ReceivedQty:number,
   RemainingSMIQty:number,
      /**  Reporting currency value of this field  */  
   Rpt1ScrUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt1ScrVendorUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2ScrUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2ScrVendorUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3ScrUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3ScrVendorUnitCost:number,
      /**  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  */  
   ScrOurUnitCost:number,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine  */  
   ScrVendorUnitCost:number,
   SearchPONum:number,
   Selected:boolean,
      /**  This boolean is set by the user in Receipt Entry to initiate the SetToLocation logic for this line.  */  
   SetToLocation:boolean,
      /**  When this flag is true, skip the Material Queue creation logic for the current RcvDtl line.  */  
   SkipMaterialQueueCreation:boolean,
   SMIComplete:boolean,
   SNStusChanged:boolean,
      /**  MtlSeq used in PrintTag option  */  
   TagMtlSeq:number,
      /**  Operation Sequence used in PrintTag  */  
   TagOprSeq:number,
   ThisTranQty:number,
   ThisTranUOM:string,
      /**  Total amount.  This is the sum of all the other total fields.  */  
   TotalAmt:number,
      /**  Total dedicated Tax amount.  */  
   TotDedTaxAmt:number,
      /**  Total duties amount.  This is the sum of RcvDtl.LCSpecLineDutyAmt + RcvDtl.LCDutyAmt  */  
   TotDutiesAmt:number,
      /**  Receipt line amount using vendor unit cost.  */  
   TotLineAmt:number,
      /**  Total Self Assessed Tax amount  */  
   TotSATaxAmt:number,
      /**  Total tax amount.  This is the sum of RcvHeadTax.TaxAmt  */  
   TotTaxAmt:number,
      /**  Total WithHolding Tax amount  */  
   TotWHTaxAmt:number,
      /**   Indicates what the item is being purchased for.  Items can be purchased for Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN").
FYI: This field indirectly sets the JobSeqType field via the write trigger. It can itself be set from the JobSeqType. System keeps them compatible. JobSeqType/TranType values are; M =PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN.  */  
   TranType:string,
   UsePurchaseCode:boolean,
   VendorCurrSymbol:string,
   VenRemQty:number,
      /**  It is true, if RcvDtl.ReceipteType = 'P' and XbSyst.AllowUpdSuppPrice is true.  */  
   AllowUpdSuppPrice:boolean,
      /**  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity.  */  
   AttributeQtyMismatch:boolean,
      /**  Indicates if the status of the PCID has changed since the receipt took place.  */  
   PCIDStatusChanged:boolean,
   CNDeclarationBill:string,
   SerialNoAttributeSetID:number,
   BitFlag:number,
   AssemblySeqDescription:string,
   BinNumDescription:string,
   CommodityDescription:string,
   CountryNumDescription:string,
   DimCodeDimCodeDescription:string,
   InspectorIDName:string,
   InvoiceNumDescription:string,
   JobNumPartDescription:string,
   PackSlipInPrice:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PartNumPartDescription:string,
   PartNumIUM:string,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   PartNumTrackLots:boolean,
   PartNumPricePerCode:string,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   PartNumAttrClassID:string,
   POLineVenPartNum:string,
   POLineLineDesc:string,
   POLinePartNum:string,
   PONumConfirmed:boolean,
   PONumApprovalStatus:string,
   PONumShipToConName:string,
   PONumShipName:string,
   PONumApprove:boolean,
   PurchCodePurchDesc:string,
   PurPointZip:string,
   PurPointState:string,
   PurPointCity:string,
   PurPointPrimPCon:number,
   PurPointAddress2:string,
   PurPointAddress3:string,
   PurPointAddress1:string,
   PurPointCountry:string,
   PurPointName:string,
   TaxCatIDDescription:string,
   VendorNumCurrencyCode:string,
   VendorNumDefaultFOB:string,
   VendorNumAddress1:string,
   VendorNumTermsCode:string,
   VendorNumState:string,
   VendorNumCountry:string,
   VendorNumZIP:string,
   VendorNumName:string,
   VendorNumVendorID:string,
   VendorNumAddress3:string,
   VendorNumAddress2:string,
   VendorNumCity:string,
   WareHouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RcvDtlTaxRow{
      /**  Company Identifier  */  
   Company:string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID.  */  
   PurPoint:string,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  */  
   PackLine:number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Tax Rate Code.  */  
   RateCode:string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   ECAcquisitionSeq:number,
      /**  ReportableAmt  */  
   ReportableAmt:number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   DocReportableAmt:number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   TaxableAmt:number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   DocTaxableAmt:number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   Percent:number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   TaxAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   DocTaxAmt:number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   Manual:boolean,
      /**  Userid of the user who created this record  */  
   CreatedBy:string,
      /**  Date and time when this record was created  */  
   CreatedOn:string,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  Date and time of the last change to this record  */  
   ChangedOn:string,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
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
      /**  CollectionType  */  
   CollectionType:number,
      /**  Timing of when to report taxes  */  
   Timing:number,
      /**  Exemption Type  */  
   ExemptType:number,
      /**  Exemption Percent  */  
   ExemptPercent:number,
      /**  Resolution Number  */  
   ResolutionNum:string,
      /**  Resolution date.  */  
   ResolutionDate:string,
      /**  Date to determine the tax rate.  */  
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
      /**  Unique Identifier for Legal Text  */  
   TextCode:string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   DocTaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmtVar:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CurrencyCode:string,
   CurrencySwitch:boolean,
   DocScrDedTaxAmt:number,
   DocScrReportableAmt:number,
   DocScrTaxableAmt:number,
   DocScrTaxAmt:number,
   DocScrTaxAmtVar:number,
   Rpt1ScrDedTaxAmt:number,
   Rpt1ScrReportableAmt:number,
   Rpt1ScrTaxableAmt:number,
   Rpt1ScrTaxAmt:number,
   Rpt1ScrTaxAmtVar:number,
   Rpt2ScrDedTaxAmt:number,
   Rpt2ScrReportableAmt:number,
   Rpt2ScrTaxableAmt:number,
   Rpt2ScrTaxAmt:number,
   Rpt2ScrTaxAmtVar:number,
   Rpt3ScrDedTaxAmt:number,
   Rpt3ScrReportableAmt:number,
   Rpt3ScrTaxableAmt:number,
   Rpt3ScrTaxAmt:number,
   Rpt3ScrTaxAmtVar:number,
   ScrDedTaxAmt:number,
   ScrReportableAmt:number,
   ScrTaxableAmt:number,
   ScrTaxAmt:number,
   ScrTaxAmtVar:number,
      /**  Document Fixed Tax Amount  */  
   DocScrFixedAmount:number,
      /**  Display Fixed Amount in base currency.  */  
   ScrFixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt1ScrFixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt2ScrFixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt3ScrFixedAmount:number,
      /**  Collection Type Description  */  
   DescCollectionType:string,
   BitFlag:number,
   RateCodeDescription:string,
   RcvDtlPONum:number,
   TaxCodeDescription:string,
   VendorCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RcvDutyRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID.  */  
   PurPoint:string,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  */  
   PackLine:number,
      /**  Unique Number automatically assigned which is used along with VendorNum, PurPoint, PackSlip and PackLine to uniquely identify the Duty record within the Receipt Line.  */  
   DutySeq:number,
      /**  Tariff Code must be for a Preference Scheme that is linked to the Country of Origin.  */  
   TariffCode:string,
      /**   Duty Amount is calculated based on PO Release Value, Shipment Qty, Tariff Rate, Tariff Percent and Tariff Specific Amount.
Formula: (Total Shipment Qty * Tariff Rate) + (Total Shipment Value * Tariff Percent) + Specific Duty Amount  */  
   DutyAmt:number,
      /**  Receipt Line Duty Comments  */  
   CommentText:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Duty Amount is calculated based on PO Release Value, Shipment Qty, Tariff Rate, Tariff Percent and Tariff Specific Amount.  */  
   InDutyAmt:number,
      /**  Flag to indicate if landed cost info can be updated.  */  
   AllowLCUpdate:boolean,
      /**   Duty Amount is calculated based on PO Release Value, Shipment Qty, Tariff Rate, Tariff Percent and Tariff Specific Amount.
Formula: (Total Shipment Qty * Tariff Rate) + (Total Shipment Value * Tariff Percent) + Specific Duty Amount  */  
   ScrDutyAmt:number,
   BitFlag:number,
   TariffDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RcvHeadAttchRow{
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

export interface Erp_Tablesets_RcvHeadListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID.  */  
   PurPoint:string,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  Receipt Date. Defaults as current system date.  */  
   ReceiptDate:string,
      /**  Person that entered the transaction. It is set to the DCD-USERID that was logged on when the record was created . This is not maintainable by the user. This is could be used as a selection parameter for reporting and browsing.  */  
   EntryPerson:string,
      /**  An internal flag that indicates this receipt document is to be saved for retrieval by A\P invoice entry. This is set based on the value stored in APSyst.SaveForInvoicing.  */  
   SaveForInvoicing:boolean,
      /**  An internal flag that indicates "ALL" the details items on this receipt document have been invoiced. This is set to "Yes" when there are no related RcvDtl records where RcvDtl.Invoiced = No. This flag along with the SaveForInvoicing flag are used to present a list of uninvoiced packing slips.  */  
   Invoiced:boolean,
      /**  Contains comments about the overall Receipt.  */  
   ReceiptComment:string,
      /**  Short name or initials of person who actually did the receiving. A totally optional field which can be used for internal reference.  */  
   ReceivePerson:string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia.  */  
   ShipViaCode:string,
      /**  The system date when this record was created.  */  
   EntryDate:string,
      /**  Site that received the goods.  */  
   Plant:string,
      /**  Purchase order number that uniquely identifies the purchase order.  */  
   PONum:number,
      /**  Reference field for Landed Costs  */  
   LCReference:string,
      /**  Comment field for Landed Costs  */  
   LCComment:string,
      /**  Total amount of landed cost spread amongst the lines.  This amount includes all duties and indirect costs of all lines.  */  
   LandedCost:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  This field holds the variance amount for the landed costs.  */  
   LCVariance:number,
      /**  Indicates if linked to a inter-company shipment  */  
   ICLinked:boolean,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   GlbVendorNum:number,
      /**  Global Purchase Point identifier.  Used in Consolidated Purchasing.  */  
   GlbPurPoint:string,
      /**  Global Packing Slip identifier.  Used in Consolidated Purchasing.  */  
   GlbPackSlip:string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   ContainerID:number,
      /**  Weight  */  
   Weight:number,
      /**  Identifies how the landed cost was disbursed among the container details.  Valid options are Volume (only for po releases tied to a container), Weight, Value and Manual.  */  
   LCDisburseMethod:string,
      /**  This is a flag representing whether or not this is a receipt that was auto generated.  It could only be true if it is associated with an SMI type PO.  */  
   AutoReceipt:boolean,
      /**  Indicates the type of transaction that created this auto receipt.  This field will only be populated if AutoReceipt = true.  */  
   AutoTranType:string,
      /**  POType Identifier of the associated PO ('Std', 'CMI', or 'SMI')  */  
   POType:string,
      /**  The unique number of the PartTran record that was the source of this transaction.  This field will only be populated if AutoReceipt = true.  */  
   AutoTranID:number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  */  
   WeightUOM:string,
      /**  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  */  
   UpliftPercent:number,
      /**  This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the receipt lines using the line tariffs as a factor.  */  
   SpecDutyAmt:number,
      /**  The total Landed Cost Amount disbursed for this receipt.  */  
   AppliedLCAmt:number,
      /**  The total Duty Amount of the entire receipt.  */  
   LCDutyAmt:number,
      /**  The total Indirect Cost Amount of the entire receipt.  */  
   LCIndCost:number,
      /**  Flag to indicate if all of the receipt duties and indirect costs needs to be applied or disbursed.  */  
   ApplyToLC:boolean,
      /**  Flag to indicate if the entire receipt has been completely received.  */  
   Received:boolean,
      /**  The date the shipment arrived. Defaults as current system date.  */  
   ArrivedDate:string,
      /**  The total Landed Cost Amount applied for this receipt.  */  
   AppliedRcptLCAmt:number,
      /**  The total Uplift Indirect Cost Amount of the receipt. The total LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and SpecDutyAmt.  */  
   LCUpliftIndCost:number,
      /**  This field holds the applied variance amount for the landed costs.  */  
   AppliedLCVariance:number,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Stores the number of the import document.  Default value for lines.  */  
   ImportNum:string,
      /**  Stores the Country from which the document is imported.  Default value for lines.  */  
   ImportedFrom:number,
      /**  Location description from which the document is imported.  Default value for lines.  */  
   ImportedFromDesc:string,
      /**  Gross Weight  */  
   GrossWeight:number,
      /**   Qualifies the unit of measure of the GrossWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t  if Part.GrossWeightUOM is not known.  */  
   GrossWeightUOM:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Address Information from Vendor or VendorPP  */  
   AddrList:string,
   LegalNumberMessage:string,
      /**  Display field used for container landed costs.  */  
   DispLandedCost:number,
      /**  This field is used to hold the original total landed cost for containers for all plants.  */  
   OrigLandedCost:number,
   POTypeDesc:string,
      /**  Flag to indicate if record can be updated.  */  
   AllowLCUpdate:boolean,
      /**  Flag to indicate if UpliftPercent should be enabled.  */  
   AllowUplift:boolean,
      /**  Flag to indicate if details need to be refreshed after changing the UpliftPercent from header.  */  
   UpdateDtlRecs:boolean,
      /**  Logical used to indicate if all details have been received.  */  
   eshReceived:boolean,
      /**  Logical indicating whether or not the receipt has been fully received.  If yes then the receipt has only been partially received.  */  
   PartialReceipt:boolean,
      /**  Landed cost message used to inform the user on retrieval of data that the applied and landed costs do not equal.  */  
   LCMessage:string,
      /**  Flag to indicate if receipt details need to be refreshed after changing the Receipt Date from header.  */  
   UpdateDtlRcptDate:boolean,
      /**  Flag to indicate if receipt details need to be refreshed after changing the Arrival Date from header.  */  
   UpdateDtlArvdDate:boolean,
   PurPointState:string,
   PurPointPrimPCon:number,
   PurPointAddress1:string,
   PurPointCity:string,
   PurPointCountry:string,
   PurPointAddress3:string,
   PurPointAddress2:string,
   PurPointZip:string,
   PurPointName:string,
   ShipViaCodeDescription:string,
   ShipViaCodeWebDesc:string,
   VendorNumTermsCode:string,
   VendorNumCountry:string,
   VendorNumAddress1:string,
   VendorNumZIP:string,
   VendorNumCurrencyCode:string,
   VendorNumName:string,
   VendorNumDefaultFOB:string,
   VendorNumAddress2:string,
   VendorNumState:string,
   VendorNumAddress3:string,
   VendorNumCity:string,
   VendorNumVendorID:string,
   vrPONumShipToConName:string,
   vrPONumShipName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RcvHeadListTableset{
   RcvHeadList:Erp_Tablesets_RcvHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_RcvHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID.  */  
   PurPoint:string,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  Receipt Date. Defaults as current system date.  */  
   ReceiptDate:string,
      /**  Person that entered the transaction. It is set to the DCD-USERID that was logged on when the record was created . This is not maintainable by the user. This is could be used as a selection parameter for reporting and browsing.  */  
   EntryPerson:string,
      /**  An internal flag that indicates this receipt document is to be saved for retrieval by A\P invoice entry. This is set based on the value stored in APSyst.SaveForInvoicing.  */  
   SaveForInvoicing:boolean,
      /**  An internal flag that indicates "ALL" the details items on this receipt document have been invoiced. This is set to "Yes" when there are no related RcvDtl records where RcvDtl.Invoiced = No. This flag along with the SaveForInvoicing flag are used to present a list of uninvoiced packing slips.  */  
   Invoiced:boolean,
      /**  Contains comments about the overall Receipt.  */  
   ReceiptComment:string,
      /**  Short name or initials of person who actually did the receiving. A totally optional field which can be used for internal reference.  */  
   ReceivePerson:string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia.  */  
   ShipViaCode:string,
      /**  The system date when this record was created.  */  
   EntryDate:string,
      /**  Site that received the goods.  */  
   Plant:string,
      /**  Purchase order number that uniquely identifies the purchase order.  */  
   PONum:number,
      /**  Reference field for Landed Costs  */  
   LCReference:string,
      /**  Comment field for Landed Costs  */  
   LCComment:string,
      /**  Total amount of landed cost spread amongst the lines.  This amount includes all duties and indirect costs of all lines.  */  
   LandedCost:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  This field holds the variance amount for the landed costs.  */  
   LCVariance:number,
      /**  Indicates if linked to a inter-company shipment  */  
   ICLinked:boolean,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   GlbVendorNum:number,
      /**  Global Purchase Point identifier.  Used in Consolidated Purchasing.  */  
   GlbPurPoint:string,
      /**  Global Packing Slip identifier.  Used in Consolidated Purchasing.  */  
   GlbPackSlip:string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   ContainerID:number,
      /**  Weight  */  
   Weight:number,
      /**  Identifies how the landed cost was disbursed among the container details.  Valid options are Volume (only for po releases tied to a container), Weight, Value and Manual.  */  
   LCDisburseMethod:string,
      /**  This is a flag representing whether or not this is a receipt that was auto generated.  It could only be true if it is associated with an SMI type PO.  */  
   AutoReceipt:boolean,
      /**  Indicates the type of transaction that created this auto receipt.  This field will only be populated if AutoReceipt = true.  */  
   AutoTranType:string,
      /**  POType Identifier of the associated PO ('Std', 'CMI', or 'SMI')  */  
   POType:string,
      /**  The unique number of the PartTran record that was the source of this transaction.  This field will only be populated if AutoReceipt = true.  */  
   AutoTranID:number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  */  
   WeightUOM:string,
      /**  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  */  
   UpliftPercent:number,
      /**  This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the receipt lines using the line tariffs as a factor.  */  
   SpecDutyAmt:number,
      /**  The total Landed Cost Amount disbursed for this receipt.  */  
   AppliedLCAmt:number,
      /**  The total Duty Amount of the entire receipt.  */  
   LCDutyAmt:number,
      /**  The total Indirect Cost Amount of the entire receipt.  */  
   LCIndCost:number,
      /**  Flag to indicate if all of the receipt duties and indirect costs needs to be applied or disbursed.  */  
   ApplyToLC:boolean,
      /**  Flag to indicate if the entire receipt has been completely received.  */  
   Received:boolean,
      /**  The date the shipment arrived. Defaults as current system date.  */  
   ArrivedDate:string,
      /**  The total Landed Cost Amount applied for this receipt.  */  
   AppliedRcptLCAmt:number,
      /**  The total Uplift Indirect Cost Amount of the receipt. The total LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and SpecDutyAmt.  */  
   LCUpliftIndCost:number,
      /**  This field holds the applied variance amount for the landed costs.  */  
   AppliedLCVariance:number,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Stores the number of the import document.  Default value for lines.  */  
   ImportNum:string,
      /**  Stores the Country from which the document is imported.  Default value for lines.  */  
   ImportedFrom:number,
      /**  Location description from which the document is imported.  Default value for lines.  */  
   ImportedFromDesc:string,
      /**  Gross Weight  */  
   GrossWeight:number,
      /**   Qualifies the unit of measure of the GrossWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t  if Part.GrossWeightUOM is not known.  */  
   GrossWeightUOM:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  The Tax Liability for this Receipt  */  
   TaxRegionCode:string,
      /**  Tax Point  */  
   TaxPoint:string,
      /**  Date Used to calculate Tax Rates  */  
   TaxRateDate:string,
      /**  Indicates that the tax is included in the unit price  */  
   InPrice:boolean,
      /**  ** NOT USED TO BE DROPPED 10.2 ** This flag determines whether any manual taxes were created for a header miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  */  
   HdrTaxNoUpdt:boolean,
      /**  Tax Rate Group Code - FUTUREUSE  */  
   TaxRateGrpCode:string,
      /**  The flag indicates that taxes have been calculated.  Once the flag is true is should never be changed back to false.  This will be set to true when any receipt line is marked as received, or when taxes have been calculated via the Calculate All Taxes menu option.  */  
   TaxesCalculated:boolean,
      /**  Internal usage for inclusive taxes - The total Landed Cost Amount disbursed for this receipt.  */  
   InAppliedLCAmt:number,
      /**  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  */  
   InAppliedLCVariance:number,
      /**  Internal usage for inclusive taxes - The total Landed Cost Amount applied for this receipt.  */  
   InAppliedRcptLCAmt:number,
      /**  Internal usage for inclusive taxes - Total amount of landed cost spread amongst the lines.  This amount includes all duties and indirect costs of all lines.  */  
   InLandedCost:number,
      /**  Internal usage for inclusive taxes - The total Duty Amount of the entire receipt.  */  
   InLCDutyAmt:number,
      /**  Internal usage for inclusive taxes - The total Indirect Cost Amount of the entire receipt.  */  
   InLCIndCost:number,
      /**  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the receipt. The total LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and SpecDutyAmt.  */  
   InLCUpliftIndCost:number,
      /**  Internal usage for inclusive taxes - This field holds the variance amount for the landed costs.  */  
   InLCVariance:number,
      /**  Internal usage for inclusive taxes - This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the receipt lines using the line tariffs as a factor.  */  
   InSpecDutyAmt:number,
      /**  Declaration Bill  */  
   CNDeclarationBill:string,
      /**  Bonded  */  
   CNBonded:boolean,
      /**  APTaxRoundOption  */  
   APTaxRoundOption:number,
      /**  Address Information from Vendor or VendorPP  */  
   AddrList:string,
      /**  Logical indicating whether or not the receipt has been fully received.  If yes then the receipt has only been partially received.  */  
   PartialReceipt:boolean,
   POLine:number,
   PORel:number,
   POTypeDesc:string,
   ShipViaDesc:string,
      /**  Total amount.  This is the sum of all the other total fields.  */  
   TotalAmt:number,
      /**  Total dedicated Tax amount.  */  
   TotDedTaxAmt:number,
      /**  Total duties amount.  This is the sum of RcvHead.SpecDutyAmt + RcvHead.LCDutyAmt  */  
   TotDutiesAmt:number,
      /**  Total Gross Weight of all receipt lines  */  
   TotGrossWeight:number,
      /**  Qualifies the unit of measure of the Gross Weight field.  */  
   TotGrossWeightUOM:string,
      /**  Total Indirect Costs amount.  This is a sum of all RcvMisc.ActualAmt.  */  
   TotIndirectCostsAmt:number,
      /**  Total amount for all receipt lines.  This is the sum of RcvDtl.POTransValue.  */  
   TotLinesAmt:number,
      /**  Total Self Assessed Tax amount  */  
   TotSATaxAmt:number,
      /**  Total tax amount.  This is the sum of RcvHeadTax.TaxAmt  */  
   TotTaxAmt:number,
      /**  Total Weight of all receipt lines  */  
   TotWeight:number,
      /**  Qualifies the unit of measure of the Weight field.  */  
   TotWeightUOM:string,
      /**  Total WithHolding Tax amount  */  
   TotWHTaxAmt:number,
      /**  Flag to indicate if receipt details need to be refreshed after changing the Arrival Date from header.  */  
   UpdateDtlArvdDate:boolean,
      /**  Flag to indicate if receipt details need to be refreshed after changing the Receipt Date from header.  */  
   UpdateDtlRcptDate:boolean,
      /**  Flag to indicate if details need to be refreshed after changing the UpliftPercent from header.  */  
   UpdateDtlRecs:boolean,
      /**  Flag to indicate if record can be updated.  */  
   AllowLCUpdate:boolean,
      /**  Flag to indicate if UpliftPercent should be enabled.  */  
   AllowUplift:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Display field used for container landed costs.  */  
   DispLandedCost:number,
      /**  Logical used to indicate if all details have been received.  */  
   eshReceived:boolean,
   IntQueID:number,
      /**  Landed cost message used to inform the user on retrieval of data that the applied and landed costs do not equal.  */  
   LCMessage:string,
   LegalNumberMessage:string,
      /**  This field is used to hold the original total landed cost for containers for all plants.  */  
   OrigLandedCost:number,
      /**  The formatted address Information from Vendor or VendorPP  */  
   AddrListFormatted:string,
   BitFlag:number,
   PurPointName:string,
   PurPointCountry:string,
   PurPointState:string,
   PurPointAddress3:string,
   PurPointAddress1:string,
   PurPointPrimPCon:number,
   PurPointAddress2:string,
   PurPointCity:string,
   PurPointZip:string,
   ShipViaCodeWebDesc:string,
   ShipViaCodeDescription:string,
   TaxRegionCodeDescription:string,
   VendorNumState:string,
   VendorNumTermsCode:string,
   VendorNumVendorID:string,
   VendorNumAddress2:string,
   VendorNumCity:string,
   VendorNumDefaultFOB:string,
   VendorNumCurrencyCode:string,
   VendorNumName:string,
   VendorNumZIP:string,
   VendorNumCountry:string,
   VendorNumAddress3:string,
   VendorNumAddress1:string,
   vrPONumCNBonded:boolean,
   vrPONumShipToConName:string,
   vrPONumShipName:string,
   XbSystReceiptTaxCalculate:boolean,
   XbSystAPTaxLnLevel:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RcvHeadTaxRow{
      /**  Company Identifier  */  
   Company:string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID.  */  
   PurPoint:string,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Tax Rate Code.  */  
   RateCode:string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   ECAcquisitionSeq:number,
      /**  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcReportableAmt.  */  
   ReportableAmt:number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   DocReportableAmt:number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   TaxableAmt:number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   DocTaxableAmt:number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   Percent:number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   TaxAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   DocTaxAmt:number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   Manual:boolean,
      /**  Userid of the user who created this record  */  
   CreatedBy:string,
      /**  Date and time when this record was created  */  
   CreatedOn:string,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  Date and time of the last change to this record  */  
   ChangedOn:string,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
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
      /**  Date to determine the tax rate.  */  
   TaxRateDate:string,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   DefTaxableAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
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
      /**  TextCode  */  
   TextCode:string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   DocTaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmtVar:number,
      /**  flag to indicate if this record is used only to total detail records,  */  
   SummaryOnly:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BaseCurrSymbol:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencySwitch:boolean,
   CurrSymbol:string,
      /**  Collection Type Description  */  
   DescCollectionType:string,
   EnableSuperGRate:boolean,
   Rpt1ScrDedTaxAmt:number,
      /**  Display field for Rpt1ScrFixedAmount  */  
   Rpt1ScrFixedAmount:number,
   Rpt1ScrReportableAmt:number,
   Rpt1ScrTaxableAmt:number,
   Rpt1ScrTaxAmt:number,
   Rpt1ScrTaxAmtVar:number,
   Rpt2ScrDedTaxAmt:number,
      /**  Display field for Rpt2FixedAmount  */  
   Rpt2ScrFixedAmount:number,
   Rpt2ScrReportableAmt:number,
   Rpt2ScrTaxableAmt:number,
   Rpt2ScrTaxAmt:number,
   Rpt2ScrTaxAmtVar:number,
   Rpt3ScrDedTaxAmt:number,
      /**  Display field for Rpt3rFixedAmount  */  
   Rpt3ScrFixedAmount:number,
   Rpt3ScrReportableAmt:number,
   Rpt3ScrTaxableAmt:number,
   Rpt3ScrTaxAmt:number,
   Rpt3ScrTaxAmtVar:number,
   ScrDedTaxAmt:number,
   ScrDocDedTaxAmt:number,
      /**  Doc Fixed Amount  */  
   ScrDocFixedAmount:number,
   ScrDocReportableAmt:number,
   ScrDocTaxableAmt:number,
   ScrDocTaxAmt:number,
   ScrDocTaxAmtVar:number,
      /**  FixedAmount  */  
   ScrFixedAmount:number,
   ScrReportableAmt:number,
   ScrTaxableAmt:number,
   ScrTaxAmt:number,
   ScrTaxAmtVar:number,
   BitFlag:number,
   RateCodeDescription:string,
   TaxCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RcvMiscRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID.  */  
   PurPoint:string,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  Unique Number automatically assigned within the Company/VendorNum/PurPoint/PackSlip to uniquely identify each Indirect Costs for this receipt.  */  
   MiscSeq:number,
      /**  Miscellaneous Charge ID that is flagged for Landed Cost  */  
   MiscCode:string,
      /**  Flag to indicate if the Indirect Cost is to be excluded from the Landed Cost calculation.  Disabled when IncTransValue is checked.  */  
   ExcludeFromLC:boolean,
      /**  Flag to indicate if the Indirect Cost is to be included in the Transaction Value (statistical value) which is used to calculate duties.  Disabled when the ExcludeFromLC is checked.  */  
   IncTransValue:boolean,
      /**  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  */  
   LCDisburseMethod:string,
      /**  Actual Miscellaneous Charge Amount.  */  
   ActualAmt:number,
      /**  Actual Miscellaneous Charge Amount in the currency specified.  */  
   DocActualAmt:number,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**  Receipt Indirect Cost Comments  */  
   CommentText:string,
      /**  Reporting currency value of the Actual Amount.  */  
   Rpt1ActualAmt:number,
      /**  Reporting currency value of the Actual Amount.  */  
   Rpt2ActualAmt:number,
      /**  Reporting currency value of the Actual Amount.  */  
   Rpt3ActualAmt:number,
      /**  The date that will be used to get the exchange rate if the indirect cost is not associated with an invoice miscellaneous charge.  */  
   ApplyDate:string,
      /**  Unique identifier of the currency rate group.  */  
   RateGrpCode:string,
      /**  Invoice Number from corresponding APInvMsc record.  */  
   InvoiceNum:string,
      /**  Invoice Line from corresponding APInvMsc record.  */  
   InvoiceLine:number,
      /**  The unique sequence number identifying the AP invoice miscellaneous charge.  */  
   MscNum:number,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   Percentage:number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   Type:string,
      /**  VendorNum duplicated from the corresponding APInvHed record.  Not directly maintainable by the operator.  */  
   APInvVendorNum:number,
      /**  Reference to RcvDtl.PackLine. An integer that uniquely identifies a detail record within a Packing slip.  */  
   PackLine:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates the Tax Category for this Receipt Misc. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  */  
   TaxCatID:string,
      /**  Indicates if the Indirect Cost is taxable  */  
   Taxable:boolean,
      /**  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  */  
   NoTaxRecalc:boolean,
      /**  Actual Miscellaneous Charge Amount.  */  
   InActualAmt:number,
      /**  Actual Miscellaneous Charge Amount in the currency specified.  */  
   DocInActualAmt:number,
      /**  Reporting currency value of the Actual Amount.  */  
   Rpt1InActualAmt:number,
      /**  Reporting currency value of the Actual Amount.  */  
   Rpt2InActualAmt:number,
      /**  Reporting currency value of the Actual Amount.  */  
   Rpt3InActualAmt:number,
      /**  Exchange rate that will be used for this indirect cost.  */  
   ExchangeRate:number,
      /**  Label for the exchange rate  */  
   RateLabel:string,
      /**  Total dedicated Tax amount.  */  
   TotDedTaxAmt:number,
      /**  Total Self Assessed Tax amount  */  
   TotSATaxAmt:number,
      /**  Total tax amount  */  
   TotTaxAmt:number,
      /**  Flag to indicate if landed cost info can be updated.  */  
   AllowLCUpdate:boolean,
      /**  Currency.CurrSymbol for currency "BASE"  */  
   BaseCurrSymbol:string,
      /**  Actual Miscellaneous Charge Amount - Screen value.  */  
   ScrActualAmt:number,
      /**  Reporting currency value of the Actual Amount - Screen value.  */  
   Rpt1ScrActualAmt:number,
      /**  Reporting currency value of the Actual Amount - Screen value.  */  
   Rpt2ScrActualAmt:number,
      /**  Reporting currency value of the Actual Amount - Screen value  */  
   Rpt3ScrActualAmt:number,
      /**  Actual Miscellaneous Charge Amount in the currency specified - Screen value  */  
   DocScrActualAmt:number,
   BitFlag:number,
   APInvVendorName:string,
   APInvVendorVendorID:string,
   CurrencyCurrSymbol:string,
   CurrencyCurrencyID:string,
   CurrencyDocumentDesc:string,
   CurrencyCurrDesc:string,
   CurrencyCurrName:string,
   PurMiscLCDisburseMethod:string,
   PurMiscLCCurrencyCode:string,
   PurMiscDescription:string,
   PurMiscLCAmount:number,
   RateGrpDescription:string,
   RcvHeadReceiptDate:string,
   RcvHeadInPrice:boolean,
   TaxCatIDDescription:string,
   VendorName:string,
   VendorVendorID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RcvMiscTaxRow{
      /**  Company Identifier  */  
   Company:string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID.  */  
   PurPoint:string,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  Unique Number automatically assigned within the Company/VendorNum/PurPoint/PackSlip to uniquely identify each Indirect Costs for this receipt.  */  
   MiscSeq:number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Tax Rate Code.  */  
   RateCode:string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   ECAcquisitionSeq:number,
      /**  ** NOT USED TO BE DROPPED 10.2 ** Miscellaneous Charge ID that is flagged for Landed Cost  */  
   MiscCode:string,
      /**  ReportableAmt  */  
   ReportableAmt:number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   DocReportableAmt:number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   TaxableAmt:number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   DocTaxableAmt:number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   Percent:number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   TaxAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   DocTaxAmt:number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   Manual:boolean,
      /**  Userid of the user who created this record  */  
   CreatedBy:string,
      /**  Date and time when this record was created  */  
   CreatedOn:string,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  Date and time of the last change to this record  */  
   ChangedOn:string,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
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
      /**  CollectionType  */  
   CollectionType:number,
      /**  Timing of when to report taxes  */  
   Timing:number,
      /**  Exemption Type  */  
   ExemptType:number,
      /**  Exemption Percent  */  
   ExemptPercent:number,
      /**  Resolution Number  */  
   ResolutionNum:string,
      /**  Resolution date.  */  
   ResolutionDate:string,
      /**  Date to determine the tax rate.  */  
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
      /**  Unique Identifier for Legal Text  */  
   TextCode:string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   DocTaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmtVar:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CurrencyCode:string,
   CurrencySwitch:boolean,
   DocScrDedTaxAmt:number,
   DocScrReportableAmt:number,
   DocScrTaxableAmt:number,
   DocScrTaxAmt:number,
   DocScrTaxAmtVar:number,
   Rpt1ScrDedTaxAmt:number,
   Rpt1ScrReportableAmt:number,
   Rpt1ScrTaxableAmt:number,
   Rpt1ScrTaxAmt:number,
   Rpt1ScrTaxAmtVar:number,
   Rpt2ScrDedTaxAmt:number,
   Rpt2ScrReportableAmt:number,
   Rpt2ScrTaxableAmt:number,
   Rpt2ScrTaxAmt:number,
   Rpt2ScrTaxAmtVar:number,
   Rpt3ScrDedTaxAmt:number,
   Rpt3ScrReportableAmt:number,
   Rpt3ScrTaxableAmt:number,
   Rpt3ScrTaxAmt:number,
   Rpt3ScrTaxAmtVar:number,
   ScrDedTaxAmt:number,
   ScrReportableAmt:number,
   ScrTaxableAmt:number,
   ScrTaxAmt:number,
   ScrTaxAmtVar:number,
      /**  Collection Type Description  */  
   DescCollectionType:string,
      /**  Display Fixed Amount in base currency.  */  
   ScrFixedAmount:number,
      /**  Document Fixed Tax Amount  */  
   DocScrFixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt1ScrFixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt2ScrFixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt3ScrFixedAmount:number,
   BitFlag:number,
   RateCodeDescription:string,
   RcvMiscCurrencyCode:string,
   TaxCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ReceiptTableset{
   RcvHead:Erp_Tablesets_RcvHeadRow[],
   RcvHeadAttch:Erp_Tablesets_RcvHeadAttchRow[],
   RcvHeadTax:Erp_Tablesets_RcvHeadTaxRow[],
   RcvDtl:Erp_Tablesets_RcvDtlRow[],
   RcvDtlAttch:Erp_Tablesets_RcvDtlAttchRow[],
   RcvDtlAttrValueSet:Erp_Tablesets_RcvDtlAttrValueSetRow[],
   RcvDtlTax:Erp_Tablesets_RcvDtlTaxRow[],
   RcvDuty:Erp_Tablesets_RcvDutyRow[],
   RcvMisc:Erp_Tablesets_RcvMiscRow[],
   RcvMiscTax:Erp_Tablesets_RcvMiscTaxRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   PendingRcvDtl:Erp_Tablesets_PendingRcvDtlRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   SupplierXRef:Erp_Tablesets_SupplierXRefRow[],
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

export interface Erp_Tablesets_SupplierXRefRow{
   Company:string,
   MfgID:string,
   MfgName:string,
   MfgNum:number,
   MfgPartNum:string,
   PartNum:string,
   POReference:boolean,
   Receipt:boolean,
   VendNum:number,
   VendPartNum:string,
   Invoice:boolean,
      /**  RcvXRefNum  */  
   RcvXRefNum:number,
   Inspected:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtReceiptTableset{
   RcvHead:Erp_Tablesets_RcvHeadRow[],
   RcvHeadAttch:Erp_Tablesets_RcvHeadAttchRow[],
   RcvHeadTax:Erp_Tablesets_RcvHeadTaxRow[],
   RcvDtl:Erp_Tablesets_RcvDtlRow[],
   RcvDtlAttch:Erp_Tablesets_RcvDtlAttchRow[],
   RcvDtlAttrValueSet:Erp_Tablesets_RcvDtlAttrValueSetRow[],
   RcvDtlTax:Erp_Tablesets_RcvDtlTaxRow[],
   RcvDuty:Erp_Tablesets_RcvDutyRow[],
   RcvMisc:Erp_Tablesets_RcvMiscRow[],
   RcvMiscTax:Erp_Tablesets_RcvMiscTaxRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   PendingRcvDtl:Erp_Tablesets_PendingRcvDtlRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   SupplierXRef:Erp_Tablesets_SupplierXRefRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param poNum
   */  
export interface ExistsRcvHeadWithDifferentPO_input{
   vendorNum:number,
   purPoint:string,
   packSlip:string,
   poNum:number,
}

export interface ExistsRcvHeadWithDifferentPO_output{
   returnObj:boolean,
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param poNum
   */  
export interface ExistsRcvHead_input{
   vendorNum:number,
   purPoint:string,
   packSlip:string,
      /**  PO Number  */  
   poNum:number,
}

export interface ExistsRcvHead_output{
parameters : {
      /**  output parameters  */  
   warning:string,
}
}

export interface GetAvailTranDocTypes_output{
parameters : {
      /**  output parameters  */  
   listAvailTranDocTypes:string,
}
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
   returnObj:Erp_Tablesets_ReceiptTableset[],
}

   /** Required : 
      @param piVendorNum
      @param pcPurPoint
      @param pcPackSlip
      @param piPONum
   */  
export interface GetByIdChkContainerID_input{
      /**  The vendor for the selected PO.  */  
   piVendorNum:number,
      /**  The purchase point for the selected PO  */  
   pcPurPoint:string,
      /**  The pack slip selected by the user  */  
   pcPackSlip:string,
      /**  The PO number selected by the user  */  
   piPONum:number,
}

export interface GetByIdChkContainerID_output{
   returnObj:Erp_Tablesets_ReceiptTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ReceiptTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ReceiptTableset[],
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
      @param containerID
   */  
export interface GetContainerReceiptPartTranPKs_input{
      /**  The Container Landed Cost ID  */  
   containerID:number,
}

export interface GetContainerReceiptPartTranPKs_output{
parameters : {
      /**  output parameters  */  
   partTranPKs:string,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
   */  
export interface GetDtlAssemblyInfo_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
}

export interface GetDtlAssemblyInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param jobNum
      @param ds
   */  
export interface GetDtlJobInfo_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  The new Job Number  */  
   jobNum:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface GetDtlJobInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param lotNum
   */  
export interface GetDtlLotInfo_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  New Lot Number to validate  */  
   lotNum:string,
}

export interface GetDtlLotInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
   questionMsg:string,
   errorMsg:string,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param poNum
      @param requiresUserInput
   */  
export interface GetDtlPOInfo_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  New PO Number  */  
   poNum:number,
      /**  Verifies if User Input is required  */  
   requiresUserInput:boolean,
}

export interface GetDtlPOInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
   poStatusQstnMsg:string,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param poLine
   */  
export interface GetDtlPOLineInfo_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  New POLine Number  */  
   poLine:number,
}

export interface GetDtlPOLineInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
   serialWarning:string,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param poRelNum
   */  
export interface GetDtlPORelInfo_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  New PO Release Number  */  
   poRelNum:number,
}

export interface GetDtlPORelInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param partNum
      @param SysRowID
      @param rowType
   */  
export interface GetDtlPartInfo_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  Proposed partNum value  */  
   partNum:string,
      /**  SysRowID of found row typically from multiple matches  */  
   SysRowID:string,
      /**  FindPart match record  */  
   rowType:string,
}

export interface GetDtlPartInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
   partNum:string,
   multipleMatch:boolean,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param inputOurQty
      @param inputIUM
      @param whichField
   */  
export interface GetDtlQtyInfo_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  Proposed change to the Input qty field  */  
   inputOurQty:number,
      /**  Proposed change to the IUM field  */  
   inputIUM:string,
      /**  Indicates either 'QTY' or 'UOM' field changed  */  
   whichField:string,
}

export interface GetDtlQtyInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
   warnMsg:string,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param rcvdTo
   */  
export interface GetDtlRcvdToInfo_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  Proposed ReceivedTo value  */  
   rcvdTo:string,
}

export interface GetDtlRcvdToInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
   rcvdTo:string,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param jobSeq
   */  
export interface GetDtlSeqInfo_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  Vendor Number  */  
   vendorNum:number,
      /**  Purchase Point  */  
   purPoint:string,
      /**  Packing slip number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  Proposed JobSeq change  */  
   jobSeq:number,
}

export interface GetDtlSeqInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
   serialWarning:string,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param vendorQty
   */  
export interface GetDtlVenQtyInfo_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  Vendor Number  */  
   vendorNum:number,
      /**  Purchase Point  */  
   purPoint:string,
      /**  Packing slip number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  Proposed VendorQty value  */  
   vendorQty:number,
}

export interface GetDtlVenQtyInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
   warnMsg:string,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
   */  
export interface GetExistingRcvHead_input{
   ds:Erp_Tablesets_ReceiptTableset[],
   vendorNum:number,
   purPoint:string,
   packSlip:string,
}

export interface GetExistingRcvHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param whereClauseRcvDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetListReceipts_input{
   whereClauseRcvDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetListReceipts_output{
   returnObj:Erp_Tablesets_ReceiptTableset[],
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
   returnObj:Erp_Tablesets_RcvHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param inPartNum
      @param inLotNum
   */  
export interface GetLotImportInfo_input{
      /**  PartNum  */  
   inPartNum:string,
      /**  LotNum  */  
   inLotNum:string,
}

export interface GetLotImportInfo_output{
parameters : {
      /**  output parameters  */  
   outImportNum:string,
   outImportedFromDesc:string,
}
}

   /** Required : 
      @param company
      @param pcid
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param tranType
   */  
export interface GetMtlQueueSeqValue_input{
   company:string,
   pcid:string,
   vendorNum:number,
   purPoint:string,
   packSlip:string,
   packLine:number,
   tranType:string,
}

export interface GetMtlQueueSeqValue_output{
   returnObj:number,
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
   */  
export interface GetNewRcvDtlAttch_input{
   ds:Erp_Tablesets_ReceiptTableset[],
   vendorNum:number,
   purPoint:string,
   packSlip:string,
   packLine:number,
}

export interface GetNewRcvDtlAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
   */  
export interface GetNewRcvDtlAttrValueSet_input{
   ds:Erp_Tablesets_ReceiptTableset[],
   vendorNum:number,
   purPoint:string,
   packSlip:string,
   packLine:number,
}

export interface GetNewRcvDtlAttrValueSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
      @param VendorNum
      @param PurPoint
      @param PackSlip
   */  
export interface GetNewRcvDtlMisc_input{
   ds:Erp_Tablesets_ReceiptTableset[],
   VendorNum:number,
   PurPoint:string,
   PackSlip:string,
}

export interface GetNewRcvDtlMisc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param taxCode
      @param rateCode
   */  
export interface GetNewRcvDtlTax_input{
   ds:Erp_Tablesets_ReceiptTableset[],
   vendorNum:number,
   purPoint:string,
   packSlip:string,
   packLine:number,
   taxCode:string,
   rateCode:string,
}

export interface GetNewRcvDtlTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
   */  
export interface GetNewRcvDtl_input{
   ds:Erp_Tablesets_ReceiptTableset[],
   vendorNum:number,
   purPoint:string,
   packSlip:string,
}

export interface GetNewRcvDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
   */  
export interface GetNewRcvDuty_input{
   ds:Erp_Tablesets_ReceiptTableset[],
   vendorNum:number,
   purPoint:string,
   packSlip:string,
   packLine:number,
}

export interface GetNewRcvDuty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
   */  
export interface GetNewRcvHeadAttch_input{
   ds:Erp_Tablesets_ReceiptTableset[],
   vendorNum:number,
   purPoint:string,
   packSlip:string,
}

export interface GetNewRcvHeadAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param taxCode
      @param rateCode
   */  
export interface GetNewRcvHeadTax_input{
   ds:Erp_Tablesets_ReceiptTableset[],
   vendorNum:number,
   purPoint:string,
   packSlip:string,
   taxCode:string,
   rateCode:string,
}

export interface GetNewRcvHeadTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param poNum
   */  
export interface GetNewRcvHeadWithPONum_input{
   ds:Erp_Tablesets_ReceiptTableset[],
   vendorNum:number,
   purPoint:string,
   poNum:number,
}

export interface GetNewRcvHeadWithPONum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
   */  
export interface GetNewRcvHead_input{
   ds:Erp_Tablesets_ReceiptTableset[],
   vendorNum:number,
   purPoint:string,
}

export interface GetNewRcvHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param miscSeq
      @param taxCode
      @param rateCode
   */  
export interface GetNewRcvMiscTax_input{
   ds:Erp_Tablesets_ReceiptTableset[],
   vendorNum:number,
   purPoint:string,
   packSlip:string,
   miscSeq:number,
   taxCode:string,
   rateCode:string,
}

export interface GetNewRcvMiscTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
   */  
export interface GetNewRcvMisc_input{
   ds:Erp_Tablesets_ReceiptTableset[],
   vendorNum:number,
   purPoint:string,
   packSlip:string,
}

export interface GetNewRcvMisc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
      @param poNum
      @param fromReceiptEntryNewRcpt
   */  
export interface GetPOInfo_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  Proposed Purchase Order Number  */  
   poNum:number,
      /**  Flag to indicate this was called from the ReceiptEntry, non-tracker mode  */  
   fromReceiptEntryNewRcpt:boolean,
}

export interface GetPOInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
   vendorNum:number,
   purPoint:string,
   warnMsg:string,
   poStatusWarnMsg:string,
}
}

   /** Required : 
      @param packSlip
      @param poNum
      @param vendorNum
   */  
export interface GetPartTranPKs_input{
      /**  The PackSlip number  */  
   packSlip:string,
      /**  The PO number  */  
   poNum:number,
      /**  The Vendor number  */  
   vendorNum:number,
}

export interface GetPartTranPKs_output{
parameters : {
      /**  output parameters  */  
   partTranPKs:string,
}
}

   /** Required : 
      @param partNum
   */  
export interface GetPartXRefInfo_input{
      /**  Proposed partNum value  */  
   partNum:string,
}

export interface GetPartXRefInfo_output{
parameters : {
      /**  output parameters  */  
   partNum:string,
   multipleMatch:boolean,
}
}

   /** Required : 
      @param ds
      @param inPONum
   */  
export interface GetPendingDtl_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  The PO number  */  
   inPONum:number,
}

export interface GetPendingDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
      @param purPoint
   */  
export interface GetPurPointInfo_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  Proposed Purchase Point value  */  
   purPoint:string,
}

export interface GetPurPointInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
   purPoint:string,
}
}

   /** Required : 
      @param company
      @param vendorNum
      @param purPoint
      @param packSlip
   */  
export interface GetRcvDtlLCIndCost_input{
   company:string,
   vendorNum:number,
   purPoint:string,
   packSlip:string,
}

export interface GetRcvDtlLCIndCost_output{
   returnObj:number,
}

   /** Required : 
      @param ds
      @param inContainerID
   */  
export interface GetReceiptDetailsFromContainer_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  Container ID to retrieve records for  */  
   inContainerID:number,
}

export interface GetReceiptDetailsFromContainer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param maxNumOfCards
   */  
export interface GetReceiptRelationshipMap_input{
   vendorNum:number,
   purPoint:string,
   packSlip:string,
   maxNumOfCards:number,
}

export interface GetReceiptRelationshipMap_output{
   returnObj:string,
}

   /** Required : 
      @param whereClauseRcvHead
      @param whereClauseRcvHeadAttch
      @param whereClauseRcvHeadTax
      @param whereClauseRcvDtl
      @param whereClauseRcvDtlAttch
      @param whereClauseRcvDtlAttrValueSet
      @param whereClauseRcvDtlTax
      @param whereClauseRcvDuty
      @param whereClauseRcvMisc
      @param whereClauseRcvMiscTax
      @param whereClauseLegalNumGenOpts
      @param whereClausePendingRcvDtl
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSNFormat
      @param whereClauseSupplierXRef
      @param vendorNum
      @param invoiceNum
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForAPInvoice_input{
   whereClauseRcvHead:string,
   whereClauseRcvHeadAttch:string,
   whereClauseRcvHeadTax:string,
   whereClauseRcvDtl:string,
   whereClauseRcvDtlAttch:string,
   whereClauseRcvDtlAttrValueSet:string,
   whereClauseRcvDtlTax:string,
   whereClauseRcvDuty:string,
   whereClauseRcvMisc:string,
   whereClauseRcvMiscTax:string,
   whereClauseLegalNumGenOpts:string,
   whereClausePendingRcvDtl:string,
   whereClauseSelectedSerialNumbers:string,
   whereClauseSNFormat:string,
   whereClauseSupplierXRef:string,
   vendorNum:number,
   invoiceNum:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsForAPInvoice_output{
   returnObj:Erp_Tablesets_ReceiptTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseRcvHead
      @param whereClauseRcvHeadAttch
      @param whereClauseRcvHeadTax
      @param whereClauseRcvDtl
      @param whereClauseRcvDtlAttch
      @param whereClauseRcvDtlAttrValueSet
      @param whereClauseRcvDtlTax
      @param whereClauseRcvDuty
      @param whereClauseRcvMisc
      @param whereClauseRcvMiscTax
      @param whereClauseLegalNumGenOpts
      @param whereClausePendingRcvDtl
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSNFormat
      @param whereClauseSupplierXRef
      @param poNum
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForPO_input{
   whereClauseRcvHead:string,
   whereClauseRcvHeadAttch:string,
   whereClauseRcvHeadTax:string,
   whereClauseRcvDtl:string,
   whereClauseRcvDtlAttch:string,
   whereClauseRcvDtlAttrValueSet:string,
   whereClauseRcvDtlTax:string,
   whereClauseRcvDuty:string,
   whereClauseRcvMisc:string,
   whereClauseRcvMiscTax:string,
   whereClauseLegalNumGenOpts:string,
   whereClausePendingRcvDtl:string,
   whereClauseSelectedSerialNumbers:string,
   whereClauseSNFormat:string,
   whereClauseSupplierXRef:string,
   poNum:number,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsForPO_output{
   returnObj:Erp_Tablesets_ReceiptTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseRcvHead
      @param whereClauseRcvHeadAttch
      @param whereClauseRcvHeadTax
      @param whereClauseRcvDtl
      @param whereClauseRcvDtlAttch
      @param whereClauseRcvDtlAttrValueSet
      @param whereClauseRcvDtlTax
      @param whereClauseRcvDuty
      @param whereClauseRcvMisc
      @param whereClauseRcvMiscTax
      @param whereClauseLegalNumGenOpts
      @param whereClausePendingRcvDtl
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSNFormat
      @param whereClauseSupplierXRef
      @param headNum
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForPayment_input{
   whereClauseRcvHead:string,
   whereClauseRcvHeadAttch:string,
   whereClauseRcvHeadTax:string,
   whereClauseRcvDtl:string,
   whereClauseRcvDtlAttch:string,
   whereClauseRcvDtlAttrValueSet:string,
   whereClauseRcvDtlTax:string,
   whereClauseRcvDuty:string,
   whereClauseRcvMisc:string,
   whereClauseRcvMiscTax:string,
   whereClauseLegalNumGenOpts:string,
   whereClausePendingRcvDtl:string,
   whereClauseSelectedSerialNumbers:string,
   whereClauseSNFormat:string,
   whereClauseSupplierXRef:string,
   headNum:number,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsForPayment_output{
   returnObj:Erp_Tablesets_ReceiptTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseRcvHead
      @param whereClauseRcvHeadAttch
      @param whereClauseRcvHeadTax
      @param whereClauseRcvDtl
      @param whereClauseRcvDtlAttch
      @param whereClauseRcvDtlAttrValueSet
      @param whereClauseRcvDtlTax
      @param whereClauseRcvDuty
      @param whereClauseRcvMisc
      @param whereClauseRcvMiscTax
      @param whereClauseLegalNumGenOpts
      @param whereClausePendingRcvDtl
      @param whereClauseSelectedSerialNumbers
      @param whereClauseSNFormat
      @param whereClauseSupplierXRef
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseRcvHead:string,
   whereClauseRcvHeadAttch:string,
   whereClauseRcvHeadTax:string,
   whereClauseRcvDtl:string,
   whereClauseRcvDtlAttch:string,
   whereClauseRcvDtlAttrValueSet:string,
   whereClauseRcvDtlTax:string,
   whereClauseRcvDuty:string,
   whereClauseRcvMisc:string,
   whereClauseRcvMiscTax:string,
   whereClauseLegalNumGenOpts:string,
   whereClausePendingRcvDtl:string,
   whereClauseSelectedSerialNumbers:string,
   whereClauseSNFormat:string,
   whereClauseSupplierXRef:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ReceiptTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param isReceived
      @param receivedToVal
   */  
export interface GetSNStatus_input{
   isReceived:boolean,
   receivedToVal:string,
}

export interface GetSNStatus_output{
   returnObj:string,
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
      @param ipJobNum
      @param ipAsmSeq
      @param ipSubOprSeq
      @param ipReceivedTo
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
   ipJobNum:string,
   ipAsmSeq:number,
   ipSubOprSeq:number,
   ipReceivedTo:string,
}

export interface GetSelectSerialNumbersParams_output{
   returnObj:Erp_Tablesets_SelectSerialNumbersParamsTableset[],
}

   /** Required : 
      @param ds
      @param vendorID
   */  
export interface GetVendorInfo_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  Proposed Vendor ID value  */  
   vendorID:string,
}

export interface GetVendorInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
   vendorNum:number,
   purPoint:string,
}
}

   /** Required : 
      @param poNum
   */  
export interface GetWarningPOClosed_input{
      /**  PO Number  */  
   poNum:number,
}

export interface GetWarningPOClosed_output{
parameters : {
      /**  output parameters  */  
   cWarning:string,
}
}

   /** Required : 
      @param piPONum
      @param pcPackSlip
   */  
export interface HHCanEditPackSlip_input{
      /**  A valid PONumber  */  
   piPONum:number,
      /**  Packing slip to check if this one was received  */  
   pcPackSlip:string,
}

export interface HHCanEditPackSlip_output{
parameters : {
      /**  output parameters  */  
   pbIsEdit:boolean,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param poLine
   */  
export interface HHOnChangeDtlPOLine_input{
   ds:Erp_Tablesets_ReceiptTableset[],
   vendorNum:number,
   purPoint:string,
   packSlip:string,
   packLine:number,
   poLine:number,
}

export interface HHOnChangeDtlPOLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param poRelNum
   */  
export interface HHOnChangeDtlPORelNum_input{
   ds:Erp_Tablesets_ReceiptTableset[],
   vendorNum:number,
   purPoint:string,
   packSlip:string,
   packLine:number,
   poRelNum:number,
}

export interface HHOnChangeDtlPORelNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param partNum
      @param sysRowID
      @param rowType
   */  
export interface HHOnChangeDtlPartNum_input{
   ds:Erp_Tablesets_ReceiptTableset[],
   vendorNum:number,
   purPoint:string,
   packSlip:string,
   packLine:number,
   partNum:string,
   sysRowID:string,
   rowType:string,
}

export interface HHOnChangeDtlPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
   partNum:string,
   multipleMatch:boolean,
}
}

   /** Required : 
      @param partNum
      @param lotNum
   */  
export interface HHValRecDocReq_input{
      /**  Part number  */  
   partNum:string,
      /**  Part Lot number  */  
   lotNum:string,
}

export interface HHValRecDocReq_output{
parameters : {
      /**  output parameters  */  
   infoMsg:string,
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
      @param intQueId
      @param checkForManualPrompt
      @param ds
   */  
export interface ImportReceipt_input{
      /**  Unique key of IMRcvHead  */  
   intQueId:number,
      /**  If true then Get Legal Number defaults and check if Generate Type is manual and set RequiresUserInput appropriately, otherwise just generate Legal Number  */  
   checkForManualPrompt:boolean,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface ImportReceipt_output{
parameters : {
      /**  output parameters  */  
   vendorNum:number,
   purPoint:string,
   packSlip:string,
   requiresUserInput:boolean,
   legalNumMsg:string,
   closedPOWarningMsg:string,
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
   */  
export interface InitializeLandedCost_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
}

export interface InitializeLandedCost_output{
   returnObj:Erp_Tablesets_MassReceiptTableset[],
parameters : {
      /**  output parameters  */  
   lcComment:string,
   lcReference:string,
}
}

   /** Required : 
      @param inContainerID
   */  
export interface IsContainerReceived_input{
   inContainerID:number,
}

export interface IsContainerReceived_output{
   returnObj:boolean,
}

   /** Required : 
      @param ds
      @param packSlip
      @param packLine
   */  
export interface LCChangeLCAmt_input{
   ds:Erp_Tablesets_MassReceiptTableset[],
      /**  Receipt Pack Number  */  
   packSlip:string,
      /**  Receipt Line Number  */  
   packLine:number,
}

export interface LCChangeLCAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MassReceiptTableset,
}
}

   /** Required : 
      @param PCIDSGenerated
      @param pkgControlOutboundContainer
      @param ds
   */  
export interface MassReceiptsGeneratePCIDUpdate_input{
   PCIDSGenerated:string,
   pkgControlOutboundContainer:boolean,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface MassReceiptsGeneratePCIDUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
      @param ipCompany
      @param ipContainerID
      @param ipNewArrivedDate
      @param ipOldArrivedDate
   */  
export interface OnChangeContainerHdrArrivedDate_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  Container Company  */  
   ipCompany:string,
      /**  ContainerID  */  
   ipContainerID:number,
      /**  Proposed arrived date to be validated  */  
   ipNewArrivedDate:string,
      /**  Previous arrived date  */  
   ipOldArrivedDate:string,
}

export interface OnChangeContainerHdrArrivedDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
   opNeedsRecalc:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeContainerImportFld_input{
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeContainerImportFld_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param newBinNum
      @param requiresUserInput
      @param ds
   */  
export interface OnChangeDtlBinNum_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  New BinNum code to check  */  
   newBinNum:string,
      /**  Set to True if question / warnings are to be returned  */  
   requiresUserInput:boolean,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeDtlBinNum_output{
parameters : {
      /**  output parameters  */  
   questionMsg:string,
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param ipCommCode
      @param ds
   */  
export interface OnChangeDtlCommodity_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  Proposed Commodity Code to be validated  */  
   ipCommCode:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeDtlCommodity_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param ipCountryNum
      @param ds
   */  
export interface OnChangeDtlCountryNum_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  Proposed Country of Origin to be validated  */  
   ipCountryNum:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeDtlCountryNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param ipLCIndCost
      @param LCIndCostSum
      @param ds
   */  
export interface OnChangeDtlLCIndCost_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  Proposed LC Indirect Cose to be validated  */  
   ipLCIndCost:number,
      /**  Total amount of Indirect cost on all the lines  */  
   LCIndCostSum:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeDtlLCIndCost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param pcid
      @param requiresUserInput
      @param selectedSerialNumberCount
      @param serialNumber
      @param ds
   */  
export interface OnChangeDtlPCID_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  PCID  */  
   pcid:string,
      /**  Set to True if question / warnings are to be returned  */  
   requiresUserInput:boolean,
      /**  Count of selected serial numbers if tracked used for validation  */  
   selectedSerialNumberCount:number,
      /**  First Serial Number if tracked used for validation  */  
   serialNumber:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeDtlPCID_output{
parameters : {
      /**  output parameters  */  
   questionMsg:string,
   warnMsg:string,
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
      @param poNum
   */  
export interface OnChangeDtlPOSelected_input{
   ds:Erp_Tablesets_ReceiptTableset[],
   poNum:number,
}

export interface OnChangeDtlPOSelected_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
   poStatusQstnMsg:string,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param receiptType
      @param tranType
      @param ds
   */  
export interface OnChangeDtlReceiptTypeTranType_input{
   vendorNum:number,
   purPoint:string,
   packSlip:string,
   packLine:number,
   receiptType:string,
   tranType:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeDtlReceiptTypeTranType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param receiptType
      @param ds
   */  
export interface OnChangeDtlReceiptType_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  Receipt Type  */  
   receiptType:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeDtlReceiptType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param ipReceived
      @param ds
   */  
export interface OnChangeDtlReceived_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  Received flag  */  
   ipReceived:boolean,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeDtlReceived_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param poNum
   */  
export interface OnChangeDtlSelectedSinglePO_input{
   poNum:number,
}

export interface OnChangeDtlSelectedSinglePO_output{
parameters : {
      /**  output parameters  */  
   poStatusQstnMsg:string,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
   */  
export interface OnChangeDtlSupplierPrice_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
}

export interface OnChangeDtlSupplierPrice_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param taxCatID
      @param ds
   */  
export interface OnChangeDtlTaxCatID_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  Tax Category  */  
   taxCatID:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeDtlTaxCatID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param taxExempt
      @param ds
   */  
export interface OnChangeDtlTaxExempt_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  Tax Exempt  */  
   taxExempt:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeDtlTaxExempt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param ipUpliftPercent
      @param ds
   */  
export interface OnChangeDtlUpliftPercent_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  Proposed Uplift Percentage to be validated  */  
   ipUpliftPercent:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeDtlUpliftPercent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param newWareHouseCode
      @param requiresUserInput
      @param ds
   */  
export interface OnChangeDtlWareHouseCode_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  New warehouse code to check  */  
   newWareHouseCode:string,
      /**  Set to True if question / warnings are to be returned  */  
   requiresUserInput:boolean,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeDtlWareHouseCode_output{
parameters : {
      /**  output parameters  */  
   questionMsg:string,
   warnMsg:string,
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param dutySeq
      @param ipTariffCode
      @param ds
   */  
export interface OnChangeDutyTariffCode_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  Receipt Duty Sequence  */  
   dutySeq:number,
      /**  Proposed Tariff Code to be validated  */  
   ipTariffCode:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeDutyTariffCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param ipReceived
      @param ds
   */  
export interface OnChangeHdrReceived_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Received flag  */  
   ipReceived:boolean,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeHdrReceived_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param newTaxRegionCode
      @param ds
   */  
export interface OnChangeHdrTaxRegionCode_input{
   newTaxRegionCode:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeHdrTaxRegionCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param proposedFixedAmt
      @param ds
   */  
export interface OnChangeHeaderTaxFixedAmount_input{
      /**  The proposed fixed amount  */  
   proposedFixedAmt:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeHeaderTaxFixedAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param proposedRateCode
      @param ds
   */  
export interface OnChangeHeaderTaxRateCodeMaster_input{
      /**  The proposed rate code  */  
   proposedRateCode:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeHeaderTaxRateCodeMaster_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeHeaderTaxRateCode_input{
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeHeaderTaxRateCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param proposedReportableAmt
      @param ds
   */  
export interface OnChangeHeaderTaxReportableAmt_input{
      /**  The proposed reportable amount  */  
   proposedReportableAmt:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeHeaderTaxReportableAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param proposedTaxAmt
      @param ds
   */  
export interface OnChangeHeaderTaxTaxAmt_input{
      /**  The proposed tax amount  */  
   proposedTaxAmt:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeHeaderTaxTaxAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param proposedTaxCode
      @param ds
   */  
export interface OnChangeHeaderTaxTaxCode_input{
      /**  The proposed tax code  */  
   proposedTaxCode:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeHeaderTaxTaxCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param proposedTaxDeductable
      @param ds
   */  
export interface OnChangeHeaderTaxTaxDeductable_input{
      /**  The proposed tax deductable  */  
   proposedTaxDeductable:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeHeaderTaxTaxDeductable_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param proposedTaxPercent
      @param ds
   */  
export interface OnChangeHeaderTaxTaxPercent_input{
      /**  The proposed tax percent  */  
   proposedTaxPercent:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeHeaderTaxTaxPercent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param proposedTaxableAmt
      @param ds
   */  
export interface OnChangeHeaderTaxTaxableAmt_input{
      /**  The proposed taxable amount  */  
   proposedTaxableAmt:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeHeaderTaxTaxableAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
   */  
export interface OnChangeInspReq_input{
   ds:Erp_Tablesets_ReceiptTableset[],
      /**  Vendor Number  */  
   vendorNum:number,
      /**  Purchase Point  */  
   purPoint:string,
      /**  Packing slip number  */  
   packSlip:string,
      /**  Receipt Line  */  
   packLine:number,
}

export interface OnChangeInspReq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param miscSeq
      @param ipApplyDate
      @param ds
   */  
export interface OnChangeMiscApplyDate_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Indirect Cost Sequence  */  
   miscSeq:number,
      /**  Proposed Apply Date to be validated  */  
   ipApplyDate:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeMiscApplyDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param miscSeq
      @param ipChargeID
      @param ds
   */  
export interface OnChangeMiscCharge_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Indirect Cost Sequence  */  
   miscSeq:number,
      /**  Proposed PurMisc ID to be validated  */  
   ipChargeID:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeMiscCharge_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param miscSeq
      @param ipCurrCode
      @param ds
   */  
export interface OnChangeMiscCurrencyCode_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Indirect Cost Sequence  */  
   miscSeq:number,
      /**  Proposed Currency Code to be validated  */  
   ipCurrCode:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeMiscCurrencyCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param miscSeq
      @param ipDocActualAmt
      @param ds
   */  
export interface OnChangeMiscDocActualAmt_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Indirect Cost Sequence  */  
   miscSeq:number,
      /**  Proposed Actual Amount in document currency  */  
   ipDocActualAmt:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeMiscDocActualAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param miscSeq
      @param ipExchangeRate
      @param ds
   */  
export interface OnChangeMiscExchangeRate_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Indirect Cost Sequence  */  
   miscSeq:number,
      /**  Proposed Currency Exchange Rate to be validated  */  
   ipExchangeRate:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeMiscExchangeRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param miscSeq
      @param ipInvLine
      @param ds
   */  
export interface OnChangeMiscInvoiceLine_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Indirect Cost Sequence  */  
   miscSeq:number,
      /**  The AP Invoice Line to be validated  */  
   ipInvLine:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeMiscInvoiceLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param miscSeq
      @param ipInvNum
      @param ds
   */  
export interface OnChangeMiscInvoiceNum_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Indirect Cost Sequence  */  
   miscSeq:number,
      /**  The AP Invoice Number to be validated  */  
   ipInvNum:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeMiscInvoiceNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param miscSeq
      @param ipMscNum
      @param ds
   */  
export interface OnChangeMiscMscNum_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Indirect Cost Sequence  */  
   miscSeq:number,
      /**  The AP Invoice Line Miscellaneous Sequence Number to be validated  */  
   ipMscNum:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeMiscMscNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param miscSeq
      @param ipPercent
      @param ds
   */  
export interface OnChangeMiscPercent_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Indirect Cost Sequence  */  
   miscSeq:number,
      /**  Proposed Actual Amount in document currency  */  
   ipPercent:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeMiscPercent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param miscSeq
      @param ipRateGrpCode
      @param ds
   */  
export interface OnChangeMiscRateGrp_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Indirect Cost Sequence  */  
   miscSeq:number,
      /**  Proposed Currency Rate Group Code to be validated  */  
   ipRateGrpCode:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeMiscRateGrp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param miscSeq
      @param taxCatID
      @param ds
   */  
export interface OnChangeMiscTaxCatID_input{
   vendorNum:number,
   purPoint:string,
   packSlip:string,
   miscSeq:number,
   taxCatID:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeMiscTaxCatID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param miscSeq
      @param vendID
      @param ds
   */  
export interface OnChangeMiscVendor_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Indirect Cost Sequence  */  
   miscSeq:number,
      /**  Proposed vendor ID to be validated  */  
   vendID:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeMiscVendor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param received
      @param partNum
      @param rcvDate
      @param ds
   */  
export interface OnChangeReceiptDate_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
      /**  If the POLine or the Pack Slip has been receipt or not  */  
   received:boolean,
      /**  Set to True if question / warnings are to be returned  */  
   partNum:string,
      /**  Receipt Date.  */  
   rcvDate:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeReceiptDate_output{
parameters : {
      /**  output parameters  */  
   wrnLines:string,
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangeRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param tableName
      @param proposedTaxDeductable
      @param ds
   */  
export interface OnChangeTaxDeductable_input{
      /**  Table Name RcvMiscTax or RcvDtlTax  */  
   tableName:string,
      /**  The proposed tax deductible  */  
   proposedTaxDeductable:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeTaxDeductable_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param tableName
      @param proposedFixedAmt
      @param ds
   */  
export interface OnChangeTaxFixedAmount_input{
      /**  Table Name RcvMiscTax or RcvDtlTax  */  
   tableName:string,
      /**  The proposed reportable amount  */  
   proposedFixedAmt:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeTaxFixedAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param tableName
      @param proposedTaxPercent
      @param ds
   */  
export interface OnChangeTaxPercent_input{
      /**  Table Name RcvMiscTax or RcvDtlTax  */  
   tableName:string,
      /**  The proposed tax percent  */  
   proposedTaxPercent:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeTaxPercent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param tableName
      @param proposedRateCode
      @param ds
   */  
export interface OnChangeTaxRateCode_input{
      /**  Table Name RcvMiscTax or RcvDtlTax  */  
   tableName:string,
      /**  The proposed rate code  */  
   proposedRateCode:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeTaxRateCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param tableName
      @param proposedReportableAmt
      @param ds
   */  
export interface OnChangeTaxReportableAmt_input{
      /**  Table Name RcvMiscTax or RcvDtlTax  */  
   tableName:string,
      /**  The proposed reportable amount  */  
   proposedReportableAmt:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeTaxReportableAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param tableName
      @param proposedTaxAmt
      @param ds
   */  
export interface OnChangeTaxTaxAmt_input{
      /**  Table Name RcvMiscTax or RcvDtlTax  */  
   tableName:string,
      /**  The proposed tax amount  */  
   proposedTaxAmt:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeTaxTaxAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param tableName
      @param proposedTaxCode
      @param ds
   */  
export interface OnChangeTaxTaxCode_input{
      /**  Table Name RcvMiscTax or RcvDtlTax  */  
   tableName:string,
      /**  The proposed tax code  */  
   proposedTaxCode:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeTaxTaxCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param tableName
      @param proposedTaxableAmt
      @param ds
   */  
export interface OnChangeTaxTaxableAmt_input{
      /**  Table Name RcvMiscTax or RcvDtlTax  */  
   tableName:string,
      /**  The proposed taxable amount  */  
   proposedTaxableAmt:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangeTaxTaxableAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param ds
   */  
export interface OnChangedDtlPOTransValue_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Line to check  */  
   packLine:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangedDtlPOTransValue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangedHeaderTaxManual_input{
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangedHeaderTaxManual_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param tableName
      @param ds
   */  
export interface OnChangedTaxManual_input{
      /**  Table Name RcvMiscTax or RcvDtlTax  */  
   tableName:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface OnChangedTaxManual_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param inContainerID
   */  
export interface PreReceiveContainer_input{
   inContainerID:number,
}

export interface PreReceiveContainer_output{
}

   /** Required : 
      @param ds
   */  
export interface PreUpdate_input{
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface PreUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
   RequiresUserInput:boolean,
}
}

   /** Required : 
      @param pintQueId
      @param curpackSlip
      @param ds
   */  
export interface ProcessIM_input{
      /**  A valid IntQueId  */  
   pintQueId:number,
      /**  Packing slip number  */  
   curpackSlip:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface ProcessIM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
   */  
export interface ProcessLandedCosts_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  Receipt Packing Number  */  
   packSlip:string,
}

export interface ProcessLandedCosts_output{
   returnObj:Erp_Tablesets_ReceiptTableset[],
}

   /** Required : 
      @param company
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
   */  
export interface RcvDtlNegInvCheck_input{
      /**  Company  */  
   company:string,
      /**  Vendor Num  */  
   vendorNum:number,
      /**  Purchase Point  */  
   purPoint:string,
      /**  Packing Slip Num  */  
   packSlip:string,
      /**  Packing Slip Line  */  
   packLine:number,
}

export interface RcvDtlNegInvCheck_output{
parameters : {
      /**  output parameters  */  
   negQtyAction:string,
   msg:string,
}
}

   /** Required : 
      @param company
      @param vendorNum
      @param purPoint
      @param packSlip
   */  
export interface RcvHeadNegInvCheck_input{
      /**  Company  */  
   company:string,
      /**  Vendor Num  */  
   vendorNum:number,
      /**  Purchase Point  */  
   purPoint:string,
      /**  Packing Slip Num  */  
   packSlip:string,
}

export interface RcvHeadNegInvCheck_output{
parameters : {
      /**  output parameters  */  
   negQtyAction:string,
   msg:string,
}
}

   /** Required : 
      @param ipReceived
      @param ds
   */  
export interface ReceiveAllLines_input{
      /**  Received flag  */  
   ipReceived:boolean,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface ReceiveAllLines_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ReceiveAll_input{
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface ReceiveAll_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
      @param inContainerID
      @param ipArrivedDate
      @param inCreateNewPoRels
   */  
export interface ReceiveContainerUpdateUsingArriveDate_input{
   ds:Erp_Tablesets_ReceiptTableset[],
   inContainerID:number,
      /**  Arrived Date  */  
   ipArrivedDate:string,
   inCreateNewPoRels:string,
}

export interface ReceiveContainerUpdateUsingArriveDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
   outEshReceived:boolean,
   outPartialReceipt:boolean,
   outReceiveAll:boolean,
}
}

   /** Required : 
      @param ds
      @param inContainerID
      @param inCreateNewPoRels
   */  
export interface ReceiveContainerUpdate_input{
   ds:Erp_Tablesets_ReceiptTableset[],
   inContainerID:number,
   inCreateNewPoRels:string,
}

export interface ReceiveContainerUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
   outEshReceived:boolean,
   outPartialReceipt:boolean,
   outReceiveAll:boolean,
}
}

   /** Required : 
      @param ds
      @param inContainerID
      @param ipArrivedDate
   */  
export interface ReceiveContainerUsingArrivedDate_input{
   ds:Erp_Tablesets_ReceiptTableset[],
   inContainerID:number,
   ipArrivedDate:string,
}

export interface ReceiveContainerUsingArrivedDate_output{
   returnObj:Erp_Tablesets_ContainerTrackingTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
      @param inContainerID
   */  
export interface ReceiveContainer_input{
   ds:Erp_Tablesets_ReceiptTableset[],
   inContainerID:number,
}

export interface ReceiveContainer_output{
   returnObj:Erp_Tablesets_ContainerTrackingTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ipVendorNum
      @param ipPurPoint
      @param ipPackSlip
      @param ipDisburseMethod
   */  
export interface ResetLandedCostDisbursements_input{
      /**  Vendor Number to reset  */  
   ipVendorNum:number,
      /**  Purchase Point to reset  */  
   ipPurPoint:string,
      /**  Packing Slip Number to reset  */  
   ipPackSlip:string,
      /**  Landed Cost Disbursment method  */  
   ipDisburseMethod:string,
}

export interface ResetLandedCostDisbursements_output{
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param ds
   */  
export interface SetPrimaryBin_input{
      /**  Vendor Number  */  
   vendorNum:number,
      /**  Purchase Point Number  */  
   purPoint:string,
      /**  Receipt Packing Slip Number  */  
   packSlip:string,
      /**  Receipt Line number  */  
   packLine:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface SetPrimaryBin_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param ds
   */  
export interface SetToLocation_input{
      /**  Vendor Number  */  
   vendorNum:number,
      /**  Purchase Point Number  */  
   purPoint:string,
      /**  Receipt Packing Slip Number  */  
   packSlip:string,
      /**  Receipt Line number  */  
   packLine:number,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface SetToLocation_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtReceiptTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtReceiptTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param RunChkLCAmtBeforeUpdate
      @param RunChkHdrBeforeUpdate
      @param ipVendorNum
      @param ipPurPoint
      @param ipPackSlip
      @param ipPackLine
      @param lRunChkDtl
      @param lRunChkDtlCompliance
      @param lRunCheckCompliance
      @param lRunPreUpdate
      @param lRunCreatePartLot
      @param partNum
      @param lotNum
      @param lOkToUpdate
      @param ds
   */  
export interface UpdateMaster_input{
      /**  bool to determine whether to run certain code segment  */  
   RunChkLCAmtBeforeUpdate:boolean,
      /**  bool to determine whether to run certain code segment  */  
   RunChkHdrBeforeUpdate:boolean,
      /**  current vendor number  */  
   ipVendorNum:number,
      /**  current PurPoint  */  
   ipPurPoint:string,
      /**  current packSlip  */  
   ipPackSlip:string,
      /**  current packLine  */  
   ipPackLine:number,
      /**  bool to determine whether to run certain code segment  */  
   lRunChkDtl:boolean,
      /**  bool to determine whether to run certain code segment  */  
   lRunChkDtlCompliance:boolean,
      /**  bool to determine whether to run certain code segment  */  
   lRunCheckCompliance:boolean,
      /**  bool to determine whether to run certain code segment  */  
   lRunPreUpdate:boolean,
      /**  bool to determine whether to run certain code segment  */  
   lRunCreatePartLot:boolean,
      /**  current partNum  */  
   partNum:string,
      /**  current lotNum  */  
   lotNum:string,
      /**  bool to determine if the Update should be run in this process  */  
   lOkToUpdate:boolean,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface UpdateMaster_output{
parameters : {
      /**  output parameters  */  
   cLCAmtMessage:string,
   opUpliftWarnMsg:string,
   opReceiptWarnMsg:string,
   opArriveWarnMsg:string,
   qMessageStr:string,
   sMessageStr:string,
   lcMessageStr:string,
   pcMessageStr:string,
   qDtlComplianceMsgStr:string,
   lCompliant:boolean,
   lRequiresUserInput:boolean,
   lUpdateWasRun:boolean,
   wrnLines:string,
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateOurQtyFromAttributes_input{
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface UpdateOurQtyFromAttributes_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param poNum
      @param vendorNum
   */  
export interface ValidateMRPONum_input{
      /**  The PO Number to validate  */  
   poNum:number,
      /**  The Receipt Header Vendor's Number  */  
   vendorNum:number,
}

export interface ValidateMRPONum_output{
parameters : {
      /**  output parameters  */  
   errorMsg:string,
}
}

   /** Required : 
      @param poNum
   */  
export interface ValidatePONum_input{
      /**  The PO Number to validate  */  
   poNum:number,
}

export interface ValidatePONum_output{
   returnObj:boolean,
}

   /** Required : 
      @param tableName
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
   */  
export interface ValidateReceiptRecords_input{
   tableName:string,
   vendorNum:number,
   purPoint:string,
   packSlip:string,
   packLine:number,
}

export interface ValidateReceiptRecords_output{
   returnObj:boolean,
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param poNum
      @param packSlip
      @param partNum
   */  
export interface ValidateSMIReceiptAttrPart_input{
      /**  Receipt Vendor Number  */  
   vendorNum:number,
      /**  Receipt Purchase Point  */  
   purPoint:string,
      /**  PO Number for Purchase Order Receipts  */  
   poNum:number,
      /**  Receipt Packing Number  */  
   packSlip:string,
      /**  Receipt Part Number  */  
   partNum:string,
}

export interface ValidateSMIReceiptAttrPart_output{
}

   /** Required : 
      @param ipPartNum
      @param ipAttributeSetID
      @param ipSerialNo
      @param ipVendorNum
      @param ipJobNum
      @param ipAsmSeq
      @param ipSubOprSeq
      @param ipPackSlip
      @param ipPackLine
      @param ipReceivedTo
      @param ipJobSeqType
   */  
export interface ValidateSN_input{
   ipPartNum:string,
   ipAttributeSetID:number,
   ipSerialNo:string,
   ipVendorNum:number,
   ipJobNum:string,
   ipAsmSeq:number,
   ipSubOprSeq:number,
   ipPackSlip:string,
   ipPackLine:number,
   ipReceivedTo:string,
   ipJobSeqType:string,
}

export interface ValidateSN_output{
parameters : {
      /**  output parameters  */  
   warningMsg:string,
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param voidReason
      @param ds
   */  
export interface VoidLegalNumber_input{
      /**  Vendor Number  */  
   vendorNum:number,
      /**  Purchase Point  */  
   purPoint:string,
      /**  Packing Slip  */  
   packSlip:string,
      /**  The void reason text  */  
   voidReason:string,
   ds:Erp_Tablesets_ReceiptTableset[],
}

export interface VoidLegalNumber_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptTableset,
}
}

   /** Required : 
      @param ipPONum
      @param ipPOLine
      @param ipPORelNum
      @param ipPackSlip
      @param ipPackLine
   */  
export interface chkUnReceive_input{
   ipPONum:number,
   ipPOLine:number,
   ipPORelNum:number,
   ipPackSlip:string,
   ipPackLine:number,
}

export interface chkUnReceive_output{
   returnObj:boolean,
}

